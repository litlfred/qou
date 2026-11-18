---
# qou-sof3
title: The SDP producer's primal_obj/duality_gap are the arithmetic floor, not a measurement — they track prec_bits
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:11:29Z
updated_at: 2026-10-04T15:25:00Z
parent: qou-5vkl
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


## Item 2 ATTEMPTED and it is a NEGATIVE — the static criterion does not decide

`computations/audits/lp_floor_valued_objective_audit.py` implements the
proposed criterion

    cancellation_decades = log10(max|x*|) - log10(|primal_obj|)
    available_decades    = prec_bits * log10(2)
    flag when cancellation > FRACTION * available

and measures that it **cannot separate floor-valued objectives from
legitimately small ones**. Two independent reasons, both measured over the
146 scorable LP/SDP dual records on `main`:

**1. The threshold is a cliff.** Same data, varying only the fraction:

    fraction   0.80  0.90  0.95  0.96  0.98  1.00  1.05
    flagged      74    62    62    62     7     7     3

55 records sit in a narrow band at ratio ~0.97, so any count between 0.90 and
0.96 is an artifact of where the threshold was placed. **The "62" I would have
reported is not a measurement.** Only ratio > 1 is threshold-free (it means the
objective is below what the arithmetic can resolve at all) and that gives 7.

**2. It misses its own confirmed positive — the decisive failure.**
`qbeta-symbolic-sdp-strict-complementarity` was PROVED floor-valued by sweeping
`prec_bits` (3.9e-44 at 167 -> 3.8e-100 at 400 -> 3.8e-196 at 800). It scores
ratio **0.97 and ranks 59 of 146** — inside the cluster, and below the
threshold-free cut. A criterion that cannot rank its one known positive above
55 unknowns is not separating anything.

**Why, structurally.** A legitimately tiny optimum and a floor-valued one are
*identical* in the published numbers. The only discriminator is whether the
objective MOVES when `prec_bits` changes, which requires re-running the
producer — deliberately not done in an audit, since producers rewrite sibling
witnesses.

**What the 7 threshold-free survivors are.** All are f64-era (no
`precision_bits`, available 16.0 decades) and **6 of the 7 live in
`computations/_deprecated/`**. The single live one is
`computations/borromean-axial-coupling.witness.json` at ratio 1.31 — the
strongest candidate in the corpus and the only one worth a sweep.

**Disposition.** The script is kept as a RANKING and as the record of this
negative, not as a detector. It prints the sensitivity sweep and its own
calibration rank on every run, so a future reader cannot quote a flag count
without seeing how much it moves. Do not build a gate on it.

**The one actionable item left:** sweep `borromean-axial-coupling` at two
precisions and see whether its objective moves. That is a single producer
re-run and it either confirms a live floor-valued objective or clears it.


## The one actionable item is CONFIRMED — `borromean-axial-coupling` was floor-valued

Swept it, as the previous entry proposed. Decisive:

    committed   primal_obj = 3.814822595553291e-16
    re-run      primal_obj = 3.5733110840282835e-44

A **28-order move**. The objective tracks the arithmetic floor, so it is
floor-valued -- a TRUE POSITIVE for the ranking, and the only live one outside
`_deprecated/`.

**Mechanism, which is `qou-dke6` exactly.** The producer already asks for
`backend="clarabel"` (line 128). The committed witness was written when the
MPFR binary was absent and the call fell through to scipy f64, before the
strict-raise guard existed. Nothing in the file said so, because the producer
cherry-picked `float(lp.primal_obj)` and dropped `backend` / `precision_bits`
entirely -- it is one of the 105 unattributable records.

**The certificate barely moved; only the objective did.** `x_star[0]` went
-265025.00781985413 -> -265025.00781985425, ~14 digits stable. That is the
cancellation signature: x* is fine, the objective is the artifact. **`g_A` did
not move at all** -- the physics conclusion is untouched.

## And a SECOND vacuous assertion, worse than the first

`lp_active_set_nonempty` read

    computed = float(len(active_set)),  expected = 1.0,  tolerance = 10.0

An EMPTY active set gives |0 - 1| = 1 <= 10 and **passes**. The assertion could
not detect the one condition it is named for. Its own comment claimed the
opposite ("passes for any non-empty active set"), which is presumably why it
survived review: the name and the comment agreed with each other, and both
disagreed with the tolerance.

Fixed to `computed=bool(len(active_set) >= 1), expected=True, tolerance=0`.
That pattern is demonstrably falsifiable in-corpus -- the SDP producer's
`selector_direction_S_independent` uses it and reports `passed=False`.

`lp_duality_gap_zero` (tolerance 1e-10 against a 1e-44 floor, passed on both
sides of the 28-order move) replaced by the certified form, tolerance derived
from the cancellation floor: computed 2.0157e-45 against 1.4167e-43.

## Generalisation worth noting

Two producers examined, two pairs of vacuous LP assertions found. That is not
a sample anyone should extrapolate from, but it does suggest the pattern
"assert a floor-valued quantity against a fixed absolute tolerance" is not
isolated. The 54 LP/SDP witnesses of `qou-dke6` are the population to check.
