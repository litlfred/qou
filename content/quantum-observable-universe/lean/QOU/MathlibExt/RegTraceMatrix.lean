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

end QOU.MathlibExt
