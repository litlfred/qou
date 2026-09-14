---
# qou-u5qs
title: gamma-gamma production DERIVES the contiguous strand layout, uniquely — and that is why there is no 3-cell
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T19:44:28Z
updated_at: 2026-09-14T19:45:11Z
---

## 2026-09-14 — the measurement (probe 15/15, exact combinatorics, read-only)

`computations/onedim/gamma_gamma_forces_the_layout_probe.py`.

**The question.** `qou-9ven`'s follow-on probe measured that the contiguous
layout `nucleon k -> strands (3k, 3k+1, 3k+2)` is corpus-uniform (61 refs / 41
files) and found nowhere DOWNSTREAM a non-contiguous one could come from.
`NoThreeCellOnTheChain.lean` proves a linear layout has no triangle, hence no
3-cell -- but takes `LinearLayout` as a HYPOTHESIS. So: what forces it?
Owner ruling `qou-ales` says selection is gamma-gamma + confinement SDP,
never census -- so the answer had to come from there.

**The hypothesis, stated before the run.** `GammaGammaWordSelection.lean`
defines `vertex i = [sigma_i, sigma_{i+1}^{-1}]` -- ADJACENT Artin generators.
`sigma_j` exchanges strands `j, j+1`, so the vertex touches exactly
`{i, i+1, i+2}`. A nucleon's internal word `beta_Bor = vertex(0)^3` is
internal iff the strands it touches lie in that nucleon's own block.

**Measured, exhaustively over every 3-uniform partition of the 3A strands:**

| A | partitions | all-interval | gg-internal everywhere | carrying a triangle |
|---|---|---|---|---|
| 2 | 10 | 1 | 1 | 0 |
| 3 | 280 | 1 | 1 | **234** (83.6 %) |
| 4 | 15400 | 1 | 1 | **13969** (90.7 %) |

1. A 3-block admits an internal gamma-gamma vertex **iff** it is an interval
   (324 subsets over n = 6, 9, 12; 0 mismatches; decided by brute force over
   generator indices, not by the interval test, so it is not self-checking).
2. The all-interval partition is **UNIQUE** at every A, and it IS the
   contiguous layout. So the layout is not merely constrained -- it is
   DETERMINED.
3. Its block quotient is the path `P_A` -- which supplies the `LinearLayout`
   hypothesis `NoThreeCellOnTheChain.lean` assumes.
4. No all-interval partition carries a triangle; 83.6 % / 90.7 % of the
   others do. **The exclusion has content.**
5. The interleaved "residue" layout `{k, k+A, k+2A}` -- the obvious
   non-linear candidate -- has block quotient the **cycle C_A**, a triangle at
   A = 3. It is excluded because NOT ONE of its blocks is an interval, so
   under the Artin-adjacent reading no nucleon of it can carry an internal
   gamma-gamma word at all.

**So the contiguous layout is DERIVED, and the missing 3-cell is downstream of
the gamma-gamma definition rather than of a convention.** That closes the
`qou-9ven` follow-on question in the direction opposite to the one being
looked for: there is no derivable non-linear layout, and the failure to find
one is the result.

**Scope (b)**, invariant named: a `sigma_j` crossing joins CONSECUTIVE strands
only, so a 3-strand set closed under a gamma-gamma vertex is an interval, and
length-3 intervals tile `[0, 3A)` uniquely.

**NOT excluded, and it is the one real decision here:** a BAND-generator
reading. `a_{ts} = (sigma_{t-1}...sigma_{s+1}) sigma_s (...)^{-1}` crosses two
non-adjacent strands with writhe 1, so a band vertex `a_{ts} a_{t's'}^{-1}`
has writhe 0 and passes `writhe_eq_zero` while NOT being a `GammaGammaWord`
under the corpus's inductive definition. Under a band reading the
non-contiguous layouts reopen. Which reading the physics means is
definitional; choosing the one that yields a 3-cell would be selection against
the target (AGENTS.md "NO FITTING"), so it is left open for the owner.

Next: formalize (1)-(3) in Lean so `NoThreeCellOnTheChain`'s hypothesis is
supplied rather than assumed.
