#!/usr/bin/env python3
"""Generate content-types.d.ts from types-schema.yaml and content-schema.yaml.

Called by the pre-commit hook after validation passes.
Can also be run standalone:  python3 scripts/generate_types.py
"""

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
TYPES_SCHEMA_PATH = REPO_ROOT / "scripts" / "types-schema.yaml"
TYPES_TS_PATH = REPO_ROOT / "content-types.d.ts"

TS_TYPE_MAP = {
    "text": "string",
    "number": "number",
    "date": "string",
    "checkbox": "boolean",
    "multitext": "string | string[]",
    "aliases": "string | string[]",
    "tags": "string | string[]",
    "cssclasses": "string | string[]",
}


def load_yaml(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def generate(schema: dict, types_schema: dict) -> str:
    """Return the TypeScript type definitions as a string."""
    types_defs = types_schema.get("content_types", {})
    content_fields = schema.get("fields", {})

    lines = [
        "// Auto-generated from scripts/types-schema.yaml and "
        "scripts/content-schema.yaml",
        "// Do not edit manually. Changes are committed automatically "
        "by the pre-commit hook.",
        "",
    ]

    sorted_types = sorted(t for t in types_defs if t != "root")
    if "root" in types_defs:
        sorted_types.insert(0, "root")

    for content_type in sorted_types:
        fields = types_defs.get(content_type, {})
        if not fields:
            continue

        required_keys = set(
            content_fields.get(content_type, {}).get("required", [])
        )
        type_name = content_type.capitalize() + "Fields"

        lines.append(f"export interface {type_name} {{")

        for field_name, field_def in sorted(fields.items()):
            ts_type = TS_TYPE_MAP.get(field_def["type"], "unknown")
            is_required = (
                field_def.get("required", True) or field_name in required_keys
            )
            optional = "" if is_required else "?"
            comment = ""
            if field_def["type"] == "date":
                comment = "  // YYYY-MM-DD"
            lines.append(
                f"  {field_name}{optional}: {ts_type};{comment}"
            )

        lines.append("}")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    schema = load_yaml(SCHEMA_PATH)
    types_schema = load_yaml(TYPES_SCHEMA_PATH)
    content = generate(schema, types_schema)
    TYPES_TS_PATH.write_text(content, encoding="utf-8")
    print(f"  ✔ Generated {TYPES_TS_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
