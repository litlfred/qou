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

end QOU.Mathlib.SYTVandermonde
