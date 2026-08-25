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
