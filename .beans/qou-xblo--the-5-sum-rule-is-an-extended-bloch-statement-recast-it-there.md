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
(6 gates, all pass, dps 45). Source: **`uploads/0307092v2.pdf`** — W D Neumann,
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
