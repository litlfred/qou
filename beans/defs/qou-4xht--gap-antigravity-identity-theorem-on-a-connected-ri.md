---
# qou-4xht
title: 'GAP (Antigravity): identity theorem on a connected Riemann surface, to discharge hloc of ChartStep'
status: in-progress
type: task
priority: high
tags:
    - for-antigravity
    - bring-foundations
    - lean
    - mathlib-gap
created_at: 2026-11-21T07:30:00Z
updated_at: 2026-11-23T17:32:52Z
parent: qou-mq3p
---

Created 2026-11-21 by W9 (session_01VQDpPcjxVSqN8ELUBjiBHk). The owner ruling of 2026-11-21 says time- or resource-limited work goes to a bean for Antigravity.

**Target.** `QOU.RiemannSurface.ChartStep.isCyclic_stabilizer_of_chart` (PR from branch `claude/bring-chart-step-2026-11-21`) proves that point stabilisers of a finite holomorphic action are cyclic. It assumes one hypothesis, `hloc`: no g ≠ 1 in the stabiliser of p fixes a neighbourhood of p pointwise.

**What to prove.** Let M be a connected complex 1-manifold (`ChartedSpace ℂ M` with holomorphic transition maps), and let f : M → M be holomorphic with f = id on a nonempty open set. Then f = id. Consequence: for an effective holomorphic action, hloc holds.

**Plan.**
1. Let U be the set of points near which f = id. U is open by definition and nonempty.
2. U is closed. For q in the closure of U, work in a chart at q and apply `AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq` on a small disk. f(q) = q by continuity, so the coordinate expression of f is defined near q.
3. Connectedness gives U = M.

**Mathlib status.** The identity theorem exists on open sets of ℂ. The `MDifferentiable` / complex-manifold version is absent.

**Must not:** use an axiom or a class standing in for the theorem.


## 2026-11-22 — wave-2 sibling bring-riemann-gerbes (session_01Qmmkt7Jw9nSDCzSdsd8hLX)

Identity theorem PROVED, sorry-free, on branch `claude/riemann-identity-theorem-2026-11-22` (commits c0b3526ba, 69b56b092; stacked on PR #8750). File `QOU/RiemannSurface/IdentityTheorem.lean`:
- `eq_id_of_eventuallyEq_id`: M connected, T2, `IsManifold 𝓘(ℂ) 1 M`; holomorphic (`MDifferentiable`) f : M → M with f = id near one point is id.
- `local_effective_of_faithful`: hloc of ChartStep holds for a faithful holomorphic action.
- `isCyclic_stabilizer_of_faithful` (ChartStep with hloc discharged) and `isCyclic_stabilizer` (no chart hypothesis at all: finite faithful holomorphic action on a connected Riemann surface has cyclic point stabilisers).
lean -DautoImplicit=false exit 0 against the restored lake-cache (ChartStep compiled lean-direct); #print axioms [propext, Classical.choice, Quot.sound]. No PR yet (math repo: owner asked first). Close this bean when the branch merges.

## 2026-11-22 applicability review (wave-2 sibling bring-riemann-gerbes, session_01Qmmkt7Jw9nSDCzSdsd8hLX)

ALREADY-DONE pending merge: PR #9133 (stacked on #8750) proves eq_id_of_eventuallyEq_id and local_effective_of_faithful, which discharge hloc. Complete this bean when #9133 merges, not before.



## 2026-11-23 — WS4 Consolidation Update (PR #9189)
- Consolidated `#8750` + `#9133` (`QOU/RiemannSurface/ChartStep.lean` + `QOU/RiemannSurface/IdentityTheorem.lean`: `holomorphic_eq_id_of_eq_on_open`, `hloc_of_faithful`, `isCyclic_stabilizer_of_faithful`, 14 theorems, 0 `sorryAx`) into Ready PR https://github.com/litlfred/qou/pull/9189 (`b5d39499b04`).
