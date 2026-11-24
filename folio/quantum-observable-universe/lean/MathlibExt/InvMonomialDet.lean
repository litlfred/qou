import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Algebra.Group.Equiv.Basic

/-!
# QOU.MathlibExt.InvMonomialDet — determinant of a matrix supported on the graph of a permutation

A *generalised permutation matrix* — one whose support is the graph
`{(v, σ v)}` of a permutation, carrying an arbitrary scalar `f v` there — has
determinant `sign σ · ∏ f`.  Mathlib has both halves separately
(`Matrix.det_diagonal`, `Matrix.det_permute'`) and not the composite, so this
file is one lemma and its group-inversion specialisation.

The specialisation is the one wanted downstream: on a finite group `G`, the
matrix `M v w = if w = v⁻¹ then f v else 0`.  That is the shape of the Gram
matrix of a symmetrizing trace in a basis indexed by `G` — see
`QOU.Hecke.TauSymmetrizing` — because such a trace pairs a basis element only
with the basis element at its inverse.

## What is proved

* `det_of_graph_monomial` — `det (fun v w => if w = σ v then f v else 0)
  = sign σ · ∏ f`, for any `σ : Equiv.Perm ι`.
* `det_of_inv_monomial` — the `σ = ` inversion case on a finite group.
* `det_of_inv_monomial_ne_zero` — nonzero over a field iff no `f v` vanishes.

Nothing here is Hecke-specific and nothing is archimedean; everything is over a
generic `[CommRing K]` (`[Field K]` only for the non-vanishing corollary), per
the §7c base-ring convention.
-/

namespace QOU.MathlibExt

open Matrix

variable {K : Type*} {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **A matrix supported on the graph of `σ` is `sign σ` times the product of
    its nonzero entries.**

    `M v w = f v` when `w = σ v` and `0` otherwise; it is `diagonal f` with its
    columns permuted, which is why `Matrix.det_permute'` closes it. -/
theorem det_of_graph_monomial [CommRing K] (σ : Equiv.Perm ι) (f : ι → K) :
    (Matrix.of fun v w => if w = σ v then f v else 0 : Matrix ι ι K).det
      = (Equiv.Perm.sign σ : K) * ∏ v, f v := by
  have hM : (Matrix.of fun v w => if w = σ v then f v else 0 : Matrix ι ι K)
      = (Matrix.diagonal f).submatrix id σ.symm := by
    ext v w
    simp only [Matrix.of_apply, Matrix.submatrix_apply, id_eq, Matrix.diagonal_apply]
    exact if_congr (by rw [Equiv.eq_symm_apply, eq_comm]) rfl rfl
  rw [hM, Matrix.det_permute', Matrix.det_diagonal]
  congr 1
  rw [← Equiv.Perm.inv_def, Equiv.Perm.sign_inv]

/-- **The inversion case.**  On a finite group, a matrix whose only nonzero
    entries sit at `(v, v⁻¹)` has determinant `sign(inv) · ∏ f`. -/
theorem det_of_inv_monomial [CommRing K] {G : Type*} [Group G] [Fintype G]
    [DecidableEq G] (f : G → K) :
    (Matrix.of fun v w => if w = v⁻¹ then f v else 0 : Matrix G G K).det
      = (Equiv.Perm.sign (Equiv.inv G) : K) * ∏ v, f v :=
  det_of_graph_monomial (Equiv.inv G) f

/-- Over a field such a determinant vanishes exactly when one of the entries
    does — the sign is a unit and contributes nothing. -/
theorem det_of_inv_monomial_ne_zero [Field K] {G : Type*} [Group G] [Fintype G]
    [DecidableEq G] {f : G → K} (hf : ∀ v, f v ≠ 0) :
    (Matrix.of fun v w => if w = v⁻¹ then f v else 0 : Matrix G G K).det ≠ 0 := by
  rw [det_of_inv_monomial]
  refine mul_ne_zero ?_ (Finset.prod_ne_zero_iff.mpr fun v _ => hf v)
  rcases Int.units_eq_one_or (Equiv.Perm.sign (Equiv.inv G)) with h | h <;>
    rw [h] <;> simp

end QOU.MathlibExt
