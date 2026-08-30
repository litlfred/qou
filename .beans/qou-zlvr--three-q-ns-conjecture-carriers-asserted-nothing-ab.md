---
# qou-zlvr
title: 'Three q-NS conjecture carriers asserted nothing about their subject (PR #6099)'
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:50:55Z
updated_at: 2026-08-30T09:05:51Z
---

PR #6099 (draft), branch `claude/upstream-vacuous-carriers-2026-08-30`.

Three carriers, one defect family: the object a claim is about must be data
or a parameter, never something the instance chooses or something the claim
never mentions.

- `QOU.FluidDynamics.QAubinLions` — one field, `∃ q_thresh : ℝ, q_thresh > 0`,
  discharged by 1. Docstring had literal holes where symbols were dropped.
- `QOU.FluidDynamics.RegularityBreakdown` — one field, `∃ Re_c : ℝ, Re_c > 0`,
  discharged by 1, AND about the wrong object: its docstring speaks of a
  critical Reynolds number and a Sobolev H² bound, neither of which the .md
  conjecture mentions.
- `QOU.FluidDynamics.LeviGrowthTrichotomy` — `condNumber` and `beta` with no
  field relating them. MEASURED against the old definition: two instances
  type-check, including `condNumber ≡ 1` (true exponent 0) with `beta = 1`,
  the opposite branch of the conjecture. All three theorems in the file used
  only `beta_mem`, so they were facts about [0,1] dressed as facts about a
  Levi trichotomy.

All three now parametrised by the objects their .md is about, one field per
clause, with consistency witnesses and six negative controls. The tie earns a
theorem: `bounded_condNumber_forces_beta_zero` derives the .md's branch-(A)
identification of β = 0 with C_L = O(1), which the old definition made false.

lean-direct exit 0 on all three; no sorry; #print axioms clean; qa-sweep
refreshed; zero consumers of any changed declaration.

Still open and untouched: the value of β — which branch of conj:levi-degeneracy
obtains — remains the conjecture's open content.

COMPLETED — PR #6099 merged 2026-08-30.

All three fluid-dynamics carriers landed parametrised by the objects their .md
is about, with consistency witnesses and six negative controls:
QAubinLions, RegularityBreakdown, and LeviGrowthTrichotomy (whose beta is now
tied to condNumber by a two-sided limsup, earning
bounded_condNumber_forces_beta_zero).

Re-measured after the merge: scripts/unbounded-quantifier-audit.py reports 0
candidates over 57 files across fluid-dynamics/ and lean/QOU/FluidDynamics/.
The q-NS carriers no longer assert nothing.

Scope note, so this is not over-read: this closed STATEMENT HYGIENE, not
mathematics. None of the six walls in qou-innq moved. What changed is that
wall 3 (the Levi branch value beta) is now EXPRESSIBLE in Lean, which it was
not before.
