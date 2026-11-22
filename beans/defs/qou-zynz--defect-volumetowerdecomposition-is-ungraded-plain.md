---
# qou-zynz
title: 'DEFECT: VolumeTowerDecomposition is UNGRADED (plain HasSum). The rem:yekutieli-transcendence-shadow inference ''polynomial relation among volumes => tower closes at finite height'' is a non sequitur for a plain convergent sum - a relation among sums imposes ONE equation and cannot force termwise vanishing'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T22:14:21Z
updated_at: 2026-11-22T21:33:09Z
parent: qou-n4nr
---

## Progress Update (PR litlfred/qou#8244)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8244 (`457d28e500f11a4249f57fd33fcd18112faef23b`, scriptCommitSha `1086b0ae6f630df61ca513a195514ef5d6137b5c`)
- **Summary**: Added `gradewise_three_term_determines_level` and `gradewise_three_term_closure_propagates` in `QOU/Archimedean/TowerHeightAttack.lean`, verified by 80-dps mpmath probe `frust_cubic_tower_jhopf_whitehead_probe.py`.

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

No change. The fix is a change to how `rem:yekutieli-transcendence-shadow` argues, so it needs the owner. The latest note above points at batch PR #8244 (closed), which was closed unmerged; its theorems are short algebraic identities with the bean's quantities as free variables, and they do not bear on this bean's question. Treat this bean's state as what the earlier text says.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: APPLIES.** Formal mathematics (volume conjecture, Lean hyperbolic/AJ infrastructure, Mathlib gaps). Checked its premises against owner-rulings.md on main: it uses none of the retired ones (σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, substrate-q₀ derivation, virtual photons, SM quark charges). Today's rulings (strand colour states, b = −qX on colour singlets with flavour trace values unchanged, convention D on the baryon sector, photon kept with fixed constant 1) do not reach knot-complement geometry. Its batch-PR notes (Nov 16–18 Round PRs) are all still open and unmerged as of 2026-11-22.
