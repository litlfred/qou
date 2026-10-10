# A decidable hyperbolicity criterion for Obstruction A — with its hypothesis

**Status:** literature finding from a newly-ingested paper. No braid derived,
no mass checked, nothing wired. Beans `qou-qpj9`, `qou-pb1w`.

Source: [`library/arxiv-0805.1447v2/`](../../library/arxiv-0805.1447v2/) —
Tetsuya Ito, *Braid ordering and the geometry of closed braid*. Ingested
2026-08-25 from `uploads/` (it had been sitting in the incoming queue, and
**corpus-grep path 5 searches `library/` only**, so it was invisible to every
"has the corpus got this?" check until now).

## Why it matters

Obstruction A needs a way to tell, **from the braid word**, whether a
candidate's closure is hyperbolic — otherwise every candidate needs SnapPy and
the search is unbounded. The previous tool found for this,
[Giambrone's closed-3-braid volume bounds](2026-08-24-meson-braid-obstruction-a-measured.md),
turned out to require `rᵢ ≤ −3` on every negative exponent, which **excludes
the corpus's own carriers** — figure-eight and Borromean are built from `±1`
crossings. Ito's criterion has no such restriction.

## The theorem, with the hypothesis that governs it

> **Theorem 2 (Ito).** Let `β ∈ Bₙ` be a braid **whose closure is a knot**.
> **If `[β]_D ≥ 3`**, the following hold:
> 1. `β` is periodic ⟺ `β̂` is a torus knot;
> 2. `β` is reducible ⟺ `β̂` is a satellite knot;
> 3. `β` is **pseudo-Anosov ⟺ `β̂` is a hyperbolic knot**.

`[β]_D` is the **Dehornoy floor**. The hypothesis is not decoration — the
paper's Figure 2 exhibits *periodic, pseudo-Anosov and reducible* braids
**all of whose closures are the same `(2,3)` torus knot**. Drop `[β]_D ≥ 3`
and the Nielsen–Thurston type determines nothing about the closure.

For `B₃` the Nielsen–Thurston type itself is a one-line computation, since
`B₃/Z ≅ PSL(2,ℤ)` under `σ₁ ↦ [[1,1],[0,1]]`, `σ₂ ↦ [[1,0],[−1,1]]`:
`|tr| < 2` periodic, `= 2` reducible, `> 2` pseudo-Anosov.

## How the hypothesis caught an error of mine

Applying (3) *without* the hypothesis to the corpus's meson braid:

| braid | `\|tr\|` | NT type |
|---|---:|---|
| `𝔐 = (σ₁σ₂)²σ₂σ₁` — corpus meson | 3 | pseudo-Anosov |
| `(σ₁σ₂⁻¹)²` — muon carrier | 7 | pseudo-Anosov |
| `(σ₁σ₂⁻¹)³` — proton carrier | 18 | pseudo-Anosov |
| `σ₁³`, `σ₁⁵` | 2 | reducible |

Read naively, `𝔐` is pseudo-Anosov, so (3) would say its closure is
hyperbolic. But
[the 2026-08-24 audit measured `Vol(𝔐) = 0`](2026-08-24-meson-braid-obstruction-a-measured.md)
in SnapPy and identified the closure as **T(2,5)**, a torus knot. Both cannot
hold.

The contradiction is the hypothesis failing, not the theorem: `𝔐` must have
`[β]_D < 3`. And that is consistent with the same audit's own observation that
`𝔐` *"simplifies from 6 crossings to 5"* — T(2,5) has braid index 2, so `𝔐` is
a stabilised 2-braid dressed as a 3-braid, exactly the degenerate case a
Dehornoy-floor condition is there to exclude.

**Recorded because I nearly published (3) without its hypothesis.** What caught
it was not care — it was that the corpus already held a *measured* value the
naive reading contradicted. Without `Vol(𝔐) = 0` on record, a decidable-looking
one-line criterion would have gone into the ledger wrong.

## What this gives Obstruction A

A **two-part, parameter-free, decidable test** that a candidate braid's closure
is hyperbolic, computable from the word with no SnapPy and no A-adequacy:

1. `[β]_D ≥ 3` (Dehornoy floor), and
2. `|tr(β)| > 2` in `PSL(2,ℤ)` (pseudo-Anosov).

Unlike Giambrone's family this admits `±1` exponents, so it **covers the
corpus's own braid vocabulary**. It does not derive a braid — Obstruction A is
untouched — but it makes the candidate space checkable a priori, which is what
the front lacked.

## Scope and what is NOT claimed

**(a)** A criterion imported and scoped, not a result about any meson. Not
claimed: that any candidate exists, that `𝔐` can be repaired, or that
hyperbolicity suffices for the mass law (it fixes `Vol > 0`, nothing more).
The Dehornoy floor of the corpus's carriers is **not computed here** — the
`|tr|` column above is the NT type only, and without `[β]_D ≥ 3` verified,
none of those rows licenses a conclusion about its closure via Theorem 2.
Computing `[β]_D` for the candidate set is the next step, and it is
mechanical.

---

## Addendum — the corpus's braids are far below the hypothesis, and that is the pattern

Definition 1, quoted from the source:

> **Definition 1.** Dehornoy floor `[β]_D` of a braid `β ∈ Bₙ` is the minimal
> non-negative integer `m` satisfying `β ∈ (Δ^{−2m−2}, Δ^{2m+2})`.

In `B₃`, `Δ² = (σ₁σ₂)³` — 6 crossings, exponent sum 6, and it generates the
centre. Ito supplies his own calibration: **`(σ₁σ₂)⁴ ∈ B₃` has `[β]_D = 1`**
(and `0` in `B₄` — the floor depends on the ambient `Bₙ`, which he flags).

So **Theorem 2's `[β]_D ≥ 3` requires `β` to lie outside `(Δ^{−8}, Δ^{8})`.**

> **🛑 The crossing count that followed was mine and was wrong — corrected by
> computation, below.** This read *"to dominate `Δ⁸ = (σ₁σ₂)¹²`, a braid of
> **24 crossings**"*. `Δ⁸` is the *bracketing power* in Definition 1, not the
> smallest braid of floor 3. Computed, **`Δ⁶ = (σ₁σ₂)⁹` already has floor 3**,
> so the threshold is **18 crossings**. Direction and margin are unchanged —
> 18 against a corpus maximum of 6 — but the number was an estimate presented
> as a reading. See the addendum.

Against that:

| braid | crossings | exponent sum |
|---|---:|---:|
| `Δ² = (σ₁σ₂)³` (the unit of the scale) | 6 | 6 |
| `(σ₁σ₂)⁴` — Ito's example, floor **1** | 8 | 8 |
| `𝔐 = (σ₁σ₂)²σ₂σ₁` — corpus meson | 6 | 6 |
| `(σ₁σ₂⁻¹)²` — muon carrier | 4 | 0 |
| `(σ₁σ₂⁻¹)³` — proton carrier | 6 | 0 |

**What is rigorous here:** the requirement itself — `[β]_D ≥ 3` means clearing
a 24-crossing braid — read straight off Definition 1.

**What is indicative and NOT computed:** the corpus braids' actual floors. The
Dehornoy floor is **not** a function of the exponent sum — `σ₁σ₂⁻¹ > 1` with
exponent sum `0` — so the table above is a scale comparison, not a
calculation. A rigorous `[β]_D` needs handle reduction, which was not run.
Nothing below depends on the exact values.

### The pattern, which does not depend on the exact floors

This is the **second** hypothesis from this literature that the corpus's braids
fail, and the two are independent:

| source | hypothesis | why the corpus fails it |
|---|---|---|
| Giambrone, Thm 1.2 | every negative exponent `rᵢ ≤ −3` | corpus words use single `±1` crossings |
| Ito, Thm 2 | `[β]_D ≥ 3` (clears 24 crossings) | corpus words are 4–6 crossings |

Two different papers, two unrelated conditions, one cause: **the closed-3-braid
geometric literature is built for *complex* braids — long syllables, high
Dehornoy floor — and the framework's carriers are short words close to the
identity.** That is a property of the corpus's braid vocabulary, not a run of
bad luck in the reading.

### What that gives Obstruction A, constructively

It is a **lower bound on any certifiable candidate**. A braid whose closure the
literature can certify hyperbolic — rather than merely measure in SnapPy — must
be *substantially longer* than anything the framework currently writes down:
≥ 3 same-sign crossings per negative syllable (Giambrone), or clearing ~24
crossings (Ito).

That is a real constraint on the search and it points the same way as the
2026-08-24 audit's own measurement, which found the pion target bracketed only
by braids longer than the corpus's. It does not derive a braid. Obstruction A
remains open, and the honest next step is unchanged and mechanical: run handle
reduction to get the actual floors, rather than reasoning from exponent sums as
this addendum does.


---

## Addendum — the floors, computed

Probe: [`meson_braid_dehornoy_floor_probe.py`](../../computations/meson/meson_braid_dehornoy_floor_probe.py)
(witness `meson-braid-dehornoy-floor.witness.json`, 3 assertions, all passed).
This closes the step the section above left open: *"a rigorous `[β]_D` needs
handle reduction, which was not run."* It is run now.

**Validated before use** against all three values Ito states himself —
including the conjugation pair he uses to show the floor is *not* a conjugacy
invariant, which pins the implementation on the subtle case rather than only
the easy one:

| braid | Ito states | computed |
|---|---:|---:|
| `(σ₁σ₂)⁴` | 1 | **1** |
| `Δ²σ₁σ₂⁻¹` | 1 | **1** |
| `Δ²σ₂σ₁⁻¹` (conjugate to the above) | 0 | **0** |

### The corpus

| braid | crossings | `[β]_D` | Thm 2 applies? |
|---|---:|---:|---|
| `𝔐 = (σ₁σ₂)²σ₂σ₁` — corpus meson | 6 | **1** | no |
| `(σ₁σ₂⁻¹)²` — muon carrier | 4 | **0** | no |
| `(σ₁σ₂⁻¹)³` — proton carrier | 6 | **0** | no |
| `σ₁³` — trefoil | 3 | 0 | no |
| `σ₁⁵` — T(2,5) | 5 | 0 | no |

| scale | crossings | `[β]_D` |
|---|---:|---:|
| `Δ² = (σ₁σ₂)³` | 6 | 1 |
| `Δ⁴ = (σ₁σ₂)⁶` | 12 | 2 |
| **`Δ⁶ = (σ₁σ₂)⁹`** | **18** | **3** ← threshold |
| `Δ⁸ = (σ₁σ₂)¹²` | 24 | 4 |

**Two things this settles.**

1. **My "24 crossings" was wrong; it is 18.** I read Definition 1's bracketing
   power `Δ^{2m+2}` at `m = 3` as the braid that must be cleared, when it is
   merely what brackets it. Corrected at both sites. The conclusion does not
   move — the corpus maximum is 6 — but an estimate had been presented as a
   reading of the definition.
2. **`[𝔐]_D = 1`, so the contradiction is resolved by computation.** The
   section above *inferred* that `𝔐` must have `[β]_D < 3`, because it is
   pseudo-Anosov yet its closure was measured as T(2,5) with `Vol = 0`, which
   Theorem 2 forbids. The inference was right; it is now a number.

**Scope (a) — a hypothesis check.** Claimed: no braid word the corpus
currently uses satisfies Ito's hypothesis, maximum floor 1 against a required
3. Not claimed: that no candidate exists, that longer braids work, or anything
about the mass law. And since the floor is **not** a conjugacy invariant —
Ito's own example, reproduced above — these are statements about *these words*,
not about the link types they close to. Obstruction A is untouched.

---

## Addendum 2 — the short-word vocabulary is load-bearing

Probe: [`meson_braid_length_cap_probe.py`](../../computations/meson/meson_braid_length_cap_probe.py)
(witness `meson-braid-length-cap.witness.json`, 3 assertions, all passed).

The addenda above leave one question: two independent hypotheses from this
literature are unreachable by the corpus's braid words — is that because nobody
has written a long enough candidate, or because the framework forbids one?

**It forbids one.** Crossing number here is not a free parameter; it is a
**quantum number**.

`QOU/ParticleInteractions/WeakIsospinT3Grading.lean` (sorry-free) fixes
`signedWrithe` at `up 3, charm 5, top 7` and defines
`genWinding = |signedWrithe|`, noting it *"reproduces the corpus `T(2,n)`
indices `{3,5,7}`"*. And
[`lepton-meson-torus-knot-dictionary-proof.md`](../../content/quantum-observable-universe/knots-particles-confinement/lepton-meson-torus-knot-dictionary-proof.md)
gives a meson's crossing number as the **sum of its two constituent windings**:

> `K`: `ūs = 3 + 5 = 8` crossings · `η, φ`: `ss̄ = 5 + 5 = 10` crossings

That arithmetic reproduces the written braid: `𝔐 = (σ₀σ₁)²σ₁σ₀` is 6 crossings,
and the pion is `ūd = 3 + 3 = 6`. `T(2,9)` is the **gluon** — the genus-4
saturating force carrier — not a quark generation, so 9 is unavailable as a
constituent.

**So a meson braid is capped at `t̄t = 7 + 7 = 14` crossings.**

### Which floors are reachable at that length

| word length | words tested | max floor found | mode |
|---:|---:|---:|---|
| 5 | 1 024 | 1 | exhaustive |
| 7 | 16 384 | 1 | exhaustive |
| 10 | 40 000 | 2 | sampled |
| **14** — the meson cap | 40 000 | **2** | sampled |
| 18 = `Δ⁶` | — | **3** | the threshold |

**Floor 3 is not reachable at the cap.** So Ito's Theorem 2 cannot apply to
*any* meson braid this framework admits — not for want of a candidate, but
because the crossing number is bounded by the winding sum. The same ceiling is
why Giambrone's family excludes the corpus's carriers.

### Scope, and what would overturn it

**(a) — on a search plus a corpus premise.** Claimed: no `B₃` word of length
≤ 14 was *found* with floor 3, exhaustively to length 7 and by 40 000-word
sampling beyond; and the corpus's own arithmetic caps a meson at 14 crossings.

**Not claimed:** that no such word *exists* — beyond length 7 this is sampling,
not enumeration. That the cap is a theorem — *"crossing number = sum of
constituent windings"* is the corpus's stated construction, taken as given and
not re-derived here. And the floor is not a conjugacy invariant, so this is
about **words**.

**What would overturn it:** a meson whose braid is not the winding sum; a
fourth generation winding above 7; or an exhaustive search at lengths 8–14
turning up a floor-3 word.

### What it settles for the front

The closed-3-braid geometric literature is built for **complex** braids — long
syllables, high Dehornoy floor. This framework structurally cannot supply one
in the meson sector. That is a statement about **applicability**, not about
whether Obstruction A is soluble: it stays open, with one fewer route worth
importing. A tool for Obstruction A has to work on **short** braids, and none
of the three papers ingested today is one.

---

## 🛑 RETRACTION of Addendum 2 — "load-bearing" was a word-level fact dressed as a framework-level one

Addendum 2 concluded that the framework's short braid vocabulary is
**load-bearing**, that Ito's Theorem 2 "cannot apply to *any* meson braid this
framework admits", and that the closed-3-braid literature "structurally cannot"
be supplied. **All three overreach and are withdrawn.** Raised by the author
with one pointer: *"we have the Gröbner NF."*

### The defect

The **Gröbner–Shirshov normal form lives in `H₃(q)`** — a linear combination of
algebra basis elements with `q`-coefficients. It is not a braid word and has no
crossing number. What Addendum 2 capped at 14 was the *braid word*
`𝔐 = (σ₀σ₁)²σ₁σ₀`, which is a **chosen presentation**.

Three steps, and the third is unlicensed:

1. The mass law reads `Vol(K)`, a **link invariant**. Every braid word whose
   closure is that link gives the same volume; the corpus's canonical word is
   one representative among infinitely many.
2. Braid words are not length-canonical — Markov stabilisation and conjugation
   change them freely, and Ito states explicitly that `[β]_D` depends on
   *which `Bₙ`* the braid is regarded as living in, so even the strand count is
   a presentation choice.
3. So *"no word of ≤ 14 crossings reaches floor 3"* is a statement about
   **presentations**, and Addendum 2 drew a **framework-level** conclusion from
   it.

### This is the mirror of an error the corpus had already diagnosed

[`2026-08-24-meson-braid-obstruction-a-measured.md`](2026-08-24-meson-braid-obstruction-a-measured.md)
caught `lepton-meson-parallel` reading normal-form coefficients
(`σ⁻¹ = σ − h`) as geometric crossings:

> *"Negative crossings in a normal-form **coefficient** are algebra, not
> geometry, and volume sees only the geometry. The construction conflates the
> two."*

Addendum 2 conflated them the other way — treating a **presentation's** crossing
count as a constraint on the **geometry**. The warning was one file away and
quoted approvingly elsewhere in this very document.

**And the caveat was already written.** Addendum 1 says *"these are statements
about these WORDS, not about the link types they close to."* Addendum 2 then
concluded "load-bearing" and "structurally cannot supply one" regardless. A
caveat that does not constrain the conclusion drawn two sections later is
decoration.

### What the measurements still support

| claim | status |
|---|---|
| Corpus **canonical words** have floors 0–1, against Ito's required 3 | **stands** — computed, validated |
| Floor 3 unreached at length ≤ 14 in the search run | **stands**, as a search result |
| Meson crossing number = sum of constituent windings, capped at 14 | **stands** as the corpus's stated construction for *that word* |
| The framework **cannot supply** a qualifying braid | **RETRACTED** — presentation-level evidence, link-level claim |
| The literature is **structurally inapplicable** | **RETRACTED** — same defect |
| Short vocabulary is **load-bearing** vs incidental | **UNDECIDED** — the probe cannot distinguish them |

The conjugation check run at retraction time (conjugates of `𝔐`, conjugator
length ≤ 6, ~4 k samples) found no floor above 1. That is **weak evidence, not
a defence**: it is a small search over one move, and conjugation is only one of
the presentation changes available.

### What would actually settle it

Not a word-length argument. The question is at the **link** level: for the
target link types, does *any* braid representative — any strand count, any
Markov class — satisfy `[β]_D ≥ 3`? Malyutin's supremum of the floor over a
conjugacy class is a conjugacy invariant and is the right object; it is not
computed here.

What survives untouched, and is the corpus's finding rather than mine: the
framework assigns `T(2,n)` **torus** links, and torus links have `Vol = 0`.
That is genuinely link-level, and it is Obstruction A as the 2026-08-24 audit
already stated it.

---

## Addendum 3 — the link level, searched (2026-08-25)

The retraction above named the object that would settle it: *"for the target
link types, does **any** braid representative satisfy `[β]_D ≥ 3`?"* This is
that search, run — and it lands on the criterion itself, not on the framework.

Producer:
[`computations/meson/meson_braid_conjugacy_floor_search_probe.py`](../../computations/meson/meson_braid_conjugacy_floor_search_probe.py)
· witness `meson-braid-conjugacy-floor-search.witness.json` · 4 assertions,
all passed.

### Why the conjugacy class is the right orbit

A braid's closure — hence `Vol(K)`, which is what `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²`
reads — depends only on the Markov class: conjugacy (move I) and stabilisation
(move II). The Dehornoy floor is **not** a conjugacy invariant, which is exactly
why a floor read off one written word says nothing about the link. But both
sides of Ito's equivalence *are* conjugacy invariants (Nielsen–Thurston type;
hyperbolicity of the closure), so **one** qualifying representative would let
Theorem 2 speak about the whole class. That is the link-level question.

### The control that makes a null result readable

The **figure-eight knot `4₁`** is genuinely hyperbolic (`Vol = 2.0299` — the
corpus's own muon carrier) and its closure is a **knot**, so Theorem 2 applies
to it by hypothesis if the floor condition can be met at all. If even `4₁` has
no qualifying representative, the reading is about the *criterion's threshold*,
not about these links.

### Result — B₃, 118 097 freely-reduced conjugators per braid (length ≤ 10)

| braid | closure | geometry | floor as written | best over 118 097 conjugates |
|---|---|---|---|---|
| `4₁ = (σ₁σ₂⁻¹)²` | knot | **hyperbolic**, Vol 2.0299 | 0 | **0** |
| Borromean `(σ₁σ₂⁻¹)³` | 3-component **link** | hyperbolic, Vol 7.3277 | 0 | 0 |
| meson `𝔐 = (σ₁σ₂)²σ₂σ₁` | knot `T(2,5)` | torus, Vol 0 | 1 | 1 |
| `Δ⁶σ₁σ₂⁻¹` — *positive control* | — | — | 3 | **3** |
| `Δ²σ₂σ₁⁻¹` — *raising control* | — | — | 0 | **1** |

The two controls are what make the top row worth reading. The **positive**
control shows the search does find floor ≥ 3 when it is there; the **raising**
control — Ito's own conjugate pair, searched from the low side — shows the
search finds floor-*increasing* conjugates rather than merely re-reporting the
floor it started from. A run failing either asserts rather than reports.

### Finding

**A genuinely hyperbolic knot has no sampled representative meeting Ito's
hypothesis.** `4₁` is hyperbolic, is a knot, and carries the volume the muon
anchor uses — and 118 097 conjugates at minimal braid index never reach
`[β]_D ≥ 3`. So Theorem 2 cannot certify `4₁` either.

That relocates the earlier negative. What the retracted Addendum 2 read as a
fact about the *framework's vocabulary* is, on this evidence, a fact about
*where Ito's threshold sits*: `Δ⁶` — 18 crossings — is the smallest braid the
previous probe found at floor 3, and small hyperbolic knots simply live below
it. The criterion is a large-`[β]_D` tool.

### Scope — (a), and four things it is not

Classified **(a) scope-limited negative** under AGENTS.md §"Before declaring
refuted": this construction, searched this far, does not meet the hypothesis.
It is **not (b)**: no invariant is proved to forbid it.

1. **It is a search.** 118 097 conjugators of length ≤ 10 in `B₃`. The
   supremum of the floor over a full conjugacy class is **not computed**.
2. **No Malyutin bound is invoked.** The quasi-morphism bound on the floor is
   what would upgrade this search to a proof; that paper is **not in
   `library/`**, so the corpus-grep path 5 cannot support citing it and it is
   deliberately not asserted.
3. **`B₃` rests on one stated example.** Ito states `(σ₁σ₂)⁴` has floor 1 in
   `B₃` and 0 in `B₄` — `Δ_n²` lengthens with `n`, the bracketing interval
   widens, the floor can only fall — so the floor is maximised at minimal braid
   index. That is Ito's example, not a theorem verified here. Stabilisation
   (Markov II) is therefore argued past, not searched.
4. **The Borromean row is a link, not a knot.** Theorem 2's hypothesis excludes
   it regardless of its floor. It is reported for scale only.

### What this does and does not change upstream

Unchanged: Obstruction A. The framework assigns `T(2,n)` **torus** links and
torus links have `Vol = 0` — that is link-level, is the corpus's own finding
from the 2026-08-24 audit, and this addendum neither strengthens nor weakens it.

Changed: the row *"The literature is structurally inapplicable"* in the
retraction table above stays **RETRACTED as stated**, but the correctly-scoped
version now has evidence — Ito's Theorem 2 is inapplicable **at this scale**,
to the corpus's carriers *and* to a hyperbolic control alike, because its
hypothesis is not reachable below ~18 crossings. That is a statement about the
theorem's domain, which is a legitimate thing to measure; the retracted claim
was about the framework's capacity, which this still does not measure.

### Interaction with the sibling audit landed on `main` (`b437d3bb7e`)

While this ran, a sibling landed
[`docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md`](2026-08-25-atom-word-closures-are-not-hyperbolic.md)
§"Addendum 2026-08-25", reading the same Ito ingest. Two independent routes,
one paper — the convergence AGENTS.md §"Parallel exploration" describes. Their
**primary** conclusion is untouched by anything here: the atom words are
monotone, so their closures are connected sums of `(2,k)` torus links, so
periodic/reducible, so non-hyperbolic. That argument never touches the floor.

Their **secondary** item — offered explicitly as *"a candidate structural
reason, not just a fact"*, and correctly scoped by them as conjecture — reads:

> *"Ito's classification theorem carries a Dehornoy floor ≥ 3 hypothesis, and
> short atom words have small floor — precisely the regime where a word admits
> many closed-braid representatives and closures tend to be torus or composite.
> That suggests the non-hyperbolicity is forced by the shortness and
> monotonicity of the interface construction."*

**Its premise is now measured, and its implication runs the other way.**

*Premise — confirmed.* "Short atom words have small floor" was reported; it is
now computed. Corpus floors are 0–1 against a required 3, and the smallest
braid reaching floor 3 is `Δ⁶`, 18 crossings
(`meson_braid_dehornoy_floor_probe.py`).

*Direction — the paper states the implication, and it points the other way.*
Ito's **Proposition 4** is *"Let `β ∈ Bₙ` be a braid such that `K = β̂` is a
non-braided satellite knot. Then `[β]_D < 3`"*, and his **Remark 4** cites
Menasco–Nakamura for *"if a closure of `β` is a composite knot, then
`[β]_D < 2`"*. So the theorem is **composite ⇒ small floor**. Reading it as
*small floor ⇒ tends to be torus or composite* is the converse, and the
converse fails: `4₁` is **prime and hyperbolic** and has floor **0** across
118 097 conjugates at minimal braid index. A small floor is a fact about
**scale**, shared by hyperbolic and non-hyperbolic small links alike; it is not
evidence of non-hyperbolicity.

The correction is to the suggested *mechanism* only. The atom words'
non-hyperbolicity stands on monotonicity — the sibling's own primary argument —
and Ito's Proposition 4 read forwards actually *supports* them: their composite
closures are exactly the objects the theorem says must have small floor. The
floor is the consequence, not the cause.

One reading to keep straight, since this document has already made the mistake
once. The unconditional *"`F_φ` admits a complete hyperbolic structure iff `φ`
is pseudo-Anosov"* is about the **mapping torus** — Ito calls it *"this
well-known fact"* and says *"theorem 2 can be seen as some generalization of
this well-known fact in the knot theory settings."* Theorem 2, the statement
about the **closure** `β̂`, is the generalisation, and `[β]_D ≥ 3` is load-bearing
inside its proof (*"Our assumption `[β]_D ≥ 3` and theorem 1 shows `T` is
circular-foliated"*). The mapping-torus fact costs nothing; the closure
statement costs the hypothesis this addendum could not reach.

---

## Addendum 4 — Obstruction A is two statements, not one (2026-08-25)

Reading the construction rather than importing another paper, per the note this
document ends Addendum 3 on. `mass_at_3A_proper.atom_braid_word_3A`'s docstring
(landed today, [PR #5765](https://github.com/litlfred/qou/pull/5765)) already
carries the decisive fact, and it is stronger than the framing everything above
used:

> *"the returned object lies in `H_n(q)` and is **NOT** in the image of
> `rho : B_n -> H_n(q)`. … there is **NO SINGLE LINK** behind it. … So **NO
> TOPOLOGICAL quantity may be read off it** — not a volume, not a crossing
> number, not a genus."*

Confirmed by measurement, not taken on trust
([`computations/atom_word_braid_letter_census_probe.py`](../../computations/atom_word_braid_letter_census_probe.py),
3 assertions):

| isotope | letters | `σ` | `σ⁻¹` | averaged | `2A+1` | braid gens | branch closures |
|---|---:|---:|---:|---:|---:|---:|---:|
| ²H | 23 | 11 | 7 | **5** | 5 | 18 | **32** |
| ³He | 35 | 18 | 10 | **7** | 7 | 28 | 128 |
| ⁴He | 47 | 23 | 15 | **9** | 9 | 38 | 512 |

The averaged count is `2A+1` exactly at every `A`, and `2⁵ = 32` matches the
SnapPy sweep's 32/32. So the docstring's substance holds.

**So the question this document has been asking is malformed for the atom
object.** "Is the short `±1` braid vocabulary forced?" presupposes a braid word;
there is none, and no length to argue about. Obstruction A therefore splits:

1. **The atom object is not a link at all** — an `H_n(q)` element outside
   `im(ρ)`, because of `2A+1` genuinely averaged letters. Nothing topological
   applies, and no hyperbolicity literature can, whatever its hypotheses.
2. **The knot-dictionary carriers *are* links** — `4₁`, the Borromean rings —
   and for them `Vol(K)` is exactly what the mass law reads. Addendum 3 answers
   the question for these: they are below the reach of Ito's criterion, as is
   any genuinely hyperbolic knot at that size.

These had been running together. Only (2) is a statement about scale; (1) is a
statement about *kind*, and it is the stronger of the two.

### One correction to that docstring

It also said *"Only the `d == 0` letters are braid generators."* Measurably
wrong, and it points the conclusion at the wrong objects: under the module's own
`σ⁻¹ = σ − h`, a `d = −h` letter **is** a braid generator, so ²H has 18 of them,
not 11. The letters outside `im(ρ)` are the **averaged** ones — genuine weight-1
sums of two monomials. Under a `d == 0` rule the figure-eight `(σ₁σ₂⁻¹)²` — the
muon carrier, a hyperbolic **link** the mass law reads `Vol` from — would read as
"not a braid word", i.e. conclusion (1) would leak onto exactly the objects
conclusion (2) is about. Fixed at the docstring, with the census as its witness.

---

## Addendum 5 — the bound was in the corpus; (a) becomes (b) (2026-08-25)

Addendum 3's scope note says: *"no Malyutin bound is invoked — that paper is not
in `library/`, so corpus-grep path 5 cannot support citing it."* **The bound is
in `library/`.** Ito quotes it in full, attributed to both `[MN]` and `[Ma]`, in
[`sec-001-2-braid-ordering-and-dehornoy-floor`](../../library/arxiv-0805.1447v2/sections/sec-001-2-braid-ordering-and-dehornoy-floor.md)
— the same section whose conjugate pair Addendum 3 uses as its validation gate:

> **Proposition 2 ([MN],[Ma]).** Let `α, β ∈ Bₙ`. Then the following holds.
> **(1)** If `β` is represented by a braid word which contains `s` occurrences
> of `σ₁` and `k` occurrences of `σ₁⁻¹`, then `[β]_D < max{s,k}`.
> **(2)** `|[β]_D − [β′]_D| ≤ 1` if `β` and `β′` are conjugate.
> **(3)** `[αβ]_D ≤ 1 + [α]_D + [β]_D`.
> **(4)** If the closure of `β` admits destabilization or an exchange move,
> `[β]_D ≤ 1`.

**Convention checked, not assumed.** Ito's Remark 1 says his floor definition
*"is slightly different from one in `[Ma]`… rather after `[MN]`"*. Proposition 2
is stated in **Ito's** convention — which is what `_dehornoy.py` implements and
what was validated against Ito's three stated floors — so it applies to these
numbers directly, with nothing to reconcile.

### The search becomes a proof

[`meson_braid_floor_conjugacy_bound_probe.py`](../../computations/meson/meson_braid_floor_conjugacy_bound_probe.py),
4 assertions:

| braid | floor | `< max{s,k}` (2·1) | class max (2·2) | Theorem 2 reachable? |
|---|---:|---:|---:|---|
| `4₁ = (σ₁σ₂⁻¹)²` — **hyperbolic** | 0 | 2 | **1** | **no — by proof** |
| Borromean `(σ₁σ₂⁻¹)³` | 0 | 3 | 1 | no |
| meson `𝔐` | 1 | 3 | **2** | **no — by proof** |
| trefoil `σ₁³` | 0 | 3 | 1 | no |

`4₁` has floor 0, so by (2) **every** representative of its conjugacy class has
floor ≤ 1, against Theorem 2's required 3. Not "none found in 118 097 samples" —
**none exists**. Addendum 3 is therefore re-scoped **(a) → (b) structural
exclusion, invariant cited**, per AGENTS.md §"Before declaring refuted".

Two independent checks keep that from being circular. The implementation
respects **(1)** on every row — a theorem the handle-reduction code was not built
from. And **(2) is tight**: Ito's own conjugate pair differs by exactly 1, so the
bound is being applied at its sharp value, not vacuously. The 118 097-conjugate
search survives as corroboration, and corroborates twice: no counterexample, and
its raising control saturates the bound.

### Why I missed it, which is the more useful part

I grepped `Malyutin` in `library/INDEX.md` and `docs/` — and nowhere else. **`INDEX.md`
is one line per document.** A result *cited inside* a document the corpus holds is
invisible to it **by construction**, and Malyutin has no document of his own here.
AGENTS.md path 5 lists three tiers explicitly; **tier 1 answering "no" is not tier 3
answering "no"**, and I recorded the tier-1 miss as a corpus-wide absence in a
durable artifact — the exact over-claim the "Before declaring open" checklist exists
to prevent, committed while quoting the page that refuted it.

Neither Malyutin paper is ingested and neither could be: this sandbox's proxy denies
`arxiv.org` at CONNECT (403, policy), along with `export.arxiv.org`,
`link.springer.com` and `mathnet.ru`. They remain worth ingesting when reachable.
The citations, quoted verbatim from Ito's reference list in the ingested copy, are:

- **`[MN]`** A. Malyutin, N. Netsvetaev, *Dehornoy's ordering on the braid group
  and braid moves*, St. Petersburg Math. J. **15**, No. 3 (2004), 437–448.
- **`[Ma]`** A. Malyutin, *Twist number of (closed) braids*, St. Petersburg
  Math. J. **16**, No. 5 (2005), 791–813.

**No arXiv identifier is given here.** Ito's reference list supplies none for
either, and this sandbox cannot reach `arxiv.org` to check one — so any id would
be recalled, not verified, and this document has already paid once today for
stating an unchecked number. Nothing above waits on either paper.

### What does not change

The reading. Ito's threshold still sits at 18 crossings, and a genuinely hyperbolic
knot still cannot reach it — now as a theorem rather than a sample. Addendum 4's
split stands, and its point (1) is untouched, being about *kind* rather than reach.
Obstruction A is unchanged.

---

## Addendum 6 — the bridge claim that cannot hold (2026-08-25)

Addendum 4 makes a falsifiable prediction: if the atom object is not a link,
**no consumer may read a topological quantity off it.** Checked, on the 6 files
of 276 atom-word consumers that actually pair it with a topology call
(`snappy`, `knot_volumes`, `binding_link_volumes`, `_hyp_volume`).

**No consumer violates it.** The nearest candidate,
[`vol_t_he3_snappy_probe.py`](../../computations/deltalambda/vol_t_he3_snappy_probe.py),
is clean and got there first: it comments the averaged letters as *"Hecke element
`σ−h/2·1`, not a topological crossing"* and sweeps three readings
(`pos`/`neg`/`drop`) rather than silently picking one. It samples 2 corners of the
`2^(2A+1)`, which the sibling's later 32/32 SnapPy sweep completed — convergent,
and its `Vol = 0` verdict is unaffected.

### What the check did turn up

[`per_atom_hyperbolic_volume_witness.py`](../../computations/per_atom_hyperbolic_volume_witness.py)
does not read the atom object's volume — it uses a separate atlas of genuine
knots, correctly. But its docstring justified the substitution with:

> *"…distinct from the `atom_braid_word_3A(Z, N)` Hecke-algebra braid words which
> carry intra-block g₀/g₁ generators. **Same Markov class**, different topological
> realization."*

**A Markov class is a property of a braid, and this object is not one.** It sits
outside `im(ρ)` because `2A+1` of its letters are genuine averages, so there is
no class for the atlas knot to share. What it has is `2^(2A+1)` branch closures
whose classes generally differ. The sentence is not loose phrasing — it was the
**only stated bridge** between the two objects.

**No number moves.** The volumes are computed from the atlas knots directly and
never from the atom element, so this corrects a justification, not a value.
Corrected in place, with the census probe as its witness.

**And it cuts the opposite way from a reprieve.** A sibling established today
that three of the six atlas entries are an
[**admitted fit**](2026-08-25-knot-id-is-an-admitted-fit.md) — the knot chosen for
volume proximity to `B_AME`. That is a *different* defect from this one, and the
two compose badly: this removes the one principle that had been offered in place
of the fit. Whether `p`/`n`'s `"principled-derivation"` tag rests on a derivation
elsewhere is **not established here** and is the obvious next question.

### Scope

Isolated, not propagated: corpus-grep finds this the **only** live instance of the
claim. **(a)** — a documentation defect in a stated justification. It is *not* a
claim that the atlas assignment is wrong, that any volume is wrong, or that the
binding numbers move; none of that follows, and none is asserted.

---

## Addendum 7 — my suspicion was wrong, and the real defect is next door (2026-08-25)

Addendum 6 ended by asking whether `p`/`n`'s `"principled-derivation"` tag rests on
a real derivation or on the bridge claim I had just removed. **It rests on a real
one.** From
[`recursive-atom-knot-atlas-interpretation.md`](../../content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas-interpretation.md):

> *"For `principled-derivation` entries (electron, proton, neutron) the hyperbolic
> volume of the Markov closure is computed from the **σ-braid word** at ≥ 50 decimal
> digits via `hp_volume_of_link_closure(braid_word, digits=50)`…"*

That braid word comes from `def:confined-particle` — the GB-NF particle registry's
canonical `T_w` — and **is** a braid, so its Markov closure has a genuine volume.
Nothing there routes through the atom Hecke element. So the worry is answered in the
corpus's favour: **three of six atlas entries are an admitted fit, not six.**
Recorded as a negative because it was my suspicion and it failed.

### What the same page does show

That block names its provenance chain and asserts the guarantee that makes the atlas
trustworthy:

> *"…[`witness_staleness_tracker.py`] marks the affected entries stale and the atlas
> is recomputed from the sources above; **no entry is maintained by hand**."*
> …and *"The atlas is auto-rendered by [`recursive_atom_knot_atlas_render.py`]."*

**Both producers are deprecated.** Neither exists at the path the block links
(`computations/<name>.py`); both sit in `fsh-guts/deprecated/computations/`. Meanwhile the
live producer,
[`per_atom_hyperbolic_volume_witness.py`](../../computations/per_atom_hyperbolic_volume_witness.py),
carries a **hand-written `ATLAS` dict** with hardcoded knot names and braid words.

So the guarantee is **unenforced**: the auto-render is retired, the staleness tracker
that would flag drift is retired, and what actually emits the committed
`per-atom-hyperbolic-volume.witness.json` is exactly the hand-maintained table the
sentence promises does not exist. Two dead links in a published content block, and
the sentence between them no longer describes the pipeline.

### Scope

**(a)**, and deliberately narrow. This says **nothing** about whether any atlas
volume is *wrong* — the values may well be correct, and the `p`/`n` derivation above
is sound. What is established is that the block's stated freshness mechanism no
longer runs, so nothing currently detects drift between the registry's `T_w` and the
hardcoded words. **Not fixed here**: repairing the content block needs a sidecar
refresh and the render-QA gate, which would widen a docs-and-probes PR. Beaned.
