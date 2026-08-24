---
# qou-oilr
title: Benard's adjoint-torsion LES of the pair (M,dM) is a dim-H1 machine — and Reidemeister torsion is genuinely ABSENT from the corpus
status: todo
type: task
priority: normal
created_at: 2026-08-24T17:34:25Z
updated_at: 2026-08-24T17:58:24Z
---

## The source

`library/2018sorus020/` — Léo Bénard, *Reidemeister torsion on character
varieties* (HAL tel-02108892, 110 pp, 78 sections). **Ingested and UNCITED.** It
is rank **3** in `docs/audits/2026-08-15-library-uncited-triage.md` (score 521.1,
92 extracted candidates) — the highest-scoring uncited source in the library.

Sections that carry the machinery:

- §1.2 Twisted cohomology (`sec-018`) — H^k(M,A) for a Z[Gamma]-module A
- §2.1 The twisted complex with adjoint action (`sec-036`)
- §2.1.2 Computation of the twisted cohomology (`sec-038`)
- §1.5 Reidemeister torsion, three definitions (`sec-033`..`sec-035`)
- §1.4 Alexander module and character varieties (`sec-029`..`sec-031`);
  `sec-031` is specifically the **figure-eight** component of irreducible chars

Verified present, not inferred from titles: the text carries "long exact sequence
of the pair (M, dM)" and "long exact sequence in cohomology : 0 -> H^0(Cone(phi))
-> H^1(M, Ad.rho)_v".

## The check that mattered — a symbol collision I nearly walked into

The corpus has a `QOU.Torsion.*` namespace, which makes "the corpus already has
torsion machinery" look obvious. **It is a different word.** `QOU/Torsion/`
contains BraneTower, Descent, GlobalGluing, MassIdentity, YekutieliTriple — the
gerbe / twisted-2-cocycle sense. And every corpus hit for "Reidemeister" is a
Reidemeister **MOVE** (R1/R2/R3), not Reidemeister **torsion**: `grep -rn
Reidemeister content/ computations/ docs/` outside `library/` returns moves,
`reidemeister-action-table`, `conj:reidemeister-mass-invariance` — zero torsion.

So Reidemeister torsion is genuinely absent from this corpus. That is the honest
version of the finding, and it is a cleaner one than the identification would
have been. (AGENTS.md: attributes do not transfer across overloaded symbols.)

## Why H^1(M, Ad.rho) is the interesting shape

The canonical chain rests on `H^1(Bring) = 2W` carrying exactly 3 real DOF, and
`calibration-cohomology-alignment` (`QOU.Mass.calibrations_eq_cohomology`) is
explicitly a **count/alignment** claim: 3 calibrations = 3 H^1 DOF. It counts;
it does not derive.

Bénard's LES of the pair (M, dM) with adjoint coefficients is a machine for
computing exactly that kind of number — dim H^1 with Ad.rho coefficients on a
knot complement — from the boundary torus data.

**NOT an identification.** H^1(Bring) (Bring's surface) and H^1(M, Ad.rho) (a
knot complement) are different spaces and I am not claiming they are the same
object, or that either dimension count transfers. What is claimed: the corpus's
central count has the same SHAPE as a quantity this thesis computes, and the
corpus currently has no derivation of it. Whether the shapes connect is the
open question, and answering "no" would be a real result too.

## The adjacent rung it may actually serve first

`qou-m3ad` (in-progress, high) reframed Route C's M3 from "build a CoHA" to
"derive the index set Omega", and landed `QOU/QBeta/AdjointIndexSetM3.lean`
sorry-free with **H_Ad, the sl_2 adjoint, as the knot-independent core**. That
is the same `Ad` representation Bénard's §2.1 computes cohomology of, for knot
complements including 4_1 — one of the two certified-DT knots (`qou-rtec`).

Coordinate with `qou-m3ad` before touching this; per AGENTS.md an open-outcome
research overlap is permitted but must declare its distinct angle.

Also worth noting from the same triage table: rank 4 is
`arxiv-1601.02479v5` *Cohomological Donaldson-Thomas theory of a quiver with
potential*, and rank 7 `arxiv-1511.00400v2` *Reidemeister torsion, hyperbolic
three-manifolds, and character varieties* — both uncited. `qou-rtec`'s D1 rung
is literally "construct the (Q,W)". The three top-ranked uncited sources are
the three things the open arcs need; that is worth someone's attention
independent of this bean.


## 2026-08-24 — the meeting point with qou-m3ad, and why it may be nothing

Located the actual statement rather than inferring it from section titles.
`library/2018sorus020/sections/sec-038-212-computation-of-the-twisted-cohomology.md`,
**Proposition 2.1.5**, quoted from the text:

> Let rho : pi_1(M) -> SL_2(k(X-bar)) be the tautological representation, then
> H^0(M, Ad.rho) = H^i(M, Ad.rho) = 0 for i >= 3; H^1(M, Ad.rho) is one
> dimensional and H^2(M, Ad.rho) ~= k(X-bar), via eta |-> Tr((r_* eta) H).

HYPOTHESES (these are the load-bearing part, do not drop them): X-bar is a
**one-dimensional** component of X-bar(M) of **irreducible type**; rho is the
**tautological** representation over the function field k(X-bar) — not a single
SL_2(C) representation. Proof route: dim Omega_{k(X-bar)}/k = dim X-bar plus
Universal Coefficients gives dim H^1 = 1; chi(M) = 0 then gives dim H^2 = 1; the
explicit H^2 isomorphism comes from the **long exact sequence of the pair
(M, dM)**.

### Why this is worth handing to qou-m3ad

m3ad's own text gives its mechanism as: *"in complex Chern-Simons the Borel
singularities are differences of complex volumes of flat connections, and the
deformation theory of a flat connection is governed by H^1(M, Ad rho) — the
adjoint local system is the CANONICAL coefficient object, not a chosen one."*
That is an assertion of what governs the deformation theory. Prop 2.1.5 is a
**computation of the same object**, with hypotheses, for exactly this class of
manifolds.

And the numbers line up in a way that is either the point or a trap:

    m3ad, Lean-proved:  any knot-independent core forces a knot-DEPENDENT
                        remainder differing by exactly 1
                        (knot_independent_core_forces_unit_remainder)
    m3ad, under H_Ad:   the remainder is pinned to (0, 1)
                        (adjoint_core_pins_remainder)
    Benard 2.1.5:       (dim H^0, dim H^1) = (0, 1)

### THE TRAP, stated before the resonance

**These are not obviously the same (0,1).** m3ad's is a *remainder in a DT-count
decomposition*; Benard's is a *cohomology dimension vector*. Two unrelated
objects can both be (0,1). This is exactly the class of error the corpus keeps
paying for — the same session that opened this bean nearly identified
Benard's Reidemeister torsion with `QOU.Torsion.*`, which is the gerbe sense and
has nothing to do with it. **Do not write this identification into any durable
artifact until someone checks the arity.**

### The first thing to check, and it is a HYPOTHESIS question not a numbers one

Does m3ad's setting instantiate Prop 2.1.5's hypotheses? Specifically: is m3ad
working over a one-dimensional irreducible-type component with the tautological
representation, or with individual SL_2(C) representations at certified knots
(4_1, 5_2)? If the latter, 2.1.5 does not apply as stated and the (0,1) match is
about two different situations. That question is answerable by reading m3ad's
setup, costs one session, and settles whether there is anything here at all.

### Distinct angle, for the coordination record

m3ad attacks the index set through the **adjoint weight set** (representation
theory of sl_2: eigenvalues (x,1,1/x), chi_Ad(1) = 3). This route attacks the
**cohomology dimension** of the same adjoint local system (3-manifold topology,
via the LES of the pair). Same coefficient object, different machinery, and they
meet — if they meet — at the remainder 1. Per AGENTS.md an open-outcome overlap
is permitted provided the angle is declared; this is the declaration.
