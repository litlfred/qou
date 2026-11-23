---
# qou-awxv
title: 'PR #9180: CFT/holography review — Frobenius tower, Jones index, charge Cartan; next L_cal route 1'
status: todo
type: task
created_at: 2026-11-23T21:14:34Z
updated_at: 2026-11-23T21:14:34Z
---

Thread: CFT/holography review (owner ofri, 2026-11-23). Branch claude/project-thread-p6bqaz, PR #9180, issue #9179. Head ae490aa67e (main merged). NOT merged: owner's explicit go required.

Done, all sorry-free, lean-library-sweep GREEN (79 QOU.QuantumObservableUniverse modules + SweedlerFrobenius):
- SweedlerFrobenius.lean: H4 Frobenius, Nakayama nu, not symmetric when 2 is a unit.
- NakayamaTwist.lean: frobMap, twisted adjunction, nu_dag bar law.
- HigmanNormMap.lean, QExteriorCR.lean (d_q preserves CR structure).
- TwistedFrobeniusTower.lean: finite-level tower, boundary->bulk compat.
- TowerDerivations.lean: E adjoint to iota is unique, a left inverse of iota, left-linear, trace-preserving; Nakayama twists commute with iota (given right-linearity); Schur-Weyl blindness lemma.
- JonesIndexConventionD.lean: convention D = Jones TL trace, index [2]_q^2 >= 4 (Jones positivity cited).
- ChargeCartanCommutant.lean: two strands; K(x)K commutes with braid, K(x)1 does not.
- Content: F1/F4/F5 rescopes, Ch1 DHR/CQM paragraph, Ch13 CR-lift prose; 7 new refs with DOIs UNVERIFIED.
Review docs: /mnt/project-files/cft-holography-review/ (referee-review.md, prior-art-cqm-dhr-and-kerr-review.md, charge-compton-deep-analysis.md).

Open / next:
1. L_cal route 1 (owner pick 2026-11-23): Delta_EM = alpha * m_model * f. Pre-register f from the Borromean geometry BEFORE computing anything; report even a miss. Needs f ~ 0.1. No m_pi unit.
2. check-sidecars: one mass-figure allowlist hit to triage; block-manifest-audit could not run (missing platform module value-registry-di).
3. Verify DOIs of the 7 new references.
4. Lean: n-strand K^n commutes with every R_i; test Y = writhe for the p and n words; existence of the adjoint E.
5. Kadison and Jones 1983 are cited without bib keys; add them.
6. FrobeniusHopfData conflates the Frobenius Delta with the Hopf Delta and assumes S^2 = id. Flagged, not changed.
