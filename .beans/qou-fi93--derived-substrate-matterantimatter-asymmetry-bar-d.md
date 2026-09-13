---
# qou-fi93
title: 'Derived substrate matter/antimatter asymmetry: bar_defect r(z)-r(-z) = (10/27)z(4z^2+3), 7.88% at q0; connect to number density or state the gap'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T12:53:38Z
updated_at: 2026-09-13T11:20:01Z
---

ANSWERED 2026-09-07 (audit sec 17), bean kept OPEN per 13a. The 7.878% colour-curve asymmetry CANNOT reach a number density by any route the framework currently defines. Every counting object is bar-even, exactly: [n]_q = (q^n-q^-n)/(q-q^-1) negates numerator and denominator under q->1/q, so it is exactly bar-even; d_q(lambda) is a ratio of products of [n]_q via the q-hook-length formula, hence bar-even (measured worst 1.378e-40 at dps 40 over n=3,4); the Plancherel measure d_q^2/D^2 inherits it (3.444e-41, sum mu = 1.0); and sum_lambda y_lambda is bar-even to 40 digits (sec 14.1). The asymmetry lives in the colour GEOMETRY; the counting lives in bar-even measures; they do not couple. Scope (b), invariant = bar-evenness of the q-integers. CONSTRUCTIVE consequence: baryogenesis in QOU needs a counting measure NOT built from q-integers — a new structural object, not a tuning — which rules out re-weighting y_lambda, re-normalising mu, or picking a different partition measure. Also corrects sec 10.1's caveat: the 7.878% is not eight orders FROM eta, it is DISCONNECTED from eta; a magnitude gap invites a search for a suppression factor and there is no channel to suppress. RESIDUAL (why this stays open): no OTHER route is excluded — a constructed coupling between the colour geometry and a density is not ruled out.


---

## 2026-09-13 — the bar-odd channel is NOT missing from the framework; it is DIVIDED OUT

This bean's scope-(b) exclusion stands untouched. What changes is its
**constructive consequence**, which said baryogenesis here *"needs a counting
measure NOT built from q-integers — a new structural object, not a tuning."*
Such an object is already in the corpus, and the reason the counting measures
are bar-even turns out to be a **mechanism** rather than an observation.

Route in: `qou-hjs8` established that `def:crossing-energy` makes `E_cross` a
SUM of degree-(+-1) terms, `n_+ q - n_- q^-1`, and that the mirror sends
`q <-> q^-1`. A sum of `q` and `q^-1` with unequal coefficients is **not
bar-even** — so this bean's survey had an object it did not examine.

### The split, exact

    E_cross(q) + E_cross(1/q) = (n_+ - n_-)(q + q^-1) = w   (q + q^-1)
    E_cross(q) - E_cross(1/q) = (n_+ + n_-)(q - q^-1) = n_c (q - q^-1)

| | carries | topological meaning |
|---|---|---|
| bar-EVEN part | `w = n_+ - n_-` | the **writhe** |
| bar-ODD part | `n_c = n_+ + n_-` | the **crossing number** |

Two counting integers, on **opposite** bar-parities. And the mirror swaps
`n_+ <-> n_-`, so it **negates the writhe and PRESERVES the crossing number**
— the bar-odd part is the mirror-invariant one.

### Why the q-integers have no bar-odd content

`[n]_q = (q^n - q^-n)/(q - q^-1)` is bar-even **because it is a ratio of two
bar-ODD objects** — numerator and denominator each negate under the bar, and
the signs cancel. Verified symbolically for each factor separately.

So the bar-evenness this bean measured across `[n]_q`, `d_q(lambda)`, the
Plancherel measure and `sum y_lambda` is not an absence of bar-odd structure:
it is the **same factor `(q - q^-1)` appearing twice and cancelling**. The
crossing energy is the object that keeps it undivided. That is the whole
difference between the two.

### The candidate, obtained by NOT dividing

    q^n - q^-n  =  [n]_q * (q - q^-1)

is bar-ODD, indexed by an integer, and not a q-integer — the shape this bean
specifies. It introduces **no free parameter**, because it is obtained by
omitting a division rather than by adding anything.

### A numerical tie to qou-hjs8, and it is not a coincidence

At the proton pin the crossing energy's **bar-odd / bar-even ratio is
0.10396371005241014568** — the *same* number `qou-hjs8` computed as
`delta_CP = tanh(ln q0)`. It must be: `delta_CP` compares `|3q|` against
`|3/q|`, which IS the odd/even ratio. So `qou-hjs8`'s discriminant is
**identified**: it is the crossing energy's bar-odd fraction.

### WHY THIS BEAN STAYS OPEN (and it is not just §13a)

* **No number density is reached.** This exhibits a bar-ODD object carrying a
  counting integer. It does **not** construct the coupling to a density that
  this bean says is missing. The gap moved; it did not close.
* **`q^n - q^-n` is not SELECTED, only exhibited.** It is the obvious bar-odd
  companion to `[n]_q`. Choosing it *because* it has the wanted parity would
  be selection against the target, which §NO FITTING forbids. What is derived
  is the mechanism (division by a bar-odd factor destroys bar-odd content),
  not the choice of object.
* **The 7.878 % colour-curve asymmetry is untouched.** Nothing here connects
  it to the crossing number.

Artifacts: `computations/barparity/crossing_energy_bar_split_probe.py` (exact
sympy, one mpmath mpf at 60 dps, no float64, rc 0);
`QOU/Observations/CrossingEnergyBarSplit.lean` (6 declarations, sorry-free,
`lean`-direct exit 0 with zero output, generic over a Field with no anchor).
