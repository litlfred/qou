---
# qou-x631
title: 'EPIC: prove the Δ_λ covariance kernel Cov_Planch(f^λ,Σc²)≤0'
status: in-progress
type: milestone
priority: normal
created_at: 2026-07-18T19:55:42Z
updated_at: 2026-07-24T16:16:55Z
---

## Goal
Prove `cov(k) = Σ_{λ⊢k} (f^λ)³ (Σ_□c(□)² − C(k,2)) ≤ 0` (⇔ `T₃(k)=Σ_λ(f^λ)²χ^λ(3-cyc) ≤ 0`
⇔ `Cov_Planch(f^λ, Σc²) ≤ 0`) — the sole open input of the Δ_λ super-exp growth bound
(`WstdSuperExpBound.lean`, via `DeltaLambdaDReduction.D_of_T3_nonpos`, sorry-free). Growth bound
⇒ `k(A)=O(log A)` (GAP-A-3). Carried as `YoungDiagramKernel.covariance_kernel_conjecture` (§3b open).

## Status
- **Phase 0 (done, #3939/#3959/#3998):** reduction (D)→kernel; free-cumulant framing `Σ̂₃=R₄+R₂`,
  `E_Planch[R₄]=−k`; sorry-free Lean reduction; verified k≤40; faithful Lean statement.
- **Phase 1 (done, #4008):** eliminated (1) holonomic recurrence (not P-recursive, k≤28);
  (2) β-monotonicity (E_β[C₂] increases 4→5).
- **Phase 2 (done, THIS branch):** eliminated (3) sub-family sign-definiteness (two-row flips + at
  k=6, hook at k=4); (4) Murnaghan–Nakayama peeling (B(ν)=Σ_{λ/ν=BS₃}(−1)^ht(f^λ)² first >0 at the
  self-conjugate staircase ν=(3,2,1), k=9); (5) no tabulated closed form (both |T₃|,|cov| OEIS-absent
  through k=18). Pinned R₄=3ω₃−k affine (not a new lever), Lean-carried sorry-free (`r4WeightedSum_eq`).
- **Phase 3 (open):** Śniady genus expansion on the `(f^λ)³`-biased measure. Obstruction: `f^λ` is the
  exponential DIMENSION, not a bounded character ratio ⇒ Kerov-CLT/Ivanov–Olshanski not direct.

## Coordination
- DEPENDS on Specht/S_n Lean epic `sp00` + #4110/#4114/#4126 for any Lean proof of the kernel.
- Feeds Δ_λ vector V5 of keystone map #4058; growth bound = GAP-A-3 magnitude leg behind binding
  B_gate work (#4132/#4135/#4136).
- Phase-3 lead: RSK form `T₃=Σ_{w∈S_k}χ^{sh(w)}(3-cycle)` + Śniady genus expansion; or a bespoke
  second-moment identity for `Cov_Planch(f^λ, Σ_3)`.
