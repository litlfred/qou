---
# qou-yslf
title: 'GAP (Antigravity): G-equivariant triangulation of a compact Riemann surface (Rado), to supply the map in GenusFourFromEquivariantMap'
status: todo
type: task
priority: high
tags:
    - for-antigravity
    - bring-foundations
    - lean
    - mathlib-gap
created_at: 2026-11-21T07:30:00Z
updated_at: 2026-11-27T22:05:44Z
parent: qou-6qbv
---

Created 2026-11-21 by W9 (session_01VQDpPcjxVSqN8ELUBjiBHk). The owner ruling of 2026-11-21 says resource-limited work goes to a bean for Antigravity.

**Target.** `QOU.BringsSurface.GenusFourFromEquivariantMap.chi_eq_neg_six_of_equivariant_map` (merged, #8719) starts from a connected combinatorial map (darts D, rotation σ, fixed-point-free involution α) with G-actions. Its hypotheses: the actions commute with σ and α, act freely on edges and faces, and have cyclic vertex stabilisers.

**What to prove.** A compact connected Riemann surface X with a finite group G acting holomorphically carries such a map. More precisely, X has a G-invariant triangulation with every branch point a vertex, and its flag/dart encoding gives (D, σ, α). The map's genus must also equal the topological genus of X.

**Ingredients, none in Mathlib:**
- Radó's theorem (every Riemann surface is triangulable);
- the equivariant refinement: lift a triangulation of X/G, with the branch values as vertices, along the branched cover;
- the identification of the combinatorial χ with the topological one.

**Must not:** use an axiom or class standing in for the triangulation. Until proved, it stays the theorem's starting data.

## 2026-11-22 applicability review (wave-2 sibling bring-riemann-gerbes, session_01Qmmkt7Jw9nSDCzSdsd8hLX)

APPLIES. Premises checked against owner-rulings.md on origin/main (all rows to 2026-11-22: photon with fixed constant 1, γγ linking neutrality, derived quark charges, potential-energy sign, m_p = m_n at q = 1, gluon open, electron σ₀σ₁σ₀ with T(2,n) as backup, S₅ two-test rule, T(A) tangent algebra) and git log on the Lean/content paths since the last update. Radó plus equivariant refinement is unchanged and still the sole topological gap of M3. Antigravity bean per the 2026-11-21 resource ruling.

## 2026-11-22 tracker hygiene (qou-w3yy, owner-approved)

Parent set to `qou-6qbv`: old parent `qou-m3tr` is not an epic/milestone/feature; re-pointed to its nearest legal ancestor. No change to this bean's scope or status.

## 2026-11-27 — χ = −6 chain thread (session_01VQDpPbyS5NspZ1YQT2xsE6, PR #9726)

Unchanged. PR #9726's new theorem starts from the same combinatorial map, so Radó plus the equivariant refinement remains the only topological input. Not attempted (Mathlib gap).



2026-11-27 (branch claude/equivariant-triangulation-2026-11-27): the combinatorial half is proved. MathlibExt/VoltageLift.lean: a dart-free action has cyclic cell stabilisers (cycle_stabilizer_isCyclic); the voltage lift liftPerm is equivariant, free on darts and edges, and its quotient is the base map. BraidKnotOctonion/A5VoltageMapChi.lean: chi_le_neg_six_of_A5_voltage_map needs only face freeness, connectedness and hyperbolicity. What remains is split into  (monodromy as voltages) and  (Radó plus combinatorial chi = analytic chi). Stays open.



Correction to the entry above: the two split-out beans are  (monodromy as voltages) and  (Radó plus combinatorial chi = analytic chi).



Correction: the split-out beans are qou-gu23 (monodromy as voltages) and qou-0nr6 (Radó plus combinatorial chi = analytic chi).
