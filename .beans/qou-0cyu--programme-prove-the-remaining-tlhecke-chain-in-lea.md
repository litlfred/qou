---
# qou-0cyu
title: 'PROGRAMME: prove the remaining TL/Hecke chain in Lean -- four Mathlib gaps, one Mathlib ASSET (Artin-Wedderburn exists)'
status: todo
type: task
created_at: 2026-08-09T18:18:27Z
updated_at: 2026-08-09T18:18:27Z
---


Branch: claude/anchor-followups-2026-08-08, after merging main (462 commits,
PR #4857's Hecke tower). Owner directive: "then prove all in lean. add mathlib
infra as needed. bean up."

This bean is the CATALOGUE. Each item says what is open, whether Mathlib helps,
and what it would actually cost. Children get their own beans as they start.

## THE ASSET NOBODY HAS USED -- Mathlib HAS Artin-Wedderburn

Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean, at the pinned rev, provides

    exists_algEquiv_pi_matrix_divisionRing
    exists_algEquiv_pi_matrix_divisionRing_finite   [Module.Finite R_0 R]
    exists_ringEquiv_pi_matrix_divisionRing
    exists_algEquiv_matrix_divisionRing             (simple case)
    IsSimpleRing.tfae, isSimpleRing_isArtinianRing_iff
plus Mathlib/RingTheory/SimpleModule/Isotypic.lean for the isotypic pieces.

THIS IS THE EXISTENCE HALF of the Wedderburn decomposition, and it is sitting
unused. QOU.Hecke.Wedderburn's class has NO INSTANCE (qou-luq7); the finite
version above is exactly the shape needed to build one for H_n(q) over a field,
given finite-dimensionality -- which PR #4857 already proved as
IsHeckeOfFullRank (finrank = n!). The two halves have never been put together.

HIGHEST-LEVERAGE ITEM IN THIS BEAN. It converts ten modules from
"conditional on an uninhabited class" to "conditional on nothing".

## GENUINE MATHLIB GAPS -- confirmed absent at the pinned rev

Searched Mathlib for qInt / quantumInteger / TemperleyLieb / HeckeAlgebra: the
only hit is an unrelated MeasureTheory file. So ALL of the following are real
gaps, not lookup failures:

  G1. q-INTEGERS. No [m]_q, no q-factorial, no q-binomials as a developed API.
      This repo has scattered private defs (QOU.MathlibExt.QGaussianBinomialPascal,
      wedderburn_trace_identity.qInt, my TemperleyLiebTower.qint). Consolidating
      them into one Mathlib-shaped API is a prerequisite for G2 and would retire
      several duplicates. MEDIUM cost, HIGH cleanup value.
  G2. THE q-CLEBSCH-GORDAN NORMALISATION. [2]_q^n = sum_k m_k [n-2k+1]_q with
      m_k = C(n,k) - C(n,k-1) -- the q-dimension of V^(x)n for the 2-dimensional
      V. Proved here at n = 3 and n = 4 as ring identities
      (qdim_normalisation_three / _four); the general n is open. Induction on the
      three-term recursion qint_three_term, which is already proved. MEDIUM.
  G3. TEMPERLEY-LIEB ALGEBRA. Not in Mathlib at all. Needed to state
      H_n/rad = TL_n as an isomorphism rather than as a dimension count. LARGE.
  G4. CONNES SPECTRAL DISTANCE / RIEFFEL LIP-NORMS / compact quantum metric
      spaces. Not in Mathlib. Needed to state the metric results as anything
      more than the seminorm lemmas already proved
      (lip_kernel_forces_unbounded). LARGE, and arguably a research project
      rather than a formalisation task.

## THE ONE I MIS-PRICED, and the reason is worth recording

  G5. sum_k (C(n,k) - C(n,k-1))^2 = catalan n.
      I listed this in qou-u2jg as "pure combinatorics, no q" -- as though it
      were the EASY one. It is not. By RSK it says: pairs of same-shape standard
      Young tableaux with at most two rows are counted by Catalan(n), i.e.
      321-AVOIDING PERMUTATIONS ARE CATALAN. Mathlib has `catalan` but no RSK,
      no ballot numbers, and no pattern-avoidance theory.
      Two routes: (a) formalise enough RSK -- LARGE; (b) a direct induction on
      the ballot recursion, avoiding RSK entirely -- plausibly MEDIUM and worth
      trying FIRST. Verified numerically at n = 3,4,5: 1+4 = 5, 1+9+4 = 14,
      1+16+25 = 42.

## WHAT IS ALREADY PROVED, so nobody re-does it

  TemperleyLiebTower: qint_three_term_pair, markov_branching_general,
    qdim_normalisation_three/_four, branch_four_to_three_sym/_mixed,
    catalan_three/four/five, counts_are_catalan (vs Mathlib's own `catalan`),
    y_antisym_eliminated, y_antisym_factorisation, singlet_branch_pair,
    conventionD_kills_antisymmetriser, antisym_vanishes_only_at_two_roots,
    z_eq_q_forces_trivial, conventionD_unique_nontrivial (the IFF),
    not_conventionD_of_antisym_survives, y_mixed/sym_conventionD,
    IsConventionD, loop_reciprocal (q - z = 1/[2]_q, i.e. D IS the normalised
    TL trace at delta = [2]_q), qint/yw + qint_pos/yw_pos/yw_nonneg,
    qint_three_term, yw_branching, mul_div_pow_succ,
    traceRadical_* (two-sided ideal; star radical = bilinear radical),
    vanishing_step/_dom, vanishing_all_levels/_dom, dominates_of_branching,
    terms_zero_of_sum_zero, terms_zero_of_weighted_sum_zero
  WedderburnTraceDecomposition: trace_eq_sum_blocks,
    trace_decomposition_of_blocks, trace_eq_sum_weighted_characters
  YoungDiagramThreeRowCorner: isCorner_rowEnd, isCorner_lastRow,
    exists_threeRow_corner, youngPred, threeRow_vanishing_all_levels,
    card_three_threeRow_unique, threeRow_size_three_subsingleton,
    threeRow_vanishing_of_pinning

## ORDER I RECOMMEND

  1. THE WEDDERBURN INSTANCE from Mathlib's Artin-Wedderburn + IsHeckeOfFullRank.
     Highest leverage, uses an existing asset, and unblocks ten modules.
     Coordinate first -- QOU/Hecke/** is the sibling's territory
     (docs/coordination/hecke-tower-and-trace-parameter.md).
  2. G1 q-integer API, then G2 -- G2 is nearly free once G1 exists and the
     recursion is already proved.
  3. G5 route (b), the direct induction. Abandon to route (a) only if (b) fails.
  4. G3 and G4 are large enough to need their own decision, not a default yes.

## DISCIPLINE

AGENTS.md:779 -- Lean structure FIRST for any new derivation, before Python or
prose. Every item above is already a statement, so that is satisfied; keep it
that way for children of this bean.

## UPDATE -- G1 STARTED, and G2's proof is now fully worked out on paper

QOU/Mathlib/BallotNumbers.lean (NEW, sorry-free, imported from QOU.lean).
ballot_succ_succ needs only [propext, Quot.sound]; ballot_one only [propext].

    ballot n j = C(n,j) - C(n,j-1)                    (valued in Z)
    ballot_succ_succ    m_{j+1}(n+1) = m_{j+1}(n) + m_j(n)     THE ENGINE
    ballot_boundary_zero  m_{j+1}(2j+1) = 0                    THE CRUX
    ballot_one, ballot_values_{three,four,five}
    ballot_sq_sum_catalan_small   G5 at n = 3,4,5 vs Mathlib's own `catalan`

## THE FULL G2 PROOF, worked out -- write it up next, do not re-derive it

TARGET   [2]_q^n = sum_{j=0}^{floor(n/2)} m_j(n) * [n - 2j + 1]_q

STEP. Multiply the n-case by [2] and apply qint_three_term
([m+2] + [m] = [2][m+1], already proved in TemperleyLiebTower):

    [2]^{n+1} = sum_j m_j(n) ([n-2j+2] + [n-2j])

Reindex the second half by j' = j+1, using [n-2j] = [(n+1) - 2(j+1) + 1]:

    = sum_j ( m_j(n) + m_{j-1}(n) ) [n-2j+2]        over j = 0 .. M+1, M = floor(n/2)
    = sum_j m_j(n+1) [n-2j+2]                       by ballot_succ_succ

RANGE, and this is the ONLY subtle part:
  * n ODD  -> floor((n+1)/2) = M+1. The derived range matches exactly. Done.
  * n EVEN, n = 2m -> floor((n+1)/2) = m = M, but the derived sum runs to M+1.
    The surplus term sits at j = m+1 with coefficient m_{m+1}(2m+1), which is
    ZERO by ballot_boundary_zero. So it drops and the sums coincide.

So the parity split is REAL -- not an artefact of a clumsy index choice -- and
ballot_boundary_zero is exactly what resolves it. Both halves of the machinery
now exist; what remains is Finset bookkeeping over Finset.range (n/2 + 1), which
is fiddly but has no further mathematical content.

Base case n = 0: [2]^0 = 1 = m_0(0) * [1] = 1 * 1.

## WHY I DID NOT JUST FINISH IT

Honest reason: the remaining work is Finset range manipulation with a parity
case split, which is a real chunk of Lean and I would rather land the two
mathematical lemmas verified than a half-finished induction. The pieces are
proved; the assembly is mechanical and specified above.

## STILL OPEN, unchanged in priority

  1. The WEDDERBURN INSTANCE from Mathlib's Artin-Wedderburn. Still the highest
     leverage item in this bean, and untouched. QOU/Hecke/** territory.
  2. G2 assembly, per the recipe above.
  3. G5 general -- route (b), direct induction on ballot_succ_succ, avoiding
     RSK. ballot_boundary_zero will very likely be needed there too.
  4. G3 (Temperley-Lieb) and G4 (Connes/Rieffel) still need their own decision.
