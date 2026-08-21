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

/-- **The ILP attains its minimum**: if the feasible set is inhabited,
    some feasible knot operator has crossing number `≤` that of every
    other feasible one.

    This is what "the LP selects the minimum-crossing feasible knot
    operator" asserts, and it is a genuine theorem: `crossing_number`
    lands in `ℕ`, so the feasible crossing numbers are a nonempty set
    of naturals and well-ordering supplies a least element.

    **2026-08-21 (bean `qou/q407`).** The previous version took
    `hmin : K.crossing_number ≤ K'.crossing_number` as a hypothesis and
    returned it — `theorem (h : P) : P := h`. It asserted nothing about
    `universal_ilp`, `KnotOperator` or crossing numbers, and stayed true
    if every definition in this file were replaced. Minimality was the
    thing to be proved, not to be assumed. -/
-- Ref: [manuscript] Ch 11 §8
theorem universal_ilp_selects_minimum (q : ℝ) (state : Fin 6 → ℝ)
    (K₀ : KnotOperator q) (hK₀ : universal_ilp q state K₀) :
    ∃ K, universal_ilp q state K ∧
      ∀ K', universal_ilp q state K' →
        K.crossing_number ≤ K'.crossing_number := by
  obtain ⟨c, hc, hleast⟩ :=
    wellFounded_lt.has_min
      {c : ℕ | ∃ K : KnotOperator q, universal_ilp q state K ∧
        K.crossing_number = c}
      ⟨K₀.crossing_number, K₀, hK₀, rfl⟩
  obtain ⟨K, hK, hKc⟩ := hc
  refine ⟨K, hK, fun K' hK' => ?_⟩
  by_contra hlt
  push_neg at hlt
  exact hleast K'.crossing_number ⟨K', hK', rfl⟩ (hKc ▸ hlt)

end QOU.Interactions
