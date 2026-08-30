# Why `w` rises at `z=1` and turns over at the α — the negative half is closed

**Date:** 2026-08-30
**Bean:** `qou-edt7`
**Lean:** `QOU/Mass/UniformBondSimpleGraphExclusion.lean` — sorry-free, `lean`-direct exit 0, axioms clean
**Probe:** `computations/probes/coordination_weight_rise_and_turnover_probe.py` — 4/4
**Builds on:** `QOU.Mass.CoordinationWeightDifferences` (merged `d58f98165c`), `QOU.Mass.CoordinationSaturation`, `QOU.MassTheory.AggregatorConvexityDichotomy` (`qou-82mc`)

## The question

`b₃ = +1.426220 MeV > 0` is, exactly, *"the coordination weight `w(z) = B(A)/C(A,2)`
rises from `z = 1` to `z = 2`"*. Saturation of `B/A` is, exactly, *"`z·w(z)` is
bounded"*. So `w` is forced non-monotone, and the question is **why it rises and
why it turns over**.

**The negative half is now closed, and the answer is sharper than expected. The
positive half is not, and two candidate mechanisms are refuted below.**

## 1. The rise is not about which pairs bind — proved

Let the binding be a **uniform bond weight `ε` summed over a simple graph**,
`B(A) = ε·e(A)`. Then

    b₃ = ε·(e(3) − 3·e(2)) ≤ ε·(3 − 3) = 0

because a simple graph on three vertices has **at most three edges** and a bonded
pair has at least one. `b3Uniform_nonpos`. That is the whole proof — a counting
bound, with **no monotonicity, no degree cap, and no relation assumed between one
mass number and another.**

This is strictly stronger than what the corpus had. `CoordinationSaturation`
checks two endpoints — complete-graph coordination cannot saturate,
bounded-degree does — and concludes saturation forces bounded degree. Read
through the coordination weight, a degree function `d` gives `w(z) = ε·d(z+1)/z`,
so:

| coordination | `w(z)` | `b₃` |
|---|---|---|
| complete, `d = z` | `ε`, constant | `= 0` (`coordWeight_complete`) |
| bounded, `d = k` | `εk/z`, decreasing | `< 0` (`coordWeight_bounded_inv`) |
| chain, `e(3) = 2` | — | `= −ε < 0` (`b3Uniform_neg_of_chain`) |

One might hope some intermediate profile — complete at small `A`, saturating at
large `A` — could rise at the bottom. **It cannot**: `d(3) ≤ 2` for any simple
graph, which is the `e(3) ≤ 3` bound. **The entire coordination-multiplicity
family is excluded as a source of `b₃ > 0`**, not merely the two endpoints.

**Scope.** This is a case-(b) structural exclusion per AGENTS.md: the invariant is
a proved counting bound, cited, not a probe that came out badly. What is excluded
is the *conjunction* "uniform bond weight" ∧ "simple graph". Dropping the second
means multi-edges or a genuine three-body bond. Dropping the first is the physical
reading, and is where everything now sits.

## 2. So the rise is non-transferability, and it is 21.4 %

With a complete graph and a coordination-dependent weight `ε(z)`, `w(z) = ε(z)`,
and `b₃ > 0` says precisely

    ε(2) / ε(1)  =  2.6999729 / 2.2245662  =  **1.2137076**

The bond is **21.4 % stronger at coordination 2 than at coordination 1**, and at
coordination 3 it is 112 % stronger. That number is what a derivation has to
produce.

## 3. Single-ratio (Markov-power) scaling — REFUTED, for every `r`

QOU has a native mechanism for non-transferability. The Markov trace satisfies
`tr_{n+1}(β σ_n^{±1}) = z^{±1} tr_n(β)`, so embedding a two-strand bond in an
`n`-strand braid multiplies by a power of the Markov parameter. A bond weight is
therefore **not** an `n`-independent object at `z ≠ 1` — which is exactly the kind
of thing the rise needs.

The simplest quantitative form of that is `ε(z) = ε(1)·r^{z−1}` for some constant
`r`. Measured:

| ratio | value |
|---|---|
| `ε(2)/ε(1)` | 1.2137076 |
| `ε(3)/ε(2)` | 1.7466633 |
| disagreement | **43.9 %** |

**No constant `r` fits.** The refutation is independent of *which* `r` — a single
ratio of any value cannot produce two ratios 44 % apart — so it does not depend on
the convention that fixes `z` (`z_D = 0.6126880`, `z_C = 0.4993203`, `1/z_D =
1.6321520`; none is either measured ratio anyway).

**Scope (a):** this refutes the *single-ratio* family. It does **not** exclude the
Markov mechanism, which could enter with an `n`-dependent exponent or alongside
other terms. The mechanism survives; its simplest form does not.

## 4. The turnover LOCATION is forced — by a support bound, not a positivity claim

The Wigner SU(4) fully antisymmetric spin-isospin representation `[1^n]` has
`dim = C(4,n)`:

| n | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `dim [1^n]` | 4 | 6 | 4 | 1 | **0** | **0** |

It **vanishes for `n ≥ 5`**. So the regime in which every nucleon shares one
maximally symmetric spatial state ends exactly at `A = 4` — and the measured peak
of `ε(z)` is at `A = 4`. **The location is forced with no free parameter.**

Two caveats, both asserted in the witness rather than only written here:

* it locates the peak and **says nothing about its height**;
* the step from *maximal spatial symmetry* to *maximal binding* is **Wigner's
  physical assumption**, which this corpus does not derive.

> **A prior over-claim of mine, recorded so it is not repeated.** An earlier probe
> argued from `C(4,n) > 0` to a conclusion about the **sign** of a body-order term.
> That was wrong: positivity is analytic, true of any positive-weight object, and
> discriminates nothing. The claim here is a different one — a **finite support
> bound**, `C(4,n) = 0` for `n ≥ 5`. Vanishing is not positivity.

## 5. Same-orbital pair fraction — REFUTED beyond A = 7

If only pairs sharing the s-shell carried full weight, `w` would track the
same-orbital pair fraction. Normalised at the α (one parameter):

| A | fraction | predicted | measured | error |
|---:|---:|---:|---:|---:|
| 5 | 0.600 | 2.8295662 | 2.6330662 | 7.5 % |
| 6 | 0.467 | 2.2007737 | 2.1329325 | 3.2 % |
| 7 | 0.429 | 2.0211187 | 1.8688134 | 8.1 % |
| 9 | 0.444 | 2.0959750 | 1.6156673 | **29.7 %** |
| 12 | 0.515 | 2.4294256 | 1.3963899 | **74.0 %** |
| 16 | 0.600 | 2.8295662 | 1.0634943 | **166.1 %** |

Three points under 8 % followed by a 30 % miss at the next point is a
coincidence, not a law. **Scope (a):** this model *alone* fails; the ingredient is
not excluded from a multi-term closure.

## What is left

The **size** of the rise. Why `ε(2)/ε(1) = 1.2137` and `ε(3)/ε(1) = 2.1200`? No
mechanism tested here predicts either number, and nothing in this document derives
a magnitude. What it does is remove a large family from the search — every
uniform-bond simple-graph assembly, proved — and reduce the remaining question to
a single, sharply stated quantity.
