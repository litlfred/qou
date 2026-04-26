---
name: one-voice-audit
roles: [collaborator, owner]
---

# One-Voice Audit

## Role

The paper speaks with **one voice**: an authoritative, scholarly,
third-person voice making claims about quantum observable universes.
Anything that breaks that voice is a violation. Common breakages:

1. **Status markers** in body prose — `✅ Done`, `(TODO)`, `(TBD)`,
   `**Pending.**`, etc. These are work-tracker speech (CLAUDE.md §4a:
   content TODOs live in `todos/`, not in the paper).
2. **Emoji used as content** — `✅`, `❌`, `⚠`, `🔧`, `🚧` outside of
   tables. Even in tables, these belong only when used as compact
   comparison markers (✓ matches / ✗ diverges); never as work status.
3. **First-person work tone** — "we'll add X", "let me", "needs more
   work", "I'll fix this".
4. **Time-stamped notes** — "as of 2025-…", "after the recent push",
   "in the current draft" — signals draft state, not paper authority.
5. **Unicode characters that don't compile** — `↦` U+21A6, `⁻` U+207B,
   `√` U+221A, `─` U+2500, `✅` U+2705, etc. — even when intended,
   they crash `pdflatex` unless mapped in the preamble.

## When to use

- As a sub-pass of `editor` whenever content is added or edited.
- Before `prepare-merge` on any branch.
- On demand: "audit one-voice", "find status leaks", "clean up
  TODO markers".

## Workflow

### 1. Sweep (greps)

```bash
CONTENT=content/quantum-observable-universe

# Status emoji + comparison markers in .md
grep -rEn "[✅❌⚠⏳🔧🚧☑☒]|✓|✗|★" "$CONTENT" --include="*.md"

# Work-tracker words (case-insensitive, word-bounded)
grep -rEni "\b(todo|fixme|xxx|wip|to-do|tbd|in progress|pending review)\b" \
  "$CONTENT" --include="*.md"

# "Done" / "Completed" as status (avoid false positives like "is done")
grep -rEn "\*\*Done\*\*|\*\*Completed\*\*|\bDONE\b|\bCOMPLETED\b" \
  "$CONTENT" --include="*.md"

# First-person work tone
grep -rEn "\b(we'll add|I'll add|let me|needs more work|note to self|we should fix)\b" \
  "$CONTENT" --include="*.md"

# Unicode chars that crash pdflatex
grep -rln "↦\|⁻\|√\|─\|✅" "$CONTENT" --include="*.md"
```

### 2. Triage by category

| Category | Examples | Fix pattern |
|----------|----------|-------------|
| **A. Status leak** | `✅ Done`, `(TODO)`, `(TBD)` (with no follow-up content) | **Delete.** If the work item is still relevant, file as a `TodoItem` in `todos/`. |
| **B. Comparison-table marker** | `✓` / `✗` in a results table (one cell wide, replaces redundant prose) | **Keep — but only in tables.** ✓/✗ in body prose → replace with words ("matches", "diverges"). |
| **C. Warning callout** | `⚠ *…*`, `**⚠ WARNING:**` | **Replace** with `**Caveat.**` or `**Warning.**` (no symbol). |
| **D. Star marker** `★` | "best fit", "magic-receptive", "shell closure" | **Keep in tables when meaning is column-scoped.** In body prose → replace with explicit word. |
| **E. Unicode crash** | `↦`, `⁻`, `√`, `─`, `✅` | Replace with LaTeX command in math (`\mapsto`, `^{-1}`, `\sqrt{}`) or strip box-drawing comments. Add to preamble's `\newunicodechar` list only if widely used. |
| **F. First-person work tone** | "we'll add", "I'll fix" | **Rewrite in passive/scholarly voice.** Often a sign the sentence shouldn't exist at all. |

### 3. Apply mechanical fixes

These are safe to do without author approval:

- Delete Category A status leaks.
- Convert Category C warnings: `⚠ *X*` → `*Caveat: X*` or
  `**⚠ WARNING:** X` → `**Warning.** X`.
- Fix Category E Unicode crashes (use LaTeX equivalents in math; strip
  box-drawing).
- Replace clear-cut Category B/D markers in **body prose** (not
  tables) with words.

### 4. Kick back to author for items where:

- A `TBD` marks a **genuine open question** — author knows the
  resolution. Skill must not unilaterally delete.
- A table is so dense with `★`/`✓`/`✗` markers that replacing them
  with words would balloon the table; author should decide whether
  the compact markers are acceptable scholarly form for that table.
- Status updates inside **expository proofs** ("We have shown…",
  "It remains to verify…") that look like work tracking but are
  actually proof structure — author judgement on tone.

For each kickback, post a TodoItem (`todos/content-todos.ts`) with:
- `targetLabel` of the affected block
- A short description of the violation
- Suggested fix or "needs author rewrite"

### 5. Output

Report back with:
- **Fixed in this pass** — file:line list of mechanical fixes applied
- **Kicked back** — TodoItem entries created, requiring author attention
- **Verified clean** — files swept and clean

## Cross-references

- `markdown-render-check` — catches Unicode crashes and `+`-bullet
  failures *before* push; complementary preventive skill.
- `readability-editing` — broader prose tightening; one-voice is a
  subset.
- `editor` §4a — invokes this skill as a sub-pass on content changes.
- `proof-conciseness` — for trimming proofs that contain work-tracker
  language disguised as expository structure.
- `CLAUDE.md` §4a — content TODOs are external to paper; live in
  `todos/`, never in `.md` content.
