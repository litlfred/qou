# What categorical principle could fix `m` — the characteristics, worked backwards, and one literature match

**Date:** 2026-08-30 · **Branch:** `claude/mu4-magnitude-gap-2026-08-30`
**Scope:** (a). Nothing wired, no target inverted, no constant fitted. This is a
*specification* of what a closing principle must satisfy, plus a search for
candidates that meet it.

## 0 · Why this is the only remaining move

`a4-interface-magnitude-one-scalar-gate` establishes that
`b4(m) = −ln[(1−5m²)(1−m²)]` on `m ∈ (0, 1/√5)` is **surjective onto (0,∞)**:
every target is reachable and each reaching `m` is a function of the target.
So the magnitude cannot be closed by computation — only by a principle that
**fixes `m` independently of the target**. This document asks what such a
principle would have to look like.

## 1 · The characteristics, measured

Using the gate's own closed-form inverse
`m*(t) = √[(6 − √(16 + 20e^{−t}))/10]`:

| target | required `m*` | `1/√5 − m*` | `db4/dm` | digits of `m` needed for 1 % on `b4` |
|---|--:|--:|--:|--:|
| `b4 = 9.243` | 0.4471865428 | 2.71e-5 | 3.70e4 | **6.2** |
| `\|μ₄\| = 4.591` | 0.4443787009 | 2.83e-3 | 3.53e2 | **4.2** |
| `B(⁴He) = 28.296` | 0.4472135955 | 1.44e-13 | 6.95e12 | **14.5** |

**(C1) The required `m` saturates the writhe ceiling from below.** It is not
"somewhere in `(0, 1/√5)`" — it is pinned against the top of the interval.

**(C2) The precision demanded is target-dependent and spans ten orders.** This
is the practical discriminator, and it splits the problem:

- For **`μ₄`** — the object actually at issue — a principle need only supply `m`
  to **~4 significant figures**. That is squarely in range for a derived
  categorical constant, so **this route is alive for `μ₄`**.
- For **`B(⁴He)`** it needs **~14.5 figures**. No categorical principle produces
  fourteen digits "naturally"; that is fine-tuning, not derivation. **This route
  is effectively dead for the full binding**, and should stop being described as
  merely open.

That distinction has not been drawn before and it is the main content here.

**(C3) The principle must produce a suppression.** The canonical convention-D
Markov bond factor is `z_D = 0.6126880371`, which is **above** the ceiling and
hence excluded outright. The needed `m` is `≈ 0.73 × z_D`.

**(C4) It must live where `√5` lives.** The ceiling is `1/λ_max` with
`λ_max = √5`, the largest `[1⁴]` exchange eigenvalue. Note the exact identity

    1/√5 = φ/(φ² + 1),   φ = (1+√5)/2

(verified exactly, difference 0). Read honestly this is an identity *about √5*
rather than an independent fact about Markov parameters — but it does say the
ceiling is the golden-ratio trace point, `√5 = φ + φ⁻¹`. A constant of this
shape arises categorically in **Fibonacci / Yang–Lee** structures, which is
where to look.

**(C5) Stated by the gate itself:** the object wanted is *"a normalized `W`
strictly below `d_q²/D²`"* — i.e. a normalized weight lying **below the
Plancherel/Verlinde weight**.

## 2 · Working backwards: what kind of object satisfies (C1)–(C5)?

A **principled deformation of the Plancherel measure**, derived from the Hecke
structure the framework already uses, whose normalized weight sits below
`d_q²/D²`. Not a free scalar — a measure with its own definition.

## 3 · The literature match, and it is not cited in this corpus

**`library/arxiv-1001.2180v2` — *Asymptotics of q-Plancherel measures*.**

Its definition is exactly the required shape:

    M_{n,q}(λ) = D_λ(q) · dim λ / {n!}_q

where `dim λ` is the `S_n` irrep dimension and **`D_λ(q)` the generic degree**
(Geck–Pfeiffer Ch. 8). Its §2.2 is titled **"Link with representation of the
Hecke algebra"** — the corpus's own setting: `H_n(q)`, Wedderburn blocks indexed
by `λ`, weights `y_λ`.

**Corpus-grep: `q-Plancherel` appears nowhere in `computations/`, `content/` or
`docs/`.** This is a genuine gap, not a re-derivation.

Secondary candidates from the same shelf, in rough order of fit:

| doc | why it might bear |
|---|---|
| `arxiv-1402.4615v3` | Jack-polynomial (`α`) deformation of Plancherel — a *second* one-parameter family, useful as a control |
| `arxiv-math-0606222v2` | *Quantum dimensions and their non-archimedean degenerations* — quantum dimensions in the framework's own non-archimedean register |
| `arxiv-math-0111205v1` | *From Subfactors to Categories and Topology II* — the `Z(C)` centre; where `d²/D²` normalisations are established |

## 4 · The test to run, and the order to run it in

**Do not compute "which `D_λ(q)` hits 0.4444" — that is anchor inversion.** The
honest sequence is derive-then-check:

1. **First, settle whether this is even new.** The corpus's `y_λ` come from the
   Wenzl bridge (quantum-dimension-flavoured). The q-Plancherel weight comes
   from **generic degrees**. Are these the same object under two names? If yes
   the lead collapses; if no, there are two inequivalent Hecke weights in play
   and the interface may want the other one. **This is the cheapest step and
   gates everything after it.**
2. Compute the q-Plancherel normalized weight at `q₀` for the `[1⁴]` block
   structure, **with the target not consulted**.
3. Only then compare against `m* ≈ 0.4444` and the `d_q²/D²` bound, and report
   whichever way it lands.
4. If it misses, the Jack-deformed family is the pre-registered second control.

## 5 · What is NOT claimed

That the q-Plancherel measure closes the gap — untested. That `m` must equal any
particular value. That the golden-ratio identity in (C4) is more than an
identity about `√5`. That `B(⁴He)` is formally excluded — (C2) says the
precision demand makes it a fine-tuning, which is a conditioning argument, not a
proof of impossibility. No constant here is fitted and no target was inverted:
the `m*` values are diagnostics of what the mechanism *would* require, computed
from the gate's own published inverse.
