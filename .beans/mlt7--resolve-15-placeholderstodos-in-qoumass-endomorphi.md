---
# mlt7
title: Resolve 15 placeholders/TODOs in qou/mass-endomorphism
status: completed
type: task
priority: normal
created_at: 2026-06-22T02:25:52Z
updated_at: 2026-07-05T05:05:00Z
---

resweep 2026-06-22: honest counter = 2 actionable (claimed 15) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 2 (claimed 15): qbeta-per-block 1, explicit-central-idempotent 1. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

drain 2026-06-23 (#2656): de-vacuified qbeta-per-block-chi-closed-forms order-2 taylor-coeff (`: True` → real deriv statement + cited sorry). uncited-sorry → 0.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 1 TODO/FIXME marker (claimed 15) in mass-endomorphism, 0 sorries. Recommend re-scope to the 1 marker or close. (Note: duplicate bean file exists for this id.)

> **Resolved 2026-07-05 (swarm 1).** Triaged: no agent-tractable prose/metadata placeholders remain (already drained by prior sessions #2649/#2654/#2637/#2796); residual = author DOI/edition decisions, documented as deferred. Audit merged in PR #3339.

<!-- recovered 2026-08-23 from orphaned file `mlt7--resolve-15-placeholders-todos-in-qou-mass-endomorphism.md` (no front-matter; invisible to the tracker) -->

## Result (2026-06-23, session nifty-cerf, PR #2649)

Honest actionable 2 → **0**.
- `explicit-central-idempotent` item: already resolved on main (commit
  16deaa76 cited the (2,2) central-idempotent witness sorry). Counter
  confirms 0 there.
- `qbeta-per-block-chi-closed-forms.lean`: `delta_tau_M_surrogate_taylor_coeff_2`
  was a **`theorem : True := trivial` vacuity dodge** (forbidden by AGENTS.md
  §1a, caught by vacuity audit 508cbd70). Converted to the **honest §1a
  disposition 2**: stated the real proposition
  `deriv (deriv delta_tau_M_surrogate) 1 / 2 = 5/6` (the order-2 Taylor
  coefficient f''(1)/2! = 5/6, matching the docstring's `+(5/6)w²` and the
  SymPy witness) with `sorry` + the existing `-- Ref:`. Reworded the trailing
  "Stated as TODO" comment. Full 2nd-derivative proof deferred (build-gated;
  orders 3..7 remain future work vs the same witness).

NOT done (build-gated): proving the cited order-2 sorry. Pending human close.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 1 TODO/FIXME marker (claimed 15) in mass-endomorphism, 0 sorries. Recommend re-scope to the 1 marker or close. (Note: duplicate bean file exists for this id.)

> **Resolved 2026-07-05 (swarm 1).** Triaged: no agent-tractable prose/metadata placeholders remain (already drained by prior sessions #2649/#2654/#2637/#2796); residual = author DOI/edition decisions, documented as deferred. Audit merged in PR #3339.
