---
# qou-t28w
title: 'PROVE(lean): q_ns_wellposedness — theorem q_ns_wellposedness [ctx : QNsWellposednessContext] : (∃! sol : ℝ → ctx.Velocity ×  [cited manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - infra-blocked
    - reorg-2026-10-04
    - lean
    - cited-sorry
    - paper-qou
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-10-04T15:22:43Z
parent: qou-gdcu
---

**File:** `QOU/FluidDynamics/q_ns_wellposedness.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_wellposedness.lean

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


## RE-TRIAGED 2026-08-31 — MILLENNIUM-CLASS OPEN PROBLEM — not a Mathlib gap

The `Next step` line above ("Infra-blocked: needs Mathlib theory that does not exist. Track
upstream") is one verdict that was stamped on fourteen beans in six seconds, and is wrong here.
Full audit: `docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md`.

Existence + uniqueness + smoothness for q-Navier-Stokes. The Tractability line already says
"millennium-type, open"; the Next-step line then attributes the blockage to missing Mathlib.
Those are different claims and only the first is right.

Note `q_ns_energy_inequality` in the same file DOES real work -- it applies
`energy_inequality_of_balance`, an external lemma -- so the class there is carrying genuine
hypotheses, not the conclusion.

The original text is kept above, not deleted: the Tractability line is per-item and is accurate;
only the Next-step verdict is being corrected.
