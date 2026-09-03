---
# qou-54uf
title: 'Join proved in Lean: grade shift = xX, composing interfaces multiplies'
status: completed
type: task
priority: normal
created_at: 2026-08-29T01:33:43Z
updated_at: 2026-08-29T01:34:03Z
---

Landed on PR #5945, branch claude/gf-join-lean-2026-08-29.

File: content/quantum-observable-universe/lean/QOU/Knot/GradedGeneratingFunction.lean

Proves the step that was previously verified only at A=1..4, k=1..5:
  gf_shift      : gf s c (deg+1) = X * gf s c deg
  gf_interface  : gf s c (deg+1) + C d * gf s c deg = (X + C d) * gf s c deg
  gf_bonds      : list of bridges = (prod (X + C d)) * P
  gf_bonds_zero : all scalars zero => X^n * P

lean-direct exit 0; all five depend only on [propext, Classical.choice, Quot.sound].
Generic {R : Type*} [CommSemiring R]; no real numbers.

Does NOT prove that Hecke multiplication produces the shift -- that needs the
Hecke algebra in Lean (qou-e6db). The arrow from 'Hecke multiply' to 'shift'
is carried by JetGradePromotion at the level of permutations and lengths.
Moves no binding number; w_3 remains free.
