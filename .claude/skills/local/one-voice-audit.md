---
name: one-voice-audit
roles: [collaborator, owner]
---

# One-Voice Audit

## Role

The paper speaks with **one voice**: an authoritative, scholarly,
third-person voice making claims about quantum observable universes.
**Scholarly voice is the default** for both narrative `.md` AND proof
bodies (Lean docstrings, expository comments) — exceptions require an
explicit author marker (`tags: ["non-scholarly-voice-exception"]` on
the block's `.ts` manifest, with a `notes` field on the QA report
recording the rationale). Anything that breaks that voice is a
violation. Common breakages:

1. **Status markers** in body prose — `✅ Done`, `(TODO)`, `(TBD)`,
   `**Pending.**`, etc. These are work-tracker speech
   (`CLAUDE.md` §4a *TodoItem lifecycle rules*: content TODOs live
   in `todos/`, not in the paper).
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
6. **AI / status-update phrasing (LLM tells)** — "Let me think about
   this", "Here's what I did", "I'll go ahead and", "Note that we
   should", "Great question", repeated First/Second/Third bullet
   cadence, over-use of "essentially" / "comprehensive" / "leverage"
   / "streamline" / "robust" / "delve into".
7. **Non-scholarly default tone** — block prose or Lean docstring
   that drifts into lecturer cadence ("So what we're going to do is
   …"), journalistic register ("In a surprising twist, …"), or
   second-person address ("You will see that …") without explicit
   author opt-out.
8. **Block placement does not fit section/chapter** — a block whose
   topic, kind, or register is incongruent with its surrounding
   section. Symptoms: a `definition` in a "Discussion" section, a
   `proposition` outside the chapter's proof chain, a `prose` block
   that introduces a topic the chapter does not subsequently cover.
9. **Deprecated framework usage** — 5-tuple `(M, Θ, G, P, E)` instead
   of `(C, Θ, G, S)`; `$\omega$` for fibre functor (canonical: `$\tau$`);
   `$\mathcal{C}$` for category (canonical: `$\mathbf{C}$`); bare
   `$H_q$` for any of three distinct objects ($\mathcal{H}_q$,
   $\hat{H}_q$, $H_n(q)$, $H_q(\lambda)$).
10. **Archimedean / algebraic wall side mismatch** — per CLAUDE.md
    §7c, algebraic substrate blocks must NOT mention `Real.*`,
    `linarith`, `0 < q`, or `ℝ` without declaring archimedean
    specialisation; archimedean blocks must declare their `ℝ`
    types explicitly.

## When to use

- As a sub-pass of `editor` whenever content is added or edited.
- Before `prepare-merge` on any branch.
- On demand: "audit one-voice", "find status leaks", "clean up
  TODO markers".
- As the **adjudicator** for the non-automated criteria
  (`voice-scholarly-default`, `voice-ai-slop`,
  `fit-section-chapter`) dispatched by
  [`local/one-voice-integration-watcher`](one-voice-integration-watcher.md).
  When invoked in this mode, write a reviewer entry to the
  block's sidecar `<block>.qa.json` rather than (or in addition
  to) reporting in chat — see *§ QA report integration* below.

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

# Unicode chars that crash pdflatex (or render unreliably)
grep -rEn "↦|⁻|√|─|✅|·|²" "$CONTENT" --include="*.md"
```

### 2. Triage by category

| Category | Examples | Fix pattern |
|----------|----------|-------------|
| **A. Status leak** | `✅ Done`, `(TODO)`, `(TBD)` (with no follow-up content) | **Delete.** If the work item is still relevant, file as a `TodoItem` in `todos/`. |
| **B. Comparison-table marker** | `✓` / `✗` in a results table (one cell wide, replaces redundant prose) | **Keep — but only in tables.** ✓/✗ in body prose → replace with words ("matches", "diverges"). |
| **C. Warning callout** | `⚠ *…*`, `**⚠ WARNING:**` | **Replace** with `**Caveat.**` or `**Warning.**` (no symbol). |
| **D. Star marker** `★` | "best fit", "magic-receptive", "shell closure" | **Keep in tables when meaning is column-scoped.** In body prose → replace with explicit word. |
| **E. Unicode crash** | `↦`, `⁻`, `√`, `─`, `✅`, `·`, `²` | Replace with LaTeX command in math (`\mapsto`, `^{-1}`, `\sqrt{}`, `\cdot`, `^{2}`) or strip box-drawing comments. Add to preamble's `\newunicodechar` list only if widely used. |
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

## QA report integration

The watcher persists every finding to the block's sibling
`<block>.qa.json` file (schema:
[`folio-assistant/schemas/block-qa.ts`](../../../folio-assistant/schemas/block-qa.ts)).
Per-criterion staleness is keyed by SHA-256 prefix of the source
files at audit time — when the `.md` (or `.ts` / `.lean`) is later
edited, the recorded `field_hash` no longer matches, and the
criterion is stale.

### CLI primitives

- **Sweep** — runs every automated criterion on a content root and
  writes / updates the sidecars:

  ```bash
  cd content
  bun run pipeline/qa-sweep.ts \
    quantum-observable-universe/organic-chemistry
  ```

- **Staleness map** — reports which blocks have fresh / stale /
  missing audits per criterion:

  ```bash
  cd content
  bun run pipeline/qa-staleness.ts \
    quantum-observable-universe/organic-chemistry
  ```

- **CI gate** — fail the build if any block has critical findings
  or no sidecar:

  ```bash
  bun run pipeline/qa-sweep.ts \
    quantum-observable-universe --ci
  ```

### Multi-reviewer writes (when an agent adjudicates)

When invoked by the watcher for one of the non-automated criteria
(`voice-scholarly-default`, `voice-ai-slop`, `fit-section-chapter`),
**append** a new entry to the corresponding criterion's array.
**Never delete** prior entries. Reviewer identity must be
`{ kind: "agent", id: "one-voice-audit", version: "<model id>" }`
for agent runs and `{ kind: "human", id: "<github-login>" }` for
manual adjudications.

An entry's shape:

```json
{
  "field_hash": { "md": "<12-char-sha>", "ts": "<…>", "lean": "<…>" },
  "result": "pass" | "fail" | "warn" | "n/a",
  "severity": "critical" | "major" | "minor",
  "evidence": "<file:line: verbatim quote>",
  "reviewer": { "kind": "agent", "id": "one-voice-audit" },
  "reviewed_at": "<ISO-8601 UTC>",
  "reviewed_sha": "<main HEAD at audit time>",
  "notes": "<rationale / context>"
}
```

The current verdict for a criterion is the most-recent entry whose
`field_hash` matches the present source files. Human entries
outrank agent entries; agent entries outrank script entries — but
*only* when the higher-rank entry's `field_hash` is still fresh.

## Cross-references

- [`one-voice-integration-watcher`](one-voice-integration-watcher.md) —
  the watcher that drives this skill in audit-as-sidecar mode.
  Covers 11 criteria across four domains (voice, fit, framework,
  wall) and persists per-block reports.
- `markdown-render-check` — catches Unicode crashes and `+`-bullet
  failures *before* push; complementary preventive skill.
- `readability-editing` — broader prose tightening; one-voice is a
  subset.
- `editor` §4b — invokes this skill as a sub-pass on content changes
  (§4a delegates to `markdown-render-check`; §4b is this skill).
- `proof-conciseness` — for trimming proofs that contain work-tracker
  language disguised as expository structure.
- `CLAUDE.md` §4a *TodoItem lifecycle rules* — content TODOs are
  external to paper; live in `todos/`, never in `.md` content.
