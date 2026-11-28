import QOU.BringsSurface.BringConeIcosahedral
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

/-!
# Quaternion conjugation: orientation reversal that swaps left and right

Bean `qou-h0zz` (owner, 2026-11-28: "Should also look at the quaternions and the actions
there"). On the model cone `BringCone R = Quaternion R` (generic `CommRing R`, §7c):

1. `star_leftMul`, `star_rightMul`: conjugation `p ↦ p̄` intertwines left multiplication by `q`
   with right multiplication by `q̄`. It swaps the two `SU(2)` factors of `Spin(4)`.
2. `star_coord_det`: on coordinates `(a, b, c, d)` conjugation is `diag(1, −1, −1, −1)`, of
   determinant `−1`. It reverses the orientation of `ℍ = ℝ⁴`.
3. `leftMul_det`: the coordinate matrix of left multiplication by `q` has determinant
   `(normSq q)²`, so a unit quaternion acts preserving orientation.
4. `star_chiralGammaU`: conjugating the chirality grading `Γ_u = L_u ∘ M_i` by `star` gives
   `p ↦ i p u`, with the left and right units exchanged. For the canonical `u = i` it is `Γ_i`
   again (`star_chiralGamma`), so **`star` does not flip the cone's chirality grading.**
5. `leftMul_star_flips`: if a unit `w` anticommutes with `i`, then `L_w ∘ star` reverses
   orientation (det `−1`) and sends `Γ_i` to `−Γ_i`, flipping both at once.

## Reading

In `prop:hypercharge-sign-is-bring-orientation` the hypercharge sign is the orientation bit of
Bring's surface. On the cone there are two orientation-type operations. `star` reverses
orientation but keeps `Γ_i`; `L_w` for a perpendicular unit `w` (for example in `2I`) flips `Γ_i`
but keeps orientation (`leftMul_flips_chiralGammaU`). The composite `L_w ∘ star` does both.
So the cone chirality matches the hypercharge sign exactly when Bring's reflection acts on the
cone as `L_w ∘ star` rather than as `star`. Which one it is depends on how `S₅ × C₂` acts on the
cone, and the corpus does not yet establish that action (see `BringConeIcosahedral.lean`).
Like the complex volume, the quaternions place the bit; they do not fix it.

Ring arithmetic only. No empirical value enters.
-/

namespace QOU.Tetraplectic

open Matrix

variable {R : Type*} [CommRing R]

/-- The unit `i`. -/
def qI : BringCone R := ⟨0, 1, 0, 0⟩

theorem star_qI : star (qI : BringCone R) = -qI := by ext <;> simp [qI]

/-- **Conjugation turns left multiplication by `q` into right multiplication by `q̄`.** -/
theorem star_leftMul (q p : BringCone R) : star (q * p) = star p * star q := StarMul.star_mul q p

/-- And right into left. -/
theorem star_rightMul (q p : BringCone R) : star (p * q) = star q * star p := StarMul.star_mul p q

/-- Coordinates of a quaternion. -/
def coord (p : BringCone R) : Fin 4 → R := ![p.re, p.imI, p.imJ, p.imK]

/-- Conjugation in coordinates is `diag(1, −1, −1, −1)`. -/
theorem coord_star (p : BringCone R) :
    coord (star p) = Matrix.diagonal ![1, -1, -1, -1] *ᵥ coord p := by
  funext k; fin_cases k <;> simp [coord, Matrix.mulVec, dotProduct, Fin.sum_univ_four,
    Matrix.diagonal_apply]

/-- **Conjugation reverses orientation:** its coordinate matrix has determinant `−1`. -/
theorem star_coord_det : (Matrix.diagonal ![(1 : R), -1, -1, -1]).det = -1 := by
  simp [Matrix.det_diagonal, Fin.prod_univ_four]

/-- Coordinate matrix of left multiplication by `q = (a, b, c, d)`. -/
def leftMulMat (q : BringCone R) : Matrix (Fin 4) (Fin 4) R :=
  !![q.re, -q.imI, -q.imJ, -q.imK;
     q.imI, q.re, -q.imK, q.imJ;
     q.imJ, q.imK, q.re, -q.imI;
     q.imK, -q.imJ, q.imI, q.re]

theorem coord_leftMul (q p : BringCone R) : coord (q * p) = leftMulMat q *ᵥ coord p := by
  funext k
  fin_cases k <;> simp [coord, leftMulMat, Matrix.mulVec, dotProduct, Fin.sum_univ_four] <;> ring

/-- **Left multiplication by `q` has determinant `(normSq q)²`.** -/
theorem leftMul_det (q : BringCone R) : (leftMulMat q).det = (Quaternion.normSq q) ^ 2 := by
  rw [Quaternion.normSq_def']
  simp [leftMulMat, Matrix.det_succ_row_zero, Fin.sum_univ_succ, Fin.succAbove]
  ring

/-- **`star` conjugates `Γ_u` to `p ↦ i p u`**: the left and right units are exchanged. -/
theorem star_chiralGammaU (u p : BringCone R) (hu : star u = -u) :
    star (chiralGammaU u (star p)) = qI * p * u := by
  have hr : ∀ x : BringCone R, reebM_i x = x * qI := fun x => rfl
  simp only [chiralGammaU, leftMul, hr, StarMul.star_mul, star_star, hu, star_qI]
  noncomm_ring

/-- **`star` keeps the canonical chirality grading `Γ_i`.** -/
theorem star_chiralGamma (p : BringCone R) :
    star (chiralGammaU qI (star p)) = chiralGammaU qI p := by
  rw [star_chiralGammaU _ _ star_qI]
  show qI * p * qI = qI * (p * qI)
  rw [mul_assoc]

/-- **`L_w ∘ star` flips `Γ_i` when `w` is a unit anticommuting with `i`.** Together with
`star_coord_det` and `leftMul_det` it reverses orientation and flips chirality at once. -/
theorem leftMul_star_flips (w p : BringCone R) (hw : star w * w = 1) (hww : w * star w = 1)
    (hanti : w * qI = -(qI * w)) :
    w * star (chiralGammaU qI (star (star w * p))) = -(chiralGammaU qI p) := by
  rw [star_chiralGamma]
  have hanti' : qI * star w = -(star w * qI) := by
    calc qI * star w = (star w * w) * qI * star w := by rw [hw, one_mul]
      _ = star w * (w * qI) * star w := by noncomm_ring
      _ = star w * (-(qI * w)) * star w := by rw [hanti]
      _ = -(star w * qI * (w * star w)) := by noncomm_ring
      _ = -(star w * qI) := by rw [hww, mul_one]
  have hr : ∀ x : BringCone R, reebM_i x = x * qI := fun x => rfl
  simp only [chiralGammaU, leftMul, hr]
  calc w * (qI * (star w * p * qI)) = w * ((qI * star w) * p * qI) := by noncomm_ring
    _ = w * (-(star w * qI) * p * qI) := by rw [hanti']
    _ = -((w * star w) * (qI * (p * qI))) := by noncomm_ring
    _ = -(qI * (p * qI)) := by rw [hww, one_mul]

end QOU.Tetraplectic
