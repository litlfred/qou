---
# qou-47nf
title: 'TRANCHE: the non-geometric Ptolemy component at n=3 — route E''s one surviving branch'
status: todo
type: task
priority: high
created_at: 2026-09-05T07:09:45Z
updated_at: 2026-09-05T09:43:20Z
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
