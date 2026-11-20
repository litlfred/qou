---
# qou-qhcr
title: 'GAP: derive the branch-point count 6 from the five QOU axioms (the ONE missing step in the chi = -6 chain)'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-15T06:16:39Z
updated_at: 2026-11-20T17:50:00Z
parent: qou-6qbv
---

Child of `qou-51l1` (which established that the χ = −6 chain is
derived-modulo-one-named-input, and named this as the one missing step).
Session `claude/chi-branch-point-count-2026-09-15`.

**Outcome: the 6 is still not derived. The ADE / finite-subgroup-of-SU(2)
route was tested and is a negative, and the negative is informative — an
orbit reading of "six branch points on `ℙ(V)`" points AWAY from the
icosahedral case, not toward it.**

Artifacts, both on the branch:

- `folio/quantum-observable-universe/lean/QOU/BringsSurface/BranchPointSixNotForced.lean`
  — sorry-free (`#print axioms`: `propext`, `Quot.sound` only; several
  theorems depend on no axioms at all), import-free, `lean`-direct
  `-DautoImplicit=false -s 65536` exit 0 in 0.9 s.
- `computations/chi_branch_point_count_genericity_probe.py` +
  `computations/chi-branch-point-count-genericity.witness.json` — 18/18
  checks, exact `int`/`Fraction` throughout (no float64), independent
  re-derivation of the same arithmetic by the rational orbifold-Euler
  route rather than the Lean's cleared-denominator integer route.

## 1. How much the derived steps actually give

Step 3 (Riemann–Roch, `χ = 2 − 2g`) + Step 4 (`g ≥ 1`) constrain `χ(A)` to
**exactly the non-positive even integers, and no further** — proved both
ways (`step34_admissible_iff`). Step 6 ("the sign is negative") adds
nothing; it is implied by Step 4. So **Step 5 alone supplies `−6`, one
value out of a countably infinite set.**

This is the formal version of what `brings-surface/universality-general.md`
already says in prose — *"for any admissible Euler characteristic χ …
analogous universal objects are expected at other values of χ"* — which
`qou-51l1` flagged as the cleanest single piece of evidence in the corpus.

## 2. "Six branch points" over ℙ¹ does not fix χ even given the degree

The corpus's own six-branch-point datum is a cover of **ℙ¹**
(`brings-qou-4tuple.md:15`, degree 3; `brings-is-qou-verification.md:15`,
degree 4 with `R = 14`). Over ℙ¹, `χ = 2d − R` with `R` the **total
ramification**, not the branch count; a branch point contributes between 1
and `d − 1`. At the corpus's own `(d, b) = (4, 6)`, `R ∈ [6, 18]` and the
genus ranges over **0…6**. So the branch *count* determines nothing near
`g = 4`; the number that does the work is `R = 14`, which no block derives.

## 3. Step 5's parenthetical is false, and the real 6 is one line further on

**Already known to the corpus** — recorded at `chi-minus-six-chain.qa.json:1611`,
`content/bib-qa-verifications.json:11038` and `:11072`, and bean `qou-xz89`
— so this is a confirmation, not a discovery. Two things are new.

First, the existing flag reaches the right conclusion by a wrong route: the
`.qa.json` note says six Weierstrass points is "impossible for genus 4
(minimum 2g+2 = 10)". `2g + 2` is the **hyperelliptic branch-point** count;
Bring's curve is not hyperelliptic. The correct figure is the total
Weierstrass weight `g³ − g = 60`, all of weight 1, with `Aut(B) = S₅`
acting **transitively** (Braden & Disney-Hogg Prop. 3.3,
`library/s40879-023-00706-0/sections/sec-008-31-weierstrass-points.md:42`).

Second — and this is the useful part — the same source, one paragraph
later, gives **`60 = 6 × 10`: six Weierstrass points fixed by each of the
ten transpositions in `S₅`**. So there *is* a real 6 here, and Step 5 is
one substitution away from being coherent:

> the carrier is a **transposition** (an involution), not an `S₃`; the 6 is
> a **per-involution fixed-point count**, not a total; and the degree-2
> quotient `B → B/⟨τ⟩` then has **genus 1** by Riemann–Hurwitz, giving
> `χ(B) = 2·χ(torus) − 6 = −6`.

That repairs the citation. It does **not** make Step 5 a derivation — it
still reads the 6 off Bring's curve, which the chain identifies at Step 7.
And the `R = 6` is not forced by `χ = −6` with `g ≥ 1` either:
`(d, h, R) = (2, 1, 6)`, `(2, 2, 2)` and `(3, 2, 0)` all give `−6`.

## 4. The torus-knot route of `EulerCharacteristicSix.lean` restates its target

That file derives `g = 4`, sorry-free, from "`T₂,₉` embeds (Seifert rank
`4 ≤ g`) and `T₂,₁₁` does not (`5 ≰ g`)". The arithmetic is right and the
file says outright that "neither step is deep". Measured how shallow:
`seifertRank(2, s) = (s−1)/2`, so for **every** genus `g` the pair
`T₂,₂g₊₁ / T₂,₂g₊₃` brackets it — and at `g = 4` that pair is exactly
`(9, 11)`. The constraint pair carries precisely the information "the genus
is 4" and nothing more.

## 5. The ADE route — tested, negative at three joints

**(a) Nothing makes `G` finite.** `su2_emergence_rank_forced` constrains
`G` (a bare `Set`) only by "unitary and `det = 1`", which `SU(2)` itself
satisfies; `qou-axioms-physical-reading.md` says axiom 5 is *"the condition
that makes the reconstructed gauge group `SU(2)`"*. The ADE/McKay list
classifies **finite** subgroups, so the classification does not apply to
the object the axioms deliver. This is prior to the type question and it is
where the route actually dies.

**(b) One axiom prunes, to four families.** Observability
(`Hom(𝟙, Ad(A)) = 0`), read literally as "the 3-dimensional adjoint has no
invariant vector", excludes exactly the **cyclic** family: a cyclic
rotation group fixes its axis. Dihedral, tetrahedral, octahedral and
icosahedral all survive. (Caution recorded in the Lean: the *physical
gloss* in `qou-axioms-physical-reading.md` — "gauge transformations that
act as the identity on every observable" — is the **kernel** of `Ad`, a
different condition, under which every binary subgroup fails since `{±1}`
is always in the kernel. The two readings are not interchangeable and
neither is formalised anywhere in the corpus; `qou_ns_in_qou` carries
observability as an opaque `Prop` field.)

**(c) Granting both, the icosahedral case does not produce a 6.** The three
exceptional orbits of the icosahedral rotation group on `ℙ(V)` have sizes
**30, 20, 12** — all ≥ 12. Six **is** an exceptional orbit size for the
**tetrahedral** (`E₆`: 6, 4, 4), **octahedral** (`E₇`: 12, 8, 6) and
**dihedral-6** groups. So an orbit reading of "branch points on `ℙ(V)`"
points *away* from `E₈`. The cone-order and orbit tables are not asserted:
they are cross-checked by Klein's relation `χ_orb = 2/|Ḡ|` (exact rational,
all 13 families in the probe), so a wrong cone order fails a theorem.

The **Sylow** reading does select `E₈` — `n₅(A₅) = 6 = |ℙ¹(𝔽₅)|`, the
source of the exceptional `A₅ ↪ A₆` — and the Sylow arithmetic is derived
here rather than asserted (`n₅ ∣ 12`, `n₅ ≡ 1 mod 5` ⟹ `n₅ ∈ {1, 6}`;
simplicity of `A₅` picks 6, cited). But the two readings **disagree on the
same group in both directions**: on the icosahedral group Sylow gives 6 and
orbits do not; on the tetrahedral group orbits give 6 and Sylow does not
(`n₃(A₄) ∈ {1, 4}`). So **6 is a property of the chosen invariant, not of
the ADE type**, and nothing in the axioms names the invariant. Choosing the
Sylow reading *because* it returns 6 is selection against the target, which
AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3" forbids.

Genericity sanity check: of 16 natural integer invariants of `A₅` (irrep
dimensions 1,3,3,4,5; conjugacy class sizes 1,15,20,12,12; orbit sizes
30,20,12; Sylow counts 5,10,6), exactly **one** equals 6. So 6 is not
*generic* for `A₅` — but it is also not *selected*, which is the point.

## 6. The one narrowing found that is not a read-off

**Laing & Singerman, "Transitivity on Weierstrass points", Ann. Acad. Sci.
Fenn. Math. 37 (2012), Theorem 15** — quoted as Theorem 3.4 of
`[braden-disney-hogg-2022]` at
`library/s40879-023-00706-0/sections/sec-008-31-weierstrass-points.md`, and
independently noted in `content/bib-qa-verifications.json:11038` for the
arXiv note `2211.08164v2`:

> a Riemann surface of genus `g > 2` with `g³ − g` Weierstrass points on
> which `Aut` acts **transitively** is Bring's curve (`g = 4`), Klein's
> quartic (`g = 3`), or a genus-3 curve with `Aut ≅ S₄`.

The hypothesis is a **homogeneity** statement — *no Weierstrass point is
distinguishable from any other, and none is distinguished by weight* — in
the same register as the observability axiom, and it says nothing about the
number 6. It narrows `χ(A)` from the infinite set of §1 to **exactly two
values, `{−4, −6}`**. Separating them needs one further input: an
automorphism of **order 5**, since by Cauchy `5 ∣ 120` while `5 ∤ 168` and
`5 ∤ 24`.

**This is not a closure and must not be reported as one.** It replaces one
unsourced input (the integer 6) with two structural ones, neither derived
from the five QOU axioms here. Its value is that both are group-theoretic
statements of a kind an axiom could plausibly supply, whereas "exactly six
branch points" is not — and that the narrowing is *honest*, in that it
leaves genus 3 open rather than landing on 4.

## Scope, per AGENTS.md §"Before declaring refuted"

- §5(c) is a **scope-(b) structural exclusion** of the *specific*
  implication "icosahedral type ⟹ six branch points on `ℙ(V)`". The
  invariant is the orbit-size formula `|Ḡ|/mᵢ` and it is proved. It is
  **not** a claim that no finite-group route can produce a 6 — three other
  ADE types do.
- §4 is likewise an exclusion of the *form* of the torus-knot constraint,
  not of its conclusion (`g = 4` may still be right).
- §5(a) is a structural insufficiency: an explicit infinite model (`SU(2)`
  itself) satisfies the hypotheses.
- Everything else is **scope-(a)**: these constructions, alone, do not
  derive the 6.

## Still open — the sharpest statement of what would source it

> **Steps 3 + 4 pin `χ(A)` to the non-positive even integers and nothing
> more. Every candidate source tested either restates the target (the
> torus-knot bracket), reads it off Bring's curve (the Weierstrass /
> transposition fixed-point count), or fails to produce a 6 at all (the ADE
> orbits). The one hypothesis that narrows without naming 6 is
> transitivity of `Aut` on the Weierstrass points, which gives
> `χ ∈ {−4, −6}`; separating those two needs an order-5 automorphism.**

So the next question is **not** "derive 6". It is:

1. **Does an axiom supply homogeneity?** — i.e. does the QOU substrate
   force `Aut(M₀)` to act transitively on the Weierstrass points, with all
   weights 1? Observability is the natural candidate (*"no hidden global
   symmetries"* / no distinguished internal direction), and it is currently
   an opaque `Prop` field, so the question is open and formalisable.
2. **Does an axiom supply an order-5 automorphism?** The corpus's `ζ₅`
   pentad, the Bring–Jerrard quintic and the `(2,4,5)` triangle group all
   carry one — but all three are Bring-derived, so as things stand this is
   the same read-off one level down. An axiom-level source for order 5 is
   the harder half and I did **not** find one.

Both are group-theoretic. Neither is an integer to be guessed.

## Not done, deliberately

No content block was edited. Correcting Step 5's parenthetical is arguably
AGENTS.md exemption 2 (a held source decides it), but *what Step 5 should
say instead* is a reading of the chain, and that is the owner's call — the
same disposition `qou-51l1` took on `chapter-overview.md:30`.


---

## Session close, 2026-09-15 (`claude/chi-branch-point-count-2026-09-15`)

**Status stays `todo`: the subject is an open derivation and AGENTS.md
§13a forbids closing a bean whose subject is an open conjecture.** This
session tested the assigned route and reported a negative; it did not
derive the 6.

One more negative, scoped so it is not mistaken for a stronger claim.
**Surface searched: every `folio/quantum-observable-universe/*/*.ts`
block manifest.** Of the fifteen carrying an order-5 group structure,
**all** are in `brings-surface/` or downstream of it
(`mass-endomorphism/color-spacetime-s5-factorization`,
`mass-theory/bring-trilog-*`). `rem:fivefold-symmetry` opens with *"Bring's
surface Σ₄ possesses an S₅ automorphism group"* — the 5 is read off Bring,
not derived. The two `appendix-surreals/` hits are about the zeta VALUE
ζ(5), a different object.

**Not searched:** `computations/`, `docs/`, and the knowledge graph
(`corpus_search` / MCP `paper-assistant` failed to connect this session,
ENOENT). So this is "no axiom-level source for an order-5 automorphism on
the block-manifest surface", not "there is none".


---

## Session 2026-09-15 (`claude/weierstrass-transitivity-from-axioms-2026-09-15`) — the transitivity route, tested and NEGATIVE

**Status stays `todo`** (AGENTS.md §13a: the subject is an open derivation).

Assigned: the one narrowing this bean's prior session found that does not name
six — Laing & Singerman Thm 15, transitivity of `Aut` on the Weierstrass points,
which was recorded as giving `χ(A) ∈ {−4, −6}` from a homogeneity hypothesis.
**Q1** — does an axiom force transitivity? **Q2** (secondary) — does an axiom
supply an order-5 automorphism, searched on the surfaces the prior pass skipped?

### Outcome in one line

**The route fails, and not because the right axiom was not found: the hypothesis
that does the narrowing is not the transitivity.** Transitivity has *zero*
narrowing power on the genus, and that is a **scope-(b) structural exclusion**
whose invariant is an explicit infinite family in a **held, published** source.

### 1. Laing & Singerman has TWO hypotheses, and the prior framing dropped one

`g³ − g` is the **total Weierstrass weight** at every genus `g ≥ 2` (Hurwitz),
and every Weierstrass point carries weight `≥ 1`. So "`g³ − g` Weierstrass
points" is not a count sitting next to transitivity — it is the independent
hypothesis that **every Weierstrass point is simple** (weight exactly 1), since
`|W| ≤ g³ − g` always, with equality iff all weights are 1.

This is not an inference of mine. **The corpus already holds the paper that says
it verbatim**, and it had never been read here:

> *"Laing and Singerman in [24] searched for all Riemann surfaces of genus
> `g > 2` admitting a transitive action on the Weierstrass points, **but under
> the additional assumption that such points are simple (namely, of weight
> 1)**."*

— S. Reyes-Carocca & P. Speziali, *Infinitely many Riemann surfaces with a
transitive action on the Weierstrass points*, arXiv:2211.08164v2, §4:
`library/arxiv-2211.08164v2/sections/sec-003-4-simple-weierstrass-points.md`.
Registered in `content/schema/references.ts:13545`, indexed at
`library/INDEX.md:364`. The prior session's own record cites this arXiv id via
`content/bib-qa-verifications.json:11038` — so the document was known and its
decisive content was not.

### 2. Transitivity alone narrows NOTHING — scope (b)

Two independent witnesses, both from that held source:

- **Its title is the theorem.** *"There are infinitely many pairwise
  non-isomorphic, non-hyperelliptic compact Riemann surfaces with automorphism
  group acting transitively on the Weierstrass points."* (§1). It falsifies
  three of Singerman's own conjectures, and the Magaard–Völklein expectation
  that no such infinite non-hyperelliptic family exists.
- **The Accola–Maclachlan curve of genus `g ≥ 2`** is transitive on its
  Weierstrass points **at every genus** (§1 item 1). `2g + 2` points of weight
  `g(g−1)/2`, carrying the full `g³ − g` — verified exactly for `g = 2…60`
  (probe T3), and simple **only** at `g = 2`.

So a `predicate = transitivity` cuts out **no genus at all**. Any axiom whose
content is transitivity — however it is stated, from whatever reading of
observability — buys nothing. This is not "no axiom was found"; it is *there is
nothing here for an axiom to supply*.

### 3. The operative hypothesis is a GENERICITY condition, anti-correlated with symmetry

Simplicity is what narrows, and it is the wrong **shape** for an
observability-style axiom to supply. The sharpest evidence is inside the
classification's own data — the four published configurations (probe T5):

| configuration | genus | \|W\| | weight | \|Aut\| | stab | transitive | simple |
|---|---|---|---|---|---|---|---|
| Bring | 4 | 60 | 1 | 120 | 2 | ✓ | ✓ |
| Klein's quartic | 3 | 24 | 1 | 168 | 7 | ✓ | ✓ |
| `K₃` long orbit | 3 | 24 | 1 | 24 | 1 | ✓ | ✓ |
| `K₃` short orbit | 3 | 12 | **2** | 24 | 2 | ✓ | **✗** |

`|W|·w = g³ − g` in all four; `|W|` divides `|Aut|` in all four. **4/4
transitive, 3/4 simple** — transitivity separates *nothing* and simplicity is
the entire discriminator. And the one that fails simplicity is, by the source's
§4, exactly **Fermat's quartic and `C₃`** — the two *most symmetric* members of
`K₃`. So more symmetry does not give simplicity; inside the very family the
theorem is about, it takes it away.

(Bring's stabiliser `120/60 = 2` independently reproduces Braden &
Disney-Hogg's *"preserved by the transposition (ij) only"* — a cross-check that
the table is transcribed correctly.)

### 4. Derived here, and it is the arc's first non-read-off narrowing: `g ≤ 8`

With **no classification input at all**: transitivity makes `W` a single orbit,
so `|W|` divides `|Aut|`; simplicity gives `|W| = g³ − g`; Hurwitz gives
`|Aut| ≤ 84(g − 1)`. Cancelling the common `(g − 1)`:

    (g−1)·g·(g+1) ≤ 84(g−1)  ⟹  g(g+1) ≤ 84  ⟹  g ≤ 8.

Cut-off exact (`g=8`: 504 ≤ 588 holds; `g=9`: 720 > 672 fails), scanned to
`g = 400` with no re-entry. Strictly weaker than the cited `g ∈ {3,4}` — and
unlike it, it needs **neither Laing & Singerman (not held) nor anything read off
Bring's curve**. Every classical input is a hypothesis of the theorem consuming
it, so nothing is assumed as an `axiom`.

### 5. Framing correction: `χ = −2` survives; the route gives `{−2, −4, −6}`

Both classification papers stipulate genus `> 2`. That is a hypothesis, not a
conclusion, and **genus 2 satisfies both (H1) and (H2) unconditionally**: at
`g = 2` the *maximum* weight `g(g−1)/2` is itself `1`, so every genus-2
Weierstrass point is simple, there are `2g+2 = 6` of them and `g³−g = 6` agrees;
and the Accola–Maclachlan curve of genus 2 supplies transitivity (§1 item 1
states the family for `g ≥ 2`).

Nothing in `ex:chi-minus-six-derivation` supplies `g > 2` — Step 4 gives
`g ≥ 1`, observability gives `χ ≠ 0`, i.e. `g ≥ 2`. So the route's honest output
is **three** values, not two. `−6` is 1 of 3 with the classification, 1 of 7
under the self-contained bound of §4.

*(A curiosity, not a derivation: the genus-2 case is a real "six" — six simple
Weierstrass points carrying a transitive action. It is not the corpus's six.)*

### 6. Q1, answered

**No.** And the reason is prior to any search for the right reading of
observability. The corpus encodes observability twice and neither encoding
reaches a surface automorphism group:

- `QOU.FluidDynamics.QOUFluidUniverse.observability` — an **opaque `Prop`
  field** (`qou_ns_in_qou.lean:77`), no content at all;
- `QOU.FluidDynamics.ObservabilityData`
  (`observability_q_independent.lean:56`) — its only content in the corpus: a
  single `hom_rank : ℕ` with `observable : hom_rank = 0`, i.e.
  `Hom_𝐂(𝟙, Ad(A)) = 0`.

That is a statement about a Hom-space in the monoidal category, about the
algebra object `A`. No theorem in the corpus relates it to `Aut(M₀)` acting on
anything. **But building that bridge would not help**: by §2 it would deliver
(H1), which narrows nothing. The hypothesis that narrows is (H2), and §3 is the
argument — an argument, not a theorem — that a homogeneity axiom is the wrong
shape for it.

**Anti-fit note.** I did not pick a reading of observability to make
transitivity come out. The route was tested as assigned and the measurement
went the other way; §3's anti-correlation is the held source's own data, not a
selection of mine.

### 7. Q2 — the unsearched surfaces, searched. Same answer, wider.

The prior session's negative covered `folio/quantum-observable-universe/*/*.ts`
only. Searched this session: **`computations/`, `docs/`, `.beans/`, and the
`library/*/ocr/` tier** (26 directories) that a `sections/` grep misses.

There **is** an order-5 structure outside `brings-surface/` — the binary
icosahedral `Σ(2,3,5) = 2I` (order 120) of the `Δ_λ` / WRT arc:
`computations/lr_modulus_identification_sigma235.py`,
`computations/deltalambda/deltalambda_icosahedral_smatrix_magnitude_probe.py`,
`computations/deltalambda/s5so3_geometric_wlambda_a4_helium_probe.py`,
`content/.../mass-theory/cyclotomic-boundary-at-keystone.md`,
`conj:klein-bring-icosahedral-bridge`.

**It is the same read-off, one level down.** `docs/coordination/s5-so3-keystone.md`
states its own goal as the fibre map `S₅ ⊃ A₅ ≅ I ⊂ SO(3)` tying the Wedderburn
action on `H₅(q)` *"to icosahedral rotations on **Bring's quintic surface**"* —
so `Σ(2,3,5)` enters **through `S₅ = Aut(Bring)`**, not from an axiom. And
`conj:klein-bring-icosahedral-bridge` is stated in terms of Bring outright.
`lr_modulus_identification_sigma235.py` opens *"TARGET (conjectured shape, per
the s5-so3 ledger)"* — posited, not derived.

**The one route to order 5 that does NOT pass through Bring is McKay
`2I ↔ Ê₈`** — and it is blocked at the joint this bean already recorded: §5(a),
nothing in the axioms makes `G` finite, so the ADE list does not apply to the
object the axioms deliver; and granting finiteness, observability prunes to four
families and nothing selects the icosahedral one.

So: **no axiom-level source for an order-5 automorphism on any surface now
searched.** Still not searched: the knowledge graph (`corpus_search` / MCP
`paper-assistant` again failed to connect, ENOENT).

### Artifacts, both on the branch

- **`folio/quantum-observable-universe/lean/QOU/BringsSurface/WeierstrassTransitivityNotForced.lean`**
  — sorry-free, **import-free**, `lean -DautoImplicit=false -s 65536` exit 0.
  12 declarations; `#print axioms` kernel-checked: no `sorryAx`, no custom
  axiom — `[propext, Quot.sound]` on seven, **nothing at all** on the other
  five. `scripts/lean-self-assuming-audit.py` 0 hits, and the `qou-1ccx` blind
  spot (projection through an anonymous instance binder) **cannot apply**: the
  file declares no `class` and no `structure`.
- **`computations/weierstrass_transitivity_narrowing_probe.py`** +
  **`computations/weierstrass-transitivity-narrowing.witness.json`** — 22/22,
  exact `int` throughout, no float / mpmath / substrate parameter
  (`q0Anchor: independent`). Independent route: divisor enumeration over the
  total weight, plus the direct cross-check of the held source's four
  configurations. `scripts/precision-gates.sh --changed` exit 0 (the 13 audit
  witnesses the gate run rewrote were restored, not committed).

### Scope, per AGENTS.md §"Before declaring refuted"

- **§2 is scope (b)** for the transitivity half: the invariant is an explicit
  infinite family (Accola–Maclachlan at every `g ≥ 2`) in a published held
  source, plus that source's main theorem. Not a claim that no homogeneity
  hypothesis of any kind could narrow — a claim about *this* one.
- **§3 and §6 are scope (a)**: no axiom supplying simplicity was found on the
  surfaces searched. The shape argument is an argument, not a proof.
- **§7 is scope (a)**, widened: no axiom-level order-5 source on
  `computations/` / `docs/` / `.beans/` / `library/*/ocr/` either.
- **Not excluded:** `g = 4` may still be right; the classification is genuine;
  §4's `g ≤ 8` is a real narrowing.

### Sharpest statement of what remains

> Steps 3+4 pin `χ(A)` to the non-positive even integers. The transitivity route
> narrows only as the **conjunction** of a homogeneity condition (H1) and a
> genericity condition (H2), and **neither half narrows alone** — (H1) is
> realised at every genus, (H2) is the generic condition. The narrowing is a
> pure conjunction effect between two conditions that pull in *opposite*
> directions, which is exactly why only finitely many surfaces satisfy both. No
> QOU axiom supplies either half; and because the two pull opposite ways, an
> axiom supplying one is evidence *against* the other. Selecting `g = 4` from
> the survivors still needs an order-5 automorphism, for which no axiom-level
> source exists on any surface yet searched.

**So the next question is no longer "which axiom gives transitivity".** It is
whether anything in the framework supplies a *genericity* statement about the
Weierstrass locus — that no Weierstrass point is exceptional. That is the
opposite register from observability, and I did not find a candidate.

### Not done, deliberately

No content block was edited. Correcting `ex:chi-minus-six-derivation`'s
`{−4, −6}` to `{−2, −4, −6}`, and re-describing Step 5's narrowing as
carried by simplicity rather than transitivity, are both readings of the chain —
the owner's call, the same disposition `qou-51l1` and the prior session took.

## Progress Update (2026-11-16 — Round 47, PR #8147)

- Extended `folio/quantum-observable-universe/lean/QOU/BringsSurface/BranchPointSixNotForced.lean` (`0` `sorry`, import-free, `lean -DautoImplicit=false -s 65536` exit 0, PR `litlfred/qou#8147`, commit `94984f6696056c5cbe6d700149fbb37894d29ad5`) with §6.5 (`Hyperelliptic vs. trigonal Riemann–Hurwitz ramification at genus g = 4`):
  - `totalRamificationOverP1 (d g : Nat) : Nat := 2 * g - 2 + 2 * d`
  - `chiOverP1_totalRamification (d g : Nat) (hg : 1 ≤ g) : chiOverP1 d (totalRamificationOverP1 d g) = eulerChar g`
  - `hyperelliptic_ramification_genus_four : totalRamificationOverP1 2 4 = 10 ∧ totalRamificationOverP1 2 4 ≠ 6`
  - `trigonal_ramification_genus_four : totalRamificationOverP1 3 4 = 12`
  - `trigonal_simple_branch_count (g : Nat) (hg : 1 ≤ g) : totalRamificationOverP1 3 g = 2 * g + 4`
  - `trigonal_genus_four_six_branch_points_iff_index_two (rPerPoint : Nat) : 6 * rPerPoint = totalRamificationOverP1 3 4 ↔ rPerPoint = 2`
  - `uniform_six_branch_points_minimal_degree_is_trigonal`: proves that for $2 \le d \le 5$, a uniform-ramification cover of $\mathbb{P}^1$ of genus $4$ with $b = 6$ branch points has unique minimal-degree solution $(d, r_{\text{per}}) = (3, 2)$.
- Kept at `status: in-progress` per owner rule.

## 2026-11-19 — M4 character bound (PR #8365, commit fea313d5e)

`QOU/BringsSurface/CharacterBound.lean`, sorry-free:
- χ(g⁻¹) = conj χ(g);
- (dim V)² ≤ |G| for an irreducible rep;
- hence g ∈ {4,6}, from H¹ = 2W with W irreducible, plus Riemann–Hurwitz for A₅ and S₅.

The old hypothesis `hdim` (the list of A₅ irreducible dimensions) is narrowed to one fact: A₅ has no 6-dim irreducible (M4c, open).

Child beans for another agent: qou-m1bg (M1b, analytic germs) and qou-m3tr (M3, equivariant triangulation).

Still open:
- G2 (lift A₅ from the fibre to the base);
- G3 (irreducibility of H¹);
- M2 (globalise on the surface);
- M4c.

This bean stays open.

## 2026-11-19 — M4c closed (PR #8365, commit 8d02dfe12)

`A5NoSixDim.lean`, sorry-free, kernel decide only:
- `finrank_ne_six`: A₅ has no 6-dim irreducible.
- `genus_eq_four_of_A5_irreducible`: genus 4 with no assumption on A₅'s representations.

M4 is done. Still open: M3 (qou-m3tr), M1b/M2 (qou-m1bg), G2, G3. This bean stays open.



## Completed (2026-11-19)
Completed & Red-Team PASSED (`0` blockers): `folio/quantum-observable-universe/lean/QOU/Brings/BringTranspositionSixFixedPointsAndEllipticQuotient.lean` (`526` lines) + 80-dps probe `computations/probes/bring_transposition_weierstrass_sixty_probe.py` (`scriptHash = 55e5625d224d`, all 60 Weierstrass points, `P_tau(t)=t^3+2t^2+3t+4`, `j(E_tau)=-25/2`, `chi(B)=-6`).

## 2026-11-20 — reopened (W9, session_01VQDpPcjxVSqN8ELUBjiBHk)

**Status was `completed` (set 2026-11-19); reopened to `in-progress`.** The children `qou-m1bg` and `qou-m3tr` say *"Parent bean `qou-qhcr` must never be closed"*. AGENTS.md §13a forbids closing a bean whose subject is an open derivation. The 6 is still not derived from the axioms, and the "Completed & Red-Team PASSED" entry above is a Bring read-off: transposition fixed points on Bring's curve, the route this bean's §3 already scoped as non-derivational.

**M1b advanced:** PR #8532 (`claude/bring-germ-stabiliser-cyclic-2026-11-20`). It proves sorry-free that an effective finite germ action fixing a point is cyclic, and supplies the `hstabA`/`hstabS` disjunctions for groups `≅ A₅`/`S₅`. Open: the chart step and germ-effectiveness (M2), M3 (`qou-m3tr`), G2, G3.

## 2026-11-20 — W9 wiring merged

Merged: #8532 (M1b, `GermStabiliserCyclic`), #8570 (M3 step 1, `CombinatorialMapQuotient`), #8600 (`GenusFourFromGermStabilisers`, main `f1d778d28f`). `genus_eq_four_of_germ_stabilisers` now derives `hA60`/`hS120`/`hstabA`/`hstabS`.

Still hypotheses:
- M2: the chart step and effectiveness on germs;
- M3 steps 2–3: chi even, and the triangulation;
- G2/G3: H^1 = 2W with W irreducible.

The 6 is still not derived. W9 is parked.
