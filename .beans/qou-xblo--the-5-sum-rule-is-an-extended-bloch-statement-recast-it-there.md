---
# qou-xblo
title: 'The 5₂ sum rule is an EXTENDED Bloch statement — Σ R̂(y_σ; ε_σ, 0) = −π²/6, flattening supplied by the cubic'
status: in-progress
type: task
created_at: 2026-08-09T10:30:00Z
updated_at: 2026-08-09T10:30:00Z
---

Claimed by the session on `claude/fivetwo-level7-ladder-numerators` (restarted
from `main` after #4701 merged). Split out of `qou-0yqu`, which stays the parent
gap; this bean is the **route**, not the gap.

## The reformulation, measured

With `L(z) = Li₂(z) + ½·log z·log(1−z)` the Rogers dilogarithm and

    R̂(z; p, q) = L(z) − (πi/2)·( p·log(1−z) + q·log z )

Neumann's **flattened** Rogers dilogarithm, the 5₂ saddle roots satisfy

    Σ_σ R̂(y_σ ; ε_σ , 0) = −π²/6            residual 0.0 at 60 dps

where `ε = (+1, −1, 0)` is **not fitted** — it is the cubic's own branch data,

    ε_j = ( 2·log y_j − 3·log(1−y_j) ) / (2πi)

measured as exactly `(1, −1, 0)`. That those are integers is already a
sorry-free Lean theorem on `main`: `branch_data_of_cubic` in
`QOU/QBeta/FiveTwoSaddleSumRule.lean`, proved from the cubic alone with no
dilogarithm involved.

> ⚠ **NARROWED by Route 44 — see the section at the end.** This bean originally
> read "**the flattening the extended Bloch group needs is already a theorem in
> the corpus**". That is too strong. The `y`-level identity above is exact and
> unchanged, but the identification of the branch data *with* the flattening
> does **not** generalise up the tower, and flattenings turn out to be a torsor
> modulo the branch relation, so no single tuple is "the" flattening at all.

Equivalent to the sum rule, not weaker: `Σ V_j` and `3·Σ R̂` differ by an
elementary term computable from the cubic, verified to 50 dps.

## Why this is the right home — the ordinary Bloch group provably is not

Route 42 measured the obstruction. `D(y₁)` carries the entire 5₂ volume
(`Vol(5₂) = 3·D(y₁) = 6·D(c₁)`), but `Σ_σ D(σ y) = 0` **identically** — `y₂ = ȳ₁`,
`D(z̄) = −D(z)`, real root gives `0`. `D` is exactly the ordinary Bloch group's
regulator, so that machinery evaluates to zero on a Galois-summed dilogarithm
and can carry no information about `A`. Routes 1–5, 40 and 41 could not have
closed.

The extended Bloch group keeps what `D` discards: its regulator is the complex
volume `Vol + i·CS`, and `R̂` is well defined on it modulo `π²/6`.

## The quantisation signature

    −3π²/2  =  −9 · (π²/6)          the sum rule, in V-normalisation
    Σ_σ R̂   =  −1 · (π²/6)          the same statement, flattened

while the individual `Re(V_j)/(π²/6)` are `−2.1615…`, `−2.1615…`, `−4.6769…` —
irrational separately, integral only in the sum. That is the signature of a
Chern–Simons-type invariant, whose indeterminacy is exactly `π²/6`, and it is
the strongest evidence so far that the avenue is right.

## What is open — this is a reformulation, NOT a proof

The target is now: **show `Σ_σ [y_σ; ε_σ, 0]` is torsion in `ℬ̂(ℂ)`.** By
Neumann's theory that forces `Σ R̂` into `(π²/6)·ℤ`, and the sum rule is the
statement that the integer is `−1`.

⚠ Honest limits on what is measured:

* Neumann's **parity / geometric conditions** on a flattening are NOT imposed
  here. `ε` was found to work by search over `p, q ∈ {−2..2}` and then
  recognised as the branch data; a second assignment `(p,q) = (−2,2)` also
  gives an integer (`11`). So the measured claim is "the cubic's branch data,
  used as a flattening, makes the Galois sum an exact integer multiple of
  `π²/6`" — not "the geometric flattening does".
* Nothing here derives the integer `−1`. Getting it is the proof.
* No Lean. `R̂` and `ℬ̂(ℂ)` are not formalised in the corpus.

## Next

1. Impose Neumann's flattening conditions and check `ε` satisfies them — that
   turns the search hit into the geometric object.
2. Finish `qou-0yqu` Route 41's gated `G4` branch bookkeeping (pentagon over the
   three embeddings missed `3π²/2` by 6.4718; the real embedding is exact, the
   two complex ones deviate by `−3.2359 ± 1.3251i`, which is **not** a multiple
   of `π²/6` under principal branches — as expected, since the quantisation is a
   statement about the flattened form).
3. The five-term relation lifted to `ℬ̂(ℂ)`, then redo Route 41's rank
   computation there. The ordinary-Bloch rank result (46→47, 153→154) says
   nothing about the extended one.
4. Coordinate with **#4824** (`claude/extended-bloch-tetrahedron-wx3mc4`),
   already in extended-Bloch territory. Do not duplicate.

**Do not retry:** distribution (rank 4→5) or the ordinary five-term/Bloch ladder
over the `c^m` orbits. Anything reducing to an ordinary Bloch-group computation
is blind here, for the reason above.

Probe: `computations/probes/qbeta_5two_route43_flattened_rogers_probe.py`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 44 — the flattening is a TORSOR, and Route 43's identification is narrowed

Probe `computations/probes/qbeta_5two_route44_flattening_torsor_probe.py`
(5 gates, all pass, dps 45).

### What stands

`Σ_σ R̂(y_σ; ε_σ, 0) = −π²/6` at the `y` level — exact, unchanged (G2).

### What is narrowed — my own claim, by a test I ran to confirm it

The tower carries a branch relation at **every** level, and all three are
integral (G1):

| level | relation | branch data |
|---|---|---|
| `y` | `2·log y − 3·log(1−y) = 2πi·ε` | `(+1, −1, 0)` |
| `w` | `2·log(1−w) − 3·log w = 2πi·η` | `(−1, +1, 0)` |
| `c` | `log(1−c) − 5·log c = 2πi·δ` | `(−2, +2, 0)` |

So the raw material exists everywhere — which is what makes the failure real
rather than a missing input. **Branch data in the `p` slot gives an integer
multiple of `π²/6` only at `y`** (G3). At `w` the integer-valued flattening
sits in the `q` slot instead; at `c` the single hit over `p,q ∈ [−3,3]` is
`(1,−1)`, neither `+δ` nor `−δ`. The *placement* is not determined by the
branch relation and does not transfer.

### The structure that explains it

The branch relation is a **null direction** of the flattening correction (G4):
`3·log(1−y₃) − 2·log y₃ = 0` at the real root to 46 dps, so shifting `(p₃,q₃)`
by `(3,−2)` changes the total by nothing. Flattenings form a **torsor** modulo
the branch relation — which is why `(p₃,q₃) ∈ {(−3,2), (0,0), (3,−2)}` all give
the identical sum, and why *"is ε the flattening"* was the wrong question. Only
its **class** can be.

Integer flattenings are rare but not unique (G5): 6 hits at `y`, 6 at `w`, 1 at
`c`. Reported because Route 43 found `ε` by exactly this kind of search and only
then recognised it.

### Consequence for the plan

Step 1 of this bean — "impose Neumann's parity/geometric conditions and check ε
satisfies them" — is no longer a formality to tick off. It is **the blocking
step**: without those conditions there is no distinguished flattening to check,
only a torsor with several integer-valued representatives, and the `y`-level
integer `−1` cannot be derived. Everything downstream (the lifted five-term
relation, the rank computation in `ℬ̂(ℂ)`) waits on it.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 46 — the bookkeeping is COMPLETE, and the y-orbit needed nothing

Probe `computations/probes/qbeta_5two_route46_bookkeeping_complete_probe.py`
(5 gates, all pass, dps 60). Lean §7f in `FiveTwoSaddleSumRule.lean`.

The Rogers pentagon summed over the three embeddings at `x = y = z`:

| orbit | result |
|---|---|
| `y` (5₂ saddle cubic) | **`= 3π²/2` exactly, principal branches, NO flattening** — residual 2.5e-60 |
| `c` (`X³+X²−1`) | misses by 6.4718; needs the one crossing Route 45 derived |

So the configuration this lane cares about needs **no branch bookkeeping at
all**, and the 6.4718 discrepancy Route 41 reported belongs to the `c`
configuration, not the `y` one.

### ⚠ This corrects Route 45's own stated reason

Route 45's G5 said the derived flattening "does not transfer to the y-orbit,
which needs its own derivation" — implying `y` needs a *different* correction.
It needs **none**: the c-recipe **over-corrects**, moving an exact total off by
4.873. G5's numeric claim stands; the explanation attached to it did not.

### The method, validated

Correction read off winding numbers along the continuation path —
`πi·Σᵢ(w1ᵢ·log aᵢ + w0ᵢ·log(1−aᵢ))` — reproduces Route 45's hand-derived
c-orbit answer to 2.4e-35. On the y-orbit **every winding is zero**, which is
*why* no correction arises: derived, not observed after the fact.

### Consequence for Route 41

Route 41's rank no-go carried a gated limit: its rows were Bloch-group
statements, and converting one to a `Σ Li₂` statement needed bookkeeping that
was not done. **For the y-orbit that is now done and is trivial** — the pentagon
row is an exact `Σ L` identity there. The rank conclusion is firmer, and still a
no-go.

### Lean §7f — the collapse, sorry-free

On the diagonal `(1−z)/(1−z²) = 1/(1+z)`, so two pairs of arguments coincide and
the five-term relation is really three-term:

    pentagon_diagonal : 2·L(z) + 2·L(1/(1+z)) + L(1−z²) = π²/2

with `L` abstract carrying the pentagon hypothesis, plus `sum_pentagon_diagonal`
over the three roots. Standard axioms, zero `sorry`, `lake build` exit 0 with the
`.olean` deleted first. Numerically cross-checked in the collapsed form: residual
0.0 at 40 dps.

That is algebra only — **the analytic input (a complex Li₂ with the pentagon
identity) is still owed**, and no instance exists.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 47 — the sum rule's cleanest form: no log² term at all

Probe `computations/probes/qbeta_5two_route47_rogers_closed_form_probe.py`
(5 gates, all pass, dps 60).

    Σ_σ L(y_σ) = π²/2 − (2π/3)·arg(y₁)          residual 9e-61

equivalently `11π²/6 − 2πΘ`, the two linked by `3Θ = 2π + arg(y₁)` (gated).

Every earlier form carried a `log²` term:

| form | statement |
|---|---|
| V | `Σ Re(V_j) = −3π²/2`, `V_j = 3Li₂ + (log y + b·πi)²` |
| A | `A = −(9/2)L² + 6(Θ−π)² − π²/6` |
| flattened | `Σ R̂(y; ε, 0) = −π²/6` |
| **this one** | **`π²/2 − (2π/3)·arg(y₁)` — π² and π×angle only** |

That is the shape a Chern–Simons / flattening statement takes, so it is formal
support for the extended-Bloch framing of Routes 42–46 rather than another
reformulation for its own sake. Equivalent to the sum rule, not a weakening
(G2): `L = Li₂ + ½log·log` and the log-product Galois sum is elementary.

### What did not come with it

It fell out of Route 46's raw-closing diagonal pentagon
`2P + 2Q + R = 3π²/2` with `P = Σ L(y)`, `Q = Σ L(1/(1+y))`, `R = Σ L(1−y²)`.
`P` is elementary; **`Q` and `R` are not** — PSLQ finds nothing for either at
maxcoeff 1e7, nor widened with `log 7` (G3). So the relation says only that
`2Q + R` is elementary: one equation, two unknowns, closes nothing. Absence of a
PSLQ hit is evidence, not proof, and is gated as such.

⚠ **The diagonal leaves the unit tower.** `N(1+y) = 7`, so `1/(1+y)` is not an
algebraic integer — minimal polynomial `7x³−10x²+5x−1`, not monic (G4). The
prime 7 enters here. Flagged because this lane is named for a level-7 ladder,
but **no connection to that ladder is measured** and none should be assumed.

### The symmetry question, answered

The five-to-three collapse is a **ℤ/2, not an S₃** (G5): the `x↔y` swap induces
`(0 1)(2 4)(3)` — cycle type `[1,2,2]`, a reflection — whose orbits on the
diagonal are the multiplicities `[2,2,1]`. The S₃ in this subject is the
anharmonic group `⟨z↦1−z, z↦1/z⟩` on a **single** argument: a different action.
Geometrically the five-term relation is the 2–3 Pachner move (`5 = 2+3`) and the
reflection is a bipyramid symmetry; the tetrahedron-shape reading of
`Vol(5₂) = 3·D(y₁)` is **inference, not measured against a triangulation**.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 48 — the closed form is NOT general; two new exact values; a fourth alphabet

Probe `computations/probes/qbeta_5two_route48_not_general_probe.py` (4 gates,
all pass, dps 50). PR **#4865**.

### The negative that matters most

Route 47's `Σ L(y_σ) = π²/2 − (2π/3)·arg(y₁)` has the shape of a Chern–Simons
statement, which raises the obvious worry that it is a **general identity being
rediscovered** — in which case the sum rule reduces to a citation.

**It is not general.** It holds for the 5₂ saddle orbit and fails for every
other orbit tried — `w`, `c`, `−c`, `ρ`, `c⁵`, and two other cubic fields —
including `X³−X²+1`, which lies in the **same field** (G1). So no known theorem
is being rediscovered, and the form is special to `y`.

### Two exact values that fell out of falsifying it (G2)

    Σ_σ L over X³−X²+1   =  π²/6      exactly, residual 8e-51
    P(c⁵)  =  2·P(w)                  exactly, residual 0.0

with `P(·)` the Rogers-L Galois sum. Neither predicted, neither explained.
Gated rather than left in scrollback.

### A fourth alphabet, the same gap (G3)

Route 47 showed Route 41's alphabet was closed over **units**, so it never
contained `1/(1+y)` (norm 7, not an algebraic integer) and missed the diagonal
pentagon. Admitting non-units and closing under `1−z`, `1/z`, `1/(1+z)`, `1−z²`:
**57 orbits, 52 relations, rank 43 → 44.** Still not determined.

| alphabet | rank → with target |
|---|---|
| pure power tower `c^m` | not determined |
| 82 orbits, closed under `1−x`, `1/x` | 46 → 47 |
| 168 orbits, same closure | 153 → 154 |
| **57 orbits, non-units admitted** | **43 → 44** |

The gap has been **exactly 1 across four independent alphabets**. That
consistency is itself the finding: the missing input is not a relation of this
kind that was overlooked.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 49 — Neumann's actual definitions OVERTURN this bean's own target

Probe `computations/probes/qbeta_5two_route49_neumann_kernel_probe.py`
(6 gates, all pass, dps 45). Source: **`library/0307092v2/0307092v2.pdf`** — W D Neumann,
*Extended Bloch group and the Cheeger–Chern–Simons class*, Geom. Topol. 8 (2004)
413–474.

### What the paper actually says

1. `R(z;p,q) = R(z) + (πi/2)(p·log(1−z) + q·log z) − π²/6`, valued in **ℂ/π²ℤ**
   (Prop 2.5). Routes 43–47 used a **minus** sign and omitted the `−π²/6`.
2. **`ℬ̂(ℂ) = ker ν`**, `ν([z;p,q]) = (log z + pπi) ∧ (−log(1−z) + qπi)`
   (Def 2.4, Lemma 2.3). *That* is the membership condition — concrete and
   computable. It is exactly what Route 44 was missing when it could only say
   flattenings form a torsor.
3. `R ∘ λ = i(vol + i·cs)` — the Cheeger–Chern–Simons class.

### ⚠ This bean's stated target was wrong, twice over

The bean said: *show `Σ_σ [y_σ; ε_σ, 0]` is torsion in `ℬ̂(ℂ)`.* Both halves fail.

**(a) `(ε,0)` is not in `ker ν`** (G2). `ν = 0` requires
`X = Σ(q·log y + p·log(1−y)) ∈ ℚ·πi`; for `(±ε,0)` the ratio `Im(X)/π =
∓0.8961794846…`, no rational at maxcoeff 1e4. The element is not in the group.

**(b) The admissible flattenings give a non-torsion value.** The condition forces
`3q + 2p = 0` at **every** root — `(p,q) ∈ ℤ·(3,−2)` — derived from the branch
relation and confirmed by search (G3). **That is precisely the null direction
Route 44 found empirically**, now *derived*. For those, the correction is
`π²·k·ε ≡ 0 (mod π²)`, so `R` is flattening-independent (G4):

    R(ξ) = −(2π/3)·arg(y₁)        exactly, mod π²

and `arg(y₁)/π = 0.32786538652883426446…` is irrational to PSLQ at maxcoeff 1e8,
so **`R(ξ) is not torsion`** (G5).

### The target, corrected

`R(ξ)` is **real**, so by `R ∘ λ = i(vol + i·cs)` the volume part vanishes —
consistent with Route 42's `Σ_σ D = 0` — and the sum rule is the Chern–Simons
**evaluation**

    cs(ξ) = (2π/3)·arg(y₁)        (mod π²)

not a torsion statement (G6). Sharper and better founded than the old target,
and in the paper's own normalisation rather than my reconstruction.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Routes 49b–50 — the open statement is NOT open, and the pentagon is under way

### ⚠ Correction: `arg(y₁)/π ∉ ℚ` is a theorem, not a conjecture

An earlier session note called it "genuine open number theory". **Wrong.** It is
elementary via **Kronecker**: `arg(y₁)/π ∈ ℚ` iff `y₁/ȳ₁` is a root of unity,
and `y₁/ȳ₁ = y₁²y₃` is an algebraic integer of modulus 1 with minimal
polynomial `x⁶−3x⁵+11x⁴+5x³+11x²−3x+1`, whose conjugates have moduli
`0.2821`, `1`, `3.5445`. Not all on the unit circle ⟹ not a root of unity ⟹
irrational. Nothing external, nothing named, nothing to look up.

**Downstream this matters.** `cs(ξ) = (2π/3)·arg(y₁)` is therefore *provably*
not a rational multiple of `π²`. So no torsion, rationality or finite-order
argument can prove the sum rule — which is why Route 43's target had to die and
why four alphabets all left a rank gap of exactly 1: those searches look for
**rational** relations and the answer is not rational.

### The pentagon, in Lean

Two halves, both landed:

* **algebraic** — `FiveTwoSaddleSumRule.lean` §7h,
  `pentagon_deriv_x_eq_zero`: the `x`-derivative of the Rogers pentagon sum is
  `0`, with the five logs as **free variables** so no branch choice is made.
  Verified symbolically first: collecting the numerator on `log x`, `log(1−x)`,
  `log y`, `log(1−y)`, `log(1−xy)` gives coefficient `0` for each, plus zero
  remainder.
* **analytic** — new module `QOU/MathlibExt/ComplexRogersDilog.lean`:
  `cRogersL z = cLiTwoExt z + ½·log z·log(1−z)` built on the corpus's own
  integral continuation, with

      hasDerivAt_cRogersL : L′(z) = −½·( log(1−z)/z + log z/(1−z) )

  under exactly the four hypotheses the pieces need (`z ∈ notCut`, `z ≠ 0`,
  `z` and `1−z ∈ slitPlane`). Wired into `QOU.lean` so it is not an orphan.

Both sorry-free, standard axioms, `lake build` exit 0.

### What is still owed for the five-term identity

1. Chain-rule assembly at the three composite pentagon arguments.
2. **The branch conditions** under which `log a₃ = log(1−x) − log(1−xy)` and its
   two companions hold. This is the delicate part, and it is not new: those
   expansions are exactly where flattening enters, so it is Routes 45–46's
   bookkeeping and Neumann's `ker ν` reappearing.
3. Connectedness + pinning the constant (the `Landen` pattern already in the
   corpus).

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 51 — the chain-rule assembly, and a non-vacuity check

New module `QOU/QBeta/FiveTwoComplexPentagon.lean` (imports both halves; wired
into `QOU.lean`). **Item 1 of "what is still owed" is done.**

### What landed

* `hasDerivAt_argThree/Four/Five` — the three chain-rule factors §7h *assumed*,
  `(y−1)/(1−xy)²`, `−y`, `(1−y)y/(1−xy)²`, are now proved from
  `HasDerivAt.div`. Nothing about the differentiation is on faith any more.
* `hasDerivAt_pentagonSum` — for `L = cRogersL`, the five-term sum

      L(x) + L(y) + L((1−x)/(1−xy)) + L(1−xy) + L((1−y)/(1−xy))

  has `x`-derivative `0`, given four `rogersDomain` memberships and the five
  branch conditions. §7h is invoked, not re-proved: the total is discharged by
  `linear_combination pentagon_deriv_x_eq_zero`.
* `rogersDomain = slitPlane ∩ notCut` in `ComplexRogersDilog.lean`, with
  `one_sub_mem_slitPlane_iff`. This is a genuine simplification, not packaging:
  `1 − z ∈ slitPlane` **is** `z ∈ notCut` (both say `z ∉ [1,∞)`), and
  `z ∈ slitPlane` already gives `z ≠ 0`. So `hasDerivAt_cRogersL`'s four
  hypotheses were two, and the domain is just the plane minus both real cuts.

### The check that matters — the hypotheses are satisfiable

Ten hypotheses that cannot hold together prove anything, and nothing in the
statement of `hasDerivAt_pentagonSum` rules that out. So:
`pentagon_branch_conditions_of_real` proves **all five branch conditions** on
`0 < x, y < 1`, and `hasDerivAt_pentagonSum_of_real` discharges every hypothesis
there. The theorem is not vacuous.

The mechanism is one lemma, `clog_of_eq_ofReal`: a complex expression that
equals a *positive real* has `Complex.log` the cast of `Real.log`, after which
every expansion is `Real.log_mul` / `Real.log_div` and no branch is chosen.

All sorry-free, standard axioms, per-module `lake build` exit 0 with the
`.olean` deleted first.

### ⚠ What this is not

It is not the five-term identity for `cRogersL`. The **real** five-term identity
on `(0,1)` was already proved sorry-free in the corpus
(`FiveTwoAbelFiveTerm.rogersL_fiveTerm`, bean `qou-abel`) — so the real square is
a region where the answer was already known. What the 5₂ lane needs is the
complex identity, because `|y₁| = 1.52 > 1` and `y₁, y₂` are not real.

### Still owed

2. Continuation of the **branch conditions** off the real square. Unchanged and
   still the delicate part: those expansions are where flattening enters, so it
   is Routes 45–46 and Neumann's `ker ν` again.
3. Connectedness + pinning the constant (the `Landen` pattern in the corpus).

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 52 — the branch conditions travel, and item 2 becomes a question about a region

Same module, `QOU/QBeta/FiveTwoComplexPentagon.lean`. **Item 2 changes shape:**
it is no longer bookkeeping, it is one geometric question.

### The observation

`log a₃ = log(1−x) − log(1−xy)` is not an identity, but the **defect**

    d₃(w) = log a₃(w) − log(1−w) + log(1−wy)

is holomorphic wherever the three logarithms are, and its derivative vanishes
*identically as a rational function*:

    a₃′/a₃ + 1/(1−w) − y/(1−wy)
      = [(y−1) + (1−wy) − y(1−w)] / ((1−w)(1−wy)) = 0.

All five defects go the same way (checked each: `d₃`, `d₃′`, `d₄′`, `d₅`, `d₅′`).
So a defect that vanishes at one point of an open **connected** region vanishes
on all of it — `eq_zero_of_hasDerivAt_zero`, over
`IsOpen.is_const_of_deriv_eq_zero`.

This avoids the discreteness argument (`exp(d) = 1` ⟹ `d ∈ 2πiℤ` ⟹ locally
constant) entirely: the derivative is *already* zero, so the same machinery the
pentagon itself uses does the transport.

### What landed

* `PentagonRegular y w` — the four `rogersDomain` memberships. Everything else
  (`w ≠ 0`, `1−w ≠ 0`, `y ≠ 0`, `1−y ≠ 0`, `1−wy ≠ 0`, slit-plane membership for
  each logarithm) is a **consequence**, proved in the namespace.
* `hasDerivAt_defectThree/Three'/Four'/Five/Five'` — all five derivatives vanish.
* `eq_zero_of_hasDerivAt_zero` — the propagation principle.
* `defects_eq_zero_of_real` — a real base point supplies all five base values.
* `pentagonSum_eq_of_region` / `..._of_real` — **on any open connected set of `x`
  on which the pentagon stays regular and which contains a real point of
  `(0,1)`, the complex five-term sum is constant.** No branch condition is
  assumed at the far point; they are transported.

Sorry-free, standard axioms, per-module `lake build` exit 0 with the `.olean`
deleted first, no linter warnings.

### ⚠ What is still owed — sharpened

1. ~~chain-rule assembly~~ (Route 51).
2. **A region.** Not "continue the branch conditions" any more, but: exhibit an
   open connected set of `x` that stays `PentagonRegular` and reaches `(0,1)`.
   For the 5₂ saddle values none is exhibited, and this is exactly where
   flattening / `ker ν` can obstruct — a regular region reaching the real square
   would *force* the naive expansions, so if the flattening is non-trivial no
   such region can exist. The obstruction and the missing region are the same
   fact seen twice.
3. **Pinning the constant as a number.** "Constant on the region" does not yet
   read `π²/2`, because `cRogersL` has not been identified with the corpus's real
   `rogersL` on `(0,1)`. That identification is a separate, tractable job
   (`cLiTwoExt` vs `LiTwo` on the unit interval).

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 53 — the constant is pinned; a complex five-term identity, modulo one region

Same module. **Item 3 is done**, and with it the three-item list from Route 51
collapses to one.

### The bridge that was missing

`cRogersL` and the corpus's real `rogersL` were never connected. They are the
same function on `(0,1)`:

* `cLiTwo (t:ℂ) = ↑(LiTwo t)` — the complex and real `Li₂` series are *literally
  the same series*, `∑' k, z^(k+1)/(k+1)²`, so `Complex.ofReal_tsum` plus a
  termwise `push_cast` does it;
* `cLiTwoExt (t:ℂ) = ↑(LiTwo t)` for `|t| < 1`, via `cLiTwoExt_eq_cLiTwo`;
* `cRogersL_ofReal` — both logarithms are real on `(0,1)`, so
  `cRogersL ↑t = ↑(rogersL t)`.

### The real pentagon is `π²/2`

`rogersL_pentagon`. Abel's relation (`FiveTwoAbelFiveTerm.rogersL_fiveTerm`,
already sorry-free, bean `qou-abel`) is over `x, y, xy, x(1−y)/(1−xy),
y(1−x)/(1−xy)`. Three reflections convert its last three into the pentagon's
`1−xy`, `(1−x)/(1−xy)`, `(1−y)/(1−xy)`, since

    1 − (1−x)/(1−xy) = x(1−y)/(1−xy)      1 − (1−y)/(1−xy) = y(1−x)/(1−xy)

at a cost of `3·π²/6 = π²/2`, and Abel's zero absorbs the rest.

### Result — a complex five-term identity

`pentagonSum_eq_pi_sq_div_two_of_region`: on any open connected set `S` of `x`
that stays `PentagonRegular` for a real `y ∈ (0,1)` and contains a real point of
`(0,1)`,

    L(x) + L(y) + L((1−x)/(1−xy)) + L(1−xy) + L((1−y)/(1−xy)) = π²/2

for `L = cRogersL`, at **every** point of `S` — including points where nothing is
real.

Also `pentagonSum_symm : pentagonSum y x = pentagonSum x y` (the five arguments
are permuted, not changed, by `x ↔ y` — this is §7g's `Z/2` again), so transport
in the *second* variable is the same theorem, not a new one. That matters:
reaching the 5₂ saddle needs both variables to move.

### The list is now one item

1. ~~chain-rule assembly~~ (Route 51).
2. ~~continuation of the branch conditions~~ — reduced to a region (Route 52).
3. ~~pinning the constant~~ (this route).

**Remaining: exhibit an open connected regular region reaching `(0,1)`.** And
this is not a technicality left for later — it is the obstruction itself. A
regular region reaching the real square *forces* the naive log expansions, so
where the flattening is non-trivial no such region exists. `ker ν` and the
missing region are one fact seen twice.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 54 — the region exists in ONE variable. A complex five-term identity, unconditional.

The "one remaining item" from Route 53 turned out to be answerable — for one
variable — by a two-line computation, and the answer locates the obstruction
exactly.

### The region is `rogersDomain` itself

Fix a **real** `a ∈ (0,1)` in the other slot and write `w = u + iv`. Then

    Im(1 − wa) = −av        Im[(1−w)·conj(1−wa)] = v(a−1)
                            Im[(1−a)·conj(1−wa)] = (1−a)av

so every one of the four `w`-dependent arguments has non-zero imaginary part as
soon as `v ≠ 0` — and a point with non-zero imaginary part is off **both** cuts
automatically. Where `v = 0`, `w` is real in `(0,1)` and `PentagonRegular.of_real`
applies. So the whole of `rogersDomain` is regular; it is open
(`isOpen_rogersDomain`) and connected (`isPreconnected_rogersDomain`: two
half-planes joined through the strip `0 < re < 1`), and it contains `(0,1)`.

### The theorem — no hypotheses left

`pentagonSum_eq_pi_sq_div_two`: for **every** real `a ∈ (0,1)` and **every** `w`
off both real cuts,

    L(a) + L(w) + L((1−a)/(1−aw)) + L(1−aw) + L((1−w)/(1−aw)) = π²/2

with `L = cRogersL`. No branch hypothesis. No region hypothesis. Sorry-free,
standard axioms, `lake build` exit 0 with the `.olean` deleted first.

### ⚠ Where it stops — and the address of the obstruction

**One** variable. Probe
`computations/probes/qbeta_5two_route54_complex_pentagon_probe.py` (5 gates,
40 dps):

* G1 — 30 pairs, `|w|` to 40, `w` straddling both cuts, `w` within 1e-8 of the
  real axis: exact.
* G3 — **the negative**. With both variables non-real it is FALSE, and the
  deviation is not even a *real* multiple of `π²` (at `(2+0.5i, 1.5−0.9i)`:
  `(−0.0780 + 0.2303i)·π²`). So it is a genuine `2πi·(log)` term, not a
  flattening integer, and no sharpening of the same argument reaches it.
* G4 — the address. The theorem **reaches** `(y₃, y₁)`, the saddle cubic's real
  root against a complex one, because `y₃ = 0.4301597… ∈ (0,1)`. It **does not
  reach** `(y₁, ȳ₁)` — the pair `Vol(5₂) = 3·D(y₁)` needs.

That is the whole story of this lane in one line: the five-term identity survives
exactly as far as one real argument, and the volume lives one step past it.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 55 — the saddle cubic IS the plastic cubic, and that is a NEGATIVE

Asked what Route 54's theorem actually *says* at the one 5₂ pair it reaches.
The answer retro-explains four routes and kills a hope.

### The identity

    ((y−1)/y)³ − (y−1)/y + 1  =  (y³ − 2y² + 3y − 1) / y³

**an identity of rational functions** — nothing reduced modulo the cubic (checked
at generic points where the cubic does not vanish, so it is not a modular
coincidence). So the anharmonic map `y ↦ 1 − 1/y` carries the 5₂ saddle cubic
*onto* `X³ − X + 1`, whose roots are the **negatives of the plastic numbers**.

The saddle orbit and the plastic orbit are ONE orbit of ⟨`z ↦ 1−z`, `z ↦ 1/z`⟩.

### ⚠ Why that is a negative

Routes 41, 47 and 48 closed their alphabets under exactly `1−z` and `1/z`. So
every relation Route 54's pentagon produces at `(y₃, y₁)` was **already inside
those alphabets** — the ones whose rank gap was exactly 1, four times over.
**Route 54's theorem adds no rank.** It should not be read as progress on the
sum rule, and this bean entry exists so it cannot be.

The degree-6 field does not rescue it either: `a₃, a₅` share the palindromic
`X⁶−3X⁵+5X⁴−5X³+5X²−3X+1`, but `a₅ = 1/a₃`, so `L(a₃) + L(a₅)` is elementary by
inversion and the degree-6 elements cancel, leaving only the degree-3 orbit.

### What it does buy

An explanation. The plastic tower (`c` = root of `X³+X²−1` = `1/ρ`, and `c²`,
`c³`, `1−c = c⁵`) ran through Routes 40–48 and was never explained. It is the
same orbit. Not a coincidence, not a discovery — a coordinate change.

### The exceptional structure at `(y₃, y₁)`, all exact

Verified by Gröbner reduction against `a+b+c=2`, `ab+ac+bc=3`, `abc=1`, then
measured to 60 dps:

* `a₅ = 1/a₃` ⟺ `(1−a)(1−b) = (1−ab)²` — and the identity **is** the cubic,
  satisfied by the third root;
* `1 − a₃ = conj(a₃)` (so `Re a₃ = 1/2` exactly);
* `|a₃|² = y₃`;
* `a₄ = 1 − y₃y₁ = 1 − 1/y₂` is a root of `X³ − X + 1`.

In Lean, sorry-free, standard axioms: `saddle_to_plastic`, `plastic_of_saddle`,
`saddle_of_plastic`, `pentagon_arg_reciprocal`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 56 — flattening removes the two-variable failure. Neumann's pentagon, in Lean.

Route 54 proved the identity with one real variable and measured it failing with
two. This route removes the failure by removing the assumption that caused it.

### The move

The identity needs `log a₃ = log(1−x) − log(1−xy)` and four companions, and those
DO fail. But nothing forces the use of `log a₃`. Carry the **expansion** as the
logarithm:

    flatRogers(z, Λ, Λ′) = Li₂(z) + ½·Λ·Λ′ + (log(1−z) − Λ′)·log z

Its derivative is `rogersDeriv(z, Λ, Λ′)·z′` **exactly** — the `log z` factor's
contribution cancels against the `Λ′` one. So §7h applies verbatim and the
flattened pentagon has vanishing derivative under `PentagonRegular` **alone**.
Five branch hypotheses → zero.

What makes it work is that each `Λ` differentiates correctly *as a rational
function*: `Λ₃′ = −1/(1−x) + y/(1−xy) = (y−1)/((1−x)(1−xy)) = a₃′/a₃`. No branch
is chosen anywhere. That identity and its four companions is what got traded for
the branch conditions.

### It is Neumann's `R(z;p,q)`

With `δ = log z − Λ`, `δ′ = log(1−z) − Λ′`:

    flatRogers = L(z) + ½δ′·log z − ½δ·log(1−z) + ½δδ′

and `δ = 2πi·p`, `δ′ = 2πi·q` makes this `R(z;p,q)` up to normalisation. So the
theorem is the pentagon in `ℬ̂(ℂ)` — what this bean said the lane needed, back at
Route 49.

### Measured (Route 56 probe, 5 gates, 40 dps)

* G1 — flattening repairs **every** two-variable failure, including the worst
  (`(−0.447 + 0.354i)·π²`). Max flattened deviation `2.8e-40`.
* G2 — the ten defects per point are **integers**, measured: max distance to the
  nearest integer `1.2e-41`, all in `{0, ±1}`.
* G3 — inert where the branch conditions already hold, so it extends Route 54
  rather than replacing it.
* G4 — the control: the unflattened sum still fails at those points, so G1 is not
  a tautology.
* G5 — **the flattened identity holds at `(y₁, ȳ₁)`** to `3.7e-40`. That is the
  pair `Vol(5₂) = 3·D(y₁)` needs.

### ⚠ What is still owed — now exactly one geometric fact

Lean gets constancy on a connected regular region and `π²/2` on a region reaching
the real square. **No region joining the real square to `(y₁, ȳ₁)` is
exhibited.** G5 is evidence the identity holds there, not a proof that a path
exists. But the question is now purely about regularity — all four arguments off
both cuts along a path — with no branch bookkeeping in it at all.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 57 — Route 56's region does not exist: the pair is ON the cut

Route 56 left exactly one item: a connected regular region joining the real
square to `(y₁, ȳ₁)`. **It does not exist**, and the reason is one line.

### The negative

From `y₁y₂y₃ = 1`:

    y₃·(1 − y₁y₂) = y₃ − 1        so    1 − y₁ȳ₁ = (y₃−1)/y₃

and `y₃ = 0.4301597… ∈ (0,1)` makes that a **negative real** — `−1.3247179…`,
minus the plastic number. Route 55's map `y ↦ 1 − 1/y` for the third time. A
negative real is off `slitPlane`, so `log(1 − xy)` sits exactly on its branch cut
and `PentagonRegular` **fails** at the pair `Vol(5₂)` needs. Not "hard to reach":
on the boundary of the domain.

Lean, sorry-free: `one_sub_mul_of_prod_eq_one` (`linear_combination -hprod`, one
line) and `not_pentagonRegular_of_prod_eq_one`.

### Why that is better news than it sounds

On the boundary is not outside. Two measurements (Route 57 probe, 40 dps):

* **G2** — the straight segment from *any* real `a ∈ (0,1)` to `y₁`, with `ȳ₁`
  fixed, is regular at every interior point: 1500 samples each, five values of
  `a`, zero interior failures. Only `t = 1` fails, and only in the single
  argument `1 − wy`. (Sampled, not certified — the gate says so.)
* **G3** — the approach is from the **upper** half-plane:
  `Im(1 − w·ȳ₁) = a(1−t)·Im y₁ > 0`, decreasing to `0`. That is the side on which
  the principal `Complex.log` (`arg ∈ (−π, π]`) is continuous at a negative real.

So the residue is a **boundary-continuity argument at one point**, not a search
for a region. Smaller problem, different problem. **Not done here.**

### Also gated (G4), all equivalent to the cubic

`(1−a)(1−b) = (1−ab)²` for any two roots, so `a₅ = 1/a₃`; here additionally
`a₅ = ā₃`, hence **`|a₃| = 1`** — the two composite arguments sit on the unit
circle. Gröbner-verified before measurement.

### The ledger now

1. ~~chain-rule assembly~~ (51) · 2. ~~branch conditions travel~~ (52) ·
3. ~~constant pinned~~ (53) · 4. ~~region, one variable~~ (54) ·
5. ~~flattening removes the branch hypotheses~~ (56)

**Remaining: continuity of the flattened pentagon at a single boundary point,
approached from the upper half-plane.** Everything else in the chain is proved.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 58 — a COMPLETE PROOF PATH from an already-proved theorem. Four elementary links left.

**The 5₂ sum rule remains verified to 80 dps, unproved.** This route does not
prove it. It exhibits a chain from a Lean theorem that *is* proved to the sum
rule's stated target, and gates every link. Four links are open.

### The chain

Route 54's `pentagonSum_eq_pi_sq_div_two` (sorry-free) applies at **both**
`(y₃, y₁)` and `(y₃, y₂)` — the real root against each complex one, since
`y₃ = 0.4301597… ∈ (0,1)` and `y₁, y₂` are off both cuts. Adding the two
instances and using `a₅ = 1/a₃` (Route 55) gives

    Σ_y L + L(y₃) + inv_a + inv_b + L(a₄) + L(b₄) = π²

with `a₄ = 1 − y₃y₁ = 1 − 1/y₂`. Four elementary evaluations collapse it:

    inv_a = L(a₃) + L(1/a₃)  = (π² + πθ)/6 + iπ·log(y₃)/4        [G3, OPEN]
    L(a₄) − L(y₂)            = (3πθ − π²)/6 − iπ·log(y₃)/4       [G4, OPEN]
    ⟹  Σ_y L = π²/2 − (2π/3)·θ                                  [Route 47's form]
    Σ log y log(1−y) = log²y₃ − (4/3)θ² + (4π/3)θ                [G6, OPEN]
    ⟹  A = −π²/6 − ½log²y₃ + (2/3)(θ−π)²                        [the stated target]

Every residual ≈ 1e-60 at 60 dps. `A` matches the corpus's own target expression.

### ⚠ What this changes, and what it does not

Route 47's closed form was a **numerical observation with no derivation**. It is
now the consequence of a proved theorem plus two elementary links. And the sum
rule itself is now separated from a theorem by **branch bookkeeping**, not by
analysis. The analytic input this lane lacked — a complex `Li₂` carrying the
pentagon — is done.

It does **not** prove the sum rule. G3, G4, G6 and the angle identity are not
proved, here or in Lean.

### One quarter of one link, closed

`saddle_arg_cube` (Lean, sorry-free): for two roots `a`, `c` of the cubic,

    ((1−c)/(1−ca))³ · a = −c            i.e.   a₃³·y₁ = −y₃

so `3·arg a₃ + arg y₁ = π`, which is the angle identity G3 rests on. Not a
consequence of the pair relation alone — the cubic is needed too, and the
cofactors are what a Gröbner reduction against both returns.

### The open list, exactly

1. `inv_a` evaluation (inversion `L(z)+L(1/z)`, branch pinned).
2. `arg(a₃) = (π − arg y₁)/3` — algebraic core now proved, the argument/mod-2π
   step is not.
3. `L(1−1/z) − L(z)` evaluation (the anharmonic relation, branch pinned).
4. `Σ log y log(1−y)` evaluation (the saddle branch equation).

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 59 — Rogers inversion, proved. Link G3's analytic half is done.

`cRogersL_add_inv` (Lean, sorry-free), on `ℂ ∖ [0,∞)` with `arg z ≠ π`:

    L(z) + L(1/z) = −π²/6 − ½·log(−z)² + ½·log z·log(−z)

Built on the corpus's **existing** complex inversion
(`ComplexDilogarithmInversion.invCombo_eq`, `log_one_sub_inv_add_log_neg`) — no
new analysis, just the two Rogers half-`log·log` terms added and the
`log z·log(1−z)` pieces cancelled against each other. One `linear_combination`.

Verified at six points first — both half-planes, negative reals, near and far —
all off the 5₂ configuration, so nothing peculiar to that locus carries it.

### What this leaves of link G3

Route 58's G3 was `inv_a = (π² + πθ)/6 + iπ·log(y₃)/4`. It is now:

* the **analytic** content — the inversion formula — **proved**;
* the algebraic core of the angle identity — `a₃³·y₁ = −y₃`, `saddle_arg_cube` —
  **proved**;
* what remains is **branch pinning only**: from `a₃³y₁ = −y₃`,
  `3·log a₃ + log y₁ = log(−y₃) + 2πik`, and `k = 0` needs
  `3·arg a₃ + arg y₁ ∈ (−π, π]`. Numerically `3(0.70386) + 1.03002 = π` exactly.
  Plus `log(−a₃) = log a₃ − iπ`, which needs `arg a₃ ∈ (0, π)`.

So G3 is now a bounds problem on the arguments of two specific algebraic numbers,
not a dilogarithm problem. `QOU/Archimedean/BranchIntegerPinning.lean` pins a
branch integer along a *continuous family*; pinning one at a single algebraic
point by an argument window is a different technique and is not in the corpus.

### The open list, updated

1. G3 — **analytic half done**; branch pinning of `arg a₃` remains.
2. G4 — `L(1−1/z) − L(z)`, the anharmonic relation. Same shape: reflection plus
   inversion, then branch pinning. Both ingredients now exist.
3. G6 — `Σ log y log(1−y)`, from the saddle branch equation.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 60 — complex Rogers reflection, and the anharmonic relation. Both links' analytic halves done.

The corpus had `Li₂` **inversion** on `ℂ` but no complex **reflection**. Both are
now available for `cRogersL`, so the whole anharmonic group acts.

### Reflection — `cRogersL_add_one_sub`

    L(z) + L(1−z) = π²/6      for every z off both real cuts

Cheap, once the pieces from Routes 51–54 exist:

* `L′(z) − L′(1−z) = 0` **identically** as a rational expression — the Rogers
  half is exactly what makes reflection differentiate to nothing;
* `rogersDomain` is invariant under `z ↦ 1−z` (`one_sub_mem_rogersDomain_iff`):
  it is `ℂ` minus both real cuts and the involution swaps them;
* it is open (Route 51) and connected (Route 54), so constancy is immediate;
* the constant is pinned at the **real** point `1/2`, by `cRogersL_ofReal`
  (Route 53) and the corpus's real `rogersL_reflection`.

No branch hypothesis anywhere.

### The anharmonic relation — `cRogersL_one_sub_inv_sub`

Reflection at `1/z` minus inversion:

    L(1 − 1/z) − L(z) = π²/3 + ½·log(−z)² − ½·log z·log(−z)

`z ↦ 1 − 1/z` is the order-3 anharmonic element — the same map Route 55 showed
carries the saddle cubic onto `X³ − X + 1`. This is that map read on `L`.
Verified at six points first, including both `y₁` and `y₂`.

### Where Route 58's links stand now

| link | analytic content | what remains |
|---|---|---|
| G3 `inv_a` | `cRogersL_add_inv` **proved** | evaluate `log a₃`: needs `arg a₃ = (π−θ)/3`, whose algebraic core `a₃³y₁ = −y₃` is **proved** — branch pinning only |
| G4 anharmonic | `cRogersL_one_sub_inv_sub` **proved** | evaluate `log y₂ = −½log y₃ − iθ` — branch pinning only |
| G6 `Σ log·log` | — | the saddle branch equation |

So **every dilogarithm-level ingredient of links G3 and G4 is now proved**, and
what is left of them is uniformly the same thing: pinning the argument of a
specific algebraic number inside a `(−π, π]` window. That is a bounds problem,
not an analysis problem, and it is not in the corpus —
`Archimedean/BranchIntegerPinning.lean` pins a branch integer along a
*continuous family*, which is a different technique.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 61 — the branch pinning, and it is not tight

The obstacle after Route 60 was: from `a₃³·y₁ = −y₃`, conclude
`3·log a₃ + log y₁ = log y₃ + iπ` — i.e. pin `k = 0` in a `2πik`. That looked
like it needed sharp bounds on the arguments of specific algebraic numbers. **It
does not.**

    arg a₃ ∈ [0, π/2]   and   arg y₁ ∈ [0, π]
      ⟹  3·arg a₃ + arg y₁ ∈ [0, 5π/2] ⊂ (−π, 3π)

and `π` is the only value in `(−π, 3π)` congruent to `π` mod `2π`. `5π/2 < 3π`
with room to spare — the window is *loose*, and the bounds needed are crude sign
conditions, not numerics.

### Landed (Lean, sorry-free, standard axioms)

* `clog_eq_of_exp_eq` — `exp u = c` and `Im u ∈ (−π, π]` ⟹ `log c = u`. One line
  over `Complex.log_exp`.
* `im_eq_pi_of_exp_eq_neg_ofReal` — **the window lemma**: `exp u` a negative real
  forces `Im u ≡ π (mod 2π)`; a window `(−π, 3π)` pins it to `π`.
  `Archimedean/BranchIntegerPinning.lean` does this along a *continuous family*;
  this is the single-point version, which is what the saddle needs.
* `clog_cube_mul` — `a³b = −t`, `t > 0`, `arg a ∈ [0,π/2]`, `arg b ≥ 0` ⟹
  `3 log a + log b = log t + iπ`.
* `saddle_clog_cube` — the above composed with `saddle_arg_cube'` (Route 58).

### What remains of link G3

Exactly three **sign conditions** on the specific numbers, taken as hypotheses:

    0 ≤ arg a₃     arg a₃ ≤ π/2     0 ≤ arg y₁

which are `Im a₃ ≥ 0`, `Re a₃ ≥ 0`, `Im y₁ ≥ 0`. Route 55 proved
`a₃ + ā₃ = 1`, so `Re a₃ = 1/2`. These are facts about roots of a cubic, not
about dilogarithms.

### The ledger

| link | status |
|---|---|
| G3 inversion | `cRogersL_add_inv` **proved** (59) |
| G3 angle, algebra | `saddle_arg_cube` **proved** (58) |
| G3 angle, pinning | `saddle_clog_cube` **proved** modulo three sign conditions (61) |
| G4 anharmonic | `cRogersL_one_sub_inv_sub` **proved** (60) |
| G4 evaluate `log y₂` | open — same shape, `log y₂ = −½log y₃ − iθ` |
| G6 `Σ log·log` | open — the saddle branch equation |

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 62 — the infrastructure, built out. Link G3 has no `arg` hypothesis left.

Two general simplifications collapse both remaining evaluations, and the bounds
problem turns out to be one exact algebraic fact.

### The `log²` terms cancel completely

Eliminating `log(−z)` in favour of `log z`:

    L(z) + L(1/z)     =  π²/3 + (iπ/2)·log z        for Im z > 0
    L(1 − 1/z) − L(z) = −π²/6 + (iπ/2)·log z        for Im z < 0

**No quadratic term at all.** That is why Route 58's links G3 and G4 have values
with no `log²` in them — it was never a coincidence of the saddle. Both verified
at six points first, and both **fail** on the wrong side of the axis (residual
2.92), which is the control.

### The infra, in `MathlibExt` (the Mathlib-gap layer)

* `arg_ne_pi_of_im_ne_zero`, `clog_neg_of_im_pos`, `clog_neg_of_im_neg`
* `arg_nonneg_of_im_nonneg`, `arg_le_pi_div_two_of_re_nonneg`,
  `mem_invDomain_of_im_ne_zero`
* `clog_eq_of_exp_eq`, `im_eq_pi_of_exp_eq_neg_ofReal` (the window lemma),
  `clog_cube_mul` (Route 61)
* `cRogersL_add_inv` (59), `cRogersL_add_inv_of_im_pos`

and in the 5₂ layer: `cRogersL_add_one_sub` (complex reflection, 60),
`cRogersL_one_sub_inv_sub`, `cRogersL_one_sub_inv_sub_of_im_neg`,
`inv_mem_rogersDomain_of_im_ne_zero`.

### The bounds problem, solved

`saddle_pair_rel`, `one_sub_mul_third`, `saddle_argThree_add_eq_one`:

    (1−c)/(1−ca) + (1−c)/(1−cb) = 1

for the three roots — cofactors `c·R − a·C`, from a Gröbner reduction. With
`b = conj a` and `c` real this is **`Re a₃ = 1/2` exactly**, and that is the only
one of the three sign conditions with any content. `saddle_arg_bounds` discharges
all three.

### Link G3 now

`saddle_clog_cube_of_roots`:

    3·log a₃ + log y₁ = log y₃ + iπ

from **root data alone** — symmetric functions, the cubic, three non-vanishing
conditions, the conjugate-pair structure, and two `Im ≥ 0` facts. No `arg`
hypothesis survives. Nothing numeric enters anywhere.

### What is left

* **G3**: assemble — feed `saddle_clog_cube_of_roots` into
  `cRogersL_add_inv_of_im_pos`. Mechanical.
* **G4**: evaluate `log y₂ = −½log y₃ − iθ` — `|y₁|²y₃ = 1` and `arg(conj y₁) =
  −arg y₁`; both are one-liners over Mathlib now.
* **G6**: `Σ log y log(1−y)` from the saddle branch equation. Untouched, and the
  only remaining link with its own input.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 63 — the anharmonic toolkit is complete, and the orbit sum assembles

### Four one-log forms, both sides of the axis

    L(z) + L(1/z)     =  π²/3 + (iπ/2)·log z     Im z > 0
    L(z) + L(1/z)     =  π²/3 − (iπ/2)·log z     Im z < 0
    L(1−1/z) − L(z)   = −π²/6 − (iπ/2)·log z     Im z > 0
    L(1−1/z) − L(z)   = −π²/6 + (iπ/2)·log z     Im z < 0

The anharmonic group's action on `cRogersL` is now completely tabulated, and
every evaluation Route 58 needs is a substitution. All four sorry-free; each
verified at four to six points first and each **fails** on the wrong side of the
axis, which is the control.

### The assembly — `saddle_sum_cRogersL`

    2·(L(c) + L(a) + L(b)) = 2π²/3 − (iπ/2)·(log A₃ − log B₃ + log b − log a)

from the two pentagon instances and the four evaluations, by one
`linear_combination`. **No dilogarithm on the right.**

With `b = conj a`, `B₃ = conj A₃`, `c` real, the bracket is `2i(arg A₃ − arg a)`
and this reads

    Σ_y L = π²/3 + (π/2)·(arg A₃ − arg a)

Route 61's `saddle_clog_cube_of_roots` supplies `arg A₃ = (π − arg a)/3`, giving
`Σ_y L = π²/2 − (2π/3)·arg y₁` — Route 47's closed form. Checked numerically at
50 dps: assembly residual `2.1e-50`, and all three routes to `Σ_y L` agree to 30
digits.

### The ledger

| link | status |
|---|---|
| G3 inversion | **proved** (59, 62) |
| G3 angle | **proved from root data**, no `arg` hypothesis (58, 61, 62) |
| G4 anharmonic | **proved**, both signs (60, 63) |
| assembly to `Σ_y L` | **proved** (63) |
| conjugate-root inputs | `log(conj z) = conj(log z)` — Mathlib, one line |
| **G6** `Σ log y log(1−y)` | **open** — the saddle branch equation |

Everything between the proved pentagon and Route 47's closed form is now in
place. **G6 is the last link with its own input**, and it is the bridge from
`Σ L` to `A`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 64 — link G6, and the chain end to end

### The bridge, from the branch equation alone

`cRogersL` and `cLiTwoExt` differ by `½·log z·log(1−z)`, so `Σ L` and `A` differ
by `½·Σ log y·log(1−y)`. That sum looks like a period; the **saddle branch
equation** makes it elementary, because it turns each `log(1−y)` into a multiple
of `log y`:

    Σ lⱼ·mⱼ = (2/3)·Σ lⱼ² − (2πi/3)·Σ εⱼ·lⱼ        given 2lⱼ − 3mⱼ = 2πi·εⱼ

`sum_log_mul_log_one_sub` — stated for **any** three branch equations with the
`ε` free, so it is the branch equation doing the work, not the 5₂ cubic. Nothing
quadratic in `m` survives, which is why `A` inherits `Σ L`'s elementary shape.

### The capstone — `sum_cLiTwoExt_eval`

    2·Σ Li₂(yⱼ) = 2π²/3 − (iπ/2)·(log A₃ − log B₃ + log b − log a)
                  − (2/3)·Σ log²yⱼ + (2πi/3)·Σ εⱼ·log yⱼ

The left side is twice the sum rule's `A`. **The right side contains no
dilogarithm at all** — only `π²` and logarithms of the roots. Checked at 50 dps:
residual `2.7e-50` against `2A`, and the branch data comes out exactly
`ε = (+1, −1, 0)`, the value already recorded.

### ⚠ What is still input

* the two pentagon values — **theorems** (`pentagonSum_eq_pi_sq_div_two`);
* the three **branch equations** `2 log yⱼ − 3 log(1−yⱼ) = 2πi εⱼ` — hypotheses;
* to turn the right side into `−π²/6 − ½log²y₃ + (2/3)(θ−π)²`: `|y₁|²y₃ = 1`,
  `y₂ = conj y₁`, and `arg A₃ = (π − arg y₁)/3` (Route 61, proved from root data).

None of the second and third groups is discharged. **The 5₂ sum rule is not
proved.**

### What changed over Routes 51–64

The lane began with the complex five-term identity absent from Mathlib and from
this corpus. It now has: the identity (one real variable, unconditional), its
flattened form (Neumann's `ℬ̂(ℂ)` pentagon, no branch hypotheses), complex
reflection and inversion, the anharmonic group's action completely tabulated, a
single-point branch-window lemma, and a chain from the pentagon to `A` with no
dilogarithm on the right. What separates that from the sum rule is the branch
equations and three facts about the roots.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 65 — the branch equations, proved from the cubic

Route 64's capstone took the three branch equations as hypotheses. **They are not
extra input.**

### `y² = (1−y)³` IS the cubic

    (1−y)³ − y² = −(y³ − 2y² + 3y − 1)        identically

so `saddle_sq_eq_one_sub_cube` is one `linear_combination`. Hence
`exp(2·log y − 3·log(1−y)) = y²/(1−y)³ = 1`, and `2·log y − 3·log(1−y) ∈ 2πiℤ`
with **no branch assumption anywhere**.

### The window, again loose

`eq_intMul_two_pi_I_of_exp_eq_one`: `exp u = 1` and `Im u ∈ (2π(n−1), 2π(n+1))`
force `u = n·2πi`. Width `4π` and still only one multiple of `2π` inside — which
is what makes the saddle's crude bounds enough. `Re u = 0` comes free; it is not
a hypothesis.

### The three integers

* **`ε₃ = 0`** — `saddle_branch_eq_real`. **Fully proved**, no window needed:
  both `arg y₃` and `arg(1−y₃)` vanish because `y₃ ∈ (0,1)`.
* **`ε₁ = +1`** — `saddle_branch_eq_upper`. From two sign conditions, `Im y > 0`
  and `Re y ≤ 1`: they give `arg y ∈ (0,π)` and `arg(1−y) ∈ [−π/2, 0)`, so the
  branch expression lies in `(0, 7π/2) ⊂ (0, 4π)`. Nothing numeric.
* **`ε₂ = −1`** — the mirror, by conjugation.

`Re y₁ ≤ 1` is itself root data: `2·Re y₁ = 2 − y₃` with `y₃ ∈ (0,1)`, so
`Re y₁ = 1 − y₃/2 < 1`.

### The ledger now

| input to Route 64's capstone | status |
|---|---|
| the two pentagon values | **theorems** (54) |
| branch equation, real root | **proved** (65) |
| branch equation, complex roots | **proved from `Im y > 0`, `Re y ≤ 1`** (65) |
| `arg A₃ = (π − arg y₁)/3` | **proved from root data** (61, 62) |
| `\|y₁\|²y₃ = 1`, `y₂ = conj y₁` | not yet stated in Lean |

The last row is what is left before the capstone becomes unconditional in the
root data — and it is the conjugate-pair structure of a real cubic with one real
root, not anything about dilogarithms.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 66 — the root data, packaged; the branch datum `ε = (+1, −1, 0)` PROVED

Every hypothesis Route 64's capstone still carried is a consequence of one
bundle. `SaddleRoots` states it once:

    t : ℝ,  a : ℂ,  0 < t < 1,  Im a > 0
    a + conj a + t = 2,   a·conj a + a·t + conj a·t = 3,   a·conj a·t = 1

— a real root in `(0,1)` and a conjugate pair, with the three symmetric functions
being `X³ − 2X² + 3X − 1`. Each field is a checkable fact about the cubic and
nothing numeric appears anywhere.

### Derived from it, sorry-free

| fact | how |
|---|---|
| `cubic_t`, `cubic_a` | Vieta, one `linear_combination` each |
| `ne_zero`, `one_sub_ne_zero` | from `Im a > 0` |
| `two_re : 2·Re a = 2 − t` | the trace, real part |
| `re_le_one : Re a ≤ 1` | `two_re` and `t > 0` |
| `pair_rel` | Route 62 |
| `normSq_mul : \|a\|²·t = 1` | `Complex.mul_conj` and the product |

### The branch datum, proved

| | value | route |
|---|---|---|
| `branch_real` | `ε₃ = 0` | no window needed — both arguments vanish |
| `branch_upper` | `ε₁ = +1` | window, from `Im a > 0` and `Re a ≤ 1` |
| `branch_lower` | `ε₂ = −1` | the mirror, `saddle_branch_eq_lower` |

`ε = (+1, −1, 0)` was **measured** when this lane started, and the corpus's
`branch_data_of_cubic` proved only that the `ε` are *integers*. Their **values**
are now theorems, from the cubic and two sign conditions.

### What Route 64's capstone still needs

Only the two pentagon values (theorems) and the identification of its abstract
`A₃`, `B₃`, `a`, `b`, `c` with the `SaddleRoots` data. Every hypothesis in
between is now derived.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 67 — the first pentagon instance, derived from the root data

`SaddleRoots.pentagon_upper`:

    L(t) + L(a) + L(A₃) + L(1 − b⁻¹) + L(A₃⁻¹) = π²/2

with `A₃ = (1−t)/(1−at)` and `b = conj a` — **exactly the shape Route 64's
capstone takes as `P1`**, now a theorem about `SaddleRoots` rather than a
hypothesis.

Three facts make the pentagon's own five arguments fit that shape:

* `inv_A3` — `(1−a)/(1−at) = A₃⁻¹`, i.e. Route 55's `(1−a)(1−b) = (1−ab)²`
  applied to the pair `(a, t)` with third root `conj a`. Needed the cubic *and*
  the pair relation, with cofactors `−2t·R + 2a·C` on top of the reciprocal
  identity — a Gröbner reduction, not a guess.
* `one_sub_inv_conj` — `1 − b⁻¹ = 1 − a·t`, from `a·b·t = 1`.
* `A3_im_pos` — `Im A₃ > 0`: a positive real numerator over a denominator below
  the axis, `im_div_ofReal_pos` (new in `MathlibExt`, with its mirror).

### The remaining gap, stated exactly

`P2` — the same at `(t, conj a)` — is the mirror and is not yet written. With it,
Route 64's capstone becomes a theorem about `SaddleRoots` with **no hypotheses
beyond the structure itself**, giving

    2·Σ Li₂ = 2π²/3 − (iπ/2)(log A₃ − log B₃ + log b − log a)
              − (2/3)Σ log² + (2πi/3)Σ εⱼ log yⱼ

and the `ε` are already `branch_real`/`branch_upper`/`branch_lower`. The final
step to `−π²/6 − ½log²y₃ + (2/3)(θ−π)²` then needs `arg A₃ = (π−θ)/3`
(`saddle_clog_cube_of_roots`, proved) and `log a = −½log t + iθ`
(`normSq_mul`, proved, plus the argument).

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 68 — the capstone, with every hypothesis discharged from the root data

`SaddleRoots.sum_cLiTwoExt_root_data`:

    2·Σ Li₂ = 2π²/3 − (iπ/2)(log A₃ − log B₃ + log b − log a)
              − (2/3)·Σ log² + (2πi/3)·(1·log a + (−1)·log b + 0·log t)

**No hypotheses beyond the `SaddleRoots` structure.** Every input Route 64 listed
is now a theorem about it:

| input | discharged by |
|---|---|
| pentagon at `(t, a)` | `pentagon_upper` (67) |
| pentagon at `(t, conj a)` | `pentagon_lower` — the mirror, by conjugating `inv_A3` and `one_sub_inv_conj` |
| `Im A₃ > 0`, `Im B₃ < 0` | `A3_im_pos`, `B3_im_neg` (`B₃ = conj A₃`, since `t` is real) |
| the three branch equations | `branch_upper`, `branch_lower`, `branch_real` (66) |
| the `ε` values | now literally `1`, `−1`, `0` in the statement |

The mirror cost nothing: `B₃ = conj A₃`, and each `A₃` fact conjugates.

### ⚠ What the right side still is

**Logarithms**, not `−π²/6 − ½log²t + (2/3)(θ−π)²`. Turning it into that needs two
substitutions, both already proved from root data but not yet applied here:

* `arg A₃ = (π − arg a)/3` — `saddle_clog_cube_of_roots` (61, 62);
* `log a = −½·log t + i·arg a` — `normSq_mul` (66) plus the argument.

So the chain is complete from the pentagon to a logarithmic expression for `A`,
with nothing assumed but the cubic's root structure; what is not done is the last
substitution into the sum rule's stated form.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 69 — the sum rule's stated form, from `SaddleRoots`. And the one gap that is left.

`SaddleRoots.sum_cLiTwoExt_closed`:

    Σ Li₂ = −π²/6 − ½·log²t + (2/3)·(arg a − π)²

for **every** `S : SaddleRoots`. Every logarithm in Route 68's capstone is
evaluated:

* `log a = −½·log t + i·arg a` — from `‖a‖²·t = 1` (`norm_sq_eq`, `log_norm`);
* `log b = conj` of it;
* `log A₃ = ½·log t + i·(π − arg a)/3` — from Route 61's angle identity
  (`three_log_A3`), instantiated at the root data;
* `log B₃ = conj` of it.

What is left after substitution is `π²`, `log t`, `arg a` — the sum rule's target
expression, exactly as the corpus records it.

## ⚠⚠ THE GAP: `SaddleRoots` IS NOT PROVED INHABITED

A theorem `∀ S : SaddleRoots, …` is worth exactly what the inhabitation is worth,
and **inhabitation is not established anywhere in this chain**. Nothing here
proves that `X³ − 2X² + 3X − 1` has a real root in `(0,1)` together with a
conjugate pair — it is true (numerically `t = 0.4301597…`, `a = 0.78492 +
1.30714i`), and the probes have measured it since Route 42, but it is not a Lean
theorem.

That is now the whole gap, and it is a **root-existence** problem, not a
dilogarithm one:

* the real root: IVT on `f(0) = −1 < 0`, `f(1) = 1 > 0` — `intermediate_value_Ioo`;
* the conjugate pair: the residual quadratic `x² + (t−2)x + 1/t` has discriminant
  `(t−2)² − 4/t ≈ −6.84 < 0`, so its roots are non-real conjugates;
* then the three symmetric functions are Vieta.

Until that is done, `sum_cLiTwoExt_closed` proves the sum rule's **shape** holds
of any `SaddleRoots`, and says nothing about the actual 5₂ saddle sum.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

---

## Route 70 — THE GAP IS CLOSED. `SaddleRoots` is inhabited; the 5₂ sum rule is PROVED

Route 69 left one thing owed, and said so in capitals: `SaddleRoots` was not
proved inhabited, so `sum_cLiTwoExt_closed` proved the sum rule's *shape* and
said nothing about the actual 5₂ saddle sum. That is now discharged.

### The inhabitation (`FiveTwoComplexPentagon`, `SaddleRoots` namespace)

* `exists_real_root` — `intermediate_value_Ioo` on `f(x) = x³ − 2x² + 3x − 1`
  over `[0,1]`, with `f(0) = −1 < 0 < 1 = f(1)`. Gives `t ∈ (0,1)` with
  `f(t) = 0`.
* `disc_pos` — `0 < 3t² − 4t + 8` for **every** real `t`, by
  `nlinarith [sq_nonneg (3t − 2)]`. Unconditional, so no root-location
  side-condition is needed to take the square root.
* `ofRealRoot` — builds the conjugate pair explicitly as
  `a = (2−t)/2 + (√(3t² − 4t + 8)/2)·i`, and discharges the four structure
  fields (`hsum`, `hp2`, `hprod`, `him`) by Vieta from `f(t) = 0`.
* `instance : Nonempty SaddleRoots`.

The gap was, as recorded, a **root-existence** problem and not a dilogarithm
one; it priced out at exactly the three steps Route 69 predicted.

### The headline theorems

`fiveTwo_saddle_sum_rule` — quantified over nothing, hypotheses on nothing:

    ∃ t : ℝ, ∃ a : ℂ,  0 < t < 1,  0 < Im a,
      t, a, ā  all roots of  X³ − 2X² + 3X − 1,   and
      Li₂(a) + Li₂(ā) + Li₂(t) = −π²/6 − ½·log²t + ⅔·(arg a − π)²

`fiveTwo_sum_V` — the same in `V`-form: `Σ Vⱼ = −3π²/2 + 2π·log t·i`, so
`Σ Re Vⱼ = −3π²/2`. The imaginary part is a **bonus**: the corpus only ever
recorded the real part, and `2π·log t` was not part of the target.

`fiveTwoSaddleSumRule_holds` — the corpus's own conjecture class
`QOU.QBeta.FiveTwo.FiveTwoSaddleSumRule`, whose docstring read "No instance is
provided: the statement is open", constructed at `Li = cLiTwoExt`,
`y = ![a, ā, t]`, `b = ![−1, +1, +1]`.

### Verification (per-module, `.olean` deleted first, `lake` not `lean`)

* `lake build QOU.QBeta.FiveTwoComplexPentagon QOU.QBeta.FiveTwoFlattenedPentagon`
  → exit 0, 3241 jobs, **0 warnings**.
* `lake build QOU.QBeta.FiveTwoSaddleSumRule` → exit 0, 1893 jobs.
* `#print axioms` on `fiveTwo_saddle_sum_rule`, `fiveTwo_sum_V`,
  `fiveTwoSaddleSumRule_holds`, `SaddleRoots.ofRealRoot`,
  `SaddleRoots.exists_real_root` → all `[propext, Classical.choice, Quot.sound]`.
* Zero `sorry` in code across the three modules (the 11 grep hits are all the
  string "sorry-free" in docstrings).
* `origin/main` at the time of measurement: `f689f12d2d06aee2959002f13b9ac39c1a79e3cf`.

### The probe is a control on the STATEMENT, not evidence

`computations/probes/qbeta_5two_route70_sum_rule_proved_probe.py`, 80 dps, all
four gates pass. A proved theorem needs no numerics; what it *can* still be is
a proof of the wrong statement, and that is the failure mode a proof cannot
detect. So:

* **G1** the witnesses are as described — real root in `(0,1)`, conjugate pair,
  all three roots of the cubic;
* **G2 — the one that matters** — the expression proved is the one the corpus
  recorded: `A_computed` matches the recorded `A = 0.9717306814686482591277741699`
  and the closed form to `< 1e-60`;
* **G3** the branch assignment is **pinned, not chosen**: of five assignments
  tried, `b = (−1,+1,+1)` is the *only* one reaching `−3π²/2`; the others miss
  by 9.87 to 25.9;
* **G4** the scope, stated so it cannot be overread: `D` cancels identically on
  the Galois sum (`|Σ D| < 1e-50`), which is exactly why the sum rule fell
  without touching the volume.

`probe-float64-guard.py --diff` run in place: clean.

### Stale claims corrected

The standing claim "The 5₂ sum rule remains verified to 80 dps, unproved" was
true for 69 routes and is now false. All 13 occurrences replaced across
`ComplexRogersDilog.lean` (1), `FiveTwoComplexPentagon.lean` (6),
`FiveTwoFlattenedPentagon.lean` (3), `FiveTwoSaddleSumRule.lean` (3). The last
file's header, its `FiveTwoSaddleSumRule` class docstring ("the statement is
open"), and its `FiveTwoDilogLadder` docstring ("a second independent relation
is required to close the sum rule") were all rewritten — the ladder is still
unproved but is **no longer needed**, since the route that worked was the
pentagon, which determines `A` outright.

### What is NOT proved

The 5₂ **volume** conjecture. `Vol(5₂) = 3·D(y₁)` with `D` the Bloch–Wigner
function, and `D` cancels on the Galois sum — so nothing in this lane speaks to
it. Do not let the sum rule's proof be read as progress on the volume.

`FiveTwoDilogLadder` also remains unproved, and off the critical path.

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. Bean `qou-xblo`
and its parent `qou-0yqu` are closed by this route.
