---
# qou-t28w
title: 'PROVE(lean): q_ns_wellposedness — theorem q_ns_wellposedness [ctx : QNsWellposednessContext] : (∃! sol : ℝ → ctx.Velocity ×  [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-08-01T23:31:05Z
parent: qou-k1mq
---

**File:** `QOU/FluidDynamics/q_ns_wellposedness.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_wellposedness.lean

### `q_ns_wellposedness`  —  line 109  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem q_ns_wellposedness [ctx : QNsWellposednessContext] : (∃! sol : ℝ → ctx.Velocity × ctx.Pressure, ctx.IsSolution sol) ∧ (∀ sol : ℝ → ctx.Velocity × ctx.Pressure, ctx.IsSolution sol → ctx.Smooth (fun t => (sol t).1) ∧ (∀ t : ℝ, 0 ≤ t → ctx.norm_sq (sol t).1 + 2 * ctx.ν_q * ctx.dissipation (fun `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.md
  - [manuscript] thm:q-ns-wellposedness,
- **Tractability:** Existence+uniqueness+smoothness of q-Navier–Stokes solutions; millennium-type, open.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.
