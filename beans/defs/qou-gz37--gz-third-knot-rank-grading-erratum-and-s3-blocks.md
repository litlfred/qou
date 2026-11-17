---
# qou-gz37
title: 'Third knot found in-corpus: GZ rank grading is NOT s(x) (guard), a source erratum adjudicated, and W_0 as S_3 partition blocks'
status: in-progress
type: task
priority: high
tags:
    - g3-aomega
    - route-c
    - literature
    - reorg-2026-10-04
created_at: 2026-08-19T12:10:00Z
updated_at: 2026-11-17T10:23:09Z
parent: b9cj
---

## Context

M3 (qou-m3ad) closed saying the one cheap remaining test for H_Ad was a RANK-6 knot
whose grading is not multiplicity-free, and that no such data was in the 371-PDF
corpus -- so it needed outbound search, which this sandbox blocks.

That operational conclusion was WRONG. The data is in the corpus.

## The methodology defect (self-correction)

The M3 sweep keyed on the string "Stokes". Garoufalidis-Zagier "Knots and Their
Related q-Series" (SIGMA 19 (2023) 082, library/arxiv-2111.06645/2304.09377v2.pdf) says "Stokes"
EXACTLY ONCE, so it ranked below thirty other files and was never opened. It is not
obscure -- it is the sequel [44] that 2111.06645 announces IN ITS OWN ABSTRACT, an
abstract I had already quoted.

General lesson: a corpus sweep keyed on the vocabulary of the answer you EXPECT will
miss the paper that answers in different words. The sweep looked for resurgence
vocabulary; the data arrived in quantum-modularity vocabulary.

The narrower §6 claim -- "no q->0 STOKES MATRIX for a third knot in the corpus" --
remains accurate and is NOT retracted. What was wrong was the conclusion drawn from it.

## The near-miss (why the guard is load-bearing)

GZ §3.5 reports for (-2,3,7) "a new phenomenon ... the weight spaces have higher
multiplicity" -- weights totalling r=6 with one of dimension 4. That reads as exactly
the rank-6 non-multiplicity-free refutation of H_Ad that M3 asked for.

IT IS NOT. The graded object has total r, which is 2 at 4_1, while s(1)=3; and 4_1's
weight set is {-1/2,+1/2}, two elements against s(x)'s three. DIFFERENT OBJECTS.
This is the da-arity-conflation failure mode, one inference away from retiring a
hypothesis on the strength of an unrelated grading. Guard: T4 + the Lean theorem
higher_multiplicity_does_not_refute_h_ad, which states both halves in one place so
neither can be quoted without the other.

## Erratum adjudicated in the source

Three GZ §3.5 statements describe one grading:
  prose "weights 0,1,2 with dimensions 1, 4 and 1"          -> (1,4,1)
  explicit W_0=<H0,H3,H4,H5>, W_1=<H1>, W_2=<H2>            -> (4,1,1)
  delta=(0,1,2,0,0,0); weight vector (-1,0,1,-1,-1,-1)      -> (4,1,1)

Two independent internal statements against one: the PROSE TRANSPOSES its first two
dimensions. Both readings total 6, so a sum-check cannot catch it -- same shape as the
GGM eq-(200) q^1 erratum adjudicated earlier in this arc.

## What is genuinely new

1. CORROBORATION on a third knot. GZ ranks r = 2,3,6 (stated in 2111.06645 §2.1;
   recovered independently in 2304.09377 §3.4 from q-series counts 4,6,12 = 2r).
   M3 Part 4's signature rule gives r = real + 2*pairs = 2,3,6, and r = |P_K| - 1.
   Three knots, three DISTINCT values, three routes, one answer.

2. W_0 IS AN S_3 REPRESENTATION IN PARTITION BLOCKS. rho is the identity on W_1,W_2
   and has kernel Gamma(2) on W_0, so W_0 carries a rep of S_3 = Gamma/Gamma(2),
   decomposing as "the 2-dimensional irrep and two copies of the trivial" =
   (2,1) + (3)^2, dim 2+1+1 = 4. S_3-irreps are indexed by partitions of 3 -- the SAME
   Wedderburn indexing the QOU Hecke programme uses at q=1. The third knot's modular
   structure lands in the corpus's own language without being put there.

3. THE SIGN BLOCK IS ABSENT (multiplicity 0). Under the standard identification the
   sign block is the bar-odd one, so the Gamma/Gamma(2) action on the level-2 part
   carries no sign component -- a chirality-flavoured asymmetry on the same involution
   that grades the DT split.

4. THE ABSENCE IS FORCED (added same session, upgrading item 3 from an observation).
   chi(W_0) = [4,2,1] on the S_3 classes (e, transpositions, 3-cycles) of sizes
   (1,3,2). That is exactly [3,1,0] + [1,1,1] = the character of the PERMUTATION
   MODULE ON 3 POINTS plus a trivial. Characters determine complex reps up to iso,
   so W_0 = C[X] + C for a 3-element S_3-set X. And a 3-point permutation module of
   S_3 contains NO sign component -- <perm,sign> = (1*3*1 + 3*1*(-1) + 2*0*1)/6 = 0,
   a general fact with nothing knot-specific in it; trivial summands contribute 0 to
   sign multiplicity, so no number of them can create one. The missing sign block is
   FORCED BY SHAPE.

5. BUT THE SCOPE IS ONE KNOT (adversarial, tempering item 4). GZ introduces the level
   as "a new phenomenon" at (-2,3,7), N=2; 4_1 and 5_2 have N=1, so rho factors
   through the TRIVIAL quotient -- no finite group acts, hence no sign block there to
   be absent. General mechanism, single-instance instantiation. Item 1 of the previous
   NEXT STEP ("get 4_1/5_2 comparanda") is therefore ANSWERED AND CLOSED: there are no
   comparanda to get, and that is a fact about the level, not a gap in the search.

WHAT STAYS INTERPRETIVE: that X is geometrically the three cusps of Gamma(2) (or the
three non-zero 2-torsion classes) is the standard Gamma/Gamma(2) = S_3 picture, but GZ
does not say W_0 realizes it and nothing here claims so. Character identity proved;
geometric reading not. Nothing wired.

## Artifacts

- Lean: QOU.QBeta.GZThirdKnotRankGrading (core Int, imports AdjointIndexSetM3;
  lean-direct exit 0, sorry-free, #print axioms shows no sorryAx)
- Probe: computations/probes/gz_third_knot_rank_grading.py, 29/29
- Audit: docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md §7

## Part G (2026-08-19): the 6_1 prediction CONFIRMED by a sibling

The Part-F conditional prediction (6_1 -> r=4, |P_K|=5 from DG trace-field type [0,2])
was independently certified while this work was in progress: main 96d65d02e, bean
qou-btvl, probe apoly_census_ldegree_certification_probe.py (3/3), from the Culler
A-polynomial census (uploads/A_census.tgz, owner upload).

  4_1 = K2_1: geom L-degree 2, full 3
  5_2 = K3_2: geom L-degree 3, full 4
  6_1 = K4_1: geom L-degree 4, full 5     <- matches the prediction

WHY IT IS A TEST: the prediction side is the DEGREE OF A NUMBER FIELD
(x^4-2x^3+x^2+3x+1, signature [0,2], disc 257); the certification side is the
L-DEGREE OF A NEWTON POLYGON (census A-polynomial of K4_1). Unrelated objects,
unrelated sources, agreeing on three knots with three distinct values (2,3,4) -- and
6_1 was predicted before its census value was in hand.

NOT A TEST (sibling flagged first): full = geom + 1 is definitional, the +1 being the
abelian rep. The |P_K| = r+1 leg corroborates nothing; all content is in
deg F_K = geom L-degree = r.

CONTROL FIRES: the identity FAILS at (-2,3,7) -- trace field degree 3 vs rank 6 --
exactly where A_K^red strictly contains F_K. The rule does not fit everything.

CREDIT: the census certification is the sibling's work; ours is the prediction it
confirms and the hypothesis that made it a prediction rather than a fit.

Lean Part G: geomLDegree, fullLDegree, sixOne_prediction_confirmed,
degree_equals_geom_ldegree_on_all_three, the_three_degrees_are_distinct,
plus_one_leg_is_definitional, control_fires_where_hypothesis_fails. Probe now 21/21.

## Part H (2026-08-19): a THIRD route to r(6_1)=4 — from the saddle analysis

Went after "an independent resurgence DT count for 6_1". Did NOT get one -- see the
scope note -- but got a third independent determination of r, and the closest one yet
to the resurgence side.

Ohtsuki-Yokota (library/ki6c/ki6c.pdf; saddle data extracted by a sibling, bean qou-6ort)
give 6_1's gluing-equation quartic 2z^4 - z^3 - 2z^2 + z + 1, from a STATIONARY-PHASE
analysis of the Kashaev integral. Measured exactly: irreducible, discriminant 257
(prime), 0 real roots -> signature [0,2]. Matches DG's trace field on every invariant.

AND THE FIELDS ARE EQUAL, not merely invariant-matched: with a a root of DG's quartic,
gamma := -a^3 + 3a^2 - 4a - 1 satisfies gamma^4 - gamma^3 - 4gamma^2 + 4gamma + 8 = 0
exactly in Z[a]/(dg), and gamma/2 is a root of the Ohtsuki-Yokota quartic. Both
irreducible of degree 4 => Q(gamma) = Q(a). (disc(x^4-x^3-4x^2+4x+8) = 16448 =
2^6 * 257: same field, index-2 scaling gamma = 2*beta.) Machine-checked in Lean as
integer 4-tuple arithmetic, not asserted.

THREE CONSTRUCTIONS WITH NOTHING IN COMMON BUT THE KNOT now give r(6_1) = 4:
  a number field           (DG trace field, degree 4)
  a Newton polygon         (Culler census geometric A-poly L-degree 4)
  a stationary-phase analysis (Ohtsuki-Yokota gluing quartic, degree 4)

SCOPE -- STILL NOT A DT COUNT, stated plainly so the agreement is not oversold. The
saddles are the CRITICAL POINTS; the DT invariants are the Stokes constants on the
Borel rays BETWEEN them. All three routes measure r, the R1 / Euler-characteristic
shadow. The resurgence DT count for 6_1 is exactly as open as before, and the sibling
bean qou-btvl names the same gap. What the agreement buys is a falsifiable SHAPE:
with |P_K| = 5, 6_1's reduced Stokes matrix is 4x4 against 5_2's 3x3.

Lean Part H: Alg4, mulAlg4, reduction_table_consistent, gamma,
saddle_field_equals_trace_field, gamma_powers, gamma_is_not_rational,
three_routes_agree_on_sixOne, sixOne_stokes_matrix_is_four_by_four. Probe 25/25.

## Part I (2026-08-19): 9_12 kills a coincidence the rule had to be separated from

Went after "(-2,3,9) -> r = 5". Could NOT verify it (see below). But found and killed
a coincidence that had to die before any of Parts F-H could count as evidence.

Across 4_1/5_2/6_1 the IDEAL-TETRAHEDRON COUNT equals the trace-field degree (2,3,4).
Three for three. If the rank rule were riding on the TRIANGULATION rather than the
number field, everything above would be an artifact -- and nothing up to here
distinguished the two readings.

DG S6.5's 9_12 settles it: 10 IDEAL TETRAHEDRA, trace field of DEGREE 17, irreducible,
type [1,8] -- verified here independently by exact Sturm sequence (exactly 1 real root,
r1 + 2r2 = 17, no floats). 10 != 17. The coincidence dies at the fourth knot, and the
rule -- which reads the SIGNATURE and never the triangulation -- is untouched.

SHARPER THAN THE CORPUS'S EXISTING GUARD: PR #5277 refutes "degree ~ tetrahedra" using
the Whitehead link and Borromean rings, both LINKS, so the heuristic could be rescued
by restricting to knots. 9_12 is a KNOT and kills the knot-restricted version too.

NEW PREDICTION: under A_K^red = F_K, r(9_12) = 17 and |P_K| = 18. Far more falsifiable
than the small cases -- a wrong rule has 17 ways to miss here rather than 4.

STILL NOT VERIFIED, and 9_12 does NOT substitute: (-2,3,9)'s predicted r = 5 remains
open. Census identification needs SnapPy (absent in this sandbox; import fails) and no
(-2,3,9) saddle data is in the corpus, so neither the census route (Part G) nor the
gluing-quartic route (Part H) is available for it.

Lean Part I: idealTetrahedra, tetrahedra_match_degree_on_the_small_knots,
nineTwelveTetrahedra/Real/Pairs/Degree, nineTwelve_signature_gives_degree_seventeen,
tetrahedra_coincidence_breaks_at_nineTwelve, rank_rule_never_used_tetrahedra,
nineTwelve_prediction. Probe 29/29.

## NEXT STEP

1. [CLOSED THIS SESSION] Explain the absent sign block. DONE -- it is forced by W_0
   being a permutation module (item 4), and the "get 4_1/5_2 comparanda" sub-task is
   moot: those knots have level 1, so no group acts (item 5).
1b. OPEN SUCCESSOR: find a FOURTH knot with level > 1 and check whether its analogue
   of W_0 is again permutation-type. That is the only way to tell whether
   "permutation-type, hence no sign" is a general feature of these gradings or a
   coincidence of the one level-2 example. GZ ties level 2 to (-2,3,7)'s Newton
   polygon having HALF-INTEGER SLOPES, which is a searchable criterion for picking
   candidates rather than guessing knots.
2. [EXECUTED THIS SESSION] Re-ran the corpus sweep on structural vocabulary (knot
   names, pretzel, weight space, Galois orbit, trace field, quantum modularity,
   boundary-parabolic, level of a knot, A-polynomial) instead of "Stokes".
   RESULT: 94 of 371 PDFs match; the ranking is materially different from the
   Stokes ranking, and it surfaced a SECOND confirmed miss:

     library/ki6c/ki6c.pdf = Ohtsuki-Yokota, "On the asymptotic expansions of the Kashaev
     invariant of the knots with 6 crossings" -- i.e. 6_1, 6_2, 6_3, with the volume
     conjecture proved for them. It contains the string "Stokes" ZERO times, so it was
     structurally invisible to the original sweep. Second instance of the same defect,
     from the same cause.

   HONEST YIELD, stated so this is not oversold: ki6c does NOT close open items 1 or 3.
   It gives asymptotic expansions of the Kashaev invariant (the perturbative side) and
   works with the SINGLE geometric critical point -- not the full set of
   boundary-parabolic representations, so no |P_K| for 6-crossing knots -- and it
   carries no Stokes matrices. It is a genuine fourth/fifth/sixth-knot resource on the
   perturbative leg, and it is proof that the vocabulary bias hid more than one paper.
   FOLLOWED UP on the top unopened hit: 1511.05628 = Dimofte-Garoufalidis, "Quantum
   Modularity and Complex Chern-Simons Theory". §6 states trace fields as SIGNATURES
   [r1,r2] for FIVE knots -- the exact input the Part-4 rule consumes:
     4_1 x^2-x+1 [0,1] disc -3    | 5_2 x^3-x^2+1 [1,1] disc -23
     6_1 x^4-2x^3+x^2+3x+1 [0,2] disc 257
     (-2,3,-3)=(-2,3,9) x^5-x^4+x^3+2x^2-2x+1 [1,2] disc 23*733
     (-2,3,7) same trace field as 5_2 -> [1,1]
   (a) CONFIRMS Part 4's inputs for 4_1 and 5_2 from an independent source (Part 4 read
       them off GZ prose; DG states them as types).
   (b) FORCES PART 4's SILENT HYPOTHESIS INTO THE OPEN. The rule needs the signature of
       A_K^red, NOT of the trace field F_K. They coincide at 4_1 and 5_2 -- so the
       two-knot agreement settled nothing -- and (-2,3,7) is the counterexample: trace
       field = 5_2's (3 embeddings), measured rank 6, because P_K picks up a second
       Galois orbit over the totally real Q(eta).
   (c) TWO CONDITIONAL PREDICTIONS, stated with their hypothesis: under A_K^red = F_K,
       6_1 has r=4 / |P_K|=5 and (-2,3,9) has r=5 / |P_K|=6. Falsifiable, unverified.
   (d) GUARDED NON-INFERENCE: DG Table 2's "Level" column (4_1 <=7, 6_1 <=3, ...) is the
       CHERN-SIMONS level zeta^k=1, NOT GZ's level N. Reading it as the latter would
       manufacture the fourth level>1 knot out of an unrelated quantity. THIRD instance
       of this conflation trap in this arc.
   Still unopened: 2412.04241 (Garoufalidis-Scholze-Wheeler-Zagier, "The Habiro Ring of
   a Number Field" -- likely relevant to the corpus's Habiro-element work), 1303.5278.
3. The H_Ad polynomial test is STILL open and still needs a genuine Stokes matrix for
   a third knot -- unchanged by this bean, and still not in the corpus.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-19 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 83 Execution Note (2026-11-17T10:23:09Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8301`](https://github.com/litlfred/qou/pull/8301) (`feat/qou-b9cj-1gkf-gz37-ips1-ized-m1nz`, HEAD `8def28bdd6676a091a84204c0314f39da9ee6d5c`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/GaroufalidisZagierS3BlockAndFiveTwoDiscBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/garoufalidis_zagier_s3_block_and_five_two_disc_brick_probe.py` & `computations/probes/garoufalidis-zagier-s3-block-and-five-two-disc-brick.witness.json` (`scriptCommitSha = d726ce17152d0bdd416fbd50d86ba08930c726e7`, `scriptHash = 1b13751c9d60`, `outputHash = 36c8353af8986ccd33f16fae6cef94ba4dab83e96f5a0e688d772b07b9d32e72`).
