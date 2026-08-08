---
# qou-glbl
title: 'Gap A: the globally differentiable root labelling — the last hypothesis in the transport'
status: todo
type: task
priority: high
tags:
    - lean
    - 5two
    - qou-trns
    - envelope
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-08-08T17:30:00Z
---

## What is open

`hasDerivAt_envelopeS` (`S′ = 2φ`) and `envelopeS_total` (`S(π) − S(0) = π²`)
are proved in `QOU/QBeta/FiveTwoTransport.lean`, but they take the root
labelling `Y₁, Y₂, Y₃ : ℝ → ℂ` as **given, differentiable functions**. Supplying
that labelling is the single remaining hypothesis in the transport chain —
every other input in the table is proved.

## Why it is narrow, and much narrower than it was

Three measurements have shrunk it:

1. **`S` is symmetric in the roots**, so as a function of `φ` it needs no
   labelling to be *defined* — only to be *differentiated term by term*, which
   is local. `envelope_integrate` already tolerates one exceptional point.
2. **Route 32 G8: the real root never collides.** `|∂p/∂y|` at the positive real
   root never drops below **1.75** on the arc. Only the *other two* roots
   collide, and only at `φ₀ = 137.9206708879635°`.
3. **The symmetric functions of the colliding pair are smooth.** With `t` the
   real root, `y₂ + y₃ = 2c − t` and `y₂y₃ = 1/t` — both differentiable wherever
   `t` is, with no exceptional point.

So the obstruction is confined to **splitting one quadratic with smooth
coefficients**, at one point where its discriminant vanishes.

## Attack vectors

### B1 — Split the labelling: `t` globally, the pair symmetrically
Prove `t : ℝ → ℝ` differentiable on all of `[0,π]` directly from the scalar IFT
(`QOU/MathlibExt/ImplicitScalar.lean`, already proved), using `|∂p/∂y| ≥ 1.75`
as the non-degeneracy hypothesis — **no exceptional point at all** for `t`.
Then handle `y₂, y₃` only through `y₂ + y₃` and `y₂y₃`, never individually.
**This is the intended route** and the reason Route 32 measured the 1.75 bound.
The question to settle first: does `Σⱼ ∂V/∂x` and the envelope collapse actually
factor through the symmetric functions, or does some step need `y₂` alone? If
the latter, B1 fails and B2/B3 are needed.

### B2 — Accept the exceptional point and use what already exists
`constant_of_hasDerivWithinAt_zero_off_point`
(`QOU/Archimedean/ConstantOffOnePoint.lean`, proved) is built for exactly this:
continuous everywhere, derivative zero off **one** point. If the labelling can
be made differentiable on `[0,π] ∖ {φ₀}` and `S` shown merely *continuous* at
`φ₀`, the theorem closes with no global labelling at all. Continuity of `S` at
`φ₀` should be easy — `S` is symmetric, and the roots vary continuously through
a collision even though the labelling does not. **This may be strictly easier
than B1** and it reuses a lemma already in the tree.

### B3 — Local IFT on each side, glued
Two applications of the scalar IFT on `[0, φ₀)` and `(φ₀, π]`, then glue. The
gluing is where it gets delicate: `dy/dφ` **diverges** like
`0.65040643/√|φ−φ₀|` (Route 31 G6, `C = 2.6016257` stable over five decades), so
the labelled derivative does not extend. What saves it is that `∂V/∂y = 0`
annihilates the divergent `y′`, leaving the labelled *term's* derivative bounded
at **2.7268867** all the way in. That is the envelope theorem visible
numerically — but turning "the product stays bounded" into a Lean derivative
statement at `φ₀` needs care, and a first draft of Route 31 G6 got the reason
wrong (it claimed the terms *jump*; they do not).

### B4 — Puiseux / square-root parametrisation through the collision
The two colliding roots separate like `C·√|φ−φ₀|`, so `y₂, y₃` are analytic in
`√(φ−φ₀)`, not in `φ`. A labelling in the Puiseux variable would be globally
smooth. **Costly**: Mathlib has no Puiseux-series API for this, and it would be
new infrastructure for one point. Listed for completeness; do not start here.

## Do this first

**Decide between B1 and B2 by inspection, not by proving either.** Read
`FiveTwoEnvelopeSum.lean` and `FiveTwoEnvelopeWiring.lean` and answer one
question: does any proved step need an individual `y₂`, or do they all factor
through `y₂+y₃` and `y₂y₃`? That single answer picks the route and saves
attempting the wrong one.

## ⚠ What this does NOT get you

Closing this proves `S(π) − S(0) = π²`. **That is not the sum rule.**
`S(0) = −3π²/2` *is* the 5₂ sum rule (residual 1e-30) and `S(0) = 3·S(π)`, so
the transport **reformulates** the sum rule rather than approaching it. Anyone
picking this up should know that before starting: it closes a named gap in a
proved chain, it does not move the headline.

## Refs

* `qou-trns` (parent), `qou-0yqu`, `qou-rstq`
* Proved and waiting on this: `QOU/QBeta/FiveTwoTransport.lean`
* Tools already in tree: `QOU/MathlibExt/ImplicitScalar.lean`,
  `QOU/Archimedean/ConstantOffOnePoint.lean`
* Probes: Route 31 (G4 non-vacuity, G6 the bounded-derivative measurement),
  Route 32 (G8 the 1.75 bound)

**The 5₂ sum rule remains verified to 80 dps, unproved.**
