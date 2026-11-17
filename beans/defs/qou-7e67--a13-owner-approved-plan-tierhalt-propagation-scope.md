---
# qou-7e67
title: 'A^(1/3): owner-approved plan -- tier+halt propagation, scope-restrict, derive archimedean id, binding-derived size; NO measured-radius input'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T11:51:31Z
updated_at: 2026-10-04T15:16:13Z
parent: qou-v2om
---


Branch: claude/anchor-followups-2026-08-08. Owner rulings 2026-08-09.

## The problem is TWO problems, and they are independent

  (a) PROVENANCE. R ~ A^(1/3) rests on "volume extensivity": bond-sum
      extensivity (derived) + Lean chain bond count M_n = n-1 (proved) + the
      ledger identification B = m_e*Vol => Vol ~ A => R ~ Vol^(1/3) ~ A^(1/3).
      The third link is an ARCHIMEDEAN IDENTIFICATION the corpus does not
      derive -- the hyperbolic volume of a link complement is a TOPOLOGICAL
      invariant, not a Euclidean spatial volume. Corpus tiers it itself,
      CONDITIONAL/PARTIAL: deltalambda/mirror_split_continuum_em_probe.py:39-49.
      The coefficient step R = 1*lambdabar_pi*A^(1/3) is separately called
      "THE UNDERIVED STEP" at :50-53.

  (b) EMPIRICAL. A^(1/3) is the WRONG FUNCTIONAL FORM for A <= 4 regardless of
      provenance. Solving R = lambdabar_pi*A^x for x:
          2H 0.9679   3H 0.4314   3He 0.5326   4He 0.3067   (needs 0.3333)
      Size tracks BINDING, not nucleon count -- 4He is tightly bound and compact
      (x ~ 1/3), 2H is a halo (x ~ 1).

FIXING (a) DOES NOT FIX (b). A perfectly derived hyperbolic->Euclidean map still
yields A^(1/3), still wrong at A<=4. (b) is the one that matters for the mirror
pairs.

## Options TESTED AND ELIMINATED before the owner ruled

  * "Is the exponent a DIMENSION question?" R ~ Vol^(1/D); Bring's surface and
    P(V) = S^2 are 2-real-dimensional, which would give x = 1/2 not 1/3.
    NO: no single exponent fits (4He wants 1/3, 3He ~1/2, 2H ~1). Not dimension.
  * "Reformulate with NO LENGTH OBJECT." hbar c/R(A) = m_pi/A^(1/3), so
    E_C = (3/5) alpha_EM Z(Z-1) m_pi / A^(1/3) -- masses only, no fm. Verified
    numerically identical. Removes the LENGTH but NOT the A^(1/3). COSMETIC.

## OWNER RULINGS

  1. TIER IT AND HALT PROPAGATION -- YES. Every consumer declares the tier so no
     downstream number silently inherits an underived step.
  2. SCOPE-RESTRICT to saturated nuclei -- YES.
  3. DERIVE THE ARCHIMEDEAN IDENTIFICATION -- YES. (Fixes (a) only; the Connes
     spectral-distance route is the identified opening -- see qou-mumr.)
  4. BINDING-DERIVED SIZE -- YES. (Fixes (b), the physically right answer.
     Currently circular: QOU binding is ~30 % off so it gives +37.8 %. Unblocks
     the moment the NN sector lands.)
  5. MEASURED CHARGE RADIUS AS A DECLARED INPUT -- NO. Rejected. Do not add a
     CAL-4. The parameter-free claim is not to be traded for light-nucleus EM
     numbers.

## ON THE SCOPE RESTRICTION: the "12" is TWO DIFFERENT 12s

Owner asked whether A ~ 12 is a compute limit that a bigger machine would move.
It is not, and the confusion is real because n = 3A puts two twelves in play:

    A = 12   MASS NUMBER, the saturation threshold           PHYSICS
    H_12     12 STRANDS = A = 4, the L1-certified ceiling    COMPUTE

Reaching A = 12 needs n = 36 strands. Scaling, by method:

     A    n=3A   dim H_n = n!        p(n) partitions   regime
     4     12    479,001,600                     77    L1-CERTIFIED
     7     21    5.11e19                        792    default max_strands cap
    12     36    3.72e41                     17,977    SATURATION regime
    56    168    2.53e302            228,204,732,751

Full-algebra route: 12 -> 36 strands is 33 ORDERS OF MAGNITUDE. No machine.
Partition-indexed route (Markov trace / Wedderburn): p(36) = 17,977. TRACTABLE.

So the closed-form bond chain is NOT compute-blocked at A = 12. What is capped
at n = 21 is the EXACT-TRACE CROSS-CHECK that VALIDATES the chain
(mass_binding_dashboard.py:20, "purely to VALIDATE the chain"). Therefore:

    BETTER COMPUTE EXTENDS THE VALIDATION, NOT THE PREDICTION.

The real barrier at A >= 12 is not compute -- it is qou-h7mh, the coordination /
bond-count question. The chain walks A-1 bonds through a 3-D object; at A = 12
that is 11 bonds against 66 all-pairs, and neither topology works across the
range (chain: 4He at 0.42x; all-pairs: fixes 4He at 0.84x but blows 6Li/7Li to
1.85x/2.20x). Scope-restricting to A >= 12 therefore moves the problem from the
radius law to the coordination law -- it does not remove it.

## Consequence for the scope restriction as ruled

Ruling 2 is adopted, but with this caveat recorded: there is currently NO A at
which the framework can quote a validated Coulomb energy. Below ~12 the radius
law is the wrong form; at and above ~12 the radius law is fine but the
coordination law is unresolved AND the exact-trace validation is out of reach.
State that limitation wherever a Coulomb number is published.
