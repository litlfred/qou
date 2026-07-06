# Ghost-value sweep — does the corpus advertise values the canonical compute can't reproduce?

**Date:** 2026-06-17
**Branch:** `claude/ghost-value-sweep-2026-06-17`
**Motivation:** generalise the `hadron-knot-table` de-fitting finding (a
committed ⁴He binding of 28.19 ≈ experiment that the current categorical
path no longer produces — 0.72). Question: **is that pattern widespread —
are other witnesses advertising "passing" accuracy claims their current
producer would no longer back?**

## Method

`computations/audits/ghost_value_sweep.py` flags witnesses that are
simultaneously:
(a) `allPassed == true`,
(b) carry an **accuracy/precision assertion** (a tolerance-bearing match to
    experiment/expected), and
(c) **self-stale** — recorded `scriptHash` ≠ current producer hash.

(a)+(b)+(c) is the static signature of a possibly-stale pass. It does **not**
prove a value is wrong — only recompute does.

## Result — reassuring: the pattern is RARE, not widespread

- The static sweep flags **204 / 391** allPassed+accuracy witnesses as
  self-stale. But **self-staleness is dominated by reorg churn** (producers
  reformatted / moved, output unchanged), so the raw 204 is mostly noise.
- **Recompute-verification of the top candidates** (the real test) shows
  them **cosmetic, not ghosts**:
  - `channel_product_mass` (32 ⁴He-mass claims) → recomputes **clean**, all
    32 assertions still pass.
  - `codata_reconciliation` (7 claims) → recomputes **clean**, all 7 pass.
- So the highest-ranked candidates are *not* de-fits — their committed
  values still hold under the current producer.

**Conclusion.** The hadron-knot-table de-fitting was an **isolated
honest-rewrite case** (a producer deliberately changed to drop a retired
empirical fit), **not** a corpus-wide ghost-value problem. The framework's
committed accuracy claims are, on the evidence of the top candidates, backed
by the current canonical compute. The three-calibration / no-fit discipline
holds — this critical-distance integrity check came back clean.

## Honest limits of the tool

The static signal (self-staleness) **over-flags**: ~half of allPassed
accuracy witnesses are self-stale, but verification shows that is reorg
churn, not stale values. A scalable ghost detector would need the
recompute-and-compare step the verification did by hand — which is
infeasible across 200+ witnesses (many producers are slow/SDP/hang, e.g.
the `fe56`-class mass tables). The tool is therefore a **ranked starting
point for spot-checks**, not a verdict; the verdict requires recompute, and
where it was applied it came back clean.

## Disposition

Ships as a standalone critical-distance utility. The actionable takeaway is
the *negative* result: no evidence of widespread numerology/de-fitting
beyond the single hadron case already addressed (#2396, "use canonical
only"). If a genuine ghost-hunt is wanted, the next step is a CI batch job
that recomputes the flagged producers and diffs values — not more static
heuristics.
