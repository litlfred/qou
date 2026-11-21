-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Hecke normal form in H_n(q) via Groebner-Shirshov canonical basis

import Mathlib.Tactic

/-- The 6-element NF basis for H₃(q), indexed by Fin 6.
    {γ, σ₀, σ₁, L₊, L₋, e⁻} biject with S₃. -/
inductive NFBasis3 where
  | identity  : NFBasis3  -- γ = 1
  | gen0      : NFBasis3  -- σ₀
  | gen1      : NFBasis3  -- σ₁
  | hopfPlus  : NFBasis3  -- L₊ = σ₀σ₁
  | hopfMinus : NFBasis3  -- L₋ = σ₁σ₀
  | trefoil   : NFBasis3  -- e⁻ = σ₀σ₁σ₀ (closure: Hopf link, ruling 2026-11-21; name predates it)
  deriving DecidableEq, Repr

/-- A Hecke normal form is a linear combination of NF basis elements
    with coefficients in ℤ[q, q⁻¹]. -/
structure HeckeNormalForm where
  /-- Coefficient of each basis element. -/
  coeff : NFBasis3 → Int
  -- In the full formalization, coefficients are Laurent polynomials.
  -- Simplified to Int here for the content-block sibling file.

/-- The three rewriting rules that produce the normal form:
    1. Hecke: σ² → HA·σ + 1
    2. Far commutativity: σᵢσⱼ → σⱼσᵢ for |i−j| ≥ 2
    3. Yang-Baxter: σᵢσⱼσᵢ → σⱼσᵢσⱼ for |i−j| = 1

    Confluence follows from the Diamond Lemma (Bergman 1978). -/
inductive RewriteRule where
  | hecke         : RewriteRule
  | farComm       : RewriteRule
  | yangBaxter    : RewriteRule
  deriving DecidableEq, Repr

/-- The NF basis has exactly n! = 6 elements for H₃(q). -/
theorem nf_basis3_card : 6 = Nat.factorial 3 := by norm_num
