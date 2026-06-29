import QOU.Mathlib.SYTLagrangeInterp

/-!
# QOU.Mathlib.SYTBetaLagrange — the β-Lagrange identity

The Greene–Nijenhuis–Wilf hook-summation identity reduces, in β-number coordinates, to the
self-contained `ℚ` **β-Lagrange identity**

    ∑ᵢ βᵢ · ∏_{j≠i} (βᵢ − 1 − βⱼ)/(βᵢ − βⱼ)  =  (∑ᵢ βᵢ) − C(k,2).

This file assembles it on the Lagrange leading-coefficient keystone
(`SYTLagrangeInterp.interp_leadingCoeff`).

**Route.** Let `Q(X) = ∏ⱼ (X − βⱼ)` (vanishes at every node `βᵢ`, since the `j=i` factor is `0`) and
`G(X) = X · ∏ⱼ (X − (βⱼ+1))`, so `G(βᵢ) = βᵢ ∏ⱼ(βᵢ − 1 − βⱼ)`.  Removing the `j=i` factor flips a sign,
`∏_{j≠i}(βᵢ−1−βⱼ) = −∏ⱼ(βᵢ−1−βⱼ)`, so the left side is `−∑ᵢ G(βᵢ)/Dᵢ` with `Dᵢ = ∏_{j≠i}(βᵢ−βⱼ)`.
Writing `G = R + (X − C k)·Q` with `deg R < k` (the top two coefficients cancel by Vieta), the keystone
gives `∑ᵢ G(βᵢ)/Dᵢ = R.coeff (k−1) = C(k,2) − ∑βᵢ`, whence the identity.

Pure `ℚ` polynomial algebra; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBetaLagrange

open Polynomial Finset

variable {k : ℕ}

/-- `Q(X) = ∏ⱼ (X − βⱼ)` — the node polynomial. It vanishes at every node. -/
noncomputable def nodePoly (β : Fin k → ℚ) : ℚ[X] :=
  ∏ j, (X - C (β j))

/-- `Q` vanishes at every node `βᵢ` (the `j = i` factor is `βᵢ − βᵢ = 0`). -/
theorem nodePoly_eval (β : Fin k → ℚ) (i : Fin k) : (nodePoly β).eval (β i) = 0 := by
  unfold nodePoly
  rw [eval_prod]
  apply Finset.prod_eq_zero (mem_univ i)
  rw [eval_sub, eval_X, eval_C, sub_self]

/-- **Decomposition reduction.** If `G = R + H·Q` with `deg R < k`, then `∑ᵢ G(βᵢ)/Dᵢ = R.coeff (k−1)`:
`Q` kills the `H·Q` part at every node, and the keystone evaluates the `R` part. -/
theorem sum_eval_div_eq_of_decomp (β : Fin k → ℚ) (hβ : Function.Injective β) (hk : 0 < k)
    (G R H : ℚ[X]) (hR : R.natDegree < k) (hdec : G = R + H * nodePoly β) :
    ∑ i, G.eval (β i) / vWeight β i = R.coeff (k - 1) := by
  have hval : ∀ i, G.eval (β i) = R.eval (β i) := by
    intro i
    rw [hdec, eval_add, eval_mul, nodePoly_eval, mul_zero, add_zero]
  rw [Finset.sum_congr rfl (fun i _ => by rw [hval i])]
  exact interp_leadingCoeff β hβ hk R hR

/-- The shifted-node polynomial `∏ⱼ (X − (βⱼ+1))`, whose value at `βᵢ` is `∏ⱼ(βᵢ − 1 − βⱼ)`. -/
noncomputable def shiftPoly (β : Fin k → ℚ) : ℚ[X] :=
  ∏ j, (X - C (β j + 1))

/-- `G(X) = X · ∏ⱼ (X − (βⱼ+1))`: at a node, `G(βᵢ) = βᵢ · ∏ⱼ(βᵢ − 1 − βⱼ)`. -/
noncomputable def bigPoly (β : Fin k → ℚ) : ℚ[X] := X * shiftPoly β

/-- The residual `R = G − (X − C k)·Q`. -/
noncomputable def residPoly (β : Fin k → ℚ) : ℚ[X] :=
  bigPoly β - (X - C (k : ℚ)) * nodePoly β

theorem bigPoly_decomp (β : Fin k → ℚ) :
    bigPoly β = residPoly β + (X - C (k : ℚ)) * nodePoly β := by
  unfold residPoly; ring

/-- Value of `G` at a node: `G(βᵢ) = βᵢ · ∏ⱼ(βᵢ − 1 − βⱼ)`. -/
theorem bigPoly_eval (β : Fin k → ℚ) (i : Fin k) :
    (bigPoly β).eval (β i) = β i * ∏ j, (β i - 1 - β j) := by
  unfold bigPoly shiftPoly
  rw [eval_mul, eval_X, eval_prod]
  congr 1
  apply Finset.prod_congr rfl
  intro j _
  rw [eval_sub, eval_X, eval_C]
  ring

/-- **(Vieta, residual degree)** The residual has degree `< k`: the `Xᵏ⁺¹` and `Xᵏ` coefficients of
`G` and `(X − C k)·Q` cancel. -/
theorem residPoly_natDegree_lt (β : Fin k → ℚ) (hk : 0 < k) :
    (residPoly β).natDegree < k := by
  -- Ref: [macdonald1995] https://doi.org/10.1093/oso/9780198534891.001.0001 (Vieta / elementary
  -- symmetric coefficients of ∏(X − aⱼ); §I.2). Top two coeffs of G and (X − C k)·Q agree.
  sorry

/-- **(Vieta, residual leading coefficient)** `R.coeff (k−1) = C(k,2) − ∑ⱼ βⱼ`.  Computed from the
degree-`(k−1)` and degree-`(k−2)` coefficients of `G` and `Q` via Vieta and the `βⱼ ↦ βⱼ+1` shift of
the second elementary symmetric polynomial. -/
theorem residPoly_coeff (β : Fin k → ℚ) (hk : 0 < k) :
    (residPoly β).coeff (k - 1) = (k.choose 2 : ℚ) - ∑ j, β j := by
  -- Ref: [macdonald1995] https://doi.org/10.1093/oso/9780198534891.001.0001 (Vieta + esymm shift
  -- e₂(β+1) = e₂(β) + (k−1)e₁(β) + C(k,2); §I.2).
  sorry

/-- Removing the `j = i` factor from `∏ⱼ(βᵢ − 1 − βⱼ)` flips a sign (that factor is `βᵢ−1−βᵢ = −1`). -/
theorem prod_erase_eq_neg (β : Fin k → ℚ) (i : Fin k) :
    ∏ j ∈ univ.erase i, (β i - 1 - β j) = - ∏ j, (β i - 1 - β j) := by
  rw [← Finset.mul_prod_erase univ _ (mem_univ i)]
  have : β i - 1 - β i = -1 := by ring
  rw [this]
  ring

/-- **The β-Lagrange identity.** For distinct nodes `β : Fin k → ℚ` (`k ≥ 1`),

    ∑ᵢ βᵢ · ∏_{j≠i}(βᵢ − 1 − βⱼ)/(βᵢ − βⱼ)  =  (∑ⱼ βⱼ) − C(k,2).

The self-contained `ℚ` partial-fractions identity the GNW hook-summation identity reduces to. -/
theorem betaLagrange (β : Fin k → ℚ) (hβ : Function.Injective β) (hk : 0 < k) :
    ∑ i, β i * (∏ j ∈ univ.erase i, (β i - 1 - β j)) / vWeight β i
      = (∑ j, β j) - (k.choose 2 : ℚ) := by
  -- rewrite each summand to −G(βᵢ)/Dᵢ via the sign flip
  have hrw : ∀ i, β i * (∏ j ∈ univ.erase i, (β i - 1 - β j)) / vWeight β i
      = - ((bigPoly β).eval (β i) / vWeight β i) := by
    intro i
    rw [prod_erase_eq_neg, bigPoly_eval, mul_neg, neg_div]
  calc ∑ i, β i * (∏ j ∈ univ.erase i, (β i - 1 - β j)) / vWeight β i
      = ∑ i, - ((bigPoly β).eval (β i) / vWeight β i) :=
        Finset.sum_congr rfl (fun i _ => hrw i)
    _ = - ∑ i, (bigPoly β).eval (β i) / vWeight β i := by rw [Finset.sum_neg_distrib]
    _ = - (residPoly β).coeff (k - 1) := by
        rw [sum_eval_div_eq_of_decomp β hβ hk (bigPoly β) (residPoly β) (X - C (k : ℚ))
              (residPoly_natDegree_lt β hk) (bigPoly_decomp β)]
    _ = (∑ j, β j) - (k.choose 2 : ℚ) := by rw [residPoly_coeff β hk]; ring

end QOU.Mathlib.SYTBetaLagrange
