import Mathlib.Algebra.Ring.Defs
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Ring.Int.Defs
import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.Ring

/-!
# Unit-modulus eigenvalues on V_{(2,1)} and Borromean fixed point

## Main results

1. **Hecke determinant**: `det(σ) = q·(−q⁻¹) = −1` on every 2-dim
   Wedderburn block (the eigenvalues of `σ` are `q`, `−q⁻¹`).
2. **Even-length determinant**: a product of `2k` generators has
   `det = (−1)^{2k} = 1`, so its eigenvalues satisfy `λ₁λ₂ = 1`
   (the unit-circle condition together with `|tr| ≤ 2`).
3. **Borromean trace (corrected 2026-11-16)**: on an explicit model of
   `V_{(2,1)}` the Borromean braid `β_Bor = (σ₁σ₂⁻¹)³` has
   `χ_{(2,1)}(β_Bor) = −(q⁴−q²+1)(q⁸−2q⁶−2q²+1)/q⁶`.  This is `+2` at
   `q = 1`, `≈ 1.994` at the substrate `q₀`, and `−1573/64` at `q = 2`.
   The earlier claim `χ_{(2,1)}(β_Bor) = −2` (eigenvalue `−1`) is false,
   and so is unit modulus for every even word: `σ₁²` has eigenvalues
   `q², q⁻²`.  Also `χ_{(2,1)}(σ₁σ₂) = −1` for every `q`, so with
   `det = 1` its eigenvalues are the primitive cube roots of unity.

## Disposition (integrity)

The previous version carried two `def … : True := trivial`
placeholders (`borromean_trace_21_eq_neg_two`,
`all_positive_trace_positive`) — vacuous, and forbidden by AGENTS.md
§1a. They are removed. The genuine algebraic content is proved:
`hecke_generator_det_neg_one` (generic field) and `even_braid_det_one`.
The later `borromean_eigenvalue_neg_one` concluded `λ = −1` from the
hypothesis `tr_{(2,1)}(β_Bor) = −2`.  That hypothesis is false (see
result 3), so the theorem was removed on 2026-11-16 and replaced by the
explicit-model computation `borromean_trace_standard`.

## Base ring (§7c)

The first two results need no field; they are stated over the weakest class that
admits them, and the previous `[Field R]` is gone.

* `hecke_generator_det_neg_one` is a **units** identity: the eigenvalue
  `−q⁻¹` only makes sense when `q` is invertible, so `q` is carried as a
  unit `q : Rˣ` over a `CommRing` and the inverse is `Units.inv`, not field
  division. Over a field this is exactly the old `q ≠ 0` hypothesis, so no
  generality is lost and `ℤ[q, q⁻¹]` (where `q` *is* a unit) is now in
  scope.
* The explicit model of `V_{(2,1)}` divides by `q` and `q² + 1`, so it is
  stated over a field with those two hypotheses.

Only the integer determinant `(−1)^{2k}` uses `ℤ`. No archimedean structure
is needed — `|λ| = 1` is the narrative reading of `λ₁λ₂ = 1` with
`|tr| ≤ 2`, not a Lean hypothesis here.

-- Ref: [leitner2026] Hecke algebra Wedderburn decomposition
-/

namespace QOU.BraidsAndKnots

/-! ## Hecke generator determinant -/

/-- The Hecke relation `σ² = h·σ + 1` forces `det(σ) = −1` on every
    2-dimensional Wedderburn block: the eigenvalues of `σ` are `q` and
    `−q⁻¹` (roots of `x² − h·x − 1`), with product `q·(−q⁻¹) = −1`.

    §7c: a **units** identity over a plain `CommRing` — the second
    eigenvalue is only defined when `q` is invertible, so `q` is carried as
    `q : Rˣ` and the inverse is `Units.inv`. Over a field this is exactly
    the old `q ≠ 0`; unlike the field version it also applies over
    `ℤ[q, q⁻¹]`, where `q` is a unit but no division is available. -/
-- Ref: [leitner2026] Iwahori-Hecke algebra, det on standard rep
theorem hecke_generator_det_neg_one {R : Type*} [CommRing R] (q : Rˣ) :
    (q : R) * (-(↑q⁻¹ : R)) = -1 := by
  rw [mul_neg, Units.mul_inv]

/-! ## Unit modulus for even-length braids -/

/-- A product of an even number `2k` of Hecke generators on `V_{(2,1)}`
    has determinant `(−1)^{2k} = 1` (each generator contributes `−1`).
    Together with `|tr| ≤ 2` this is the unit-circle condition
    `λ₁λ₂ = 1`. -/
-- Ref: [leitner2026] det(σ₁···σ_{2k}) = (−1)^{2k} = 1
theorem even_braid_det_one (n : ℕ) : (-1 : ℤ) ^ (2 * n) = 1 := by
  simp [pow_mul]

/-! ## Explicit model of `V_{(2,1)}` and the Borromean trace

`σ₁` is diagonal with eigenvalues `q, −q⁻¹`; `σ₂` is the matrix below.
`unitMod_braid` and `unitMod_s2_mul_s2inv` show this is a representation
of `H_3(q)` with `σ₂⁻¹ = σ₂ − (q − q⁻¹)`.  It is the 2-dimensional block,
since `σ₁` has both Hecke eigenvalues. -/

section StandardRep

variable {R : Type*} [Field R]

/-- `σ₁` on `V_{(2,1)}`. -/
def unitModS1 (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 0; 0, -q⁻¹]

/-- `σ₂` on `V_{(2,1)}`. -/
def unitModS2 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  !![-1 / (q * (q ^ 2 + 1)), 1;
     (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2, q ^ 3 / (q ^ 2 + 1)]

/-- `σ₂⁻¹ = σ₂ − h`, from the Hecke relation. -/
def unitModS2inv (q : R) : Matrix (Fin 2) (Fin 2) R :=
  unitModS2 q - (q - q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) R)

theorem unitMod_s2_mul_s2inv (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    unitModS2 q * unitModS2inv q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [unitModS2, unitModS2inv, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

/-- The braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂` holds in the model. -/
theorem unitMod_braid (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    unitModS1 q * unitModS2 q * unitModS1 q = unitModS2 q * unitModS1 q * unitModS2 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [unitModS1, unitModS2, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- `χ_{(2,1)}(σ₁σ₂) = −1` for every `q`. -/
theorem unitMod_trace_s1s2 (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    Matrix.trace (unitModS1 q * unitModS2 q) = -1 := by
  simp [unitModS1, unitModS2, Matrix.trace, Fin.sum_univ_two]
  field_simp; ring

/-- `σ₁σ₂⁻¹` in the model. -/
def unitModBor (q : R) : Matrix (Fin 2) (Fin 2) R :=
  !![-q ^ 4 / (q ^ 2 + 1), q;
     -(q ^ 4 + q ^ 2 + 1) / (q * (q ^ 2 + 1) ^ 2), -1 / (q ^ 2 * (q ^ 2 + 1))]

theorem unitMod_s1_mul_s2inv (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    unitModS1 q * unitModS2inv q = unitModBor q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [unitModS1, unitModS2, unitModS2inv, unitModBor, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

/-- **Borromean trace on `V_{(2,1)}`.**
    `χ_{(2,1)}((σ₁σ₂⁻¹)³) = −(q⁴−q²+1)(q⁸−2q⁶−2q²+1)/q⁶`.
    At `q = 1` this is `2`, so the eigenvalues are near `+1`, not `−1`. -/
-- Ref: [leitner2026] prop:unit-modulus-eigenvalue (corrected 2026-11-16)
theorem borromean_trace_standard (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    Matrix.trace ((unitModS1 q * unitModS2inv q) * (unitModS1 q * unitModS2inv q)
        * (unitModS1 q * unitModS2inv q))
      = -((q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 2 * q ^ 6 - 2 * q ^ 2 + 1)) / q ^ 6 := by
  rw [unitMod_s1_mul_s2inv q hq hq2]
  simp only [unitModBor, Matrix.trace, Matrix.diag, Fin.sum_univ_two, Matrix.mul_apply,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.empty_val', Matrix.cons_val_fin_one]
  field_simp
  ring

end StandardRep

end QOU.BraidsAndKnots
