---
# qou-sekl
title: 'categorical-dq-squared-proof.lean: delete shadowing :True stub'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T18:41:38Z
updated_at: 2026-11-16T18:28:22Z
parent: qou-6qbv
---

theorem categorical_dq_squared : True (line 34) shadows the real sorry-free decl at lean/QOU/CategoricalDqSquared.lean:67 (and the prop-block sibling categorical-dq-squared.lean carries the full iff proof). Fix per §0a no-shadowing-stub: delete the stub, repoint proof-block lean.ref to the real decl.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-11 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Verification & Audit Note (2026-11-16 — Round 47, PR #8147)

- Verified on `main` that the shadowing `: True` stub `categorical-dq-squared-proof.lean` was deleted in commit `969ebda6d6` (`2026-07-11`, *"fix(lean): delete shadowing categorical_dq_squared :True stub"*), and `prf:categorical-dq-squared` (`folio/quantum-observable-universe/quantum-observable-universes/categorical-dq-squared-proof.ts`) points to `qou:QOU.categorical_dq_squared` (`validation: "leanok"`) in `folio/quantum-observable-universe/lean/QOU/CategoricalDqSquared.lean` (generalized over `R_q` in `7ce4339cd1`, `0` `sorry`).
- Meanwhile `prop:categorical-dq-squared` (`folio/quantum-observable-universe/quantum-observable-universes/categorical-dq-squared.lean`) carries the full sorry-free `iff` proof `categorical_dq_squared [IsDomain R] (obs : DqSquaredObstruction R) : obs.obstruction = 0 ↔ (obs.q = 1 ∨ obs.reeb_bracket = 0)`.
- Kept at `status: in-progress` per owner rule (no unilateral bean closure; ready for owner review).
