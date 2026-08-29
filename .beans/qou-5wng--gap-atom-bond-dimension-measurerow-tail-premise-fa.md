---
# qou-5wng
title: 'GAP: atom_bond_dimension_measure.row_tail — premise false under D, float64 q0 cast, and it never ran'
status: todo
type: task
priority: normal
created_at: 2026-08-29T21:47:28Z
updated_at: 2026-08-29T21:48:00Z
---

FOUND 2026-08-29 via the witnessless-consumer list added to
`computations/audits/ylambda_threerow_frame_audit.py` on this branch. This file
emits no witness, so layers 2 (numeric) and 3 (dating) were both blind to it —
it is the seventh instance of the convention-D annihilated-stratum class, and
the first one that list caught.

## Three defects in one function, and the third explains the other two

`row_tail()` in `computations/atom_bond_dimension_measure.py`:

**1. Its stated premise is false under convention D.** The docstring opened
*"y_λ is the Wenzl PRINCIPAL Schur specialization (canonical Jones–Markov trace,
NONZERO FOR ALL λ)"*. Under D the Wenzl level is `r = 2`, so `y_λ = 0` exactly
for every partition with ≥3 rows. Measured at the proton pin: `max|y_λ|` over
the ℓ≥3 stratum is **0.0** at n=6 and n=9, against 0.115 and 0.0221 over all λ.

**2. `float(Q0)` fed a float64 into a computation.** Line 76 read
`y = y_lambda_at(n, float(Q0))` — the cast drops the 50-digit pin at digit 17
(`1.1099785827513808` against `1.109978582751380807591669…`). Not a display; the
value goes straight into the weight computation. NO-FLOAT64 applies to probes
exactly as to producers.

**3. IT NEVER RAN.** `y_lambda_at` is imported **nowhere** in the module — not at
module scope, not locally. `row_tail()` raised
`NameError: name 'y_lambda_at' is not defined` at its first atom, on every
invocation of `main()`. Note this is a genuine defect and not one of this
corpus's designed refusals: no guard the import cone defines raises `NameError`.

Defect 3 is why 1 and 2 survived the convention-D migration. A function that
always crashes is never read for its numbers, so nobody re-checked its claims.

## What the numbers actually are

Repaired (import added, `Q_MP` instead of `float(Q0)`), run end to end, exit 0:

    ROW-TAIL (>r-row contribution to |tr_M|, dps=40):
      atom     <=2 miss    <=3 miss    <=4 miss   free <=3 miss
      D      0.000e+00   0.000e+00   0.000e+00    0.000e+00
      3He    0.000e+00   0.000e+00   0.000e+00    0.000e+00
      4He    0.000e+00   0.000e+00   0.000e+00    0.000e+00

Identical at float64 and at 50 dps, so exact rather than a precision artifact.
The docstring claimed **0.2–3.4 %, growing with A**.

## The two claims, scoped separately — they do NOT fare the same

* *"the ≤3-row SU_q(3) restriction is a DIFFERENT trace, a 0.2–3.4 % error
  growing with A, invalid at the 1-ppQ floor"* — those figures are
  convention C and are kept in the file labelled as such. Under D the ≤2-row
  truncation is already exact, so **this measurement supports no error and no
  invalidity verdict**. The verdict may hold on other grounds; it does not
  follow from here. Scope (a).
* *"the free reference also carries >3-row content (≥ the atom's), refuting
  'binding lives in >3-row sectors'"* — the **conclusion survives** and is
  stronger under D (those sectors carry no weight at all), but the **evidence
  is now false**: neither atom nor free reference carries any >3-row content,
  so "≥ the atom's" compares two zeros. Do not cite this function as the
  measurement behind that refutation.

## Blast radius — measured, and it is one file

`structural()` and `numerical()` do **not** call `y_lambda_at` (one counts
Bratteli support, the other counts nonzero χ^λ), so the headline verdict
`χ_eff(k) = p(3k)` / the p(3A) wall is intrinsic is **unaffected**, and
`docs/audits/2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md` does not
carry the row-tail figures (checked). A corpus grep for the distinctive
phrasing and for `0.2–3.4` finds no other carrier.

## Done on this branch (PR #6033)

Import added; `float(Q0)` → `Q_MP`; docstring rewritten to state the D
measurement, keep the C figures labelled as convention C, and re-scope both
claims; `main()`'s summary lines corrected. Runs end to end, exit 0.

## Still open

Whether the *conclusion* "the ≤3-row SU_q(3) restriction is invalid at the
1-ppQ floor" is true on other grounds. This file no longer supports it, and I
have not looked for another support. That is the honest residue.
