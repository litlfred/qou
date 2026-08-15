# Prune-restoration tranches — index, and why size is the wrong order

Generated 2026-08-15. Bean `prn1`. **Nothing is restored by any of these.**

`2026-08-15-prune-damage-redrive.md` established that the damage cuts far better
by **target** than by source: 692 still-lost edges across 320 blocks become a few
dozen questions when you ask "must a reader have read `T` first?" once per `T`.
These are the first four, largest first.

| # | target | sources | prose-linked | mention only | **would point forward** | sheet |
|---|---|---|---|---|---|---|
| 1 | `thm:jones-markov-trace` | 21 | **2** | 4 | **0** | [sheet](2026-08-15-tranche-1-jones-markov-trace.md) |
| 2 | `def:hecke-normal-form` | 20 | **1** | 8 | **0** | [sheet](2026-08-15-tranche-hecke-normal-form.md) |
| 3 | `def:borromean-baryon` | 16 | **0** | 4 | **4** | [sheet](2026-08-15-tranche-borromean-baryon.md) |
| 4 | `def:crossing-energy` | 12 | **3** | 6 | **1** | [sheet](2026-08-15-tranche-crossing-energy.md) |

69 sources. **6 carry a prose link to the target they omit from `uses[]`** — the
block's own two halves contradicting each other, which is a defect rather than a
matter of taste. About 22 more mention the concept without linking; that is where
a reader's judgement actually decides something.

## Restoring an edge can create a forward reference — now measured, not assumed

`uses[]` pointing at a block later in the same chapter is what
`detangler-no-forward-ref` counts, and what the `fwr` arc spent five PRs cutting
from 274 to 194. Restoration adds `uses[]` entries, so some restorations push it
back up. **A correct restoration can silently undo a different piece of correct
work.**

The concrete case: `def:crossing-energy` was relocated into
`knots-particles-confinement` **§8** on 2026-08-09 *so that* the electroweak
results would stop forward-referencing their own definitions.
`prop:hadron-exists`, one of the blocks that lost the edge to it, sits at
within-chapter position **21** against `crossing-energy`'s **87**. Restoring
that edge recreates exactly what the relocation removed.

Every sheet now costs this per source, via `pointsForward` — exported from
`qa-checkers-extended.ts` for this, so nobody hand-rolls a third manifest parser
(the duplication `fsl7` exists to prevent). It answers `n/a` when either block
is unplaced: **unknown, not safe.**

## What that changes: the order

**Tranches 1 and 2 are ordering-safe wholesale.** All 41 of their sources point
backward, so restoring any or all of them cannot regress the detangler metric.
They are also the two largest. The only remaining question for them is the
editorial one, which is exactly the state a tranche is supposed to reach.

**Tranches 3 and 4 need five blocks handled individually** — four in
`borromean-baryon` (`rem:down-quark-properties`, `rem:up-quark-properties`,
`rem:binding-knots-visual-inventory`, `rem:knot-particle-dictionary`) and one in
`crossing-energy` (`prop:hadron-exists`).
Each needs `foreshadows[]`, a relocation, or a deliberate decision to accept the
forward edge. The other 23 sources in those tranches are unaffected.

So the recommended order is **1, 2, then 4, then 3** — not by size:

- **Tranche 4 (`def:crossing-energy`)** has the strongest evidence of the four
  despite being smallest: 3 of 12 link, 6 of 12 mention, and
  `rem:commutative-crossing-energy` both links in prose *and* references the
  declaration in Lean.
- **Tranche 3 (`def:borromean-baryon`)** is the weakest and should not be done
  early merely for being large: **no source links to it**, 10 of 16 have no
  `.lean`, and it carries 4 of the 5 forward-pointing blocks. It is a narrative
  cluster of remarks, an example and a simulator — a genuine reading question
  with almost no mechanical signal.

## One caution on the mention column

For **tranche 2**, bare "normal form" is generic and appears for unrelated
reasons. Only the three blocks matching **"hecke normal form"** exactly
(`prop:gb-spectral-sequence`, `def:confinement-level`,
`prop:gb-residue-spectral-sum`) carry weight; the rest are weak and should not
be read as corroboration.

## What none of this decides

Whether the edge belongs. The prune applied a mechanical rule across a corpus
without reading, and restoring mechanically repeats it in the opposite
direction — at least one removal is known deliberate (`def:adelic-substrate`
lost `def:classical-limit-functor` by owner decision in `78a570365d`, and
restoring it re-opens a cycle). The `uses-editorial-review` two-reader standard
governs what is applied. These sheets only remove the busywork from that
reading, and now also guarantee it cannot quietly cost the paper its ordering.

Regenerate any sheet: `bun run scripts/prune-tranche-sheet.ts <target-label>`.
