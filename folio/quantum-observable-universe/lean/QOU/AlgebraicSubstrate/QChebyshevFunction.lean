import Mathlib.Tactic

/-!
# QOU.AlgebraicSubstrate.QChebyshevFunction

**Canonical declaration** for content block at
[`quantum-observable-universe/q-geometric-langlands/q-chebyshev-function.ts`](quantum-observable-universe/q-geometric-langlands/q-chebyshev-function.ts).

Formalises the manuscript **definition** of the q-Chebyshev function
`ψ_q(X)` — the partial sum of the q-von Mangoldt weights over the maximal
ideals of norm `≤ X` (the `q`-deformed prime-counting function).

**Base ring (AGENTS.md §7c) — `ℝ` here is correct, not a gratuitous
specialisation.** Two independent archimedean ingredients pin it:

1. *The summands.* `Lambda_q` is the q-von Mangoldt weight of
   `QOU.AlgebraicSubstrate.QVonMangoldtFunction`, which is `ℝ`-valued **by
   design** — its defining value `(N 𝔪 ^ ℏ_q − 1)/ℏ_q` is a **real power**
   (`Real.rpow` with the real exponent `ℏ_q`), as that module's own §7c note
   records. A sum of legitimately-`ℝ` weights is legitimately `ℝ`.
2. *The cut-off.* `psi_def` sums over `ideals.filter (fun m => N m ≤ X)` — an
   **ordering** on the norms. Ordering is archimedean content (§7c reserves
   `ℝ` for exactly this), and it is the definitional content of a
   prime-counting partial sum, not an incidental convenience.

So this block sits on the observation side of the substrate→archimedean wall.
Generalising it to `{R : Type*} [CommRing R]` would be unfaithful: it would
have to drop either the real power in the weights or the order relation in the
cut-off. Recorded here so §7c sweeps stop re-flagging the file — it reads as a
bare `ℝ`-typed algebraic-namespace module unless the reason is written down.
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

-- Ref: [leitner2026] quantum-observable-universe/q-geometric-langlands/q-chebyshev-function.ts

/-- Below the smallest norm the count is empty: if every summed ideal has
    norm exceeding `X`, then `ψ_q(X) = 0`. -/
theorem psi_eq_zero_of_lt
    (ψ : QChebyshevFunction) (X : ℝ)
    (h : ∀ m ∈ ψ.ideals, X < ψ.N m) : ψ.psi_q X = 0 := by
  rw [ψ.psi_def X]
  apply Finset.sum_eq_zero
  intro m hm
  rw [Finset.mem_filter] at hm
  exact absurd hm.2 (not_le.mpr (h m hm.1))

end QOU.AlgebraicSubstrate
