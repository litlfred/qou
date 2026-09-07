import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Algebra.Polynomial.Degree.Definitions
import Mathlib.FieldTheory.IsAlgClosed.Basic
import Mathlib.Algebra.Polynomial.Splits
import Mathlib.Analysis.Complex.Polynomial.Basic

noncomputable section

open Complex Polynomial

namespace QOU.BringsSurface

/-- Bring's curve equation `y^5 + y + x = 0` -/
def bringsCurve (x y : ℂ) : Prop :=
  y^5 + y + x = 0

/-- Turning points are where `dx/dy = 0` on Bring's curve, giving `5y^4 + 1 = 0` -/
def isTurningPoint (y : ℂ) : Prop :=
  5 * y^4 + 1 = 0

/-- The x-coordinate at a turning point satisfies `x = -(4/5) * y` -/
theorem turning_point_x (x y : ℂ) (hc : bringsCurve x y) (ht : isTurningPoint y) :
    x = - (4 / 5) * y := by
  dsimp [bringsCurve] at hc
  dsimp [isTurningPoint] at ht
  have h1 : 5 * y^4 = -1 := by linear_combination ht
  have h2 : 5 * y^5 = -y := by calc
    5 * y^5 = (5 * y^4) * y := by ring
    _ = -1 * y := by rw [h1]
    _ = -y := by ring
  have h3 : x = -y^5 - y := by linear_combination hc
  calc x = -y^5 - y := h3
    _ = - (1 / 5) * (5 * y^5) - y := by ring
    _ = - (1 / 5) * (-y) - y := by rw [h2]
    _ = - (4 / 5) * y := by ring

/-- The polynomial whose roots are the turning points -/
def turningPointPoly : ℂ[X] :=
  C 5 * X^4 + C 1

/-- There are exactly 4 turning points, counted with multiplicity -/
theorem turning_point_count :
    turningPointPoly.roots.card = 4 := by
  have hs : Splits (RingHom.id ℂ) turningPointPoly := IsAlgClosed.splits_codomain turningPointPoly
  have h_map : map (RingHom.id ℂ) turningPointPoly = turningPointPoly := Polynomial.map_id
  have h_deg : turningPointPoly.natDegree = 4 := by
    dsimp [turningPointPoly]
    have h1 : (C (5 : ℂ) * X^4).natDegree = 4 := by
      rw [natDegree_C_mul_X_pow]
      exact (by norm_num : (5 : ℂ) ≠ 0)
    have h2 : (C (1 : ℂ)).natDegree = 0 := natDegree_C (1 : ℂ)
    have h3 : (C (1 : ℂ)).natDegree < (C (5 : ℂ) * X^4).natDegree := by
      rw [h1, h2]
      norm_num
    rw [natDegree_add_eq_left_of_natDegree_lt h3, h1]
  have h_card := natDegree_eq_card_roots' hs
  rw [h_map] at h_card
  rw [← h_card, h_deg]

/-- Saddle trajectory phase condition between two turning points i and j

    **`isBPS : Prop` removed 2026-09-07. Its own comment called it a "placeholder
    for `Im ∫_{x_i}^{x_j} (y_i - y_j) dx = 0`", and typed with the *universe*
    `Prop` it asserted nothing — an instance chose the proposition. Neither read
    nor constructed anywhere. Stating it needs the path integral, which is what
    the adjacent comment says is unavailable.** -/
structure SaddleTrajectory where
  yi : ℂ
  yj : ℂ
  hti : isTurningPoint yi
  htj : isTurningPoint yj
  -- Using a sorry'd condition for the integral since actual path integration in Mathlib is complex
  -- condition : Im (∫ (y(x) - yj) dx) = 0

end QOU.BringsSurface
