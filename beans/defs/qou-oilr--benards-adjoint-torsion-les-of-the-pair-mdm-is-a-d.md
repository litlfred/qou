---
# qou-oilr
title: Benard's adjoint-torsion LES of the pair (M,dM) is a dim-H1 machine — and Reidemeister torsion is genuinely ABSENT from the corpus
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T17:34:25Z
updated_at: 2026-11-18T11:12:15Z
parent: 08a2
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
`library/2018sorus020/sections/sec-029-212-computation-of-the-twisted-cohomology.md`,
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


## 2026-08-24 — the (0,1) match is REFUTED. Different index sets, and m3ad's already has a derived source.

I flagged this as possibly-coincidental before building on it. It is coincidental.
Recording the refutation with the same weight the speculation got.

### The arity check, which is the whole answer

`QOU/QBeta/AdjointIndexSetM3.lean`:

    theorem adjoint_core_pins_remainder
        (extra : KKnot -> Int)
        (h41 : sAtOne + extra fourOne = 3)
        (h52 : sAtOne + extra fiveTwo = 4) :
        extra fourOne = 0 /\ extra fiveTwo = 1

`extra : KKnot -> Int`. The `(0, 1)` is `(extra 4_1, extra 5_2)` — **indexed by
KNOT**, a 2-vector over `{4_1, 5_2}`.

Benard Prop 2.1.5's `(0, 1)` is `(dim H^0(M, Ad.rho), dim H^1(M, Ad.rho))` —
**indexed by COHOMOLOGICAL DEGREE**, for a single fixed M.

Two 2-vectors over completely different index sets, agreeing because both happen
to be `(0,1)`. This is the `da-arity-conflation` class in
`local/devils-advocate-watcher`, and it is exactly what the AGENTS.md
"grep the claim SHAPE, not only the topic" rule exists to catch: I had resolved
the topic (both are `H*(M, Ad rho)`-adjacent) and not the arity.

### Independently fatal: m3ad's (0,1) is ALREADY derived, and not cohomologically

Part 3 of the same file, `decide`-proved:

    theorem forced_remainder_is_the_real_embedding_count :
        floorRemainder PKnot.fourOne = realEmbeddings PKnot.fourOne /\ ...

with the docstring: *"4_1's remainder is 0 because its trace field is imaginary
quadratic (no real embedding); 5_2's is 1 because the discriminant -23 cubic has
exactly one."*

So the corpus already explains that `(0,1)` by the **real-embedding count of the
trace field** — number theory, derived, not assumed. A cohomological
re-explanation would have to displace a standing derivation, not fill a gap. It
does not.

### What survives, and it is smaller than I hoped

One real thing. m3ad's mechanism paragraph asserts, uncited:

> in complex Chern-Simons the Borel singularities are differences of complex
> volumes of flat connections, and the deformation theory of a flat connection is
> governed by H^1(M, Ad rho) — the adjoint local system is the CANONICAL
> coefficient object, not a chosen one.

Benard Prop 2.1.5 is a **citation for exactly that claim**, with hypotheses
(one-dimensional component of irreducible type, tautological rep over
`k(X-bar)`) and the LES of the pair `(M, dM)` as the proof route, and it computes
`dim H^1(M, Ad.rho) = 1` — the one-dimensionality that makes "the deformation
theory" a well-posed singular object rather than a family.

That is a citation upgrade for an uncited mechanism sentence. It is NOT a
numerical input to the index-set derivation, and nothing downstream should treat
it as one.

### Hypothesis question, answered as far as it goes

Does m3ad's setting satisfy 2.1.5's hypotheses? Partially, and it does not
matter given the above. m3ad works in `x = m^2` with `m` the meridian
eigenvalue treated as a variable, which is the right *register* for a
function-field statement rather than a numeric SL_2(C) evaluation. But since the
quantities being compared are not the same kind of object, matching the
hypotheses would not rescue the match.

### Instruction to a later agent

Do not re-open this as "the (0,1)s might line up after all". They are a
knot-indexed vector and a degree-indexed vector. If you want Benard here, use it
as the citation for the deformation-theory sentence, and cite Prop 2.1.5 WITH its
hypotheses.


Citation key is ready: `benard2018` in `content/schema/references.ts` (docId
`2018sorus020`). No references.ts work needed — \cite{benard2018} plus "Prop 2.1.5"
and its hypotheses is the whole edit, in whichever file carries the mechanism
sentence. NOT done here: `qou-m3ad` is in-progress and owned by a sibling, and a
citation is not worth stepping on a live claim for.

- Round 82 (`lane-e667`): Formalized `qou-71ma`, `qou-n226`, `qou-oilr`, `qou-omuz`, `qou-wxmm` in `QOU.Foundations.ValuationGradeSelectionUpperHalfPlaneNonDegeneracyTwistedPairCohomologyDimensionLaurentRingUnitDivisionLinearDualityCertificate` with 80-dps `mpmath` 2-commit witness stamp (`84401456f07c58b1279d96f566c292313ce4c028` -> `0c9aa2b99fc76a7fc726e889fc36119e8f63d65c`, `scriptHash=f07174204f482f7a01972e149c17324ec39a978434a088c3f7d45077e7857c97`) in PR `litlfred/qou#8441` (`status: in-progress`).
