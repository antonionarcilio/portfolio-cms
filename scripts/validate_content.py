#!/usr/bin/env python3
"""Pre-commit validation for portfolio-cms content structure.

Validation rules (all checked against staged files only):
  1. Only known content types exist under content/
  2. Entry folder names are lowercase kebab-case
  3. Only index.md / index.en.md inside entry folders
  4. Every index.md has a counterpart index.en.md (and vice versa)
  5. YAML frontmatter is valid and required fields are present
  6. Wikilink targets correspond to existing tracked files

Exit code 0 = valid, 1 = invalid.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "Error: PyYAML is required. Install with: pip install pyyaml",
        file=sys.stderr,
    )
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "scripts" / "content-schema.yaml"

FLAT_TYPES = {"about"}
INDEX_RE = re.compile(r"^index(\.en)?\.md$")
KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")

errors: list[str] = []


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_schema() -> dict:
    with open(SCHEMA_PATH) as f:
        return yaml.safe_load(f)


def get_staged_files() -> set[str]:
    """Return relative paths of staged files (added / copied / modified / renamed)."""
    result = subprocess.run(
        [
            "git", "diff", "--cached", "--name-only",
            "--diff-filter=ACMR",
        ],
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        print("Error: git diff --cached failed", file=sys.stderr)
        sys.exit(1)
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def get_all_content_files() -> set[str]:
    """Return all tracked files under content/ via the git index."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "content/"],
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        print("Error: git ls-files failed", file=sys.stderr)
        sys.exit(1)
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def classify_path(rel_path: str):
    """Return (content_type, entry_key, locale) or None if path is not a content entry.

    entry_key is:
      - None for root entries
      - str for simple entry types (e.g. "hello-world")
      - (str, str) tuple for project entries (company, project_name)
    """
    parts = Path(rel_path).parts
    n = len(parts)

    if not rel_path.startswith("content/"):
        return None

    # Root index files
    if n == 2 and parts[0] == "content" and INDEX_RE.match(parts[-1]):
        return ("root", None, "en" if ".en." in parts[-1] else "pt")

    if n < 3 or parts[0] != "content":
        return None

    content_type = parts[1]
    locale = "en" if ".en." in parts[-1] else "pt"

    if not INDEX_RE.match(parts[-1]):
        return None

    # Flat type: content/<type>/index.md (e.g. content/about/index.md)
    if n == 3 and content_type in FLAT_TYPES:
        return (content_type, content_type, locale)

    # Project: content/project/<company>/<project>/index.md
    if content_type == "project":
        if n < 5:
            return None
        return ("project", (parts[2], parts[3]), locale)

    # Other entry types: content/<type>/<entry>/index.md
    if n < 4:
        return None
    return (content_type, parts[2], locale)


def resolve_wikilink_target(target: str) -> str:
    """Normalise a wikilink target to a repo-relative file path."""
    target = target.split("|")[0].strip()
    if not target.endswith(".md"):
        target += ".md"
    return target


# ---------------------------------------------------------------------------
# Validation rules
# ---------------------------------------------------------------------------

def validate_structure(rel_path: str, schema: dict) -> None:
    """Rule 1-3: known types, kebab-case, no extra files."""
    parts = Path(rel_path).parts
    n = len(parts)
    allowed = set(schema["allowed_types"])

    if parts[0] != "content":
        return

    # Root level
    if n == 2:
        if INDEX_RE.match(parts[-1]):
            return
        if parts[1] in allowed:
            return
        errors.append(
            f"{rel_path}: only index.md, index.en.md and known content "
            f"type dirs are allowed at content/ root"
        )
        return

    content_type = parts[1]
    if content_type not in allowed:
        errors.append(
            f"{rel_path}: unknown content type '{content_type}'. "
            f"Allowed: {', '.join(sorted(allowed))}"
        )
        return

    filename = parts[-1]

    # Flat type (e.g. about)
    if content_type in FLAT_TYPES:
        if n == 3 and INDEX_RE.match(filename):
            return
        errors.append(
            f"{rel_path}: content/{content_type}/ may only contain "
            f"index.md and index.en.md (no subdirectories or extra files)"
        )
        return

    # Entry types require content/<type>/<entry>/...
    if n < 4:
        errors.append(
            f"{rel_path}: unexpected file at content/{content_type}/ level"
        )
        return

    # Project nested structure
    if content_type == "project":
        if n < 5:
            errors.append(
                f"{rel_path}: project paths must be "
                f"content/project/<company>/<project>/index.md"
            )
            return
        company, proj = parts[2], parts[3]
        if not KEBAB_RE.match(company):
            errors.append(
                f"{rel_path}: company folder '{company}' must be "
                f"lowercase kebab-case"
            )
        if not KEBAB_RE.match(proj):
            errors.append(
                f"{rel_path}: project folder '{proj}' must be "
                f"lowercase kebab-case"
            )
    else:
        entry = parts[2]
        if not KEBAB_RE.match(entry):
            errors.append(
                f"{rel_path}: entry folder '{entry}' must be "
                f"lowercase kebab-case"
            )

    # Only index.md / index.en.md inside entry folders
    if not INDEX_RE.match(filename):
        errors.append(
            f"{rel_path}: only index.md and index.en.md are allowed "
            f"inside entry folders"
        )


def validate_bilingual(rel_path: str, staged: set[str]) -> None:
    """Rule 4: every index.md needs its index.en.md counterpart and vice versa."""
    p = Path(rel_path)
    if not INDEX_RE.match(p.name):
        return

    parts = p.parts
    # Root index
    if len(parts) == 2 and parts[0] == "content":
        counterpart = str(p.parent / ("index.md" if p.name == "index.en.md" else "index.en.md"))
        if counterpart not in staged and not (REPO_ROOT / counterpart).exists():
            errors.append(
                f"{rel_path}: missing counterpart '{counterpart}'"
            )
        return

    counterpart = str(p.parent / ("index.md" if p.name == "index.en.md" else "index.en.md"))
    if counterpart not in staged and not (REPO_ROOT / counterpart).exists():
        errors.append(
            f"{rel_path}: missing counterpart '{counterpart}'. "
            f"Every entry must have both index.md and index.en.md"
        )


def validate_frontmatter(rel_path: str, schema: dict, all_files: set[str]) -> None:
    """Rule 5-6: parse YAML, check required fields, validate wikilinks."""
    cls = classify_path(rel_path)
    if cls is None:
        return

    content_type, entry_key, locale = cls
    file_path = REPO_ROOT / rel_path

    if not file_path.is_file():
        return  # Deleted or not present on disk – nothing to parse

    raw = file_path.read_text(encoding="utf-8")

    if not raw.startswith("---"):
        errors.append(f"{rel_path}: missing YAML frontmatter (must start with '---')")
        return

    end = raw.find("---", 3)
    if end == -1:
        errors.append(f"{rel_path}: YAML frontmatter has no closing '---'")
        return

    yaml_text = raw[3:end].strip()
    try:
        fm = yaml.safe_load(yaml_text)
    except yaml.YAMLError as exc:
        errors.append(f"{rel_path}: invalid YAML frontmatter: {exc}")
        return

    if not isinstance(fm, dict):
        errors.append(f"{rel_path}: frontmatter must be a key-value mapping")
        return

    # Required fields (exact name match required — no aliases)
    required = schema.get("fields", {}).get(content_type, {}).get("required", [])
    for field in required:
        val = fm.get(field)
        if val is None:
            errors.append(
                f"{rel_path}: missing required field '{field}' "
                f"for content type '{content_type}'"
            )
        elif isinstance(val, (list, str)) and len(str(val).strip()) == 0:
            errors.append(
                f"{rel_path}: field '{field}' is required but empty "
                f"for content type '{content_type}'"
            )

    # Wikilink validation
    for field_name, field_value in fm.items():
        links = _extract_wikilinks(field_value)
        for target in links:
            resolved = resolve_wikilink_target(target)
            if resolved not in all_files:
                errors.append(
                    f"{rel_path}: field '{field_name}' wikilink "
                    f"target '{target}' does not exist "
                    f"(expected '{resolved}' in repository)"
                )


def _extract_wikilinks(value):
    """Recursively extract wikilink targets from a frontmatter value."""
    links = []
    if isinstance(value, str):
        links.extend(WIKILINK_RE.findall(value))
    elif isinstance(value, list):
        for item in value:
            links.extend(_extract_wikilinks(item))
    elif isinstance(value, dict):
        for item in value.values():
            links.extend(_extract_wikilinks(item))
    return links


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    schema = load_schema()
    staged = get_staged_files()
    all_files = get_all_content_files()

    content_staged = {f for f in staged if f.startswith("content/")}

    for rel_path in sorted(content_staged):
        validate_structure(rel_path, schema)
        validate_bilingual(rel_path, content_staged)
        if rel_path.endswith(".md"):
            validate_frontmatter(rel_path, schema, all_files)

    if errors:
        print(
            f"\n❌ Content validation failed ({len(errors)} error(s)):\n",
            file=sys.stderr,
        )
        for err in errors:
            print(f"  • {err}", file=sys.stderr)
        print(
            "\n"
            "📖 If you are intentionally changing the schema (new fields, "
            "new content types,\n"
            "   removing fields), edit scripts/content-schema.yaml and "
            "commit it together\n"
            "   with your content changes.\n",
            file=sys.stderr,
        )
        return 1

    print("✅ Content validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
