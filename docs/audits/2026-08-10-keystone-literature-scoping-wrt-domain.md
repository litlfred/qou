# Keystone literature scoping — the WRT domain question, and a zero-citation gap

**Date:** 2026-08-10
**Audit type:** literature scoping for `conj:s5-so3-fiber-action` (the s5-so3 keystone)
**Bean:** follow-on to `qou-1nvh`; PR #4952
**Tier — UPGRADED 2026-08-10 (same day).** This doc was written at search tier.
The owner then uploaded three of the six papers (commit
[`95accb15`](https://github.com/litlfred/qou/commit/95accb153a132df290605fd2ad27930b2a47b8f9):
1106.6298, 1511.05628, 2605.15740), so **§3(b) is now READ TIER and confirmed by
direct quotation** — see §7. The rest of the doc (the reading list, the route
table) remains a plan. Items 1 (math/0605314), 4 (1411.6062) and 5 (2412.04241)
are still unread, and item 5 is still the one most likely to change the picture.

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


---

## §7 READ-TIER CONFIRMATION (2026-08-10, owner-supplied papers)

Three of the six arrived as [`95accb15`](https://github.com/litlfred/qou/commit/95accb153a132df290605fd2ad27930b2a47b8f9).
§3(b) survives contact with the sources, and the mechanism turns out to be
sharper than "native domain".

### 7.1 The domain statement, quoted

**Beliakova–Le, arXiv:1106.6298 §1** defines the Habiro ring as the
`(q;q)_k`-adic completion

    Ẑ[q] := lim←_k  Z[q] / ((q;q)_k),      (q;q)_k = ∏_{j=1..k} (1 − q^j)

and states:

> "Every element f(q) ∈ Ẑ[q] can be considered as a function whose domain is the
> set of roots of unity. Moreover, there is a natural Taylor series for f at
> every root of unity. [...] two elements f, g ∈ Ẑ[q] are the same if and only if
> their Taylor series at a root of unity coincide."

and, for the invariant itself:

> "For any integral homology 3-sphere M, Habiro constructed a unified invariant
> J_M whose evaluation at any root of unity coincides with the value of the WRT
> invariant at that root."

So §3(b) is confirmed as written.

### 7.2 The mechanism — why, not just that

An element is an infinite sum `Σ_k f_k(q)·(q;q)_k`, so `(q;q)_k` governs
convergence, and it does three different things. Measured at the canonical
50-dps `q₀` by
[`habiro_domain_substrate_anchor_probe.py`](../../computations/probes/habiro_domain_substrate_anchor_probe.py):

| k | \|(q₀;q₀)_k\| — substrate, q₀ ≈ 1.10998 | \|(1/q₀;1/q₀)_k\| — bar-conjugate ≈ 0.9009 |
|--:|--:|--:|
| 5 | 0.0033 | 0.00070 |
| 20 | 1.165×10⁴ | 3.55×10⁻⁶ |
| 30 | 1.953×10¹⁵ | 1.66×10⁻⁶ |
| 80 | **7.334×10¹⁴⁰** | 1.11×10⁻⁶ |

with `(1/q₀;1/q₀)_∞ = 1.109×10⁻⁶` (converges, nonzero), and at a primitive 5th
root of unity `|(z;z)_k| = 5.0, 7.5×10⁻⁴¹, 8.9×10⁻⁴¹` for k = 4, 5, 6 — i.e.
**exactly zero for k ≥ 5**, so the sum terminates.

Three regimes, then:

- **root of unity** — terminates. This is *why* the domain is the roots of unity;
  it is not a convention.
- **|q| < 1** — bounded, so convergence is possible (necessary, not sufficient).
- **|q| > 1, the substrate anchor** — diverges super-exponentially.

**Consequence, and it is the point of this section.** The `(q;q)_k`-adic
completion that makes roots of unity evaluable is the *same* one that makes real
`q > 1` diverge. So "continue the unified-WRT element to `q₀`" is not a harder
evaluation of a thing we have — it asks for something the object does not have.
Scope-(a) on the Habiro/unified-WRT route; it excludes no ingredient elsewhere,
and says nothing about state integrals.

### 7.3 The other two uploads keep everything at roots of unity

- **Dimofte–Garoufalidis, arXiv:1511.05628 §1**: a quantum modular form is "a
  complex valued function f on the set of complex roots of unity that comes
  equipped with a suitable formal power series expansion φ_ζ(ℏ) ∈ C[[ℏ]] at each
  complex root of unity ζ", appearing "in the asymptotics of the Kashaev
  invariant at each root of unity". Confirms the route table's middle row:
  asymptotics *near* roots of unity, not values at `|q| > 1`.
- **Lovejoy–Osburn–Störzer, arXiv:2605.15740 (2026)**: "Habiro's construction of
  the unified WRT invariant subsequently recast this result as an identity for a
  q-hypergeometric series **at roots of unity**. This motivated Hikami to prove
  analogous q-series identities involving the unified WRT invariants of certain
  **Brieskorn homology spheres**." So the newest paper covers the keystone's own
  manifold family — and still at roots of unity.

### 7.4 A lead this opens — the bar-conjugate point

`1/q₀ ≈ 0.9009` is in the convergent regime, and the framework already threads a
bar-involution `q ↔ q⁻¹` throughout (bar-even/bar-odd channels, the proved
`θ_{λ′} = θ_λ⁻¹` chirality law, the Q_β cosh/sinh split). Whether the unified-WRT
series converges at the bar-conjugate of the substrate anchor, and can be
bar-transported back, is a sharp question that nothing here answers.

**Stated as a lead, with its caveat.** Bounded `(q;q)_k` is **necessary, not
sufficient**: convergence of `Σ_k f_k·(q;q)_k` also needs the `f_k` not to grow
faster, and a Habiro element is only specified up to the completion, so a
convergent evaluation at `|q| < 1` is not automatic and is *not* implied by
anything measured above. Do not record this as a route until someone bounds the
`f_k` for a specific Σ(2,3,5) series.

### 7.5 The remaining three, also read (2026-08-10, second upload)

All six are now read. Both open questions resolve, and in opposite directions.

**2412.04241 — *The Habiro Ring of a Number Field* (Garoufalidis–Scholze–Wheeler–Zagier).
Does NOT relax the domain; it goes p-adic.** The abstract defines elements as
"collections of power series **at each complex root of unity**". The extension it
provides is explicitly p-adic: the collection "can be used to define a single
**p-adic analytic function on the disconnected domain {q ∈ C_p | |q|_p = 1}**,
which is the union of the (not all distinct) open unit discs centred at roots of
unity." And decisively for the archimedean question, on the complex side:

> "f_m(x) are formal series with **no convergence properties assumed**. In fact,
> in examples ... coming from perturbative knot invariants, the associated series
> will be **factorially divergent series over the complex numbers**, whereas at
> the same time they are always **p-adically convergent**."

So the newest and most authoritative extension **strengthens** §7.2 rather than
overturning it: the convergence it recovers is p-adic, and the complex-analytic
behaviour is factorially divergent. The substrate anchor is archimedean and real.

**1411.6062 — state integrals. The substrate anchor IS in the domain.**
Garoufalidis–Kashaev §1.1: `I_{A,B}(b) = ∫ Φ_b(x)^B e^{−Aπix²} dx` is
"an **absolutely convergent** integral ... for a complex number b with
`b² ∉ ℝ≤0`". Mapping the anchor through `q = e^{2πiτ}` with the Faddeev
convention `τ = b²`
([`state_integral_domain_substrate_anchor_probe.py`](../../computations/probes/state_integral_domain_substrate_anchor_probe.py)):

    q₀ real > 1  ⇒  τ = b² = −0.0166063414046 i   (purely imaginary)
    b² ∈ ℝ≤0 ?   No  ⇒  converges

So the route table's third row is confirmed positively: **the analytic route
reaches the substrate anchor where the Habiro route provably cannot.**

Three caveats, none of them small:
1. **Convergence is not identification.** Nothing here says a state integral
   reproduces `W_λ`.
2. **The paper's evaluation theorem does not transfer.** Its results are at
   *rational* `b² = M/N`, via Rogers + cyclic dilogarithm and finite state-sums
   at roots of unity. Our `b²` is purely imaginary, not rational — only the
   convergence statement carries over.
3. **`τ = b²` is inferred**, not quoted from the extracted text; it is the standard
   Faddeev convention and is consistent with the paper's own `b = √(M/N)`
   rational-point setup. A different normalisation moves the arithmetic.

**An observation, explicitly not a result.** The paper's headline identity is
`I_{1,2}(1) = (e^{iπ/6}/√3)·2·sinh(V/2π)` with `V = 2·Im(Li₂(e^{iπ/3})) =
2.0298832…` — verified here to be *the corpus's own* `Vol(4₁) = 2·Cl₂(π/3)` to
3.9e-31. So the CAL-2 muon-anchor volume appears in the literature inside a
**sinh**, and the framework independently carries a bar-odd `sinh` / bar-even
`cosh` split (`Q_β` is "the bar-odd sinh partner of the bar-even cosh meson scale
`m_π`"). This is at `b = 1`, *not* the substrate anchor, and `2·sinh(V/2π) =
0.6574…` is matched to nothing. Per anti-numerology discipline: a question to
carry, not a correspondence. Two objects containing `Vol(4₁)` is the expected
state of affairs when one of them is *defined* by the figure-eight knot.

**math/0605314** (foundational unified-WRT) was read for the domain statement;
1106.6298 §1 already carried it verbatim, so it adds no new constraint here.
