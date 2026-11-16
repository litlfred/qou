---
# qou-mha1
title: 'detector blindspot: pin-STAMPED is not pin-DEPENDENT (symbolic payloads)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:20:24Z
updated_at: 2026-10-04T15:18:49Z
parent: qou-2002
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


## Progress Update — 2026-11-16 (PR litlfred/qou#8176)

- **Lean 4 Formalization (`0` `sorry`, `0` vacuity audit hits/advisories)**:
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/MuonAnchorInversionAndStraddleClassification.lean` (wired into `QOU.lean`) proves:
    - `cal2MuonQ_roundtrip_and_excess`, `cal2MuonQ_secant_and_rel_shift`, and `cal2MuonQ_strict_three_value_ordering` (`qou-5op4`)
    - `crossAnchor_drift_magnification_and_inv_hbar_sq_secant` (`qou-72rd`)
    - `habiroSymbolicPayload_stamp_independent_and_secant` (`qou-mha1`)
    - `markovZD_over_markovZC_and_diff` and `fourMethod_straddle_cross_ratio_and_rel_delta` (`qou-3zby`, `qou-dau6`)
- **50-dps Verification Probe & Witness (`0` raw `float64` fields)**:
  - `computations/probes/muon_anchor_inversion_and_straddle_classification_probe.py` -> `computations/probes/muon-anchor-inversion-and-straddle-classification-probe.witness.json` (`allPassed: true`, 4/4 assertions, `scriptHash: 3b8c800c79a2`, `scriptCommitSha: 80719a03fb31a87a5718702e605db5cbed1f57ce`).
- **PR**: `litlfred/qou#8176` (`0e75c0ddb6a55fd2ce17a4041ac822379106c89c`).
