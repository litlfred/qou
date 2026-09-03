---
# qou-m3sh
title: 'Fary-Milnor: total curvature is the substrate-computable half of the serpenoid tower; the twist is the other half'
status: todo
type: task
created_at: 2026-09-03T04:32:27Z
updated_at: 2026-09-03T04:32:27Z
---


Queued by the owner behind the size-only recursion write-up. Prompted by the
serpenoid image (swimming snake + the drawn family of its osculating circles),
with the note that the right-hand panel is "almost like tower".

## What the picture actually is
A serpenoid is *defined* by sinusoidal curvature in arclength, `kappa(s) =
a sin(omega s)`. So the osculating radius `rho = 1/kappa` runs from a finite
minimum `1/a` at each curvature extremum out to `infinity` at each inflection,
and repeats every half-period. Drawing the whole family gives a scale-indexed
pencil that blows up at each inflection and repeats — which is why it reads as a
tower. The dots on the axis are the centres: the **evolute**, cusped at the
curvature extrema, escaping at the inflections.

## Why it is the right analogy, and where it stops
It is a one-parameter family of purely LOCAL second-order data (an osculating
circle is `kappa` and nothing else) whose *correlation structure* — the envelope,
the evolute — recovers the global curve. That is structurally the owner's point
about the tower: you do not read the graded piece off order zero, you read the
correlations between order-zero observables, and those are indicative.

The analogy stops in a place that is USEFUL rather than disappointing. The
osculating circle sees `kappa` and is blind to torsion `tau`. Calugareanu splits
`Lk = Tw + Wr`; `Wr` is a crossing count (integer, combinatorial) and `Tw =
(1/2pi) * integral of (tau + dtheta/ds)` is the torsion integral. So the picture
is exactly the curvature half, and the twist is exactly the half it does not
show.

That maps onto what the arc already measured: the trace produces `kappa`-like
data — local bond constants, additive over components, exchangeable, routing-
invariant (all four now confirmed at 200 bits, `qou-wx83`) — and the ONE thing
the hull-exit analysis says is needed and missing is a fractional framing
scalar, i.e. twist, not writhe (`the_hull_exit_is_a_fractional_twist_probe`,
`the_twist_is_absent_where_it_is_needed_probe`).

## The concrete attempt
Fary-Milnor: a closed curve with `integral kappa ds <= 4pi` is unknotted. Total
curvature is a SUM OF LOCAL SECOND-ORDER DATA, which is the shape of quantity
this machinery evaluates well — unlike torsion. So the question to pose is
whether a substrate analogue of `integral kappa ds` exists as an order-zero
trace observable, and whether the `4pi` threshold has an image under it.

Success would be a knottedness obstruction the substrate can evaluate. It would
NOT supply the twist; nothing here does. Worth stating in advance so the result
is not oversold either way: this is a test of whether the curvature half is
reachable, and the honest prior from the twist probes is that the half that
matters for the binding gap is the other one.

## Prerequisite
Do not start this before the size-only recursion probe lands (A=6 homonuclear,
running exact at 128 bits).
