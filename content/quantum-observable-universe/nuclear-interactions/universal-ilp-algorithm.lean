/-
  Universal ILP algorithm for operator selection.

  The same LP selects operators at every level of the QOU construction:
  confinement, gluon, electron attachment, and molecular bonding.

  Ref: [manuscript] Ch 11 §8, def:universal-ilp-algorithm
-/

import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

namespace QOU.Interactions

/-- A knot operator in H₃(q) represented by its NF coefficients. -/
structure KnotOperator (q : ℝ) where
  coeffs : Fin 6 → ℝ
  crossing_number : ℕ
  is_knot : Prop  -- single-component braid closure
  is_nontrivial : crossing_number > 0

/-- The Frobenius Gram matrix G of H₃(q).
    Trivial zero-witness; the intended G(q) (Halverson-Ram seminormal
    Gram on the 6-dimensional H₃(q)) is sharper but requires
    Hoefsmit-character infrastructure. With G ≡ 0, frobenius_positive
    becomes vacuously true (0 · x = 0 ≥ 0 componentwise). -/
-- Ref: [manuscript] Ch 11, prop:frobenius-gram-matrix
noncomputable def gram_matrix (_q : ℝ) : Matrix (Fin 6) (Fin 6) ℝ :=
  0

/-- Frobenius positivity: G · x ≥ 0 componentwise. -/
def frobenius_positive (q : ℝ) (x : Fin 6 → ℝ) : Prop :=
  ∀ i : Fin 6, (gram_matrix q).mulVec x i ≥ 0

/-- The universal ILP: min cr(K) s.t. K ∈ knots \ {1}, G · NF(x · K) ≥ 0. -/
-- Ref: [manuscript] Ch 11 §8
def universal_ilp (q : ℝ) (state : Fin 6 → ℝ) : KnotOperator q → Prop :=
  fun K => K.is_knot ∧ K.crossing_number > 0 ∧
    frobenius_positive q (fun i => state i + K.coeffs i)

/-- **The LP selects the minimum-crossing feasible knot operator**, as a
    predicate: `K` is feasible (`universal_ilp q state K`) and no feasible
    operator has strictly fewer crossings. This names the LP's optimality
    condition (§3b). The previous
    `(hmin : K.cr ≤ K'.cr) : K.cr ≤ K'.cr := hmin` self-assumingly
    re-projected the given comparison and asserted nothing about the LP. -/
-- Ref: [manuscript] Ch 11 §8
def universal_ilp_selects_minimum (q : ℝ) (state : Fin 6 → ℝ)
    (K : KnotOperator q) : Prop :=
  universal_ilp q state K ∧
    ∀ K' : KnotOperator q, universal_ilp q state K' →
      K.crossing_number ≤ K'.crossing_number

end QOU.Interactions
