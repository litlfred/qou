# Keystone literature scoping — the WRT domain question, and a zero-citation gap

**Date:** 2026-08-10
**Audit type:** literature scoping for `conj:s5-so3-fiber-action` (the s5-so3 keystone)
**Bean:** follow-on to `qou-1nvh`; PR #4952
**Tier — READ THIS FIRST:** everything below is at **search-result tier**, not
read-tier. I searched, I did not read the papers. No claim here is a corpus
finding, nothing is refuted, and nothing should be cited as established until
someone reads the sources. What this doc is for is *aiming* that reading.

---

## §1 Why literature at all

The keystone's single open object, per
[`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) §Current state and the
2026-07-12 frontier-sharpening banner, is now pinned to:

> the **archimedean continuation** of the colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel
> q-series from the fibre root-of-unity to the substrate `q₀ ≈ 1.10998` (real,
> `> 1`, growth regime), reproducing `W_λ = d_q(λ)²/[n]_q!`.

That is a question about *where a quantum invariant is defined*, which is a
mathematical-literature question before it is a framework question. The ledger
also says explicitly: do **not** re-chase framing-cancellation as new ground, it
is the archimedean-continuation restatement. So the productive move is to find
out what the literature says about evaluating these invariants off the roots of
unity, rather than to run another probe.

## §2 The citation gap that prompted this

Counting matches in [`references.ts`](../../content/schema/references.ts):

| term | hits |
|---|---:|
| garoufalidis | 48 |
| habiro | 29 |
| zagier | 24 |
| woronowicz | 12 |
| koelink | 12 |
| hahn | 12 |
| exton | 8 |
| state integral | 7 |
| wrt | 4 |
| brieskorn | 4 |
| seifert | 3 |
| witten-reshetikhin | 3 |
| **beliakova** | **0** |

So the corpus is deep on the q-Bessel / `E_q(2)` side (Koelink, Woronowicz,
Hahn–Exton) and on quantum modularity (Garoufalidis, Zagier, Habiro), and thin
exactly where the open object lives — the **unified WRT invariants of Seifert /
Brieskorn spheres**. Beliakova at zero is the sharpest signal: that is a principal
author of the unified-WRT programme, and Σ(2,3,5) is a Brieskorn sphere.

## §3 What the search turned up (search tier)

Two things, and the second is the useful one.

**(a) The unified-WRT programme covers the manifolds we care about.** Habiro
initiated generating functions for WRT invariants ("unified WRT invariants");
Beliakova, Le, Blanchet and Buehler extended the construction to broader classes
of 3-manifolds, with applications computed *for Seifert fibered spaces* and with
Brieskorn spheres `Σ(p₁,p₂,p₃)` studied in this context. So there is an existing,
named construction aimed at exactly the manifold family the keystone needs.

**(b) — the load-bearing one — the native domain of these invariants is the
roots of unity.** Two independent search summaries state it:

> "Every element in the Habiro ring can be considered as a function whose domain
> is the set of roots of unity, with a natural Taylor series at every root of
> unity, and two elements are the same if and only if their Taylor series at a
> root of unity coincide."

> "quantum invariants [are] a kind of 'analytic function' defined on the set of
> roots of unity."

If that is right as stated, it bears directly on the keystone: a unified-WRT /
Habiro-ring element is **natively a function on roots of unity**, and the
substrate anchor `q₀ ≈ 1.10998` is real and `> 1` — not a root of unity, and not
in the closure of that domain in any way the ring itself supplies. The
archimedean continuation the ledger names is therefore not a gap in *our*
bookkeeping that a better construction closes; it is a request to leave the
object's native domain.

**Consequence for route selection, if (b) holds.** The two candidate literatures
answer different questions:

| route | what it gives | reaches real `q₀ > 1`? |
|---|---|---|
| Habiro ring / unified WRT | an element evaluable **at** each root of unity | not natively — that is the whole point of the domain statement |
| quantum modularity (Zagier QMC, Garoufalidis–Zagier) | asymptotic series **at each** root of unity | describes behaviour *near* roots of unity, not at `\|q\|>1` |
| state integrals (Andersen–Kashaev, Garoufalidis–Kashaev) | genuine analytic functions of `q`, evaluated at rational points via quasi-periodicity of Faddeev's `Φ_q` | this is the one that is analytic in `q` by construction |

That ordering is a **hypothesis to check by reading**, not a result. But it is
actionable, and it is consistent with something the corpus already carries: the
cheat sheet's §4 already sorts `Φ_q` (Faddeev / compact q-dilog) against `Li₂^q`
(Rogers), and Faddeev's `Φ_q` is precisely the state-integral kernel. If the
state-integral route is the one that is analytic in `q`, the framework is already
holding the right object and the keystone question becomes "which state integral",
not "how to continue a Habiro element".

## §4 Specific reading list, in priority order

1. **[math/0605314](https://arxiv.org/abs/math/0605314)** — *A unified
   Witten–Reshetikhin–Turaev invariant for integral homology spheres.* The
   foundational unified-WRT paper. Read for the precise domain statement in §3(b)
   — that is the claim everything above turns on, and it must be verified from the
   source, not from a search summary.
2. **[1106.6298](https://arxiv.org/abs/1106.6298)** — *On the unification of
   quantum 3-manifold invariants.* The survey; fastest route to whether Σ(2,3,5)
   specifically is covered and in what form.
3. **[1511.05628](https://arxiv.org/abs/1511.05628)** — *Quantum modularity and
   complex Chern–Simons theory* (Garoufalidis–Zagier). Read to confirm or kill the
   middle row of the table: does quantum modularity say anything at `|q| > 1`, or
   only asymptotically at roots of unity?
4. **[1411.6062](https://arxiv.org/abs/1411.6062)** — *Evaluation of state
   integrals at rational points* (Garoufalidis–Kashaev). The analyticity route.
   Read for what the domain of a state integral actually is, and whether real
   `q > 1` is inside it.
5. **[2412.04241](https://arxiv.org/abs/2412.04241)** — *The Habiro ring of a
   number field* (Dec 2024). Recent, and the obvious place to look for whether the
   root-of-unity domain restriction has since been relaxed. If any single paper
   overturns §3(b), it is most likely this one.
6. **[2605.15740](https://arxiv.org/abs/2605.15740)** — *Bailey pairs, Eichler
   integrals and unified WRT invariants* (2026). Newest of the set; check whether
   it supersedes 1 and 2.

Two more that came up and are probably peripheral to the keystone but relevant to
the corpus's Σ(2,3,5) interest:
[2110.10958](https://arxiv.org/pdf/2110.10958) (WRT, homological blocks and
quantum modular forms for plumbing graphs) and
[1503.03549](https://arxiv.org/pdf/1503.03549) (unified quantum invariants for
integral homology spheres, general simple Lie algebras).

## §5 What must NOT be concluded from this doc

Per AGENTS.md §"Before declaring refuted": nothing here is a refutation. In
particular:

- **Do not** record "the Habiro route is dead". §3(b) is a search-summary
  paraphrase of a domain statement; it needs reading item 1 to become a claim, and
  item 5 could have relaxed it since.
- **Do not** treat the route table in §3 as a corpus result. It is a reading plan.
- **Do not** add any of these to `references.ts` on the strength of this doc. Cite
  on read, per the repo's bibliography discipline.

What this doc *does* establish, and the only thing it does: the corpus has a
zero-citation gap on the unified-WRT literature that is aimed squarely at the
keystone's manifold family, and there is a specific, ordered way to close it.

## §6 Tooling note for the next agent

`mcp__paper-search-mcp__search_arxiv` returned an **empty result set for every
query in this sandbox, including the trivial control query "knot theory"**. That
is a broken/blocked tool, not a null result — do not read its silence as "no such
literature". `WebSearch` with `allowed_domains: ["arxiv.org"]` worked and produced
everything above.
