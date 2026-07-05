import Mathlib.Tactic

/-!
# QOU.AlgebraicSubstrate.QChebyshevFunction

**Canonical declaration** for content block at
[`quantum-observable-universe/q-geometric-langlands/q-chebyshev-function.ts`](quantum-observable-universe/q-geometric-langlands/q-chebyshev-function.ts).

Formalises the manuscript **definition** of the q-Chebyshev function
`ψ_q(X)` — the partial sum of the q-von Mangoldt weights over the maximal
ideals of norm `≤ X` (the `q`-deformed prime-counting function).
-/

open Classical

namespace QOU.AlgebraicSubstrate

/-- Data for the q-Chebyshev function `ψ_q`.

    A `definition` carrier: over a finite collection `ideals` of maximal
    ideals with norm `N` and q-von Mangoldt weight `Lambda_q`, `psi_q X`
    is pinned to the sum of the weights over those ideals of norm `≤ X`. -/
structure QChebyshevFunction where
  /-- Index type for the maximal ideals `𝔪`. -/
  Idx : Type
  /-- Norm `N(𝔪)`. -/
  N : Idx → ℝ
  /-- q-von Mangoldt weight `Λ_q(𝔪)`. -/
  Lambda_q : Idx → ℝ
  /-- The finite collection of ideals summed over. -/
  ideals : Finset Idx
  /-- The q-Chebyshev function. -/
  psi_q : ℝ → ℝ
  /-- Defining identity: `ψ_q(X) = Σ_{N(𝔪) ≤ X} Λ_q(𝔪)`. -/
  psi_def : ∀ X,
    psi_q X = ∑ m ∈ ideals.filter (fun m => N m ≤ X), Lambda_q m

-- Ref: [manuscript] quantum-observable-universe/q-geometric-langlands/q-chebyshev-function.ts

/-- Below the smallest norm the count is empty: if every summed ideal has
    norm exceeding `X`, then `ψ_q(X) = 0`. -/
theorem QChebyshevFunction.psi_eq_zero_of_lt
    (ψ : QChebyshevFunction) (X : ℝ)
    (h : ∀ m ∈ ψ.ideals, X < ψ.N m) : ψ.psi_q X = 0 := by
  rw [ψ.psi_def X]
  apply Finset.sum_eq_zero
  intro m hm
  rw [Finset.mem_filter] at hm
  exact absurd hm.2 (not_le.mpr (h m hm.1))

end QOU.AlgebraicSubstrate
