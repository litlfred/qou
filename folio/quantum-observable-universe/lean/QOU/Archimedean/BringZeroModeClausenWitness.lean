import QOU.Archimedean.EmCouplingBringZeroMode
import QOU.Archimedean.CatalanClausenBridge
import QOU.Knot.Clausen
import Mathlib.Analysis.Real.Pi.Bounds

/-!
# `BringZeroModeBlochClass`: what its field actually asks (issue #7942)

The class field is `∃ θ : ℝ, BlochWigner_unit_circle θ = 2/(3π)`.

* `BlochWigner_unit_circle` was a `noncomputable opaque` until 2026-11-15, so
  the field could be neither proved nor refuted.  It is now defined as its
  documented body `Cl_2` (`BlochWignerUnitCircle.lean`).
* With that body, the field is
  an **intermediate-value fact**: `Cl_2 0 = 0` and `Cl_2 (π/2) = G > 0.915`
  (Catalan's constant), while `2/(3π) < 2/9`.  So some `θ ∈ [0, π/2]` works.
  This file proves that, sorry-free (`bringZeroModeBlochClass_holds`), and
  deliberately gives **no** global instance; see that theorem's docstring.

So the "transcendence obstruction" recorded in the class docstring does **not**
bear on the class as written: a real angle always exists.  The obstruction is
about an angle that is a *rational multiple of `π`* (a root-of-unity shape, i.e.
an algebraic Bloch class).  That stronger statement is
`BringZeroModeRootOfUnityClass` below; it is recorded as a conjecture with no
instance, and nothing here proves or refutes it.

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

/-- **Smallest honest hypothesis.**  If `BlochWigner_unit_circle` is the
    Clausen function (its documented body), the class has an instance. -/
theorem bringZeroModeBlochClass_of_eq_Cl_2
    (h : ∀ θ : ℝ, BlochWigner_unit_circle θ = Cl_2 θ) :
    BringZeroModeBlochClass := by
  obtain ⟨θ, -, hθ⟩ := exists_Cl_2_eq_bringZeroModeValue
  exact ⟨⟨θ, by rw [h θ, hθ]⟩⟩

/-- **The class holds, but there is deliberately no global instance.**
    `BlochWigner_unit_circle` is defined as `Cl_2`, so the field is true.  Its
    content is only that `2/(3π)` lies in the range of `Cl₂`; it says nothing
    about which Bloch class, if any, realises the value, and that
    identification (the Yekutieli triple on `{T(2,9), T(3,5)}`) is the open
    claim the class was written for (bean `qou-006b`).  A global `instance`
    would let typeclass search discharge every `[BringZeroModeBlochClass]`
    hypothesis, such as the one on `bring_zero_mode_additive_form`, without
    the open claim, contrary to §3b-cond.  So this is a named theorem; use it
    explicitly where the weak (range) reading is what you mean. -/
theorem bringZeroModeBlochClass_holds : BringZeroModeBlochClass :=
  bringZeroModeBlochClass_of_eq_Cl_2 (fun _ => rfl)

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
