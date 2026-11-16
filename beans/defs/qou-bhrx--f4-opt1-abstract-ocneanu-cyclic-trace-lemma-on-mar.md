---
# qou-bhrx
title: 'F4-opt1: abstract Ocneanu cyclic-trace lemma on MarkovStabilization (light permanent closure, all-n)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T17:13:51Z
updated_at: 2026-11-16T19:07:00Z
parent: qou-rtxm
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


## Progress note is superseded for H₄ (verified 2026-08-22, by another session)

The 2026-07-19 note above ends: *"the full 'light permanent closure' still needs
the abstract Ocneanu word-length induction OR the character/Wedderburn
decomposition ... That is the OPEN keystone ... next step under this bean."*

**For `n = 4` that is done, by the second of the two routes named.** Recording
it here because this bean is still `in-progress` and its note is the thing other
agents read — I wrote a dependency claim into `qou-9ttb` off this note without
checking the corpus, which is the cost. Evidence:

- `QOU.Machinery.MarkovTraceH4` — `trM_cyclic` at `n = 4`, off `gram_symm`'s
  576 computed entries, reduced through the `cyclic_of_gram_symm` this bean
  delivered. **Unconditional.**
- `QOU.Machinery.HeckeH4RepDecomp` — the Wedderburn/character route as
  `trM4_gram_symm_of_markov_basis`, **conditional** on `hbasis` (24 basis-level
  Markov identities), which that file states explicitly and assigns to
  `qou-x64l` step 4.
- Zero real `sorry` across `MarkovTraceH4`, `H4Cyclicity`, `H4GeneratorAction`,
  `HeckeH4RepDecomp`, `BilinearTraceRepBasis`, `BilinearTraceCyclicity`.
- The H₄ NF table this needed exists:
  `computations/markov/hecke-regular-nf-h4.witness.json`, GB-NF generated
  (`qou-1jrr`), `Fin 24` = 4! normal forms.

**Not closing this bean** — it is scoped "all-n", and general `n` is not done;
only H₃ and H₄ are. Left `in-progress` for its owner. If the intent was H₄
closure, it is closeable on the evidence above.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-22 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (2026-11-16 — PR #8160)
- **PR:** [`litlfred/qou#8160`](https://github.com/litlfred/qou/pull/8160) (`c0fb591249c67f13f6a77b40075589852babb011`)
- **Resolution:**
  - Extended `folio/quantum-observable-universe/lean/QOU/Machinery/BilinearTraceRepBasis.lean` (`0` `sorry`, `0` self-assuming audit hits; leaves `MarkovTraceTowerStabilization.lean` untouched) with:
    1. `cyclic_of_rep_decomp_of_basis`: chains `gram_symm_of_rep_decomp_of_basis` directly into `cyclic_of_gram_symm`, providing the all-$n$ (`[Fintype ι] [DecidableEq ι]`) closure from basis-level character decomposition $\tau(e_i) = \sum_{\lambda \in s} w_\lambda \operatorname{tr}(\rho_\lambda(e_i))$ to full trace cyclicity $\tau(B(u, v)) = \tau(B(v, u))$.
    2. `ocneanu_stabilization_cyclic`: proves the abstract Ocneanu single-generator stabilization cyclicity step $\tau_{n+1}(\iota(u) g \iota(v)) = \tau_{n+1}(\iota(v) g \iota(u))$ from $\tau_{n+1}(\iota(x) g \iota(y)) = z \tau_n(xy)$ and level-$n$ cyclicity $\tau_n(uv) = \tau_n(vu)$.
  - Status kept at `in-progress` pending PR #8160 merge and owner verification.
