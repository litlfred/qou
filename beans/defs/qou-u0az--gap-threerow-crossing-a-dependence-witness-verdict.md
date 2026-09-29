---
# qou-u0az
title: 'GAP: threerow-crossing-a-dependence witness verdict contradicted its own data three ways'
status: completed
type: task
priority: normal
created_at: 2026-08-30T01:00:36Z
updated_at: 2026-08-30T03:17:59Z
---

Parent: qou-5wng. Found by reading the highest-scoring remaining flagged file in
the y_λ triage. This is the sharpest instance of the arc: a **committed,
convention-D-era, `allPassed: true` witness whose headline verdict is
contradicted three separate ways by its own data**.

## The committed verdict

    verdict:      A_DEPENDENT_crossing_above_q0
    verdict_text: "A-DEPENDENT. The n=9 crossing EXISTS but lies ABOVE q₀ —
                   the deuteron is NOT special; q₀ sits between the n=6 and
                   n=9 crossings."
    allPassed:    true    (with ZERO assertions)

## Three contradictions, all from fields in the same file

1. **"the crossing EXISTS"** — every measured F in the witness is zero:
   `F_at_qlo = F_at_q0 = '0.0'` and `sign_qlo = sign_q0 = 0`, for D, T and ³He
   alike; the character-free companion G is `0.0` at n = 6, 9, 12.

2. **"q₀ sits between the n=6 and n=9 crossings"** — `crossings_below_or_at_q0`
   is `[]` for every isotope. There is no n=6 crossing on the physical interval
   for q₀ to sit above. The printed line even rendered it as
   `crossing q: D (n=6) = []  [≤ q₀, PHYSICAL]`.

3. **"A-DEPENDENT"** — D, T and ³He all give first crossing
   **1.5378214048144982**, identical to 17 digits, and G finds the same value at
   n = 6, 9 AND 12. That is A-INDEPENDENT, and a location identical across three
   braid words, three n and two different objects is not a property of any of
   them.

## Why it happened

The verdict branches only on the diagnostic ray and on the physical interval
being EMPTY:

    n9_above = [... if diagnostic_first_crossing_above_q0 is not None]
    n9_below = [... if crossings_below_or_at_q0]
    if n9_above and not n9_below:
        verdict = "A_DEPENDENT_crossing_above_q0"

Nothing checks whether F is nonzero at all, so **an identically-zero F lands in
the A-dependent branch by construction**, the moment round-off changes sign
anywhere on the ray. The 2026-08-25 convention-D regeneration updated the
MEASUREMENTS to 0.0 and left the VERDICT.

## The measurement

Under D the Wenzl level is r = 2, so `y_λ = 0` for `ℓ(λ) > 2` **identically in
q** — the diagnostic ray does not escape it. At 70 dps, max|y_λ| over the ℓ≥3
stratum against the noise floor:

    q                       max|y| ell>=3     floor
    1.0001                  0.0               1.09e-63
    1.1099785827513808      0.0               1.15e-63
    1.5378214048144982      1.34e-72          2.08e-63   <- a "located crossing"
    2.2810884055126934      9.77e-73          4.31e-63   <- another
    4.0                     2.63e-74          7.41e-63

Nine orders below, everywhere. The located crossings are sign changes of
cancellation residue.

## NOT refuted: the convention-C result

#4829's crossing at q ≈ 1.05365 with F(q₀) = −0.1950 was a real convention-C
measurement. It is **out of frame, not wrong**. The defect is the regeneration
keeping a C-era verdict over D-era numbers.

## Fixed on PR #6033

* structural-zero guard runs BEFORE the verdict; new verdict
  `structural_zero_no_crossing_exists` with text explaining that the question
  has no answer because there is no crossing;
* the `[≤ q₀, PHYSICAL]` line prints `NONE` rather than `[]`;
* **the assertion this witness did not have** —
  `verdict_does_not_claim_a_crossing_in_a_vanishing_object`. Zero assertions is
  how `allPassed: true` sat over a refuted verdict.
* A-independence recorded as data (`diagnostic_first_crossing_by_isotope`,
  `diagnostic_first_crossing_is_isotope_INDEPENDENT: true`).

Negative control: restoring the pre-fix branch order returns the verdict to
`A_DEPENDENT_crossing_above_q0` and the witness records FAILURES.

## Noted, not changed

The script exits 0 even when an assertion fails; `allPassed` in the witness is
what carries it, which matches how this corpus reads the two honest `false`
witnesses on this same axis. Left alone rather than changing a signal other
readers may depend on.
