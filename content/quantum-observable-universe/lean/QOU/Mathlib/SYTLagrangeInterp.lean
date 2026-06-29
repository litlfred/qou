import Mathlib.Algebra.Polynomial.Roots
import Mathlib.RingTheory.Polynomial.Vieta
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.BigOperators.Field

/-!
# QOU.Mathlib.SYTLagrangeInterp — the Lagrange leading-coefficient keystone for β-Lagrange

The Greene–Nijenhuis–Wilf hook-summation identity (`SYTHookGNW.gnwHookIdentity`) reduces, in β-number
coordinates, to a self-contained `ℚ` partial-fractions identity (the **β-Lagrange identity**).  Its
crux is the classical **Lagrange leading-coefficient identity**: for distinct nodes `β₀,…,β_{k−1}` and
the divided-difference weights `D i = ∏_{j≠i}(βᵢ − βⱼ)`,

    ∑ᵢ f(βᵢ) / Dᵢ = [Xᵏ⁻¹] f      whenever  deg f < k.

The pinned Mathlib has no `LinearAlgebra.Lagrange` olean in this build (and no Mathlib *source* to build
it from), so this is hand-rolled from `Polynomial.Roots` (`card_roots'`: a nonzero polynomial has at most
`natDegree` roots).  From the keystone, interpolating `Xᵏ⁻¹, Xᵏ, Xᵏ⁺¹` (Vieta supplying the top two
coefficients of `∏(X − βⱼ)`) gives the three power sums the β-Lagrange assembly needs.

Pure `ℚ` polynomial algebra; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBetaLagrange

open Polynomial Finset

variable {k : ℕ}

/-- The divided-difference / Vandermonde weight `Dᵢ = ∏_{j≠i}(βᵢ − βⱼ)`. -/
noncomputable def vWeight (β : Fin k → ℚ) (i : Fin k) : ℚ :=
  ∏ j ∈ univ.erase i, (β i - β j)

/-- For injective nodes, every weight `Dᵢ` is nonzero (each factor `βᵢ − βⱼ ≠ 0`, `j ≠ i`). -/
theorem vWeight_ne_zero (β : Fin k → ℚ) (hβ : Function.Injective β) (i : Fin k) :
    vWeight β i ≠ 0 := by
  unfold vWeight
  rw [Finset.prod_ne_zero_iff]
  intro j hj
  rw [Finset.mem_erase] at hj
  exact sub_ne_zero.mpr (fun h => hj.1 (hβ h).symm)

/-- The Lagrange basis numerator `Nᵢ(X) = ∏_{j≠i}(X − βⱼ)`. -/
noncomputable def basisNum (β : Fin k → ℚ) (i : Fin k) : ℚ[X] :=
  ∏ j ∈ univ.erase i, (X - C (β j))

/-- `Nᵢ` is monic. -/
theorem basisNum_monic (β : Fin k → ℚ) (i : Fin k) : (basisNum β i).Monic :=
  monic_prod_of_monic _ _ (fun j _ => monic_X_sub_C (β j))

/-- `Nᵢ` has degree `k − 1` (a product of `k − 1` monic linears). -/
theorem basisNum_natDegree (β : Fin k → ℚ) (i : Fin k) :
    (basisNum β i).natDegree = k - 1 := by
  unfold basisNum
  rw [natDegree_prod _ _ (fun j _ => X_sub_C_ne_zero (β j))]
  simp only [natDegree_X_sub_C, Finset.sum_const, Finset.card_erase_of_mem (mem_univ i),
    Finset.card_univ, Fintype.card_fin, smul_eq_mul, mul_one]

/-- The coefficient of `Nᵢ` at degree `k − 1` is `1` (it is the leading coefficient of a monic
polynomial of that degree). -/
theorem basisNum_coeff (β : Fin k → ℚ) (i : Fin k) :
    (basisNum β i).coeff (k - 1) = 1 := by
  have hm := basisNum_monic β i
  have hd := basisNum_natDegree β i
  rw [← hd, hm.coeff_natDegree]

/-- Evaluating `Nᵢ` at node `βₗ`: it is `Dᵢ` when `l = i`, and `0` otherwise (the factor `j = l`
vanishes). -/
theorem basisNum_eval (β : Fin k → ℚ) (i l : Fin k) :
    (basisNum β i).eval (β l) = if l = i then vWeight β i else 0 := by
  unfold basisNum vWeight
  rw [eval_prod]
  simp only [eval_sub, eval_X, eval_C]
  by_cases h : l = i
  · subst h; rw [if_pos rfl]
  · rw [if_neg h]
    apply Finset.prod_eq_zero (i := l)
    · rw [Finset.mem_erase]; exact ⟨h, mem_univ l⟩
    · rw [sub_self]

/-- **Uniqueness of low-degree interpolants.** Two polynomials of degree `< k` that agree at `k`
distinct nodes are equal. Proved from `card_roots'` (a nonzero polynomial has at most `natDegree`
roots) applied to their difference. -/
theorem eq_of_eval_eq (β : Fin k → ℚ) (hβ : Function.Injective β)
    (p q : ℚ[X]) (hp : p.natDegree < k) (hq : q.natDegree < k)
    (h : ∀ i, p.eval (β i) = q.eval (β i)) : p = q := by
  by_contra hpq
  have hr0 : p - q ≠ 0 := sub_ne_zero.mpr hpq
  have hrdeg : (p - q).natDegree < k :=
    lt_of_le_of_lt (natDegree_sub_le p q) (max_lt hp hq)
  -- every node is a root of p - q
  have hroot : ∀ i, β i ∈ (p - q).roots := by
    intro i
    rw [mem_roots hr0]
    simp only [IsRoot.def, eval_sub, h i, sub_self]
  -- the k distinct nodes inject into the root finset
  have hsub : (univ.image β) ⊆ (p - q).roots.toFinset := by
    intro x hx
    rw [Finset.mem_image] at hx
    obtain ⟨i, _, rfl⟩ := hx
    rw [Multiset.mem_toFinset]
    exact hroot i
  have hcard : k ≤ (p - q).roots.toFinset.card := by
    calc k = (univ.image β).card := by
            rw [Finset.card_image_of_injective _ hβ, Finset.card_univ, Fintype.card_fin]
      _ ≤ _ := Finset.card_le_card hsub
  have hle : (p - q).roots.toFinset.card ≤ (p - q).natDegree :=
    le_trans (Multiset.toFinset_card_le _) (card_roots' _)
  omega

/-- **Lagrange leading-coefficient keystone.** For distinct nodes and any `f` with `deg f < k`,

    ∑ᵢ f(βᵢ) / Dᵢ = [Xᵏ⁻¹] f.

The interpolant `g = ∑ᵢ C(f(βᵢ)/Dᵢ) · Nᵢ` agrees with `f` at every node and has degree `< k`, so
`g = f` by `eq_of_eval_eq`; comparing the degree-`(k−1)` coefficient (each `Nᵢ` contributes its leading
`1`) yields the identity. -/
theorem interp_leadingCoeff (β : Fin k → ℚ) (hβ : Function.Injective β) (hk : 0 < k)
    (f : ℚ[X]) (hf : f.natDegree < k) :
    ∑ i, f.eval (β i) / vWeight β i = f.coeff (k - 1) := by
  set g : ℚ[X] := ∑ i, C (f.eval (β i) / vWeight β i) * basisNum β i with hg
  -- g has degree < k
  have hgdeg : g.natDegree < k := by
    rw [hg]
    apply lt_of_le_of_lt (natDegree_sum_le_of_forall_le _ _ (n := k - 1) ?_)
    · omega
    · intro i _
      apply le_trans (natDegree_C_mul_le _ _)
      rw [basisNum_natDegree]
  -- g agrees with f at every node
  have hagree : ∀ l, g.eval (β l) = f.eval (β l) := by
    intro l
    rw [hg, eval_finset_sum]
    simp only [eval_mul, eval_C]
    rw [Finset.sum_eq_single l]
    · rw [basisNum_eval, if_pos rfl, div_mul_cancel₀]
      exact vWeight_ne_zero β hβ l
    · intro i _ hil
      rw [basisNum_eval, if_neg (fun h => hil h.symm), mul_zero]
    · intro hl; exact absurd (mem_univ l) hl
  -- so g = f, and we read off coeff (k-1)
  have hgf : g = f := eq_of_eval_eq β hβ g f hgdeg hf hagree
  have := congrArg (fun p => Polynomial.coeff p (k - 1)) hgf
  simp only at this
  rw [← this, hg, finset_sum_coeff]
  simp only [coeff_C_mul, basisNum_coeff, mul_one]

end QOU.Mathlib.SYTBetaLagrange
