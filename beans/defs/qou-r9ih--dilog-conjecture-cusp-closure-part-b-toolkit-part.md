---
# qou-r9ih
title: 'Dilog conjecture: cusp closure + Part B toolkit + Part A convergence'
status: todo
type: epic
priority: normal
created_at: 2026-07-18T14:57:00Z
updated_at: 2026-10-04T15:10:00Z
parent: b9cj
---

## 2026-07-24 reconciliation

Children: brick 1 (`qou-60ga`) ✅, brick 2 (`qou-4utw`) ✅, brick 3 reflection
(`qou-er3g`) ✅ — landed on main as `LiTwo_reflection'` + `hasDerivAt_LiTwo`
(the dilog derivative Mathlib lacked) via sibling sessions; brick 4 Tauberian
(`qou-jbd5`) ⏳ OPEN.

**Cusp closure** ✅ (`LiTwo 1 = π²/6`). **Part B toolkit** ✅ (pole-subtraction
`log_neg_factor_split`; numerics in `docs/audits/2026-07-17-dilog-archimedean-
limit-partB-pole-cancellation.md`). **Dilog algebra** ✅ (special values,
reflection, duplication, integral rep, Clausen — all sorry-free on main).

The milestone's remaining scope collapses to a SINGLE open item: **Part A
Tauberian/DCT convergence** `(1−q)·log Φ_n(x;q) → Li₂(x)` for `x∈(0,1)` —
tracked in `qou-jbd5`, in-flight on `claude/dilog-litwo-neg-one-2026-07-18`.
This is also the wall the alpha-em 1/π thread reduces to. Keep milestone open
until `ArchimedeanLimit x` is inhabited off `x=0`.



## Reorganisation 2026-10-04

Now the epic for P2.DILOG under UMBRELLA: open conjectures (formal mathematics only).
