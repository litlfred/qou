---
# qou-bhrx
title: 'F4-opt1: abstract Ocneanu cyclic-trace lemma on MarkovStabilization (light permanent closure, all-n)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-19T17:13:51Z
updated_at: 2026-07-19T17:28:19Z
---


## Progress (2026-07-19)
Delivered the level-agnostic REDUCTION (not yet the full closure):
- New QOU.Machinery.BilinearTraceCyclicity (sorry-free): cyclic_of_gram_symm over
  ANY Fintype ι — τ(B u v)=τ(B v u) for all u,v FROM Gram symmetry
  G i j = τ(B(e i)(e j)), given B bilinear + τ linear. Reusable at H3/H4/H5/....
- H4.trM_cyclic_of_gram_symm now INSTANTIATES it (dedup; ~50 lines of redundant
  Fin-24 local machinery pruned). lean-direct exit 0.
This generalizes the reduction to all-n. It does NOT discharge Gram symmetry —
the full "light permanent closure" still needs the abstract Ocneanu word-length
induction OR the character/Wedderburn decomposition (tr_M = Σ_λ w_λ χ_λ, each χ_λ
cyclic by trace_mul_comm). That is the OPEN keystone (MarkovTraceOnHecke.lean
"open keystone infra"); next step under this bean.
