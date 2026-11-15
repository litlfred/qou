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

> **🛑 CORRECTED 2026-08-30 — the sentence that stood here was wrong, and the
> lead it introduced is now CLOSED. Read this before the paragraph above.**
>
> **What I asserted:** *"Corpus-grep: `q-Plancherel` appears nowhere in
> `computations/`, `content/` or `docs/`. This is a genuine gap, not a
> re-derivation."*
>
> **What is true.** Measured with
> `grep -ril "q-plancherel\|q_plancherel" computations/ content/ docs/`:
> **202 live files**, plus 8 under `fsh-guts/deprecated/computations/` and 16 beans.
> The corpus carries content blocks named
> `prop:q-plancherel-asymptotic-skeleton` and
> `conj:q-plancherel-asymptotic-skeleton`, and `computations/deltalambda/`
> uses a weight it calls *"Ocneanu / q-Plancherel"* throughout. My grep was
> too narrow. **An absence is a measurement, and I did not make it** — this is
> the negative-result failure mode this repo's own §"Terse ≠ compressed"
> names: *"I found no rationale"* and *"there is no rationale"* are different
> claims and only one of them was measured.
>
> **What survives, and it is narrower but sharper.** The corpus's
> *"q-Plancherel"* is a **DIFFERENT object** from the paper's — established
> symbolically, not by inspection:
>
> | | corpus `W_λ` (s5-so3 keystone) | paper `M_{n,q}` (arxiv-1001.2180v2) |
> |---|---|---|
> | formula | `d_q(λ)²/[n]_q! = [n]_q!/∏[h]_q²` | `Q^{b(λ)}·dim λ/∏{h}_Q` |
> | q-integer | balanced `[m]_q` | unbalanced `{m}_Q` |
> | hooks | squared | first power |
> | `dim λ` | absent | classical, in the numerator |
> | `Σ_λ` | **not 1** (see below) | **1 exactly**, every `n`, every `Q` |
> | `q → 1` | `(dim λ)²/n!` | `(dim λ)²/n!` |
>
> They are unequal at every partition for `n = 2,3,4`, and agree only at
> `q = 1` — which is why both carry the name. So the paper's measure is
> genuinely unused; the *name* is not free, and future work must say which
> q-Plancherel it means.
>
> **A second measurement — and my first reading of it was ALSO wrong.**
> `Σ_λ W_λ` at `q₀` is 0.99458 (n=2), 0.98744 (n=3), 0.98217 (n=4), 0.98222
> (n=5), **1.11092 (n=9)** — not 1, not monotone. I first wrote that this made
> the (C5) reference object "mis-normalized in the corpus" and that the right
> denominator is `D² = Σ_μ d_q(μ)²`. **Both halves are retracted**, caught by
> corpus-grep path 6 (the beans), which is exactly the path this repo added for
> this failure:
>
> - **It is not a defect.** The owner ruled on 2026-08-16, in
>   [`notation/notation-collisions.md`](../../content/quantum-observable-universe/notation/notation-collisions.md),
>   that `Σ_λ w_λ(q) ≠ 1` at `q ≠ 1` **by design** — *"Never write a
>   normalisation claim on bare `w_λ`"* — quoting **0.987 at n=3** and
>   **1.051 at n=8**. My numbers reproduce the ruling's independently. The
>   retracted claim would have broken that ruling in the opposite direction.
> - **`Σ_μ d_q(μ)²` is not canonical either.** Bean `qou-sf1t` states that
>   `QPlancherel.sum_measureOn_eq_one` is *"NOT evidence that `Σ_λ d_q(λ)²` is
>   the canonical normaliser for the Ocneanu weights"* — it is one line from
>   `Finset.sum_div`, true by construction for any self-normalised family. A
>   sibling's 2026-08-29 `n = 3` result identifies the actual normaliser as the
>   **Molien perfect square** `Z = (q² − qz − 1)²`, neither `[n]_q!` nor
>   `Σ_μ d_q(μ)²`.
>
> **What replaces it is stronger than what it replaces.** `W_λ` is
> conjugation-symmetric — `λ` and `λ'` share a hook multiset and `[n]_q!`, so
> `W_λ = W_{λ'}` exactly (verified for `n = 2,3,4,5`). At `n = 2` that forces,
> for **every** normalisation constant `c`,
>
>     z = c·[W_(2)·q + W_(1,1)·(−q⁻¹)] = c·(q²−1)/(q²+1) = c · 0.1039637101
>
> so reaching `m* = 0.4443787009` needs `c = 4.2743636`, i.e. a normaliser
> under which `Σ_λ W_λ = 0.23395295` — about 4.3× away from any
> probability-like normalisation, and in the wrong direction from both the raw
> 0.99458 and the self-normalised 1. **So no choice of normaliser rescues the
> `d_q²` weight**, and the live question of which normaliser is canonical does
> not bear on this conclusion at all. That is a normalisation-independent
> exclusion of the whole family, not a miss by two evaluated numbers.
>
> **And the lead itself is CLOSED.** Pushed through the corpus's own canonical
> weights → parameter map `y_lambda_su_n.z_from_weights`:
>
> | weight system | implied `z` at `q₀` | verdict |
> |---|--:|---|
> | corpus `y_λ` (convention D, production) | 0.612688037 | **above** the `1/√5` ceiling — excluded, `det(I+G) < 0` |
> | corpus `W_λ = d_q²/[n]_q!` (as used) | 0.103963710 | admissible, far below `m*` |
> | corpus `W_λ` self-normalized (`Σ = 1`; **not** the canonical normaliser) | 0.104530149 | admissible, far below `m*` |
> | paper `M_{n,q}` (generic degrees) | **0 exactly** | at the floor; `b4(0) = 0`, no binding |
> | *needed for `\|μ₄\| = 4.591`* | *0.444378701* | *(C1): saturates the ceiling* |
>
> The paper's `z = 0` is not a numerical near-miss but a definitional
> consequence: `M_{n,q}` decomposes the **regular** trace, and
> `τ_q(T_σ) = 0` for every `σ ≠ id`; `σ₁ = T₁/q` is such an element. **The
> same one-line argument excludes the entire regular-trace/Plancherel family**,
> including classical Plancherel at `q → 1`, so the search restricts to Markov
> traces and their deformations from the outset. That exclusion is worth more
> than the lead was.
>
> Scope: **(a)** for the interface — this weight system does not supply `m`;
> the gate's surjectivity wall is untouched and the magnitude stays open.
> Measured in
> [`computations/probes/q_plancherel_vs_y_lambda_probe.py`](../../computations/probes/q_plancherel_vs_y_lambda_probe.py),
> witness `q-plancherel-vs-y-lambda.witness.json`, 23 checks, all exact
> (sympy) — the discriminators are decided symbolically, never by comparing
> floats to a tolerance. Bean `qou-ntck`.
>
> Superseded text follows.

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
