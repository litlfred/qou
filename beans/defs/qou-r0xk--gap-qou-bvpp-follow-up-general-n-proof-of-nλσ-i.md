---
# qou-r0xk
title: 'GAP (qou-bvpp follow-up): general-n proof of (†) n(λ)=Σ_i C(λ''_i,2) — nStatList=sumChoose2∘conjugate'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:17:19Z
updated_at: 2026-11-15T13:40:00Z
parent: qou-1oif
---

The general-n dtEuler=deltaLambda unification is LANDED in PR #4558 (DeltaLambdaDTIndexGeneralN.lean, sorry-free): the single-degree graded-Euler collapse dtEulerG_collapse (all N,d) gives dtEuler=(-1)^{n(λ)}·dim=Δ_λ for every partition, and the merged n=5 anchor (PartitionOf5.dtEuler) is subsumed (definitional bridge dtEuler_eq_dtEulerG=rfl + re-derivation via collapse).

SOLE RESIDUAL: to also match the GEOMETRIC chirality formula sgn(w0^{S_λ'})=(-1)^{Σ C(λ'_i,2)} at general n, one needs (†) n(λ)=Σ_i C(λ'_i,2), i.e. nStatList parts = sumChoose2 (conjugate parts). This is a TEXTBOOK double-counting identity (NOT open math), proved in the corpus only at n≤5 by decide (PartitionOf5.nStat_eq_sumChoose2_conj). parity_eq_w0_sign_of_nStat_eq_sumChoose2 (in #4558) closes the geometric leg CONDITIONALLY on (†).

NEXT STEP: define a general conjugate : List ℕ → List ℕ (λ'_j = #{i : λ_i ≥ j}) and prove nStatList parts = sumChoose2 (conjugate parts) by a Young-diagram / induction argument. Then the general-n geometric-chirality leg is fully unconditional. Blocked on nothing — purely a formalization task.

## Closed 2026-11-15 (owner tap, E1 bean triage)

Proved for general n: `aStat_eq_sumChoose2_conjugate` (`QOU/BraidsAndKnots/NStatConjugateGeneral.lean:215`), with `aStat` defeq to `nStatList` (per `DeltaLambdaGeneralNUnconditional.lean`). lean-direct exits 0 with no sorry.
