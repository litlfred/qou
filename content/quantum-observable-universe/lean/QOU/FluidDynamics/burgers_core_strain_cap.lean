import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# QOU.FluidDynamics.burgers_core_strain_cap

**The finite-core strain cap** — deriving the two-regime model's phase-2
saturation *value* `α = Γ/(πV₁)` from the Gaussian vortex profile
(bean `qou-zuz0`, sub-item U4 of the model-to-PDE decomposition,
[`2026-08-14-qns-model-to-pde-uniformity-decomposition.md`](../../../../../docs/audits/2026-08-14-qns-model-to-pde-uniformity-decomposition.md)).

A singular point vortex of circulation `Γ` exerts co-rotation strain
`Γ/(2πr²)` at distance `r` — **unbounded** as `r → 0`
(`pointStrain_unbounded`).  A finite Gaussian core of variance `a²`
(the profile of both the Lamb–Oseen and the steady Burgers vortex, both
exact NS solutions) exerts

  `coreStrain = Γ/(2πr²) · (1 − exp(−r²/(2a²)))`,

and the elementary inequality `1 − e^{−x} ≤ x` gives the **uniform cap**

  `coreStrain ≤ Γ/(4πa²)`  for every `r > 0`  (`coreStrain_le_cap`),

attained in the limit `r → 0`.  This is the regularization mechanism of
the overlap regime, *derived*: however close the approach, a finite core
cannot exert more than `Γ/(4πa²)` strain.  Under the model's stretching
normalization `V₁ = 4a²` the cap reads `Γ/(π·V₁)` — **the phase-2
saturation value of `rem:hyperbolic-overlap-saturation`, now derived
from the exact-solution profile up to the `V₁` normalization
convention** (`cap_eq_model_saturation`).

**Scope (honest).**  Derived: the cap inequality for the Gaussian
profile, and its identity with the model's saturation under the stated
`V₁` convention.  Named conventions/hypotheses, not derived here: the
choice `V₁ = 4a²` (the model's stretching coordinate is pinned to core
variance by this dictionary); applying the *single-vortex* profile to
the two-vortex hyperbolic overlap geometry (the same per-core
localization hypothesis as the rest of the two-regime model).  The
steady Burgers balance `γ = 4ν/a²` (strain that holds the core steady)
is noted in the audit; not needed for the cap.  This file is
archimedean (`ℝ`) by §7c necessity: `Real.exp` and `Real.pi` are the
statement.
-/

namespace QOU.FluidDynamics.BurgersStrainCap

open Real

/-- Co-rotation strain of a singular point vortex at distance `r`:
    `Γ/(2πr²)`. -/
noncomputable def pointStrain (Γ r : ℝ) : ℝ := Γ / (2 * π * r ^ 2)

/-- Co-rotation strain of a Gaussian-core vortex (Lamb–Oseen / Burgers
    profile, core variance `a²`) at distance `r`:
    `Γ/(2πr²)·(1 − exp(−r²/(2a²)))`. -/
noncomputable def coreStrain (Γ a2 r : ℝ) : ℝ :=
  Γ / (2 * π * r ^ 2) * (1 - Real.exp (-(r ^ 2 / (2 * a2))))

/-- **The singular vortex's strain is unbounded on approach**: for every
    level `M > 0` there is a positive distance at which the point-vortex
    strain exceeds it (namely `r = √(Γ/(4πM))`, where the strain is
    exactly `2M`). -/
theorem pointStrain_unbounded (Γ M : ℝ) (hΓ : 0 < Γ) (hM : 0 < M) :
    ∃ r : ℝ, 0 < r ∧ M < pointStrain Γ r := by
  have hπ := Real.pi_pos
  have harg : 0 < Γ / (4 * π * M) := by positivity
  refine ⟨Real.sqrt (Γ / (4 * π * M)), Real.sqrt_pos.mpr harg, ?_⟩
  unfold pointStrain
  rw [Real.sq_sqrt (le_of_lt harg)]
  have hden : 2 * π * (Γ / (4 * π * M)) = Γ / (2 * M) := by
    field_simp
    ring
  rw [hden]
  rw [div_div_eq_mul_div, lt_div_iff₀ (by positivity : (0 : ℝ) < Γ)]
  nlinarith

/-- **The finite-core strain cap**: for every distance `r > 0` the
    Gaussian-core strain is at most `Γ/(4πa²)`.  From
    `1 − e^{−x} ≤ x` (Mathlib `Real.add_one_le_exp`) applied at
    `x = r²/(2a²)` — the `r`-dependence cancels exactly.  This is the
    saturation: the approach can no longer amplify the strain once the
    separation is inside the core. -/
theorem coreStrain_le_cap (Γ a2 r : ℝ) (hΓ : 0 ≤ Γ) (ha : 0 < a2)
    (hr : 0 < r) :
    coreStrain Γ a2 r ≤ Γ / (4 * π * a2) := by
  have hπ := Real.pi_pos
  unfold coreStrain
  have hexp : 1 - Real.exp (-(r ^ 2 / (2 * a2))) ≤ r ^ 2 / (2 * a2) := by
    have h := Real.add_one_le_exp (-(r ^ 2 / (2 * a2)))
    linarith
  have hpos : 0 ≤ Γ / (2 * π * r ^ 2) := by positivity
  calc Γ / (2 * π * r ^ 2) * (1 - Real.exp (-(r ^ 2 / (2 * a2))))
      ≤ Γ / (2 * π * r ^ 2) * (r ^ 2 / (2 * a2)) :=
        mul_le_mul_of_nonneg_left hexp hpos
    _ = Γ / (4 * π * a2) := by
        field_simp
        ring

/-- **The cap is the model's saturation value**: under the two-regime
    model's stretching normalization `V₁ = 4a²`, the derived cap
    `Γ/(4πa²)` reads exactly `Γ/(π·V₁)` — the phase-2 strain of
    `rem:hyperbolic-overlap-saturation`.  The saturation *value* is
    thereby derived from the Gaussian (exact-NS) profile up to this
    normalization convention. -/
theorem cap_eq_model_saturation (Γ a2 V1 : ℝ) (hV : V1 = 4 * a2) :
    Γ / (4 * π * a2) = Γ / (π * V1) := by
  subst hV
  ring_nf

end QOU.FluidDynamics.BurgersStrainCap
