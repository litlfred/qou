---
# qou-47nf
title: 'TRANCHE: the non-geometric Ptolemy component at n=3 — route E''s one surviving branch'
status: todo
type: task
priority: high
created_at: 2026-09-05T07:09:45Z
updated_at: 2026-09-05T07:42:48Z
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


## 🛑 STEP 1 DONE 2026-09-05 — and it corrects THIS BEAN twice, plus a near-miss of mine

Step 1 was "read the papers, confirm the Groebner feasibility claim actually
says what ptlm reports". Done. Three findings, two of which weaken what this
bean asserted above.

### (i) MY OWN NEAR-MISS — a zero-hit grep I nearly reported as a finding

I grepped both held Ptolemy papers for "Groebner|Gr.bner" and got ZERO hits, in
sections AND ocr, and was about to report that the claim is unverifiable from
the held text. FALSE. The extractor renders the umlaut as `Gr¨ obner` —
diacritic split off with a SPACE INSERTED — so no naive pattern matches.

Bean ptlm records hitting this EXACT trap and being "one step from recording
'the citation is misattributed'". I read the first 45 lines of ptlm, acted, and
walked into the same wall it had already documented forty lines further down.

RULE, restated because I proved it needs restating: a zero-hit grep over
PDF-extracted text is NOT evidence of absence. Search a diacritic-free
substring ("bner", "impractical") before concluding a source is silent.

### (ii) THE CLAIM IS REAL — verbatim, 1207.6711 section 1.3

  "For the Ptolemy varieties exact computations are possible for n = 2 even when
   there are many simplices, and there are often several components of
   representations besides the geometric one. We should point out that while
   Groebner basis computations are feasible for the Ptolemy varieties even for
   many simplices, they are usually impractical for the gluing equations even
   when the cusp equations are added. However, the monomial map mu can be used
   to obtain shapes from Ptolemy coordinates."

"often several components of representations BESIDES THE GEOMETRIC ONE" is the
full sentence; the truncated form quoted higher in this bean lost the operative
clause.

### (iii) 🛑 THE FEASIBILITY IS STATED FOR n = 2. THIS TRANCHE NEEDS n = 3.

Read it again: "exact computations are possible for **n = 2**". The paper does
NOT claim n = 3 is feasible. Higher in this bean I wrote that the computation
"is not a research programme; it is a Groebner basis over Q on a variety
designed to be computable" — that is the n = 2 statement applied to an n = 3
task, and it is the same ambient-vs-instance slip this whole arc keeps
correcting, committed by me while writing the bean that corrects it.

### (iv) 🛑 AND IT IS NOT RUNNABLE IN THIS CONTAINER — ptlm MEASURED THIS

Both papers use MAGMA for the primary decomposition (1207.6711 section 14;
1507.03238's Algorithm Step 3 is "compute the primary decomposition of the
reduced Ptolemy variety"). ptlm tested the tooling directly on 2026-08-10:

  snappy.Manifold("4_1").ptolemy_variety(2, obstruction_class=0)   builds fine
  .retrieve_solutions()  -> RuntimeError, 403 Forbidden: the precomputed
                            database at ptolemy.unhyperbolic.org is
                            NETWORK-BLOCKED by the agent proxy
  .compute_solutions()   -> ValueError: could not find the Magma executable

So the blocker is not compute time; it is two missing capabilities, both
already measured. This bean as first written did not carry that, and would have
sent the next agent to rediscover it.

### WHAT THIS TRANCHE ACTUALLY NEEDS NOW

  1. A primary-decomposition backend that is neither Magma nor the blocked
     database. Candidates, in order of plausibility: Singular via Sage (is Sage
     present? ptlm notes find_field already needs it and Route 75 hand-rolled
     around that), sympy.groebner (available, but n = 3 Borromean may not
     terminate), or an exact linear-algebra route that avoids full primary
     decomposition altogether.
  2. Confirmation that n = 3 is tractable AT ALL for a 8-tetrahedron
     complement — the paper's feasibility sentence does not cover it.
  3. Only then the character-reality read.

Step (1) is the real gate and it is an INFRASTRUCTURE question, not a
mathematical one. Until it is answered this tranche cannot start, and saying so
is the honest state rather than opening a computation that will fail the same
way ptlm's did.


## 🟢 THE INFRASTRUCTURE BLOCKER IS CLEARED 2026-09-05 — and it was cheap

Step (1) of the three above ("a primary-decomposition backend that is neither
Magma nor the blocked database") is ANSWERED. What ptlm measured as blocking on
2026-08-10 was two missing capabilities; both are now present.

  BEFORE (measured this session, before any install)
    sage / Singular / magma / gp / maxima   ALL absent
    sage, pysingular, galois, flint         ALL absent as python modules
    snappy                                  absent
    sympy 1.14.0                            the only algebra backend

  AFTER
    Singular 4.3.2   sudo apt-get install -y --no-install-recommends singular
                     43 MB. primdecGTZ VERIFIED working on a test ideal:
                     split x*(y-1), x*z into components (x) and (z, y-1).
    snappy 3.3.2     python3 -m pip install snappy
                     Vol(4_1) = 2.0298832128 — matches the corpus's canonical
                     2*Cl_2(pi/3) exactly, so the install is sane.

BOTH INSTALLERS WERE ALREADY IN folio-assistant AND NOBODY HAD RUN THEM:
scripts/setup-singular.sh and scripts/setup-sage.sh (plus scripts/sage-mcp.sh).
The provisioning existed the whole time. ptlm recorded the blocker correctly and
did not check whether the sibling repo shipped a fix for it.

SINGULAR, NOT SAGE, DELIBERATELY. setup-sage.sh's real path is a ~2 GB Docker
image (native Sage needs Python <= 3.12; this container is 3.11 so native might
work, but the script defaults to Docker). Free disk was 659 MB at decision time
and 154 MB after the snappy install alone — a 2 GB pull would have wedged the
container, which had ALREADY happened once this session at 120K free. Singular
is the direct backend for the one operation needed and cost 43 MB.

DISK IS THE REAL CONSTRAINT ON THIS TRANCHE, not compute. snappy took free from
582 MB to 154 MB. Reclaim before any large run: rm -rf /root/.cache/pip
~/.cache/pip recovered it to 266 MB.

## THE VARIETY BUILDS AT n = 3 — the n=2/n=3 gap above is narrower than feared

  snappy.Manifold('L6a4')            Borromean rings, 8 tets, 3 cusps,
                                     vol 7.32772475342
  .ptolemy_variety(2, obstruction_class=0)   11 eqns, 8 vars   (instant)
  .ptolemy_variety(3, obstruction_class=0)   38 eqns, 32 vars  (instant)

So CONSTRUCTION at n = 3 is free. The paper's "n = 2" feasibility sentence is
about the exact SOLVING, not the building, and the distinction matters: the open
question is now specifically whether primdecGTZ terminates on 38 quadrics in 32
unknowns, which is being measured now rather than assumed either way.

The equations are clean Ptolemy relations, e.g.
  - c_0012_0*c_1011_0 + c_0012_0*c_1101_0 + c_0111_0*c_1002_0

NOT YET IMPOSED, and it must be before any component is called a
representation: the Ptolemy variety requires all c != 0, and snappy's own
convention adds a normalisation. The raw ideal is what was handed to Singular;
saturation by the coordinate product is a further step and its absence means a
component found now could be a degenerate locus rather than a representation.
