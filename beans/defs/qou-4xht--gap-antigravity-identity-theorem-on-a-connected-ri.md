---
# qou-4xht
title: 'GAP (Antigravity): identity theorem on a connected Riemann surface, to discharge hloc of ChartStep'
status: todo
type: task
priority: high
tags:
    - for-antigravity
    - bring-foundations
    - lean
    - mathlib-gap
created_at: 2026-11-21T07:30:00Z
updated_at: 2026-11-21T07:30:00Z
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
