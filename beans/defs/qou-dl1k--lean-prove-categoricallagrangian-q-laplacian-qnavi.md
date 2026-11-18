---
# qou-dl1k
title: Lean-prove CategoricalLagrangian -> q-Laplacian / QNavierStokes -> MassTraceIdentity / MassTraceMarkov -> Two-Term Nucleon Splitting Bridge over real QOU types
status: in-progress
type: task
priority: high
tags:
    - lean
    - derivation-chain
created_at: 2026-11-18T19:52:23Z
updated_at: 2026-11-18T19:52:23Z
parent: qou-7xl8
---

In `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/CategoricalLagrangianTwoTermBridge.lean` (importing `QOU.QuantumObservableUniverses.QDifferentialGeometry`, `QOU.Torsion.MassTraceIdentity`, `QOU.Torsion.MassTraceMarkov`, and `QOU.MassTheory.NeutronProtonEMSign`):
1. Prove directly on `QOU.CategoricalDiracOperator` and `QOU.CategoricalLagrangian` in any `R`-linear preadditive category `C` (`[Category C] [MonoidalCategory C] [BraidedCategory C] [Preadditive C] [Linear R C]`) that:
   - `dirac.dirac ≫ dirac.dirac` expands bilinearly in `End_C(fh.obj)` into the 3-term `q`-Laplacian morphism sum `qinv² • (nabla ≫ nabla) + (qinv * (1 - qinv)) • (nabla ≫ reeb + reeb ≫ nabla) + (1 - qinv)² • (reeb ≫ reeb)`,
   - `lagrangian` expands into the 5-term morphism sum in `End_C(fh.obj)` combining the 3-term bosonic square and the 2-term fermionic matter coupling `qinv • (costate ≫ state ≫ nabla) + (1 - qinv) • (costate ≫ state ≫ reeb)`,
   - Any `R`-linear trace functional `τ : (fh.obj ⟶ fh.obj) →ₗ[R] R` maps `L.lagrangian` to the two-term additive sum `τ(𝒟_∇²) + τ(ψ* ⊗ 𝒟_∇ψ)`, and for two states `(ψ_n, ψ_p)` sharing the same connection `∇`, the bosonic term `τ(𝒟_∇²)` cancels in `τ(ℒ_q(∇, ψ_n)) - τ(ℒ_q(∇, ψ_p))` or isolates the spin-braid + charge-asymmetric difference!
2. Connect via `MassTraceIdentity` (`yekutieli2015`, `broda2002`) and `MassTraceMarkov` (`pimsner-popa-1986`, `jones2015vonneumann`) to `NeutronProtonEMSign`.
3. NO fake `Int`/`Bool` wrapper structs without `QOU` imports! If any sub-bridge is open, document the exact remaining Lean goal state on this bean.
