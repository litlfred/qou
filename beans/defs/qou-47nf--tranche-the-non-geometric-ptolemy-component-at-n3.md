---
# qou-47nf
title: 'TRANCHE: the non-geometric Ptolemy component at n=3 — route E''s one surviving branch'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T07:09:45Z
updated_at: 2026-10-12T20:57:57Z
parent: qou-v2om
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


## 🛑 TWO RETRACTIONS AND A HARD WALL 2026-09-05

### (v) RETRACTED — the "resurgence second access route" is SL(2), not PGL(3)

Higher in this bean I recorded resurgence as a SECOND ACCESS ROUTE to a
non-geometric PGL(3,C) representation, citing arxiv-2007.10190v2 as indexing
trans-series sectors by "the geometric representation, its conjugate and the
real". Both intersection papers are now READ and that reading is WRONG.

Garoufalidis-Gu-Marino, arxiv-2007.10190v2 and arxiv-2012.00062v3, are SL(2,C)
Chern-Simons throughout. Their own labelling, verbatim:

  "The labeling set P = {sigma_1, sigma_2}, where sigma_1 corresponds to the
   geometric representation of the 4_1 and sigma_2 to the complex conjugate of
   the geometric representation."

Two saddles for 4_1, three for 5_2. "Non-geometric" THERE means the trivial or
conjugate SL(2) connection — a DIFFERENT OBJECT from a non-geometric PGL(3)
component. So the resurgence route does not reach n = 3 at all.

THE TRAP THAT CAUSED IT, worth recording because a grep walks straight into it:
both papers contain SL(3, Z[q,1/q]) and PSL(3, Z[q,x]) — and that is the SIZE OF
THE STOKES MATRIX, not the gauge group. 4_1's q-holonomic module has RANK 2 and
three flat connections, so the Stokes data is 3x3. Likewise "I_41 has rank 2" is
the module's rank. A grep for "SL(3" finds these papers and means something else.

What IS real and worth keeping: the singularity positions are "dictated by the
values of the complex Chern-Simons function on the set of flat connections", so
Borel singularities ARE indexed by character-variety components — the structural
idea is sound, at SL(2). For 4_1 the real-axis singularities sit at
iota_pm = pm V/pi with V = Vol(4_1) = 2.02988, and the Stokes matrices M_R(q)
have integer-coefficient q-series entries conjecturally solving a linear
q-difference equation.

### (vi) B_3 AT n = 3 IS OUT OF REACH BY DIRECT GROEBNER — two algorithms, one wall

  primdecGTZ, saturated, mod 32003   OOM-killed 11m15, exit 137
  minAssGTZ,  saturated, mod 32003   OOM-killed 11m11, exit 137
  primdecGTZ, raw, over Q            killed at my own 4m00 timeout
  primdecGTZ, raw, mod 32003         killed at my own 4m26 timeout

14 GB available (free -g: total 15, available 14). Switching from full primary
decomposition to minimal associated primes bought NOTHING — same wall, same
time — which localises the bottleneck to THE GROEBNER BASIS ITSELF, not the
decomposition on top of it. The finite field also bought nothing on the raw
ideal, so it is not coefficient arithmetic either. It is the geometry: 8
tetrahedra at n = 3 is 39 quadrics in 33 unknowns.

Do NOT simply re-run with a longer timeout. The budget was 2400 s and neither
run reached it; both died on memory at ~11 min.

### (vii) THE OWNER UPLOADED THE ANSWER — a346fb8cc6, 2026-09-05T08:15Z

Six PDFs to uploads/. Four bear directly on this tranche:

  1307.6697v2  Falbel, Koseleff, Rouillier, "Representations of fundamental
               groups of 3-manifolds into PGL(3,C): EXACT COMPUTATIONS IN LOW
               COMPLEXITY". Targets exactly this object and this obstruction.
               Rouillier is the Rational Univariate Representation author — a
               fundamentally different method from primdecGTZ, and it exists
               BECAUSE full primary decomposition does not scale. READ THIS
               BEFORE SPENDING MORE COMPUTE.
  1401.5542v1  GGZ, "The Ptolemy field of 3-manifold-representations" — the
               number field of a component, i.e. the Q(sqrt-3) vs Q(sqrt-7)
               split this tranche computed by hand on 4_1.
  1111.2828v2  Garoufalidis-THURSTON-Zickert, "The complex volume of
               SL(n,C)-representations". The paper I MIS-ATTRIBUTED GGZ's
               gluing-equations work to. Both are now held, so the distinction
               is checkable rather than a thing to remember.
  2104.07437v4 Gu-Marino, "Peacock patterns and new integer invariants in
               topological string theory".

  1207.6711v1 is a duplicate of a library copy; 2404.02087v1 (Sahai, "Extreme
  plasmons") is unrelated to this arc.

🛑 ALL SIX ARE IN uploads/, WHICH CORPUS-GREP PATH 5 CANNOT SEE — it searches
library/ only. Until migrate-uploads-to-library.py runs they are invisible to
every "has the corpus got this?" check. uploads/ currently holds 28 PDFs, a
backlog, and disk is at 169 MB, so a blind bulk ingest is not safe.


## 🟢 THE WALL HAS UNTRIED LEVERS — and one is a flag I left off (2026-09-05)

A corpus-grep of the tractability question (which I should have run BEFORE
spending four expensive runs) returns three things that change the next command.

### (viii) 🛑 I RAN ALL FOUR FAILED ATTEMPTS WITH THE TREE REDUCTION SWITCHED OFF

The owner's remembered "trees" are REAL and are a held theorem:
arxiv-1507.03238v3 section 9 (Triangulation independent Ptolemy varieties):

  "Let G be a connected graph in the one-skeleton of M-hat, which has
   fundamental group Z and contains all vertices. The reduced Ptolemy variety
   P(T)red is ISOMORPHIC to the subvariety of P(T) where the Ptolemy
   coordinates of all edges in G are 1."

Remark 9.2 gives its historical form verbatim: "a maximal TREE with 1- or
3-cycle". It is a gauge-fixing of the free diagonal torus action — EXACT, an
isomorphism, not an approximation.

SnapPy implements it as ptolemy_variety(..., eliminate_fixed_ptolemys=BOOL),
DEFAULT FALSE. Measured on L6a4 just now:

  eliminate_fixed_ptolemys=False   33 vars, 39 eqns   <- ALL FOUR FAILED RUNS
  eliminate_fixed_ptolemys=True    27 vars, 33 eqns   <- free

Six variables and six equations for nothing. The flag appears in ZERO files
corpus-wide (computations, docs, content, .beans, .claude) — not prior art, an
unused switch.

### (ix) 🛑 ROUTE 76 ALREADY EXISTS AND I DUPLICATED IT

  computations/probes/qbeta_route76_ptolemy_singular_probe.py     (356 lines)
  computations/probes/qbeta_route76_strategy_matrix_probe.py      (600 lines)
  computations/probes/qbeta_route76_modstd_reach_probe.py         (431 lines)
  + two witnesses, + beans qou-mfas and ptlm

A Ptolemy -> Singular lane, offline, no Magma, with a 6-strategy x 2-ideal-form
matrix of wall-clock timings. Its measured headline (qou-mfas):

  10_100, class 1, nz form, finduni           TIMEOUT  1,800,111 ms
  10_100, class 1, nz form, modStd_finduni    ok          42,040 ms

I ran four expensive attempts without running the corpus-grep checklist first,
because the work felt like compute rather than a claim. It is exactly what the
checklist is for.

### (x) THE DIAGNOSTIC I HAD NOT RUN, and what the lane already knows

  1. TIME std(I) ALONE. It localises the wall: GB vs decomposition. Route 76
     measured 10_100 (14 tets) std 87.6 s / decomposition >312 s => wall was
     DECOMPOSITION; 11a1 (17 tets) std TIMEOUT >3600 s => wall was the GB.
     "Any route past 11a1 has to make the GB itself cheaper — a different
     ordering, a different ideal presentation, or a different algorithm — not a
     better decomposition." RUNNING NOW on the reduced 27-var ideal.
  2. dp IS degrevlex in Singular. The obvious "try degrevlex" next-step is
     already the configuration that times out; lp is the real alternative.
  3. option(redSB) BEFORE finduni, or it errors "The ideal G has to be reduced",
     which reads as a mathematical obstruction rather than an unreduced basis.
  4. SINGULAR-SIDE SATURATION IS A MEASURED 10x PESSIMISATION vs SnapPy's own
     non-zero-condition variable (1,013,930 ms vs the nz form). I am already on
     the nz form; do not switch.
  5. modStd forks ~15 parallel jobs and subprocess.run(timeout=) ORPHANS them —
     13 orphans survived one timeout and competed with the NEXT measurement.
     "Timings taken by a harness with this bug are not trustworthy in any run
     that follows a timeout." MY FOUR RUNS WERE SEQUENTIAL. Use
     start_new_session=True + os.killpg.
  6. Singular auto-enables `short` when every ring variable is one character,
     printing x^14 as x14, which sympy/PARI parse as a LINEAR polynomial in two
     variables and return a confident wrong answer. Set short = 0.
  7. Untried and installed: mprimdec.lib (modular primary decomposition),
     grwalk.lib / rwalk.lib (Groebner walk), nfmodstd, ffmodstd, zeroset,
     presolve — each measured at ZERO files corpus-wide.

### (xi) TWO CORRECTIONS TO MY OWN NEGATIVE

  * 14 OBSTRUCTION CLASSES EXIST, not 2. I ran class 0 ONLY and never said so.
  * My four runs are SCOPE-(a): two algorithms, two ideal forms, ONE obstruction
    class, on the UNREDUCED 33-variable presentation, in this container. They
    are NOT evidence that L6a4 at n=3 is out of reach. Section (vi) above words
    it correctly ("out of reach by DIRECT Groebner"); I stated it more strongly
    than that in chat and am correcting it here.

### (xii) WHAT DOES NOT TRANSFER — flatly, so nobody spends a day on it

  * markov_peel.py is a TRACE RECURSION down the Hecke tower via
    tr_M^(n)(x sigma_{n-1}) = z tr_M^(n-1)(x). No ideal, no variety, no
    decomposition. It reduces the cost of evaluating one linear functional on
    one algebra element. There is NO analogue for a commutative polynomial
    ideal in 27 variables.
  * Groebner-SHIRSHOV / gb_nf_reducer.rs / .claude/skills/local/groebner-basis.md
    are NON-COMMUTATIVE rewriting systems on braid words (Singular letterplace,
    makeLetterplaceRing/twostd/lpMult). A GS basis for H_n(q) and a commutative
    GB for a Ptolemy ideal SHARE A NAME AND NOTHING ELSE.
  * "Vanishing ideals" maps to NO code here — 3 Mathlib files and one prose
    block. That part of the recollection has no implementation behind it.
  * Bratteli / branching_tower / BlockCache / LaurentQ are representation-theory
    caches for the Hecke tower. Different object.

### (xiii) THE INGEST GAP BITES THE MOST ON-POINT SOURCE

library/1307.6697v2 (Falbel-Koseleff-Rouillier), 1401.5542v1, 1111.2828v2 and
2104.07437v4 are BARE PDFs — no sections/, no ocr/, no structure.json, no
INDEX.md row. Corpus-grep path 5 is blind to all four tiers on the single most
relevant document. RUR (Rational Univariate Representation) is absent from the
corpus's greppable surface entirely: no msolve, no rur. Run
folio-assistant's scripts/pdf-structure.py on those four.


## 2026-09-05 later — FOUR ITEMS, and TWO MORE CORRECTIONS OF MINE

### (xiv) 🛑 4_1 HAS 2 OBSTRUCTION CLASSES, NOT 14 — I carried a count across manifolds

I wrote that there are "14 obstruction classes" and that my 4_1 result covered
class 0 only "of fourteen". The 14 is L6a4's (3 cusps). 4_1 has TWO. Measured:
ptolemy_variety(3, obstruction_class='all') returns len 2 for 4_1, 14 for L6a4.
The correction is mine and it came from applying a subagent's L6a4 measurement
to a different manifold without re-measuring.

### (xv) ALL of 4_1's classes now measured — and class 1 is ENTIRELY complex type

  class    solutions   self-dual   NOT self-dual
    0          6           4            2
    1          2           0            2
  total        8           4            4

Class 1 has NO self-dual representation at all. This STRENGTHENS section (iii):
the earlier finding was 2 complex-type solutions in one class; it is now 4 of 8
across both, with an entire obstruction class carrying none that are self-dual.

### (xvi) THE FOUR PDFs ARE NOW GREPPABLE — and the ingest had SPLIT them

migrate-uploads-to-library.py had created library/<bare-id>/ holding only the
PDF. pdf-structure.py derives the doc-id from the page-1 arXiv stamp and so
wrote to library/arxiv-<id>/ — a SECOND directory. Result: PDF in one, sections
in the other, neither complete.

Consolidated onto the arxiv- form, which is what the rest of library/ uses:
  arxiv-1307.6697v2    9 sections   28pp
  arxiv-1401.5542v1   19 sections   21pp
  arxiv-1111.2828v2   27 sections   44pp
  arxiv-2104.07437v4  19 sections   52pp

Verified path 5 reaches the target: grep "rational univariate" now hits
sections/sec-005-6-computational-steps.md, which was invisible an hour ago.

NOTE FOR THE NEXT INGEST: the two scripts disagree about doc-id. Run
pdf-structure.py FIRST (or expect to merge the pair by hand).

### (xvii) FKR section 7 — the reduction is on FLAG coordinates, not Ptolemy

The worked figure-eight example uses z_ij and w_ij, one pair per tetrahedron
edge, with edge equations (Le) and face equations (Lf) as MONOMIAL products
equal to 1:
  z23 w24 z13 w31 z14 w21 = 1        (edge)
  z21 z31 z41 w21 w31 w41 = 1        (face)

That monomial form is what makes their cross-ratio substitution work: at each
vertex the relations z_ik(1-z_ij) = 1 and z_il z_ij - z_ij + 1 let you pick ONE
variable per vertex and rewrite the rest, taking 12n -> 4n. Then affine
relations A z_ij + B with A | P_0^k let you substitute again, reaching 2
equations in 2 variables for 4_1.

⚠ THIS IS NOT DIRECTLY MY SYSTEM. Theirs is Falbel's decorated-FLAG coordinate
system; mine is SnapPy's Ptolemy coordinates. Related (both parametrise
boundary-unipotent PGL(3,C) reps) but NOT the same variables, and the
cross-ratio relations they eliminate with have no literal counterpart in the
Ptolemy generators I hold. Porting the pre-processing is a real piece of work,
not a translation. Their own degree warning applies: "Blind simplifications may
lead to consider systems of equations with very large degrees ... impossible to
solve with state of the art algorithms", and their degree-minimising choice
functions are deliberately not described.

### (xviii) modStd on the reduced ideal: SEGFAULTED, then the container filled

  modStd, 27-var reduced nz ideal, over Q, dp, setsid
    -> "Singular : signal 11 (v: 4330) ... Segment fault/Bus error occurred at 6
        because of 10246 ... trying to restart..." at ~34 min, 14 forked procs
    -> killed by me when the tmpfs hit 0 MB and the harness could not write

So modStd is NOT cleanly refuted here — it crashed and self-restarted rather
than returning a verdict, and I stopped it for disk rather than on its merits.
Record it as UNMEASURED, not as a failure.

DISK IS THE RECURRING HAZARD ON THIS TRANCHE, third occurrence today:
/tmp/lean-v4.24.0 (1.5G) + lean-v4.24.0-linux.zip (697M) are RE-CREATED by a
session-start hook after deletion. The live toolchain is /root/.elan; the /tmp
copy is redundant and safe to delete, but it comes back on the next session
start. Check `df` before launching any long Singular run.

### (xix) std(I) ALONE: 4m22, NOT ">15 min" — my own claim, withdrawn

I told the author std had run ">15 min without finishing" and inferred the wall
was the Groebner basis. The timer says 4m22.874s; I had read wall-clock
conversation time rather than the process's own. Four minutes is much weaker
evidence and does NOT localise the wall. The std diagnostic remains UNRUN to
completion, and Route 76's GB-vs-decomposition question is still open for L6a4.


## 2026-09-05 — L6a4 attack: coordinates changed, tooling changed, still open

### (xx) THE ANSWER IS PRECOMPUTED AND SITS BEHIND THE FIREWALL

snappy's retrieve_solutions() asks for exactly:
  https://ptolemy.unhyperbolic.org/data/pgl3/HTLinkExteriors/08_tetrahedra/L6a4__sl3_c<k>.magma_out.gz
for k = 0..13. Goerner's database HAS the Magma primary decomposition for all 14
obstruction classes of the Borromean rings at n=3 — i.e. the whole question this
tranche is grinding on is a solved, published computation.

Measured, not assumed:
  ptolemy.unhyperbolic.org/...L6a4__sl3_c0.magma_out.gz  -> 000 (blocked)
  pypi.org/simple/                                       -> 200, 45.7 MB

So this is an EGRESS restriction, not a dead host and not a missing dataset.
Allowlisting that one host would collapse this item from "days of Groebner" to
"seconds of download", for all 14 classes at once.

### (xxi) eliminate_fixed_ptolemys — the free reduction I had never switched on

  L6a4 c0, eliminate_fixed_ptolemys=False : 32 vars, 38 eqs
  L6a4 c0, eliminate_fixed_ptolemys=True  : 26 vars, 32 eqs
(27/33 once the non-zero-condition variable is added back.)
All four earlier failed runs were on the UNREDUCED system.

### (xxii) NO CHEAP OBSTRUCTION CLASS — measured all 14

On 4_1, class 1 was both smaller (2 sols vs 6) and entirely complex type, so I
expected a small class on L6a4. There is none: class 0 is 26/32, classes 1-13
are all 27/33. The class-size shortcut does NOT generalise.

### (xxiii) msolve 0.6.5 IS APT-INSTALLABLE — new capability in this container

  apt-get install -y msolve   ->  /usr/bin/msolve  (Berthomieu, Eder, Safey El Din)

This matters because msolve computes the RATIONAL UNIVARIATE REPRESENTATION,
which is precisely the method FKR section 6.4 reaches for after reducing to a
0-dimensional system. So the useful "port" was NOT porting their flag
coordinates into my Ptolemy system — it was acquiring their solver. The
coordinate port remains real work and remains undone.

### (xxiv) WHAT IS RUNNING / WHAT FAILED, honestly

  facstd (factorizing GB)   14+ min, 58 MB, no output yet
  minAssGTZ (minimal primes only, cheaper than primdecGTZ)  running, ~1.1 GB
  msolve RUR                7.5 GB RSS at 3 min, under an 11.5 GB kill guard
  Gauss-Newton, 60 random starts, 50 dps   0 of 60 converged
  phcpy (pip) / PHCpack binary (GitHub)    unavailable; api.github.com also 000

THE NUMERICAL 0/60 IS MY METHOD FAILING, NOT A FACT ABOUT THE VARIETY. Random
complex starts on 27 variables with a non-vanishing constraint essentially never
land on a component; this says nothing about how many solutions exist. Do not
cite it as evidence.

### (xxv) THE MULTI-MANIFOLD OBSTRUCTION TEST TIMED OUT — hypothesis UNTESTED

Hypothesis worth testing later: duality NEGATES the obstruction class in
H^2(M, dM; Z/3), so any class with c != -c would contain NO self-dual rep at
all, and the Borromean question would be answered structurally without solving
anything. The 4_1 data is CONSISTENT (class 1 nontrivial -> 0 of 2 self-dual)
but one manifold with two classes is not evidence for a general claim.

The check across m003/m004/m009/m015 died in sympy on m003's class 0 inside 280 s
and produced only a header. UNTESTED, not supported. Re-run it with msolve now
that msolve exists.


## 2026-09-05 (later) — the FKR port WORKED as a reduction; the question is still open

### (xxvi) What was worth porting from FKR was NOT the coordinates

Falbel-Koseleff-Rouillier, arXiv:1307.6697v2 section 6.1. Their cross-ratio/flag
coordinates run 12n variables reduced to 4n. For L6a4 (n = 8) that is **32** — WORSE
than the 26 SnapPy already gives in Ptolemy coordinates. Porting their coordinate
system would have cost hours and lost ground. Do not do it.

Their SECOND pre-processing step is the valuable one, and it is coordinate-independent:
whenever an equation is affine in a variable, A*z + B, with A a UNIT on the constructible
set, substitute z = -B/A and drop the equation. In Ptolemy coordinates the units come
free from the non-zero condition (snappy appends (monomial)*t - 1; every variable in that
monomial is invertible).

### (xxvii) MEASURED — the reduction, exact throughout (sympy over Q)

  4_1 c0     raw      7 vars / 9 eqs / maxdeg 7
             const-A  4 vars / 6 eqs / maxdeg 13
             unit-A   3 vars / 5 eqs / maxdeg 15
  L6a4 c1    raw     28 vars / 34 eqs / maxdeg 27
             unit-A  12 vars / 18 eqs / maxdeg 12   (16 elim, 48.5 s)
  L6a4 c2    unit-A  11 vars / 17 eqs / maxdeg 12   (17 elim, 187.2 s)
  L6a4 c3    unit-A  13 vars / 19 eqs / maxdeg 12   (15 elim, 89.3 s)

CORRECTNESS CHECKED, NOT ASSUMED: both reduced 4_1 systems give dim 0 and a proper ideal
under Singular std, consistent with 4_1's known 6 solutions in class 0. No solutions are
lost because A is a unit.

**FKR's degree warning is not a law.** On 4_1 the degree ROSE 7 -> 15, as they warn. On
L6a4 it FELL 27 -> 12. Measure per manifold; do not assume either direction.

### (xxviii) The memory contrast is the evidence the reduction is real

Same question, same class, same prime:
  UNREDUCED c1 mod 32003   9.1 GB after 20 min, no answer (killed)
  REDUCED   c1 mod 32003   ~292 MB, still running

~30x less memory. The nine earlier failures were all handed the unreduced system.

### (xxix) STILL OPEN — a smaller system is not a solved one

No Groebner basis has returned. Eight runs in flight (std / slimgb / msolve RUR, classes
1-3, over Q and mod 32003). It remains entirely possible that 12 vars at degree 12 is
still out of reach in this container, in which case the port is a real improvement that
does NOT close the problem.

**SCOPE, load-bearing:** FKR's abstract limits their worked results to manifolds glued
from FEWER THAN THREE tetrahedra. 4_1 is 2; L6a4 is 8. This is an extrapolation four
times past their largest example — which is why the 4_1 calibration exists and why a
positive result here would need its own check.

### (xxx) Why non-emptiness suffices — recap

By the obstruction argument (arithmetic core lean-verified, exit 0), a representation in
a NON-TRIVIAL obstruction class cannot be self-dual. So a single point of the Ptolemy
variety in any of classes 1-13 is automatically complex type. The question is "is the
ideal proper", not "decompose the variety".

Ptolemy database host still returns 000; the allowlist has not taken effect.


## 2026-09-05 (evening) — THE BORROMEAN QUESTION IS ANSWERED (mod p)

### (xxxi) L6a4 carries complex-type PGL(3,C) representations — THREE classes, not one

Route: FKR-reduce (28 -> 11-13 vars), then generic hyperplane slicing, then msolve over
F_32003. The manifold is the one the mass construction uses, not the 4_1 proxy.

  class  H2_class (Z/3)                          trivial?  verdict
  0      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       YES       (geometric lives here)
  1      [0,0,0,0,1,0,2,0,0,0,0,0,0,1,0,0]       no        dim 5, DEGREE 18 (full RUR)
  2      [0,0,1,2,0,0,0,0,0,0,1,0,0,0,0,0]       no        positive dim (>= 7)
  3      [0,0,1,2,1,0,2,0,0,0,1,0,0,1,0,0]       no        positive dim (>= 7)

All three are NON-EMPTY and NON-TRIVIAL. By the obstruction argument (duality negates
the class; arithmetic core lean-verified), nothing in a non-trivial class is self-dual,
so every representation in all three families is COMPLEX TYPE.

Three independent classes matters: one could be an artifact of my reduction; three
behaving consistently, with class 1 fully resolved, is not.

### (xxxii) The slicing ladder — the validation, and the msolve output key

  c1, 1-4 slices   [1,12,-1,[]]  + "The ideal has positive dimension"
  c1, 5 slices     [0,[32003,12,18,...RUR...]]   dim 0, degree 18
  c1, 6-7 slices   [-1]                          empty (over-sliced)

Each generic hyperplane drops dimension by one, so dim = 5. The ladder could not arise
from a broken pipeline. MSOLVE OUTPUT KEY, verified in both directions with -v 1:
    [0, [...]]        zero-dimensional, RUR follows
    [1, n, -1, []]    POSITIVE DIMENSION (a refusal marker, NOT empty)
    [-1]              empty
The middle one is a trap: -1 reads like "dimension of the empty set". It is not.
Run with -v 1 and READ THE LOG; without -v 1 the log is 0 bytes and says nothing.

### (xxxiii) TWO BUGS OF MINE, both caught by external checks not by re-reading

1. I reported class 1 EMPTY off [1,12,-1,[]]. It is positive-dimensional. Caught by the
   monitor surfacing the log line I had not read.
2. First slicing run reported empty at 1, 2, 3 slices -- impossible for a proper ideal by
   the Nullstellensatz. That impossibility prompted the check: slice.py re-joined lines
   with ",\n" when the .ms lines already ended in ",", giving 17 double commas and
   malformed input. A mathematically impossible result is a bug signal, not a finding.

### (xxxiv) STILL OPEN

  * CHAR 0. Everything above is mod 32003. Every Singular over-Q run died on resources
    (EXIT=137/124). A char-0 msolve on the 5-sliced system is running -- that is the one
    that would establish non-emptiness over C and yield actual algebraic numbers.
  * NO EXPLICIT CHARACTER YET. The complex-type conclusion rests on the obstruction
    argument, whose two topological inputs are GGZ citations carried as hypotheses. A
    direct chi(g) vs chi(g^-1) test on a char-0 solution would be independent evidence,
    of the same kind already held for 4_1.
  * Classes 4-13 reduced (9 of 13 done); not yet solved.
  * Degree 18 counts a generic linear section, NOT representations.


## 2026-09-05 (late) — 🛑 RETRACTION: the L6a4 non-emptiness result is NOT established

### (xxxv) The FKR reduction as I implemented it is NOT solution-faithful

The substitution q -> numer(q.subs(x, -B/A)) MULTIPLIES THROUGH BY A POWER OF A, which
ADDS the locus {A = 0} to the variety. Unless the ideal is saturated by A, the reduced
system is a SUPERSET of the true image, not a faithful presentation.

Measured on L6a4 class 1: 4 of the 16 substitutions divide by a non-constant expression.

  step  0  x0  = num/(x1*x10*x11*...*x9)      -- ALL 26 other coordinates
  step 13  x19 = num/(x1*x4)
  step 14  x23 = num/(x2*x4)
  step 15  x11 = num/(x2*x4*x8)

And ALL 18 roots of the degree-18 RUR lift to points where those denominators vanish
(x0 reaches 2.75e+471). So the 5-fold slice landed ENTIRELY on spurious locus.

### (xxxvi) WHAT IS RETRACTED

  RETRACTED  "L6a4 class 1 is non-empty"            -- true of the REDUCED system only
  RETRACTED  "the Borromean rings carry complex-type PGL(3,C) representations"
  RESCOPED   "dim 5, degree 18, over Q"             -- describes the reduced system,
                                                       on what appears to be a spurious
                                                       component

The mod-p and char-0 computations were correct as computations. What was wrong was my
inference from them to the ORIGINAL variety.

### (xxxvii) WHAT SURVIVES

  * The 4_1 result. Computed on the UNREDUCED 7-variable system, exact, and independently
    reproduced twice. Untouched.
  * The obstruction argument (non-trivial class => not self-dual), arithmetic core
    lean-verified.
  * FKR affine-unit elimination as a TECHNIQUE -- but it must saturate.

### (xxxviii) THE LESSON — a calibration that PASSES is not proof of soundness

The 4_1 calibration passed at every stage: same solution count, same characters, clean
lift. It did not cover this failure mode, because on 4_1 the slice happened to land on a
GENUINE component. The defect only appears when a slice lands on spurious locus, which
4_1 never exercised.

The failure was caught by an INDEPENDENT DOWNSTREAM CHECK -- the lift blowing up to
1e471 -- not by the calibration. Three times today an external consistency check caught
what re-reading my own reasoning did not: the msolve log line, the Nullstellensatz, and
now the lift residual.

### (xxxix) THE FIX

Saturate. Either add u * (product of all denominators A_i) - 1 = 0 with a fresh variable
u, or use Singular's sat(). Note the ORIGINAL non-zero condition already asserts every
Ptolemy coordinate is invertible -- the reduction evidently destroyed that constraint
rather than preserving it, which is itself worth understanding before trusting the
technique again.


## 2026-09-05 (night) — RESOLVED: the Borromean rings DO carry complex-type reps, with a witness

### (xl) The result, and what makes it reportable this time

msolve on the SATURATED class-1 system (12 vars + u, 18 eqs + saturation), char 32003:

    Dimension of quotient: 4
    [0, [32003, 13, 4, [...], [1, [[4, [30342,592,8722,2516,1]], [0,[1]], ...

Zero-dimensional, DEGREE 4, full RUR — monic t^4 + 2516t^3 + 8722t^2 + 592t + 30342,
factoring into two quadratics, so the points live in GF(p^2).

THE ROUND TRIP — the check the first attempt failed:

    28 coordinates lifted
    original equations FAILING: 0 of 34
    zero coordinates: NONE

A point lifted through all 16 substitutions satisfies EVERY original Ptolemy equation
exactly in GF(32003^2), with no coordinate zero. This morning's 18 points all failed this,
one coordinate reaching 2.75e+471.

Class 1 is NON-TRIVIAL (H2_class [0,0,0,0,1,0,2,0,0,0,0,0,0,1,0,0], entries 1 and 2 in
Z/3). By the obstruction argument, nothing in a non-trivial class is self-dual. So L6a4 —
the manifold the mass construction uses — carries complex-type PGL(3,C) representations.

### (xli) The two runs together: the junk WAS the shortcut

    unsaturated   dim 5, degree 18   almost entirely the spurious {A = 0} locus
    saturated     dim 0, degree 4    the genuine points

Saturation removed a five-dimensional spurious component and left four honest solutions.
That is why the WRONG answer took 4 minutes and the RIGHT one took hours: removing the
degenerate locus removes the easy place for the solver to land. "Saturate and re-run" is
not a cheap repair; expect the sound version to be dramatically harder.

### (xlii) THE ENGINE MATTERS MORE THAN I ASSUMED

    Singular std, unsaturated c1     timed out at 39 min
    msolve,       unsaturated c1     ~4 min, full RUR
    Singular std/sat, saturated      halt 1 + timeout at 3-8 GB (six runs)
    msolve,       saturated          SOLVES

I routed every saturation attempt through Singular because sat() lives there — and let
that pull the SOLVING there too. Six failed runs were failing on the engine, not the
mathematics. The u-equation formulation (I + u*prod(vars) - 1) needs no sat() at all and
goes straight to msolve. Do that first next time.

### (xliii) TWO SILENT BUGS, both caught by impossible arithmetic

    numer() adding {A=0}       printed dim 5 degree 18 over Q   -> lift blew to 1e471
    sat(I,v)[1] taking gen 1   printed GB 1 dim 11 NON-EMPTY    -> dim cannot grow

Neither tool errored; both exited 0 with a confident sentence. The calibration that should
have caught the first (4_1) PASSED under the broken reduction, because 4_1's solutions
avoid the spurious locus and because I only ever tested that the guard ACCEPTS good
points. test_guard_rejects_spurious.py now pins the rejecting direction.

### (xliv) CAVEATS still attached

  * MOD 32003. Proper mod p => proper over Q unless p is bad => non-empty over C by the
    Nullstellensatz. Strong, not a proof. Char-0 run in flight.
  * Degree 4 is the mod-p count; over C it may differ.
  * The obstruction argument's two topological inputs are GGZ results carried as
    HYPOTHESES. Only its Z/3 arithmetic is lean-verified.
  * Complex type is the NECESSARY condition the Sym^2 gate demands, NOT sufficient.
    Nothing here connects these representations to the eightfold's N=3 problem.
  * Classes 2-13 unsolved (c2 segfaulted on msolve's internal ceiling).

## 2026-10-12 — §(xliii)'s own regression guard has NEVER RUN

§(xliii) above records two silent bugs, the lesson that *"neither tool errored;
both exited 0 with a confident sentence"*, and the repair: *"the calibration
that should have caught the first (4_1) PASSED under the broken reduction …
because I only ever tested that the guard ACCEPTS good points.
`test_guard_rejects_spurious.py` now pins the rejecting direction."*

**It does not. It cannot be collected, and never could have been.** Line 13 is

    core = ast.literal_eval(open('L6a4_c1_q_sl5_P.res').read().strip().rstrip(':'))[1]

at **module scope**, so it runs at import, before any test body. Measured on
`main` `ab86909398b`:

- **`L6a4_c1_q_sl5_P.res` does not exist anywhere in the repository**, and a
  corpus-wide grep finds the string in exactly **one** place — that `open()`
  call. Nothing generates it, nothing else references it.
- The `.res` files that do exist are hyphenated and come from two producers
  (`ptolemy_class_sweep.py:225`, `rur_exact_number_field.py:104`), both of
  which resolve through `HERE = pathlib.Path(__file__).resolve().parent`. This
  test is the only `.res` consumer in the tree using a **bare relative path**,
  so it would additionally be cwd-dependent even if the file existed.
- `python3 -m pytest computations/ --collect-only` →
  `ERROR computations/ptolemy/test_guard_rejects_spurious.py - FileNotFoundError`.

**So the guard written BECAUSE a calibration gave false assurance is itself
giving false assurance**, and this bean is where the claim is recorded. That is
§(xliii)'s own lesson one level up: a test that cannot run reports nothing, and
reads from the ledger as though it reports something.

**Not fixed here, deliberately.** Which file was meant is not recoverable from
the corpus — the nearest present sibling is `L6a4_c1_fkr_p.res` (the only other
underscore-named `.res`), and the hyphenated RUR outputs are a different shape.
Guessing it would be exactly the speculative repair this bean's §(xliii) warns
about. What is needed is the author's answer to *which `.res` is the degree-18
RUR from the UNSATURATED reduction*, after which the fix is one line plus the
`HERE /` idiom its two siblings already use.

Found while running the first `pytest` on `computations/` on record; full
measurement in `docs/audits/2026-10-12-first-pytest-run.md`.

### Progress (Round 73 — PR litlfred/qou#8318)
- Formalized in PR `litlfred/qou#8318` (`feat/round73-symsquare-fibretl-mu3slot-sleak-deuteronz-43c1`, Commit 1 `d5360fac6f1464f5fd03c06ef76e726e30c785fd`, Head `e58aca150b7054a3222889e8bb9937602e515ca4`, `scriptHash: 19f0b8589c79`).
