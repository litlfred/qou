---
# qou-sof3
title: The SDP producer's primal_obj/duality_gap are the arithmetic floor, not a measurement — they track prec_bits
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:11:29Z
updated_at: 2026-09-04T09:22:49Z
---

Found by the FIRST real application of the certified-residual check
(`qou-fr4d`, PR #6609) to a producer. This is what the check was built to
surface, and it fired immediately.

## The observation

`qbeta_symbolic_sdp_strict_complementarity` publishes

    primal_obj    3.9236357001094877985864428332117651675847334372542e-44
    dual_obj     -2.6702701055721053455736631999011159472425342975215e-46
    duality_gap   3.9503384011652088520421794652107763270571587802294e-44

50 digits each. Recomputing `t . x*` from the SAME witness's published
`t_at_q0` and `x_star` gives **3.7024593e-44** -- a **5.64 %** disagreement
with the `primal_obj` sitting a few lines away in the same file.

## It is not rounding, and I checked before saying so

`x_star` is published at **52 significant digits**; with `max|x*| = 265025`
the last-digit weight is **2.65e-47**, i.e. ~0.07 % of the gap. That is ~80x
too small to explain 5.64 %. Neither rescue path fired: `rescaled_by_pow2` and
`loosened_status` are both absent. On a 3x3 toy LP with no cancellation the
same two quantities agree to ~50 digits, so it is not systematic in the solver.

## The cause, established by sweeping the dial

Re-ran the producer at three working precisions:

| prec_bits | primal_obj | t . x* | rel |
|---|---|---|---|
| 167 (default) | 3.92e-44  | 3.70e-44  | 5.6e-2 |
| 400           | 3.81e-100 | 3.81e-100 | 3.0e-16 |
| 800           | 3.82e-196 | -6.34e-116 | -- |

**The objective tracks the working precision.** It is 1e-44 at 167 bits,
1e-100 at 400, 1e-196 at 800. That is the signature of a quantity whose true
value is **zero**, reported at whatever the arithmetic floor happens to be.
The mechanism is the cancellation depth: `max|x*| = 2.65e5` collapsing to an
objective of ~0 is **48 orders**, so at 50.3 decimal digits of working
precision the absolute floor on the sum is 2.65e5 x 1e-50.3 ~= 1.4e-45 --
the same order as the observed 2.21e-45 discrepancy.

## What this means for the witness

Every published digit of `primal_obj`, `dual_obj` and `duality_gap` in this
witness is arithmetic floor, not mathematics. The LP's optimum objective is 0.

And the producer's own assertion

    lp_strong_duality: computed=|primal - dual|, expected=0, tolerance=1e-6

is **vacuous**: it compares two floor values to a tolerance 38 orders larger
than either. It passes at 167 bits, at 400, at 800, and would pass if the
solver were badly wrong. It has never been capable of failing.

## What it does NOT mean

The LP is not broken and the producer's conclusions are not affected. Its
verdict rests on the ACTIVE SET and the DIRECTION (`active_set = [0]`,
`direction_max_diff_across_scales = 1151423`), neither of which is a
cancellation, and both of which are stable. Read this as: three published
fields carry no information, and one assertion cannot fail. Not as: the
result is wrong.

This is also the sharper form of what the producer's own source already says
(step 2b): the LP min-trace objective is DEGENERATE because the Frobenius Gram
is indefinite, so the optimum is driven to the slice boundary ~0. The witness
then publishes that ~0 to 50 digits as though it were measured.

## Next steps

1. Replace the vacuous assertion with one that can fail -- assert on the
   ACTIVE SET (which is the actual claim of strict complementarity) rather
   than on a floor-valued gap.
2. Consider whether other LP producers publish floor-valued objectives the
   same way. Cheap detector: flag any LP witness where
   `max|x_star| / |primal_obj|` exceeds ~10^(0.9 * prec_bits * log10 2),
   i.e. the cancellation eats most of the working precision.

## Related

- `qou-fr4d` / PR #6609 -- the check that found it.
- PR #6608 -- reported `primal_obj`/`duality_gap` moving 16 % as "16 % of a
  residual that is essentially nothing". Right in direction, understated: the
  values are not small measurements, they are not measurements.


## RESOLVED (item 1) — the vacuous assertion is replaced, PR #6609 `be1a4e2954`

`lp_strong_duality` is gone. Two falsifiable assertions in its place:

- **`lp_duality_gap_certified`** — |gap_recomputed − solver duality_gap|,
  computed 2.21176397031290088864e-45 against a tolerance of
  1.4166990072900729933e-43. The tolerance is DERIVED (100x the cancellation
  floor max|x*|*10^(-prec_bits*log10 2) = 1.4167e-45), not chosen to pass;
  the observed value is 1.56x the floor, so it clears by ~64x and goes red if
  the published certificate stops reproducing the solver by more than two
  decades above the floor. Floor recorded as `duality_gap_cancellation_floor`.
- **`strict_complementarity_dual_separation`** — 46.564656861512461309
  decades, threshold 25. This is the property the producer is NAMED for and
  never asserted. y* = [1.0, 2.72e-47, 2.72e-47, 9.77e-48, 9.77e-48,
  1.04e-47]: one genuinely positive dual, five at the floor. Threshold is half
  the ~50-digit working precision, i.e. the point below which the inactive
  duals have left the floor. Recorded as `dual_separation_decades`.

**Both shown to fail**, in `lp_dual_certified_residuals_selftest.py` §4 —
including at the boundary (24 decades FAIL, 26 pass; 1.01x tolerance FAIL).
Shipping replacements for a non-falsifiable assertion without demonstrating
they can go red would have repeated the defect.

## STILL OPEN (item 2) — the detector for other LP witnesses

Unchanged: build a detector flagging any LP witness whose objective is
floor-valued, i.e. where the cancellation eats most of the working precision.
Candidate criterion, now with a worked instance to calibrate against:

    max|x_star| / |primal_obj|  >~  10^(0.9 * prec_bits * log10 2)

This producer: 2.65e5 / 3.92e-44 = 6.8e48 against a 0.9-threshold of 10^45.2
-- flagged, correctly. What is NOT yet known is the false-positive rate; an LP
whose optimum is legitimately tiny would also trip it. Run it across the 54
LP/SDP witnesses (see `qou-dke6` for that population) before believing any
count it reports.
