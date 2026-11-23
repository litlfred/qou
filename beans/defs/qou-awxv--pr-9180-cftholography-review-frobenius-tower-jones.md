---
# qou-awxv
title: 'PR #9180: CFT/holography review — Frobenius tower, Jones index, charge Cartan; next L_cal route 1'
status: in-progress
type: task
priority: normal
created_at: 2026-11-23T21:14:34Z
updated_at: 2026-11-23T21:43:54Z
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


2026-11-23 21:15Z: since ae490aa67e, main took #9184 (gravity-spacetime.ts, where this PR also adds a block), #9199 and #9187 (folio/schema/references.ts, references.bib, QOU.lean). Expect conflicts in gravity-spacetime.ts and references.ts ORDER. Merge origin/main (do not force-push), keep both sides' blocks and refs, then re-run lean-library-sweep.


2026-11-23 21:16Z: PR #9180 MERGED (rebase) at head 832835c9f5 by owner's prepare-merge-auto; the rebase note above is obsolete. Open items 1-6 remain.

Item 1 (L_cal Route 1: Delta_EM = alpha * m_model * f, no m_pi unit) pre-registered prior to numerical evaluation in 68df40f7a41 on claude/w10-continuum-ecat-intranuc-em-20261123 (Worker 18, 2026-11-23).
