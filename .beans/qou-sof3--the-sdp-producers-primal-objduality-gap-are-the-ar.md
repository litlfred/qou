---
# qou-sof3
title: The SDP producer's primal_obj/duality_gap are the arithmetic floor, not a measurement — they track prec_bits
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:11:29Z
updated_at: 2026-09-04T09:12:07Z
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
