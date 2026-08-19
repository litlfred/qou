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
created_at: 2026-08-19T12:10:00Z
updated_at: 2026-08-19T12:45:00Z
---

## Context

M3 (qou-m3ad) closed saying the one cheap remaining test for H_Ad was a RANK-6 knot
whose grading is not multiplicity-free, and that no such data was in the 371-PDF
corpus -- so it needed outbound search, which this sandbox blocks.

That operational conclusion was WRONG. The data is in the corpus.

## The methodology defect (self-correction)

The M3 sweep keyed on the string "Stokes". Garoufalidis-Zagier "Knots and Their
Related q-Series" (SIGMA 19 (2023) 082, uploads/2304.09377v2.pdf) says "Stokes"
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
- Probe: computations/probes/gz_third_knot_rank_grading.py, 12/12
- Audit: docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md §7

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

     uploads/ki6c.pdf = Ohtsuki-Yokota, "On the asymptotic expansions of the Kashaev
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
   Other unopened high-rankers worth a look: 1511.05628, 2412.04241, 1303.5278.
3. The H_Ad polynomial test is STILL open and still needs a genuine Stokes matrix for
   a third knot -- unchanged by this bean, and still not in the corpus.
