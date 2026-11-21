---
# qou-fi93
title: 'Derived substrate matter/antimatter asymmetry: bar_defect r(z)-r(-z) = (10/27)z(4z^2+3), 7.88% at q0; connect to number density or state the gap'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T12:53:38Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-ddmn
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


### CORRECTION to the append immediately above, same day (PR #7313, commit 349cc8f8b1)

THE APPEND ABOVE OVERSTATED THE RESULT. It says the residual is
"DISCHARGED" and that "there is no choice". That holds only WITHIN A FIXED
COEFFICIENT RING, and this corpus carries TWO. Found by the corpus-grep that
should have preceded the write-up; verified independently rather than taken
on the report's word.

Write u = q^{1/2}. Then

    q - q^-1  =  (u - u^-1)(u + u^-1)  =  s * (bar-even)

so over Z[u, u^-1] the element q - q^-1 is a NON-UNIT multiple of the true
bar-odd generator s = q^{1/2} - q^{-1/2}. Measured: s/(q - q^-1) = 1/(u+u^-1)
is bar-even but is NOT a Laurent polynomial, so s is NOT in
(q - q^-1)*(bar-even) and q - q^-1 generates a PROPER SUBMODULE there. The
transition determinant in the u ring:

    N                      1   2   3   4   5   6   7   8   9  10
    det with s             1   1   1   1   1   1   1   1   1   1
    det with (q - q^-1)    0  -1   0   1   0  -1   0   1   0  -1

ZERO at every odd window -- not injective, let alone free.

NOT HYPOTHETICAL. bar-involution.lean:40, the canonical def:bar-involution
sibling, names Z[q^{+-1/2}, (q-q^-1)^-1] as the TYPICAL coefficient ring, and
docs/audits/2026-09-05-two-skein-normalisations-are-live.md records that both
normalisations are live, with s bar-odd in QOU/Braiding/SkeinNormalisation.lean.

WHAT SURVIVES, and it is the better theorem: the rank-one STRUCTURE is
ring-independent, the GENERATOR is not.

    For a Laurent ring R[x, x^-1] with bar x -> x^-1, the bar-odd part is
    free of rank one over the bar-even part, generated by x - x^-1, where x
    is THE RING'S OWN VARIABLE.

In Z[q,q^-1] that is q - q^-1; in Z[q^{+-1/2}] it is s. Each is correct in
its own ring and wrong in the other.

SO THE RESIDUAL DOES NOT VANISH -- IT RELOCATES, from "which bar-odd
object?" (answered: only one, up to a bar-even factor) to "which coefficient
ring?" (OPEN, and the corpus carries two). That second question is real and
is NOT answered by PR #7313.

The Lean is unaffected and still correct: it quantifies over FUNCTIONS
K -> K over a field, where f/(q - q^-1) always exists and no integrality is
asserted. What was wrong was the FRAMING, not the theorem. The distinction
now stated in its header is the useful one -- the function-level statement is
ring-independent and weak; the INTEGRAL statement carries the content and is
ring-dependent.

PRIOR ART, now cited in both artifacts. The closest is close enough that
omitting it would have read as a re-derivation:

  * docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md
    sec "the bar-odd channel is Skein-generated" + its probe
    computations/hh1_bar_odd_channel_is_skein_generated.py ALREADY CLAIM
    generation by q - q^-1, from the R-matrix decomposition -- scoped (a) by
    their own witness, checked at three root-of-unity points. PR #7313 adds
    the MODULE STRUCTURE (free / rank one / unimodular over Z) and the
    ring-dependence, NOT the generation claim.
  * computations/qbeta/qbeta_bar_fixed_field_is_q_of_two_probe.py proves the
    FIELD analogue by Galois: Fix(bar) = Q(q + q^-1) exactly. The integral
    version is strictly stronger and that probe names it as its own open NEXT.
  * NAMING: the generator is barOddGen
    (QOU/MassTheory/EmGermMomentVanishing.lean), h_A in the notation
    register -- NOT h, which is hbar_q = (q-1)/q, 0.0991 vs 0.2091 at q0
    (ruling qou-u87j).
  * WHICH BAR: three corpus gradings are called bar-parity
    (computations/bar_parity_involution_atlas_probe.py). All of this is the
    COEFFICIENT half q -> q^-1.

ONE MORE OPEN ITEM ADDED TO THIS BEAN by the above: WHICH COEFFICIENT RING
the framework's bar-parity arguments should be read in. The corpus is not
settled (docs/audits/2026-08-26-base-ring-options-and-axiom-4.md:104 says
"No Z[q^{+-1/2}] is required", against bar-involution.lean:40 calling it
typical), and bar parity CANNOT DETECT the difference -- the cofactor
between the two normalisations is bar-EVEN, which is exactly why the split
survived undetected (that audit's own sec "Why the split survived
undetected").


### 2026-09-13 (later still) — the SECOND ROUTE to this bean's exclusion is CONDITIONAL; the PRIMARY route is not

See qou-ndt5's correction of the same date (PR #7313, commit aa6e877569).

The append above cites qou-ndt5's consequence 3 as "a second, independent
route to qou-fi93's exclusion" -- the colour curve being exactly
bar-invariant, hence having no bar-odd part for a matter/antimatter asymmetry
to couple to. That holds only under ONE of the two lifts of the bar to
sqrt(q) that the corpus uses, and the corpus has never ruled between them:

    SkeinNormalisation.lean:74 / sJ_bar_antiinvariant    u ->  u^-1   z bar-ODD
    ColourCurveBarVsBranch.lean:49 / barLift             u -> -u^-1   z bar-EVEN

Same object (sJ and zOf are byte-identical definitions), opposite parity,
both lifts squaring to q^-1 and differing by exactly the branch swap. Under
the skein lift the colour curve DOES have bar-odd content and the second
route does not exist.

THIS BEAN'S PRIMARY ROUTE IS UNAFFECTED. The survey establishing that every
counting measure the framework defines is exactly bar-even -- [n]_q,
d_q(lambda), d_q^2/D^2, sum y_lambda -- never passes through the square root,
so the scope-(b) exclusion stands on it alone, as it did before the second
route was offered.

Noting it here because the second route was recorded in THIS bean's arc as
strengthening the exclusion, and a reader taking both routes as independent
would over-count the evidence by one.
---

COORDINATION NOTE (2026-09-13, from bean `qou-5c64` / PR #7268). Not a claim on
this bean, nothing here edited — a cross-arc arrival at your two carriers from a
different object, offered with its own limit stated.

**Your split and mine land on the same two objects.** `c8557da12ea` decomposes
the crossing energy onto

    E(q) + E(1/q) = w   (q + q^-1)     WRITHE, bar-even
    E(q) - E(1/q) = n_c (q - q^-1)     CROSSING NUMBER, bar-odd

Working the inter-nucleon bond factors of `qbeta_bond_factors_derived_probe`,
I get `b_pp = z = q^3/(q^2+1)` and `b_nn = zbar = z|_{q->1/q}` — a bar-conjugate
pair — and the pair's two natural invariants are **exactly** your carriers
(`sympy.simplify` -> 0, both):

    b_pp - b_nn        =  q - q^-1        your crossing-number carrier, coefficient 1
    sqrt(b_pp . b_nn)  =  1/(q + q^-1)    your writhe carrier, inverted

**Your "[n]_q is bar-even BECAUSE it is a ratio of two bar-ODD objects" is what
explains why `z` is not.** `z = q^3/(q^2+1)` is not such a ratio, so the
`(q - q^-1)` does not cancel — it survives as the whole bar-odd part, and
`z - zbar` is bare `h`. That is the same mechanism you describe ("the crossing
energy keeps it undivided"), one object over.

🛑 **The limit, and it is the reason this is a note and not a claim.**
Co-occurrence of `q +- q^-1` is **weak evidence on its own**: those two span the
bar eigenspaces of any Laurent object in q, so *every* bar-conjugate pair has
its difference in the odd space. The content here is not the appearance, it is:

1. the difference is **bare** `q - q^-1`, coefficient exactly 1 — not
   `3(q - q^-1)`, not `q^3 - q^-3`;
2. the **geometric** mean is exactly the bar-fixed `1/(q + q^-1)`. The
   ARITHMETIC mean is not — `b_pp + b_nn = (q^4+1)/(q^3+q)`, whose ratio to
   `q + q^-1` is `(q^4+1)/(q^2+1)^2`, not constant. The natural expectation is
   false, which is what makes the geometric one worth reporting.

Whether these are the SAME writhe/crossing decomposition or two constructions
sharing the ubiquitous `h` is **not established**, and I have not tested it. The
discriminator I would look for: does `b_pp - b_nn = q - q^-1` count something —
is there an (n_+ + n_-) reading of the p-p-vs-n-n interface with n_c = 1?

Probe `computations/qbeta/qbeta_bond_bar_parity_probe.py` (five identities, each
exactly zero); witness `computations/qbeta/qbeta-bond-bar-parity.witness.json`.
Your own scoping — "EXHIBITED, not selected" — applies verbatim to this note.


---

## 2026-09-13 — the planned search is closed, negatively, and the gap is a SUPPRESSION

`isBarOdd_iff` (`QOU.Observations.BarParityRankOne`, sorry-free) says the
bar-odd part of $\mathbb{Z}[q,q^{-1}]$ is **free of rank one** over the
bar-even part, generated by $q-q^{-1}$. So every bar-odd observable is
$(q-q^{-1})\times(\text{bar-even})$: **there is no second bar-odd shape to
look for.** That closes the search this bean was going to run.

The corpus already applies it. `QOU.Mass.BrunnianBindingChannel` proves the
count channel $n_c(q-q^{-1})/2$ bar-odd, the signed channel
$w(q+q^{-1})/2$ bar-even, and the mass-vs-binding assignment **forced by
parity** — so `qou-brng`'s open amplitude question and this bean's open
coupling question are about **the same channel**.

**So the missing object is not another asymmetry.** Every asymmetry the corpus
derives is $O(10^{-1})$:

| | value | vs $\eta_{obs}=6.1\times10^{-10}$ |
|---|---|---|
| $\delta_{CP}=\tanh(\ln q_0)$ | 0.103963710052410145676652858536 | 1.7043231e+8 (8.232 dex) |
| $\delta_z$ (colour curve) | 0.0787846669403909985963202377522 | 1.2915519e+8 (8.111 dex) |

In the standard picture $\eta \sim \varepsilon\cdot f$ with $\varepsilon$ the
CP asymmetry per decay and $f$ an entropy/washout suppression. The corpus
supplies $\varepsilon$-shaped objects and supplies **no $f$ at all**; the
required $f = \eta/\delta_{CP} = 5.867432\times10^{-9}$. An amplitude ratio and
a ratio of counts are different kinds of quantity, and the rank-one theorem
says no amount of searching the bar-odd sector produces the second kind.

**New, small:** the two asymmetries agree at leading order up to $4/3$
(measured 1.3195931910338566012, 1.03% off), because
$\delta_z = (r'(0)/r(0))z + O(z^3) = \tfrac34 z$ with $z=2\sinh(L/2)$ while
$\delta_{CP} = \tanh L$, and $z = L + O(L^3)$.

**Caveat, load-bearing:** rank-one is over $\mathbb{Z}[q,q^{-1}]$. Over
$\mathbb{Z}[q^{\pm1/2}]$ the generator is $u-u^{-1}$ and
$q-q^{-1}=(u-u^{-1})(u+u^{-1})$ is a proper multiple — see
`bar_parity_rank_one_probe.py` section 6 and `qou-ndt5`.

Probe: `computations/barparity/cp_theta_defect_and_two_asymmetries_probe.py`.
Scope (a). Bean stays open: no $f$ is derived here, and none is excluded.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8467, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-14: "beans(qou-hjs8, qou-fi93): the theta claim is live in two blocks, and fi93's search is closed negatively"). The work may be partly or fully done. Read the bean before you close it.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-read, no change on main. The bar-even exclusion is scope (b) for counting objects built from q-integers only, with the invariant cited; no density coupling derived or excluded. The η_obs comparisons in this bean are empirical context and must not enter a formal statement. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

No superseded premise: L₊ − L₋ = (q − q⁻¹)L₀ in this bean is the skein relation on crossings, not the photon's L±; z = q³/(q²+1) is z_D (convention D). The η_obs comparisons stay out of any formal statement.
