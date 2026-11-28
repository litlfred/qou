import Mathlib.RingTheory.RootsOfUnity.Complex

/-!
# QOU.Information.JonesTractableOrders — the orders of the JVW tractable points

Human statement (`prop:jvw-tractable-orders`). Jaeger, Vertigan and Welsh show that exact
evaluation of the Jones polynomial `V_L(t)` is `#P`-hard except at
`t ∈ {1, −1, i, −i, e^{2πi/3}, e^{−2πi/3}}` (cited, not formalised). Each of these six
points is a primitive root of unity of order `1, 2, 4, 4, 3, 3` respectively
(`jvw_orders`). None of them is a primitive 6th root of unity (`jvw_no_order_six`),
and `i` has order `4`, which does not divide `6` (`four_not_dvd_six`). So in the
convention `t = q`, the set of orders of the tractable points is `{1, 2, 3, 4}`,
not `{n : n ∣ 6}`.
-/

namespace QOU.Information.JonesTractable

open Complex

/-- `ω = e^{2πi/3}`. -/
noncomputable def omega : ℂ := exp (2 * Real.pi * I / 3)

theorem omega_prim : IsPrimitiveRoot omega 3 := by
  have := Complex.isPrimitiveRoot_exp 3 (by norm_num)
  simpa [omega] using this

theorem I_prim : IsPrimitiveRoot I 4 := by
  refine IsPrimitiveRoot.mk_of_lt I (by norm_num) ?_ ?_
  · norm_num [pow_succ, Complex.ext_iff]
  · intro l hl hl4
    interval_cases l <;> norm_num [pow_succ, Complex.ext_iff]

theorem negI_prim : IsPrimitiveRoot (-I) 4 := by
  refine IsPrimitiveRoot.mk_of_lt (-I) (by norm_num) ?_ ?_
  · norm_num [pow_succ, Complex.ext_iff]
  · intro l hl hl4
    interval_cases l <;> norm_num [pow_succ, Complex.ext_iff]

theorem omega_inv_prim : IsPrimitiveRoot omega⁻¹ 3 := omega_prim.inv

theorem neg_one_prim : IsPrimitiveRoot (-1 : ℂ) 2 :=
  IsPrimitiveRoot.neg_one 0 (by norm_num)

/-- **The six JVW points and their orders.** -/
theorem jvw_orders :
    IsPrimitiveRoot (1 : ℂ) 1 ∧ IsPrimitiveRoot (-1 : ℂ) 2 ∧ IsPrimitiveRoot I 4 ∧
      IsPrimitiveRoot (-I) 4 ∧ IsPrimitiveRoot omega 3 ∧ IsPrimitiveRoot omega⁻¹ 3 :=
  ⟨IsPrimitiveRoot.one, neg_one_prim, I_prim, negI_prim, omega_prim, omega_inv_prim⟩

/-- **No JVW point is a primitive 6th root of unity.** -/
theorem jvw_no_order_six (t : ℂ)
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
