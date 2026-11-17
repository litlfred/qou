---
# qou-cc97
title: Formalize Wenzl-bridge decomposition for markovTrace_branching
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T18:18:23Z
updated_at: 2026-11-17T07:06:58Z
parent: qou-rtxm
---



## Round 56 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8241 (`f5d60a0cc755a36459696dc679eebd3728acc344`)
- **Module:** `QOU.Foundations.SymplecticAtomicityWenzlSemisimplicity` (`folio/quantum-observable-universe/lean/QOU/Foundations/SymplecticAtomicityWenzlSemisimplicity.lean`), wired into `QOU.lean`.
- **Theorems:** `Hecke2Element.mul_assoc`, `hecke2_T_quad`, `hecke2_T_inv_rel`, `heckeActSym_T`, `heckeActAntisym_T`, `heckeAct_quadratic_on_decomp`, `heckeSymProj_idempotent`, `heckeAntisymProj_idempotent`, `heckeSymProj_orthog_antisymProj`, `heckeAntisymProj_orthog_symProj`, `heckeProj_completeness`, `heckeAct_spectral_decomp` — proving `H_2(q)` eigenvalue decomposition (`q` on `Sym^2`, `-q⁻¹` on `Λ^2`) and complete orthogonal idempotents over a `CommRing R`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
