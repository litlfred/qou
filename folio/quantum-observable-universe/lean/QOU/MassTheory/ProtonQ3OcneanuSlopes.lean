import QOU.MassTheory.ProtonQ3SchurElement
import QOU.MathlibExt.KLCoordinateLaurent

/-!
# Ocneanu weights of `H₃(q)` and what the derivative reading of `/q³` really uses

`tr_z` is the Markov trace on `H₃(q)` with `tr_z(σ_i) = z`. It decomposes as
`tr_z = y₃(z)·χ_triv + y₁₃(z)·χ_sign + y₂₁(z)·χ_refl`. On the classes of
`1, σ₁, σ₁σ₂, σ₁σ₂σ₁` the characters take the values

* `χ_triv`: `1, q, q², q³`;
* `χ_sign`: `1, −q⁻¹, q⁻², −q⁻³`;
* `χ_refl`: `2, q − q⁻¹, −1, 0` (from `τ = Σ χ/c_χ`);

and the trace takes `1, z, z², z(1 + (q − q⁻¹)z)`. `ocneanu_decomposition`
checks the three weights below against all four equations.

Results:

1. `ySign_slope_zD`, `yTriv_slope_zero`: each linear weight has slope
   `∓1/[3]_q!` at its zero. Since `tr_z(x₋) = c_sign·y₁₃(z)`
   (`trXMinus_eq_schurSign_mul_ySign`), the derivative `−q⁻³` of
   `tr_z(x₋)` at `z_D` is `c_sign/[3]_q!`. **So the derivative reading does not
   select the power of `q`: it returns whatever the chosen scaling of `x₋` puts
   in.** The trivial-block "check" (`linear_blocks_derivative_rule`) follows
   from the same slope and is not independent.
2. `yRefl_slope_q`: the reflection weight has slope `−q(q²+1)/(q⁴+q²+1)` at
   `z = q`; times `[3]_q!` that is `−[2]_q²`, not `±1`. The slope rule does not
   extend to the reflection block.
3. Bar involution on the sign line. `bar(x₋)` lies in the sign line, and on the
   sign character `χ_sign(bar x₋) = P(q) = q⁶·P(q⁻¹) = q⁶·χ_sign(x₋)`
   (`schurTriv_eq_q6_mul_schurSign`), so `bar(x₋) = q⁶·x₋`. A unit multiple
   `ε q^m x₋` is bar-invariant iff `m = 3` (`sign_line_bar_fixed_iff`). For the
   bar-invariant generator `q³x₋` the derivative at `z_D` is `−1`
   (`hasDerivAt_klSign_zD`) and its square constant is `q³·c_sign = [3]_q!`
   (`q3_mul_schurSign`), the bar-symmetric normaliser.
   **Applied to the element as well as to the coordinate, the integral +
   bar-invariant criterion gives `k = 0`, not the proton's `k = −3`.**

Item 3's step "`bar(x₋)` lies in the sign line" is argued, not formalised:
`σ_i x₋ = −q⁻¹ x₋` and bar sends it to `σ_i bar(x₋) = −q⁻¹ bar(x₋)`.
-/

namespace QOU.MassTheory.ProtonQ3Slopes

open QOU.MassTheory.ProtonQ3Schur QOU.MassTheory.PoincareCentering

section Weights

variable {K : Type*} [Field K]

/-- Ocneanu weight of the trivial block. -/
def yTriv (q z : K) : K := (q * z + 1) * (q ^ 3 * z + q * z + 1) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))

/-- Ocneanu weight of the sign block. -/
def ySign (q z : K) : K := q ^ 2 * (z - q) * (z * (q ^ 2 + 1) - q ^ 3) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))

/-- Ocneanu weight of the reflection block. -/
def yRefl (q z : K) : K := -(q * (z - q) * (q * z + 1)) / (q ^ 4 + q ^ 2 + 1)

theorem ocneanu_decomposition (q z : K) (hq : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    yTriv q z + ySign q z + 2 * yRefl q z = 1 ∧
    yTriv q z * q + ySign q z * (-q⁻¹) + yRefl q z * (q - q⁻¹) = z ∧
    yTriv q z * q ^ 2 + ySign q z * (q⁻¹) ^ 2 + yRefl q z * (-1) = z ^ 2 ∧
    yTriv q z * q ^ 3 + ySign q z * (-(q⁻¹) ^ 3) = z * (1 + (q - q⁻¹) * z) := by
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    rwa [show q ^ 2 * (q ^ 2 + 1) + 1 = q ^ 4 + q ^ 2 + 1 by ring]
  unfold yTriv ySign yRefl
  refine ⟨?_, ?_, ?_, ?_⟩ <;> field_simp <;> ring

/-- `[3]_q!` in the form used by these weights. -/
theorem qFact_eq (q : K) (hq : q ≠ 0) :
    qFactThreeBalanced q = (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / q ^ 3 := by
  unfold qFactThreeBalanced; field_simp

/-- `tr_z(x₋) = c_sign·y₁₃(z)`. -/
theorem trXMinus_eq_schurSign_mul_ySign (q z : K) (hq : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    trXMinus q z = schurSign q * ySign q z := by
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    rwa [show q ^ 2 * (q ^ 2 + 1) + 1 = q ^ 4 + q ^ 2 + 1 by ring]
  rw [trXMinus_factor q z hq, ← fBor_normaliser_eq_schurSign q hq, qFact_eq q hq]
  unfold ySign; field_simp

/-- `c_triv = q⁶·c_sign`: on the sign character, `bar(x₋)` is `q⁶·x₋`. -/
theorem schurTriv_eq_q6_mul_schurSign (q : K) (hq : q ≠ 0) :
    schurTriv q = q ^ 6 * schurSign q := by
  rw [schurTriv_eq q hq, ← fBor_normaliser_eq_schurSign q hq]; field_simp

/-- The bar-invariant generator `q³x₋` squares with constant `q³·c_sign = [3]_q!`,
which is bar-symmetric (`k = 0`). -/
theorem q3_mul_schurSign (q : K) (hq : q ≠ 0) :
    q ^ 3 * schurSign q = qFactThreeBalanced q := by
  rw [← fBor_normaliser_eq_schurSign q hq]; field_simp

end Weights

section Slopes

variable {𝕜 : Type*} [NontriviallyNormedField 𝕜]

/-- The sign weight has slope `−1/[3]_q!` at `z_D`. -/
theorem ySign_slope_zD {q : 𝕜} (hq : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    HasDerivAt (ySign q) (-(qFactThreeBalanced q)⁻¹) (q ^ 3 / (q ^ 2 + 1)) := by
  have hd := ((((hasDerivAt_id (q ^ 3 / (q ^ 2 + 1))).sub_const q).const_mul (q ^ 2)).mul
    (((hasDerivAt_id (q ^ 3 / (q ^ 2 + 1))).mul_const (q ^ 2 + 1)).sub_const (q ^ 3))).div_const
      ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
  rw [qFact_eq q hq]
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    rwa [show q ^ 2 * (q ^ 2 + 1) + 1 = q ^ 4 + q ^ 2 + 1 by ring]
  convert hd using 1
  simp only [id]
  field_simp
  ring

/-- The trivial weight has slope `+1/[3]_q!` at its zero `−1/(q³ + q)`. -/
theorem yTriv_slope_zero {q : 𝕜} (hq : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    HasDerivAt (yTriv q) (qFactThreeBalanced q)⁻¹ (-1 / (q ^ 3 + q)) := by
  have h4 : q ^ 3 + q ≠ 0 := by
    have e : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [e]; exact mul_ne_zero hq h1
  have hd := ((((hasDerivAt_id (-1 / (q ^ 3 + q))).const_mul q).add_const 1).mul
    ((((hasDerivAt_id (-1 / (q ^ 3 + q))).const_mul (q ^ 3)).add
      ((hasDerivAt_id (-1 / (q ^ 3 + q))).const_mul q)).add_const 1)).div_const
        ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
  rw [qFact_eq q hq]
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    rwa [show q ^ 2 * (q ^ 2 + 1) + 1 = q ^ 4 + q ^ 2 + 1 by ring]
  have h5 : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  convert hd using 1
  simp only [id, mul_one, Pi.add_apply]
  field_simp
  ring

/-- The reflection weight has slope `−q(q²+1)/(q⁴+q²+1)` at `z = q`. -/
theorem yRefl_slope_q (q : 𝕜) :
    HasDerivAt (yRefl q) (-(q * (q ^ 2 + 1)) / (q ^ 4 + q ^ 2 + 1)) q := by
  have hd := ((((hasDerivAt_id q).sub_const q).const_mul q).mul
    (((hasDerivAt_id q).const_mul q).add_const 1)).neg.div_const (q ^ 4 + q ^ 2 + 1)
  convert hd using 1
  simp only [id]
  ring

/-- Times `[3]_q!`, the reflection slope is `−[2]_q²`, not `±1`. -/
theorem yRefl_slope_times_fact {q : 𝕜} (hq : q ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    (-(q * (q ^ 2 + 1)) / (q ^ 4 + q ^ 2 + 1)) * qFactThreeBalanced q = -(q + q⁻¹) ^ 2 := by
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    rwa [show q ^ 2 * (q ^ 2 + 1) + 1 = q ^ 4 + q ^ 2 + 1 by ring]
  rw [qFact_eq q hq]; field_simp

/-- For the bar-invariant generator `q³x₋`, the derivative at `z_D` is `−1`. -/
theorem hasDerivAt_klSign_zD {q : 𝕜} (h0 : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0) :
    HasDerivAt (fun z => q ^ 3 * ((z - q) * (z * (q ^ 2 + 1) - q ^ 3) / q ^ 4))
      (-1) (q ^ 3 / (q ^ 2 + 1)) := by
  have hd := (hasDerivAt_trXMinus_zD h0 h1).const_mul (q ^ 3)
  convert hd using 1
  field_simp

end Slopes

section BarSignLine

open LaurentPolynomial QOU.MathlibExt.LaurentUnits

/-- On the sign line, `bar(f·x₋) = bar(f)·q⁶·x₋`. A unit multiple `ε q^m x₋`
is bar-invariant iff `m = 3`. -/
theorem sign_line_bar_fixed_iff {ε : ℤ} (hε : IsUnit ε) (m : ℤ) :
    invert (LaurentPolynomial.C ε * T m) * T 6 = LaurentPolynomial.C ε * T m ↔ m = 3 := by
  rw [map_mul, invert_C, invert_T, mul_assoc, ← T_add]
  constructor
  · intro h
    have h0 : ε ≠ 0 := hε.ne_zero
    have := congrArg LaurentPolynomial.degree h
    rw [degree_C_mul_T _ _ h0, degree_C_mul_T _ _ h0] at this
    have := WithBot.coe_injective this
    omega
  · rintro rfl; norm_num

end BarSignLine

end QOU.MassTheory.ProtonQ3Slopes
