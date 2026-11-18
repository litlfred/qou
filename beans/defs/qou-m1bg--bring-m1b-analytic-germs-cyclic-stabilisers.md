---
# qou-m1bg
title: 'Bring M1b: finite groups of holomorphic germs fixing a point are cyclic (discharges hstabA/hstabS of genus_eq_four_of_cellular)'
status: todo
type: task
priority: high
tags:
    - for-agy
    - bring-foundations
    - lean
created_at: 2026-11-18T19:26:09Z
updated_at: 2026-11-18T19:26:09Z
parent: qou-qhcr
---
**For agy.** Written 2026-11-18 by the Bring-foundations thread at ofri's request ("bean up for agy to do: C + A"). Parent bean `qou-qhcr` must never be closed.

## Context

Branch `claude/bring-foundations-handover-2026-11-17` (draft PR litlfred/qou#8365). The capstone `genus_eq_four_of_cellular` in `folio/quantum-observable-universe/lean/QOU/BringsSurface/RiemannHurwitzCellular.lean` takes as hypotheses `hstabA`, `hstabS`: every point stabiliser has order 1, 2, 3, 5 (for A5), or 1–6 (for S5). Those follow once a stabiliser is known to be **cyclic**: its order is then an element order of the group.

M1 is done and sorry-free in `folio/quantum-observable-universe/lean/QOU/RiemannSurface/TangentJetRigidity.lean`:
- `JetEq`, `jet_comp`, `jet_iterate`: the formal-power-series algebra of jets X + a·X^k under composition;
- `eq_X_of_finite_order`: in characteristic 0, a finite-order jet tangent to the identity is the identity;
- `isCyclic_of_injective_derivative`: a finite group whose derivative map into the units of a domain is injective is cyclic (via Mathlib `isCyclic_of_subgroup_isDomain`).

So M1 is the **formal** statement. M1b lifts it to actual holomorphic germs.

## Task

Prove: if a finite group G acts by holomorphic maps on a neighbourhood of 0 in ℂ, fixing 0, then g ↦ g′(0) is injective, so G is cyclic.

Sub-steps:
1. **Taylor coefficients of a composition.** For f, g analytic at 0 with f(0) = g(0) = 0, the low-order Taylor coefficients of f ∘ g follow the jet rule in `jet_comp`. Use Mathlib `HasFPowerSeriesAt`, `FormalMultilinearSeries.comp`, and `HasFPowerSeriesAt.comp`.
2. **Kernel is trivial.** If g′(0) = 1 and g has finite order, the first non-zero higher coefficient contradicts `eq_X_of_finite_order`. So g agrees with id to all orders at 0.
3. **Identity theorem.** Then g = id near 0. Use `AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq` or the `HasFPowerSeriesAt.eq_formalMultilinearSeries` route.
4. Conclude with `isCyclic_of_injective_derivative`. Then derive `hstabA` / `hstabS` from "cyclic subgroup of A5 / S5 has order in {1,2,3,5} / {1,…,6}" (a `decide`-able fact about element orders, given concrete A5/S5 — or keep it as the named hypothesis if the group is abstract).

The chart step, that a holomorphic action on a Riemann surface is locally such a germ action, is out of scope here. Keep it a hypothesis and say so.

## Rules

Same as qou-m3tr. Sorry-free or `-- Ref:`-cited. No axioms standing in for proofs. Report exactly what is proved. Ask ofri before opening a math PR; merge only on his tap.

## How to verify

Same recipe as qou-m3tr: GitHub-release Lean 4.24.0, Mathlib oleans from `cat/folio-assistant-sci/lake-cache/qou-v4-24-0`, `lean -DautoImplicit=false -s 65536`, `#print axioms`. The Mathlib analytic files (Analysis.Analytic.Composition, Analysis.Analytic.Uniqueness) may not be in the restored cache. If so, build them lean-direct into a scratch dir, not with lake.
