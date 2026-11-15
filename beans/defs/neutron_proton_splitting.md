---
# neutron_proton_splitting
title: neutron proton splitting missing hypotheses
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-15T14:30:00Z
---

File: `folio/quantum-observable-universe/lean/QOU/Torsion/neutron_proton_splitting.lean`
The `neutron_proton_splitting` theorem is unprovable. Its class lacks constraints on the data fields and has `*_unconstrained_false` lemmas proving that the conclusion is independent and refutable from the provided data alone.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: 1be9bf9ec0 "resolve neutron_proton_splitting — add mass_formula + codata_agreement fields". FLAG: a codata_agreement field puts an empirical comparison inside a Lean class; 4 main commits



Also known as `npsp` (its former front-matter header id; the beans CLI uses the filename id `neutron_proton_splitting`). Recorded 2026-10-04.



## Reopened 2026-10-04 (review of PR #7496)

The closing evidence (1be9bf9ec0) resolves the missing hypotheses by adding a `codata_agreement` field, which places an empirical comparison inside a Lean class. The owner's rule keeps empirical values out of formal statements, so this is not closed on that evidence. Owner decides how the hypotheses should be supplied. No content was changed.

## 2026-11-15 — completed (owner decision card: "Move them to comparison notes")

The CODATA comparison is out of Lean. `neutron_proton_splitting` now states only the
model value `α·|Φ(udd) − Φ(uud)| = 3.7449·0.3476 = 1.30172724`, and
`codataNeutronProtonSplittingMeV` is deleted (no other Lean consumer). The comparison
(+0.65 % against CODATA 2022 1.29333378 MeV) is in the block's **Comparison with
measurement** paragraph. That replaces two inconsistent figures: 0.63 % in the old
prose and 0.68 % in the old Lean (against the rounded 1.293).
Verified with `lean -DautoImplicit=false -s 65536`: exit 0. Axioms are
`[propext, Classical.choice, Quot.sound]` only. Still open, but not this bean: porting
the closed-form traced volumes so that the numeric pins become theorems.

## 2026-11-15 — convention D (owner ruling: replace C values with D even if worse)

PR #7927 now states convention-D values in both neutron–proton blocks
(mass-theory/neutron-proton-splitting and observations/neutron-proton-mass-splitting
+ proof): Phi(uud) = -0.6148859839, Phi(udd) = -0.8963949769, |dPhi| = 0.2815089929
(50 dps, z = q^3/(q^2+1), proton q0, all-pairs strand pairing of level1-qvalues.py),
model value 1.0542 MeV (alpha 3.7449) / 1.0541 MeV (alpha 3.7445), -18.5 % vs CODATA.
The C figure (+0.65 %) is kept only as a labelled historical comparison.
hecke_engine.HeckeRational.z is now exact convention-D q^3/(q^2+1).
The adjacent-crossing reading (pn_splitting_proof_provenance_probe.py) gives -2.875 %
under D but does not reproduce the old neutron C value; not adopted.
