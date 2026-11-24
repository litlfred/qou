import Mathlib.LinearAlgebra.Vandermonde

/-!
# QOU.Mathlib.SYTVandermondeKeystone — the divided-difference keystone via `det_vandermonde`

The β-Lagrange identity behind the general SYT hook-length formula (obligation (A), bean `sy7b`)
rests on the **divided-difference leading-coefficient** keystone

    ∑ i, f.eval (β i) / vWeight β i  =  f.coeff (k − 1)      (`f.natDegree < k`)

where `vWeight β i = ∏_{j ≠ i} (β i − β j)`.  This file proves it the **determinant** way — by
Laplace-expanding `Matrix.det_vandermonde` — rather than via Lagrange interpolation (owner preference:
exact determinant algebra over interpolation; and `det_vandermonde` is in the build cache while
`Mathlib.LinearAlgebra.Lagrange` is not).  This is the drop-in replacement for the hand-rolled
`SYTLagrangeInterp.interp_leadingCoeff` (coordinated on PR #2986).

## Proof skeleton

Let `V = vandermonde β` (`V i j = β i ^ j`), `cofactor i = (−1)^(i+(k−1)) · det(V.submatrix i.succAbove
(Fin.last).succAbove)`.  Laplace along the last column (`det_succ_column`) gives, for the matrix `A_d`
= `V` with the last column replaced by `β i ^ d`,

    det A_d = ∑ i, cofactor i · (β i)^d.

* `d < k−1`: `A_d` has two equal columns (`d` and `k−1`) ⇒ `det A_d = 0`.
* `d = k−1`: `A_d = V` ⇒ `det A_d = det V`.

The crux (`cofactor_mul_vWeight`): `cofactor i · vWeight β i = det V`, from `det_vandermonde` on `V` and
on the sub-vandermonde `V.submatrix i.succAbove (Fin.last).succAbove = vandermonde (β ∘ i.succAbove)`,
with the sign `(−1)^(i+k−1) = (−1)^(k−1−i)`.  Then for injective `β` (so `det V ≠ 0`):

    ∑ i, (β i)^d / vWeight β i  =  (∑ i, cofactor i (β i)^d) / det V  =  det A_d / det V  =  [d = k−1].

Linearity over the coefficients of `f` lifts the power-sum form to the polynomial keystone.

Pure exact `ℚ`/`CommRing` determinant algebra; no interpolation, no `ℝ`.
-/

namespace QOU.Mathlib.SYTVandermonde

open Matrix Polynomial Finset

variable {k : ℕ}

/-- The Vandermonde / divided-difference weight `Dᵢ = ∏_{j ≠ i}(βᵢ − βⱼ)` (matches
`SYTLagrangeInterp.vWeight`). -/
noncomputable def vWeight (β : Fin k → ℚ) (i : Fin k) : ℚ :=
  ∏ j ∈ univ.erase i, (β i - β j)

theorem vWeight_ne_zero (β : Fin k → ℚ) (hβ : Function.Injective β) (i : Fin k) :
    vWeight β i ≠ 0 := by
  unfold vWeight
  rw [Finset.prod_ne_zero_iff]
  intro j hj
  rw [Finset.mem_erase] at hj
  exact sub_ne_zero.mpr (fun h => hj.1 (hβ h).symm)

/-! ## The modified Vandermonde, its Laplace expansion, and the two column cases (sorry-free) -/

/-- The Vandermonde with its last column `(β i)^k` replaced by `(β i)^d`. -/
noncomputable def Amat (β : Fin (k + 1) → ℚ) (d : ℕ) : Matrix (Fin (k + 1)) (Fin (k + 1)) ℚ :=
  fun i j => if j = Fin.last k then (β i) ^ d else (vandermonde β) i j

/-- The cofactor of the Vandermonde along the last column at row `i`. -/
noncomputable def cof (β : Fin (k + 1) → ℚ) (i : Fin (k + 1)) : ℚ :=
  (-1) ^ ((i : ℕ) + k) * ((vandermonde β).submatrix i.succAbove (Fin.last k).succAbove).det

/-- **Laplace expansion of `Amat` along the last column.** `det (Amat β d) = ∑ᵢ cofᵢ · (βᵢ)ᵈ`. -/
theorem detAmat_laplace (β : Fin (k + 1) → ℚ) (d : ℕ) :
    (Amat β d).det = ∑ i, cof β i * (β i) ^ d := by
  rw [Matrix.det_succ_column (Amat β d) (Fin.last k)]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  have hAij : Amat β d i (Fin.last k) = (β i) ^ d := by simp [Amat]
  have hsub : (Amat β d).submatrix i.succAbove (Fin.last k).succAbove
      = (vandermonde β).submatrix i.succAbove (Fin.last k).succAbove := by
    ext a b; simp only [Matrix.submatrix_apply, Amat, Fin.succAbove_last]
    rw [if_neg (Fin.castSucc_lt_last b).ne]
  rw [hAij, hsub, cof, Fin.val_last]; ring

/-- At `d = k` the modified Vandermonde is the Vandermonde itself. -/
theorem Amat_top (β : Fin (k + 1) → ℚ) : Amat β k = vandermonde β := by
  ext i j; simp only [Amat, vandermonde_apply]
  split
  · next h => rw [h, Fin.val_last]
  · rfl

/-- For `d < k`, `Amat` has two equal columns (`d` and the last) so its determinant vanishes. -/
theorem detAmat_lt (β : Fin (k + 1) → ℚ) (d : ℕ) (hd : d < k) : (Amat β d).det = 0 := by
  have hne : (⟨d, by omega⟩ : Fin (k + 1)) ≠ Fin.last k := by
    rw [Ne, Fin.ext_iff, Fin.val_last]; simp; omega
  apply Matrix.det_zero_of_column_eq hne
  intro r
  simp [Amat, hne, vandermonde_apply]

/-! ## The crux: the Vandermonde cofactor product-split

`cofᵢ · vWeightᵢ = det V`, proved by splitting `det_vandermonde`'s pair product at the pivot
row `i` via `Fin.prod_univ_succAbove`.  The four helper lemmas below carry the reindexing; the
crux assembles them. -/

/-- The `succAbove` image of `Ioi a` is `Ioi (i.succAbove a)` with the pivot `i` removed: the
nodes above `βᵢ`-image among `q ≠ i`. -/
theorem succAbove_image_Ioi (i : Fin (k + 1)) (a : Fin k) :
    (Ioi a).image i.succAbove = (Ioi (i.succAbove a)).erase i := by
  ext q
  simp only [Finset.mem_image, Finset.mem_Ioi, Finset.mem_erase]
  constructor
  · rintro ⟨b, hb, rfl⟩
    exact ⟨Fin.succAbove_ne i b, (Fin.succAbove_lt_succAbove_iff).mpr hb⟩
  · rintro ⟨hqi, hq⟩
    obtain ⟨b, rfl⟩ := Fin.exists_succAbove_eq hqi
    exact ⟨b, (Fin.succAbove_lt_succAbove_iff).mp hq, rfl⟩

/-- The inner `Ioi (i.succAbove a)` Vandermonde-difference product splits into the sub-Vandermonde
factor (over `Ioi a`) and the single pivot factor `(β i − β (i.succAbove a))` present iff
`i.succAbove a < i`. -/
theorem inner_split (β : Fin (k + 1) → ℚ) (i : Fin (k + 1)) (a : Fin k) :
    ∏ q ∈ Ioi (i.succAbove a), (β q - β (i.succAbove a))
      = (∏ b ∈ Ioi a, (β (i.succAbove b) - β (i.succAbove a)))
        * (if i.succAbove a < i then (β i - β (i.succAbove a)) else 1) := by
  have hreindex : ∏ b ∈ Ioi a, (β (i.succAbove b) - β (i.succAbove a))
      = ∏ q ∈ (Ioi (i.succAbove a)).erase i, (β q - β (i.succAbove a)) := by
    rw [← succAbove_image_Ioi i a,
      Finset.prod_image (fun x _ y _ h => Fin.succAbove_right_injective h)]
  rw [hreindex]
  by_cases h : i.succAbove a < i
  · rw [if_pos h]
    have hi : i ∈ Ioi (i.succAbove a) := Finset.mem_Ioi.mpr h
    rw [← Finset.mul_prod_erase _ _ hi, mul_comm]
  · rw [if_neg h, mul_one]
    have hi : i ∉ Ioi (i.succAbove a) := by rw [Finset.mem_Ioi]; exact h
    rw [Finset.erase_eq_of_notMem hi]

/-- The pivot-row contribution: `(∏_{q>i}(β q − β i)) · (∏_{a : σa<i}(β i − β σa)) = (−1)^(k−i) ·
vWeightᵢ`.  The above-pivot product flips sign on each of its `k − i` factors, and the two
half-products reassemble `vWeightᵢ = ∏_{j≠i}(β i − β j)`. -/
theorem pivot_contribution (β : Fin (k + 1) → ℚ) (i : Fin (k + 1)) :
    (∏ q ∈ Ioi i, (β q - β i))
      * (∏ a : Fin k, if i.succAbove a < i then (β i - β (i.succAbove a)) else 1)
      = (-1 : ℚ) ^ (k - (i : ℕ)) * vWeight β i := by
  have hB : ∏ q ∈ Ioi i, (β q - β i) = (-1 : ℚ) ^ (k - (i : ℕ)) * ∏ q ∈ Ioi i, (β i - β q) := by
    have hneg : ∀ q, β q - β i = (-1 : ℚ) * (β i - β q) := by intro q; ring
    simp_rw [hneg]
    rw [Finset.prod_mul_distrib, Finset.prod_const, Fin.card_Ioi]
    simp only [Nat.add_sub_cancel]
  have himg2 : (univ.filter (fun a => i.succAbove a < i)).image i.succAbove = Iio i := by
    ext q; simp only [mem_image, mem_filter, mem_univ, true_and, mem_Iio]
    constructor
    · rintro ⟨a, ha, rfl⟩; exact ha
    · intro hq; obtain ⟨a, rfl⟩ := Fin.exists_succAbove_eq (ne_of_lt hq)
      exact ⟨a, hq, rfl⟩
  have hC : (∏ a : Fin k, if i.succAbove a < i then (β i - β (i.succAbove a)) else 1)
      = ∏ q ∈ Iio i, (β i - β q) := by
    rw [← Finset.prod_filter, ← himg2,
      Finset.prod_image (fun x _ y _ h => Fin.succAbove_right_injective h)]
  have hW : vWeight β i = (∏ q ∈ Iio i, (β i - β q)) * (∏ q ∈ Ioi i, (β i - β q)) := by
    unfold vWeight
    have hunion : (univ.erase i) = Iio i ∪ Ioi i := by
      ext q
      simp only [mem_erase, mem_univ, and_true, mem_union, mem_Iio, mem_Ioi]; omega
    have hdis : Disjoint (Iio i) (Ioi i) := by
      rw [Finset.disjoint_left]; intro q h1 h2
      rw [mem_Iio] at h1; rw [mem_Ioi] at h2; omega
    rw [hunion, Finset.prod_union hdis]
  rw [hB, hC, hW]; ring

/-- **The cofactor product-split, product form.**  `det V = (−1)^(k−i) · det(V₋ᵢ) · vWeightᵢ`,
where `V₋ᵢ = vandermonde (β ∘ i.succAbove)` is the Vandermonde with node `βᵢ` deleted.  Split
`det_vandermonde`'s pair product at the pivot row `i`. -/
theorem det_vandermonde_pivot_split (β : Fin (k + 1) → ℚ) (i : Fin (k + 1)) :
    (vandermonde β).det
      = (-1 : ℚ) ^ (k - (i : ℕ)) * (vandermonde (β ∘ i.succAbove)).det * vWeight β i := by
  have hQd : (vandermonde (β ∘ i.succAbove)).det
      = ∏ a : Fin k, ∏ b ∈ Ioi a, (β (i.succAbove b) - β (i.succAbove a)) := by
    rw [det_vandermonde]; rfl
  rw [det_vandermonde β, Fin.prod_univ_succAbove _ i]
  simp_rw [inner_split β i]
  rw [Finset.prod_mul_distrib, ← hQd]
  linear_combination (vandermonde (β ∘ i.succAbove)).det * pivot_contribution β i

/-- **The Vandermonde cofactor product-split (crux).**  `cofᵢ · vWeightᵢ = det V`.

The cofactor along the last column is `(−1)^(i+k) · det(V.submatrix iᵒ lastᵒ)`, and that submatrix
is `vandermonde (β ∘ i.succAbove)` (nodes with `βᵢ` deleted).  Combine with
`det_vandermonde_pivot_split`; the signs match because `(−1)^(i+k) = (−1)^(k−i)` (`i ≤ k`).

This is the heart of the determinant route; it replaces the sibling's hand-rolled
`SYTLagrangeInterp.interp_leadingCoeff` (PR #2986). -/
theorem cof_mul_vWeight (β : Fin (k + 1) → ℚ) (i : Fin (k + 1)) :
    cof β i * vWeight β i = (vandermonde β).det := by
  have hsub : (vandermonde β).submatrix i.succAbove (Fin.last k).succAbove
      = vandermonde (β ∘ i.succAbove) := by
    ext a b; simp only [Matrix.submatrix_apply, vandermonde_apply, Function.comp_apply,
      Fin.succAbove_last, Fin.coe_castSucc]
  have hile : (i : ℕ) ≤ k := Nat.lt_succ_iff.mp i.isLt
  have hsign : (-1 : ℚ) ^ ((i : ℕ) + k) = (-1 : ℚ) ^ (k - (i : ℕ)) := by
    have hik : (i : ℕ) + k = (k - (i : ℕ)) + 2 * (i : ℕ) := by omega
    rw [hik, pow_add, pow_mul]; norm_num
  rw [cof, hsub, det_vandermonde_pivot_split β i, hsign]

/-! ## The power-sum keystone and its polynomial lift (sorry-free given the crux) -/

/-- `det (vandermonde β) ≠ 0` for injective nodes. -/
theorem vandermonde_det_ne_zero (β : Fin (k + 1) → ℚ) (hβ : Function.Injective β) :
    (vandermonde β).det ≠ 0 := by
  rw [det_vandermonde, Finset.prod_ne_zero_iff]; intro a _
  rw [Finset.prod_ne_zero_iff]; intro b hb
  rw [Finset.mem_Ioi] at hb
  exact sub_ne_zero.mpr (fun h => (ne_of_lt hb) (hβ h).symm)

/-- **Power-sum form of the keystone.** `∑ᵢ (βᵢ)ᵈ / vWeightᵢ = [d = k]` for `d ≤ k`. -/
theorem powSum (β : Fin (k + 1) → ℚ) (hβ : Function.Injective β) (d : ℕ) (hdk : d ≤ k) :
    ∑ i, (β i) ^ d / vWeight β i = if d = k then 1 else 0 := by
  have hV := vandermonde_det_ne_zero β hβ
  have hstep : ∑ i, (β i) ^ d / vWeight β i = (Amat β d).det / (vandermonde β).det := by
    rw [eq_div_iff hV, detAmat_laplace, Finset.sum_mul]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    have hc : (vandermonde β).det / vWeight β i = cof β i := by
      rw [← cof_mul_vWeight β i, mul_div_assoc, div_self (vWeight_ne_zero β hβ i), mul_one]
    rw [div_mul_eq_mul_div, mul_div_assoc, hc, mul_comm]
  rw [hstep]
  by_cases hd : d = k
  · subst hd; rw [Amat_top, div_self hV, if_pos rfl]
  · rw [detAmat_lt β d (by omega), zero_div, if_neg hd]

/-- **The keystone**, matching the type of `SYTLagrangeInterp.interp_leadingCoeff` (PR #2986):
the divided-difference combination of `f` over the nodes returns its leading coefficient
`f.coeff k` whenever `f.natDegree ≤ k`.  Proved by linearity from `powSum`, no interpolation. -/
theorem interp_leadingCoeff (β : Fin (k + 1) → ℚ) (hβ : Function.Injective β)
    (f : ℚ[X]) (hf : f.natDegree ≤ k) :
    ∑ i, f.eval (β i) / vWeight β i = f.coeff k := by
  have hexp : ∀ i, f.eval (β i) = ∑ d ∈ Finset.range (k + 1), f.coeff d * (β i) ^ d := by
    intro i; rw [eval_eq_sum_range' (by omega : f.natDegree < k + 1)]
  simp_rw [hexp, div_eq_mul_inv, Finset.sum_mul]
  rw [Finset.sum_comm]
  have hper : ∀ d ∈ Finset.range (k + 1),
      ∑ i, (f.coeff d * (β i) ^ d) * (vWeight β i)⁻¹ = f.coeff d * (if d = k then 1 else 0) := by
    intro d hd
    rw [Finset.mem_range] at hd
    rw [← powSum β hβ d (by omega), Finset.mul_sum]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [div_eq_mul_inv]; ring
  rw [Finset.sum_congr rfl hper]
  simp

end QOU.Mathlib.SYTVandermonde
