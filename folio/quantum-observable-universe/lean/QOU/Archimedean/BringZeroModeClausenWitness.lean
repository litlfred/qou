import QOU.Archimedean.EmCouplingBringZeroMode
import QOU.Archimedean.CatalanClausenBridge
import QOU.Knot.Clausen
import Mathlib.Analysis.Real.Pi.Bounds

/-!
# `BringZeroModeBlochClass`: what its field actually asks (issue #7942)

The class field WAS `∃ θ : ℝ, BlochWigner_unit_circle θ = 2/(3π)` (until 2026-11-15).

* `BlochWigner_unit_circle` was a `noncomputable opaque` until 2026-11-15, so
  the field could be neither proved nor refuted.  It is now defined as its
  documented body `Cl_2` (`BlochWignerUnitCircle.lean`).
* With that body, the **old** field (`∃ θ, BlochWigner_unit_circle θ = 2/(3π)`)
  was an **intermediate-value fact**: `Cl_2 0 = 0` and `Cl_2 (π/2) = G > 0.915`
  (Catalan's constant), while `2/(3π) < 2/9`.  So some `θ ∈ [0, π/2]` works.
  This file proves that, sorry-free (`exists_Cl_2_eq_bringZeroModeValue`).
* Because that made the class contentless, the class field was restated
  (owner decision, 2026-11-15) over algebraic Bloch–Wigner combinations; the
  IVT fact above no longer proves it, and the class has no instance.

So the "transcendence obstruction" did **not** bear on the old field: a real
angle always exists.  The obstruction is
about an angle that is a *rational multiple of `π`* (a root-of-unity shape, i.e.
an algebraic Bloch class).  That stronger statement is
`BringZeroModeRootOfUnityClass` below (a one-term, unit-circle case of the
restated field); it is recorded as a conjecture with no instance, and nothing
here proves or refutes it.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-/

namespace QOU.Archimedean

open Real

/-- `2/(3π) < 2/9`, from `π > 3`. -/
theorem bringZeroModeValue_lt : bringZeroModeValue < 2 / 9 := by
  unfold bringZeroModeValue
  have hπ : (3 : ℝ) < Real.pi := by linarith [Real.pi_gt_d2]
  rw [div_lt_div_iff₀ (by positivity) (by norm_num)]
  nlinarith

theorem bringZeroModeValue_pos : 0 < bringZeroModeValue := by
  unfold bringZeroModeValue; positivity

/-- **The Clausen witness.**  There is `θ ∈ [0, π/2]` with
    `Cl₂(θ) = 2/(3π)`, by the intermediate value theorem between
    `Cl₂(0) = 0` and `Cl₂(π/2) = G > 0.915`. -/
theorem exists_Cl_2_eq_bringZeroModeValue :
    ∃ θ ∈ Set.Icc (0 : ℝ) (Real.pi / 2), Cl_2 θ = bringZeroModeValue := by
  have hG : Cl_2 (Real.pi / 2) > 0.915 := by
    rw [← catalan_G_eq_Cl_2_pi_div_two]; exact catalan_G_numerical_bounds.1
  have hmem : bringZeroModeValue ∈ Set.Icc (Cl_2 0) (Cl_2 (Real.pi / 2)) := by
    rw [Cl_2_zero]
    refine ⟨bringZeroModeValue_pos.le, ?_⟩
    have := bringZeroModeValue_lt
    linarith
  obtain ⟨θ, hθ, hval⟩ :=
    intermediate_value_Icc (by positivity) QOU.Knot.continuous_Cl_2.continuousOn hmem
  exact ⟨θ, hθ, hval⟩

/-- **Corrected statement (conjecture, no instance).**  The content the class
    docstring intends: the angle is a rational multiple of `π`, i.e. the Bloch
    class has a root-of-unity shape.  For such `θ`, `Cl₂(θ)` is an `L`-value
    combination, and `Cl₂(θ) = 2/(3π)` would make `π · Cl₂(θ)` rational, which
    is expected to fail; no proof either way is known.  Per §3b-cond there is
    no instance. -/
class BringZeroModeRootOfUnityClass : Prop where
  bring_zero_mode_root_of_unity :
    ∃ r : ℚ, Cl_2 ((r : ℝ) * Real.pi) = bringZeroModeValue

end QOU.Archimedean
