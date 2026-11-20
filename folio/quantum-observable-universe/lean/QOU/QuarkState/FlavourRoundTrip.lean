/-
# The flavour round trip through the flipping letter: label A gives the convention-D weight

Bean `qou-99qc` (which functional is `ε` in `Q_β = |ε(Δ_S)|·E₀`). Owner request 2026-11-20
("u and d have separate representation … derive it").

`QBetaChiralityReduction.lean` proves that on `Δ_S` every block-weighted trace reads one
number, the chirality expectation `y₃ = τ(J)`, and `Q_β = (h[2]/2)·y₃·E₀`. The convention-D
Markov trace has `y₃ = (q⁴+1)/(q²+1)²` (`tau_deltaS_conventionD`).

This file works in the explicit `(3,1)` representation of `H₄(q)` of
`FlavourDoubletFourStrands.lean`, where the left line of `σ₁` is a flavour doublet with two
labels side by side (owner choice 2026-11-15): **A**, the `σ₃` eigenlines `Lu`, `Ld`, flipped
by the three-strand letter `σ₂`; **B**, the `J₄` eigenlines `Ja`, `Jb`, flipped only by the
strand-4 letter `σ₃`. For a flavour pair `(P, P')` and its flipping letter `s`, the
**round trip** is `tr(P · s · P' · s)`: go from one flavour line to the other through the
letter and back.

## What is proved (generic field, no `ℝ`, no `sorry`)

* `roundTrip_A`: `tr(Lu σ₂ Ld σ₂) = (q⁴+1)/(q²+1)²`. This is **exactly** the convention-D
  weight `y₃` that `tau_deltaS_conventionD` uses, i.e. the ruled `ε` of 2026-09-08.
* `roundTrip_A_inv`: the same value with `σ₂⁻¹` on the way back, so it is bar-invariant.
* `roundTrip_B`: `tr(Ja σ₃ Jb σ₃) = (q²+1)²(q⁴+1)/(q⁴+q²+1)²`, half the `J₄` sl₂
  coupling `cJ` of `FlavourDoubletFourStrands.J4_sl2_*`; `roundTrip_B_inv` likewise.
* `roundTrip_B_gg`: the same value through the strand-4 `γγ` vertex `V₁ = σ₂σ₃⁻¹` and back.
* `roundTrip_A_ne_B`: the two values differ (at `q = 2` over `ℚ`).

## What is NOT proved

Nothing here says that the decay channel's `ε` IS a round trip, or that label B rather than
label A is the neutron–proton flavour. The file shows one rule, "`y₃` := the flavour round
trip of the flipping letter", that reproduces the ruled `ε` on label A, and computes what the
same rule gives on label B. Choosing B because its `Q_β` lands near the measurement would be
selection against the target (AGENTS.md §NO FITTING). The J₄ label is the three-strand
isospin multiplicity (`(3)` vs `(2,1)`), not `T³` (`FlavourDoubletFourStrands`, scoping note).

-- Ref: [humphreys1990] §7.4 (Hecke algebra, generic q)
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.QuarkState.FlavourDoubletFourStrands
import Mathlib.LinearAlgebra.Matrix.Trace

namespace QOU.QuarkState.FlavourRoundTrip

open Matrix QOU.QuarkState.FlavourDoubletFour

variable {K : Type*} [Field K]

/-- The round trip `tr(P · s · P' · t)`. -/
def roundTrip (P s P' t : Matrix (Fin 3) (Fin 3) K) : K := Matrix.trace (P * s * P' * t)

section A

variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0)
include hq hn

/-- Label A: the round trip through `σ₂` is the convention-D weight `y₃`. -/
theorem roundTrip_A :
    roundTrip Lu (s2 q) Ld (s2 q) = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  unfold roundTrip Lu Ld s2
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

/-- Label A, returning through `σ₂⁻¹`: the same value. -/
theorem roundTrip_A_inv :
    roundTrip Lu (s2 q) Ld (s2i q) = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  unfold roundTrip Lu Ld s2 s2i
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

end A

section B

variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0) (hD : q ^ 4 + q ^ 2 + 1 ≠ 0)
include hq hn hD

/-- Label B: the round trip through the strand-4 letter `σ₃` is `cJ/2`. -/
theorem roundTrip_B :
    roundTrip (Ja q) (s3 q) (Jb q) (s3 q) =
      (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2 := by
  unfold roundTrip Ja Jb s3
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

/-- Label B, returning through `σ₃⁻¹`: the same value. -/
theorem roundTrip_B_inv :
    roundTrip (Ja q) (s3 q) (Jb q) (s3i q) =
      (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2 := by
  unfold roundTrip Ja Jb s3 s3i
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

/-- Label B through the strand-4 `γγ` vertex `V₁ = σ₂σ₃⁻¹` and back through
`V₁⁻¹ = σ₃σ₂⁻¹`: the same value as through the bare letter. -/
theorem roundTrip_B_gg :
    roundTrip (Ja q) (s2 q * s3i q) (Jb q) (s3 q * s2i q) =
      (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2 := by
  unfold roundTrip Ja Jb s2 s3i s3 s2i
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

end B

/-- The two labels give different values: at `q = 2`, `17/25` against `425/441`. -/
theorem roundTrip_A_ne_B :
    ((2 : ℚ) ^ 4 + 1) / ((2 : ℚ) ^ 2 + 1) ^ 2 ≠
      ((2 : ℚ) ^ 2 + 1) ^ 2 * ((2 : ℚ) ^ 4 + 1) / ((2 : ℚ) ^ 4 + (2 : ℚ) ^ 2 + 1) ^ 2 := by
  norm_num

end QOU.QuarkState.FlavourRoundTrip
