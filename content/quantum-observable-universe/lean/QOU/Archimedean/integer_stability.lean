import Mathlib.Tactic

/-!
# QOU.Archimedean.integer_stability — convex-quadratic binding `E(p, A)`

**Proposition** ([`prop:integer-stability`](../../../quantum-observable-universe/archimedean-universe/integer-stability.md)).

*At fixed mass number `A = Z + N`, the nuclear binding energy is a
convex quadratic in the proton number `p`:*

```
  E(p, A) = α(A) · p² − γ · p + δ(A),     where
  α(A) = a_C / A^{1/3} + a_A / A
  γ    = a_A
  a_C  = (q − q⁻¹) · λ_C        (Coulomb coefficient, `q`-deformed)
  a_A  = Pauli asymmetry coefficient.
```

*The Coulomb coefficient `a_C` is positive at `q > 1`, so `α(A) > 0`
and the parabola is convex; the unique integer optimum `p*(A)` is
the closest integer to the real minimiser.*

The Lean encoding records the quadratic shape + the convexity claim
(`α(A) > 0`) as a single proposition.  Concretising `a_C` and `a_A`
to the substrate-derived Coulomb/Pauli scales is downstream work.

-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/integer-stability.md
-/

namespace QOU.Archimedean

/-- Abstract nuclear-binding-energy context. -/
class IntegerStabilityContext where
  /-- The substrate parameter `q`, with `q > 1`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Coulomb scale `λ_C > 0`. -/
  lam_C : ℝ
  lam_C_pos : 0 < lam_C
  /-- Pauli asymmetry coefficient `a_A > 0`. -/
  a_A : ℝ
  a_A_pos : 0 < a_A
  /-- The mass number `A ≥ 1`. -/
  A : ℕ
  A_pos : 0 < A
  /-- The intercept `δ(A)`. -/
  δ_A : ℝ

/-- The Coulomb coefficient `a_C = (q − q⁻¹) · λ_C`.  Positive at
    `q > 1` since both factors are positive. -/
noncomputable def coulombCoeff (ctx : IntegerStabilityContext) : ℝ :=
  (ctx.q - ctx.q⁻¹) * ctx.lam_C

/-- The quadratic-leading coefficient `α(A) = a_C / A^{1/3} + a_A / A`. -/
noncomputable def alphaCoeff (ctx : IntegerStabilityContext) : ℝ :=
  coulombCoeff ctx / (ctx.A : ℝ) ^ ((1 : ℝ) / 3) + ctx.a_A / (ctx.A : ℝ)

/-- The binding-energy function `E(p, A) = α(A)·p² − a_A·p + δ(A)`. -/
noncomputable def bindingEnergy (ctx : IntegerStabilityContext) (p : ℝ) : ℝ :=
  alphaCoeff ctx * p ^ 2 - ctx.a_A * p + ctx.δ_A

/-- **Coulomb coefficient is positive at `q > 1`**. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/integer-stability.md
theorem coulombCoeff_pos (ctx : IntegerStabilityContext) :
    0 < coulombCoeff ctx := by
  unfold coulombCoeff
  -- `q − q⁻¹ > 0` since `q > 1`, and `λ_C > 0` by hypothesis.
  have h_q_pos : 0 < ctx.q := by linarith [ctx.q_gt_one]
  have h_q_sub_inv : 0 < ctx.q - ctx.q⁻¹ := by
    rw [sub_pos]
    have : ctx.q⁻¹ < 1 := (inv_lt_one_iff_of_pos h_q_pos).mpr ctx.q_gt_one
    linarith [ctx.q_gt_one]
  exact mul_pos h_q_sub_inv ctx.lam_C_pos

/-- **Convex-quadratic binding energy** ([`prop:integer-stability`]).

    The binding-energy function `E(p, A)` is a convex quadratic in
    `p`: its leading coefficient `α(A)` is strictly positive. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/integer-stability.md
theorem integer_stability (ctx : IntegerStabilityContext) :
    0 < alphaCoeff ctx := by
  unfold alphaCoeff
  -- Both summands are positive: `coulombCoeff > 0`, `(A : ℝ)^{1/3} > 0`,
  -- and `a_A / A > 0` since `a_A > 0`, `A > 0`.
  have h_A_pos : (0 : ℝ) < ctx.A := by exact_mod_cast ctx.A_pos
  have h_A_third : (0 : ℝ) < (ctx.A : ℝ) ^ ((1 : ℝ) / 3) := by
    -- `a^x > 0` when `a > 0` (Real.rpow_pos_of_pos)
    exact Real.rpow_pos_of_pos h_A_pos _
  have h_first : 0 < coulombCoeff ctx / (ctx.A : ℝ) ^ ((1 : ℝ) / 3) :=
    div_pos (coulombCoeff_pos ctx) h_A_third
  have h_second : 0 < ctx.a_A / (ctx.A : ℝ) :=
    div_pos ctx.a_A_pos h_A_pos
  linarith

end QOU.Archimedean
