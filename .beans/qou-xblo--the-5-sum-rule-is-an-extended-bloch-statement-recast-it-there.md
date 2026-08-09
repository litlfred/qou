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
