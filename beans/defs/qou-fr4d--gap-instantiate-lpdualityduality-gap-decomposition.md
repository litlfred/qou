---
# qou-fr4d
title: 'GAP: instantiate LPDuality.duality_gap_decomposition against emitted LP duals'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T07:51:51Z
updated_at: 2026-10-04T15:12:56Z
parent: qou-v2om
---

## What exists

`folio/quantum-observable-universe/lean/QOU/Mathlib/LPDuality.lean` now
carries FOUR sorry-free theorems (lean-direct exit 0; `#print axioms` on all
four = `[propext, Classical.choice, Quot.sound]`, no `sorryAx`):

- `weak_duality` — gap >= 0 under primal/dual feasibility (pre-existing).
- `strong_duality` — certificate form under complementary slackness
  (pre-existing).
- `duality_gap_decomposition` — NEW, and the one that matters here. An
  UNCONDITIONAL identity, no feasibility hypothesis:

      sum_j c_j x_j - sum_i b_i y_i
        = sum_j (c_j - (A^T y)_j) * x_j  +  sum_i y_i * ((A x)_i - b_i)

- `duality_gap_le_of_residual_bounds` — NEW. If every primal and dual
  residual term is <= eps, the gap is <= (n + m) * eps.

## What is missing

Nothing consumes them. Every LP/SDP producer records the solver's OWN
`duality_gap` scalar and asserts it is near zero -- i.e. the solver both
computes the answer and grades itself. The decomposition makes that
independently checkable from the emitted certificate alone.

## Why it was not wired in this PR

The obstruction is the (A, b, c) mapping, and it is in the SHARED solver, not
in any one producer. `solve_operator_selection_lp(t, G, n_target)` poses

    min t.x  subject to  sum x = n_target,  G x >= 0,  x >= -M_bound

and packs those three blocks into whatever row order the clarabel-MPFR /
scipy-HiGHS backends want. To recompute the residuals a consumer needs (a) the
row order, (b) the sign convention `y_star` is returned in, and (c) whether
`y0_star` (the net-constraint shadow price) enters the dual sum with the same
sign as the `y_star` rows. None of that is documented at the boundary.

A WRONG mapping is worse than no check: it fails for a bookkeeping reason and
reads as a real duality failure. That is why this is a bean and not a guessed
implementation.

## Next honest step

Add `residuals()` to `LpDualResult` in
`tools/pyhecke/python/pyhecke/lp_dual_solver.py` -- the solver is the only
place that knows the packing -- returning the two residual sums as mpmath
values, plus `gap_recomputed`. Then every LP/SDP producer gets the certified
gap for free, and `lp_dual_witness_validator.py` can require it. Cross-check
against the solver's reported gap on a producer whose gap is NOT ~0 (this one
is 3.95e-44, so it cannot discriminate a correct mapping from a wrong one).

## Related

- `qou-ftuv` (completed) states "Clarabel is a float64 solver -- there is no
  `mpmath.mpf` to carry from the source". That was true on 2026-08-10 and is
  NOT true now: the clarabel-MPFR backend at `prec_bits=167` (~50 dps) exists,
  returns `*_str` decimal companions, and this branch measured the difference
  (`y0_star` first differing significant digit: 6).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 66 — PR #8274)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8274`](https://github.com/litlfred/qou/pull/8274) (branch `feat/round66-young-alien-lp-dt-spectral-43c1`, Commit 1 `efa6ab9e44128d259563d9e6208d6ab9d32edd74`, Commit 2 / Head `5423d4a1b0e6c19be96012412c48bd64329fdf2c`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/Mathlib/LPDuality.lean (`duality_gap_eq_zero_of_zero_residuals`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/young_kernel_alien_lp_dt_spectral_probe.py` (`scriptHash: 68202cff458f`) + `test/results/witnesses/young-kernel-alien-lp-dt-spectral.witness.json` (`allPassed: true`).
