---
# qou-m3sh
title: 'Fary-Milnor: total curvature is the substrate-computable half of the serpenoid tower; the twist is the other half'
status: in-progress
type: task
priority: normal
created_at: 2026-09-03T04:32:27Z
updated_at: 2026-09-03T19:40:59Z
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

## Bring's curve as the frame (owner: "we have Bring's curve", 2026-09-03)

The corpus already derives Bring's genus from torus-knot embeddability
(`BringsSurface/EulerCharacteristicSix.lean`): `T(2,9)` must embed (Seifert
rank 4 ≤ g), `T(2,11)` must not (5 > g) ⇒ `g = 4`, `χ = −6`. So the pages of
every component found here — `T(2,3/5/7)`, genera 1/2/3 — embed in Bring's
surface by the corpus's own criterion, with `T(2,9)` the maximal one.

Link of the Bring cone = circle bundle over `Σ₄` of Euler number `−deg = −6 =
χ(Σ₄)`, i.e. the unit tangent bundle `UT(Σ₄) = PSL(2,ℝ)/Γ₄`, an `~SL₂`
manifold (Bézout 1·2·3 = 6, adjunction K = O(1)). The component complements
`S³∖T(2,2g+1) = PSL(2,ℝ)/Δ(2,2g+1,∞)` are the same kind of object. Both carry
the global left-invariant frame {X geodesic, Y horocyclic, V fibre rotation}:
THAT is the coordinate frame in the complement, and it is the frame the Bring
cone link carries. Two Reeb flows on each: V (Seifert circles = the circle
pencil, Boothby–Wang form) and X (geodesic, Liouville form; closed orbits =
closed geodesics of the orbifold, modular-type knots in the complement).

**Flag, not verdict:** `BringCone.lean` models the cone-link Reeb triad on
quaternion right-multiplication, `[M_i,M_j] = 2M_k` — the compact form su(2),
i.e. the S³/Hopf picture — while `UT(Σ₄)` for a genus-4 hyperbolic surface
carries the split form sl₂(ℝ). The "degenerate quaternionic-contact" qualifier
may be doing this work; someone should say which real form is meant.

Saddle points already in the corpus: 4 turning points of `y⁵+y+x = 0`
(`TurningPoints.lean`, `5y⁴+1 = 0`, monodromy S₅) and 6 branch points of the
chiral cubic (`bring_cubic_monodromy_probe`, transpositions, sign surjective).
Corpus Reeb status: rotation channel blind to p/n (2026-06-01); constant-scale
`D/Σ|Δθ|` falsified at ⁴He, directional correlation survives (2026-06-24);
`ReebLinkingCWF.lean` derives the pn linking amplitude `ℓ(z) = z/√(1+z²)` from
Markov + CWF + Kauffman transverse selection — the corpus's own Călugăreanu
thread, and the exchange channel is the transverse (linking) direction.

- [x] Lean: `QOU/Mass/TorusKnotPages.lean` — Seifert form of T(2,n) unimodular for
  every odd n (upper-triangular det = (−1)^(n−1)); the curvature floor as
  bookkeeping (b ≥ μ + #knotted, μ = A+1, #knotted = A ⇒ 2A+1 ≤ b ≤ 3A); the
  pages T(2,3/5/7) embed on Bring's surface at the corpus's forced g = 4 via its
  own `Embeds` (`decide`), T(2,9) the last; Bennequin χ = −5, genus 3 for both
  sub-braid shapes. Sorry-free, standard axioms only. NOT formalised: Milnor's
  theorem, the torus-knot identification, the Alexander polynomial and
  monodromy order (checked exactly at n = 3,5,7 by the probe), fibered-knot
  page uniqueness.
- [x] audit `docs/audits/2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md`:
  link of the Bring cone = UT(Σ₄) canonically (Bézout + adjunction), ~SL₂
  geometry ⇒ no 3-Sasakian structure ⇒ the compact su(2) Reeb triad of
  `BringCone.lean` cannot be that of a 3-Sasakian structure on this link; the
  split sl₂(ℝ) frame {X,Y,V} is what the manifold carries, and it is the same
  frame on every component complement. Posed as a question to the lemma's owner.
- [x] **SHARP, and symbolically.** `the_canonical_closure_is_a_chain_of_torus_links_probe`
  (5/5): after resolving the averaged letters and freely reducing, the canonical
  word is a CHAIN FORM ∏ σ_{3k}^{a_k} σ_{3k+1}^{b_k} σ_{3k+2}^{ε_k} for A = 2..12
  on both branches — a_k = 7 (σ branch) or 5/3 (σ⁻¹, p/n), b_k = −2 (p) / −4 (n)
  on σ and −4 throughout on σ⁻¹, ε_k = ±1 by interface type. A chain-form
  closed braid is a linear connected sum of the T(2,e_i); the ε = ±1 bands are
  connected sums with the unknot and drop out, leaving the (2A+1)-strand chain
  W'_A with the same closure (Jones + components verified at A ≤ 4). Hence
  μ = A+1, #knotted = A, b(L) = 2A+1 and inf ∫κ = 2π(2A+1) for EVERY A.
  `the_curvature_floor_is_sharp_probe` (spherogram + Vogel, independent Jones
  cross-check) is the computational instance at A = 2,3,4,6. The two
  topological facts (composite closed braids; T(2,±1) removable) are cited,
  not re-proved; Lean carries the exponent bookkeeping only.
- [x] **Real-form question answered (owner: "see if that conciliation works").** It
  works only as the split form. The tetraplectic definition supplies a volume
  form, not a contact triad; UT(Σ₄) is Sasakian with one Reeb field and, being
  aspherical, admits no SU(2)-action, so an su(2) Reeb triad cannot exist on
  it; the triad it carries (connection, Liouville, rotated Liouville; Reeb
  fields V, X, X⊥) is sl₂(ℝ). `lean/QOU/BringConeSplit.lean`: the lemma's
  construction on split quaternions gives (2, −2, 2) — one sign flipped —
  and `split_ne_compact`. Audit addendum + second author note on the lemma
  block. The su(2) survives as the resolvent bundle's structure group only.

## Summary of Changes

Queued from the serpenoid image; delivered, all pushed:

- `total_curvature_is_the_computable_half_probe` — every multi-strand
  component of the canonical closure is a (2,odd)-torus knot on both
  classical branches; floor 2π(2A+1); Bennequin pages; Seifert forms; the
  osculating pencil made explicit and its invariant shadows (open book, Seifert
  circle fibration) named. Crofton: total curvature = π × mean critical-point
  count of the height functions — the exact form of "the oscillations happen
  at the saddle points".
- `the_curvature_floor_is_sharp_probe` (spherogram + Vogel, independent Jones
  cross-check, A = 2,3,4,6) and `the_canonical_closure_is_a_chain_of_torus_links_probe`
  (symbolic: the word is a chain form ∏ σ_{3k}^{a_k} σ_{3k+1}^{b_k} σ_{3k+2}^{±1},
  interfaces are connected-sum bands with the unknot, W'_A on 2A+1 strands
  has the same closure) — b(L) = 2A+1 and inf ∫κ = 2π(2A+1) for EVERY A.
- Lean `QOU.Mass.TorusKnotPages` (Seifert unimodularity, continuant closed
  form, divisibility, curvature-floor bookkeeping, pages embed on Bring,
  Bennequin arithmetic) and `QOU.BringConeSplit` (the lemma's construction on
  split quaternions: (2, −2, 2), `split_ne_compact`).
- Exposition: `prop:canonical-closure-torus-chain`, `rem:torus-chain-pages-on-bring`;
  author notes on `lem:bring-cone-reeb-quaternionic-twist`; forward pointer on
  `atom_closure_milnor_indeterminacy_probe`.
- Audits: the Bring cone link is UT(Σ₄) and its Reeb triad is sl₂(ℝ) (the
  "degenerate" conciliation works only as the split form); the colour cubic
  is a rank-3 spectral curve (Chevalley/Hitchin reading of the eightfold-way
  gaps — shape given, nothing closed).

Not claimed anywhere: a connection from curvature to binding, or the twist.
Left for others: whether the lemma's author amends its statement; the
sheet-sign ↔ twist-torsor identification on the colour side.

## Continuation (owner 2026-09-03: "work qou-m3sh — the Fáry–Milnor")

Reopened. Two items the closed summary had left implicit:

- [x] **The chain form's algebraic consequence — DONE, and it is a theorem
  about the binding gap.** `the_canonical_mass_trace_factorises_over_the_chain_probe`
  (4/4): the full H_{3A} Markov trace of the canonical word equals the product
  over generators of TWO-strand traces of the per-generator Hecke polynomials
  to 2.3e-59 (²H), 3.1e-59 (³H, ³He), 4.0e-59 (⁴He); Jones factorises over
  the chain exactly on both branches, A ≤ 4. Interface factor = z + d, so
  L_pp = −log z, L_nn = −log(z − h), L_pn = −log(z + d_pn) reproduce the arc's
  200-bit H_6 bond constants to ALL 60 digits. Consequence: connected sum ⟹
  multiplicative trace ⟹ additive L, so the canonical closure carries NO
  many-body binding by theorem; the arc's cumulants (c₃<0, c₄<0, c₅>0, c₆)
  belong to the all-pairs bond model, which is not a chain. The 62 % ⁴He is
  short is absent from the canonical closure because a composite link has
  nowhere to put it: a closure carrying many-body binding must be prime.
  Lean `QOU.Mass.ChainTraceFactor` (sorry-free): affine law from the Wenzl
  weights; z − h = 1/(q(q²+1)); tr₂(σ)tr₂(σ⁻¹) = 1/[2]²; L_pp + L_nn =
  2 log(q + 1/q); positivity for q ≥ 1; −log ∏ = Σ −log. The H_{3A}
  factorisation itself is checked, not formalised. ⁶Li not run (same engine,
  longer; not in the CI budget — the identity is a theorem given the chain
  form, verified through A = 12).
- [x] **The torsion half — measured, and it closes harder than expected.**
  `the_torsion_half_is_not_an_invariant_probe` (22/22): torus embeddings of
  T(2,3/5/7), r ∈ {0.45 … 0.02}, mpmath 24 dps. ∫κ/4π decreases monotonically
  to 1.0003 / 1.003 / 1.014 (floor approached, never attained); ∮τ ds and Wr
  both move with r; Wr + Tw_F is an integer at every r (worst residual ~4e-8)
  — BUT NOT THE SAME INTEGER: Lk_F = −2q on the fat side and −q on the thin
  side of r* = 4/(q²+4) (4/13, 4/29, 4/53). Exact: at t = π/q,
  γ'×γ'' = (q²r − 4(1−r))·(qrs, −qrc, −2(1−r)), so the family crosses q
  inflections at once and the Frenet self-linking jumps by q. Even the
  integer half of Călugăreanu is a property of the curve, not the knot type:
  no framing datum, fractional or integral, comes from the isotopy class.
  Lean `QOU.Mass.TorusInflection` (sorry-free): the cross-product
  factorisation, κ(π/q) = 0 ⟺ r = 4/(q²+4), the three values, cos(qt) = −1
  at the q distinct (2k+1)π/q. Numerics lesson recorded in the probe: the
  Gauss integrand's complex singularity near the diagonal sits at
  |u| ≈ 2/(rq²), and a rule refined only toward the second strand left
  Wr + Tw_F short of −14 by 4e-4 at (7, 0.45) while looking converged; the
  push-off linking integral (−14.000000007) caught it.
- [x] Exposition: new section `sec:canonical-closure-as-link` in mass-theory
  listing the five blocks this thread and `qou-wx83` produced (they had been
  unlisted): `prop:subset-cumulant-recursion`, `prop:canonical-closure-torus-chain`,
  `rem:canonical-trace-factorises-over-chain` (new), `rem:torus-chain-pages-on-bring`,
  `rem:frenet-framing-is-not-an-invariant` (new). Validation clean.

**Where this leaves the thread.** Fáry–Milnor delivered the curvature half
exactly (2π(2A+1), sharp, symbolic, Lean-backed) and then showed the other
half cannot be a knot-type invariant at all — and, separately, that the
canonical closure's trace is a product, so the many-body binding the arc
measures is not in this closure by theorem. The open question is no longer
"which invariant carries the twist" but "which PRIME closure carries the
cumulants": the next bean should ask what non-composite closure the
all-pairs bond model's band routing actually produces (it is not a chain;
is it prime? Borromean-type?), because that is where c₃…c₆ live.
