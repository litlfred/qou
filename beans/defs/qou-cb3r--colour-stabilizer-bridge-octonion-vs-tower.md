---
# qou-cb3r
title: 'Bridge between the two SU(3)s: octonion su3 e vs tower gl3 Jimbo colour (conj:sm-colour-stabilizer-action)'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - 8f-arch
created_at: 2026-11-15T10:40:00Z
updated_at: 2026-11-15T10:40:00Z
parent: qou-8lxd
---

Owner (relayed by coordinator session_01M5GA1LmsEf8tSMxFjMkmnn, 2026-11-15): "can we close gap -- conj:sm-colour-stabilizer-action ... no instance exists ... The two SU(3)s live side by side with no bridge between them."

Goal: an instance of ColourStabilizerActionOnSU3 e V induced by construction on the tower side, or an honest negative naming the extra choice. Trap: any iso of compact sl3 forms is a selection, not a bridge.

Work: PR (draft) on branch claude/colour-stabilizer-bridge-2026-11-15; audit docs/audits/2026-11-15-colour-stabilizer-bridge.md; Lean QOU/StandardModel/ColourBridgeObstructions.lean, QOU/IwahoriHecke/JimboClassicalLimit.lean.
Related: qou-ni4b (Hecke-side instantiation), qou-abtu (furey2016 citation), qou-qs4c.

## 2026-11-15 — q2c probe (option C) done, scope (a); A+B NOT started (stand-down)
Exact probe `computations/eightfold/quantum_g2_colour_stabilizer_probe.py`, audit §8.
- V7 = 1+3+3bar under the long-root operators of U_q(g2); colour deformed at q^3.
- At q != 1, no weight-(3a1+a2) element of U_q(n+) has a coproduct preserving 3(x)3 (at q=1 there is exactly one).
- The q-cross-product's L_e is not scalar on the 3, so it does not commute with the long-root operators; the 3/3bar sign survives.
The coordinator relayed owner "Q2 A B C explor" (A: strengthen the class with J, the Lie hom and a q=1 Ř field; B: a scoping
paragraph in authorNotes). Neither is started, because a stand-down from session_01Qmmkt6dCyH72NJwcLGW2sF arrived first. Still open.

## 2026-11-15: check D over ℚ(q) (taken over by the project thread "Map SM and eightfold way, probe option C")
Over ℚ(q), every U_q(g₂)-endomorphism of V₇⊗V₇ that preserves 3⊗3 is a scalar on it (W-preserving subspace dim 2 of 4). So no quantum-G₂ braiding restricts to Jimbo's Ř on the colour triplet at generic q. The triplet is forced by its weights. Audit §8.1. A and B are still to do.
