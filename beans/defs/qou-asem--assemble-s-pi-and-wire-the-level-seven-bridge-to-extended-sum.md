---
# qou-asem
title: 'CLOSED: S(π) = Σⱼ Re V(−1, yⱼ) = −π²/2 assembled in Lean'
status: completed
type: task
priority: medium
tags:
    - lean
    - 5two
    - qou-trns
    - assembly
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-09-26T11:03:25Z
---

## ✅ CLOSED 2026-08-08

    sum_re_deformedV_at_neg_one (hx : x³ − 2x² − x + 1 = 0) (hlo : 1/2 < x) (hhi : x < 1) :
      Σⱼ (deformedV (−1, yⱼ)).re = −π²/2

`QOU/QBeta/FiveTwoLevelSevenAssembly.lean`, sorry-free, `lake`-verified (3250
jobs), axioms `[propext, Classical.choice, Quot.sound]`, wired into `QOU.lean`.

Four proved pieces composed, exactly as C1 anticipated — except that C1's
"state the missing argument as an explicit hypothesis" was **not needed**,
because `qou-rstq` item 4 closed first and left nothing missing:

| piece | role |
|---|---|
| `extended_sum` | `Σₖ (2·extend L(wₖ) + extend L(−wₖ)) = π²/2` |
| `extend_eq_re_cRogersL` | item 4 — turns every `extend` into `Re` of the analytic `L` |
| `levelSeven_orbit_data` | **new** — the `wₖ` negated *are* the level-7 roots, with the signs `corr_sum_eq_neg_pi_sq` needs |
| `corr_sum_eq_neg_pi_sq` | `Σⱼ corr yⱼ = −π²` |

Two new supporting theorems:

* `deformedV_neg_one_eq` — at `x = −1`, `V` splits as
  `2·L(−y) + L(y) + (corr's integrand)`, an identity in `ℂ` before any real part
  is taken. The `corr` definition turns out to be exactly the leftover.
* `levelSeven_orbit_data` — `y ↦ −y` carries `x³−2x²−x+1` to `y³+2y²−y−1`, so
  `extended_sum`'s six arguments are the level-7 roots and their negatives.
  Proved rather than assumed: "the same up to sign" is the kind of step that
  turns out to be off by a reciprocal.

### ⚠ What this is NOT — C3's warning, restated because it still applies

`S(0) = −3π²/2` **is** the 5₂ sum rule; `S(π) = −π²/2` is the *other* endpoint,
and `S(0) = 3·S(π)`. This assembles one endpoint of a transport that
**reformulates** the sum rule rather than approaching it.

It is a composition of proved parts, and **the parts were the work** — item 4
in particular. Nothing here narrows the headline.

Still open: **Gap A** (`qou-glbl`), the globally differentiable root labelling,
which is what would connect `S(π)` to `S(0)`.

### C2's independence held

C2 predicted this would not need the labelling to be differentiable, only its
value at one point. Correct — `sum_re_deformedV_at_neg_one` takes no
differentiability hypothesis at all, so it is independent of `qou-glbl`.

## The original framing (superseded)

## What was open

Both ends exist in Lean and are **not connected to each other**:

* `extended_sum` (`FiveTwoAbelFiveTerm.lean`) — `Σₖ (2·extend L(wₖ) + extend L(−wₖ)) = π²/2`
* `corr_sum_eq_neg_pi_sq` (`FiveTwoLevelSevenBridge.lean`) — the log-bilinear
  correction sums to `−π²`, with **no dilogarithms left in it**

Route 32 established on paper that at `x = −1` the curve's cubic **is** the
level-7 cubic `y³+2y²−y−1`, that `wₖ = −yⱼ` exactly, and that the difference
between the two sides is precisely that `−π²`. Nobody has written the composition.

## Why this is now worth doing

It was blocked on `extend ≡ Re L`. That is no longer wholly blocked: as of
2026-08-08 the identification is proved for **five of the six arguments**
(`qou-rstq` item 4; the Landen and identity regimes). Only `w₁ = 2.24698`
remains, and it is `qou-invr`.

So this bean is now: **assemble everything except the one argument, and state
the residual dependency in the theorem's hypotheses rather than in prose.**
That is worth doing *before* `qou-invr` closes, because it converts "several
things are open" into "one hypothesis, named, with everything else discharged"
— and because assembly has repeatedly exposed false claims in this lane.

## Attack vectors

### C1 — Assemble with the missing argument as an explicit hypothesis
State the target theorem with a hypothesis of the exact shape
`extend (π²/6) rogersL w₁ = (cRogersL (w₁ : ℂ)).re`, discharge everything else
from proved results, and leave that one hypothesis open. **This is the right
first move.** It is honest (the gap is visible in the signature, not buried),
it is checkable now, and when `qou-invr` closes the hypothesis is discharged by
one rewrite. The lane's own record argues for it: *"'assembly of proved parts'
is not a status — it is an unexamined region"*, and two of the three joins
closed this way exposed a false claim in the parts.

### C2 — Define `S(π)` concretely and evaluate at `x = −1`
`envelopeS` is defined for a general labelling `Y₁,Y₂,Y₃ : ℝ → ℂ`. At `φ = π`,
`arcX π = −1` and the roots are the three real roots of the level-7 cubic — all
explicit. Instantiate `envelopeS` at that point with the explicit roots and
show `S(π) = Σⱼ Re V(−1, yⱼ)` unfolds to something `corr_sum_eq_neg_pi_sq` and
`extended_sum` jointly evaluate. **Does not need the labelling to be
differentiable** — only its value at one point — so it is independent of
`qou-glbl`. Worth checking that independence explicitly before starting.

### C3 — Verify the composition numerically FIRST, at 50 dps
Before any Lean: evaluate both sides at `x = −1` with the three explicit roots
and confirm the `−π²` accounts for the difference **exactly**, at the arguments
`extended_sum` actually uses — not at a generic sample. Route 32 did this at the
level of the bridge; the *composition* has not been checked end to end. If the
composition is off by anything, it is off by a `π²`-rational and that will show
up immediately.

## ⚠ Two things to hold onto while doing this

1. **`S(π) = −π²/2`, and `S(0) = −3π²/2` IS the sum rule.** Assembling `S(π)`
   does not approach the sum rule; `S(0) = 3·S(π)` is a relation between two
   values of a reformulation. Do not let the assembly's success read as progress
   on the headline.
2. **Route 32 G9 exists to stop exactly one mistake here.** It asserts that the
   numeric bridge uses the *analytic* Rogers `L` while `extended_sum` is about
   the *piecewise* `extend`, and it is written to FAIL if the lane ever quietly
   treats them as the same. When `qou-invr` closes, G9 must be updated
   deliberately — not silently satisfied.

## Refs

* `qou-trns`, `qou-rstq` item 4, `qou-invr` (the one remaining argument),
  `qou-glbl` (independent of this, per C2)
* Lean: `FiveTwoAbelFiveTerm.lean`, `FiveTwoLevelSevenBridge.lean`,
  `FiveTwoTransport.lean`, `FiveTwoExtendIdentification.lean`
* Probes: Route 32 (the map, and G9 the guard), Route 34 (five of six arguments)

**The 5₂ sum rule remains verified to 80 dps, unproved.**
