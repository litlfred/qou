---
name: glossary-build
roles: [reader, collaborator, owner]
---

# Glossary Build Skill

## Role

Maintain the paper-wide glossary of defined terms. Builds the
`glossary.json` index from every block's `defines: [...]` field,
generates the `chapters/glossary.tex` chapter, and gates CI with
`--check` mode.

## When to invoke

- A user mentions: glossary, defined terms, `defterm`, `refterm`,
  `defines[]`, "build glossary", "regenerate glossary".
- After any block's `defines: [...]` field is added, modified, or
  removed.
- As part of `local/content-validation` whenever a chapter is
  validated end-to-end.

## Tools

| Command | Purpose |
|---------|---------|
| `cd content && bun run pipeline/build-glossary.ts <paper-dir>` | Generate `glossary.json` + `chapters/glossary.tex` |
| `cd content && bun run pipeline/build-glossary.ts <paper-dir> --check` | CI gate — non-zero exit on duplicates or out-of-date JSON |
| `cd content && bun run pipeline/codemod-refterm.ts <chapter-dir>` | Dry-run: preview `:refterm[…]` backfill in a chapter |
| `cd content && bun run pipeline/codemod-refterm.ts <chapter-dir> --write` | Apply backfill to disk |
| `cd content && bun run validate <paper-dir>` | Includes the five glossary-term validation rules |
| `cd content && bun run validate <paper-dir> --strict` | Adds `term-mention-coverage` (bare-text mentions) |

## Authoring contract

Every term registered in any block's `defines: [...]` field **must** be
wrapped at every occurrence:

- **Defining occurrence** (exactly one block): `:defterm[Visible]` /
  `:defterm[Visible]{#slug}` in `.md`; `\defterm{slug}[{Visible}]` in
  `.tex`.
- **Reference occurrences** (every other mention, anywhere in the
  paper): `:refterm[Visible]` / `:refterm[Visible]{#slug}` in `.md`;
  `\refterm{slug}[{Visible}]` in `.tex`.

Plain text and `\emph{}` are no longer permitted for defined terms once
the slug appears in any `defines[]` list.

## Validation rules (Phase B)

| Rule | Severity | Trigger |
|------|----------|---------|
| `defterm-declared` | error | `:defterm[X]` whose `X` is not in this block's `defines[]` |
| `defterm-marked` | warning | `defines[]` entry with no `:defterm[X]` in the `.md` |
| `refterm-resolves` | error | `:refterm[X]` not declared in any block's `defines[]` |
| `defterm-unique` | warning | Same slug declared by multiple blocks |
| `term-mention-coverage` | warning (`--strict`) | Bare-text mention of a known slug not wrapped in `:refterm[…]` |

## CI integration (Phase E preview)

The Lean tie-in (`Glossary.lean` regenerated from `glossary.json`) is
gated by re-running `--check` in CI. Add the gate to the relevant
workflow once the backfill has reached steady state.

## See also

- `.github/copilot-instructions.md §11.0` — full authoring contract
- `CLAUDE.md §4c` — agent-facing rules
- `content/pipeline/validate-defterm.ts` — validator implementation
- `content/pipeline/build-glossary.ts` — builder implementation
- `content/pipeline/codemod-refterm.ts` — backfill codemod
