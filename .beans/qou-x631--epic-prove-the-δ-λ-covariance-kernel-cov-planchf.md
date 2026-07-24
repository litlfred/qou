---
# qou-x631
title: 'EPIC: prove the Δ_λ covariance kernel Cov_Planch(f^λ,Σc²)≤0'
status: in-progress
type: milestone
priority: normal
created_at: 2026-07-18T19:55:42Z
updated_at: 2026-07-24T15:51:17Z
---

## Goal
Prove `cov(k) = Σ_{λ⊢k} (f^λ)³ (Σ_□c(□)² − C(k,2)) ≤ 0` (⇔ `T₃ ≤ 0` ⇔ `Cov_Planch(f^λ, R₄) ≤ 0`)
— the sole open input of the Δ_λ super-exp growth bound (`WstdSuperExpBound.lean`, via
`DeltaLambdaDReduction.D_of_T3_nonpos`, sorry-free). Growth bound ⇒ `k(A)=O(log A)` (GAP-A-3).

## Status
- **Phase 0 (done, merged #3939/#3959/#3998):** reduction (D)→kernel; free-cumulant framing
  `Σ̂₃=R₄+R₂`, `E_Planch[R₄]=−k`; sorry-free Lean reduction; verified k≤40; faithful Lean
  statement `YoungDiagramKernel.covariance_kernel_conjecture` (positive-controlled).
- **Phase 1 (done, merged #4008):** eliminated two proof routes — (1) NOT P-recursive
  (no holonomic recurrence, k≤28); (2) NOT β-monotone (E_β[C₂] increases 4→5). Kernel is a
  special analytic β=2→3 fact.
- **Phase 2 (open):** Śniady genus expansion of the joint character cumulants on the
  `(f^λ)³`-biased measure. Obstruction: `f^λ` is the exponential DIMENSION, not a bounded
  character ratio ⇒ standard Kerov-CLT/Ivanov–Olshanski not directly applicable.

## Coordination (2026-07-24 week-review)
- **DEPENDS on the Specht/S_n Lean epic `sp00`** + PRs #4110 (abstract Ocneanu cyclicity),
  #4114 (Wenzl Wedderburn), #4126 (Markov inductive) — these build the S_n character / Specht
  Lean infrastructure a *Lean* proof of the kernel would need. Coordinate before Lean-proving.
- **Feeds the Δ_λ vector V5 of the keystone attack map #4058** (Δ_λ per-partition closure);
  the growth bound is the GAP-A-3 magnitude leg behind the binding B_gate work (#4132/#4135/#4136).
- Next-session Phase-2 lead: literature check (is the covariance a known Fulman/Śniady result?)
  → then genus-expansion attack via the RSK form `T₃=Σ_{w∈S_k}χ^{sh(w)}(3-cycle)`.
