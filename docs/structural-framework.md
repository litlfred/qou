# Structural framework — chapter → section → subsection

The paper's structure is a **tree of exactly three levels**. This
document is the *organizational principle* the paper is audited
against (`content/pipeline/qa-section-title-audit.ts`, structure pass).
It exists because the corpus grew two-level (chapter / section) and a
chapter-restructure migration left auto-split sibling sections
(`"X : vs"`, `"X : generation"`) that should have been subsections;
introducing subsections corpus-wide needs one consistent rule set, not
ad-hoc nesting.

## The five rules (all machine-auditable)

| # | Rule | Audited by |
|---|------|-----------|
| **P1** | **Depth ≤ 3.** chapter (L1) → section (L2) → subsection (L3). **No sub-subsections.** Block-internal markdown headings (`#`, `##`) are inline `\paragraph`s, *not* structural levels — they do not count toward depth. | a subsection that itself has `subsections` → violation |
| **P2** | **No only-child.** A parent with exactly one structural child is degenerate — flatten it. A chapter needs ≥ 2 sections; a section that opens `subsections` needs ≥ 2 of them. (A lone subsection is just the section's own blocks.) | parent with 1 structural child → violation |
| **P3** | **Band.** A **section** holds **3–18 blocks** (the detangler section band, R1–R3). A **subsection** holds **2–12** (finer). A node below its floor isn't a node — merge it up; above its ceiling — split. | weight outside the band → flag |
| **P4** | **Balance — split when > 2.5× the peers.** *weight* = a node's total descendant block count. A section whose weight exceeds **2.5× the mean weight of its peer sections** in the same chapter is over-weight: **split it into subsections** (this is the primary rebalancing move). Symmetrically, a section well *below* the peer mean (and under the P3 floor) merges up. So the tree stays "balanced" = siblings comparable in weight, with the heavy ones pushed down a level. | weight > `2.5 × mean(peers)` → split-flag |
| **P5** | **Distinct, parent-scoped titles.** No two siblings share a title; each title is short and reads correctly *under its parent* (see `one-voice-style-guide.md` §Title Conventions). Subsection titles are owned by their section and need only disambiguate within it. | same-title siblings / `" : <tag>"` artifacts → hard defect |
| **P6** | **Detanglement extends to subsections.** The detangler invariants — no forward refs (H1), the section band (R1–R3), no cross-chapter forward edges, story-coherent ordering — all apply at the **subsection** level. Flatten the tree in reading order; **no block's `uses[]` may point to a later subsection**, and **a section split into subsections must cut along a dependency-respecting boundary** (the new level introduces no backward edge). | a uses[]-edge that runs backward in the flattened (chapter→section→subsection→block) reading order → forward-ref violation |

"Balanced in some way" (P3 + P4) means: siblings are *comparable in
weight*, and no leaf is so large it hides a missing level or so small it
shouldn't be its own node.

**P6 is checkable today, for free.** `detangler-no-forward-ref`
(`qa-checkers-extended.ts` → `loadChapterGraph`) builds each block's
reading-order position by regex-matching *every* `blocks: [...]` array
in source order — which already includes subsection blocks after their
parent — so a `uses[]` edge that runs backward across the nesting is
already caught. (The `detangler-section-band` check counts each
subsection as a section, applying the 3–18 band instead of the 2–12
subsection band — a minor over-strictness to refine.) The real
subsection-recursion gaps were the **renderer** (`\subsection` output)
and the **content validator** (loading nested blocks so their labels
resolve) — both fixed; see `docs/structural-reorg-plan.md` §Stage 0.

## When to introduce a subsection

A section earns subsections **iff both**:

1. it is **over-weight** (P4: weight > 2.5× its peer-section mean), **and**
2. its blocks fall into **≥ 2** coherent sub-arcs (each a future
   subsection of ≥ 2 blocks).

Otherwise keep it flat. **Never create a single subsection** (P2).

The chapter-restructure `"X : <tag>"` auto-splits are the canonical
case: the split-off sibling becomes a **subsection of its base `X`**,
with a short contextual title ("Confinement operator selection" ›
"SDP vs LP"). Where the split was gratuitous, **merge** it back into the
base instead.

## Rendering prerequisite

The renderer currently emits `\section{}` for every L2 node and has **no
`\subsection{}` path** (`render-latex.ts`). Enabling structural
subsections requires leveling by structural depth: L2 → `\section`,
L3 → `\subsection`, with `\setcounter{secnumdepth}{2}` so subsections
are numbered. This is a prerequisite of the paper-wide nesting pass, not
of the principle itself.

## The paper-wide pass (follow-up, not this PR)

A full review applies the rules chapter by chapter:

1. **Fold artifacts** — every `"X : <tag>"` section → subsection of `X`
   (or merge if gratuitous). Section labels are not cross-referenced in
   prose (only in the manifest + regenerable `.qa.json`), so this is
   label-safe; the blocks' sidecars regenerate.
2. **Subsection oversized sections** (P3 > 12) into ≥ 2 sub-arcs.
3. **Merge undersized** sections (P3 < 2) up into a neighbour.
4. **Rebalance** any parent failing P4.
5. **Retitle** per §Title Conventions (short, parent-scoped, story-led).

Track progress per chapter; the structure audit's exit code gates the
pass.

## Audit

```bash
bun run content/pipeline/qa-section-title-audit.ts            # titles + structure
bun run content/pipeline/qa-section-title-audit.ts --report-only
```

Hard defects (P1 depth, P5 artifacts) exit non-zero; P2–P4 are reported
as structure findings with a per-chapter balance summary.

**Two reviews, both tracked in CI** (`.github/workflows/section-title-audit.yml`):

- **Machine review** — the mechanical flags above (artifacts, band,
  depth, balance). Regenerated each run into the `machine` block of the
  committed per-paper sidecar `content/<paper>/section-title-audit.qa.json`.
- **Agent / human review** — the story-coherence + conciseness
  judgement (does the title tell the section's story, read against its
  parent). Recorded in the `agent` block of the same sidecar, one slot
  per section/subsection, `result: pending → pass | fail`, with a
  `reviewed_hash`. A chapter-manifest edit changes the hash and
  **re-opens the agent review as stale** — so reviews can't silently
  rot.

CI runs `--write-sidecar` and `git diff --exit-code`s the sidecars, so a
manifest change without a re-run fails ("sidecars stale").
