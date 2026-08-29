---
# qou-t28w
title: 'PROVE(lean): q_ns_wellposedness — theorem q_ns_wellposedness [ctx : QNsWellposednessContext] : (∃! sol : ℝ → ctx.Velocity ×  [cited manuscript]'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-08-29T17:51:51Z
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

**Scope narrowed 2026-08-29** (PR #6041). The theorem no longer assumes itself:
(ii) the energy inequality and (iii) the Delta_q spectral decay are now PROVED in
`QOU/FluidDynamics/q_ns_energy_and_decay.lean` by Gronwall comparison, from the
pointwise energy balance and the modal differential inequality respectively.

What remains open, and all that remains, is global existence + uniqueness +
regularity -- the Millennium-adjacent core. The class fields are now
`existence_uniqueness` and `smooth_of_isSolution`; tier B still applies to
those, but no longer to the whole statement.

Note the tracked artifact had drifted: this bean and `qou-7aj0` both described
'1 cited sorry at line 109'; the file had no sorry at all, it had a
self-assuming projection. See `qou-llew`.
