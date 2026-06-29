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

end QOU.Mathlib.SYTVandermonde
