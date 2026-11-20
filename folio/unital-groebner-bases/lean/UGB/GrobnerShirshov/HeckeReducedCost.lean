import UGB.GrobnerShirshov.HeckeCompletion
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

/-!
# Hecke cost of the normal form, and the trace bound it gives

`heckeCost` is the `ℓ¹` norm of an element's coefficients. Applied to
`braidToAlg β` it measures the **unreduced** free-algebra expansion of a braid
word: `braidToAlg` multiplies letters in the free algebra and never applies a
Hecke relation, so `σᵢσᵢ` stays a length-2 monomial instead of becoming
`(q - q⁻¹)σᵢ + 1`. That cost depends on the word, not on the Hecke element.

This file defines the cost of the **normal form** in the completed
Gröbner–Shirshov system of `HeckeCompletion.lean`, proves it is single-valued,
and proves the bound that any functional linear in the normal-form coefficients
satisfies against it.

## Contents

* `IsReducedCost hn hp f c` — `c` is `heckeCost` of a normal form of `f`.
* `IsReducedCost.unique` — two reduced costs of one element agree.
  Inherits the Diamond-Lemma axiom `local_confluence` through
  `heckeCompleted_normalForm_unique` (`reduction_well_founded`, the other
  input, is a theorem since 2026-11-20).
* `linearFunctional` — `f ↦ Σ_m f.coeff m · t m` for a weight `t` on monomials.
  A Markov trace evaluated on a normal form has this shape, with `t w = tr(T_w)`.
* `abs_linearFunctional_le` — **the cost bound.** If every weight on the
  support satisfies `|t m| ≤ M`, then `|Σ f.coeff m · t m| ≤ M · heckeCost f`.
  `M` is a **hypothesis**: for the Ocneanu trace at `z_D` it is
  `Mₙ(q) = max_w |tr_D(T_w)|`, which is not computed here.
* `abs_scaled_le` — the same bound after multiplying by a non-negative scale.
  With scale `[2]ⁿ q^(−2w)` this is `𝔪(β) ≤ [2]ⁿ q^(−2w) · Mₙ(q) · cost(β)`
  for the mass of `def:mass-identity` (write-up `qou-crossing-energy/result.md` §3).
* `linearFunctional_one` — equality on the identity element, cost `1`.

The analytic content (absolute values over `ℝ`) is confined to the two bound
theorems. Nothing here uses a numerical value of `q`.

Bean `qou-078y`.
-/

namespace UGB.GrobnerShirshov.Hecke.ReducedCost

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Hecke

variable {n : ℕ}

/-- `c` is the Hecke cost of a normal form of `f` in the completed system. -/
def IsReducedCost (hn : 0 < n) (hp : HeckeParams)
    (f : AlgElement (HeckeGen n) ℝ) (c : ℝ) : Prop :=
  ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp) f nf ∧
    heckeCost nf = c

/-- **The reduced cost is single-valued.** Two normal forms of one element in
the completed system are equal (`heckeCompleted_normalForm_unique`), so they
have the same cost. -/
theorem IsReducedCost.unique {hn : 0 < n} {hp : HeckeParams}
    {f : AlgElement (HeckeGen n) ℝ} {c₁ c₂ : ℝ}
    (h₁ : IsReducedCost hn hp f c₁) (h₂ : IsReducedCost hn hp f c₂) : c₁ = c₂ := by
  obtain ⟨nf₁, hr₁, rfl⟩ := h₁
  obtain ⟨nf₂, hr₂, rfl⟩ := h₂
  rw [heckeCompleted_normalForm_unique hn hp f nf₁ nf₂ hr₁ hr₂]

/-- The reduced cost is non-negative. -/
theorem IsReducedCost.nonneg {hn : 0 < n} {hp : HeckeParams}
    {f : AlgElement (HeckeGen n) ℝ} {c : ℝ} (h : IsReducedCost hn hp f c) : 0 ≤ c := by
  obtain ⟨nf, _, rfl⟩ := h
  exact heckeCost_nonneg nf

/-- A functional linear in the coefficients, with weight `t m` on monomial `m`. -/
noncomputable def linearFunctional (t : Monomial (HeckeGen n) → ℝ)
    (f : AlgElement (HeckeGen n) ℝ) : ℝ :=
  f.support.sum (fun m => f.coeff m * t m)

/-- **The cost bound.** A coefficient-linear functional whose weights on the
support are bounded by `M` is bounded by `M` times the cost. -/
theorem abs_linearFunctional_le (t : Monomial (HeckeGen n) → ℝ) (M : ℝ)
    (f : AlgElement (HeckeGen n) ℝ) (hM : ∀ m ∈ f.support, |t m| ≤ M) :
    |linearFunctional t f| ≤ M * heckeCost f := by
  unfold linearFunctional heckeCost
  rw [Finset.mul_sum]
  refine (Finset.abs_sum_le_sum_abs _ _).trans (Finset.sum_le_sum fun m hm => ?_)
  rw [abs_mul, mul_comm M]
  exact mul_le_mul_of_nonneg_left (hM m hm) (abs_nonneg _)

/-- The cost bound after a non-negative scale `s`. For the mass,
`s = [2]ⁿ q^(−2w)`. -/
theorem abs_scaled_le (t : Monomial (HeckeGen n) → ℝ) (M s : ℝ) (hs : 0 ≤ s)
    (f : AlgElement (HeckeGen n) ℝ) (hM : ∀ m ∈ f.support, |t m| ≤ M) :
    |s * linearFunctional t f| ≤ s * M * heckeCost f := by
  rw [abs_mul, abs_of_nonneg hs, mul_assoc]
  exact mul_le_mul_of_nonneg_left (abs_linearFunctional_le t M f hM) hs

/-- The bound in terms of a reduced cost: whichever normal form is used, the
functional evaluated on it is bounded by `M` times the reduced cost. -/
theorem abs_linearFunctional_nf_le {hn : 0 < n} {hp : HeckeParams}
    (t : Monomial (HeckeGen n) → ℝ) (M : ℝ) {f nf : AlgElement (HeckeGen n) ℝ} {c : ℝ}
    (hnf : ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp) f nf)
    (hc : IsReducedCost hn hp f c) (hM : ∀ m ∈ nf.support, |t m| ≤ M) :
    |linearFunctional t nf| ≤ M * c := by
  have hcost : IsReducedCost hn hp f (heckeCost nf) := ⟨nf, hnf, rfl⟩
  rw [← hcost.unique hc]
  exact abs_linearFunctional_le t M nf hM

/-- On the identity element the functional is the weight of the empty word,
and the cost is `1`; so when `t [] = M` the bound is attained. -/
theorem linearFunctional_one (t : Monomial (HeckeGen n) → ℝ) :
    linearFunctional t (AlgElement.singleton []) = t [] ∧
    heckeCost (AlgElement.singleton [] : AlgElement (HeckeGen n) ℝ) = 1 := by
  unfold linearFunctional heckeCost AlgElement.singleton AlgElement.single
  simp

/-! ### When is the cost bound an equality?

`abs_linearFunctional_le` gives `|Σ c_m t_m| ≤ M · Σ |c_m|`. Equality would make the functional an
exact multiple of the cost. The two lemmas below pin down when it can hold.

* `abs_eq_of_bound_tight` — **necessity**: if the bound is an equality, every monomial with a
  non-zero coefficient has weight of absolute value exactly `M`.
* `bound_tight_of_aligned` — **sufficiency**: if every weight on the support has absolute value `M`
  and all products `c_m · t_m` are non-negative, the bound is an equality.
* `support_subset_of_bound_tight` — the consequence used for the Markov trace: if one monomial `m₀`
  is the only one with `|t| = M`, equality forces every non-zero coefficient onto `m₀`.

For the convention-D Ocneanu trace `t_w = tr(T_w)` with `q` close to `1`, the maximum `M = 1` is
attained only at the identity (computed exactly for `n ≤ 5`; it fails for larger `n` at any fixed
`q > 1`, see `qou-crossing-energy/result-three-directions.md`). There the bound is an equality only
when the element's normal form is a multiple of `1`. Bean `qou-078y`.
-/

/-- **Necessity.** If `|Σ c_m t_m| = M · Σ |c_m|` and `|t_m| ≤ M` on the support, then
`|t_m| = M` at every `m` in the support with `c_m ≠ 0`. -/
theorem abs_eq_of_bound_tight (t : Monomial (HeckeGen n) → ℝ) (M : ℝ)
    (f : AlgElement (HeckeGen n) ℝ) (hM : ∀ m ∈ f.support, |t m| ≤ M)
    (heq : |linearFunctional t f| = M * heckeCost f) :
    ∀ m ∈ f.support, f.coeff m ≠ 0 → |t m| = M := by
  have hle : |linearFunctional t f| ≤ f.support.sum (fun m => |f.coeff m| * |t m|) := by
    unfold linearFunctional
    refine (Finset.abs_sum_le_sum_abs _ _).trans (le_of_eq ?_)
    exact Finset.sum_congr rfl fun m _ => abs_mul _ _
  have hsum : f.support.sum (fun m => |f.coeff m| * (M - |t m|)) ≤ 0 := by
    have : f.support.sum (fun m => |f.coeff m| * (M - |t m|))
        = M * heckeCost f - f.support.sum (fun m => |f.coeff m| * |t m|) := by
      unfold heckeCost
      rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun m _ => by ring
    rw [this]; linarith
  have hnn : ∀ m ∈ f.support, 0 ≤ |f.coeff m| * (M - |t m|) := fun m hm =>
    mul_nonneg (abs_nonneg _) (by linarith [hM m hm])
  have hzero := (Finset.sum_eq_zero_iff_of_nonneg hnn).mp (le_antisymm hsum (Finset.sum_nonneg hnn))
  intro m hm hc
  have h0 := hzero m hm
  rcases mul_eq_zero.mp h0 with h | h
  · exact absurd (abs_eq_zero.mp h) hc
  · linarith

/-- **Sufficiency.** If every weight on the support has `|t_m| = M` and every product
`c_m · t_m` is non-negative, the cost bound is an equality. -/
theorem bound_tight_of_aligned (t : Monomial (HeckeGen n) → ℝ) (M : ℝ)
    (f : AlgElement (HeckeGen n) ℝ) (hM : ∀ m ∈ f.support, |t m| = M)
    (hsign : ∀ m ∈ f.support, 0 ≤ f.coeff m * t m) :
    |linearFunctional t f| = M * heckeCost f := by
  unfold linearFunctional heckeCost
  rw [abs_of_nonneg (Finset.sum_nonneg hsign), Finset.mul_sum]
  refine Finset.sum_congr rfl fun m hm => ?_
  rw [← abs_of_nonneg (hsign m hm), abs_mul, hM m hm, mul_comm]

/-- **Equality concentrates the coefficients on the maximiser.** If `m₀` is the only monomial of
the support with `|t| = M` (all others strictly below), equality in the cost bound forces
`c_m = 0` for every `m ≠ m₀` in the support. -/
theorem support_subset_of_bound_tight (t : Monomial (HeckeGen n) → ℝ) (M : ℝ)
    (f : AlgElement (HeckeGen n) ℝ) (m₀ : Monomial (HeckeGen n))
    (hM : ∀ m ∈ f.support, |t m| ≤ M) (hstrict : ∀ m ∈ f.support, m ≠ m₀ → |t m| < M)
    (heq : |linearFunctional t f| = M * heckeCost f) :
    ∀ m ∈ f.support, m ≠ m₀ → f.coeff m = 0 := by
  intro m hm hne
  by_contra hc
  have := abs_eq_of_bound_tight t M f hM heq m hm hc
  exact absurd this (ne_of_lt (hstrict m hm hne))

end UGB.GrobnerShirshov.Hecke.ReducedCost
