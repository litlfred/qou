import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic


/-!
# Commutative limit kills chirality

In the commutative QOU specialisation (q → 1), the Hecke parameter
H_A = q - q⁻¹ vanishes, so the chirality term H_A²·Φ₃ in the
Wedderburn mass formula vanishes identically. The atomic mass
formula reduces to two S-even terms.

This is a corollary of the Frobenius S-classification: chirality
is the unique S-anti-invariant channel; the commutative limit
makes the antipode trivial (S = id), so any S-odd quantity must
vanish.

-- Ref: [leitner2026] cor:commutative-chirality-vanishes
-/

namespace QOU.WedderburnMass

/-- The Hecke parameter H_A as a function of q. -/
noncomputable def H_A (q : ℝ) : ℝ := q - q⁻¹

/-- H_A is continuous away from q = 0, and H_A(1) = 0. -/
theorem H_A_at_one : H_A 1 = 0 := by
  unfold H_A
  simp

/-- H_A is continuous on a neighborhood of q = 1 (away from q = 0). -/
theorem H_A_continuousAt_one : ContinuousAt H_A 1 := by
  -- H_A q = q - q⁻¹.  Both q and q⁻¹ are continuous at 1 (since 1 ≠ 0).
  unfold H_A
  exact continuousAt_id.sub (continuousAt_inv₀ (one_ne_zero))

/-- H_A² → 0 as q → 1. -/
theorem H_A_sq_tends_to_zero :
    Filter.Tendsto (fun q => (H_A q) ^ 2) (nhds 1) (nhds 0) := by
  -- (H_A q)^2 is continuous at 1, and (H_A 1)^2 = 0.
  have h0 : (H_A 1) ^ 2 = 0 := by rw [H_A_at_one]; ring
  have h_cont : ContinuousAt (fun q => (H_A q) ^ 2) 1 :=
    (H_A_continuousAt_one).pow 2
  -- Continuous at 1 means tendsto along nhds 1 to value at 1; rewrite to 0.
  have := h_cont.tendsto
  rw [h0] at this
  exact this

/-- **Corollary (chirality vanishes in commutative limit).**
    For any chirality function Φ₃ that is continuous at q = 1
    (or merely tendsto a finite limit), the product H_A²·Φ₃ tends
    to zero as q → 1. -/
theorem commutative_chirality_vanishes
    (Φ₃ : ℝ → ℝ) (L : ℝ) (h_lim : Filter.Tendsto Φ₃ (nhds 1) (nhds L)) :
    Filter.Tendsto (fun q => (H_A q) ^ 2 * Φ₃ q) (nhds 1) (nhds 0) := by
  -- (H_A q)^2 → 0 and Φ₃ → L, so product → 0 · L = 0.
  have h_sq : Filter.Tendsto (fun q => (H_A q) ^ 2) (nhds 1) (nhds 0) :=
    H_A_sq_tends_to_zero
  have := h_sq.mul h_lim
  -- This gives tendsto of (H_A q)^2 * Φ₃ q to 0 * L = 0.
  simpa using this

/-- The classical (commutative) atomic-mass binding correction
    has only two terms (Φ₁ and Φ₂), the chirality term having
    vanished. -/
noncomputable def commutativeBindingCorrection
    (α Φ₁ Φ₂ : ℝ) : ℝ :=
  α * (Φ₁ - 6 * Φ₂)
  -- Note: lim_{q→1} [3]_q = 3, so -2[3]_q → -6.

end QOU.WedderburnMass
