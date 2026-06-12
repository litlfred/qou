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
   in `.beans/`, not in the paper).
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
11. **Structural-argument hedging / "exposition simplifies"
    framing** — the paper derives its results from a canonical
    derivation chain (CLAUDE.md *Canonical derivation chain*
    cheat sheet). It does not need "structural argument" /
    "morally correct" / "essentially the X" / "heuristically" /
    "simplification for exposition" / "provides the mathematical
    framework" / "broadly speaking" / "loosely speaking" /
    "for context" / "by way of background" / "in some sense" /
    "conceptually analogous" patches as a substitute for the
    derivation. These are signs that either (a) the canonical
    derivation IS in the paper and the hedge is paper-length
    cruft, or (b) the block is asserting an unsupported analogy
    and should be demoted to a remark with `interprets:` (per
    §3a) or removed. Paper-too-long policy: prefer (a) — strip
    the hedge — unless the block author flags a real gap.
    Common phrases (case-insensitive, multi-word):
    - `structural argument`
    - `morally correct`, `morally a`, `morally`
    - `essentially the`, `essentially a`, `essentially zero`,
      `essentially complete`
    - `heuristically (replaced|exploitable|the)`
    - `simplification for exposition`,
      `simplifies (the )?exposition`,
      `simplifies the paper`
    - `provides the (mathematical framework|natural setting|
      canonical duality)`, `provides a canonical (framework|
      duality|basis)`, `gives a canonical (functor|grading|
      ordering)`
    - `for context`, `by way of background`,
      `broadly speaking`, `loosely speaking`, `in some sense`,
      `conceptually analogous`
    - `amounts to`, `amount(s|ed) to`,
      `(reformulated|reformulation) as`
    Exceptions: (i) the phrase IS the canonical mathematical term
    of art and removing it changes the claim (e.g. "essentially
    surjective" as a category-theory term, "essentially zero"
    inside a results table); (ii) the block has an explicit
    `tags: ["non-scholarly-voice-exception"]` opt-out.

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

# Structural-argument hedging / "essentially" / "morally" / "heuristically"
# (criterion 11 — paper-too-long policy: prefer to strip)
grep -rEni \
  "structural argument|\bmorally\b|essentially (the |a |zero|complete|surjective|non-local)|heuristically (replaced|exploitable|the)|simplification for exposition|simplifies (the )?exposition|simplifies the paper|provides (the |a )(mathematical framework|natural setting|canonical (duality|basis|framework))|gives a canonical (functor|grading|ordering)|for context|by way of background|broadly speaking|loosely speaking|in some sense|conceptually analogous|amount(s|ed) to|(reformulated|reformulation) as" \
  "$CONTENT" --include="*.md"

# Section / subsection / chapter TITLE coherence (chapter-scoped —
# runs on chapter manifests, not blocks): auto-split " : <tag>"
# artifacts, trailing colons, over-long / compound titles. Hard
# defects exit 1; emits a per-chapter agent worklist.
bun run content/pipeline/qa-section-title-audit.ts
```

### 2. Triage by category

| Category | Examples | Fix pattern |
|----------|----------|-------------|
| **A. Status leak** | `✅ Done`, `(TODO)`, `(TBD)` (with no follow-up content) | **Delete.** If the work item is still relevant, file as a `TodoItem` in `.beans/`. |
| **B. Comparison-table marker** | `✓` / `✗` in a results table (one cell wide, replaces redundant prose) | **Keep — but only in tables.** ✓/✗ in body prose → replace with words ("matches", "diverges"). |
| **C. Warning callout** | `⚠ *…*`, `**⚠ WARNING:**` | **Replace** with `**Caveat.**` or `**Warning.**` (no symbol). |
| **D. Star marker** `★` | "best fit", "magic-receptive", "shell closure" | **Keep in tables when meaning is column-scoped.** In body prose → replace with explicit word. |
| **E. Unicode crash** | `↦`, `⁻`, `√`, `─`, `✅`, `·`, `²` | Replace with LaTeX command in math (`\mapsto`, `^{-1}`, `\sqrt{}`, `\cdot`, `^{2}`) or strip box-drawing comments. Add to preamble's `\newunicodechar` list only if widely used. |
| **F. First-person work tone** | "we'll add", "I'll fix" | **Rewrite in passive/scholarly voice.** Often a sign the sentence shouldn't exist at all. |
| **G. Structural-argument hedging** | "structural argument", "morally correct", "essentially the X", "heuristically", "simplification for exposition", "provides the mathematical framework", "amounts to" | **Strip** if the canonical derivation IS in the paper (most cases — paper is already too long). **Demote** to `remark` with `interprets:` if the block is asserting an unsupported analogy. **Keep** only if (i) the phrase is a category-theory term of art (e.g. `essentially surjective`) or (ii) the block has `tags: ["non-scholarly-voice-exception"]`. |
| **H. Banner-in-prose** | `> **Status: theorem (sorry-free)...**`, `> **Caveat (over-permissive...)...**`, `> **Status (May 2026):...**`, `> **Refined-framing note (added when promoting...)...**` | **Migrate to `authorNotes` field** on the block's `.ts` manifest. Per CLAUDE.md `BlockBase.authorNotes` (the schema field added 2026-05-24), author-tracking notes belong as metadata, not in scholarly prose. Render pipeline skips them by default; `WITH_AUTHOR_NOTES=1` env var exposes them in working drafts. **EXCEPTION:** `**Theorem (conditional on [conj:X])**` banners required by CLAUDE.md §3b-cond are STRUCTURAL parts of the theorem statement, not author notes — keep in prose. |
| **I. Audit-doc reference in paper** | `docs/audits/...`, `[audit](../../../docs/audits/...)`, `per audit`, `see audit doc` | **Remove.** Paper content must NOT reference audit documents. Audit docs are internal working artifacts — they are not part of the scholarly publication. If the audit contains a result needed in the paper, promote the result to a content block (proposition/theorem/remark) and cite that block instead. Empirical observations (percentage matches, ppm comparisons to CODATA) belong in audit docs only, never in paper `.md` blocks. |
| **J. Empirical fit in scholarly prose** | "within X% of CODATA", "matches to Y ppm", "≈ Z MeV (close to...)", "near-match", "numerical observation" | **Remove from paper content.** Empirical comparisons are audit-doc material. Paper content states the derived formula; the audit doc records how well it matches experiment. **EXCEPTION:** a content block may state a formula's formal precision target (e.g. "the substrate identity matches CODATA to $0.24\,\mathrm{ppm}$") if the block IS a proposition about precision (e.g. `prop:proton-mass-substrate-identity`). |
| **K. Title coherence** | section/subsection title ending in `" : vs"` / `" : generation"` / `" : characterisation"` / `" : comparison"`; a comma-list title of 3+ concepts; a title meaningless without its chapter | **Rewrite from the section's story** — read the section's intro block, make it short + coherent against its responsible parent (paper→chapter→section→subsection) and distinct from the sibling. Surfaced by `qa-section-title-audit.ts`; conventions in `one-voice-style-guide.md` §Title Conventions. |

### 3. Apply mechanical fixes

These are safe to do without author approval:

- Delete Category A status leaks.
- Convert Category C warnings: `⚠ *X*` → `*Caveat: X*` or
  `**⚠ WARNING:** X` → `**Warning.** X`.
- Fix Category E Unicode crashes (use LaTeX equivalents in math; strip
  box-drawing).
- Replace clear-cut Category B/D markers in **body prose** (not
  tables) with words.
- Remove Category I audit-doc references from paper `.md` files.
- Strip Category J empirical fits from scholarly prose (move to audit).
- Migrate Category H banners to `authorNotes` field (extract banner
  text → push as `{ kind, date?, body }` entry on the block's `.ts`
  manifest; remove blockquote from `.md`). Skip the `**Theorem
  (conditional on conj:X)**` §3b-cond banners — those are structural.

### 4. Kick back to author for items where:

- A `TBD` marks a **genuine open question** — author knows the
  resolution. Skill must not unilaterally delete.
- A table is so dense with `★`/`✓`/`✗` markers that replacing them
  with words would balloon the table; author should decide whether
  the compact markers are acceptable scholarly form for that table.
- Status updates inside **expository proofs** ("We have shown…",
  "It remains to verify…") that look like work tracking but are
  actually proof structure — author judgement on tone.

For each kickback, post a TodoItem (`.beans/content-todos.ts`) with:
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
  external to paper; live in `.beans/`, never in `.md` content.
