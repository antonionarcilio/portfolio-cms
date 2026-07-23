# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is an **Obsidian vault used as a headless content CMS** for a personal portfolio site (antoniomascarenhas.com.br). There is no application code, build system, or test suite here — the entire repo is structured Markdown content with YAML frontmatter that gets consumed elsewhere by the portfolio site. Work in this repo is content editing, not software engineering: adding/updating frontmatter fields, cross-linking entries, and keeping the PT/EN pairs in sync.

## Structure

All content lives under `content/`, one subfolder per content type. Each entry is a folder containing an `index.md` (Portuguese, the default locale) and an `index.en.md` (English translation) with parallel frontmatter.

- `content/index.md` / `index.en.md` — the root profile document; aggregates the whole site via wikilinks (contact, experience, education, skills, projects, achievements, seniority).
- `content/about/` — bio/about text (`description`, `excerpt`).
- `content/experience/<company>/` — work history entries (`start`, `end`, `stacks`, `employment_type`, `expertise_area`).
- `content/project/<company>/<project>/` — individual projects, linked from experience via `company` and to `stack` (technologies used).
- `content/skill/<skill>/` — skill categories (e.g. frontend, backend, devops), each linking a list of `technologies`.
- `content/technology/<tech>/` — leaf nodes describing individual tools/technologies (`aliases`, `description`). Referenced by skills, projects, and experience.
- `content/education/`, `content/seniority/`, `content/achievements/`, `content/contacts/<channel>/` — smaller standalone entry types, each with their own minimal frontmatter shape.

## Content conventions

- **Every entry is bilingual**: editing one field almost always means editing the same field in both `index.md` (pt-BR) and `index.en.md` (en). Keep wording equivalent in meaning, not literal translation.
- **Cross-links use Obsidian wikilink syntax**: `"[[content/path/to/index|Display Text]]"`. Portuguese files link to `index` targets; English files link to `index.en` targets (note: some existing links inconsistently include `.md` — match the style already used in the specific field you're editing rather than "fixing" it repo-wide).
- **Frontmatter field types are declared in `scripts/types-schema.yaml`** — this is the source of truth for type validation in the pre-commit hook and for generating `content-types.d.ts` (consumed by the frontend). `.obsidian/types.json` is only for Obsidian's in-app property UI; when adding a new field, update **both** files.
- **Multi-paragraph `description` fields use YAML block scalars** (`description: |-`) — preserve blank lines between paragraphs.
- Every content entry also carries an `excerpt` (short summary) distinct from the full `description`.
- Dates use ISO `YYYY-MM-DD`. An open-ended `end` date on current work should be left blank rather than guessed.
- Icons reference Lucide icon names with a `lucide-` prefix (e.g. `lucide-mail`, `lucide-code-xml`).
- **File and folder names use lowercase + kebab-case** (e.g. `content/project/some-company/some-project/`).
- **Root directories inside `content/`** (e.g. `experience`, `project`, `skill`, `technology`, `education`, `seniority`, `achievements`, `contacts`) refer to entities/content types and should always be named in the **singular**.

## Obsidian setup

Community plugins in use: `dataview`, `pretty-properties`, `symbols-prettifier` (see `.obsidian/community-plugins.json`). `.logs/` is generated locally by a plugin (`/subtask` command) and is gitignored — don't commit it.
