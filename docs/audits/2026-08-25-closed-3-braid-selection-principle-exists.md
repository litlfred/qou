# The selection principle exists, it is a classification theorem, and it is not optimization

**Date:** 2026-08-25 · **Bean:** `qou-v7qj` · **Source:** newly ingested
`library/pjm-v161-n1-p02-p/` (Birman–Menasco, *Studying links via closed braids
III: classifying links which are closed 3-braids*, Pacific J. Math. **161**
(1993)), with `library/arxiv-0802.1072v2/` (Birman–Menasco, *A note on closed
3-braids*) and `library/arxiv-math-0606435v2/` (Stoimenow, *Properties of closed
3-braids*).

## Where this thread had got to

Two structural negatives closed the operator-selection LP from both directions:

- **No objective works.** `NF(𝓑₃)` is relative-interior (all six Frobenius
  constraints strictly slack, min `0.342489`), and a linear functional attains
  its extrema on a face — so no linear objective selects it.
- **No invariants work.** `χ_sym`, `χ_alt`, `det ρ_std` and `tr_M(x)` are class
  functions, so no collection of them separates conjugate elements. Measured:
  37 of 38 `(e, tr_M)` classes over words of length 1–5 hold more than one
  distinct NF vector, `σ₀` and `σ₁` among them.

The open question was what *non-invariant* data picks the word. **The literature
answers it, and the answer had been sitting unread in `library/` since it was
ingested in #5707.**

## The principle, in three steps

**1. Link type → conjugacy class.** Birman–Menasco's Classification Theorem
(Version I), `sec-001`:

> *A link `𝓛` which is represented by a closed 3-braid admits a **unique
> conjugacy class** of 3-braid representatives,* with exactly three exceptional
> families:
>
> | | exception | classes |
> |---|---|---|
> | (i) | the unknot | 3 — `σ₁σ₂`, `σ₁⁻¹σ₂⁻¹`, `σ₁σ₂⁻¹` |
> | (ii) | type `(2,k)` torus links, `k ≠ ±1` | 2 |
> | (iii) | links admitting *braid-preserving flypes*: `σ₁^p σ₂^q σ₁^r σ₂^δ`, `p,q,r` distinct with `\|·\| ≥ 2`, `δ = ±1` | ≤ 2 |

**2. Conjugacy class → canonical word.** Same section: the conjugacy problem in
`B₃` has several algorithmic solutions, *"each yielding unique normal forms for
conjugacy classes"* (Schreier; Birman–Menasco note a second program producing
these normal forms directly).

**3. Therefore the word is determined** once the link is named — canonically,
not by fitting.

## `𝓑₃` is in the generic case

Checked against all three exceptions:

| exception | does `𝓑₃ = (σ₀σ₁⁻¹)³` fall in it? |
|---|---|
| (i) unknot | **no** — it is the Borromean rings, 3 components, `Vol = 7.32772475342` |
| (ii) `(2,k)` torus link | **no** — Brunnian, not a torus link |
| (iii) flype family | **no** — the flype words need `\|p\|,\|q\|,\|r\| ≥ 2`; `(σ₀σ₁⁻¹)³` has every exponent `±1` |

**So the Borromean link determines its 3-braid conjugacy class uniquely.** The
selection that the LP could not perform is performed by the classification
theorem, from topological input.

## And a direct consequence for Obstruction A

The corpus's meson braid `𝔐 = (σ₀σ₁)²σ₁σ₀` closes to **T(2,5)** (established in
#5702 via the knot group, relator `aabbbbb` ⇒ `⟨a,b ∣ a² = b⁵⟩`). That is
exception **(ii)** with `k = 5`.

So `𝔐` does **not** have a unique 3-braid representative — its link type admits
**two** conjugacy classes. Any argument that treats "the meson braid" as
determined by its closure is under-specified for exactly this link, and the
ambiguity is a known one rather than a defect in the corpus.

## What this means for `prop:operator-selection-lp`

Its defensible role was already narrowed to **verification** — `𝓑₃` is strictly
feasible against the Frobenius structure, min slack `0.342489`, which is a real
certificate. This audit supplies what it was being asked to do instead: the
selection is topological, and the classification theorem makes it canonical.

The corpus should say so directly. The physics names a **link**; Birman–Menasco
turns that into a conjugacy class; the normal form turns that into a word. No
optimization enters, and none can.

## Scope

- The classification is for **braid index 3**. Nothing here extends to `H_n`,
  `n > 3` — Birman–Menasco are explicit that the pathologies of III, IV and V
  all obstruct the generalisation.
- Read from the ingested OCR/text sections. The exception list and the
  uniqueness statement were read off `sec-001`; the (iii) flype family's text is
  OCR-damaged in places (`σfσ|σ[σ|`) and the exponent conditions are quoted from
  the surrounding prose, which is legible. Anyone relying on the precise flype
  form should check the PDF page rather than the section text.
