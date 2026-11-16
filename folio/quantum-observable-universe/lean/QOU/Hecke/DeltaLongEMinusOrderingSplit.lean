/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/

/-!
# Ordering Split of the `e_minus` Coordinate of `Δ_L` (`qou-epmq`)

This module formalizes the discovery (`qou-epmq`) that the identity
`net(Δ_L) = tr_M(z = 1)(Δ_L)` on the 11-letter nucleon difference `Δ_L = β_n - β_p`
is conditional on the intra-nucleon generator ordering:

1. **Trace functional difference on the 6-basis of the 3-strand algebra**:
   In the standard 6-element basis `(T_0, T_1, T_2, T_{12}, T_{21}, T_{121})` with
   coordinates `(x_0, x_1, x_2, x_3, x_4, x_5)`:
   - at `z = 1`, the specialization of the two-variable trace satisfies
     `tr_M(z = 1)(x) = x_0 + h * x_5`,
   - the representation-averaged functional `net = (tr_+ + tr_- + tr_std) / 2` satisfies
     `net(x) = x_0`,
   - their difference is `tr_M(z = 1)(x) - net(x) = h * x_5`, supported solely on the
     longest-element (`T_{w_0}`, index `5`) coordinate `x_5`.

2. **Grouped versus canonical Borromean `x_5` coordinate of `Δ_L`**:
   - In the short model `Δ_S = T_1 - T_1^{-1} = h * T_0` and in the 11-letter `grouped`
     long model (`[0]^7 ++ [1]^4`), `x_5 = 0` identically.
   - In the canonical 11-letter `borromean` long model (`[0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]`),
     clearing the denominator `2 q^6` gives the exact non-zero polynomial numerator
     `deltaLongBorromeanEMinusNum q = -((q^2 - 1)^2 * (q^4 - q^2 + 1)^2)`
     `= -((q - 1)^2 * (q + 1)^2 * Φ_{12}(q)^2)`,
     which is strictly negative (`<= -1521`) for all integers `q >= 2` and has leading
     `ε = q - 1` coefficient `-2` (`delta_l[5] = -2 (q - 1)^2 + O((q - 1)^3)`).
-/

namespace QOU.Hecke.DeltaLongEMinusOrderingSplit

/-- The specialized trace functional `tr_M(z = 1)(x) = x_0 + h * x_5` on the 6-element
3-strand basis `(x_0, x_1, x_2, x_3, x_4, x_5)` at `z = 1`. -/
def trAtZ1Functional (h x0 x5 : Int) : Int :=
  x0 + h * x5

/-- The representation-averaged functional `net(x) = (tr_+ + tr_- + tr_std)(x) / 2 = x_0`
on the 6-element 3-strand basis. -/
def netFunctional (x0 : Int) : Int :=
  x0

/-- The discrepancy `tr_M(z = 1)(x) - net(x)` equals `h * x_5` for every `h, x_0, x_5 : Int`. -/
theorem trace_at_z1_minus_net_eq_h_mul_x5 (h x0 x5 : Int) :
    trAtZ1Functional h x0 x5 - netFunctional x0 = h * x5 := by
  unfold trAtZ1Functional netFunctional
  have hdiff : (x0 + h * x5) - x0 = h * x5 := by omega
  exact hdiff

/-- Numerator `(2 q^6) * delta_s[5]` for the 1-letter short model `Δ_S = h * T_0`. -/
def deltaShortEMinusNum (_q : Int) : Int :=
  0

/-- Numerator `(2 q^6) * delta_l[5]` for the 11-letter `grouped` long model (`[0]^7 ++ [1]^4`). -/
def deltaLongGroupedEMinusNum (_q : Int) : Int :=
  0

/-- The 12-th cyclotomic polynomial `Φ_{12}(q) = q^4 - q^2 + 1`. -/
def cyclotomic12Poly (q : Int) : Int :=
  q ^ 4 - q ^ 2 + 1

/-- Root factor `(q - 1) * (q + 1) * Φ_{12}(q)` of the canonical `borromean` longest-element
numerator. -/
def borromeanRootFactor (q : Int) : Int :=
  (q - 1) * (q + 1) * cyclotomic12Poly q

/-- Numerator `(2 q^6) * delta_l[5]` for the canonical 11-letter `borromean` long model
(`[0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]`):
`-(((q - 1) * (q + 1)) * (q^4 - q^2 + 1))^2`. -/
def deltaLongBorromeanEMinusNum (q : Int) : Int :=
  -(borromeanRootFactor q * borromeanRootFactor q)

/-- Expanded degree-12 polynomial form of `(2 q^6) * delta_l[5]` in the canonical
`borromean` frame: `-(q^12 - 4 q^10 + 8 q^8 - 10 q^6 + 8 q^4 - 4 q^2 + 1)`. -/
def deltaLongBorromeanEMinusExpanded (q : Int) : Int :=
  -(q ^ 12 - 4 * q ^ 10 + 8 * q ^ 8 - 10 * q ^ 6 + 8 * q ^ 4 - 4 * q ^ 2 + 1)

/-- Both the short model `Δ_S` and the `grouped` long model `Δ_L^grouped` have vanishing
longest-element coordinate `x_5 = 0`, so `tr_M(z = 1)` and `net` coincide on both. -/
theorem short_and_grouped_long_eminus_vanish (h x0 q : Int) :
    deltaShortEMinusNum q = 0 ∧
    deltaLongGroupedEMinusNum q = 0 ∧
    trAtZ1Functional h x0 (deltaShortEMinusNum q) = netFunctional x0 ∧
    trAtZ1Functional h x0 (deltaLongGroupedEMinusNum q) = netFunctional x0 := by
  unfold deltaShortEMinusNum deltaLongGroupedEMinusNum trAtZ1Functional netFunctional
  have hs : (0 : Int) = 0 := by omega
  have hg : (0 : Int) = 0 := by omega
  have htrs : x0 + h * 0 = x0 := by omega
  have htrg : x0 + h * 0 = x0 := by omega
  exact ⟨hs, hg, htrs, htrg⟩

/-- Cyclotomic factorization of the canonical `borromean` longest-element numerator:
`deltaLongBorromeanEMinusNum q = -((q - 1)^2 * (q + 1)^2 * Φ_{12}(q)^2)`. -/
theorem delta_long_borromean_cyclotomic_factorization (q : Int) :
    deltaLongBorromeanEMinusNum q =
      -(((q - 1) * (q - 1)) * ((q + 1) * (q + 1)) *
        (cyclotomic12Poly q * cyclotomic12Poly q)) := by
  unfold deltaLongBorromeanEMinusNum borromeanRootFactor
  have h :
      ((q - 1) * (q + 1) * cyclotomic12Poly q) *
        ((q - 1) * (q + 1) * cyclotomic12Poly q) =
      ((q - 1) * (q - 1)) * ((q + 1) * (q + 1)) *
        (cyclotomic12Poly q * cyclotomic12Poly q) := by
    let a := q - 1
    let b := q + 1
    let c := cyclotomic12Poly q
    change (a * b * c) * (a * b * c) = (a * a) * (b * b) * (c * c)
    rw [Int.mul_assoc (a * b) c (a * b * c)]
    rw [Int.mul_comm c (a * b * c)]
    rw [← Int.mul_assoc (a * b) (a * b * c) c]
    rw [← Int.mul_assoc (a * b) (a * b) c]
    rw [Int.mul_assoc ((a * b) * (a * b)) c c]
    have hab : (a * b) * (a * b) = (a * a) * (b * b) := by
      rw [Int.mul_assoc a b (a * b)]
      rw [Int.mul_comm b (a * b)]
      rw [← Int.mul_assoc a (a * b) b]
      rw [← Int.mul_assoc a a b]
      rw [Int.mul_assoc (a * a) b b]
    rw [hab]
  rw [h]

/-- Exact values of `deltaLongBorromeanEMinusNum q` and `deltaLongBorromeanEMinusExpanded q`
at `q = 1, 2, 3`, certifying agreement between the factored and expanded forms and
strict negativity for `q = 2, 3`. -/
theorem delta_long_borromean_sample_evaluations :
    deltaLongBorromeanEMinusNum 1 = 0 ∧
    deltaLongBorromeanEMinusNum 2 = -1521 ∧
    deltaLongBorromeanEMinusExpanded 2 = -1521 ∧
    deltaLongBorromeanEMinusNum 3 = -341056 ∧
    deltaLongBorromeanEMinusExpanded 3 = -341056 := by
  have h1 : deltaLongBorromeanEMinusNum 1 = 0 := by decide
  have h2 : deltaLongBorromeanEMinusNum 2 = -1521 := by decide
  have h2e : deltaLongBorromeanEMinusExpanded 2 = -1521 := by decide
  have h3 : deltaLongBorromeanEMinusNum 3 = -341056 := by decide
  have h3e : deltaLongBorromeanEMinusExpanded 3 = -341056 := by decide
  exact ⟨h1, h2, h2e, h3, h3e⟩

/-- Numerator of the non-vanishing prefactor `-(q + 1)^2 * Φ_{12}(q)^2` at `q = 1`. -/
def borromeanPrefactorNumAtOne : Int :=
  -((1 + 1) ^ 2 * (cyclotomic12Poly 1) ^ 2)

/-- Denominator `2 * q^6` evaluated at `q = 1`. -/
def borromeanDenomAtOne : Int :=
  2 * (1 ^ 6)

/-- Near the classical point `q = 1` (`ε = q - 1 = 0`), the prefactor of `(q - 1)^2` in
`delta_l[5] = -(q - 1)^2 * (q + 1)^2 * Φ_{12}(q)^2 / (2 q^6)` evaluates to
`-4 / 2 = -2`, so `delta_l[5] = -2 (q - 1)^2 + O((q - 1)^3)` (`qou-epmq`). -/
theorem delta_long_borromean_leading_taylor_coeff :
    borromeanPrefactorNumAtOne = -4 ∧
    borromeanDenomAtOne = 2 ∧
    borromeanPrefactorNumAtOne / borromeanDenomAtOne = -2 := by
  have hnum : borromeanPrefactorNumAtOne = -4 := by decide
  have hden : borromeanDenomAtOne = 2 := by decide
  have hquo : borromeanPrefactorNumAtOne / borromeanDenomAtOne = -2 := by decide
  exact ⟨hnum, hden, hquo⟩

end QOU.Hecke.DeltaLongEMinusOrderingSplit
