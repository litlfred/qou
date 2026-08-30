/-
# QOU.MassTheory.TemperleyLiebSpinHalf — the concrete spin-½ TL relations (qou-v7ro, brick 1 of the instance)

The ∀A Milnor deficit recursion `D_{A+1}=−h²(h²+2)D_A` is proved mathematically (audit
`docs/audits/2026-08-30-milnor-recursion-forall-A-PROVED.md`) and its field-algebra core is Lean
(`QOU.MassTheory.DeficitRecursionReduction`). The remaining Lean obligation is to formalize the
Temperley–Lieb machinery the proof rests on and thereby discharge the `BrunnianDeficitRecursion`
instance for real. This file is **brick 1**: the concrete spin-½ (2-dim) building blocks and the
atomic relations, over a generic field — no `sorry`, no axiom.

What is proved here (all `ring`/`field_simp` over `[Field K]`, `q ≠ 0`):

* `eTL = q•1 − R` — the TL generator is `q − R` for the Hecke R-matrix.
* `eTL_mul_eTL` — the defining TL relation `e² = [2]·e`, `[2] = q + 1/q`.
* `ptr_muInv_eTL = 1` — the **cap-cup contraction with weight μ⁻¹ is the identity**. This is the
  crux weight of the ∀A proof (the μ→μ⁻¹ correction): the clean sub-lemma is stated for `μ⁻¹`.
* `ptr_mu_eTL = diag(q⁻², q²)` — with the *other* weight μ it is NOT the identity, which is exactly
  why the proof must use μ⁻¹.
* `band = q²•1 − h·e`, `bandInv = q⁻²•1 + h·e`, and `band_mul_bandInv = 1` — the band generator
  `σ² = A_{i,i+1}` and its inverse, `h = q − 1/q`.

Scope: this is the 2-strand / 4-dim (`V ⊗ V`) layer. The ∀n tensor-power quantum trace, the
Brunnian word `ρ(w_n)`, and the induction that composes these relations remain to be formalized —
that is the rest of the instance, not discharged here. Indexing convention: `Fin 4 ≅ V ⊗ V` as
`|00⟩=0, |01⟩=1, |10⟩=2, |11⟩=3`; the partial trace is over the second tensor factor.
-/
import Mathlib.Tactic
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation

namespace QOU.MassTheory.TemperleyLiebSpinHalf

open Matrix

variable {K : Type*} [Field K]

/-- The Hecke R-matrix on `V ⊗ V` (spin-½), eigenvalues `q` and `−1/q`. -/
def Rmat (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0;
     0, q - 1/q, 1, 0;
     0, 1, 0, 0;
     0, 0, 0, q]

/-- The Temperley–Lieb generator `e` on `V ⊗ V`. -/
def eTL (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![0, 0, 0, 0;
     0, 1/q, -1, 0;
     0, -1, q, 0;
     0, 0, 0, 0]

/-- The quantum integer `[2] = q + 1/q`. -/
def twoQ (q : K) : K := q + 1/q

/-- Partial trace over the **second** tensor factor with a diagonal weight `diag(w0, w1)`:
`(ptr X)_{a,b} = w0·X_{2a,2b} + w1·X_{2a+1,2b+1}`. -/
def ptrLast (w0 w1 : K) (X : Matrix (Fin 4) (Fin 4) K) : Matrix (Fin 2) (Fin 2) K :=
  !![w0 * X 0 0 + w1 * X 1 1, w0 * X 0 2 + w1 * X 1 3;
     w0 * X 2 0 + w1 * X 3 1, w0 * X 2 2 + w1 * X 3 3]

/-- `e = q•1 − R`: the TL generator is `q` minus the R-matrix. -/
theorem eTL_eq (q : K) : eTL q = q • (1 : Matrix (Fin 4) (Fin 4) K) - Rmat q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [eTL, Rmat, Matrix.smul_apply]

/-- The defining TL relation: `e² = [2]·e`. -/
theorem eTL_mul_eTL (q : K) (hq : q ≠ 0) :
    eTL q * eTL q = twoQ q • eTL q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [eTL, twoQ, Matrix.mul_apply, Fin.sum_univ_four, Matrix.smul_apply] <;>
    field_simp <;> ring

/-- **The cap-cup sub-lemma with the correct weight μ⁻¹ = diag(1/q, q): `ptr_{μ⁻¹}(e) = 1`.** -/
theorem ptr_muInv_eTL (q : K) (hq : q ≠ 0) :
    ptrLast (1/q) q (eTL q) = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [ptrLast, eTL] <;> field_simp

/-- With the *other* weight μ = diag(q, 1/q), the contraction is `diag(q⁻², q²)`, NOT the identity —
the reason the proof must use μ⁻¹. -/
theorem ptr_mu_eTL (q : K) (hq : q ≠ 0) :
    ptrLast q (1/q) (eTL q) = !![1/q^2, 0; 0, q^2] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [ptrLast, eTL] <;> field_simp

/-- The band generator `σ² = A_{i,i+1} = q²·1 − h·e`, with `h = q − 1/q`. -/
def band (q : K) : Matrix (Fin 4) (Fin 4) K :=
  q^2 • (1 : Matrix (Fin 4) (Fin 4) K) - (q - 1/q) • eTL q

/-- The inverse band `q⁻²·1 + h·e`. -/
def bandInv (q : K) : Matrix (Fin 4) (Fin 4) K :=
  (1/q^2) • (1 : Matrix (Fin 4) (Fin 4) K) + (q - 1/q) • eTL q

/-- `band · bandInv = 1`: the band is invertible with the stated inverse (uses `e² = [2]e`). -/
theorem band_mul_bandInv (q : K) (hq : q ≠ 0) :
    band q * bandInv q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [band, bandInv, eTL, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply,
      Matrix.smul_apply, Matrix.add_apply, Matrix.sub_apply] <;>
    field_simp <;> ring

end QOU.MassTheory.TemperleyLiebSpinHalf
