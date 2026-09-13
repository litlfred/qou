---
# qou-fi93
title: 'Derived substrate matter/antimatter asymmetry: bar_defect r(z)-r(-z) = (10/27)z(4z^2+3), 7.88% at q0; connect to number density or state the gap'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T12:53:38Z
updated_at: 2026-09-13T14:21:01Z
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


--------

## 2026-09-13 (later) — the "exhibited, not selected" residual is DISCHARGED: the bar-odd channel is FREE OF RANK ONE

PR #7313, issue #7312, branch claude/fi93-bar-odd-rank-one-2026-09-13.
Lean QOU/Observations/BarParityRankOne.lean (20 decls, sorry-free);
probe computations/barparity/bar_parity_rank_one_probe.py (rc 0).

THE RESIDUAL THIS ANSWERS is the second bullet of the append above, in its
own words: *"q^n - q^-n is not SELECTED, only exhibited. It is the obvious
bar-odd companion to [n]_q. Choosing it because it has the wanted parity
would be selection against the target, which sec NO FITTING forbids."*

That objection was correct. It is discharged not by arguing the object is a
good choice but by proving THERE IS NO CHOICE.

### The theorem

Over Z[q,q^-1] with the bar involution q -> q^-1, the bar-ODD part is a FREE
RANK-ONE module over the bar-EVEN part, generated by (q - q^-1):

    f is bar-odd   <=>   f = (q - q^-1) * g   with g bar-even

bijectively (isBarOdd_iff, inverted by div_skein_barEven). So q^n - q^-n is
not one bar-odd candidate among many -- EVERY bar-odd object factors through
the same generator, and the generator is itself the n=1 member of the family
(skein_eq_qPowOdd_one). Selection-against-the-target needs competitors; there
are none. Picking q^n - q^-n is picking a representative of the whole
channel.

### The rank is over Z, and that is the load-bearing half

A nonzero determinant would give only a Q-VECTOR-SPACE isomorphism, leaving
room for a bar-odd object that is NOT (q - q^-1) times an INTEGRAL bar-even
one -- i.e. the generator spanning a finite-index sublattice. The probe
builds both integral bases (O_k = q^k - q^-k, k=1..N; E_0 = 1, E_j = q^j +
q^-j, j=1..N-1) and takes the determinant of the transition matrix:
|det| = 1 -- UNIMODULAR -- at every window N = 1..12. Both claims are
reported separately in the probe because they are different claims.

### The generator is not a new object either

(q - q^-1) is the HECKE STRUCTURE CONSTANT. From sigma^2 = (q - q^-1) sigma
+ 1 (AGENTS.md sec 7a), multiplying by sigma^-1 gives sigma - sigma^-1 =
q - q^-1, which is the skein relation L_+ - L_- = (q - q^-1) L_0.
Equivalently it is the TRACE of sigma's two eigenvalues q (symmetric
channel) and -q^-1 (antisymmetric), whose product -1 is bar-even; the bar
EXCHANGES the two channels up to sign (verified symbolically). So the
bar-odd channel is generated by the separation between the two statistics
channels.

### Why the counting measures are bar-even, as a theorem

IsBarOdd.div_barOdd: a ratio of two bar-odd functions is bar-even. [n]_q is
exactly such a ratio. This bean's original measurement -- [n]_q, d_q(lambda),
d_q^2/D^2 and sum y_lambda all bar-even to 40 digits -- is therefore not an
absence of bar-odd structure but ONE FACTOR DIVIDED OUT, now proved rather
than observed.

### delta_CP is EXPLAINED, not re-observed

Probe sec 5, proton pin, 60 dps: (q0 - 1/q0)/(q0 + 1/q0) =
0.103963710052410145676652858536, agreeing with tanh(ln q0) to 9.7e-63.
qou-hjs8's delta_CP IS the bar-odd fraction of the degree-one channel. That
was previously a coincidence of two computed numbers; it is a consequence
now.

### Verification

lean-direct with -DautoImplicit=false -s 65536: exit 0, zero output, 0
sorry. #print axioms on the five load-bearing theorems: [propext,
Classical.choice, Quot.sound] only. Generic over a Field, no anchor, no R
(sec 7c). Two hypothesis facts, both narrower than one would guess: the
CHARACTERISTIC enters in exactly one place (IsBarOdd.eq_zero_of_inv_self,
2 != 0) and only at the bar's fixed points q^-1 = q, which is precisely
where the generator vanishes; and skein_eq_zero_iff needs NO hypothesis at
all, because in a field 0^-1 = 0 so both sides are literally the same
expression there.

### WHY THIS BEAN STILL STAYS OPEN (sec 13a)

Of the three residuals recorded above, ONE is discharged and TWO are not:

  * DISCHARGED — "not selected, only exhibited".
  * STILL OPEN — NO NUMBER DENSITY IS REACHED. Nothing here couples the
    bar-odd channel to a density, an eta, or any observable. The scope-(b)
    exclusion is untouched and still stands. This settles WHICH object
    carries bar-odd content, not WHETHER that content reaches an observable.
  * STILL OPEN — the 7.878 % colour-curve asymmetry is nowhere in this work.

And one thing deliberately NOT claimed: the skein relation
L_+ - L_- = (q - q^-1) L_0 is SUGGESTIVE of the missing coupling -- it
equates a crossing-difference with the generator times a smoothing -- but
reading (matter - antimatter) off L_+ - L_- is an INTERPRETATION, not a
derivation. Claiming it would be the exact move this work exists to avoid.
