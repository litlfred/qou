import Mathlib.Tactic
import QOU.BringCone

/-!
# Left vs right quaternion multiplication: a one-sided symmetry, and where it stops

Bean `qou-wkcd` (epic `qou-qs0e`, blocks `qou-hlx7`). Route 2 of the weak-chirality
question. On `ℍ`, `Spin(4) = Sp(1) × Sp(1)` acts by `x ↦ a x b`. The model cone
`BringCone R = Quaternion R` has its complex (Reeb) structure on the RIGHT
(`reebM_i p = p · i`), and #7825 builds the polarization `SU(2)` from LEFT
multiplication. Noncommutative-geometry Standard Models get `SU(2)_L` from an `ℍ`
factor acting on one side only. This file tests how far the same mechanism goes here.

## Proved here (generic `[CommRing R]`, §7c; `h2` = "2 is cancellable")

1. **Left multiplication is always complex-linear** for the right complex structure
   (`leftMul_complexLinear`); it is just associativity.
2. **Right multiplication by `b` is complex-linear iff `b` commutes with `i`**
   (`rightMul_complexLinear_iff`), **iff `b ∈ ℂ`** (`comm_unitI_iff`:
   `b.imJ = 0 ∧ b.imK = 0`). For a two-sided map with a unit left factor the same holds
   (`bilateral_complexLinear_iff`). So fixing the complex structure on the right breaks
   `Sp(1) × Sp(1)` to `Sp(1)_left × U(1)_right`: a full `SU(2)` on one side and a `U(1)`
   on the other. This is the shape of `SU(2) × U(1)`, and the same mechanism as the
   `ℍ` factor of `A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ)` in Connes–Chamseddine.
3. **The side is a convention**: quaternion conjugation swaps the two sides
   (`star_bilateral`) and carries the right complex structure to a left one
   (`star_reeb`). This is the Ozma bit, in quaternionic form: the asymmetry is real,
   which side carries it is not.
4. **The left `SU(2)` does not preserve the corpus chirality grading.** Left
   multiplication by `a` commutes with `Γ_u = L_u ∘ M_i` iff `a` commutes with `u`
   (`leftMul_comm_chiralGammaU_iff`). So inside one `ℍ` the left `Sp(1)` MOVES the
   chirality label `u` (the gauge of #7820) and only its `U(1)` stabiliser acts within
   a chirality. A doublet structure "SU(2) on L, trivial on R" is therefore not present
   on a single `ℍ` with this grading; in the NCG models it needs a second space for the
   right-handed singlets (`ℂ ⊕ ℂ`), which is input there.

## What is NOT proved

* That left-multiplication `Sp(1)` is the weak isospin. Scope (a).
* Any map between the quaternion sides and the Hecke eigenlines `P₊ / P₋` of a letter.
  #7825's `no_automorphism_to_orthogonal_pair` shows the polarization action reaches
  only the eigenline pair of a single letter.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [chamseddine-connes-1997] https://doi.org/10.1007/s002200050126
-/

namespace QOU.StandardModel.QuaternionSidedSymmetry

open QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-- Left multiplication commutes with the right complex structure. -/
theorem leftMul_complexLinear (a x : BringCone R) :
    reebM_i (a * x) = a * reebM_i x := by
  simp [reebM_i, mul_assoc]

/-- Right multiplication by `b` is complex-linear iff `b` commutes with `i`. -/
theorem rightMul_complexLinear_iff (b : BringCone R) :
    (∀ x : BringCone R, reebM_i (x * b) = reebM_i x * b) ↔ b * unitI = unitI * b := by
  simp only [reebM_i_eq_mul_unitI]
  constructor
  · intro h; simpa using h 1
  · intro h x; rw [mul_assoc, h, ← mul_assoc]

/-- `b` commutes with `i` iff `b` is complex (`imJ = imK = 0`). -/
theorem comm_unitI_iff (h2 : ∀ x : R, 2 * x = 0 → x = 0) (b : BringCone R) :
    b * unitI = unitI * b ↔ b.imJ = 0 ∧ b.imK = 0 := by
  rw [Quaternion.ext_iff]
  simp [unitI]
  constructor
  · rintro ⟨hj, hk⟩
    refine ⟨h2 _ ?_, h2 _ ?_⟩ <;>
      first | linear_combination hj | linear_combination -hj | linear_combination hk | linear_combination -hk
  · rintro ⟨hj, hk⟩
    simp [hj, hk]

/-- A two-sided map `x ↦ a x b` with unit left factor is complex-linear iff `b` commutes
with `i`. -/
theorem bilateral_complexLinear_iff {a : BringCone R} (ha : star a * a = 1)
    (b : BringCone R) :
    (∀ x : BringCone R, reebM_i (a * x * b) = a * reebM_i x * b) ↔
      b * unitI = unitI * b := by
  rw [← rightMul_complexLinear_iff]
  constructor
  · intro h x
    have := congrArg (star a * ·) (h x)
    simp only [reebM_i_eq_mul_unitI] at this ⊢
    simpa [← mul_assoc, ha] using this
  · intro h x
    simp only [reebM_i_eq_mul_unitI] at h ⊢
    rw [mul_assoc a x b, mul_assoc a (x * unitI) b, mul_assoc, h x, ← mul_assoc,
      ← mul_assoc]

/-- **Quaternion conjugation swaps the two sides.** -/
theorem star_bilateral (a x b : BringCone R) :
    star (a * x * b) = star b * star x * star a := by
  simp [star_mul, mul_assoc]

theorem star_unitI : star (unitI : BringCone R) = -unitI := by
  ext <;> simp [unitI]

/-- **Conjugation carries the right complex structure to a left one**. -/
theorem star_reeb (x : BringCone R) : star (reebM_i x) = -(unitI * star x) := by
  rw [reebM_i_eq_mul_unitI, star_mul, star_unitI, neg_mul]

/-- **The left `SU(2)` moves the chirality label**: `L_a` commutes with
`Γ_u = L_u ∘ M_i` iff `a` commutes with `u`. -/
theorem leftMul_comm_chiralGammaU_iff (a u : BringCone R) :
    (∀ p : BringCone R, a * chiralGammaU u p = chiralGammaU u (a * p)) ↔
      a * u = u * a := by
  simp only [chiralGammaU, QOU.Tetraplectic.leftMul, reebM_i_eq_mul_unitI]
  constructor
  · intro h
    have h1 := congrArg (· * -unitI) (h 1)
    simp only [one_mul, mul_one] at h1
    simpa [mul_assoc, unitI_mul_neg_unitI, unitI_mul_unitI] using h1
  · intro h p
    rw [← mul_assoc, h, mul_assoc, mul_assoc]

end QOU.StandardModel.QuaternionSidedSymmetry
