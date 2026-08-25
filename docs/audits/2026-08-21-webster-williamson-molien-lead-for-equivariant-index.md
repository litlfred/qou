# Lead: Webster–Williamson give a geometric Markov trace whose weights are Molien series

**Date:** 2026-08-21
**Status:** LEAD — nothing derived, nothing wired. Four open verification items below.
**Source:** [`library/arxiv-0911.4494v2`](../../library/arxiv-0911.4494v2/) — Ben Webster,
Geordie Williamson, *The geometry of Markov traces*. Registered in the bib as
`webster-williamson-2014-markov`.
**Bean:** `qou-sf1t`
**Prompted by:** the `Z(n)` normalizer question in
[`2026-06-20-keystone-wlambda-Z-defect-n-scaling.md`](2026-06-20-keystone-wlambda-Z-defect-n-scaling.md).

## Why this is worth a look

The corpus carries an owner-gated open item: an **S¹-equivariant (Reeb-graded) index
reproducing the partition weights geometrically, with a conjugation symmetry coming from
a Hodge-★ / Poincaré duality**. That is a description of a geometrically-constructed
trace on the Hecke algebra whose character expansion is graded.

Webster–Williamson construct exactly that shape. Their main theorem, quoted from the
introduction:

> The geometrically defined trace `Tr_Γ` satisfies the following properties:
> • It satisfies a Markov condition analogous to that of the Jones–Ocneanu trace.
> • For Weyl groups, it coincides with the trace defined by Gomi.
> • Its expansion in terms of simple characters is given explicitly in terms of Molien
>   series and Lusztig's Fourier transform.

and the categorified form:

> the decomposition of `Tr_Γ` on a Kazhdan–Lusztig basis element into "almost characters"
> … is categorified by a decomposition of the `B_Δ`-equivariant intersection cohomology
> of `BwB` into summands whose mixed Poincaré series are given by Molien series.

Structurally, term by term:

| the corpus's gated item wants | §6 of Webster–Williamson supplies |
|---|---|
| an equivariant index | `B_Δ`-equivariant intersection cohomology |
| a Reeb **grading** | a bigrading by degree and weight; mixed **Poincaré** series |
| the weights reproduced geometrically | the character expansion **as Molien series** |
| Poincaré / Hodge-★ duality | equivariant formality (⇒ Hochschild homology of any Soergel bimodule is free) |

The concrete machinery, from §6: with `t* = X(T) ⊗ ℂ` and

```text
  E = Sym•(t*) ⊗ ∧•t*        (a W-module, canonically H*_{T_Δ}(T))
```

the Molien series of an irreducible `ν ∈ Ŵ` is

```text
  M_ν(q, t) = Σ_{i,j} q^{i/2} · t^{j-i} · dim Hom_W(V_ν, E)_{i,j}
```

with **Proposition 12:** `H•_{G_Δ}(V_ν) = Hom_W(V_ν, E)`.

## Why the Molien shape bears on the `Z(n)` question specifically

`E` is a symmetric algebra tensored with an exterior algebra, so its Molien/Poincaré
series is of the form `∏(1 + t·q^{…}) / ∏(1 − q^{d_i})` — a ratio of cyclotomic-type
factors over the degrees of `W`. That is the same family of denominators `[n]_q!` belongs
to. If the geometric weights are natively Molien series, then the "right" normalizer on
the geometric side is a Poincaré/Molien series rather than a bare `[n]_q!`, which would
explain the `Σ_λ w_λ(q) ≠ 1` mismatch **structurally** instead of as a defect.

Note this is consistent with — not a reopening of — the owner ruling of 2026-08-16
(`notation/notation-collisions.md`), which already fixes `Σ w_λ(q) ≠ 1` as by-design and
assigns the probability-measure role to `y_λ` and `w_λ(1)`. The question this lead is
aimed at is the *narrow* survivor: what the geometric-realization target should be.

## Open verification items — none of these are established here

1. **Is `Tr_Γ` the Jones–Ocneanu trace?** The paper's abstract calls the result a
   geometric interpretation *of* the Jones–Ocneanu trace, while the introduction says
   `Tr_Γ` satisfies a Markov condition *"analogous to"* it and *"coincides with the trace
   defined by Gomi"*. Those are different assertions. The corpus's `tr_M` is
   Jones–Ocneanu, so this identification is load-bearing and is **not** settled by
   reading the introduction.
2. **Bigraded `(q, t)` versus one real `q₀`.** `M_ν(q, t)` carries two gradings (degree
   and weight). The corpus evaluates at a single real substrate `q₀ ≈ 1.10998`. Which
   specialization of `(q, t)` — if any — reproduces the corpus's weights is exactly the
   work, and a two-variable object matching a one-variable one is the sort of claim that
   needs the specialization exhibited, not asserted.
3. **General type versus type A.** Webster–Williamson work with `K^{B×B}(G)` in general
   type. The corpus is type A at a real anchor. They note their type-A case is
   essentially equivalent to Khovanov–Rozansky triply-graded homology categorifying
   HOMFLYPT, and that equivariant formality was proved in type A by Rasmussen — so type A
   is the best-covered case, but the descent still has to be written down.
4. **Which weight family do the Molien weights land on?** `y_λ` (Jones–Markov),
   `w_λ(q)` (q-deformed Wedderburn) and `w_λ(1)` (classical Plancherel) are distinct at
   `q ≠ 1` per the register, and the Wenzl-bridge identity `y_λ = w_λ(q)` holds only on
   the self-conjugate stratum (`κ_λ = Σ_x c(x) = 0`). A geometric weight has to be
   matched against a *named* family, not against "the weights".

## Citation status (corpus-grepped 2026-08-21)

- **Registered** in `content/schema/references.ts` as `webster-williamson-2014-markov`,
  with `docId: arxiv-0911.4494v2` and the library dir wired.
- **Cited** by exactly one content block,
  [`mass-theory/hecke-markov-interpretation`](../../content/quantum-observable-universe/mass-theory/hecke-markov-interpretation.md)
  — but as a bare `cites:` entry; that block's prose never discusses the paper.
- **"Molien" appears nowhere** in `content/`, `docs/` or `computations/`. The mechanism
  above is unmined.
- Listed in [`2026-06-08-uploaded-paper-results-ingestion-backlog.md`](../workplans/2026-06-08-uploaded-paper-results-ingestion-backlog.md)
  as `0911.4494 | Webster–Williamson (geometry of Markov traces) | yes | Markov (cite)`.

So the paper was ingested and cited, and its *content* was never pulled through. This
note is the pull-through proposal, not the pull-through.

## What this note does NOT claim

No derivation, no identification, no wiring. It does not claim `Tr_Γ = tr_M`, does not
claim the Molien series reproduces `w_λ(q)` or `y_λ`, and does not reopen the 2026-08-16
ruling. It claims only that a paper already in the library constructs an object of the
shape the gated item describes, and names the four things someone would have to prove to
connect them.

Read of the source is partial: introduction and §6 (Character sheaves and Molien series);
the proofs were not worked through.
