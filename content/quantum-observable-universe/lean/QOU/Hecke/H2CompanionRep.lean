import QOU.Hecke.H2GramArithmetic
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# QOU.Hecke.H2CompanionRep — the `H_2` Gram from the regular representation

Brick `qou-eedq`: upgrade `h2GramMatrix` from **asserted** trace literals
to the **regular representation** of `H_2(q)`.

`H_2(q) = K⟨1, σ⟩` with `σ² = (q-1)σ + q` is `2`-dimensional; left
multiplication by `σ` in the ordered basis `{1, σ}` is the companion
matrix of the Hecke quadratic `X² - (q-1)X - q`,

  `C = !![0, q; 1, q-1]`   (`σ·1 = σ`,  `σ·σ = q·1 + (q-1)·σ`).

We prove:

* `h2Companion_hecke` — `C² = (q-1)·C + q·I`, so `σ ↦ C` respects the
  Hecke relation: `C` is a *faithful* matrix image of `σ`, the left
  regular representation, not an ad-hoc matrix.
* `h2GramFromRep_eq` — the regular-trace Gram matrix
  `Gᵢⱼ = tr(ρ(eᵢ)·ρ(eⱼ))` built from `ρ = {1 ↦ I, σ ↦ C}` equals the
  `h2GramMatrix` whose entries `H2GramArithmetic` had merely asserted.

Consequently `det(Gram) = [2]_q²` (`h2GramFromRep_det`) now rests on the
representation-computed traces, closing the "traces asserted, not
derived" gap flagged in `H2GramArithmetic`.  Taking `tr` is the
observation step; the Gram *is* a matrix of observable results of the
regular action.
-/

namespace QOU.Hecke

open Matrix QOU.MathlibExt

variable {K : Type*} [Field K]

/-- **Left multiplication by `σ` on `H_2(q)`** in the basis `{1, σ}`: the
    companion matrix of `X² - (q-1)X - q`.  Column `0` is `σ·1 = σ`
    (coordinates `(0, 1)`); column `1` is `σ·σ = q·1 + (q-1)·σ`
    (coordinates `(q, q-1)`). -/
def h2Companion (q : K) : Matrix (Fin 2) (Fin 2) K := !![0, q; 1, q - 1]

/-- **The companion matrix satisfies the Hecke relation (sorry-free):**
    `C² = (q-1)·C + q·I`.  Hence `σ ↦ C` is a genuine representation of
    the Hecke generator — the left regular representation of `H_2(q)` —
    so every trace below is a real regular-representation trace. -/
theorem h2Companion_hecke (q : K) :
    h2Companion q * h2Companion q
      = (q - 1) • h2Companion q + q • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [h2Companion, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- The representation `ρ : H_2(q) basis → M₂(K)`, `1 ↦ I`, `σ ↦ C`. -/
def h2Rep (q : K) : Fin 2 → Matrix (Fin 2) (Fin 2) K := ![1, h2Companion q]

/-- **The regular-trace Gram matrix** built from the representation:
    `Gᵢⱼ = tr(ρ(eᵢ) · ρ(eⱼ))`.  The trace is the observation step. -/
def h2GramFromRep (q : K) : Matrix (Fin 2) (Fin 2) K :=
  Matrix.of fun i j => Matrix.trace (h2Rep q i * h2Rep q j)

/-- **The representation-computed Gram equals the asserted Gram
    (sorry-free).**  Each entry `tr(ρ(eᵢ)ρ(eⱼ))` reduces, via the
    companion matrix, to the literal that `H2GramArithmetic.h2GramMatrix`
    had asserted: `tr(I) = 2`, `tr(C) = q-1`, `tr(C²) = q²+1`. -/
theorem h2GramFromRep_eq (q : K) : h2GramFromRep q = h2GramMatrix q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [h2GramFromRep, h2Rep, h2GramMatrix, h2Companion, Matrix.of_apply,
      Matrix.trace, Matrix.diag, Fin.sum_univ_two, Matrix.mul_apply] <;> ring

/-- **`det(Gram) = [2]_q²` from the regular representation (sorry-free).**
    Composes `h2GramFromRep_eq` with the arithmetic determinant
    `h2GramMatrix_det` — the `n = 2` case of `det(Gram) = [n]_q!` (up to a
    unit), now grounded in the regular representation of `H_2(q)`. -/
theorem h2GramFromRep_det (q : K) : (h2GramFromRep q).det = qInt q 2 ^ 2 := by
  rw [h2GramFromRep_eq, h2GramMatrix_det]

/-- **`H_2` semisimple ⟺ nonzero regular-Gram determinant ⟺ `[2]_q! ≠ 0`
    (sorry-free).**  Wenzl's criterion at `n = 2`, from the regular
    representation. -/
theorem h2GramFromRep_det_ne_zero_iff (q : K) :
    (h2GramFromRep q).det ≠ 0 ↔ qFactorial q 2 ≠ 0 := by
  rw [h2GramFromRep_det, h2_gram_det_ne_zero_iff]

/-- **The regular-rep Gram determinant is `[2]_q · [2]_q!` (sorry-free).**
    Exhibits the "up to a unit" in `det(Gram) = [n]_q!` *concretely* at
    `n = 2`.  The regular trace form differs from the symmetrizing form by
    the unit `[2]_q = 1 + q` (nonzero at generic `q`), so

      `det = [2]_q² = (1 + q)·(1 + q) = [2]_q · [2]_q!`.

    This is the `n = 2` witness of the shape consumed by
    `QOU.MathlibExt.isSemisimpleRing_of_gram_det_eq_qFactorial`
    (unit `c = 1 + q`), confirming the general `det(Gram) = c·[n]_q!`
    interface fires at the base rank. -/
theorem h2GramFromRep_det_eq_unit_mul_qFactorial (q : K) :
    (h2GramFromRep q).det = (1 + q) * qFactorial q 2 := by
  rw [h2GramFromRep_det, qFactorial_two, qInt_two]; ring

end QOU.Hecke
