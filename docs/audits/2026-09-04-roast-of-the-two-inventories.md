# Roast: what the two inventories could not have found

**2026-09-04.** Adversarial pass over the 27 beans produced by the citation-gap
and Mathlib-infrastructure inventories (`2babf21b46`, `d12aa51089`), asking not
*"are they right?"* but *"do they land what the arc needs?"*

Both inventories are sound within their scope. The criticism is about the scope,
and it is mine rather than theirs: **I asked two agents what *infrastructure* is
missing, and neither could have found what *mathematics* is missing, because I
did not ask.**

---

## R1 — the arc's own open step is beaned nowhere

The owner's ask this session, verbatim: *"remember the knots themselves are
operators and sewing should be able to extend the knot actions to the knot
complement, or show that they degenerate there."*

Measured across the whole tracker and corpus:

| term | `content/` | `docs/` | `.beans/` |
|---|---|---|---|
| `sewing` | 0 | 0 | **0** |
| `sewn` | 0 | 0 | **0** |
| `gluing axiom` | 0 | 0 | 0 |
| `extend.*action.*complement` | 0 | 1 | **0** |

Checked under other names too, in case the concept is present with different
vocabulary: `TQFT` (28 / 46 / 6), `Turaev` (76 / 58 / 15), `cobordism`
(8 / 3 / 1). So the *ambient literature* is well represented and the
*specific move* is not: no bean, no content block, no audit asks whether the
knot-as-operator action extends across the complement or degenerates there.

The corpus does have the operator side —
`braids-and-knots/fundamental-knots-operator-basis.md` and six siblings state
knots as operators. What is missing is the extension.

**Why neither agent found it.** The citation agent looks for a claim with a
source that does not carry it; the Mathlib agent looks for an API that does not
exist. This is neither: it is a mathematical question nobody has asked in a
durable artifact, so it has no citation to be wrong and no API to be absent.
**A gap with no artifact is invisible to an artifact-scanning sweep.**

Beaned as `qou-yb2b`.

## R2 — a completed bean already answers the arc's headline question

`qou-52fu` — *"T3e: PGL(3) decoration of the knot complement (higher
Teichmüller)"*, **completed 2026-08-04**, parented to this same epic
`qou-8lxd` — records:

> Answers 'does hyperbolic geometry on the complement give SU(3)?' -- **NO**:
> the holonomy of a hyperbolic structure is `rho: pi_1 -> PSL(2,C)`, **RANK 1**.
> Hyperbolic geometry supplies MORE SL(2) [...] QOU is an SL_2 theory
> throughout. The right object is instead the PGL(3,C) analogue:
> Garoufalidis-Thurston-Zickert gluing equations for PGL(n), Fock-Goncharov
> coordinates, higher Teichmüller.

Neither agent surfaced it. Both ran corpus-grep paths 1-5 diligently and
neither ran **path 6 (`.beans/`)** against the *arc's own question* — they ran
their greps against their own subject matter. Path 6 exists precisely because a
prior agent's conclusion often sits in a bean body and nowhere else, and a
**`completed`** bean is the one that bites.

**This is not an over-claim in the hyperbolic-volume audit.**
`2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md` is about the
volume feeding **mass and binding**; it never claims a flavour route, and a grep
for `eightfold|SU(3)|flavour` in it returns one line, a file path. But the audit
sits under an *eightfold* epic with an eightfold-sounding title, and a reader
will assume otherwise. One citation fixes it, added in this commit.

**What it does change** is the ranking below.

## R3 — the largest BUILD item's justification over-reaches by half

`qou-jvua` (manifold differential `k`-forms, **~300-600 lines**, the inventory's
own "unblocks the most") justifies itself as:

> the prerequisite for any statement about the contact volume form or the
> hyperbolic volume form as objects rather than as degree counts.

For the **hyperbolic** form that is right. For the **contact** form it is not,
and the arc's own strongest result says so.
`QOU/QuantumObservableUniverse/CalculusDimensionObstruction.lean:63` states the
categorical route is *"**stronger**, because it needs no manifold, no metric, no
`H = ker Θ ⊂ TM`"*, and `:156` has the volume form *"constructed with no
manifold"* — `Θ_A ∧ dΘ_A` in the Woronowicz calculus on `𝒪_q(SU(2))`. The
corpus **already has** the contact volume form as an object.

So the item is half-motivated on its own terms, and its surviving half serves
the route `qou-52fu` calls rank-1. That does not make it worthless — Milnor's
`Λ`-sum is currently a *definition* and only forms would let anyone connect it
to a metric volume — but it does mean **300-600 lines is not the cheapest next
step**, and the inventory's own `qou-tc8y` (**~5 lines**, a sealed `opaque`
whose body is already written next door) almost certainly is.

Appended to `qou-jvua` rather than filed separately, since it is a correction to
that bean's scope, not a new gap.

---

## What holds

Both inventories' *findings* survive this pass unchanged. The eight false
"Mathlib lacks X" claims are real and checkable; the "held ≠ held in full"
distinction is real and is the sharpest thing either agent produced. Nothing
here retracts a measurement.

## The method lesson, for the next sweep

Three sweeps this session were scoped by **artifact type** — citations, Mathlib
API, Lean declarations. Every one of them is blind to a gap that has no
artifact. A fourth sweep scoped by **the argument's own steps** — take the
claim chain end to end and ask, at each arrow, *what would have to be true* —
would have found R1 immediately and R2 by construction. That is the sweep to
run first next time, and the other three afterwards.
