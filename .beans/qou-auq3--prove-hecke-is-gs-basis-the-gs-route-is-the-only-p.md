---
# qou-auq3
title: Prove hecke_is_gs_basis — the GS route is the only path from n<=4 to general n
status: todo
type: task
created_at: 2026-08-09T16:10:13Z
updated_at: 2026-08-09T16:10:13Z
---


`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean:156`:

```lean
/-- **Theorem** (Bokut & Shiao 2001, Theorem 3.5):
    The Hecke relations form a GS basis for `H_n(q)`. -/
-- Ref: [bokutchen2014] https://doi.org/10.1007/s13373-014-0054-6
axiom hecke_is_gs_basis (n : ℕ) (hp : HeckeParams) :
    IsGrobnerShirshovBasis (HeckeGen n) ℝ (heckeOrder n) (heckeRewritingSystem n hp)
```

Everything constructive around it is already there — `heckeOrder` is a `def`
(deg-lex from `AlgOps`), so are `heckeRewritingSystem`, `embedGenerator`,
`braidToAlg`, `heckeCost`. The file's own axiom-budget table lists exactly one
axiom, and this is it. Downstream, `heckeCost_well_defined` and
`threading_cost_unique` inherit it.

## Why this is the highest-value item on the Hecke roadmap

Every concrete rung — `H2`, `H3A`, `H4A` — is a hand-built or generated table at
one `n`. The scoping answer in
`docs/audits/2026-08-09-hecke-infrastructure-what-is-needed.md` is that `n = 4`
is the last level worth building that way: `H₅` is 120 basis elements, `H₁₂` is
479 001 600, and the manuscript's physics lives at `H₆`, `H₉`, `H₁₂`, `H₁₈` and
up to `H₁₂₀`.

A **proved** GS basis is the one route to general `n`. It gives normal forms and
the `n!` count for all `n` at once, and it is the constructive substitute for
Matsumoto / Coxeter word reduction, which Mathlib does not have (rev
`f897ebcf`: `GroupTheory/Coxeter/{Basic,Inversion,Length,Matrix}` exist, Hecke
algebras do not — `find Mathlib -iname "*Hecke*"` returns nothing).

With it, `QOU.Hecke.finrank_of_rank_recursion` and `isHeckeOfFullRank_succ`
(`QOU/Hecke/FullRank.lean`) close the induction: the GS normal forms give the
rung, the tower law gives `n!`.

## Why it cannot simply be imported as-is

The H₃/H₄ work is axiom-clean (`propext, Classical.choice, Quot.sound`), and
`HeckeH4AlgebraLaws` commits to that explicitly — "no axiom, no `sorry`, no
conditional class, no `native_decide`". Importing `hecke_is_gs_basis` would put
an unproved axiom underneath results that currently have none. `qou` does
`require` the UGB package (`lakefile.toml:45`), and exactly one QOU module
imports it (`QOU/PhotonThreading.lean`) — which reads as deliberate quarantine
rather than oversight.

## The work

Discharge the axiom via `UGB.GrobnerShirshov.CompositionLemma`: verify that every
composition (overlap and inclusion) of the Hecke relations is trivial modulo the
system. For type A that is the standard Bokut–Shiao argument — finitely many
overlap types coming from the braid and quadratic relations. `CompositionLemma`
is in the tree for exactly this purpose.

Cross-check available for free: the GS normal forms at `n = 3, 4` must reproduce
the 6- and 24-word bases already committed
(`QOU.Machinery.MarkovTraceOnHecke`, `HeckeH4AlgebraLaws.wordAction`), which were
computed as GB normal forms by `computations/markov/hecke_regular_nf_table.py`.
Two independent derivations of the same word list is a real check on both.
