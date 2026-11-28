import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# The Coulomb pair weight's size law from the strand count — gap G3

Bean `qou-tcl3`. Audit `docs/audits/2026-11-28-coulomb-block-size.md`. Follows
`QOU.Nuclear.CoulombRingMu` (PR #9854): the vertex-pair factor `μ = 1 − αh²` is a contact factor
with no size, while the comparison data need `ε ∝ A^{−1/3}`.

## Hypotheses (named, none measured)

* **(H1) Homogeneity.** The Coulomb pair energy is homogeneous of degree `−1` under a dilation
  of the block: `ε(λL) = λ⁻¹ ε(L)`, i.e. `ε·L = κ` for a block-independent `κ`. This is the
  dilation law that `QOU.Nuclear.CoulombShellShapeFactor` (PR #9699) proves for the shape factor
  `f² = E²M₂/Q⁵`.
* **(H2) Volume additive in strands.** The block of `3A` strands has volume `L³ = A·v`, one cell
  `v` per nucleon (three strands). The 2026-08-01 audit's Freedman–He template
  `Vol^{−1/3}` uses the same reading.

## What is proved (any field, algebraic: no cube root is taken)

* `size_law`: (H1) and (H2) give `ε³·A·v = κ³`. So `ε ∝ A^{−1/3}` with nothing fitted.
* `size_ratio`: for two blocks, `ε₁³·A₁ = ε₂³·A₂`. The exponent `−1/3` is fixed; only one
  overall scale `κ³/v` is left.
* `size_ratio_mirror`: the mirror split `ε(A−1)/2` then obeys
  `(2Δ₁/(A₁−1))³·A₁ = (2Δ₂/(A₂−1))³·A₂`.

## What is not proved

* The magnitude `κ³/v`. That is one length, the same open energy-to-length map as before
  (bean `qou-mbfv`).
* (H1) and (H2) themselves. (H2) fails for a block with internal structure that does not fill
  space evenly, such as a shell change at `A = 5`.
-/

namespace QOU.Nuclear.CoulombBlockSize

variable {K : Type*} [Field K]

/-- **Size law.** Homogeneity `ε·L = κ` and additive volume `L³ = A·v` give `ε³·A·v = κ³`. -/
theorem size_law (ε L κ A v : K) (hH : ε * L = κ) (hV : L ^ 3 = A * v) :
    ε ^ 3 * (A * v) = κ ^ 3 := by
  rw [← hV, ← hH]; ring

/-- **Two blocks, one scale.** `ε₁³ A₁ = ε₂³ A₂` when both obey the size law with the same
`κ` and cell `v ≠ 0`. -/
theorem size_ratio (ε₁ ε₂ L₁ L₂ κ A₁ A₂ v : K) (hv : v ≠ 0)
    (h₁ : ε₁ * L₁ = κ) (h₂ : ε₂ * L₂ = κ) (V₁ : L₁ ^ 3 = A₁ * v) (V₂ : L₂ ^ 3 = A₂ * v) :
    ε₁ ^ 3 * A₁ = ε₂ ^ 3 * A₂ := by
  have e₁ := size_law ε₁ L₁ κ A₁ v h₁ V₁
  have e₂ := size_law ε₂ L₂ κ A₂ v h₂ V₂
  have : (ε₁ ^ 3 * A₁) * v = (ε₂ ^ 3 * A₂) * v := by linear_combination e₁ - e₂
  exact mul_right_cancel₀ hv this

/-- **Mirror form.** With the mirror split `Δ = ε(A − 1)/2` (`emEnergy_mirror` at `T_z = ½`),
the size law reads `(2Δ₁/(A₁−1))³ A₁ = (2Δ₂/(A₂−1))³ A₂`. -/
theorem size_ratio_mirror (ε₁ ε₂ Δ₁ Δ₂ L₁ L₂ κ A₁ A₂ v : K) (hv : v ≠ 0) (h2 : (2 : K) ≠ 0)
    (hA₁ : A₁ - 1 ≠ 0) (hA₂ : A₂ - 1 ≠ 0)
    (hΔ₁ : Δ₁ = ε₁ * (A₁ - 1) / 2) (hΔ₂ : Δ₂ = ε₂ * (A₂ - 1) / 2)
    (h₁ : ε₁ * L₁ = κ) (h₂ : ε₂ * L₂ = κ) (V₁ : L₁ ^ 3 = A₁ * v) (V₂ : L₂ ^ 3 = A₂ * v) :
    (2 * Δ₁ / (A₁ - 1)) ^ 3 * A₁ = (2 * Δ₂ / (A₂ - 1)) ^ 3 * A₂ := by
  have e₁ : 2 * Δ₁ / (A₁ - 1) = ε₁ := by rw [hΔ₁]; field_simp
  have e₂ : 2 * Δ₂ / (A₂ - 1) = ε₂ := by rw [hΔ₂]; field_simp
  rw [e₁, e₂]
  exact size_ratio ε₁ ε₂ L₁ L₂ κ A₁ A₂ v hv h₁ h₂ V₁ V₂

end QOU.Nuclear.CoulombBlockSize
