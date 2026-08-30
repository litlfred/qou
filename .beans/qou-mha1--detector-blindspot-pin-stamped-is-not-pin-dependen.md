---
# qou-mha1
title: 'detector blindspot: pin-STAMPED is not pin-DEPENDENT (symbolic payloads)'
status: todo
type: task
priority: normal
created_at: 2026-08-30T09:20:24Z
updated_at: 2026-08-30T09:20:25Z
---

Found while working the one remaining stage-2 hit from
`pin_straddle_unguarded_audit`. It was a FALSE POSITIVE OF MY OWN DETECTOR,
and I came close to "fixing" correct code to satisfy it — the mirror of the
peel_map error on PR #6132, where I made a cross-check tautological while
repairing it.

## The case

    computations/mass_formula_6term_mpfr_50dps.py   pins proton
        loads habiro-coefficients-extended.witness.json   (stamped muon)

Reported as a straddle. It is not. The artifact's payload is a SYMBOLIC
Habiro expansion:

    a_m = "768"
    a_m = "-35712*u - 35712"
    a_m = "491861*u**2 + 503768*u + 515411"      all_integral: true

Polynomials in `u` with integer coefficients, and the data rows carry NO q
stamp at all. `term_6_via_habiro_coeffs_mp` evaluates them at
`u_0 = q_0^{1/2}` from its OWN runtime pin, so reading them at the proton pin
is correct.

## The general lesson

The witness's top-level q stamp records THE RUN THAT PRODUCED the symbolic
object, not a frame the data lives in. Stage 2 compares producer-anchor to
artifact-stamp, so it cannot distinguish **pin-STAMPED** from
**pin-DEPENDENT** — an artifact can carry a pin it does not depend on.

That is the eighth false-positive mechanism for this detector, and the first
that would have caused a WRONG EDIT rather than just noise.

## The fix

`_payload_is_pin_independent` — evidence, not an allow-list: symbolic
coefficient strings in the payload plus an `all_integral` marker. Deliberately
narrow. A numeric artifact that merely contains one such string will not
match; a symbolic artifact whose consumer nonetheless needs the stamp WOULD be
wrongly exempted, and if that appears the test should be tightened there
rather than by adding the producer to a list, which would hide the reason.

Verified: stage 2 goes 1 -> 0, and `--selftest` still PASSes, so the exemption
does not swallow the two known straddles it was built to catch.

## Not established

Whether other pin-stamped artifacts in the corpus are similarly
pin-independent. I checked this one because the detector pointed at it; I have
not swept for the class. A symbolic-payload witness read by a differently
pinned producer would look identical to a straddle under the old rule, so
there may be more of these — in either direction.
