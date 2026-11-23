---
# qou-awxv
title: 'PR #9180: CFT/holography review — Frobenius tower, Jones index, charge Cartan; next L_cal route 1'
status: in-progress
type: task
priority: normal
created_at: 2026-11-23T21:14:34Z
updated_at: 2026-11-23T23:52:44Z
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

EOS 2026-11-23 (PR #9219, HEAD 23ab7c141ec): Executed item 1 (L_cal Route 1: Delta_EM = alpha_q(q_0) * m_model(q_0) * f, NO m_pi unit, pre-registered in 68df40f7a41 prior to evaluation; alpha_q*m_model = 6.846931 MeV, empirical target f_emp ~ 0.111-0.146). Full 80-dps results across all 11 pre-registered shapes f: f_R1_1a=1/9=0.11111 (0.76077 MeV, matches Cottingham 0.76 MeV), f_R1_1b=1/(3[3]_q)=0.10952 (0.74985 MeV), f_R1_1c=1/6=0.16667 (1.14116 MeV, +0.88 sigma vs BMW 1.00(16) MeV), f_R1_2c=Vol(4_1)/(24G)=0.09234 (0.63223 MeV), Compton-HO f_R1_3a..c=0.05644-0.08465 (0.38641-0.57962 MeV), pure Borromean O2/volume f_R1_2a,2b=0.04549-0.04584 (0.31146-0.31385 MeV), Planck-defect hbar_q/3=0.03303 (0.22614 MeV), and O(hbar_q^4) connected Hecke trace f_R1_3d=0.000431 (0.00295 MeV, 250x miss).

2026-11-23 (Worker 24): Items 3 and 5 prepared on `claude/prior-art-doi-verified-pkg-20261123` (`63446514c77`, awaiting owner OK per `qou-cvu9`): all 7 `#9180` DOIs live-verified on Crossref + `doi.org`, and `kadison1999` (10.1090/ulect/014) + `jones1983` (10.1007/BF01389127) added and wired into `TwistedFrobeniusTower.lean`, `JonesIndexConventionD.lean`, and Ch. 2 `substrate-preamble`.
