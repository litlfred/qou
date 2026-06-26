import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Unit-modulus eigenvalues on V_{(2,1)} and Borromean fixed point

## Main results

1. **Hecke determinant**: `det(σ) = q·(−q⁻¹) = −1` on every 2-dim
   Wedderburn block (the eigenvalues of `σ` are `q`, `−q⁻¹`).
2. **Even-length determinant**: a product of `2k` generators has
   `det = (−1)^{2k} = 1`, so its eigenvalues satisfy `λ₁λ₂ = 1`
   (the unit-circle condition together with `|tr| ≤ 2`).
3. **Borromean fixed point**: the Borromean braid
   `β_Bor = (σ₁σ₂⁻¹)³` has the degenerate eigenvalue `λ = −1` on
   `V_{(2,1)}`.

## Disposition (integrity)

The previous version carried two `def … : True := trivial`
placeholders (`borromean_trace_21_eq_neg_two`,
`all_positive_trace_positive`) — vacuous, and forbidden by AGENTS.md
§1a. They are removed. The genuine algebraic content is proved:
`hecke_generator_det_neg_one` (generic field), `even_braid_det_one`,
and `borromean_eigenvalue_neg_one` (now concludes `λ = −1`, not merely
the discriminant). The rep-theory inputs those placeholders gestured
at — that `tr_{(2,1)}(β_Bor) = −2` (Hoefsmit seminormal rep /
`BorromeanMarkovTrace.lean` closed form) and that all-positive braids
have `0 < tr < 2` — are **not** formalised here (they need the Hoefsmit
matrix infrastructure); they enter `borromean_eigenvalue_neg_one` as
the explicit hypotheses `tr = −2`, `det = 1`, so the eigenvalue
conclusion is a genuine *conditional* on those inputs, not a vacuous
assertion.

## Base ring (§7c)

The determinant/eigenvalue facts are pure field identities, so they are
stated over a generic `{R : Type*} [Field R]`; only the integer
determinant `(−1)^{2k}` uses `ℤ`. No archimedean structure is needed —
`|λ| = 1` is the narrative reading of `λ₁λ₂ = 1` with `|tr| ≤ 2`, not a
Lean hypothesis here.

-- Ref: [manuscript] Hecke algebra Wedderburn decomposition
-/

namespace QOU.BraidsAndKnots

/-! ## Hecke generator determinant -/

/-- The Hecke relation `σ² = h·σ + 1` forces `det(σ) = −1` on every
    2-dimensional Wedderburn block: the eigenvalues of `σ` are `q` and
    `−q⁻¹` (roots of `x² − h·x − 1`), with product `q·(−q⁻¹) = −1`.
    Generic over any field (pure field identity, §7c). -/
-- Ref: [manuscript] Iwahori-Hecke algebra, det on standard rep
theorem hecke_generator_det_neg_one {R : Type*} [Field R] {q : R} (hq : q ≠ 0) :
    q * (-q⁻¹) = -1 := by
  rw [mul_neg, mul_inv_cancel₀ hq]

/-! ## Unit modulus for even-length braids -/

/-- A product of an even number `2k` of Hecke generators on `V_{(2,1)}`
    has determinant `(−1)^{2k} = 1` (each generator contributes `−1`).
    Together with `|tr| ≤ 2` this is the unit-circle condition
    `λ₁λ₂ = 1`. -/
-- Ref: [manuscript] det(σ₁···σ_{2k}) = (−1)^{2k} = 1
theorem even_braid_det_one (n : ℕ) : (-1 : ℤ) ^ (2 * n) = 1 := by
  simp [pow_mul]

/-! ## Borromean eigenvalue -/

/-- **Borromean eigenvalue is `−1`.** If `λ` is an eigenvalue of
    `ρ_{(2,1)}(β_Bor)` — a root of the `2×2` characteristic polynomial
    `λ² − tr·λ + det` with the Borromean data `tr = −2`, `det = 1` —
    then `λ = −1` (the degenerate fixed point).

    Over any field the characteristic polynomial is `(λ + 1)²`, and a
    field has no zero divisors, so `(λ + 1)² = 0 ⇒ λ + 1 = 0 ⇒ λ = −1`.
    The data `tr = −2` is the Hoefsmit / Markov-trace input (carried as
    a hypothesis, not asserted here); `det = 1` is `even_braid_det_one`
    for the 6-generator word. -/
-- Ref: [manuscript] BorromeanMarkovTrace.lean closed form (tr_{(2,1)}(β_Bor) = −2)
theorem borromean_eigenvalue_neg_one {R : Type*} [Field R]
    (lam tr det : R) (h_tr : tr = -2) (h_det : det = 1)
    (h_root : lam ^ 2 - tr * lam + det = 0) : lam = -1 := by
  subst h_tr; subst h_det
  have hsq : (lam + 1) * (lam + 1) = 0 := by linear_combination h_root
  have h1 : lam + 1 = 0 := mul_self_eq_zero.mp hsq
  linear_combination h1

end QOU.BraidsAndKnots
