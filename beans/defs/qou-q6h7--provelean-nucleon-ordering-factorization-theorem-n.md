---
# qou-q6h7
title: 'PROVE(lean): nucleon_ordering_factorization — theorem nucleon_ordering_factorization [ctx : NucleonOrderingFactorizationContext] : ctx.t [cited jones1987,manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-jones1987
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-10-04T15:22:40Z
parent: qou-l2vh
---

**File:** `QOU/Interactions/nucleon_ordering_factorization.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/Interactions/nucleon_ordering_factorization.lean

### `nucleon_ordering_factorization`  —  line 89  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem nucleon_ordering_factorization [ctx : NucleonOrderingFactorizationContext] : ctx.trM_N = ctx.W_sym * ctx.S_pi + ctx.W_std * (ctx.z * ctx.a_pi + ctx.b_pi) + ctx.W_alt * ctx.A_pi `
- **Cited:** `[manuscript]`, `[jones1987]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/particle-interactions/nucleon-ordering-factorization.md
  - [jones1987] Jones (1987), *Hecke algebra representations of braid groups and link polynomials* — https://doi.org/10.2307/1971403
- **Tractability:** trM_N = W_sym·S_π + W_std·(…) + W_alt·A_π factorization; repo Hecke/Markov compute identity.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

## Progress Update (Round 92 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/NucleonOrderingAndBringAdjointTorsionBrick.lean` with 80-dps probe `computations/probes/nucleon_ordering_and_bring_adjoint_torsion_brick_probe.py` and witness `computations/probes/nucleon-ordering-and-bring-adjoint-torsion-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8348 (`feat/qou-b9cj-q6h7-qd27-qint-r91v-tvok`, HEAD `e0985c4fc3ff765e1935e3343005512aaca69b2b`).
