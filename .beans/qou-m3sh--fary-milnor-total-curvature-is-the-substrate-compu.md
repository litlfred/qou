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

## Result (2026-09-03) — `total_curvature_is_the_computable_half_probe.py`, 23/23

**The curvature half is worth `2π(2A+1)`, and the round-chain picture is
refuted.** Exact-integer Kauffman bracket on each component of the canonical
closure (other strands deleted), both classical branches of the `2A+1`
averaged letters:

| A | μ | components (σ branch)              | components (σ⁻¹ branch)             | inf ∫κ ≥ |
|---|---|------------------------------------|-------------------------------------|----------|
| 2 | 3 | T(2,7), T(2,7), unknot             | T(2,5), T(2,3), unknot              | 2π·5     |
| 3 | 4 | T(2,7)×3, unknot                   | T(2,5), T(2,3), T(2,3), unknot      | 2π·7     |
| 4 | 5 | T(2,7)×4, unknot                   | T(2,5)×2, T(2,3)×2, unknot          | 2π·9     |
| 6 | 7 | T(2,7)×6, unknot                   | T(2,5)×3, T(2,3)×3, unknot          | 2π·13    |

Every multi-strand component is a `(2, odd)`-torus knot — never an unknot —
on both branches, for every isotope. The single 1-strand component is the
unknot. So `b(L) ≥ μ + #knotted = (A+1) + A = 2A+1`, and Milnor gives

    inf ∫κ ds  ≥  2π(2A+1)      (slope 4π per nucleon, extensive)
    inf ∫κ ds  ≤  2π·3A         (braid presentation)

Fáry–Milnor proper: each knotted component has `∫κ > 4π` on every realisation.
Consecutive pairs are NOT `(2,2lk)`-torus links (all 2×14 pairs tested), so the
"round chain of unknots" that would have made the bound sharp is refuted — the
bound is a floor, not a value.

**Cross-corpus consequence, and it matters more than the curvature.** The
triton Borromean model (`binding_mn_milnor_linking.py`) and the μ̄-route
(`atom_closure_milnor_indeterminacy_probe`) both lean on the Brunnian picture:
pairwise-unlinked UNKNOTS whose whole content sits in a triple invariant.
Milnor's μ̄ is defined for any link, but that picture is not: the canonical
closure's components are `(2,odd)`-torus knots on every branch, each carrying
its own knot-level content (non-trivial Jones, bridge number 2) before any
linking is counted. That is a second, independent obstruction to modelling
the triton as Borromean rings, on top of the non-vanishing pairwise linking
that probe already found. Forward pointer added there.

**Reeb / saddle points, answered.** Under Crofton, `∫κ ds = π·⟨μ_v⟩` where
`μ_v` is the number of critical points of the height function in direction
`v`, averaged over the sphere. The oscillations ARE the curvature, integrated;
the Reeb graph of each height function has those critical points as nodes.
Milnor's `μ_v ≥ 2b` is what turns the count into the bridge bound.

**Not done, and not claimable:** no connection from this bound to binding; no
twist. `Tw` is a torsion integral and the osculating circle is blind to it.
The bound's extensivity (`4π` per nucleon) is noted next to the `θ_λ` gate's
need for an extensive channel as a shape coincidence, nothing more.

- [x] compute per-component knot types on both branches, A = 2,3,4,6
- [x] Milnor bridge bound from μ + #knotted
- [x] round-chain test (refuted)
- [x] forward pointer on `atom_closure_milnor_indeterminacy_probe`
- [ ] is `2A+1` sharp? needs `b(L)` from above: a `(2A+1)`-bridge presentation or a
      stronger lower bound. Open.

## The pencil, explicitly (owner asked 2026-09-03)

Plane: Tait–Kneser nest of osculating circles per quarter-wave, centres on the
evolute; a linear pencil only in the concentric case; coordinates `(s, θ)` on
the foliated region, singular at vertices and inflections; defined on a CURVE,
so not on the substrate's isotopy class. Space, on a curve: the Frenet framing
it induces has `Lk = Wr + (1/2π)∮τ ∈ ℤ` — the torsion the pencil is blind to
is exactly the framing datum the hull-exit needs.

Complement, invariantly — two pencils, both present because the components are
torus knots: (i) the Milnor open book (pages of genus g, binding K, monodromy
order 2(2g+1), Seifert form unimodular ⇒ `H₁(page)` self-dual: a frame with a
dual frame); (ii) the Seifert circle fibration (orbits of the (2,2g+1)-weighted
circle action = Reeb orbits, transverse to the pages, two exceptional fibres of
orders 2 and 2g+1, K a regular fibre). Coordinates: page angle × page point, or
orbifold base × fibre angle. The 2g Morse saddles of a morsification of
`z² + w^(2g+1)` are the vanishing cycles whose Dehn twists compose to the
monodromy — that is "the oscillation is driven at the saddle points", exactly.

Frobenius: corpus sense = trace pairing making A self-dual (`frobenius_relation`);
page sense = unimodular Seifert form; algebra sense = Markov–Gram form on TL_n
(exact inverse in `pyhecke.tl`). NOT established: a map TL_n-frame → complement
frame (would need the skein module of the complement; not computed).

Computed: Bennequin `χ = k − c = −5` for every multi-strand component on both
branches, so Bennequin genus 3 throughout. σ branch: every component is T(2,7)
of genus 3, so the Bennequin surface has MINIMAL genus and — fibered knots
having a unique minimal-genus Seifert surface — is isotopic to the page. (Most
of those sub-braids are also positive as written; a few carry one σ⁻¹ that does
not cancel freely, so the page claim rests on genus, not Stallings. First draft
of this note said "all positive" — wrong, corrected by the probe's own check.)
σ⁻¹ branch: words mixed, Bennequin surface non-minimal (3 > g). Seifert matrices of T(2,3/5/7):
det V = 1, Δ = (tⁿ+1)/(t+1), monodromy order 2n — all verified exactly.

- [x] pencil made explicit; fibration/Seifert data added to the probe (§F)
