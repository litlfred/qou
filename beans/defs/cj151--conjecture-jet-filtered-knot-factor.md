---
# cj151
title: 'Conjecture carrier: jet_filtered_knot_factor (jet_filtered_knot_factor.lean) — §3b, framework/substrate §3b carrier'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-18T09:14:00Z
parent: qou-j5ch
---

§3b conjecture-class Lean carrier `instance : jet_filtered_knot_factor := sorry` at folio/quantum-observable-universe/lean/QOU/BraidKnot/jet_filtered_knot_factor.lean:67. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.

## Progress Update (2026-11-18 — Round 66, PR #8415)

- Added unconditional q-Plancherel weight consequences (`jetWeight_eq_zero_of_dq_zero`, `jetWeight_mul_partitionFunction`), conditional `jet_filtered_knot_factor` consumer theorems (`factor_sub_eq_zero`, `weighted_factor_eq`, `factor_diff_eq`), and falsifiability witness `not_of_mismatch` in `QOU/BraidKnot/jet_filtered_knot_factor.lean` (PR litlfred/qou#8415).
