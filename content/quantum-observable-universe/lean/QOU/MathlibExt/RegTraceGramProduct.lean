import QOU.MathlibExt.RegTraceMatrix
import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.LinearAlgebra.StdBasis

/-!
# QOU.MathlibExt.RegTraceGramProduct — the Gram determinant of a product algebra

Bean `qou-kwoa`, the determinant's **value**: the assembly step.

`RegTraceMatrix` derives the Gram determinant of a **single** matrix block,
`± d^(d²)`.  This file assembles the blocks: for a finite product of algebras, the Gram
determinant in a product basis is the **product of the block Gram determinants**.  Composed
with the block computation it derives the integer constant
`∏_λ d_λ^(d_λ²)` that `computations/hecke/tw_gram_determinant_probe.py` measured by factoring
exact symbolic determinants.

## A correction to the blocker I previously named

PR #6552 recorded the assembly as blocked on a *named Mathlib gap*: `Matrix.det_blockDiagonal`
is uniform-block-size only, and there is no determinant lemma for `Matrix.blockDiagonal'`.
The first half is true and the second half is true, **and neither is the obstruction** —
`Matrix.BlockTriangular.det_fintype` (`Mathlib/LinearAlgebra/Matrix/Block.lean:276`) already
gives

    M.det = ∏ k, (M.toSquareBlock b k).det

for `b : m → α` whose fibres are the blocks — of **arbitrary, differing** sizes.  A
block-diagonal matrix is block-triangular for every `b`, so that lemma covers this case
outright.  The search that produced the wrong conclusion was `det` intersected with
`blockDiagonal'`; the capability is present under a different name.  Recorded because the
shape of the error — reporting the absence of a *spelling* as the absence of a
*capability* — is the one the corpus-grep discipline exists to catch.

## Contents

* `det_eq_prod_of_offDiagonal_eq_zero` — the general statement, for any square matrix over a
  sigma index whose off-diagonal blocks vanish.  This is the reusable piece and it is where
  `BlockTriangular.det_fintype` is discharged; `Matrix.det_blockDiagonal'` would be an
  immediate corollary.
* `regTraceForm_pi_single_of_ne` / `regTraceGram_pi_offDiagonal` — the regular trace form on a
  product pairs *different* factors to zero, so its Gram in `Pi.basis` is block diagonal.
* `regTraceGram_pi_det` — the assembly: `det = ∏ i, det (block Gram)`.
* `regTraceGram_pi_matrix_det` — the two composed, for a product of matrix algebras: the
  integer constant `∏ i, ± d_i^(d_i²)`, derived.

## What is still NOT claimed

This computes the Gram determinant in the **product basis** `Pi.basis`.  Transporting it to
the `T_w` basis of a Hecke algebra changes it by `(det P)²` for the change-of-basis `P`, so
this determines the constant only up to a square — and says nothing at all about the
`q`-part, where the Schur elements live.  **This is not a proof of Geck–Pfeiffer 7.2.6.**
-/

namespace QOU.MathlibExt

open LinearMap Matrix BigOperators

section GeneralDet

variable {R : Type*} [CommRing R]
variable {ι : Type*} [Fintype ι] [DecidableEq ι] [LinearOrder ι]
variable {κ : ι → Type*} [∀ i, Fintype (κ i)] [∀ i, DecidableEq (κ i)]

/-- **A block-diagonal matrix over a sigma index has determinant the product of its blocks**,
with the blocks allowed to have *different* sizes.

This is the general form of what `Matrix.det_blockDiagonal` gives only for uniform blocks.
The whole content is `Matrix.BlockTriangular.det_fintype` plus the identification of the
fibre `{p // p.1 = k}` with `κ k`; the linear order on `ι` is an artifact of that lemma and
does not appear in the conclusion. -/
theorem det_eq_prod_of_offDiagonal_eq_zero
    (M : Matrix ((i : ι) × κ i) ((i : ι) × κ i) R)
    (hoff : ∀ p q : (i : ι) × κ i, p.1 ≠ q.1 → M p q = 0) :
    M.det = ∏ i : ι, (Matrix.of fun a b : κ i => M ⟨i, a⟩ ⟨i, b⟩).det := by
  have hbt : M.BlockTriangular Sigma.fst := fun p q h => hoff p q h.ne'
  rw [hbt.det_fintype]
  refine Finset.prod_congr rfl fun k _ => ?_
  rw [← Matrix.det_submatrix_equiv_self (Equiv.sigmaSubtype (β := κ) k).symm
    (M.toSquareBlock Sigma.fst k)]
  rfl

/-- **`Matrix.det_blockDiagonal'` — the named Mathlib gap, as an immediate corollary.**

Mathlib has `Matrix.det_blockDiagonal` for `blockDiagonal` (uniform block size) and no
determinant lemma at all for `blockDiagonal'` (dependent block sizes).  This supplies it, and
the point of stating it here is evidential: it shows that
`det_eq_prod_of_offDiagonal_eq_zero` really is the general form of the missing lemma, and
that the missing lemma was never the obstruction — the whole proof is
`BlockTriangular.det_fintype` plus a fibre reindex. -/
theorem det_blockDiagonal' (M : ∀ i, Matrix (κ i) (κ i) R) :
    (Matrix.blockDiagonal' M).det = ∏ i : ι, (M i).det := by
  rw [det_eq_prod_of_offDiagonal_eq_zero _ (fun p q hpq => by
    obtain ⟨i, a⟩ := p; obtain ⟨j, c⟩ := q
    exact Matrix.blockDiagonal'_apply_ne M a c hpq)]
  exact Finset.prod_congr rfl fun i _ => by
    congr 1
    ext a b
    simp

end GeneralDet

section PiGram

variable {K : Type*} [Field K]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {B : ι → Type*} [∀ i, Ring (B i)] [∀ i, Algebra K (B i)]
variable [∀ i, FiniteDimensional K (B i)]

/-- **Different factors of a product algebra are orthogonal for the regular trace form.**

Every summand of `regTraceForm_pi` is killed: at index `i ≠ j` the first argument is zero,
and at `i = j ≠ k` the second is. -/
theorem regTraceForm_pi_single_of_ne {j k : ι} (hjk : j ≠ k) (x : B j) (y : B k) :
    regTraceForm K (∀ i, B i) (Pi.single j x) (Pi.single k y) = 0 := by
  rw [regTraceForm_pi]
  refine Finset.sum_eq_zero fun i _ => ?_
  rcases eq_or_ne i j with rfl | hij
  · rw [Pi.single_eq_of_ne hjk]
    simp [regTraceForm]
  · rw [Pi.single_eq_of_ne hij]
    simp [regTraceForm]

/-- **Same factor**: the form restricts to the factor's own regular trace form. -/
theorem regTraceForm_pi_single_same (j : ι) (x y : B j) :
    regTraceForm K (∀ i, B i) (Pi.single j x) (Pi.single j y) = regTraceForm K (B j) x y := by
  rw [regTraceForm_pi, Finset.sum_eq_single j]
  · simp
  · intro i _ hij
    rw [Pi.single_eq_of_ne hij]
    simp [regTraceForm]
  · intro h
    exact absurd (Finset.mem_univ j) h

variable {κ : ι → Type*} [∀ i, Fintype (κ i)] [∀ i, DecidableEq (κ i)]

/-- **The Gram matrix of the product, in a product basis, is block diagonal.** -/
theorem regTraceGram_pi_offDiagonal (b : ∀ i, Module.Basis (κ i) K (B i))
    (p q : (i : ι) × κ i) (hpq : p.1 ≠ q.1) :
    BilinForm.toMatrix (Pi.basis b) (regTraceBilin K (∀ i, B i)) p q = 0 := by
  rw [BilinForm.toMatrix_apply, Pi.basis_apply, Pi.basis_apply, regTraceBilin_apply]
  exact regTraceForm_pi_single_of_ne hpq _ _

/-- **The diagonal blocks are the factors' own Gram matrices.** -/
theorem regTraceGram_pi_diagonal (b : ∀ i, Module.Basis (κ i) K (B i)) (k : ι) :
    (Matrix.of fun a c : κ k =>
        BilinForm.toMatrix (Pi.basis b) (regTraceBilin K (∀ i, B i)) ⟨k, a⟩ ⟨k, c⟩)
      = BilinForm.toMatrix (b k) (regTraceBilin K (B k)) := by
  ext a c
  rw [Matrix.of_apply, BilinForm.toMatrix_apply, Pi.basis_apply, Pi.basis_apply,
    regTraceBilin_apply, regTraceForm_pi_single_same, BilinForm.toMatrix_apply,
    regTraceBilin_apply]

/-- **The assembly**: the Gram determinant of a finite product of algebras, in a product
basis, is the product of the factors' Gram determinants.

The linear order on `ι` is inherited from `BlockTriangular.det_fintype` and is invisible in
the statement; `regTraceGram_pi_det'` supplies one for an arbitrary index type. -/
theorem regTraceGram_pi_det [LinearOrder ι] (b : ∀ i, Module.Basis (κ i) K (B i)) :
    (BilinForm.toMatrix (Pi.basis b) (regTraceBilin K (∀ i, B i))).det
      = ∏ i : ι, (BilinForm.toMatrix (b i) (regTraceBilin K (B i))).det := by
  rw [det_eq_prod_of_offDiagonal_eq_zero _ (regTraceGram_pi_offDiagonal b)]
  exact Finset.prod_congr rfl fun k _ => by rw [regTraceGram_pi_diagonal b k]

/-- `regTraceGram_pi_det` with no order hypothesis: any `Fintype` admits a linear order, and
the conclusion does not mention it. -/
theorem regTraceGram_pi_det' (b : ∀ i, Module.Basis (κ i) K (B i)) :
    (BilinForm.toMatrix (Pi.basis b) (regTraceBilin K (∀ i, B i))).det
      = ∏ i : ι, (BilinForm.toMatrix (b i) (regTraceBilin K (B i))).det := by
  haveI : LinearOrder ι :=
    LinearOrder.lift' (Fintype.equivFin ι) (Fintype.equivFin ι).injective
  exact regTraceGram_pi_det b


/-! ### Composed with the block computation: the integer constant, derived -/

variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]

/-- **The Gram determinant of a product of matrix algebras**, in the product of matrix-unit
bases: the product over blocks of `± d_i^(d_i²)`.

This is `regTraceGram_pi_det'` composed with `regTraceGram_stdBasis_det`, and it is the
derivation of the integer constant that
`computations/hecke/tw_gram_determinant_probe.py` measured by factoring exact symbolic
determinants.  Up to the signs it is `∏_i d_i^(d_i²)`; reading the block dimensions off the
Wedderburn decomposition of `H_{n+1}` — the SYT counts of the partitions of `n+1` — that is
`1`, `2⁴`, `2⁴·3¹⁸` at `n = 1, 2, 3`, the probe's three measured constants. -/
theorem regTraceGram_pi_matrix_det :
    (BilinForm.toMatrix (Pi.basis fun i => Matrix.stdBasis K (J i) (J i))
        (regTraceBilin K (∀ i, Matrix (J i) (J i) K))).det
      = ∏ i : ι, (Equiv.Perm.sign (Equiv.prodComm (J i) (J i)) : K)
          * (Fintype.card (J i) : K) ^ (Fintype.card (J i) * Fintype.card (J i)) := by
  rw [regTraceGram_pi_det']
  exact Finset.prod_congr rfl fun i _ => regTraceGram_stdBasis_det K (J i)

/-- **The product Gram determinant vanishes exactly when some block dimension dies in `K`.**

The sharp characteristic statement for a semisimple algebra in Wedderburn form: the regular
trace form degenerates iff `char K` divides one of the block dimensions.  Over a
characteristic-zero field no block can die, which is the route
`RegTraceGramNondegenerate` takes to `det(twGram) ≠ 0` — this says the char-zero hypothesis
there is not merely sufficient but exactly right. -/
theorem regTraceGram_pi_matrix_det_ne_zero_iff [∀ i, Nonempty (J i)] :
    (BilinForm.toMatrix (Pi.basis fun i => Matrix.stdBasis K (J i) (J i))
        (regTraceBilin K (∀ i, Matrix (J i) (J i) K))).det ≠ 0
      ↔ ∀ i, (Fintype.card (J i) : K) ≠ 0 := by
  rw [regTraceGram_pi_det', Finset.prod_ne_zero_iff]
  simp only [Finset.mem_univ, forall_const]
  exact forall_congr' fun i => regTraceGram_stdBasis_det_ne_zero_iff K (J i)

end PiGram

end QOU.MathlibExt
