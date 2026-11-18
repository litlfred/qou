---
# qou-k6is
title: 'FLAG: DerivedAtom.confinement_universality is definitional (polarization argument discarded)'
status: in-progress
type: task
tags:
    - quark-state
created_at: 2026-11-15T08:17:22Z
updated_at: 2026-11-15T08:17:22Z
parent: qou-qs0e
blocking:
    - qou-qs2u
---

From qou-qs2u, PR #7825. QOU/Interactions/DerivedAtom.lean:126-158 defines crossingCoeffsWithPol ct _ := crossingCoeffs ct and then proves independence of the polarization by simp. It is true by definition and says nothing about the gamma-gamma chain. Not edited (owner ask rule). Options: scope it as a definitional remark, or route it through the flavour-extraction map once that exists.

## Progress (PR #8452)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PolarizationArgumentDiscardDecayWindowFractionSurprisalVolumeTermStepUnitDomainWallDilution.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_k6is_kh7e_lsvj_mumr_qjh8_probe.witness.json` (`Commit 1` = `ffa2d78ef5414a49bba12e0efccca6fbb72626d5`, `HEAD` = `078aa49b3db67c82ebbd4ebd6bd00b088ab2f9d9`).
