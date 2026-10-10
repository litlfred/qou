import QOU.MathlibExt.RegTraceGramNondegenerate
import Mathlib.LinearAlgebra.Matrix.ToLin

/-!
# QOU.MathlibExt.RegTraceMatrix — the regular trace form of a matrix algebra

Bean `qou-kwoa`, the determinant's **value**.

`RegTraceGramNondegenerate` proves `det(twGram) ≠ 0` without computing the determinant, and
gets the characteristic hypothesis it needs from `regTraceForm_one_one` (`B(1,1) = finrank`).
That is enough for non-vanishing, but it is not the sharp statement.  The sharp statement is

    regTraceForm K (Matrix ι ι K) x y = (card ι) * (x * y).trace

— the regular trace is `d` times the *ordinary matrix trace*.  `B(1,1) = d²` is its diagonal
corollary (`tr 1 = d`), and the whole characteristic story reads off it: the form is
`d · tr(xy)`, and `tr` is nondegenerate over any field, so the form degenerates **exactly**
when `d = 0` in `K`.  `docs/audits/2026-08-30-tw-gram-determinant-measured.md` asserts that
equivalence as the premise of its scope-(b) exclusion; this file proves it.

## Why the proof is short

Left multiplication by `M` acts on each **column** of `X` independently — column `j` of
`M * X` is `M *ᵥ (column j of X)` — so `lmul M` is literally block-diagonal, with `card ι`
identical blocks `M.mulVecLin`.  That is exactly the shape `QOU.MathlibExt.trace_piDiag`
(`TracePi.lean`) was written for, so no basis computation is needed.  `Matrix.stdBasis`
exposes no `repr` simp lemma, which makes the direct route painful; this one avoids it.

## The block Gram determinant

In the matrix-unit basis the Gram matrix is `d •` the identity, row-permuted by the
transpose involution `(i,j) ↦ (j,i)` — because `tr(E_ij · E_kl) = δ_{jk} δ_{il}`.  So its
determinant is `sign(prodComm) · d^(d²)`, and the per-block factor `d^(d²)` of the integer
constant `∏_λ d_λ^(d_λ²)` measured by the probe is *derived* rather than observed.

**Numerical cross-check against the probe.**  Assembling `d^(d²)` over the Wedderburn blocks
of `H_{n+1}` — i.e. over the partitions of `n+1`, with `d_λ` the SYT count — reproduces the
probe's measured integer constant exactly at every rank it computed:

| `n` | block dims `d_λ` | `∏_λ d_λ^(d_λ²)` | probe's constant |
|---|---|---|---|
| 1 | 1, 1 | 1 | 1 |
| 2 | 1, 2, 1 | 16 | `2⁴` |
| 3 | 1, 3, 2, 3, 1 | 6198727824 | `2⁴·3¹⁸` |

The probe obtained its constants by factoring exact symbolic determinants and did *not* use
this lemma; the agreement is therefore a check on both.  **The assembly itself is not yet
formalised** — that needs the Gram of a product form in a product basis to be block diagonal,
plus the change-of-basis square relating the matrix-unit basis to `T_w`.  Both are the
natural next steps and neither is claimed here.

## What this is a step toward, and what it is NOT

Geck–Pfeiffer 7.2.6 gives `det(Gram) = ∏_λ (Schur_λ)^{f^λ}`.  The measured values
(`computations/hecke/tw_gram_determinant_probe.py`, exact arithmetic) factor as an integer
constant `∏_λ d_λ^(d_λ²)` times a `q`-part.  This file supplies the block form that the
*integer constant* comes from.  It says nothing about the `q`-part, which is where the Schur
elements live, and it is not a proof of Geck–Pfeiffer.
-/

namespace QOU.MathlibExt

open LinearMap Matrix

variable {K : Type*} [Field K] {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **Reading a square matrix by its columns**: `colEquiv K ι X j` is column `j` of `X`.

This is the identification under which left multiplication becomes block-diagonal. -/
def colEquiv (K : Type*) [Field K] (ι : Type*) : Matrix ι ι K ≃ₗ[K] (ι → (ι → K)) where
  toFun X := fun j i => X i j
  invFun v := Matrix.of fun i j => v j i
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  left_inv _ := rfl
  right_inv _ := rfl

omit [Fintype ι] [DecidableEq ι] in
@[simp] theorem colEquiv_apply (X : Matrix ι ι K) (j i : ι) :
    colEquiv K ι X j i = X i j := rfl

/-- **Left multiplication is block-diagonal over the columns.**

Column `j` of `M * X` is `M *ᵥ (column j of X)`, with the *same* `M` in every block — so
`lmul M` is `card ι` copies of `M.mulVecLin`, conjugated by `colEquiv`. -/
theorem colEquiv_lmul (M : Matrix ι ι K) :
    piDiag (fun _ : ι => M.mulVecLin)
      = (colEquiv K ι).conj (Algebra.lmul K (Matrix ι ι K) M) := by
  refine LinearMap.ext fun v => ?_
  funext j i
  simp [piDiag_apply, LinearEquiv.conj_apply, colEquiv, Matrix.mulVec, dotProduct,
    Matrix.mul_apply]

/-- **The trace of left multiplication on a matrix algebra**: `card ι` copies of the ordinary
matrix trace, one per column. -/
theorem trace_lmul_matrix (M : Matrix ι ι K) :
    LinearMap.trace K (Matrix ι ι K) (Algebra.lmul K (Matrix ι ι K) M)
      = (Fintype.card ι : K) * M.trace := by
  have hblock := colEquiv_lmul M
  have hpi := trace_piDiag (K := K) (ι := ι) (M := fun _ : ι => (ι → K))
    (fun _ => M.mulVecLin)
  rw [hblock, LinearMap.trace_conj'] at hpi
  have hcol : LinearMap.trace K (ι → K) M.mulVecLin = M.trace := by
    rw [← Matrix.toLin'_apply']
    exact Matrix.trace_toLin'_eq M
  rw [hpi, hcol, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]

/-- **The regular trace form of a matrix algebra is `d ·` the matrix trace.**

The sharp form of what `regTraceForm_one_one` gives only on the diagonal.  Every statement
this corpus makes about the form degenerating "exactly when `char K ∣ d`" is a corollary of
this together with nondegeneracy of `tr`. -/
theorem regTraceForm_matrix (x y : Matrix ι ι K) :
    regTraceForm K (Matrix ι ι K) x y = (Fintype.card ι : K) * (x * y).trace := by
  rw [regTraceForm, trace_lmul_matrix]

/-- **Consistency check between the two routes, kept as a regression.**

`regTraceForm_one_one` (proved from `L_1 = id` and `LinearMap.trace_id`) says
`B(1,1) = finrank K A`.  `regTraceForm_matrix` (proved from the column block decomposition
and `trace_piDiag`) says `B(1,1) = d · tr 1 = d · d`.  The two arguments share nothing, so
their agreement — `finrank K (Matrix ι ι K) = d²` — is a real cross-check on both.  A dropped
factor or a wrong index set in either would show up here. -/
theorem card_mul_trace_one_eq_finrank_matrix :
    (Fintype.card ι : K) * ((1 : Matrix ι ι K) * 1).trace
      = (Module.finrank K (Matrix ι ι K) : K) :=
  (regTraceForm_matrix (K := K) (ι := ι) 1 1).symm.trans regTraceForm_one_one

/-! ### The Gram determinant of a single block -/

/-- **The matrix-unit Gram entries**: `tr(E_ij · E_kl) = δ_{jk} δ_{il}`, so the regular trace
form pairs `E_ij` with `E_ji` and nothing else. -/
theorem regTraceForm_single (i j k l : ι) :
    regTraceForm K (Matrix ι ι K) (Matrix.single i j 1) (Matrix.single k l 1)
      = (Fintype.card ι : K) * (if (j, i) = (k, l) then 1 else 0) := by
  rw [regTraceForm_matrix]
  congr 1
  rcases eq_or_ne j k with rfl | hjk
  · rcases eq_or_ne i l with rfl | hil
    · simp
    · simp [Matrix.trace_single_eq_of_ne _ _ _ hil, Prod.ext_iff, hil]
  · simp [Prod.ext_iff, hjk]

/-- **The Gram matrix of a block, in the matrix-unit basis, is `d •` the identity with its
rows permuted by the transpose involution.** -/
theorem regTraceGram_stdBasis_eq (K : Type*) [Field K] (ι : Type*) [Fintype ι] [DecidableEq ι] :
    BilinForm.toMatrix (Matrix.stdBasis K ι ι) (regTraceBilin K (Matrix ι ι K))
      = (((Fintype.card ι : K) • (1 : Matrix (ι × ι) (ι × ι) K)).submatrix
          ⇑(Equiv.prodComm ι ι) _root_.id) := by
  ext p q
  obtain ⟨i, j⟩ := p
  obtain ⟨k, l⟩ := q
  rw [BilinForm.toMatrix_apply, Matrix.stdBasis_eq_single, Matrix.stdBasis_eq_single,
    regTraceBilin_apply, regTraceForm_single]
  simp [Matrix.submatrix_apply, Matrix.one_apply, Equiv.prodComm]

/-- **The block Gram determinant is `± d^(d²)`, sorry-free.**

This is where the integer constant of the Gram determinant comes from.
`computations/hecke/tw_gram_determinant_probe.py` measures that constant as
`∏_λ d_λ^(d_λ²)` at `n = 1, 2, 3` and identifies it empirically; the per-block factor
`d^(d²)` is derived here, from `tr(E_ij · E_kl) = δ_{jk} δ_{il}` and nothing else.

The sign is the signature of the transpose involution on `ι × ι`. -/
theorem regTraceGram_stdBasis_det (K : Type*) [Field K] (ι : Type*) [Fintype ι] [DecidableEq ι] :
    (BilinForm.toMatrix (Matrix.stdBasis K ι ι) (regTraceBilin K (Matrix ι ι K))).det
      = Equiv.Perm.sign (Equiv.prodComm ι ι)
          * (Fintype.card ι : K) ^ (Fintype.card ι * Fintype.card ι) := by
  rw [regTraceGram_stdBasis_eq, Matrix.det_permute, Matrix.det_smul, Matrix.det_one, mul_one,
    Fintype.card_prod]

/-- **The block Gram determinant vanishes exactly in the bad characteristic.**

`d^(d²) = 0` in `K` iff `d = 0` in `K`, so this is the sharp form of the obstruction that
`docs/audits/2026-08-30-tw-gram-determinant-measured.md` states — and the reason the
determinant route can never certify semisimplicity when `char K ∣ d`. -/
theorem regTraceGram_stdBasis_det_ne_zero_iff (K : Type*) [Field K] (ι : Type*) [Fintype ι]
    [DecidableEq ι] [Nonempty ι] :
    (BilinForm.toMatrix (Matrix.stdBasis K ι ι) (regTraceBilin K (Matrix ι ι K))).det ≠ 0
      ↔ (Fintype.card ι : K) ≠ 0 := by
  rw [regTraceGram_stdBasis_det]
  constructor
  · intro h hd
    exact h (by rw [hd, zero_pow (by positivity), mul_zero])
  · intro hd
    refine mul_ne_zero ?_ (pow_ne_zero _ hd)
    rcases Int.units_eq_one_or (Equiv.Perm.sign (Equiv.prodComm ι ι)) with h | h <;> simp [h]

end QOU.MathlibExt
