# Claude Code — Quantum Observable Universe

This repository is a LaTeX manuscript for a formal mathematics paper.

## Skills

Skills are organized under `.claude/skills/`:

- **`local/`** — repo-specific skills (latex-validation, scientific-accuracy,
  readability-editing)
- **`<package-name>/`** — skills synced nightly from external packages defined
  in `skills-config.json`

### When to use skills

See **§12 Using Skills for Content Changes** in
`.github/copilot-instructions.md` for the authoritative task-to-skill mapping
and rules. That section is the single source of truth — do not duplicate its
guidance here.

### Coding conventions

Follow the detailed rules in `.github/copilot-instructions.md` — they govern
LaTeX structure, labeling, cross-references, prose style, notation, and skill
usage for content changes.

## Project structure

| Path | Purpose |
|------|---------|
| `main.tex` | Preamble and document structure |
| `chapters/*.tex` | One file per chapter |
| `references.bib` | BibTeX database |
| `.claude/skills/local/` | Repo-specific review skills |
| `.claude/skills/<pkg>/` | Synced external skill packages |
| `skills-config.json` | Skill package subscriptions |
