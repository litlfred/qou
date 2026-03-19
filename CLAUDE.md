# Claude Code — Quantum Observable Universe

This repository is a LaTeX manuscript for a formal mathematics paper.

## Skills

Skills are organized under `.claude/skills/`:

- **`local/`** — repo-specific skills (latex-validation, scientific-accuracy,
  readability-editing)
- **`<package-name>/`** — skills synced nightly from external packages defined
  in `skills-config.json`

### When to use skills

When making **any content change** to `.tex` files or `references.bib`:

1. **Before writing**: consult `scientific-writing`, `hypothesis-generation`,
   or `literature-review` skills as appropriate for the task.
2. **While writing**: follow `scientific-accuracy` and `latex-validation`
   guidelines.
3. **After writing**: apply `readability-editing` and `peer-review` skills to
   self-review the change.

For equations and proofs, consult the `sympy` skill for verification.
For figures, consult `scientific-visualization` and `matplotlib`.
For references, consult `citation-management` and `arxiv-database`.

### Coding conventions

Follow the detailed rules in `.github/copilot-instructions.md` — they govern
LaTeX structure, labeling, cross-references, prose style, and notation.

## Project structure

| Path | Purpose |
|------|---------|
| `main.tex` | Preamble and document structure |
| `chapters/*.tex` | One file per chapter |
| `references.bib` | BibTeX database |
| `.claude/skills/local/` | Repo-specific review skills |
| `.claude/skills/<pkg>/` | Synced external skill packages |
| `skills-config.json` | Skill package subscriptions |
