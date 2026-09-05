---
# qou-47nf
title: 'TRANCHE: the non-geometric Ptolemy component at n=3 — route E''s one surviving branch'
status: todo
type: task
priority: high
created_at: 2026-09-05T07:09:45Z
updated_at: 2026-09-05T07:11:44Z
---

OPENED 2026-09-05. Route E's ONE surviving branch, now a named held construction
rather than a direction. Parent epic qou-2q85; follows qou-g1m8 and PR #6743.

## WHY THIS IS THE ONLY THING LEFT

PR #6743 closed route E's geometric side completely:
  SymSquareHolonomyIsRealType   every Sym^2-induced rep is self-dual, hence
                                real/quaternionic, hence excluded — a property
                                of the map SL(2)->SL(3), so it prunes every knot
  AmphichiralHolonomyIsSelfDual conjugate holonomy is the mirror's holonomy, so
                                an amphichiral knot's holonomy is self-dual
  MirrorSwapCompatibility       resolves the Borromean tension AGAINST the route:
                                mu-bar(123) is negated by BOTH mirroring and a
                                component transposition, so mirror-after-swap
                                preserves it — which is how the Borromean rings
                                are amphichiral while the ordered invariant still
                                separates them from the bare mirror

So 4_1 (amphichiral), 3_1 (torus knot, no hyperbolic holonomy) and B_3 (via
Mostow) are all pruned FOR GEOMETRIC HOLONOMIES. What survives is a genuinely
non-geometric PGL(3,C) rep.

## THE OBLIGATION, precisely

Take a NON-GEOMETRIC Ptolemy component at n = 3 for the Borromean complement and
read off whether its character is real-valued. A representation is self-dual iff
its character is real, so a SINGLE group element with non-real trace settles
complex type — and unlike the geometric component, nothing forces it real.

If some component is complex type: route E delivers what the Sym^2 gate demands
and the eightfold's N=3 problem has a candidate for the first time.
If every component is real/quaternionic: route E closes, and epic qou-2q85 has
no surviving route at all.

## HELD SOURCES — and my count was an UNDERCOUNT

  arxiv-1207.6711v1  Garoufalidis-GOERNER-Zickert, "Gluing equations for
                     PGL(n,C)-representations of 3-manifolds". Says it directly:
                     "there are often several components of representations".
  arxiv-1507.03238v3 "Triangulation independent Ptolemy varieties" — a SECOND
                     on-point source I MISSED in my own searches. Found via bean
                     ptlm.

TWO CORRECTIONS TO MY OWN WORK, both from bean ptlm (completed 2026-08-10):
  1. I wrote Garoufalidis-THURSTON-Zickert throughout the route-E audits, PR
     #6743 and its comments. WRONG. 1207.6711 is Garoufalidis-GOERNER-Zickert.
     Garoufalidis-Thurston-Zickert is a DIFFERENT paper ("The complex volume of
     SL(n,C)-representations of 3-manifolds"). Corrected in both audits and in
     SymSquareHolonomyIsRealType.lean.
  2. I called 1207.6711 "the ONE substantive held source" for the rank-2 route.
     There are at least two.

## AND THE ROUTE IS TRACTABLE — which I did not know

Bean ptlm records the decisive practical fact: Groebner bases ARE feasible for
PTOLEMY varieties "even for many simplices", while being impractical for the
gluing equations, and a MONOMIAL MAP recovers the shapes from Ptolemy
coordinates. So the computation above is not a research programme; it is a
Groebner basis over Q on a variety the literature says is designed to be
computable. That is why this tranche is worth opening now rather than deferring.

## SECOND ACCESS ROUTE, independent: resurgence

Twelve library dirs on alien calculus / trans-series / Stokes constants.
arxiv-2007.10190v2 ("The Resurgent Structure of Quantum Knot Invariants")
indexes trans-series sectors by critical points — "the geometric representation,
its conjugate and the real" — so a non-geometric rep is reachable as ANOTHER
SADDLE of the same asymptotic series. The corpus is already partway onto this
ground: kashaev-surreal.md cites Ecalle; mass-theory/stokes-dt-bps-bridge.md and
dt-spectrum-bar-eigenspace.md are live blocks.

CAUTION carried forward: that paper treats the geometric rep and its conjugate
as DIFFERENT critical points. Correct for a general hyperbolic knot, and NOT a
contradiction with the Mostow argument, which binds only amphichiral manifolds.

## STEPS

  1. Read 1207.6711 sec on components + 1507.03238. Confirm the Groebner
     feasibility claim is actually in the paper and says what ptlm reports.
  2. Build the Ptolemy variety for the Borromean complement at n = 3.
  3. Decompose into components; identify the non-geometric ones.
  4. For each, compute the character on a few group elements EXACTLY (Q or a
     number field — NO FLOAT64, this is a producer). One non-real trace ends it.
  5. Report: complex type found (route E lives) or not (route E closes).

VOCABULARY NOTE, the fourth instance this arc: "non-geometric solution / flat
connection / component" returns ZERO library hits; "Ptolemy" /
"boundary-unipotent" / "component of the character variety" return EIGHT. And
bean ptlm — which had the answer, the second source AND the tractability fact —
was found only by the .beans/ grep (checklist path 6), not by any content or
library search.
