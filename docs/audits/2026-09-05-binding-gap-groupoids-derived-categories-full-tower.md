# Groupoids and derived categories on the full mass tower: what they could do for the binding gap, what the corpus already holds, and what to download

**Date:** 2026-09-05 · **Branch:** `claude/binding-gap-categorical-research-cem5tp`
**Beans:** `qou-2akx` (session), `qou-onte` (this document), `qou-3pck` (literature request)
**Scope:** research survey + attack-route analysis. **Nothing is derived, nothing is refuted,
nothing is wired, no number moves.** Every "would" below is a proposal; every "is" is cited to a
file. Written for the owner's decision on which routes and which literature to pursue.
**Method:** corpus-grep paths 1–6 run by hand (path 0 `corpus_search` unavailable — the
`paper-assistant` MCP server failed to connect; all absences below are therefore *lexical*);
library inventory over both the `sections/` and `ocr/` tiers; external search with arXiv ids
confirmed from listing pages only (direct `arxiv.org` fetch is proxy-blocked — see §9).

---

## 0. The claim, flatly

1. **The binding gap is, as of this morning's landings, a *shape* gap of 22.5 % (p5–p95), not a
   scale gap (0.99 %), on top of a law the framework derives with zero fitted constants**
   (`B = E₀·log(tr_M(β_free)/tr_M(β_atom))`,
   [`2026-09-05-binding-law-arc-synthesis.md`](2026-09-05-binding-law-arc-synthesis.md) §6). The
   missing shape splits into four named pieces, of which three are already *structurally located*
   by sorry-free Lean: surface (supplied by any bounded-degree packing's boundary deficit —
   `QOU.Mass.CoordinationSurfaceDeficit`), Coulomb (forbidden to *every* bounded-degree bond graph —
   `QOU.Hecke.BoundedDegreeCoulomb`), symmetry sign (locked by AM–GM —
   `QOU.Hecke.SymmetrySignAmGm`). The fourth — the **irreducibly many-body term**, measured as the
   connected 3-body cumulant `b₃ = +1.4262 MeV` against a model value of exactly `0` — is the one
   with no located source, and it is the one this document is about.

2. **The reason the model's `b₃` is `0` is not an accident of the bond graph. It is a shadow of
   semisimplicity.** The corpus proves `b₃ = 0` follows from pair-locality
   (`QOU.Mass.CrossingModelPairLocality.b3_eq_zero_of_pairLocal`) and separately records that
   `HH^k(H_n(q), H_n(q)) = 0` for `k ≥ 1` at generic `q`
   ([`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md),
   Whitehead's lemma). Vanishing higher Hochschild cohomology is exactly the statement that the
   algebra admits **no non-trivial higher operations** (it is intrinsically formal as an
   `A_∞`-algebra). A quantity built from a trace on such an algebra has nowhere to store a genuinely
   3-body datum *except* in the word's topology. §2 states this as a conjecture to prove, not a
   theorem — the bridge from "formal" to "pair-local" is the thing to formalise first.

3. **Therefore: groupoid and derived-category infrastructure is not a decoration here. It is the
   only class of machinery that breaks semisimplicity without breaking the framework** — by
   categorifying the trace (Hochschild homology of the Hecke *category*, where the higher degrees
   are non-zero and are exactly what `tr_M` forgets), by integralising it (the tower over
   `ℤ[q^{±1}]` / the Habiro ring / the affine Hecke algebra, which are *not* semisimple), or by
   groupoidifying it (spans of flag groupoids, where `H_n(q)` is a *counting* object and a
   many-body term is a class on a configuration groupoid rather than a per-block weight). This is
   the mathematical content of the owner's 2026-09-03 ruling *"use the full tower even though what is
   observable is only order zero"*: order zero **is** the semisimple fibre, and the tower is where the
   higher degrees live.

4. **Yekutieli is not exhausted — but the unexhausted part is not where the corpus has been
   looking.** At the start of this session only *one* Yekutieli work was held (the
   surface-integration book, `arxiv-1007.1250v4`); the gerbes paper (`yekutieli2010`) that **148
   corpus files cite by theorem number** was *not held*. **The owner uploaded it during the session
   (commit `ad60e3f2`, with two more: *Combinatorial Descent Data for Gerbes* and *An Averaging
   Process for Unipotent Group Actions*), and all three are ingested on this branch** —
   `library/arxiv-0801.0083v4`, `library/arxiv-1109.1919v3`, `library/arxiv-math-0505170v2`,
   greppable, with `references.ts` joins. **First check against the held text: the theorem numbers
   the corpus cites — `Thm 1.7`, `Thm 3.4`, `Thm 4.5` — do not exist in the paper** (its numbered
   theorems are 3.13, 4.6, 4.17, 5.11, 6.10); the obstruction results the corpus means are
   Thm 4.6 (lifting isomorphisms, `cl¹`) and Thm 4.17 (lifting objects, `cl²`). §9 records the
   defect; the 148 files are not touched here. Of the held book, the corpus uses §§3–4 and §6 (kites, Riemann products,
   2-dim Stokes) and has **zero hits** on its main new result — Thm 8.6.6, the 3-dimensional
   non-abelian Stokes theorem with its "inert" 3-curvature (a bulk-3-form ↔ boundary-2-holonomy
   identity, which is the *shape* of a volume↔surface exchange), on Thm 6.3.1 (the fundamental
   relation `Ψ(g) = Ad_H(h)`), on Thm 7.5.1 (square puzzles: free-group relations transport verbatim
   to holonomy relations), or on Conjecture 9.5.2 (MI as a bijection onto descent data of Deligne
   groupoids — the very subject of the corpus's own `lifting-and-descent` chapter). §4 has the table.

5. **Recommendation (judgement, not finding):** run the two cheap *prunes* in §7 first — they are
   formalize-first statements that decide whether the derived route can matter at all — then
   acquire the six A-priority papers in §8, then build route A (categorified Markov trace) with route
   E (factorization homology) as its theoretical frame. Do **not** start with the Yekutieli 3-dim
   Stokes route: it stacks on Step 2 of the canonical chain, which the corpus downgraded on
   2026-08-25 to a factorisation identity with no geometry behind it. The default — do nothing — is
   safe: nothing here changes any production number.

---

## 1. Where the binding gap is, precisely (state on `main` at `4946c6a4e4`)

Everything in this section is corpus fact with a file behind it; nothing is new.

### 1.1 The law and its residual

The refuted law `B = Q_β·Δtr` was replaced by the log law, and the replacement is forced: `tr_M`
is multiplicative along the chain and binding is extensive, and `log` is the unique map carrying
one to the other ([synthesis §3](2026-09-05-binding-law-arc-synthesis.md)). The law reads

```
B = E₀ · log( tr_M(β_free) / tr_M(β_atom) ) = E₀ × (number of Markov reduction steps)
```

with `b_pp = z` a derived identity (one p–p bond is exactly one Markov reduction) and
`E₀ = m_e/(q(q−1))` derived from constants that exist anyway. Residual after the 2026-09-05
brane-tower ruling: **scale freedom 0.99 %, shape residual 22.5 %** (p5–p95 over 2548 AME2020
nuclides). The law is an *upper bound* on 2547 of 2548 nuclides; the one exception is ⁴He.

### 1.2 The four missing pieces and where each stands

| piece | status | Lean / audit |
|---|---|---|
| surface `A^{2/3}` | **supplied** by any bounded-degree packing's boundary deficit; `a_S/a_V = c(k−k′)/k`, `ε` and `k` cancel; the *magnitude* test is generic | `QOU.Mass.CoordinationSurfaceDeficit` (6 decls), [`2026-09-05-coordination-surface-deficit.md`](2026-09-05-coordination-surface-deficit.md) |
| Coulomb `Z(Z−1)` | **forbidden** to every bounded-degree bond graph (degree-sum formula: pair share ≤ `d/(n−1)`); the only door is a `Z`-dependent per-bond energy, a different *form* of law | `QOU.Hecke.BoundedDegreeCoulomb`, bean `qou-556v` |
| symmetry sign | **locked**: a bond sum wants the geometric mean, the construction delivers the arithmetic one; `AM − GM = h²/(2[2]_q)`; a repair must move the convex weight `w` below `1/(q²+1)` | `QOU.Hecke.SymmetrySignAmGm`, bean `qou-i01a` |
| **irreducibly many-body** | **open**: measured `b₃ = +1.4262 MeV`; model `0`; pair-local ⇒ `b₃ = 0` is proved, so the measurement *refutes pair-locality* of the carrier | `QOU.Mass.CrossingModelPairLocality`, `QOU.MassTheory.AmeBindingNotPairwise`, bean `qou-brng` |

Two further sorry-free constraints box the fourth piece in:

- **Intensive cannot become extensive.** No per-block (per-partition) weight converts an intensive
  quantity into an extensive one; the pairwise cap `ρ_A ≤ C(A,2)` is proved
  (`QOU.MassTheory.exchangeDet_pow_two_le_four`). Complete-graph coordination is excluded by
  saturation (`QOU.Mass.CoordinationSaturation`), the linear chain by arrangement-dependence
  (`QOU.MassTheory.ChainBondOrderDependence`). So the missing object is *not* a new `λ`-indexed
  number.
- **The multiplicative cumulant route has the wrong sign.** For any multiplicative assembly
  `W = 1 − ∏ f_ij` with positive bond factors, `b₃ ≤ 3·f_pn − 2`, so a positive 3-body cumulant
  needs `f_pn > 2/3`, independent of the edge set (`QOU.MassTheory.MayerThreeBodySign`). Deriving the
  bond set cannot repair this.

### 1.3 One positive signal already inside `tr_M`, and what it tells us

The Markov trace **is not bond-multiplicative at `n = 4`**: the interleaved word `s₀s₁s₀s₂s₁` and the
sequential `s₀²s₁²s₂` differ by exactly `z(z² − hz − 1)`, and `z² − hz − 1 = −(q⁴+q²+1)/q² · y_{(2,1)}`
is the two-row Wedderburn weight ([`2026-09-03-markov-trace-not-bond-multiplicative-n4.md`](2026-09-03-markov-trace-not-bond-multiplicative-n4.md),
bean `qou-kru4`). The interleaved trace is *smaller*, i.e. interleaving carries **extra binding**,
the direction the collective term needs.

This matters for the diagnosis in §2, so it is worth being exact about what it is and is not. It is
a non-pair-local contribution *at degree zero*, sourced from the **topology of the word** (which
crossings interleave), not from any higher operation of the algebra. The production chain word is
sequential, so it never sees it. So there are two candidate sources of many-body structure and the
corpus has found the first:

| source | lives in | seen by `tr_M`? | corpus status |
|---|---|---|---|
| **word topology** (interleaving, braid-group structure of the carrier) | degree 0 of the trace | yes | scope-(a) positive at `n = 4`; not wired; the carrier's word is the open input |
| **higher structure** (Hochschild degree ≥ 1, higher `A_∞` operations, descent degree ≥ 2) | above degree 0 | **no** — `tr_M` is the Euler characteristic | absent: `HH^{≥1} = 0` at generic `q` |

The first is a groupoid question in disguise (the braid group is `π₁` of a configuration space; an
interleaved word is a path that is not a concatenation of pairwise paths). The second is the
derived question. Both are inside the owner's "full tower".

### 1.4 The ruling that frames all of this

Owner, 2026-09-03: *"The QOU should be on the full tower in the derivations … even though what is
observable is only order zero,"* confirmed to mean **both** all `n` of the Hecke tower **and** all
orders in `q` ([`2026-09-03-sm-26-term-status.md` §10](2026-09-03-sm-26-term-status.md)). The
decision paper [`2026-09-04-full-tower-reposing-options.md`](2026-09-04-full-tower-reposing-options.md)
already established that *"climb to higher `n` on the same fibre"* is blocked by the row cap and
that *"sum over all partitions"* is already an identity. What that paper did not consider — because
it was about the SM parameters — is the reading this document takes: **the full tower is the
non-semisimple object whose generic fibre is `H_n(q₀)`**, and "order zero" is the fibre. The
corpus wrote this reading down itself, in a different context, before the ruling existed:

> *QOU's defining move is … evaluate at a single generic `q₀` where the shared tower collapses to
> one finite, fixed Wedderburn fibre `H_n(q₀) ≅ ⊕ M_{d_λ}`, then realize archimedean-ly. KS keeps
> the whole nerve because it needs the global data.*
> — [`2026-06-04-kontsevich-soibelman-0811.2435-qou-comparison.md` §15](2026-06-04-kontsevich-soibelman-0811.2435-qou-comparison.md)

The ruling reverses that trade. This document is about what the un-collapsed object has that the
fibre does not.

---

## 2. The structural diagnosis: semisimplicity ⇒ formality ⇒ nowhere to put a 3-body term

### 2.1 What is proved, what is standard, what is conjectural

**Proved / recorded in the corpus.**

- `HH^k(H_n(R,q), H_n(R,q)) = 0` for `k ≥ 1` when `H_n` is semisimple — Whitehead's lemma
  ([`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md)).
  Semisimplicity holds at generic `q`, in particular at `q₀`, since `[n]_q! ≠ 0` there.
- Pair-locality ⇒ `b₃ = 0` (`CrossingModelPairLocality`), and the measured `b₃ ≠ 0` ⇒ the carrier
  is not pair-local (`not_pairLocal_of_b3_ne_zero`).
- The Markov trace is a cyclic 0-cocycle on the Hochschild complex
  ([`gs-graded-markov-trace-existence.md`](../../content/quantum-observable-universe/mass-theory/gs-graded-markov-trace-existence.md),
  "Categorical statement").
- The corpus's own 2026-08-25 reading of the collapse: *"if the collapse holds, it is the first
  candidate proved invariant for a scope-(b) exclusion of 'look harder inside `H_n(q)`'"*
  ([`2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md`](2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md)).
  That audit also found the Lean carrier `spectral_sequence_collapses_to_centre` proves only
  idempotence and never uses its `[WhiteheadHH]` instance — so the collapse is *asserted*, not
  formalised. §7 makes closing that the first prune.

**Standard mathematics (citable, not in the corpus).**

- `HH^2(A,A) = 0` ⇒ `A` has no non-trivial first-order deformations; `HH^{≥2}(A,A) = 0` ⇒ `A` is
  *intrinsically formal*: every `A_∞`-structure on `A` with `m₁ = 0, m₂ = ` the product is
  `A_∞`-quasi-isomorphic to `A` with all `m_k = 0` for `k ≥ 3` (Kadeishvili; the obstruction to
  killing `m_k` lies in `HH^{k}` with a degree shift). A semisimple algebra over a field of
  characteristic 0 is intrinsically formal. **This is the precise sense in which the Hecke fibre has
  "no higher operations."**
- `HH_0(A) = A/[A,A]` is the universal receiver of traces; for a semisimple `A` it is spanned by
  the primitive central idempotents, i.e. by `{e_λ}` — which is exactly why the corpus's every trace
  is `Σ_λ y_λ χ_λ`. The higher `HH_k(A)` of a semisimple algebra vanish. **So at the fibre, the whole
  Hochschild complex is the Wedderburn decomposition and nothing else.**

**Conjectural — the bridge, stated so it can be proved or refuted (the first formalize-first item).**

> **(F1)** Let `A` be a semisimple algebra with a Markov trace `tr`, and let an assembly of `A`
> components be modelled by a braid word obtained by *sequential* juxtaposition of pairwise
> interface words (the production chain's construction). Then the functional `log tr(β_atom)` is
> pair-local in the sense of `CrossingModelPairLocality.PairLocal`, hence `b₃ = 0`.

This is the claim the model's `b₃ = 0` *would follow from*, and the `n = 4` interleaving cross term
of §1.3 is exactly a witness of what happens when the word is *not* sequential. F1 is not deep —
it is a bookkeeping statement about which words are products — and that is the point: proving it
in Lean would settle that the model's `b₃ = 0` is forced by *two* things (semisimple trace, sequential
word), so that breaking either is necessary, and would fix which of the two routes in §1.3 each
attack below is actually on.

### 2.2 Why the six previous negatives are consistent with this diagnosis

The six closure ansätze that failed on the deuteron (Frobenius co-Casimir, Demazure fibre,
LP-Plancherel, LP-Frobenius, crystal graph, augmented Markov — AGENTS.md §Δ_λ gate) were all
per-block weights; the intensive/extensive wall excludes all per-block weights; and per-block
weights are precisely the elements of `HH_0` of the semisimple fibre. The Mayer cumulant has the
wrong sign for any positive multiplicative assembly. The complete graph and the chain are both
pair-local edge sets. **Every negative on this arc is a negative about degree zero of a semisimple
object.** None of them is evidence about the tower, which is precisely what the owner's ruling says
(*"the residual of an order-zero-only construction is not evidence about the tower"*).

### 2.3 What breaks semisimplicity without breaking the framework

There are exactly three moves, and they are the three route families of §5:

| move | object | why it is not semisimple | what it costs the framework |
|---|---|---|---|
| **categorify** | Hecke category (Soergel bimodules); Hochschild homology `HH_*(SBim)`; Rouquier complexes of braids | `HH_*` of the *category* is huge (it is HOMFLY-PT homology); its Euler characteristic is `tr_M` | nothing at order zero — `tr_M` is recovered exactly as `χ`; new: two extra gradings |
| **integralise** | `H_n` over `ℤ[q^{±1}]`; over the Habiro ring; the affine Hecke algebra `H_n^{aff} ⊃ H_n` | not semisimple over the ring (cellular, Graham–Lehrer); `H_n^{aff}` infinite-dimensional with `HH_* ≠ 0` (Solleveld, **held**) | nothing at order zero — specialise to `q₀`; new: all orders in `q`, the Jucys–Murphy lattice |
| **groupoidify** | `H_n(q)` as spans of flag groupoids over `𝔽_q` (Baez–Hoffnung–Walker); groupoid cardinality | `H_n(q)` becomes a *counting* object; a trace is a cardinality; a many-body term is a class on a configuration groupoid | the construction needs `q` a prime power — usable only as *polynomial identities in `q`*, then evaluated at `q₀` (legitimate: a Laurent-polynomial identity holding at infinitely many prime powers holds identically) |

The corpus's own `lifting-and-descent` chapter is a fourth move already made — **descend** (Čech
nerve of a gerbe; cosimplicial crossed groupoid) — whose degree-`≥2` descent data is likewise
outside the fibre. §4 treats it with Yekutieli.

---

## 3. What the corpus already holds (so nothing below is re-derived)

### 3.1 Content blocks and audits (paths 1–4, 6)

| what | where | status | relevance |
|---|---|---|---|
| **Yekutieli lifting triple / cosimplicial crossed groupoid** — `[n] ↦ 𝔊_n` from Δ to gerbes; cofaces = jet prolongation, codegeneracies = descent; crossed structure = `SU_q(2)` conjugation | [`lifting-and-descent/cosimplicial-crossed-groupoid.md`](../../content/quantum-observable-universe/lifting-and-descent/cosimplicial-crossed-groupoid.md), `yekutieli-triple.md`, 36 `.lean` siblings (2 files carry `sorry`: `descent-lemma`, `motivic-substrate`) | proposition; consumed by 4 blocks outside the chapter incl. `mass-theory/volume-tower-decomposition`, `archimedean-functor-uniqueness` | the corpus's *own* higher-groupoid object; degree-`≥2` descent data is the natural home of an irreducibly 3-body datum (§4.3) |
| **Markov moves = cosimplicial directions**: conjugation = horizontal (within a level), stabilisation = vertical (jet prolongation) | [`braids-and-knots/markov-moves-brane-tower.md`](../../content/quantum-observable-universe/braids-and-knots/markov-moves-brane-tower.md) | remark, no Lean | this is the informal statement that `tr_M` is `HH_0` of a simplicial object; the derived route is literally "take its higher homology" |
| `HH^{≥1}(H_n) = 0`; collapse at `E_1`; centre = Wedderburn | [`mass-theory/spectral-sequence-collapse.md`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md) + proof | proposition; Lean carrier vacuous (see 2026-08-25) | the obstruction of §2 |
| Markov trace as **cyclic 0-cocycle** on the Hochschild complex | [`mass-theory/gs-graded-markov-trace-existence.md`](../../content/quantum-observable-universe/mass-theory/gs-graded-markov-trace-existence.md) | theorem-conjectural; Lean class field | names the degree-0 object; higher cyclic cocycles are the obvious extension nobody has written |
| Hochschild–Kummer–gerbe comparison `HH²(𝒰_q, Ad) → H²(𝒮, 𝔾_m)`; classical-limit obstruction as a **Hochschild tower** | [`lifting-and-descent/hochschild-kummer-connection.md`](../../content/quantum-observable-universe/lifting-and-descent/hochschild-kummer-connection.md), [`stochastic-mechanics/classical-limit-obstruction-properties.md`](../../content/quantum-observable-universe/stochastic-mechanics/classical-limit-obstruction-properties.md) | remarks | the corpus already identifies deformation (Hochschild) and gerbe (Yekutieli) obstructions as one class — the bridge §5-D would use |
| The extensive term as a **body-order series on the jet filtration**, proved extensive; magnitude open | [`mass-theory/binding-manybody-jet-filtration.md`](../../content/quantum-observable-universe/mass-theory/binding-manybody-jet-filtration.md), `jet-filtration-binding-extensive.md` | conjecture + sorry-free extensivity | the *shape* the derived route must reproduce; its body-order index `n` is the natural match for Hochschild/descent degree |
| **"The spectral-sequence work is a no-go, not a tool"** | [`2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md`](2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md) | audit | reached §2's conclusion first; this document supplies the *constructive* complement |
| **KS §15**: the semisimple *nerve* (cellular tower, Habiro ring, `A_∞` minimal model) is shared; QOU collapses it at `q₀` | [`2026-06-04-kontsevich-soibelman-0811.2435-qou-comparison.md`](2026-06-04-kontsevich-soibelman-0811.2435-qou-comparison.md) §15 | audit | the "integralise" move was already named by the owner in June |
| **Webster–Williamson** lead: geometric Markov trace, weights = Molien series, categorified by `B_Δ`-equivariant IC of `BwB` | [`2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md`](2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md), bean `qou-sf1t` | lead, four open verification items | the held door into route A |
| Non-commutative cumulant structure exists (Garoufalidis–Le arc-graph zeta) but the parameter is wrong | [`2026-08-31-noncommutative-cumulant-structure-exists-colored-jones.md`](2026-08-31-noncommutative-cumulant-structure-exists-colored-jones.md) | audit | the "log of a determinant is a sum over connected cycles" identity is a degree-0 cumulant structure; it is the classical shadow of factorization-homology gluing (§5-E) |
| Yekutieli per-cell `λ_scale` route — tried in production, **purged 2026-05-24** (bijection negative, PR #985) | [`2026-05-22-yekutieli-percell-conjecture-formalized.md`](2026-05-22-yekutieli-percell-conjecture-formalized.md), [`2026-05-24-yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md), [`2026-05-25-non-abelian-stokes-reading-a-exploration.md`](2026-05-25-non-abelian-stokes-reading-a-exploration.md) | historical | a **mass-side** use of Yekutieli that failed; it never touched binding or the 3-dim Stokes theorem |
| Step 2 of the canonical chain **downgraded**: the "curvature 2-form" is stipulated, the Lean is a `ring` identity, `prop:hecke-spectral-sequence` does not exist | [`canonical-derivation-cheat-sheet.md` §2a](../canonical-derivation-cheat-sheet.md) (2026-08-25) | audit | any Yekutieli route that builds *on* Step 2 inherits an unproved geometry |
| Where a surface term could come from; non-abelian Stokes unpacked; "the exact paper is already held" | [`2026-08-30-nonabelian-stokes-and-the-surface-term.md`](2026-08-30-nonabelian-stokes-and-the-surface-term.md), bean `qou-edt7` | scope-(a) | the closest prior work to §5-D; it did not reach Thm 8.6.6 |
| `qou-dwsh` (completed, high): *"a groupoid with inequivalent fibre objects carrying a 3-dim `W` whose fundamental is not self-dual"* is the only honest route to flavour SU(3) | `.beans/qou-dwsh--…` | completed bean; reached again by PR #6458 (`FibreFunctorDimensionNotCategorical`) | groupoid route already named for the *flavour* problem; distinct from the binding problem but shares the machinery |
| `qou-tower` (in-progress): the production code path reduces every nucleus to the same 6-dim NF at every step — *"there is no tower"* in that path; later corrected: the GS reduction *digests* entanglement into coefficients, the q-degree grading **is** the many-body decomposition; symbolic NF is 6 coefficients at any `A` | `.beans/qou-tower--…`, PR #6333 | in-progress | the compute-side statement that the fibre-collapse is where the tower is lost; the q-degree grading is the *integralise* move seen from the code |

### 3.2 Library (path 5, both tiers) — held vs not held

Measured this session over 576 directories (552 `INDEX.md` rows, 23 duplicate dirs — the index is
stale by exactly one work, `library/ant-v14-n7-s`, which lacks a `summary.json`).

**Held and directly usable (all greppable under `library/<id>/sections/`):**

| doc-id | work | why it matters here |
|---|---|---|
| `arxiv-1007.1250v4` | **Yekutieli, Nonabelian Multiplicative Integration on Surfaces** (139 pp; all body text in one file `sec-000-0-introduction.md` — ingestion defect, text complete) | §4 |
| `arxiv-0801.0083v4` | **Yekutieli, Central Extensions of Gerbes** — *ingested this session* (36 pp, 7 sections, 43 candidates) | §4.3, route D1; verifies (and corrects) the `lifting-and-descent` citations |
| `arxiv-1109.1919v3` | **Yekutieli, Combinatorial Descent Data for Gerbes** — *ingested this session* (13 pp; Thm 0.1 = Thm 2.4: a weak equivalence of cosimplicial crossed groupoids induces a bijection on gauge classes of descent data) | route D1: the corpus's own `prop:cosimplicial-crossed-groupoid` object, with its invariance theorem |
| `arxiv-math-0505170v2` | **Yekutieli, An Averaging Process for Unipotent Group Actions** — *ingested this session* (11 pp; Thm 0.1: weighted average `wav_G` gluing local torsor sections into a global simplicial section) | the gluing device behind twisted DQ; the "simplicial section" is a global object built from local ones — the descent direction of route D1 |
| `arxiv-1108.5286v3` | **Solleveld, Hochschild homology of affine Hecke algebras** | route B: the non-semisimple object containing `H_n` whose `HH_*` is computed |
| `arxiv-0911.4494v2` | **Webster–Williamson, The geometry of Markov traces** (character sheaves ×24, Soergel ×8) | route A's held door |
| `07243231`, `arxiv-1702.00039v1`, `arxiv-2501.03424v1` | Elias–Makisumi–Thiel–Williamson book; Libedinsky; Wynner — Soergel bimodules | route A's presentation |
| `arxiv-1409.2799v2` | Diagram categories for `U_q`-tilting modules at roots of unity | route B (roots of unity) |
| `arxiv-1202.5547v1` | Markov property and Khovanov–Rozansky homology, Coxeter case | route A: the Markov property *of the categorified trace* |
| `arxiv-1203.2182v1` | Fuji et al., Volume Conjecture: Refined and Categorified | route A ↔ volume |
| `centsim` | **Geck–Rouquier, Centers and simple modules for Iwahori–Hecke algebras** — **98 % of its text is in `ocr/` only**; a `sections/` grep cannot see it | the centre = `HH_0`; the object every corpus trace lives in |
| `arxiv-1103.4815v3` | Nikolaus–Waldorf, Four equivalent versions of non-abelian gerbes (crossed module ×18) | §4: gerbe ≡ crossed module ≡ 2-bundle ≡ stack |
| `arxiv-1003.4485v2`, `arxiv-math-0511710v2` | Baez–Huerta, Invitation to higher gauge theory; Baez–Schreiber, Higher gauge theory | §4: the mainstream 2-holonomy against which Yekutieli's MI is to be compared |
| `arxiv-1901.08945v2` | Decompositions of derived categories of gerbes | the one held derived-category ↔ gerbe bridge |
| `arxiv-2510.04782v2` | q-Hodge complexes over the Habiro ring (∞-categorical) | route B, all orders in `q` |
| `arxiv-math-9806163v1` | Orellana, Weights of Markov traces on Hecke algebras (Bratteli) | route G; the `y_λ` object |
| `arxiv-math-0411505v2` | Garoufalidis–Le, non-commutative formula for the colored Jones function | the degree-0 cumulant structure |
| `arxiv-2111.06645v3`, `0307092v2`, `arxiv-1712.04887v3` | Garoufalidis–Zagier; Neumann extended Bloch group; Calegari–Garoufalidis–Zagier | route H (volume as a degree-3 class) |
| `arxiv-2507.19896v1` | Generalized Markov traces and Jucys–Murphy elements | route B: JM elements = the affine lattice |

**Cited by the corpus but NOT held (cannot be checked from the library):**

| bib key | work | citing files | consequence |
|---|---|---|---|
| ~~`yekutieli2010`~~ | Central Extensions of Gerbes — **HELD as of this session** (`library/arxiv-0801.0083v4`, owner upload `ad60e3f2`) | **148** — by theorem number (`Thm 1.7`, `§3`, `Thm 3.4`, `Thm 4.5`) | **now checkable, and the check fails: none of `Thm 1.7 / 3.4 / 4.5` exists in the paper.** Its theorems are 3.13 (quotient gerbe), 4.6 (obstruction to lifting isomorphisms), 4.17 (obstruction to lifting objects), 5.11 (existence of `cl²` under `N`-acyclic coverings), 6.10 (pronilpotent gerbes). "Thm 4.5 — twisted quantization map on algebraic varieties" is not in this paper at all; it is presumably in the twisted-DQ paper (`0905.0488`, still not held) and mis-keyed |
| `yekutieli2008` | Twisted Deformation Quantization (survey) | 22 | still not held; the likely true home of the "Thm 4.5" citation |
| `yekutieli2009` | MC Elements in Pronilpotent DG Lie Algebras | 12 | still not held |
| `khovanov2000`, `khovanov-rozansky2008`, `khovanovlauda2009`, `brundankleshchev2009` | categorification foundations | few | route A's primary sources absent |
| `wenzl1988`, `wenzl1990` | Hecke algebras and subfactors | load-bearing (the `IsOcneanuWeightSystem` class cites it with zero instances) | already flagged 2026-09-04 |
| `bridgeland2007`, `lurie2009`, `freed2010`, `suslin1991`, `matveev1982` | — | — | — |

**Held nothing at all on:** factorization homology (0 documents, 0 `references.ts` entries),
Ben-Zvi / Nadler / Francis (0), Toën (2 incidental), Drinfeld centre by name (4 incidental),
planar algebras (3 incidental), Baez–Hoffnung–Walker groupoidification (0). Route E and route C have
**no held source**.

---

## 4. Yekutieli: what is exhausted, what is not

### 4.1 The corpus's engagement is at the level of vocabulary, not theorems

Concept counts over `content/ docs/ computations/` (this session): *multiplicative integral* 62
files, *kite* 61, *crossed module* 26, *Riemann product* 7 — against *balloon* **1**, *additive
feedback* **1**, *quasi crossed* **1**, *3-curvature* **0**. And

```
grep -rl "Theorem 0.4.2|0.5.4|8.6.6|4.4.15|3.3.19|6.2.1|6.3.1|5.4.8|9.3.5" content/ docs/ computations/ .beans/
→ 0 files for every one
```

The single structured citation is `\cite[Ch. 5–6]{yekutieli2015}` in
[`yekutieli-mapping-table.md`](../../content/quantum-observable-universe/lifting-and-descent/yekutieli-mapping-table.md)
("Mass identity ↔ nonabelian multiplicative integral; 2D nonabelian Stokes theorem"). No numbered
theorem of the held book is cited anywhere.

### 4.2 The held book, result by result

| result | statement (as held) | corpus use | relevance to binding |
|---|---|---|---|
| Thm 0.2.4 / 4.4.15 | existence of `MI(α,β\|σ,τ) ∈ H` as a limit of Riemann products over a kite; functorial in the crossed module | adopted (kites, RP) — the mass-side `λ_scale` attempt of 2026-05 | the *definition* of Step 2 |
| Thm 0.4.2 / 6.2.1 | **2-dim Stokes**: `Φ(MI(α,β\|σ,τ)) = MI(α\|∂(σ,τ))`; Schlesinger when `G = H = GL_m` | adopted by name | boundary-holonomy consistency; degree-0 |
| **Thm 6.3.1** | **fundamental relation** `Ψ(g) = Ad_H(h)` with `g = MI(α\|∂)`, `h = MI(α,β\|σ,τ)` | **never cited** | a structural constraint on any `G`↔`H` split: the 1-holonomy (Hecke) acts on the 2-holonomy (surface) by conjugation. The mapping-table row "G ↔ Hecke, H ↔ linking group" must satisfy it |
| **Thm 7.5.1** | **square puzzles**: any relation `w(a_i) = 1` in `π₁(sk¹ sd^k I²)` among boundary loops transports to `w(h_i) = 1` in `H` | **never cited** | a free-group-to-holonomy transfer: braid relations become relations among surface holonomies. This is the shape of a "word topology ⇒ observable" bridge (§1.3, first row) |
| **Thm 8.6.6 / 0.5.4** | **3-dim Stokes** — the book's stated main new result: with `γ` the 3-curvature, (1) `γ` is *inert* (a generalised Bianchi identity, Rem. 8.6.7); (2) for any balloon, `MI(α,β\|∂(σ,τ)) = MI(α,γ\|τ)` | **never cited; 0 hits on "3-curvature"** | a **boundary product over a closed surface equals a bulk integral of a 3-form**. That is literally a volume ↔ surface exchange. Whether it has anything to do with `a_V`/`a_S` is a question, not a result (§5-D) |
| §5 (quasi crossed modules, additive feedback) | the weakened axioms `Φ = (Φ₀, Φ_X)` in which Thm 8.6.6 actually runs | 1 hit | needed to use 8.6.6 at all |
| Thm 2.1.2 | CBH estimate `‖log ∏ exp(α_i)‖ ≤ c₀(G)·…` | quoted in the 2026-08-30 audit without number | the analytic engine; the `h²`-coefficient story of 2026-05-24 is a CBH expansion |
| Conj. 9.5.2 | `MI(−\|Δ) : MC(Ñ(f)) → Desc(Del(f))` is a bijection for a cosimplicial nilpotent quantum-type DG Lie algebra | **never mentioned** | the book's own open problem *is* the `lifting-and-descent` chapter's subject: MI as the map from Maurer–Cartan elements to descent data of Deligne groupoids |

### 4.3 The Yekutieli works not held, and what each would add

Links are to the arXiv abstract; ids confirmed from listing pages only (§9).

| work | link | flavour | what it would add to the binding question |
|---|---|---|---|
| **Central Extensions of Gerbes** (Adv. Math. 2010) — **HELD, `library/arxiv-0801.0083v4`** | [arXiv:0801.0083](https://arxiv.org/abs/0801.0083) | groupoid | **now verifies 148 corpus citations — and they fail on theorem number (§9).** Obstruction classes to lifting through a central extension are *by construction* classes that vanish on restriction and are non-zero on the whole — the shape of a 3-body term. Highest-value acquisition regardless of route |
| **Combinatorial Descent Data for Gerbes** (JNCG 2014) — **HELD, `library/arxiv-1109.1919v3`** | [arXiv:1109.1919](https://arxiv.org/abs/1109.1919) | groupoid | descent data in **cosimplicial crossed groupoids** — the corpus's own `prop:cosimplicial-crossed-groupoid` object; weak equivalences induce bijections on gauge classes. Degree-`≥2` descent data is not determined by degree-1 (pairwise) data: the cleanest statement in Yekutieli's own language of "higher descent degree = irreducibly higher-body datum" |
| An Averaging Process for Unipotent Group Actions (2006) — **HELD, `library/arxiv-math-0505170v2`** | [arXiv:math/0505170](https://arxiv.org/abs/math/0505170) | groupoid/descent | the weighted-average `wav_G` that glues local sections of a unipotent torsor into a global *simplicial* section — the concrete gluing mechanism the twisted-DQ papers use; the simplicial degree is a descent degree |
| MC Elements in Pronilpotent DG Lie Algebras (JPAA 2012) | [arXiv:1103.1035](https://arxiv.org/abs/1103.1035) | hinge | the Deligne 2-groupoid; the one paper in both halves of his work; where gauge-invariance of a deformation-theoretic obstruction is proved |
| Twisted Deformation Quantization of Algebraic Varieties (Adv. Math. 2015) + survey | [arXiv:0905.0488](https://arxiv.org/abs/0905.0488), [arXiv:0801.3233](https://arxiv.org/abs/0801.3233) | groupoid | the "stack-like version of a deformation" the `direct-limit-algebra` / `stack-like-structure` blocks describe; read the survey first |
| Derived Categories (CUP 2019) | [arXiv:1610.09640](https://arxiv.org/abs/1610.09640) | derived | reference only; no mechanism for a many-body term |
| The Squaring Operation for Commutative DG Rings | [arXiv:1412.4229](https://arxiv.org/abs/1412.4229) | derived | rigidity = a self-referential normalisation; analogy only |
| Duality and Tilting for Commutative DG Rings | [arXiv:1312.6411](https://arxiv.org/abs/1312.6411) | derived | derived Picard group is ⊗-multiplicative — same formal shape as `tr_M`; speculative |
| Rigid Dualizing Complexes on Schemes; (with Zhang) Rings with Auslander Dualizing Complexes | [arXiv:math/0405570](https://arxiv.org/abs/math/0405570), [arXiv:math/9804005](https://arxiv.org/abs/math/9804005) | derived | the Zhang paper is the only derived item about *noncommutative* rings; no known application to Hecke algebras |
| Rigidity, Residues and Duality: Overview | [arXiv:2102.00255](https://arxiv.org/abs/2102.00255) | derived (survey) | the cheapest way to decide the derived half: read this instead of the four above, and if nothing speaks to traces, close it |
| Porta–Shaul–Yekutieli, Homology of Completion and Torsion; Flatness and Completion Revisited; Weak Proregularity and Derived Completion | [arXiv:1010.4386](https://arxiv.org/abs/1010.4386), [arXiv:1606.01832](https://arxiv.org/abs/1606.01832), [arXiv:2002.04901](https://arxiv.org/abs/2002.04901) | derived | *derived completion* is "all orders in `q`" stated algebraically — relevant to the ruling's second half, silent on many-body |

**Assessment, stated as judgement.** Yekutieli's corpus splits into two bodies of work that do not
talk to each other. The groupoid-flavoured half (surface integration, crossed groupoids, gerbes,
MC elements) is the toolkit for the Step-2 bridge and for the `lifting-and-descent` chapter, and it
is half-unread. The derived-flavoured half (dualizing complexes, DG rings, rigidity, completion) is
Grothendieck duality; I found no theorem in it that touches traces on a tower, and I would not
spend the owner's time on it beyond the 2021 overview. **"Quarter to kill you" is right in one
sense: the four gerbe/descent papers are the ones to finish, and the one that matters most is the one
we do not hold.**

### 4.4 A caveat about kites that is decidable from the definitions

Every 2-cell in the book's construction is a *kite*: a 2-simplex **tethered to the basepoint by a
path** `σ`. The resulting 2-holonomy is therefore a composition of transports along the tether,
i.e. of *pairwise* data (basepoint–cell). If that reading is right, the 2-dimensional MI is
structurally pair-local, and only the **balloon** (a 3-cell, Thm 8.6.6) is the first object whose
value is not a composite of tethered pieces. This is checkable from Definitions 4.x and 8.x of the
held text and is worth an hour before any construction — it would say, in advance, that no
2-dimensional Yekutieli object can carry `b₃`, and that the 3-dim Stokes theorem is the *only* place
in the book a 3-body term could sit. **Unverified; recorded as the first thing to check on route D.**

---

## 5. The attack routes

Each route carries the same frame: what it means · what it buys · what it costs · what it risks ·
what it commits to · the formalize-first prune · the falsifiable test · literature needed · my
judgement. "Held" refers to §3.2.

### Route A — Categorified Markov trace: Hochschild homology of the Hecke category

**What it means.** Replace the number `tr_M(β)` by the triply-graded HOMFLY-PT homology
`HHH(β̂)` of the braid closure (Khovanov: `HHH = HH_*` of the Rouquier complex of `β` in Soergel
bimodules; Khovanov–Rozansky). Its Euler characteristic in the third grading is the HOMFLY-PT
polynomial, i.e. `tr_M(β)` in the corpus's normalisation. The extra gradings are **new information
the trace cannot see**. The corpus's forced functional `log(tr_free/tr_atom)` is then the degree-0
shadow of `log` of a Poincaré polynomial `P_β(a, q, t)`.

**What it buys.** (i) Exactly the object the ruling asks for on the "all `n`" axis, with `tr_M`
recovered *identically* at `t = −1` — nothing at order zero changes. (ii) A concrete, computable
place for a class that is non-zero on a 3-component closure and vanishes on every 2-component
sub-closure: HOMFLY-PT homology of a link is *not* a Künneth product of its sublinks' homologies
in general (only the split union is). (iii) Webster–Williamson's geometric model (`HH_*` of Soergel
bimodules = equivariant IC of `B×B`-orbit closures; type A equivariantly formal; exterior algebra
over a polynomial ring, explicit Hilbert series) makes the higher degrees calculable, and the
corpus already holds their companion paper and has a lead open on it (`qou-sf1t`).

**What it costs.** Real compute: the Rouquier complex of an `n`-strand braid word is a complex of
`2^{ℓ}` Soergel bimodules for a word of length `ℓ`; for the atom word at `A = 2` (`n = 6`,
`ℓ ≈ 10`) this is tractable by hand-rolled Soergel calculus or by existing HOMFLY-homology code;
at `A = 3, 4` one needs Gorsky–Neguț–Rasmussen's flag-Hilbert-scheme route or Oblomkov–Rozansky. No
Lean: Mathlib has no Hochschild homology, no Soergel bimodules. The theory side is a citation, not
a formalisation.

**What it risks.** The **selection risk is severe and must be named now.** A triply-graded object
offers a continuum of specialisations `(a, q, t) ↦ number`; picking the one that reproduces `b₃` is
exactly the fit the anti-fit directive forbids (*"selection against the target"*). The only
admissible use is *structural*: a class that provably vanishes on pairwise restrictions and
provably does not on the triple, with its specialisation fixed by the framework's existing
conventions (`q = q₀`, and `t`, `a` fixed by a *derived* rule or left symbolic). If no such rule is
derived, the route yields a reframing and a computation, not a number — and that must be reported
as such.

**What it commits to.** Adopting the Hecke *category* as the fibre-level object. Downstream this is
consistent with the fibre-vs-observable banner (AGENTS.md) and with `markov-moves-brane-tower`
(`HH_0` of a simplicial object). It does not touch Δ_λ, the log law, or any witness.

**Formalize-first prune (cheap, decisive).** Before computing anything: prove that for a *split*
link `HHH(L₁ ⊔ L₂) ≅ HHH(L₁) ⊗ HHH(L₂)` (Künneth — standard) and therefore that `log P` is
*additive* over split unions at every grading; then state as the test statement that for the
3-component **atom closure** (which is not split — the carrier is a path-linked `#_g T(2,e_g)`),
the connected 3-body cumulant of `log P_β(a,q,t)` is non-zero at some grading. If it is identically
zero at every grading, route A is scope-(a) dead on contact and the many-body term is not a
Hochschild degree.

**Falsifiable test.** Compute `P_β(a,q,t)` for the atom words at `A = 2, 3` (`n = 6, 9`) and the
three 2-component sub-closures; form the cumulant `log P(3) − Σ log P(2) + …` at each grading.
Report the full polynomial, not a number. Cross-check `t = −1` against the corpus's `tr_M` witnesses
to 50 dps (this is a required consistency check, and cheap).

**Literature.** Held: Webster–Williamson (`arxiv-0911.4494v2`), the three Soergel expositions,
`arxiv-1202.5547v1`. Needed: Khovanov [arXiv:math/0510265](https://arxiv.org/abs/math/0510265);
Khovanov–Rozansky II [arXiv:math/0505056](https://arxiv.org/abs/math/0505056); Webster–Williamson
*geometric model for HH of Soergel bimodules* [arXiv:0707.2003](https://arxiv.org/abs/0707.2003)
(distinct from the held *geometry of Markov traces*); Elias–Williamson Soergel calculus
[arXiv:1309.0865](https://arxiv.org/abs/1309.0865); Rouquier [arXiv:math/0409593](https://arxiv.org/abs/math/0409593);
Gorsky–Neguț–Rasmussen [arXiv:1608.07308](https://arxiv.org/abs/1608.07308);
Oblomkov–Rozansky [arXiv:1608.03227](https://arxiv.org/abs/1608.03227); Ben-Zvi–Nadler *Character
theory of a complex group* [arXiv:0904.1247](https://arxiv.org/abs/0904.1247) (the Hecke category
is 2-dualizable Calabi–Yau; its categorical trace is computed); Ben-Zvi–Nadler *Nonlinear traces*
[arXiv:1305.7175](https://arxiv.org/abs/1305.7175).

**Judgement.** The strongest route for the "all `n`" half of the ruling, and the one whose prune is
cheapest. Its danger is entirely on the selection side.

### Route B — Integralise: the tower over `ℤ[q^{±1}]`, the Habiro ring, and the affine Hecke algebra

**What it means.** Stop evaluating at `q₀` before taking cohomology. Over `ℤ[q^{±1}]` (or the Habiro
ring) `H_n` is cellular and *not* semisimple; its Hochschild (co)homology is non-trivial and its
`q`-adic / cyclotomic structure is the "all orders in `q`" of the ruling. Concretely: the affine
Hecke algebra `H_n^{aff} = H_n ⋉ ℤ[X_1^{±1},…,X_n^{±1}]` contains `H_n`, its polynomial part is
generated by the Jucys–Murphy elements the corpus already uses, and **Solleveld's computation of
`HH_*(H_n^{aff})` is held** (`arxiv-1108.5286v3`). The `q`-degree grading that `qou-tower` found
survives the GS reduction ("the q-degree grading *is* the many-body decomposition") is this move
seen from the code.

**What it buys.** A non-zero `HH_{≥1}` on an object that *contains* the framework's algebra, with
held literature; the "all orders in `q`" half of the ruling satisfied by construction (the corpus's
Habiro-element vocabulary for α_EM and the `c_k` ladder is the same move); and a natural candidate
for the interleaving cross-term of §1.3 to be a *degree-1* class (the JM lattice is what
distinguishes interleaved from sequential words).

**What it costs.** Moderate: Solleveld's computation is for the affine algebra of a *root datum*,
at generic and root-of-unity parameters; transporting it to a braid closure needs the closure map
`H_n^{aff} → ` (something with a trace), which is not in his paper. Habiro-ring membership of
`tr_M(β_atom)` as a function of `q` is a real question (the corpus's own KS §16.2 lists it as "one
useful theorem-shape").

**What it risks.** Low mathematical risk; the risk is scope creep into the SM-side Habiro programme
(`qou-cds1`, convention-D re-derivation of the `c_k` ladder), which is a different arc. Also: a
*root-of-unity* fibre (`arxiv-1409.2799v2` tilting modules) is non-semisimple but `q₀ ≈ 1.11` is
not a root of unity, so root-of-unity results reach `q₀` only through the Habiro-ring gluing
(Garoufalidis–Zagier, held).

**What it commits to.** Carrying `q` symbolic through the trace and only specialising at the end —
which is already the §7c base-ring convention. No conflict.

**Formalize-first prune.** Prove in Lean (over a generic `[CommRing R]`) the statement the
2026-08-25 audit found *unproved*: that the corpus's `WhiteheadHH` collapse is honestly stated —
i.e. replace the vacuous `spectral_sequence_collapses_to_centre` by a content-bearing conditional
whose hypothesis is semisimplicity and whose conclusion is `HH_1 = 0` in a concrete model (the
`Fin n`-indexed idempotent decomposition), and *exhibit* an element of `HH_1` over `ℤ[q^{±1}]` at
`n = 2` or `3` that is killed by inverting `[2]_q`. That single example is the proof that "the
tower has degrees the fibre lacks," and it is elementary.

**Falsifiable test.** Does the interleaving cross term `z(z² − hz − 1)` of §1.3 have a `q`-adic
valuation (order of vanishing at `q = 1`) strictly higher than the sequential product's? If yes,
the cross term is an "order-`≥1` in `q`" object and the ruling's second half is where it lives; if
no, interleaving is an order-zero phenomenon and route B's relevance to `b₃` is weakened.
(Exact algebra in `ℚ(q)`; one afternoon.)

**Literature.** Held: Solleveld; Geck–Rouquier (`centsim`, OCR tier); Garoufalidis–Zagier; the
Habiro ring papers; JM-element Markov traces. Needed: Graham–Lehrer cellular algebras (not on
arXiv; Invent. Math. 123 (1996)); Habiro, *Cyclotomic completions of polynomial rings*
[arXiv:math/0209324](https://arxiv.org/abs/math/0209324); Venkatesh, *Derived Hecke algebra*
[arXiv:1608.07234](https://arxiv.org/abs/1608.07234) — for the structural idea only (*"the Hecke
algebra was too small; the right object is a graded algebra whose degree-0 part is the classical
one"*), not for its arithmetic content.

**Judgement.** The route most continuous with what the corpus already does and the one with the
most held literature. It is the natural home of the `q`-degree grading `qou-tower` found. It is
less likely than A to produce a 3-body *class* by itself and more likely to explain the interleaving
cross term.

### Route C — Groupoidify: `H_n(q)` as spans of flag groupoids; binding as a log-cardinality

**What it means.** Baez–Hoffnung–Walker realise `H_n(q)`, for `q` a prime power, as
degroupoidified spans of groupoids of flags over `𝔽_q`; the `q`-numbers are groupoid
cardinalities. Groupoid cardinality is additive over coproducts and multiplicative over products —
the exact profile of `tr_M` — and it is obtained by **counting**, not by weighting. In that
presentation `log(tr_free/tr_atom)` is a **relative entropy / log-cardinality**, and a many-body
term is a class on a configuration groupoid, which has no per-block index at all — precisely the
shape the intensive/extensive wall demands.

**What it buys.** (i) A structural answer to *why the weights are what they are* (a count), which
no per-block route can give. (ii) A home for the word-topology source of §1.3: the braid group is
`π₁` of configuration space, and an interleaved word is a path that is not a concatenation of
pairwise paths — a statement about a fundamental groupoid. (iii) Contact with `qou-dwsh`'s
flavour specification (a groupoid with inequivalent fibre objects).

**What it costs.** The construction needs `q` a prime power; `q₀ ≈ 1.11` is real. So it can only
deliver **identities of Laurent polynomials in `q`** (valid at infinitely many prime powers ⇒ valid
identically ⇒ valid at `q₀`). That is a legitimate and standard technique, but it means the
groupoid never sees the archimedean anchor — it is a fibre-level (formal-`q`) object, exactly as
the fibre-vs-observable banner says. Also: groupoid cardinality is rational-valued; the corpus's
weights are in `ℚ(q)`, fine, but any *transcendental* ingredient (`Vol`) is outside this route.

**What it risks.** Reframing without theorem. The danger is spending effort building a groupoid
that reproduces `tr_M` and stopping, having learned nothing about `b₃`.

**Formalize-first prune.** State: "the BHW span for a *sequential* juxtaposition of interface words
is a product of spans" (this should be a one-page lemma), and "for the `n = 4` interleaved word it
is not"; then the `n = 4` cross term is a groupoid-cardinality statement and route C has proved
something the trace could only measure.

**Falsifiable test.** Reproduce the §1.3 cross term `z(z² − hz − 1)` as a difference of groupoid
cardinalities at `q = 2, 3, 4, 5` and confirm the polynomial. Exact and cheap once the spans are
written.

**Literature (none held).** Baez–Hoffnung–Walker [arXiv:0908.4305](https://arxiv.org/abs/0908.4305)
(**the** paper); Baez–Dolan [arXiv:math/0004133](https://arxiv.org/abs/math/0004133) (groupoid
cardinality, short); Morton [arXiv:0810.2361](https://arxiv.org/abs/0810.2361) (linearisation
`Span(Gpd) → 2Vect`) and [arXiv:math/0601458](https://arxiv.org/abs/math/0601458) (the many-particle
worked example); weak Hopf algebras / quantum groupoids — Nikshych–Vainerman survey
[arXiv:math/0006057](https://arxiv.org/abs/math/0006057), Böhm–Nill–Szlachányi
[arXiv:math/9805116](https://arxiv.org/abs/math/9805116) (integral/Haar theory = a theory of
*non*-multiplicative traces on a tower-like object).

**Judgement.** The most conceptually satisfying route and the least likely to yield a MeV. Worth
the two papers and the one-page lemma; not worth a construction until A or B has shown a class.

### Route D — Yekutieli higher: degree-`≥2` descent data and the 3-dimensional Stokes theorem

**What it means.** Two sub-routes, sharing the corpus's `lifting-and-descent` machinery.

- **D1 (descent).** The corpus's `prop:cosimplicial-crossed-groupoid` is a cosimplicial object whose
  degree-1 data are the transition 1-morphisms `g_ij` (pairwise) and whose degree-2 data are the
  2-morphisms `a_ij` and the twisted cocycle `d(g_ijk) = a·g·a⁻¹`. **Degree-`≥2` descent data is not
  determined by degree-1 data** — that is what a non-trivial gerbe class `κ_n ∈ H²` *is*. A 3-body
  term as "the `H²`/`H³` obstruction class of the assembled brane tower that vanishes on every
  2-component sub-assembly" is a precise proposal in the corpus's own vocabulary, and Yekutieli's
  *Combinatorial Descent Data* paper (not held) is where its gauge-invariance would be proved.
- **D2 (3-dim Stokes).** Thm 8.6.6: `MI(α,β|∂(σ,τ)) = MI(α,γ|τ)` — the 2-holonomy over a closed
  surface equals the bulk integral of the (inert) 3-curvature. If the framework's binding
  2-holonomy over the assembled surface `S_c` is the *boundary* of a 3-cell, then its value is a
  *volume* integral, and the ratio "surface piece / volume piece" is a ratio of `∫γ` to `∫β` — a
  candidate *derivation* of an `a_S/a_V`-type ratio with no constant chosen.

**What it buys.** D1: a many-body term with no per-block index, in a chapter that already exists,
consumed already by `mass-theory/volume-tower-decomposition`. D2: the only route on this list that
talks about a *volume vs surface* split in the language the framework already uses for Step 2.

**What it costs.** Both stack on **Step 2 of the canonical chain, which is not derived**: the
"curvature 2-form `F(σ) = σ² − (q−q⁻¹)σ − 1`" is stipulated; no connection, no surface, no
multiplicative integral exists in the Lean; `prop:hecke-spectral-sequence` does not exist
(cheat-sheet §2a, 2026-08-25). D2 additionally needs the framework's surface to be a boundary
(is `S_c` a 2-cycle bounding a 3-chain in the brane tower? — unasked) and needs the 3-curvature `γ`
to be *computed*, not stipulated, or the whole thing is the Step-2 tautology one dimension up.

**What it risks.** The *tautology risk* is the same one that bit Step 2: naming a 3-form after the
answer. And the 2026-05 per-cell route was a mass-side Yekutieli attempt that was purged as a
coincidence basin; D2 is not that route (it is about binding and about the 3-dim theorem), but a
reviewer will ask why this one is different, and the answer has to be "because the 3-form is
computed."

**What it commits to.** Nothing new — the chapter exists. But making D1 or D2 load-bearing for
binding raises the stakes on the 148 unverified `yekutieli2010` citations.

**Formalize-first prune.** (i) The kite-tethering check of §4.4 — decidable from definitions, one
hour. (ii) For D1: prove in Lean, on the existing `ccg-cosimplicial-identities.lean` carrier, that
the degree-2 cocycle `a_ij` restricted to any 2-object sub-cover is a coboundary while the full
3-object cocycle is not — i.e. exhibit a non-trivial `H²` class that is pairwise-trivial. That is
the *shape* of `b₃` and it is finite combinatorics. (iii) For D2: state 8.6.6 in Lean as a
conditional class with `γ` a *field*, then check whether **any** candidate `γ` computable from the
Hecke data is non-zero — if `γ = 0` on the Hecke connection (fake-flat *and* 3-flat), 8.6.6 says
the boundary MI is trivial and D2 is dead on contact.

**Falsifiable test.** D2's decisive check is `γ = 0` or not. D1's is the pairwise-trivial class.

**Literature.** Held: the book (§4.2), Nikolaus–Waldorf, Baez–Huerta, Baez–Schreiber. Needed:
*Central Extensions of Gerbes* [arXiv:0801.0083](https://arxiv.org/abs/0801.0083) (verifies the
chapter); *Combinatorial Descent Data* [arXiv:1109.1919](https://arxiv.org/abs/1109.1919) (D1);
Schreiber–Waldorf, *Connections on non-abelian gerbes and their holonomy*
[arXiv:0808.1923](https://arxiv.org/abs/0808.1923) (the gluing axioms — the sharpest audit tool for
what a tethered kite discards); Martins–Picken, *On two-dimensional holonomy*
(TAMS 362 (2010); arXiv id [0710.4310](https://arxiv.org/abs/0710.4310) unverified) — same Lie
crossed module, thin-homotopy 2-groupoid method: the independent construction to compare the MI
against.

**Judgement.** D1 is a genuinely good idea whose cost is the unverified gerbes paper; D2 is the
highest-upside/highest-tautology-risk item on the list. Neither should be started before the
prunes.

### Route E — Factorization homology: extensivity and non-pair-locality as *axioms*

**What it means.** Factorization homology `∫_M A` of an `E_n`-algebra (n-disk algebra) `A` over a
(stratified) `n`-manifold `M` is a functor satisfying ⊗-excision: it is **multiplicative over
disjoint union by axiom** (the framework's forced extensivity) and its value on a manifold glued
along a collar is a *relative tensor product* — a genuinely many-body gluing, not a product of
pairwise pieces. Ayala–Francis–Tanaka's stratified version explicitly produces **link-homology
theories from 1-submanifolds of 3-manifolds** — a nucleus is a link in `S³`. Ginot–Tradler–Zeinalian
prove higher Hochschild homology *is* factorization homology over higher-dimensional sources,
which makes routes A and E one route.

**What it buys.** A finite **decision procedure**: the Ayala–Francis axioms are an
Eilenberg–Steenrod-style characterisation, so a candidate binding functional either satisfies
⊗-excision or it does not. Every pair-local functional fails it. The intensive/extensive wall and
the non-pair-locality theorem are, in this language, "the binding functional is not a homology
theory of the disjoint-union type; is it one of the excision type?"

**What it costs.** Theory-heavy; **no held source at all** (0 documents, 0 references). The real
mathematical question it reduces to — *is the QOU coefficient object an `E_3`-algebra?* — is open
and may well be *no* (the Hecke category is `E_1`; an `E_3` structure would need the braided
structure plus more). Costello–Gwilliam is two volumes.

**What it risks.** Formalism without contact. If the coefficient object is not `E_3`, route E
contributes vocabulary only.

**Formalize-first prune.** Write the ⊗-excision axiom for a functional on links in `S³` and prove
that pair-locality (`PairLocal`) contradicts it — a clean scope-(b) statement that "the many-body
term must be an excision-type object," which upgrades the corpus's `b₃`-based refutation of
pair-locality from a measurement to an axiom-level exclusion.

**Falsifiable test.** None cheap; this route's value is as the frame for A.

**Literature (none held).** Ayala–Francis–Tanaka [arXiv:1409.0848](https://arxiv.org/abs/1409.0848)
(**top of the list**); Ayala–Francis [arXiv:1206.5522](https://arxiv.org/abs/1206.5522);
Ginot–Tradler–Zeinalian [arXiv:1011.6483](https://arxiv.org/abs/1011.6483); Costello–Gwilliam vol. 1
(CUP 2017, chapters 1–3, 6); Beilinson–Drinfeld *Chiral Algebras* (AMS 2004; the Ran space — the
space of finite subsets — is the one object here *about varying particle number*); Pirashvili,
*Hodge decomposition for higher order Hochschild homology* (Ann. ENS 2000,
[DOI 10.1016/s0012-9593(00)00107-5](https://doi.org/10.1016/s0012-9593(00)00107-5), no arXiv) — the
canonical *indexing* of the higher Hochschild groups into weight pieces, i.e. how one would *name*
a 3-body class.

**Judgement.** The correct theoretical frame and the one I would want a mathematician to read
first; not a route to a number by itself.

### Route F — Yekutieli's derived half (dualizing complexes, rigidity, completion)

Assessed in §4.3. **Judgement:** read the 2021 overview
([arXiv:2102.00255](https://arxiv.org/abs/2102.00255)); if nothing in it speaks to traces on a
tower — and I found nothing — close it. Derived completion is the algebraic form of "all orders
in `q`" and is the one thing worth knowing from this half.

### Route G — Planar algebras, Bratteli diagrams, paragroups: irreducibly `n`-ary operations on the tower itself

**What it means.** In Jones's planar algebras the *tower* (Bratteli diagram) is the primary object
and a planar tangle with a 3-input box is an operation that is not a composite of 2-input boxes.
The corpus's `y_λ` are Ocneanu weights (Orellana, held). A 3-input tangle evaluated on the
Temperley–Lieb / Hecke tower is a candidate irreducibly 3-body operation *at degree zero*.

**Buys / costs / risks.** Cheap to evaluate; degree-0, so it lives on the word-topology side of
§1.3, not the higher-structure side; the risk is that every 3-input tangle reduces by TL relations
to 2-input ones at generic `q` (which is what one would expect from semisimplicity — and would be
a *nice* negative, because it would say the planar route needs the non-semisimple tower too).

**Prune / test.** Is there a 3-box planar tangle on `TL_3(q)` not in the span of 2-box composites?
Finite linear algebra.

**Literature.** Held: Orellana. Needed: Jones, *Planar Algebras I*
[arXiv:math/9909027](https://arxiv.org/abs/math/9909027). Ocneanu's paragroup original (LMS
Lecture Notes 136, 1988) is not on arXiv and is expositionally superseded.

### Route H — Volume as a degree-3 class (extended Bloch group / `K_3^{ind}`)

Held: Neumann, Zickert-adjacent, Garoufalidis–Zagier, CGZ. `Vol` as a class in
`H₃(PSL(2,ℂ)^δ)` (groupoid homology of a one-object groupoid) rather than a number is the right
*shape* for a 3-body quantity; but the corpus's `2026-09-04-roast-of-the-six-attack-routes.md`
already found the rank mismatch between the shuffle depth grading and the K-theory weight tower,
and the deuteron ruling (2026-08-29) says the deuteron binding is *not* a hyperbolic-volume term.
**Judgement:** do not open this for binding; it is the flavour/volume arc's business (`qou-2q85`).

---

## 6. Downstream implications, in paper-and-physics terms

**What none of the routes changes.**

- `Δ_λ = (−1)^{n(λ)} dim V_λ` (proved) — untouched; it is the `HH_0` datum and stays exactly that.
- The log law and `E₀ = m_e/(q(q−1))` — untouched at order zero; every route recovers `tr_M`
  identically at the fibre.
- The Coulomb exclusion (`BoundedDegreeCoulomb`) — **not rescued by any route here.** Coulomb is
  `1/r` long-range and outside the bond-graph *form*; a higher Hochschild class or a descent class
  does not supply `Z(Z−1)` with `A^{−1/3}` geometry. The honest statement is that the derived routes
  address the fourth piece of §1.2 and not the second. Anyone selling a derived route as "closing
  the binding gap" is overclaiming by the 47.7 % that Coulomb is at ²⁰⁸Pb.
- The surface term — already supplied structurally by the bounded-degree deficit; route D2 would
  at most *re-derive* its ratio, and only if `γ ≠ 0`.
- No witness, no dashboard, no production script. This is a research document.

**What would move if a route landed.**

- A non-zero 3-body class (A, D1) would replace the conjectural `I` in `binding = −log I` with a
  derived object and would retire the "`I` must carry irreducibly many-body structure" open item on
  `qou-brng`. The `carrier_must_break_three_to_one` acceptance test (any carrier must break
  `μ_t = 3·μ_p`) is the number it would have to hit *without being selected to*.
- The `binding-manybody-jet-filtration` conjecture would acquire a candidate identification of its
  body-order index `n` with a Hochschild / descent degree — which is exactly the *bridge* the
  2026-08-25 audit found unstated (body order = jet degree = GB depth, with three excluded readings
  of `J^•`).
- The `lifting-and-descent` chapter would become load-bearing for binding, which raises the cost of
  its 148 unverified `yekutieli2010` citations from cosmetic to structural.

**Blast radius on the Lean surface.** Mathlib has no Hochschild (co)homology, no Soergel
bimodules, no factorization homology. Every route's *theory* is a citation; only the prunes in §7
are formalisable today, and they are formalisable *because* they are elementary (idempotent
decompositions, product-of-spans lemmas, a `Fin`-indexed cocycle). The corpus's `WhiteheadHH`
class is the one existing carrier and it is currently unused by its own theorem.

**Reception.** A referee at a mathematics venue will accept "the Markov trace is `HH_0`; the
categorified trace has higher degrees; here is the one that is pairwise-trivial" as a *statement*
with a computation behind it. The same referee will reject any specialisation `(a,q,t) ↦ ℝ` chosen
to land on `b₃`. Routes A/B/C/D are publishable as structure; none is publishable as a number
without a derived specialisation rule, and that rule is the actual open problem the derived
language exposes.

---

## 7. Recommendation and ordered plan (judgement)

**Ordering principle:** prunes before constructions; held literature before acquisitions; the
route whose failure is cheapest to detect first.

1. **Prune P1 — formality bridge (F1, §2.1).** Lean, generic ring, elementary: sequential
   juxtaposition of interface words + a trace ⇒ `PairLocal` ⇒ `b₃ = 0`. Settles that the model's
   zero is forced by *two* things and tells every later route which of the two it is breaking.
   Cost: hours. Risk: none.
2. **Prune P2 — the fibre has no degrees, the tower does (route B's prune).** Replace the vacuous
   `spectral_sequence_collapses_to_centre` with an honest conditional and exhibit an `HH_1` element
   over `ℤ[q^{±1}]` at `n = 2` killed by inverting `[2]_q`. Cost: a day. This is also the fix for a
   recorded Lean defect (2026-08-25 audit §2a).
3. **Test T1 — `q`-adic order of the interleaving cross term** (route B's test). Exact algebra, one
   afternoon. Decides whether the one positive many-body signal the corpus has is an "all orders in
   `q`" object.
4. **Check C1 — kite tethering (§4.4).** One hour with the held book. Decides whether any
   2-dimensional Yekutieli object can carry `b₃`.
5. **Acquire** the six A-priority papers of §8 (links there), plus the gerbes paper regardless.
6. **Route A construction** — `P_β(a,q,t)` at `A = 2, 3` with the Künneth prune and the `t = −1`
   cross-check; report polynomials, not numbers. Frame it with route E's excision axiom.
7. **Route D1** only after the gerbes paper is held and C1 is done; **D2** only if a computed
   `γ ≠ 0`.
8. Routes C, G: the one-page lemma and the `TL_3` linear-algebra check, as idle-time work.
9. Routes F, H: closed for this arc.

**What happens if the owner does nothing.** Nothing changes. The beans stay open as a plan, no
number moves, the corpus keeps reporting `b₃ = 0` against `+1.426`. That is a safe default.

**What would change this recommendation.** If P1 fails to prove (i.e. sequential words with a
semisimple trace can be non-pair-local), the diagnosis of §2 is wrong and the many-body term is a
degree-0 word-topology object after all — in which case route C moves to the top and route A to the
bottom.

---

## 7b. The two prunes, executed (same day, owner's go) — what they proved and what they corrected

**Item 1 (F1) was already in the corpus, and I had missed it.** Corpus-grep run before writing
a line found the whole chain in three files: `QOU.MathlibExt.MonotoneWordFactorizes.tr_stabWord_eq_prod_tr`
(a monotone word's trace is the product of its letters' traces),
`QOU.Mass.MarkovBondRuleForcesPairwise.b3_eq_zero_of_bondRule` (a bond product under any
multiplicative-to-additive map gives `b₃ = b₄ = 0`), and
`QOU.MathlibExt.InterleavedCrossTerm.interleaved_sub_sequential` (the exact `n = 4` cross term
`z(z² − hz − 1)`). §2.1's F1 is therefore **proved, not conjectural**, and its statement here should
be read with one correction: **semisimplicity does no work in it.** The zero is forced by the
*ordering* of the word alone — the monotone/stabilising-letter hypothesis — with nothing about the
trace beyond the Markov axioms. What landed is the composition, so both hypotheses are visible in
one type: [`QOU/Mass/FormalityBridgeF1.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/FormalityBridgeF1.lean)
(5 declarations, `lean -DautoImplicit=false` exit 0, axioms `[propext, Classical.choice, Quot.sound]`
or none, no `sorry`): `f_tr_stabWord_eq_sum` — for any `f` with `f(xy) = f x + f y`, the `f`-image of a
monotone word's trace is the **sum** of the letters' `f`-images; `interleaved_ne_sequential` /
`f_interleaved_ne_f_sequential` — with a non-zero cross term the interleaved word's trace (and any
injective image of it) is **not** the bond sum of the same letters. So the corpus's one positive
many-body signal (`qou-kru4`) is the failure of F1's ordering hypothesis, not a counterexample to
F1; a degree-zero many-body term is word topology, and an *algebraic* one has to live where the
semisimple fibre's trace cannot see — item 2. Bean `qou-dchj`.

**Item 2 (the honest `HH_1` example) is new and is the structural content of §2 at the one `n`
where the corpus has a genuine `HeckeAlgebra` instance.**
[`QOU/Hecke/H2KaehlerDegrees.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/H2KaehlerDegrees.lean)
(8 declarations, same verification, no `sorry`). For `A_h = R[X]/(X² − hX − 1)` — the corpus's
`InstanceH2.H2` at `h = q − q⁻¹` — with `f′(x) = 2x − h`:

| declaration | statement |
|---|---|
| `two_x_sub_h_sq` | `(2x − h)² = h² + 4` in `A_h`; at the Hecke parameter `h² + 4 = (q + q⁻¹)² = [2]_q²` (`two_x_sub_h_sq_hecke`) |
| `kaehlerIdeal_eq_top_of_isUnit` | `h² + 4` a unit of `R` ⇒ `(2x − h) = A_h` ⇒ `A_h/(2x − h) = 0` — **the fibre has no degree** (every generic `q`, `kaehlerIdeal_eq_top_of_qint_ne_zero`) |
| `kaehlerIdeal_ne_top_of_hom` | a ring hom `R → K` (field, `2 ≠ 0`) with `h² + 4 ↦ 0` ⇒ `(2x − h) ≠ A_h` — **the tower has one**; for `ℤ[q^{±1}] → ℂ`, `q ↦ i` this is `HH_1(H₂/ℤ[q^{±1}]) ≠ 0`, and at a fourth root of unity directly `kaehlerIdeal_ne_top_of_fourth_root` |

**Cited, not proved:** `HH_1(A/R) ≅ Ω¹_{A/R}` for commutative `A` (HKR in degree one; Weibel
9.4.3) and `Ω¹ ≅ A/(f′)` for a monogenic algebra. Mathlib's `KaehlerDifferential` was not
exercised; there is no Hochschild framework. The file says so in its header. Scope: `n = 2` only
(`H_n` is non-commutative for `n ≥ 3`, where `HH_1 ≠ Ω¹` and the corpus has no instance). The
vacuous `QOU.WedderburnMass.centralIdempotent_idem` is left in place — its GAP note stands — and
this file complements rather than replaces it. Bean `qou-s6ff`.

**What the two together say.** The degree the derived route needs exists over `ℤ[q^{±1}]` and is
destroyed by inverting `[2]_q`; and the `b₃ = 0` of the production chain is an ordering fact the
algebra's semisimplicity does not even enter. Both halves of §2's diagnosis survive, with the
attribution corrected: *ordering* owns the degree-0 zero, *semisimplicity* owns the absence of a
higher degree. The `q`-adic-order test (§7 item 3) is unaffected and still queued.

**Verification note.** Four modules of the F1 import cone (`OcneanuTrace`, `InterleavedCrossTerm`,
`MonotoneWordFactorizes`, `MarkovBondRuleForcesPairwise`) postdate the 2026-08-31 olean cache and
were compiled from source first, all exit 0, per the "run the sweep, not bare lean-direct" rule.
`scripts/check-sidecars.sh`: both files *"library Lean — no ℝ, generic OK"*. Both modules are
registered in `QOU.lean`; the full aggregator was not rebuilt (875 imports).

## 7c. Test T1, executed (same day) — the interleaving cross term is an ORDER-ZERO object

**Claim.** The answer to route B's falsifiable test is **no**. At convention D the three traces of
§1.3 are the explicit rational functions

    S = q³ (q⁴+1)² / (q²+1)³          I = q⁵ (q⁶+q²−1) / (q²+1)³
    Δ = I − S = −q³ (q⁴+q²+1) / (q²+1)³ = −q³ Φ₃(q) Φ₆(q) / Φ₄(q)³

and their orders of vanishing at `q = 1` are all **zero**: `S(1) = 1/2`, `I(1) = 1/8`,
`Δ(1) = −3/8`. The cross term is not "strictly higher order than the sequential product"; it is
present in full at `q = 1`.

**The order-zero term has a name.** At `q = 1` with `z = 1/2` the Ocneanu trace on `ℚS₄` is the
cycle-count trace `tr(w) = 2^{c(w) − 4}`, `c(w)` the number of cycles of the underlying permutation
— the number of **components of the braid closure**. The interleaved word `s₀s₁s₀s₂s₁` closes to a
knot (`c = 1 → 1/8`); the sequential word `s₀²s₁²s₂` closes to a three-component link (`c = 3 →
1/2`). The corpus's one positive many-body signal is, at order zero, a difference of component
counts — word topology in the most classical sense, which is the attribution §7b reached from the
Lean side.

**What the `q`-deformation adds, measured.** In `ℏ = 1 − q⁻¹` the exact series is
`Δ = −3/8 − (3/4)ℏ − (17/16)ℏ² − (21/16)ℏ³ − …`, `I/S = 1/4 + (3/2)ℏ + (5/4)ℏ² − 2ℏ³ − …`, with
radius of convergence exactly `√2` (poles at `q = ±i`). At the proton pin (`ℏ ≈ 0.0991`) the
order-zero term carries **81.3 %** of `Δ(q₀) = −0.46117…`; the extra log-suppression is
`0.895` nats against the classical `2 ln 2 = 1.386` nats — the deformation *reduces* the
classical cross term's binding effect by a third, it does not create it.

**The Habiro half of route B, for this word.** The normalised traces have a **triple pole at
`Φ₄`** (`q² = −1`), so none of `S, I, Δ` is a Laurent polynomial or a Habiro element as normalised.
The pole is the normalisation `tr(1) = 1`, i.e. division by `[2]_q⁴`; the unnormalised
quantum-trace cross term `[2]_q⁴·Δ = −(q⁶+2q⁴+2q²+1)/q` **is** a Laurent polynomial, with simple
zeros at `Φ₃, Φ₄, Φ₆` and value `−6` at `q = 1` — `q`-adic order still zero. (That the pole locus
`q² = −1` is where the `H₂` Kähler ideal of §7b is proper is a coincidence of loci, recorded, not
derived.)

**Consequence for the plan (judgement).** Route B's relevance to `b₃` is **weakened** exactly as
the test said it would be: the cross term is a degree-0 / order-0 object dressed by a convergent
perturbative series, not an object that first appears at higher order in `q`. Route B keeps its
"tower has degrees the fibre lacks" content (§7b's `HH₁` example), but the many-body signal does
not live there. Routes A and C (where a *class* or a *cardinality* can be a many-body datum at
order zero) move up relative to B; nothing else in §7 changes. Scope (a): one word pair, convention
D; whether a nucleus is an interleaved word class remains `qou-5vhf`.

**Artifact.** [`computations/probes/interleaving_cross_term_q_adic_order_probe.py`](../../computations/probes/interleaving_cross_term_q_adic_order_probe.py)
(exact sympy + integer synthetic division; mpmath 50 dps for the one anchor evaluation; 15/15;
witness `interleaving-cross-term-q-adic-order.witness.json`, `q0Anchor: proton`). Bean `qou-212w`.

## 7d. Results of §7 items 4–5 — route A step 1 and route C step 1 (2026-09-06)

Both executed the day after T1, on the same word pair, exact throughout
(`computations/probes/interleaving_cross_term_closures_probe.py`, 13/13, witness
`q0Anchor: independent` — no `q₀` is read). Beans `qou-amw3`, `qou-8uxw`.

**Route A step 1 — what the two words are.** From the Ocneanu axioms alone
(`QOU/MathlibExt/InterleavedWordClosures.lean`, sorry-free, axioms standard):

    tr(s₀ s₁ s₀ s₂ s₁) = z² · tr(σ³)        interleaved = doubly-stabilised σ³   → trefoil
    tr(s₀² s₁² s₂)     = z  · tr(σ²)²       sequential  = stabilised Hopf-chain → three components
    Δ                  = z² · tr(σ³) − z · tr(σ²)²                                (`crossTerm_eq_closures`)

with `z` and `h` free, i.e. at the two-variable (HOMFLY-PT) level, and confirmed in the 16-dim
spin-½ representation. So the "cross term" is the difference of two link invariants of two
**different** links. Verdict on "is `Δ` an Euler characteristic": true only in the content-free
sense — each side is the graded Euler characteristic of a Khovanov–Rozansky homology, so `Δ` is
`χ` of a shifted direct sum. The sense that would matter — a natural chain map between the two
complexes whose cone carries `Δ` — is supplied by nothing in the corpus: the closures have
different component counts and no braid move relates the words. Route A's honest step 2 is to
construct such a map (a cobordism map: two saddles join the three components into one) and
compute its cone; not attempted here.

**Route C step 1 — what the order-zero term counts.** At `q = 1` with `z = 1/N` the Markov trace
on `ℚSₙ` is the normalised character of `Sₙ` on `V^{⊗n}`, `dim V = N`: `N^{c(w)}/N^n`. The
character of a permutation representation is a Burnside fixed-point count — the `w`-invariant
colourings of the strands, which are exactly the colourings constant on each cycle. Verified on all
24 permutations of `S₄` at `N = 2, 3`. The interleaved word fixes 2 two-colourings, the sequential
word 8; the difference `−6` is T1's `[2]_q⁴·Δ|_{q=1}`. Both counts are pinned in Lean by finite
search (`QOU/Mass/CrossTermFixedPointCount.lean`, `decide` on 16 colourings — the one place that
tactic is the honest tool). In groupoidification (Baez–Hoffnung–Walker) that character is the
degroupoidified span `X ← X^w → X`, so **the order-zero cross term is a groupoid cardinality**.
The 16-dim quantum trace degenerates to exactly this count at `q = 1` (the R-matrix becomes the
swap), so the `q`-deformation is a `q`-count of fixed points. Whether *that* is a groupoid
cardinality — the Hecke-algebra-as-groupoid-algebra reading, which lives over `𝔽_q` with `q` a
prime power, while the framework's `q₀ ≈ 1.11` is not — is route C's step 2, open.

**Net effect on the recommendation.** T1 (§7c) moved the cross term to order zero; 7d names the
order-zero object twice over — as trefoil-minus-chain (A) and as a fixed-point-count difference
(C) — and both readings agree that the classical part is *topology of the closure*, not
algebra of the tower. Route C is the one with a positive, exact foothold; route A has an
identification and a named gap. Neither has yet produced anything about `b₃`, and §7's honest
statement stands: the many-body term the binding gap needs is not visible in this word pair
beyond its component count.

## 7e. Check C1, route G's prune, and what that does to route D (2026-09-06)

**C1 — kite tethering (bean `qou-20bk`). Decided from the held definitions, and my §4.4 reason was
wrong while the conclusion survives, sharpened.** Read: Def. 4.1.1 (a kite is a string `σ` from the
basepoint plus a linear square `τ`), Def. 4.3.3 (the basic Riemann product is
`exp_H(area · Ψ_h(g)(β̃(z)))` with `g` the 1-dimensional integral along the tether and a probe into
the cell), Def. 4.3.6 / 4.2.7 (the refined product is the ordered product over the `4^k` kites of the
binary tessellation), Def. 4.4.16 (`MI` is the limit), Thm 0.4.2 (2-dim Stokes:
`Φ(MI(α,β|σ,τ)) = MI(α|∂(σ,τ))`), Thm 0.9.1 (`Ψ(g) = Ad_H(h)`), §0.5 (`H₀ = ker Φ` is the inertia
subgroup, central and abelian), Def. 8.6.1 (`γ = dβ + ψ_h(α)(β)`), Lemma 8.6.3
(`MI(α,β|∂balloon) ∈ H₀`), Thm 8.6.6 (`γ` is inert; `MI(α,β|∂(σ,τ)) = MI(α,γ|τ)`).

The tether is a basepoint gauge choice and is **not** what makes the object pair-local. The
mechanism is the 2-dimensional Stokes theorem together with the Peiffer identity: for a
connection–curvature (fake-flat) pair the surface holonomy `h ∈ H` is determined by its boundary
path holonomy `g = Φ(h)` **up to `ker Φ`, and `ker Φ` is central**. That algebra is now in Lean over
arbitrary groups (`QOU/LiftingDescent/CrossedModuleSurfaceHolonomy.lean`, sorry-free, axioms
standard: `ker_le_center`, `eq_mul_center_of_feedback_eq`, `classFn_factors_through_feedback`).
Read back into the geometry:

1. the **non-abelian** content of any 2-dimensional Yekutieli object is its boundary 1-holonomy — a
   path-ordered product, i.e. *word/ordering* data, the degree-0 class §7b–7d characterised;
2. everything beyond it is abelian (inert), and over a closed surface it is the **abelian volume
   integral of the inert 3-curvature `γ`** over the 3-cell (Thm 8.6.6), additive over 3-cells.

So **no 2-dimensional Yekutieli object carries a non-abelian 3-body term**, and the only
3-body-shaped object in the book is `∫γ` over a balloon: abelian, extensive, additive over triples —
exactly the "super-pairwise additive extensive object" the Δ_λ audit asks for. It is live **iff**
`γ ≠ 0` for the framework's connection, and that cannot be evaluated: Step 2's curvature is
stipulated, not a form; no `α`, `β` exist in the Lean (cheat-sheet §2a). Route D2's decisive check is
therefore "construct `(α, β)` as forms on the brane tower and compute `γ`", which is Step 2 itself.
Route D1's Lean prune (ii) is vacuous as I stated it: in the alternating Čech complex a 2-object cover
has `C² = 0`, so every `H²` class is "pairwise trivial" by definition; the content is whether
`κ_n ≠ 0` for the tower, which needs the tower's transition data, which the corpus does not hold as
values (grep for a computed `cl²` / `κ_n`: none).

**Route G — prune (bean `qou-fvsq`), scope (b) with the invariant cited.** The question was whether a
3-input planar tangle on `TL₃(q)` could be an irreducibly ternary operation. It cannot, before any
Temperley–Lieb relation is used: Jones states (held, `library/arxiv-math-9909027v1`, §0, the
paragraph introducing Prop. 1.20) that *"the planar operad `P` is generated by the Temperley-Lieb
algebra and tangles of two kinds"* — the multiplication tangle (two input discs) and the annular
tangles (one input disc); the figure naming the two kinds is not in the held text, the sentence is.
An operad generated by elements of arity `≤ 2` has every `k`-input element as an iterated composite
of `≤ 2`-input ones, so a 3-box tangle is a composite of 2-box and 1-box tangles as a *tangle*, and
its evaluation on any planar algebra, `TL₃` included, factors accordingly. No finite linear-algebra
check is needed and none was run. Route G is closed for this arc.

**Net effect.** Routes B, D (2-dim), G are now pruned; route D survives only as D2's `∫γ`, which is
the right *shape* and is blocked on Step 2. Route A has its identification and a named gap (a
cobordism chain map); route C has an exact foothold at `q = 1` and an open `q`-deformation. Routes E
(factorization homology: extensivity as an axiom) and H (`K₃^{ind}`) have not been touched today.

## 8. Literature to download — prioritised, with links and one-line justification

**Priority A — likely to change what can be *proved***

| # | work | link | justification |
|---|---|---|---|
| 1 | Ayala–Francis–Tanaka, *Factorization homology of stratified spaces* | [arXiv:1409.0848](https://arxiv.org/abs/1409.0848) | constructs link-homology-valued invariants of 1-submanifolds of 3-manifolds that are extensive and non-pair-local **by axiom** — the target object, already built |
| 2 | Ginot–Tradler–Zeinalian, *Derived higher Hochschild homology, topological chiral homology and factorization algebras* | [arXiv:1011.6483](https://arxiv.org/abs/1011.6483) | proves higher Hochschild = factorization homology; collapses routes A and E into one |
| 3 | Khovanov, *Triply-graded link homology and Hochschild homology of Soergel bimodules* | [arXiv:math/0510265](https://arxiv.org/abs/math/0510265) | the Markov trace is the Euler characteristic of `HH_*` of the Hecke category |
| 4 | Ben-Zvi–Nadler, *The character theory of a complex group* | [arXiv:0904.1247](https://arxiv.org/abs/0904.1247) | the Hecke category is 2-dualizable Calabi–Yau; its categorical trace is computed — the licence to evaluate the tower on surfaces |
| 5 | Baez–Hoffnung–Walker, *Groupoidification* (HDA VII) | [arXiv:0908.4305](https://arxiv.org/abs/0908.4305) | `H_n(q)` itself as spans of flag groupoids; a many-body term as a class on a configuration groupoid |
| 6 | ~~**Yekutieli, *Central Extensions of Gerbes***~~ — **HELD (ingested this session)** | [arXiv:0801.0083](https://arxiv.org/abs/0801.0083) | was: cited in 148 corpus files by theorem number and not held. Now held; the citations fail on number (§9) |
| 7 | ~~Yekutieli, *Combinatorial Descent Data for Gerbes*~~ — **HELD (ingested this session)** | [arXiv:1109.1919](https://arxiv.org/abs/1109.1919) | descent data in cosimplicial crossed groupoids — the corpus's own object; degree-`≥2` data = irreducibly higher-body datum |
| 8 | Ayala–Francis, *Factorization homology of topological manifolds* | [arXiv:1206.5522](https://arxiv.org/abs/1206.5522) | the axioms are a finite decision procedure for a candidate binding functional |
| 9 | Schreiber–Waldorf, *Connections on non-abelian gerbes and their holonomy* | [arXiv:0808.1923](https://arxiv.org/abs/0808.1923) | gluing axioms for surface transport: the sharpest tool for auditing what Yekutieli's tethered kite discards (§4.4) |
| 10 | Webster–Williamson, *A geometric model for Hochschild homology of Soergel bimodules* | [arXiv:0707.2003](https://arxiv.org/abs/0707.2003) | type-A `HH_*` as an exterior algebra with explicit Hilbert series — the higher degrees become calculable (companion to the held *Geometry of Markov traces*) |
| 11 | Gorsky–Neguț–Rasmussen, *Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology* | [arXiv:1608.07308](https://arxiv.org/abs/1608.07308) | `HH_*` of an `n`-strand braid as sheaf cohomology — the only route with a chance of reaching `n = 3A` |
| 12 | Elias–Williamson, *Soergel calculus* | [arXiv:1309.0865](https://arxiv.org/abs/1309.0865) | the finite diagrammatic presentation without which nothing in route A is computable |

**Priority B — reframing, cross-checks, and the rest of Yekutieli**

| # | work | link | justification |
|---|---|---|---|
| 13 | Ben-Zvi–Nadler, *Nonlinear traces* | [arXiv:1305.7175](https://arxiv.org/abs/1305.7175) | the general theory of "what a trace is once you refuse to decategorify"; joins routes A and C via spans |
| 14 | Rouquier, *Categorification of the braid groups* | [arXiv:math/0409593](https://arxiv.org/abs/math/0409593) | how a braid word enters the categorified picture |
| 15 | Khovanov–Rozansky, *Matrix factorizations and link homology II* | [arXiv:math/0505056](https://arxiv.org/abs/math/0505056) | the original HOMFLY-PT homology |
| 16 | Oblomkov–Rozansky, *Knot homology and sheaves on the Hilbert scheme of points on the plane* | [arXiv:1608.03227](https://arxiv.org/abs/1608.03227) | independent geometric model; cross-check for any `HH_*` computation |
| 17 | Yekutieli, *MC elements in pronilpotent DG Lie algebras* (`yekutieli2009`, 12 citing files, **still not held**) | [arXiv:1103.1035](https://arxiv.org/abs/1103.1035) | the Deligne 2-groupoid; the hinge between the two halves of his work; cited by 12 files, not held |
| 18 | Yekutieli, *Twisted deformation quantization* (survey `yekutieli2008`, 22 citing files, **still not held**; then the paper — the likely true home of the corpus's "Thm 4.5" citation) | [arXiv:0801.3233](https://arxiv.org/abs/0801.3233), [arXiv:0905.0488](https://arxiv.org/abs/0905.0488) | the "stack-like deformation" the `direct-limit-algebra` blocks describe; cited by 22 files, not held |
| 19 | Yekutieli, *Rigidity, residues and duality: overview* | [arXiv:2102.00255](https://arxiv.org/abs/2102.00255) | the cheapest way to close the derived half |
| 20 | Baez–Dolan, *From finite sets to Feynman diagrams* | [arXiv:math/0004133](https://arxiv.org/abs/math/0004133) | groupoid cardinality, short |
| 21 | Morton, *2-vector spaces and groupoids*; *Categorified algebra and quantum mechanics* | [arXiv:0810.2361](https://arxiv.org/abs/0810.2361), [arXiv:math/0601458](https://arxiv.org/abs/math/0601458) | linearisation of spans; the many-particle worked example |
| 22 | Nikshych–Vainerman, *Finite quantum groupoids and their applications* (survey) | [arXiv:math/0006057](https://arxiv.org/abs/math/0006057) | non-multiplicative traces on a tower-like object, rigorously |
| 23 | Jones, *Planar algebras I* | [arXiv:math/9909027](https://arxiv.org/abs/math/9909027) | irreducibly `n`-ary operations on the Bratteli tower |
| 24 | Venkatesh, *Derived Hecke algebra and cohomology of arithmetic groups* | [arXiv:1608.07234](https://arxiv.org/abs/1608.07234) | the structural idea only: a graded algebra whose degree 0 is the classical Hecke algebra |
| 25 | Bezrukavnikov–Finkelberg, *Equivariant Satake category and Kostant–Whittaker reduction* | [arXiv:0707.3799](https://arxiv.org/abs/0707.3799) | type case of "the derived version of a monoidal category has strictly more structure"; loop rotation ≈ deformation parameter |
| 26 | Habiro, *Cyclotomic completions of polynomial rings* | [arXiv:math/0209324](https://arxiv.org/abs/math/0209324) | the Habiro ring itself (route B) |
| 27 | Martins–Picken, *On two-dimensional holonomy* | TAMS 362 (2010) 5657–5695; arXiv id [0710.4310](https://arxiv.org/abs/0710.4310) **unverified** | the independent thin-homotopy construction of the same 2-holonomy as Yekutieli's MI |
| 28 | Pirashvili, *Hodge decomposition for higher order Hochschild homology* | [DOI 10.1016/s0012-9593(00)00107-5](https://doi.org/10.1016/s0012-9593(00)00107-5) (no arXiv) | the canonical indexing of higher Hochschild pieces |
| 29 | Costello–Gwilliam, *Factorization algebras in QFT* vol. 1 | CUP 2017, ISBN 9781107163102 (book) | chapters 1–3, 6: the factorization axiom as the formalisation of "observables on disjoint regions multiply" |
| 30 | Beilinson–Drinfeld, *Chiral algebras* | AMS Colloq. Publ. 51 (2004) (book) | the Ran space: the one object here about *varying* particle number |

**Priority C** (not recommended for this arc; listed for completeness): Yekutieli's derived papers
(§4.3 links); Galatius–Venkatesh [arXiv:1608.07236](https://arxiv.org/abs/1608.07236);
Ben-Zvi–Sakellaridis–Venkatesh [arXiv:2409.04677](https://arxiv.org/abs/2409.04677);
Crainic–Fernandes [arXiv:math/0105033](https://arxiv.org/abs/math/0105033); PTVV shifted symplectic
[arXiv:1111.3209](https://arxiv.org/abs/1111.3209); Andersen–Kashaev
[arXiv:1109.6295](https://arxiv.org/abs/1109.6295); Toën–Vezzosi
[arXiv:0903.3292](https://arxiv.org/abs/0903.3292); Hoyois–Scherotzke–Sibilla
[arXiv:1511.03589](https://arxiv.org/abs/1511.03589).

**Already held — read these first, they cost nothing:** Solleveld `arxiv-1108.5286v3`;
Webster–Williamson `arxiv-0911.4494v2`; the Yekutieli book `arxiv-1007.1250v4` §§5, 7, 8;
Nikolaus–Waldorf `arxiv-1103.4815v3`; Baez–Huerta `arxiv-1003.4485v2`; Geck–Rouquier `centsim`
(use the `ocr/` tier); `arxiv-1202.5547v1`; `arxiv-2507.19896v1`.

---

## 8b. Addendum (same session, later): eleven more papers ingested — every priority-A item is now held

The owner uploaded eleven PDFs in `8a730706` (root of the repo), and they are ingested on this
branch with `references.ts` joins (`--check` clean; the file loads, 838 entries, no duplicate ids):

| doc-id | work | §8 row | candidates |
|---|---|---|---|
| `arxiv-1409.0848v3` | Ayala–Francis–Tanaka, *Factorization homology of stratified spaces* | 1 | 76 |
| `arxiv-1011.6483v3` | Ginot–Tradler–Zeinalian, *Derived higher Hochschild homology…* | 2 | 91 |
| `arxiv-math-0510265v3` | Khovanov, *Triply-graded link homology and HH of Soergel bimodules* | 3 | 9 |
| `arxiv-0904.1247v3` | Ben-Zvi–Nadler, *The character theory of a complex group* | 4 | 61 |
| `arxiv-0908.4305v3` | Baez–Hoffnung–Walker, *Groupoidification* | 5 | 39 |
| `arxiv-0808.1923v3` | Schreiber–Waldorf, *Connections on non-abelian gerbes and their holonomy* | 9 | 45 |
| `arxiv-0707.2003v2` | Webster–Williamson, *A geometric model for HH of Soergel bimodules* | 10 | 22 |
| `arxiv-1309.0865v1` | Elias–Williamson, *Soergel calculus* | 12 | 95 |
| `arxiv-1103.1035v4` | Yekutieli, *MC elements in pronilpotent DG Lie algebras* (`yekutieli2009`, 12 citing files — now checkable) | 17 | 41 |
| `arxiv-0801.3233v4` | Yekutieli, *Twisted deformation quantization* (survey; `yekutieli2008`, 22 citing files — now checkable; the likely home of the mis-keyed "Thm 4.5") | 18 | 23 |
| `arxiv-2102.00255v1` | Yekutieli, *Rigidity, residues and duality: overview* | 19 | 51 |

With these, **routes A, C, D and E all have their primary sources in the library**, and every
Yekutieli work the corpus cites by key (`yekutieli2008/2009/2010/2015`) is held. Still not held
from §8: rows 8 (Ayala–Francis 2012), 11 (Gorsky–Neguț–Rasmussen), 13–16, 20–30 — none blocking.
The "held nothing on factorization homology / Ben-Zvi" statement in §3.2 is superseded by this
table. **Nothing in §§5–7 changes:** the prunes come before the reading, and the reading is now
possible.

### 8c. Second addendum: twenty more (owner upload `a7d6a3b5`) — §8 is now held in full except the two books and Pirashvili

All ingested with `references.ts` joins (`--check` clean; the array loads; no duplicate ids):

| §8 row | doc-id | work |
|---|---|---|
| 8 | `arxiv-1206.5522v6` | Ayala–Francis, *Factorization homology of topological manifolds* |
| 11 | `arxiv-1608.07308v1` | Gorsky–Neguț–Rasmussen, *Flag Hilbert schemes…* |
| 13 | `arxiv-1305.7175v4` | Ben-Zvi–Nadler, *Nonlinear traces* |
| 15 | `arxiv-math-0505056v2` | Khovanov–Rozansky, *Matrix factorizations and link homology II* |
| 16 | `arxiv-1608.03227v4` | Oblomkov–Rozansky (title parsed as a date by `pdf-structure`; supplied by hand in `references.ts`) |
| 18 (paper) | `arxiv-0905.0488v5` | Yekutieli, *Twisted deformation quantization of algebraic varieties* — full paper; the survey is `arxiv-0801.3233v4` |
| 20 | `arxiv-math-0004133v1` | Baez–Dolan, *From finite sets to Feynman diagrams* (0 extractor candidates — expository) |
| 21 | `arxiv-0810.2361v2`, `arxiv-math-0601458v1` | Morton ×2 |
| 22 | `arxiv-math-0006057v2` | Nikshych–Vainerman survey |
| 23 | `arxiv-math-9909027v1` | Jones, *Planar algebras I* (122 pp) |
| 27 | `arxiv-0710.4310v2` | Martins–Picken — **arXiv id now verified from the PDF**; the §9 "unverified" flag is closed |
| §4.3 derived half | `arxiv-1610.09640v4` (459 pp, 852 candidates), `arxiv-1412.4229v4`, `arxiv-1312.6411v4`, `arxiv-math-9804005v3`, `arxiv-1010.4386v5`, `arxiv-1606.01832v3`, `arxiv-2002.04901v5` | Yekutieli: *Derived Categories*; squaring; duality and tilting; (with Zhang) Auslander dualizing complexes; completion/torsion; flatness and completion; weak proregularity |
| C-list | `arxiv-math-9805116v3` | Böhm–Nill–Szlachányi, *Weak Hopf algebras I* |

**Not held from §8 after this:** row 14 (Rouquier, `math/0409593`), 24–26 (Venkatesh; Bezrukavnikov–Finkelberg; Habiro cyclotomic completions), 28 (Pirashvili, no arXiv), 29–30 (the Costello–Gwilliam and Beilinson–Drinfeld books), and the C-list items. None blocks a route. **Every Yekutieli work named in §4.3 is now held**, so the "read the 2021 overview instead of the four derived papers" advice in route F is moot — the papers are here; the judgement that the derived half carries no trace-on-a-tower theorem stands until someone reads them against that question.

### 8d. Third addendum: the last four arXiv items (owner upload `783c4cf4`) — §8 is now held in full except Pirashvili and the two books

~~`arxiv-math-0209324v1` Habiro~~ — **was ALREADY HELD** (`library/arxiv-math-0209324v1`, ref `habiro2004cyclotomic`); the "not held" in §8 row 26 and §8b/§8c was a lexical miss of mine (the INDEX row carries the title, not the author, and I grepped the author). The owner's re-upload was byte-identical and was dropped rather than ingested twice;
`arxiv-math-0409593v1` Rouquier, *Categorification of sl₂ and braid groups* (row 14; the Rouquier complexes);
`arxiv-0707.3799v3` Bezrukavnikov–Finkelberg, *Equivariant Satake category and Kostant–Whittaker reduction* (row 25);
`arxiv-1608.07234v3` Venkatesh, *Derived Hecke algebra and cohomology of arithmetic groups* (row 24).
All with `references.ts` joins, sync clean. **Remaining unheld from §8:** Pirashvili (no arXiv),
Costello–Gwilliam, Beilinson–Drinfeld — books; nothing on the list blocks any route.

## 9. Verification limits and hygiene items found on the way

- **Direct `arxiv.org` fetch is proxy-blocked** for both `curl` and `WebFetch` this session; every
  arXiv id above was confirmed from search-listing pages showing the `arxiv.org/abs/<id>` URL beside
  a matching title and author. Ids of the form `math/NNNNNNN` are the likeliest to be mistranscribed.
  The one flagged unverified is Martins–Picken.
- **`corpus_search` (path 0) unavailable** (`paper-assistant` MCP: `ENOENT`). All corpus absences in
  this document are lexical.
- **`library/INDEX.md` is stale by one row** (`ant-v14-n7-s`, no `summary.json`); fix is
  `python3 scripts/summarize-library.py --apply`. Not done on this branch (out of scope).
- **`library/arxiv-1007.1250v4`** holds an 11-chapter book in two section files, the entire body in
  `sec-000-0-introduction.md`. Text is complete; the TOC in `structure.json` is correct. A reader
  checking the section list will think it is a stub.
- **`library/centsim`** (Geck–Rouquier) is 98 % `ocr/`-tier; invisible to the documented path-5
  `sections/` grep. Same class as the Moffatt–Ricca case AGENTS.md records.
- **Ingested this session (owner upload `ad60e3f2`):** `library/arxiv-0801.0083v4`,
  `library/arxiv-1109.1919v3`, `library/arxiv-math-0505170v2` — Stage A (`pdf-structure.py`),
  Stage B (`extract-candidates.py`: 43 / 16 / 14 candidates), moved by hand rather than by
  `migrate-uploads-to-library.py --apply` (whose blanket pass would also have swept 28 unrelated raw
  PDFs still sitting in `uploads/`), `summarize-library.py --apply` (three new `INDEX.md` rows;
  idempotent on the rest), and `sync-references-library.py --apply` with `PDF library/<id>/<file>`
  possession markers in the notes so the joins are regenerated by the script rather than
  hand-typed. The sync also filled one unrelated stale join (`9511222v1`) — kept, it is the
  script's own output.
- **🛑 Dangling theorem numbers in the `yekutieli2010` citations.** The corpus cites *Central
  Extensions of Gerbes* as `Thm 1.7` (recursive brane tower ↔ central extension; twisted Čech
  cocycle), `§3` (obstruction classes), `Thm 3.4` (twisted sectors), `Thm 4.5` (twisted quantization
  map) — 148 files, canonical carrier
  [`yekutieli-mapping-table.md`](../../content/quantum-observable-universe/lifting-and-descent/yekutieli-mapping-table.md).
  Checked against the held text: the paper's numbered theorems are **3.13, 4.6, 4.17, 5.11, 6.10**
  (plus Prop. 3.4, Thm 0.1 as the introduction's summary). There is no Theorem 1.7, no Theorem 3.4
  and no Theorem 4.5. The obstruction results the corpus means are **Thm 4.6** (lifting
  isomorphisms, class `cl¹`) and **Thm 4.17** (lifting objects, class `cl²` of Def. 4.15), with
  existence under `N`-acyclic coverings in **Thm 5.11** and the pronilpotent case in **Thm 6.10**;
  "twisted quantization map on algebraic varieties" is not in this paper and is presumably in
  `0905.0488`. Recorded on bean `qou-3pck`; **not fixed here** — the mapping-table block is a content
  block and the fix is a one-block edit plus a sweep of the theorem-number strings, which is a
  separate tranche.

  **🛑 CORRECTED 2026-09-06 (bean `qou-smw9`, the sweep that fixed it).** Three claims in the bullet
  above were mine and wrong, and the sweep measured all three. (i) **Which paper.** The theorem
  numbers 3.13 / 4.6 / 4.17 / 5.11 / 6.10 are those of *Central Extensions of Gerbes*
  (`library/arxiv-0801.0083v4/`, the file `yekutieli2010` is joined to), **not** of the
  multiplicative-integration book `arxiv-1007.1250v4` (`yekutieli2015`, numbered 0.1 … 9.3). The
  numbers were right; the attribution in this bullet and in bean `qou-3pck` was to the wrong file.
  (ii) **"148 files."** That counted every mention of the key. Measured: **104** files name
  `yekutieli2010` (94 `content/`, 6 `docs/`, 4 `.beans/`), and only **10** non-record files carried a
  nonexistent theorem number. (iii) **"Prop. 3.4, Thm 0.1."** Neither is the paper's own: the only
  `Proposition 3.4` is `[Gr2, Corollaire to Proposition 3.4.2]` and the only `Theorem 0.1` is
  `[Ye, Theorem 0.1]`, both citations to other works. **Fixed on PR #6891** (`507aa3c560`):
  Thm 1.7 → **Thm 4.17** (lifting objects, class `cl²` of Def. 4.15); Thm 3.4 (twisted sectors)
  → **Thm 4.17**; the central-extension tower → **Thm 3.13 + §6**; "§3 obstruction classes" →
  **§4, Def. 4.15**; and the "twisted quantization map" → **`yekutieli2015-twisted-dq`
  Thm 0.10.1** (arXiv 0905.0488, verified in its held text), with `cites[]` extended on the two
  carrier blocks. **Still dangling, deliberately untouched** (recorded on `qou-cqs9`): `Theorem 4.2`
  ×3 and `Definition 2.1` ×5 on the cosimplicial-crossed-groupoid carriers, and `Theorem 1.1` in
  `weak-equiv-invariance-proof.md` — none exists in 0801.0083; the likely home is
  `arxiv-1109.1919v3` (*Combinatorial Descent Data*), which needs its own verification. This
  correction also invalidates the "148 unverified citations" cost quoted under route D above.
- The Lean carrier `QOU.WedderburnMass.spectral_sequence_collapses_to_centre` proves idempotence
  and never uses its `[WhiteheadHH]` instance (2026-08-25 audit §2a); it is not in the vacuity
  ledger. §7 item 2 is the fix.

## 10. Sibling coordination

Open PRs at the time of writing that touch adjacent scope, none on this route: #6815 (Route E,
PGL(3) — flavour arc), #6821 (two atomic braids, one name — the mass law's carrier), #6826 (Φ_k is
not a trace). No file overlap; no intent comment posted. This branch touches one new file.
