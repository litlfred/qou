import Mathlib.NumberTheory.Cyclotomic.PrimitiveRoots

/-!
# QOU.Information.JonesTractableOrders — the orders of the JVW tractable points

Human statement (`prop:jvw-tractable-orders`). Jaeger, Vertigan and Welsh show that exact
evaluation of the Jones polynomial `V_L(t)` is `#P`-hard except at the six roots of unity
`t ∈ {1, −1, i, −i, ω, ω⁻¹}` (formally written `ω = e^{2πi/3}`, `ω⁻¹ = e^{−2πi/3}`; cited,
not formalised). Per the 2026-11-27 transcendental-boundary ruling (`qou-dk7p`), all six
points live algebraically in the 12th cyclotomic field `ℚ(ζ₁₂)` (`C12`) via `I = ζ₁₂³`
(`I² = −1`) and `ω = ζ₁₂⁴` (`ω² + ω + 1 = 0`), with `e^{±2πi/3}` as a formal label.
Each of these six points is a primitive root of unity of order `1, 2, 4, 4, 3, 3`
respectively (`jvw_orders`). None of them is a primitive 6th root of unity
(`jvw_no_order_six`), even though primitive 6th roots exist in `ℚ(ζ₁₂)` (`zeta6_prim`),
and `I` has order `4`, which does not divide `6` (`four_not_dvd_six`). So in the
convention `t = q`, the set of orders of the tractable points is `{1, 2, 3, 4}`,
not `{n : n ∣ 6}`.
-/

namespace QOU.Information.JonesTractable

/-- The 12th cyclotomic field `ℚ(ζ₁₂)`, algebraic home of the 1st, 2nd, 3rd, 4th, and 6th
roots of unity. -/
noncomputable abbrev C12 : Type := CyclotomicField 12 ℚ

/-- Canonical primitive 12th root of unity `ζ₁₂ ∈ ℚ(ζ₁₂)`. -/
noncomputable def zeta12 : C12 := IsCyclotomicExtension.zeta 12 ℚ C12

theorem zeta12_prim : IsPrimitiveRoot zeta12 12 :=
  IsCyclotomicExtension.zeta_spec 12 ℚ C12

/-- Algebraic fourth root of unity `I = ζ₁₂³`, satisfying `I² = −1`. -/
noncomputable def I : C12 := zeta12 ^ 3

/-- Algebraic cube root of unity `ω = ζ₁₂⁴` (formal label `e^{2πi/3}`), satisfying
`ω² + ω + 1 = 0`. -/
noncomputable def omega : C12 := zeta12 ^ 4

theorem I_prim : IsPrimitiveRoot I 4 := by
  simpa [I] using zeta12_prim.pow_of_dvd (by norm_num : (3 : ℕ) ≠ 0) (by norm_num : 3 ∣ 12)

theorem I_sq : I ^ 2 = -1 := by
  have h4 : (I ^ 2) ^ 2 = 1 := by
    calc (I ^ 2) ^ 2 = I ^ 4 := by ring
    _ = 1 := I_prim.pow_eq_one
  rcases sq_eq_one_iff.mp h4 with h1 | hm1
  · exact absurd h1 (I_prim.pow_ne_one_of_pos_of_lt (by norm_num) (by norm_num))
  · exact hm1

theorem negI_eq_pow_three : -I = I ^ 3 := by
  calc -I = (-1) * I := by ring
  _ = I ^ 2 * I := by rw [I_sq]
  _ = I ^ 3 := by ring

theorem negI_eq_inv : -I = I⁻¹ := by
  apply eq_inv_of_mul_eq_one_left
  calc (-I) * I = -(I ^ 2) := by ring
  _ = -(-1) := by rw [I_sq]
  _ = 1 := by ring

theorem negI_prim : IsPrimitiveRoot (-I) 4 := by
  rw [negI_eq_inv]
  exact I_prim.inv

theorem omega_prim : IsPrimitiveRoot omega 3 := by
  simpa [omega] using zeta12_prim.pow_of_dvd (by norm_num : (4 : ℕ) ≠ 0) (by norm_num : 4 ∣ 12)

theorem omega_cyclotomic : omega ^ 2 + omega + 1 = 0 := by
  have h3 : (omega - 1) * (omega ^ 2 + omega + 1) = 0 := by
    calc (omega - 1) * (omega ^ 2 + omega + 1) = omega ^ 3 - 1 := by ring
    _ = 1 - 1 := by rw [omega_prim.pow_eq_one]
    _ = 0 := sub_self 1
  rcases mul_eq_zero.mp h3 with h1 | hcyc
  · exact absurd (sub_eq_zero.mp h1) (omega_prim.ne_one (by norm_num))
  · exact hcyc

theorem omega_inv_prim : IsPrimitiveRoot omega⁻¹ 3 := omega_prim.inv

theorem neg_one_prim : IsPrimitiveRoot (-1 : C12) 2 :=
  IsPrimitiveRoot.neg_one 0 (by norm_num)

/-- Primitive 6th roots of unity exist in `ℚ(ζ₁₂)` (`ζ₁₂²` has order `6`), witnessing that
`jvw_no_order_six` is non-vacuous in the ambient field. -/
theorem zeta6_prim : IsPrimitiveRoot (zeta12 ^ 2) 6 := by
  simpa using zeta12_prim.pow_of_dvd (by norm_num : (2 : ℕ) ≠ 0) (by norm_num : 2 ∣ 12)

/-- **The six JVW points and their orders.** -/
theorem jvw_orders :
    IsPrimitiveRoot (1 : C12) 1 ∧ IsPrimitiveRoot (-1 : C12) 2 ∧ IsPrimitiveRoot I 4 ∧
      IsPrimitiveRoot (-I) 4 ∧ IsPrimitiveRoot omega 3 ∧ IsPrimitiveRoot omega⁻¹ 3 :=
  ⟨IsPrimitiveRoot.one, neg_one_prim, I_prim, negI_prim, omega_prim, omega_inv_prim⟩

/-- **No JVW point is a primitive 6th root of unity.** -/
theorem jvw_no_order_six (t : C12)
    (ht : t = 1 ∨ t = -1 ∨ t = I ∨ t = -I ∨ t = omega ∨ t = omega⁻¹) :
    ¬ IsPrimitiveRoot t 6 := by
  intro h6
  rcases ht with rfl | rfl | rfl | rfl | rfl | rfl
  · exact absurd (IsPrimitiveRoot.one.unique h6) (by norm_num)
  · exact absurd (neg_one_prim.unique h6) (by norm_num)
  · exact absurd (I_prim.unique h6) (by norm_num)
  · exact absurd (negI_prim.unique h6) (by norm_num)
  · exact absurd (omega_prim.unique h6) (by norm_num)
  · exact absurd (omega_inv_prim.unique h6) (by norm_num)

theorem four_not_dvd_six : ¬ (4 ∣ 6) := by decide

end QOU.Information.JonesTractable
