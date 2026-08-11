---
# qou-uoal
title: 'SW-7-gen: general dim H_n(q) ≤ n! (spanning, T_w basis) — Coxeter/Matsumoto infra'
status: todo
type: task
priority: normal
created_at: 2026-08-11T00:33:45Z
updated_at: 2026-08-11T00:34:47Z
parent: qou-59vq
---

Spanning half of the Iwahori–Hecke basis theorem dim H_n(q) = n! for general n: H_n(q) is spanned by {T_w : w ∈ S_n} (n! reduced words).

## Mathlib assessment (2026-08-11)
Foundations PRESENT: Mathlib.GroupTheory.Coxeter.{Basic,Length,Inversion,Matrix} — CoxeterSystem, length, IsReduced, inversions/exchange. ABSENT: Matsumoto's theorem (reduced-word independence / T_w well-definedness), any Hecke algebra, the T_w basis.

## Route (multi-day)
1. Symmetric group as CoxeterSystem (check Mathlib instance).
2. Per w ∈ S_n choose reduced word; define T_w ∈ Hecke (product of σ's).
3. Span-closure induction on length: T_s·T_w = T_{sw} (l up) or (q-q⁻¹)T_w + T_{sw} (l down) — the general form of the 12 reductions done concretely at n=3 in HeckeDim3.gen_mul_mem.
4. adjoin{σ_i}=⊤ (as HeckeDim3.adjoin_gens_eq_top) ⇒ span{T_w}=⊤ ⇒ dim ≤ n!.

The lower bound dim ≥ n! (independence) needs ALL irreps = general Hoefsmit (qou-im9l). n=3 fully done (dim=6, PR #4963); this bean is the general-n spanning generalization.
