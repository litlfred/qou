import QOU.MathlibExt.RegTraceGramProduct

/-!
# QOU.MathlibExt.RegTraceGramBasisChange — transporting the Gram determinant between bases

Bean `qou-kwoa`, the determinant's **value**: the transport step.

`RegTraceGramProduct` computes the Gram determinant of a semisimple algebra **in a product
basis**, deriving the integer constant `∏_i d_i^(d_i²)`.  That left one gap, stated there and
in PR #6552 as the thing not claimed: a Hecke algebra's Gram is taken in its `T_w` basis, and
the two bases differ.  A Gram matrix transforms as `Pᵀ G P`, so the determinant picks up
`(det P)²` — the constant was pinned only **up to a square**.

This file closes the transport in general.  It does **not** evaluate `det P` for the
Hecke case; see *What is still NOT claimed*.

## Contents

* `bilin_toMatrix_det_basis_change` — the square.  Gram determinants in two bases of the same
  space differ by exactly `(det (b.toMatrix c))²`.  Holds for **any** bilinear form; nothing
  about the regular trace enters.
* `bilin_toMatrix_det_reindex` — relabelling a basis does not move the determinant, because it
  permutes rows and columns *by the same* permutation.  This is what lets a product basis
  indexed by `Σ λ, κ λ` be compared with a `T_w` basis indexed by permutations.
* `regTraceGram_toMatrix_map` — pulling a basis back along an **algebra** equivalence leaves
  the regular-trace Gram matrix *equal*, not merely congruent.  The regular trace form is an
  algebra invariant (`regTraceForm_algEquiv`, #6517), so the transported Gram is the same
  matrix and contributes no factor at all.
* `regTraceGram_det_eq_sq_mul_prod_matrix` — the three composed: for any algebra carrying a
  Wedderburn isomorphism to a product of matrix algebras, and any basis of it, the Gram
  determinant is a square times the derived integer constant.

## Why the square cannot be removed, and what that means for the constant

`(det P)²` is not an artifact of a clumsy route — a Gram determinant is a genuine invariant
only up to squares of units, because congruence `G ↦ PᵀGP` is the transformation law of a
bilinear form.  So *no* choice of argument makes a basis-independent integer appear.  What
`regTraceGram_det_eq_sq_mul_prod_matrix` says is the sharp version: **the constant
`∏_i d_i^(d_i²)` is exactly the square class of the Gram determinant**, and the `T_w` basis
contributes the representative.

Two consequences worth keeping straight:

* **Non-vanishing transports for free**, since a square is nonzero iff its root is.  That is
  consistent with `RegTraceGramNondegenerate`, which reaches `det(twGram) ≠ 0` without any of
  this — and is a check on it.
* **The integer value does not transport for free.**  Pinning it needs `det P` for the change
  of basis from `T_w` to the pulled-back matrix-unit basis, which is a statement about the
  Wedderburn isomorphism's matrix and is not computed here.

## What is still NOT claimed

`det P` is **not** evaluated, for the Hecke case or any other.  In particular this does not
say the Hecke Gram determinant *equals* `∏_λ d_λ^(d_λ²)` — it says the two differ by a square,
which is the correct statement and is weaker.  Nothing here touches the `q`-part, where the
Schur elements live, so this is **not** a proof of Geck–Pfeiffer 7.2.6.
-/

namespace QOU.MathlibExt

open LinearMap Matrix

section BasisChange

variable {K M : Type*} [Field K] [AddCommGroup M] [Module K M]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **A Gram determinant is basis-dependent exactly up to a square.**

`BilinForm.toMatrix_mul_basis_toMatrix` gives the congruence `Pᵀ G P`; taking determinants
turns the two copies of `P` into the square.  This is the reason a Gram determinant pins an
integer only up to `(det P)²`, and it holds for every bilinear form — no algebra structure and
no trace is involved. -/
theorem bilin_toMatrix_det_basis_change (b c : Module.Basis ι K M) (B : LinearMap.BilinForm K M) :
    (BilinForm.toMatrix c B).det
      = (b.toMatrix c).det ^ 2 * (BilinForm.toMatrix b B).det := by
  rw [← BilinForm.toMatrix_mul_basis_toMatrix b c B, Matrix.det_mul, Matrix.det_mul,
    Matrix.det_transpose]
  ring

/-- **Relabelling a basis leaves the Gram determinant alone.**

Reindexing permutes rows and columns by the *same* map, so the determinant is untouched — in
contrast to a genuine change of basis, which contributes the square above.  This is what makes
it legitimate to compare a product basis indexed by `Σ λ, κ λ` with a `T_w` basis indexed by
permutations. -/
theorem bilin_toMatrix_det_reindex {ι' : Type*} [Fintype ι'] [DecidableEq ι']
    (b : Module.Basis ι K M) (e : ι ≃ ι') (B : LinearMap.BilinForm K M) :
    (BilinForm.toMatrix (b.reindex e) B).det = (BilinForm.toMatrix b B).det := by
  have h : BilinForm.toMatrix (b.reindex e) B
      = (BilinForm.toMatrix b B).submatrix e.symm e.symm := by
    ext i j
    simp [BilinForm.toMatrix_apply, Module.Basis.reindex_apply]
  rw [h, Matrix.det_submatrix_equiv_self]

/-- **A change-of-basis determinant is a unit.**

`b.toMatrix c` and `c.toMatrix b` are mutually inverse, so their determinants multiply to `1`.
This is what upgrades the square in `bilin_toMatrix_det_basis_change` from "some factor" to "a
factor that cannot vanish" — without it the transport says nothing about non-vanishing. -/
theorem isUnit_det_basis_toMatrix (b c : Module.Basis ι K M) : IsUnit (b.toMatrix c).det :=
  isUnit_of_mul_eq_one _ _ (by
    rw [← Matrix.det_mul, Module.Basis.toMatrix_mul_toMatrix_flip, Matrix.det_one])

end BasisChange

section AlgEquivTransport

variable {K A B : Type*} [Field K] [Ring A] [Ring B] [Algebra K A] [Algebra K B]
variable [FiniteDimensional K A] [FiniteDimensional K B]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **Pulling a basis back along an algebra equivalence leaves the regular-trace Gram matrix
literally equal** — not merely congruent to it.

The regular trace form is an algebra invariant (`regTraceForm_algEquiv`), so transporting the
*basis* along `e.symm` transports the form with it and the matrix of entries is unchanged.
This is why the Wedderburn isomorphism contributes **no** factor to the determinant: the only
square in the whole transport comes from the change of basis *within* the algebra. -/
theorem regTraceGram_toMatrix_map (e : A ≃ₐ[K] B) (b : Module.Basis ι K B) :
    BilinForm.toMatrix (b.map e.symm.toLinearEquiv) (regTraceBilin K A)
      = BilinForm.toMatrix b (regTraceBilin K B) := by
  ext i j
  rw [BilinForm.toMatrix_apply, BilinForm.toMatrix_apply, Module.Basis.map_apply,
    Module.Basis.map_apply, regTraceBilin_apply, regTraceBilin_apply]
  exact regTraceForm_algEquiv e.symm (b i) (b j)

end AlgEquivTransport

section Composed

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [FiniteDimensional K A]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {ι' : Type*} [Fintype ι'] [DecidableEq ι']
variable {J : ι' → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]

/-- **The transport, composed: any Gram determinant of a Wedderburn-decomposable algebra is a
square times the derived integer constant.**

Given a Wedderburn isomorphism `E` to a product of matrix algebras and *any* basis `c` of the
algebra, the Gram determinant of the regular trace form in `c` is

    (det P)² · ∏ᵢ ± d_i^(d_i²)

where `P` is the change of basis from the pulled-back matrix-unit basis to `c`.  The product
is `regTraceGram_pi_matrix_det` from `RegTraceGramProduct`; the square is
`bilin_toMatrix_det_basis_change`; the Wedderburn isomorphism itself contributes nothing, by
`regTraceGram_toMatrix_map`.

Specialised to a Hecke algebra with `c = basisTwOfField`, the left side is `(twGram …).det`.
**`det P` is not evaluated** — see the module docstring. -/
theorem regTraceGram_det_eq_sq_mul_prod_matrix
    (E : A ≃ₐ[K] (∀ i, Matrix (J i) (J i) K))
    (c : Module.Basis ι K A) (f : ((i : ι') × (J i × J i)) ≃ ι) :
    (BilinForm.toMatrix c (regTraceBilin K A)).det
      = ((((Pi.basis fun i => Matrix.stdBasis K (J i) (J i)).map
              E.symm.toLinearEquiv).reindex f).toMatrix c).det ^ 2
        * ∏ i : ι', (Equiv.Perm.sign (Equiv.prodComm (J i) (J i)) : K)
            * (Fintype.card (J i) : K) ^ (Fintype.card (J i) * Fintype.card (J i)) := by
  rw [bilin_toMatrix_det_basis_change
    ((((Pi.basis fun i => Matrix.stdBasis K (J i) (J i)).map E.symm.toLinearEquiv).reindex f))
    c (regTraceBilin K A)]
  congr 1
  rw [bilin_toMatrix_det_reindex, regTraceGram_toMatrix_map, regTraceGram_pi_matrix_det]

end Composed

end QOU.MathlibExt
