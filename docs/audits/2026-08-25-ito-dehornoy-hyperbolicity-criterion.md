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
