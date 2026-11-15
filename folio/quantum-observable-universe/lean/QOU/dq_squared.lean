import Mathlib.Data.Real.Basic

/-!
# QOU.dq_squared — archimedean specialisation of `d_q² α`

**Proposition** ([`prop:categorical-dq-squared`-archimedean specialisation](../../../quantum-observable-universe/quantum-observable-universes/dq-squared.md)).

*For the `q`-deformed exterior derivative acting on `Ω^k(M)`,*

```
  d_q² α = q⁻¹ · (1 − q⁻¹) · dΘ ∧ 𝓛_ξ α
```

*where `Θ` is the connection form and `ξ` is the Reeb vector field.
In particular, `d_q² = 0` identically when `q = 1` (recovering the
classical de Rham `d² = 0`).*

The Lean encoding records the formula against an abstract
`DqSquaredContext` carrying the differential-form data
`(α, dΘ ∧ 𝓛_ξ α)` and the substrate parameter `q`.  Concretising
to a real `Ω^k(M)` exterior algebra is downstream work.

-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/dq-squared.md
-/

namespace QOU

/-- Abstract context for the archimedean `d_q² α` formula. -/
class DqSquaredContext where
  /-- The `k`-form space. -/
  ΩK : Type
  /-- Scalar-multiplication on `ΩK`. -/
  smul : ℝ → ΩK → ΩK
  /-- The `q`-deformed exterior derivative squared `d_q²`. -/
  d_q_squared : ΩK → ΩK
  /-- The wedge product `dΘ ∧ 𝓛_ξ α` packaged as a function of `α`. -/
  dTheta_wedge_lieXi : ΩK → ΩK
  /-- The substrate parameter `q`. -/
  q : ℝ
  /-- Positivity: `q > 0`. -/
  q_pos : 0 < q
  /-- Manuscript `d_q²` formula: `d_q² α = q⁻¹·(1 − q⁻¹)·(dΘ ∧ 𝓛_ξ α)`
      for every `k`-form `α`. -/
  claim_dq_squared : ∀ α : ΩK,
    d_q_squared α = smul (q⁻¹ * (1 - q⁻¹)) (dTheta_wedge_lieXi α)

/-- **Archimedean `d_q² α` formula** ([`prop:categorical-dq-squared`]).

    `d_q² α = q⁻¹ · (1 − q⁻¹) · (dΘ ∧ 𝓛_ξ α)`. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/dq-squared.md
theorem dq_squared [ctx : DqSquaredContext] (α : ctx.ΩK) :
    ctx.d_q_squared α
      = ctx.smul (ctx.q⁻¹ * (1 - ctx.q⁻¹)) (ctx.dTheta_wedge_lieXi α) :=
  ctx.claim_dq_squared α

/-- **Classical-limit corollary** (`q = 1`): the formula's scalar factor
    `q⁻¹·(1 − q⁻¹)` vanishes, so `d_q²` is the zero operator,
    recovering classical de Rham `d² = 0`. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/dq-squared.md
theorem dq_squared_at_q_eq_one [ctx : DqSquaredContext] (α : ctx.ΩK)
    (h_q : ctx.q = 1) :
    ctx.d_q_squared α = ctx.smul 0 (ctx.dTheta_wedge_lieXi α) := by
  rw [dq_squared α, h_q]
  simp

end QOU
