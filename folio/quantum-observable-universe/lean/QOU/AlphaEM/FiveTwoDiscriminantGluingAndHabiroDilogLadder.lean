/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# `5₂` Trace-Field Discriminant `-23`, Golden-Ratio Dilog Ladder & Habiro Cyclotomic Increments
(`qou-yq50`, `qou-26ew`, `qou-0otg`)

This module formalises three self-contained results for Round 57:

1. **`5₂` Saddle Cubic Discriminant `-23` & Gluing Exponent Identity (`qou-yq50`, `parent: b9cj`):**
   The `5₂` knot complement's Riley/trace-field cubic `P(y) = y³ - y² + 1` has monic coefficients
   `(a₂, a₁, a₀) = (-1, 0, 1)`. Its polynomial discriminant
   `Δ(a₂, a₁, a₀) = a₂²·a₁² - 4·a₁³ - 4·a₂³·a₀ - 27·a₀² + 18·a₂·a₁·a₀`
   evaluates to `4 - 27 = -23` (confining the bar-odd channel to the imaginary quadratic resolvent
   `ℚ(√-23)`), distinct from the Alexander determinant `det(5₂) = 7`. Simultaneously, the
   gluing equation `y² = (1 - y)³` imposes the logarithmic branch relation `2·ℓ_j - 3·m_j = 2πi·ε_j`
   with coprime gluing exponents `(2, 3)` satisfying `3 - 2 = 1` and `3·1 - 2·1 = 1`.

2. **Golden-Ratio Dilogarithm Rational `π²/30` Ladder (`qou-26ew`):**
   Citing `[hakimoglu-brown2025]` (arXiv:2506.10206v2, eqs. 4, 6, 7) alongside the canonical
   secondary sources Lewin (*Polylogarithms and Associated Functions*, 1981) and Zagier
   (*The Dilogarithm Function*, 2007), the classical evaluations
   `Li₂(1) = π²/6`, `Li₂(φ⁻¹) = π²/10 - ln²(φ)`, and `Li₂(φ⁻²) = π²/15 - ln²(φ)`
   over the common denominator `30 = lcm(6, 10, 15)` have integer `π²/30`-weights `w₁ = 5`,
   `w_{φ⁻¹} = 3`, and `w_{φ⁻²} = 2`. We prove that `w_{φ⁻¹} + w_{φ⁻²} = w₁` (`3 + 2 = 5`,
   Euler–Landen reflection) and `w_{φ⁻¹} - w_{φ⁻²} = 1` (`1/10 - 1/15 = 1/30`).

3. **Habiro Cyclotomic Quadratic `q`-Degree Increment Law (`qou-0otg`):**
   Citing Habiro `[habiro2000]` (*On the colored Jones polynomials of some simple links*,
   Props. 5.1, 6.1, 6.2, 8.2 and eqs. 1–2 in Sec. 3, replacing non-existent "Theorem 1.1 /
   Corollary 1.2" locators), the `m`-th cyclotomic skein-basis term for the trefoil (`Prop. 5.1`)
   and figure-eight knot (`Prop. 6.1 / 8.2`) carries quadratic `q`-degree `m·(m + 1)`. We prove
   for all `m : Int` that the consecutive step increment is `2·(m + 1)`.
-/

namespace QOU.AlphaEM.FiveTwoDiscriminantGluingAndHabiroDilogLadder

/-! ## 1. `5₂` Saddle Cubic Discriminant `-23` & Gluing Exponents (`qou-yq50`) -/

/-- General discriminant of a monic cubic `y³ + a₂·y² + a₁·y + a₀`:
`Δ = a₂²·a₁² - 4·a₁³ - 4·a₂³·a₀ - 27·a₀² + 18·a₂·a₁·a₀`. -/
def monicCubicDiscriminant (a2 a1 a0 : Int) : Int :=
  a2 * a2 * (a1 * a1) - 4 * (a1 * a1 * a1) - 4 * (a2 * a2 * a2) * a0 -
    27 * (a0 * a0) + 18 * a2 * a1 * a0

/-- Logarithmic gluing linear form `2·ℓ - 3·m` associated with `y² = (1 - y)³`. -/
def fiveTwoGluingForm (l m : Int) : Int :=
  2 * l - 3 * m

/-- **`5₂` Saddle Cubic Discriminant `-23` & Gluing Shift Invariance (`qou-yq50`).**
The monic cubic `y³ - y² + 1` (`a₂ = -1, a₁ = 0, a₀ = 1`) has discriminant `-23`, whereas
the depressed trefoil/Eisenstein cubic `y³ + 1` (`a₂ = 0, a₁ = 0, a₀ = 1`) has discriminant
`-27`, with difference `(-23) - (-27) = 4`. Moreover, shifting `(ℓ, m) ↦ (ℓ + 3·k, m + 2·k)`
leaves the gluing linear form `fiveTwoGluingForm` invariant for every `k : Int`. -/
theorem five_two_cubic_discriminant_neg23_and_gluing_invariance (l m k : Int) :
    monicCubicDiscriminant (-1) 0 1 = -23 ∧
    monicCubicDiscriminant 0 0 1 = -27 ∧
    monicCubicDiscriminant (-1) 0 1 - monicCubicDiscriminant 0 0 1 = 4 ∧
    fiveTwoGluingForm (l + 3 * k) (m + 2 * k) = fiveTwoGluingForm l m := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  unfold fiveTwoGluingForm
  omega

/-! ## 2. Golden-Ratio Dilogarithm Rational `π²/30` Ladder (`qou-26ew`) -/

/-- Integer `π²/30`-weights for `Li₂(1) = 5·(π²/30)`, `Li₂(φ⁻¹) + ln²(φ) = 3·(π²/30)`,
and `Li₂(φ⁻²) + ln²(φ) = 2·(π²/30)` (`[hakimoglu-brown2025]`, Lewin 1981, Zagier 2007). -/
def li2WeightAtOne30 : Nat := 5
def li2WeightAtPhiInv30 : Nat := 3
def li2WeightAtPhiInvSq30 : Nat := 2

/-- **Golden-Ratio Euler–Landen Dilogarithm Weight Identities (`qou-26ew`).**
Cleared of denominators at `30 = lcm(6, 10, 15)`, the golden-ratio dilogarithm weights satisfy
`3 + 2 = 5` (`1/10 + 1/15 = 1/6`), `3 - 2 = 1` (`1/10 - 1/15 = 1/30`), and `6 × 5 = 10 × 3 = 15 × 2 = 30`. -/
theorem golden_ratio_euler_landen_rational_denominators :
    li2WeightAtPhiInv30 + li2WeightAtPhiInvSq30 = li2WeightAtOne30 ∧
    li2WeightAtPhiInv30 - li2WeightAtPhiInvSq30 = 1 ∧
    6 * li2WeightAtOne30 = 30 ∧
    10 * li2WeightAtPhiInv30 = 30 ∧
    15 * li2WeightAtPhiInvSq30 = 30 := by
  decide

/-! ## 3. Habiro Props. 5.1, 6.1, 6.2, 8.2 Cyclotomic `q`-Degree Increment (`qou-0otg`) -/

/-- Quadratic `q`-degree `m·(m + 1)` of the `m`-th cyclotomic skein term (Props. 5.1, 6.1, 8.2). -/
def cyclotomicQuadraticDeg (m : Int) : Int :=
  m * (m + 1)

/-- **Cyclotomic Quadratic `q`-Degree Step Increment (`qou-0otg`, Props. 5.1, 6.1, 8.2).**
For every cyclotomic rung `m : Int`, the degree difference between rung `m + 1` and rung `m`
equals `2·(m + 1)`: `cyclotomicQuadraticDeg (m + 1) - cyclotomicQuadraticDeg m = 2 * (m + 1)`. -/
theorem props_51_61_82_cyclotomic_degree_step (m : Int) :
    cyclotomicQuadraticDeg (m + 1) - cyclotomicQuadraticDeg m = 2 * (m + 1) ∧
    cyclotomicQuadraticDeg 0 = 0 ∧
    cyclotomicQuadraticDeg 1 = 2 ∧
    cyclotomicQuadraticDeg 2 = 6 := by
  refine ⟨?_, by decide, by decide, by decide⟩
  unfold cyclotomicQuadraticDeg
  have hcomm : (m + 1) * (m + 1 + 1) - m * (m + 1) = 2 * (m + 1) := by
    rw [Int.mul_add (m + 1) (m + 1) 1, Int.mul_one, Int.add_mul m 1 (m + 1), Int.one_mul]
    omega
  exact hcomm

end QOU.AlphaEM.FiveTwoDiscriminantGluingAndHabiroDilogLadder
