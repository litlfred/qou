---
# qou-bgur
title: 'Orbit3Braid docstring: size-3 orbit characterised by ADJACENCY, should be COMPARABILITY'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T02:59:25Z
updated_at: 2026-11-17T13:00:03Z
parent: qou-1oif
---


## The inaccuracy (mine, in merged prose)

Orbit3Braid.lean's module docstring says a size-3 orbit is

  "the standard fillings of a DOMINO together with a disjoint cell.  The domino's two
   cells are ADJACENT, which forces their relative order, so only 3!/2! = 3 of the six
   assignments are standard."

The count 3 is right; the REASON is wrong, and the characterisation is too narrow.

Exact enumeration of standard fillings by 3-cell configuration:

  3 in a row  (0,0)(0,1)(0,2)          -> 1
  3 in a column                        -> 1
  chain       (0,0)(0,1)(1,1)          -> 1     <- not previously considered
  HOOK        (0,0)(0,1)(1,0)          -> 2     <- the size-2 case, never characterised
  row-domino + disjoint                -> 3
  col-domino + disjoint                -> 3
  TWO IN A ROW, FAR APART (0,0)(0,5)(3,9) -> 3  <- refutes the adjacency claim
  3 mutually non-adjacent              -> 6

Two same-row cells that are NOT adjacent still give 3. What forces the order is
COMPARABILITY (same row, or same column), not adjacency. Adjacency is neither necessary
nor the operative property.

Why the confusion arose: sameRow_adjacent proves that cells holding CONSECUTIVE entries
k, k+1 in the same row must be adjacent. That is true and is used correctly elsewhere. But
in a size-3 orbit the two same-row cells may hold k and k+2, which need not be adjacent —
so the lemma does not license the docstring's phrasing.

FIX (not applied; prose-only, and the owner asked for new prose issues to be beaned rather
than fixed mid-stream): restate as "exactly one comparable pair (two cells sharing a row or
a column); the comparability forces one order relation, halving 6 to 3." The Lean is
unaffected — genA/genB and both theorems are parametrised by sc and a1/a2, never by
adjacency.

### Progress Update (Round 68 — PR litlfred/qou#8356)
- **PR:** https://github.com/litlfred/qou/pull/8356 (`2c058b5e380e076d0aec9233aad57fa6af43d018`)
- **Lean 4 Module:** `QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling` (`LEAN_EXIT=0`, `0` warnings, `0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 major, 0 advisory` across all directory-mode static vacuity & borrowed-name audits)
- **Numerical Probe & Witness:** `computations/probes/bring_curve_hochschild_stale_weight_cyclicity_three_cell_comparability_quadratic_rescaling_probe.py` & `computations/probes/bring-curve-hochschild-stale-weight-cyclicity-three-cell-comparability-quadratic-rescaling.witness.json` (`COMMIT1 = 8ee314938e6a9bac9ee46faedf9aebdee8b895fb`, `scriptHash = 326bd13833f0`, `allPassed = True`, `dps = 80`)
