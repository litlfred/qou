---
# qou-59x9
title: 'GAP: prop:content-scaling-correspondence — BoxContent.lean has no theorem; the content ↦ m_j claim is unformalised'
status: in-progress
pr: 8198
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T06:21:23Z
updated_at: 2026-11-16T20:55:00Z
parent: qou-10v9
---

Opened 2026-09-04 from docs/audits/2026-09-04-lean-ref-resolution-count-mass-theory.md (bean qou-jkam, PR #6554). The block's lean.ref RESOLVES, so no presence-keyed or sorry-keyed detector fires; the resolved declaration is not the block's claim. Honest next step: state the proposition as a real Lean statement (a theorem with sorry + -- Ref:, or the named-Prop carrier form the qou-z9ws drain uses), then derive what can be derived. Do not repoint the ref at a positivity or specialisation lemma — that swaps one non-claim for another (Correction 2 in the audit).



RESULT 2026-09-04 (branch claude/content-scaling-theorem-2026-09-04): the proposition's literal claim is FALSE, and the obstruction is structural (scope (b), Lean-proved, sorry-free, lean-direct exit 0): for two-row (a,b), #cells a+b != #weights a-b+1 for ALL a,b (would need 2b=1), and for a+b>=3 the cell (0,a-1) has 2*content = 2a-2 > a-b, so its content is not a weight of V_(a,b) under any assignment. (1,0) fails by parity, (1,1) by range; (2,0) is the only shape where every content is a weight. What is true: contents are the q-JM eigenvalues (QOU.SchurWeyl.QJucysMurphyEigen.SeminormalRep.jmDiagVal has q^(2*content) on the diagonal) — a Casimir/total-spin-increment datum, not m_j. The consumer crystal-isospin-degeneracy-proof uses only c(.) and content differences, untouched. Lean landed in BoxContent.lean (the resolved carrier) + rfl bridge to the canonical YoungDiagramCells.content. NOT done: rewording the .md (owner call — it changes the chapter's claim); lean.ref left on boxContent (a proposition's ref must not point at its own refutation).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 54 Progress (PR #8198)
- [x] Added `twoRow_all_weights_forces_two_zero` (complete classification showing `(2,0)` is the unique non-empty two-row shape whose box contents all lie in the `SU(2)` weight set of `V_(a,b)`), `boxContent_transpose_neg`, `axialDistance`, and `axialDistance_shift_invariant` to `folio/quantum-observable-universe/lean/QOU/BraidKnot/BoxContent.lean` (`0 sorry`, `0` new vacuity hits).
- [x] Verified two-row shape classification and axial-distance shift invariance in `computations/probes/boxcontent_ward_nv_interface_binding_probe.py` (`computations/probes/boxcontent-ward-nv-interface-binding.witness.json`, Commit 1 `f173f5c66fdcbc0069dcbfce2da8a154bd52f3e4`).
- [ ] Await CI verification and Merge Manager merge of PR #8198 (`1f80984f96ba3e6334bf43a2df76dd82a90eba3e`).
