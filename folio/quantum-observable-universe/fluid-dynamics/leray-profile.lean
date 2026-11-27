import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# QOU.FluidDynamics.LerayProfile — discretely self-similar Leray profile

LaTeX label: `def:leray-profile`

A backward self-similar velocity field on `ℝ³` with blow-up point `x₀` and
blow-up time `T` is written in Leray's similarity variables

    v(x, t) = (T - t)^{-1/2} · V(y, s),   y = (x - x₀)/√(T - t),   s = -log(T - t).

The profile `V` is **discretely self-similar** with period `P > 0` if it is
`P`-periodic in `s`. This file defines the field built from a profile
(`lerayField`), the periodicity condition (`DSSLerayProfile`), and proves that
periodicity in `s` is the same as the classical discrete scaling invariance
`v(x, t) = λ v(x₀ + λ(x - x₀), T - λ²(T - t))` with `λ = exp(P/2)`, i.e.
`P = 2 log λ` (`lerayField_discrete_scaling`).

No value of `P` is fixed here, and nothing about the existence of a nonzero
profile solving the Leray equations is asserted: that is the open content of
`conj:regularity-breakdown`, Part B.

## Base ring (§7c)
Archimedean: the rescaling uses `√`, `log` and the Euclidean space `ℝ³`.

## References
- [leitner2026] fluid-dynamics/leray-profile, regularity-breakdown
- Leray, Acta Math. 63 (1934) (`leray1934`)
- Bradshaw–Tsai, arXiv:1802.00038 (`bradshaw-tsai2018survey`)
-/

namespace QOU.FluidDynamics.LerayProfile

/-- Euclidean `ℝ³`. -/
abbrev R3 := EuclideanSpace ℝ (Fin 3)

/-- The velocity field built from a Leray profile `V(y, s)` with blow-up point
    `x₀` and blow-up time `T`:
    `v(x, t) = (T - t)^{-1/2} V((x - x₀)/√(T - t), -log(T - t))`. -/
noncomputable def lerayField (V : R3 → ℝ → R3) (x₀ : R3) (T : ℝ) (x : R3) (t : ℝ) : R3 :=
  (Real.sqrt (T - t))⁻¹ • V ((Real.sqrt (T - t))⁻¹ • (x - x₀)) (-Real.log (T - t))

/-- **Definition (discretely self-similar Leray profile).** `V` is a
    discretely self-similar profile with period `P` if `P > 0` and `V` is
    `P`-periodic in the similarity time `s`. -/
structure DSSLerayProfile (V : R3 → ℝ → R3) (P : ℝ) : Prop where
  period_pos : 0 < P
  periodic : ∀ y s, V y (s + P) = V y s

/-- **Periodicity in `s` is discrete scaling invariance.** If `V` is
    `P`-periodic in `s`, the field `v = lerayField V x₀ T` satisfies, for
    every `t < T`,
    `v(x, t) = λ · v(x₀ + λ(x - x₀), T - λ²(T - t))` with `λ = exp(P/2)`.
    With `x₀ = 0`, `T = 0` this is the classical `v(x, t) = λ v(λx, λ²t)`. -/
theorem lerayField_discrete_scaling {V : R3 → ℝ → R3} {P : ℝ}
    (h : DSSLerayProfile V P) (x₀ : R3) (T : ℝ) (x : R3) {t : ℝ} (ht : t < T) :
    lerayField V x₀ T x t =
      Real.exp (P / 2) • lerayField V x₀ T (x₀ + Real.exp (P / 2) • (x - x₀))
        (T - Real.exp (P / 2) ^ 2 * (T - t)) := by
  have hτ : 0 < T - t := sub_pos.mpr ht
  have hl0 : 0 < Real.exp (P / 2) := Real.exp_pos _
  have hl2 : Real.exp (P / 2) ^ 2 = Real.exp P := by
    rw [sq, ← Real.exp_add]; ring_nf
  have hs0 : 0 < Real.sqrt (T - t) := Real.sqrt_pos.mpr hτ
  unfold lerayField
  have e1 : T - (T - Real.exp (P / 2) ^ 2 * (T - t)) = Real.exp (P / 2) ^ 2 * (T - t) := by
    ring
  have e2 : x₀ + Real.exp (P / 2) • (x - x₀) - x₀ = Real.exp (P / 2) • (x - x₀) := by
    abel
  rw [e1, e2]
  have hsq : Real.sqrt (Real.exp (P / 2) ^ 2 * (T - t))
      = Real.exp (P / 2) * Real.sqrt (T - t) := by
    rw [Real.sqrt_mul (by positivity), Real.sqrt_sq hl0.le]
  have hlog : -Real.log (Real.exp (P / 2) ^ 2 * (T - t)) = -Real.log (T - t) - P := by
    rw [Real.log_mul (by positivity) hτ.ne', hl2, Real.log_exp]; ring
  rw [hsq, hlog, smul_smul, smul_smul]
  have ha : (Real.exp (P / 2) * Real.sqrt (T - t))⁻¹ * Real.exp (P / 2)
      = (Real.sqrt (T - t))⁻¹ := by
    field_simp
  have hb : Real.exp (P / 2) * (Real.exp (P / 2) * Real.sqrt (T - t))⁻¹
      = (Real.sqrt (T - t))⁻¹ := by
    field_simp
  have hp : ∀ y, V y (-Real.log (T - t) - P) = V y (-Real.log (T - t)) := by
    intro y
    have := h.periodic y (-Real.log (T - t) - P)
    rw [sub_add_cancel] at this
    exact this.symm
  rw [ha, hb, hp]

/-- A steady profile (independent of `s`) is discretely self-similar for every
    period. So the steady case, excluded by Nečas–Růžička–Šverák and Tsai, is
    contained in every DSS class; a DSS profile of interest must be
    non-constant in `s`. -/
theorem dssLerayProfile_of_steady {V : R3 → ℝ → R3}
    (hst : ∀ y s, V y s = V y 0) {P : ℝ} (hP : 0 < P) : DSSLerayProfile V P :=
  ⟨hP, fun y s => by rw [hst y (s + P), hst y s]⟩

end QOU.FluidDynamics.LerayProfile
