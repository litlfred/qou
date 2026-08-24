---
# qou-0cyu
title: 'PROGRAMME: prove the remaining TL/Hecke chain in Lean -- four Mathlib gaps, one Mathlib ASSET (Artin-Wedderburn exists)'
status: todo
type: task
priority: normal
created_at: 2026-08-09T18:18:27Z
updated_at: 2026-08-24T20:03:10Z
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


## CORRECTION -- I OVER-PROMISED THE WEDDERBURN ITEM. Read this before starting it.

I listed "the Wedderburn instance from Mathlib's Artin-Wedderburn" as HIGHEST
LEVERAGE and implied it could be assembled from existing pieces. I have now
checked, and that was wrong in the way that matters.

WHAT I GOT RIGHT. Mathlib does have Artin-Wedderburn, and this tree already has
two Mathlib-gap fills around it that I had not noticed:

    QOU/MathlibExt/MatrixSemisimple.lean   isSemisimpleRing_of_nonempty --
      matrix rings over a division ring are semisimple. Fills Mathlib's own
      `proof_wanted IsSemisimpleRing.matrix`. Bean qou-5mrn.
    QOU/MathlibExt/EndSemisimple.lean      isSemisimpleRing_end -- endomorphism
      rings of finite-dimensional vector spaces are semisimple. Fills Mathlib's
      `proof_wanted IsSemisimpleRing.module_end`. Bean qou-ciun / epic qou-otbb.

WHAT I GOT WRONG, and it is the blocker. EVERY Mathlib Wedderburn theorem --
exists_algEquiv_pi_matrix_divisionRing, ..._finite, exists_ringEquiv_pi_matrix_*,
all of them -- is stated under `variable (R) [IsSemisimpleRing R]`. Mathlib gives
the STRUCTURE theorem; the SEMISIMPLICITY HYPOTHESIS is the hard part, and for
H_n(q) it is the Tits deformation / Gyoja-Uno argument. It is not in Mathlib and
it is not in this tree (grep for IsSemisimpleRing in QOU/ returns only the two
MathlibExt files above and a comment). So there is no assembly; there is a
research-grade prerequisite.

AND A PHANTOM I PROPAGATED. Commit 47c4199bd's message says "the tree already
had H3A/H4A and their Wedderburn isomorphisms". It does NOT. That commit touched
only FullRank.lean, InstanceH3.lean and InstanceH4.lean -- rank and dimension --
and grepping InstanceOnH3A/InstanceOnH4A for AlgEquiv or RingEquiv returns
NOTHING. There is no concrete algebra isomorphism to a product of matrix
algebras anywhere for H3A or H4A.

I repeated that claim to the sibling as Ask 2 on litlfred/qou#4857 ("if that
isomorphism is a usable Lean equiv, finrank = 24 follows directly"). I hedged it
there -- "not asserted, the equiv has not been read closely from this side" --
and the hedge was correct. Now it is settled: the equiv does not exist. If
anyone acts on that ask, they will be chasing something that is not there.

## THE ROUTE THAT WOULD ACTUALLY WORK, at low n only

Semisimplicity transfers along a ring equivalence, and a finite product of
matrix algebras over a field is semisimple (MatrixSemisimple gives the factor
case). So at n = 3 and n = 4 specifically:

  1. CONSTRUCT the concrete AlgEquiv H3A = M_1 x M_2 x M_1 (and H4A = M_1 x M_3
     x M_2 x M_3 x M_1, or its TL quotient M_1 x M_3 x M_2). This is the real
     work, and it does not exist yet.
  2. Semisimplicity then FOLLOWS -- no Tits deformation needed at fixed n.
  3. Mathlib's Wedderburn then applies, and the central idempotents pi_lambda
     can be read off the product decomposition.
  4. y_lambda and the block scaling still need the Markov trace's own structure;
     see qou-luq7, where the block scaling is identified as the axiom the class
     SHOULD have carried.

REVISED PRIORITY. This is no longer the cheapest item in this bean -- step 1 is
a substantial explicit construction. G2 (recipe fully specified above, both
ingredients proved) is now the cheapest real progress. Do G2 first.


## G2: THE STATEMENT IS NOW VERIFIED CORRECT BEFORE PROVING IT

Formulating a general theorem and then discovering mid-proof that it is subtly
false is the expensive failure here, so I checked first, at 40 dps, n = 0..12:

    [2]_q^n  =  sum_{j in Finset.range (n+1)} ballot n j * qint q (n + 1 - 2*j)

with NATURAL SUBTRACTION semantics on the index (clamp to 0) and qint q 0 = 0.
Residual is pure round-off throughout -- 0.0 at n = 0 rising to 4.7e-37 at
n = 12, tracking the magnitude of [2]^12 = 4371.97, not a defect.

Also swept for counterexamples to the two ingredients over the same range:
ballot_succ_succ for all n <= 12 and all j, and ballot_boundary_zero for
j <= 7. NONE.

So the exact Lean statement to prove is:

    theorem qdim_normalisation (q : R) (hq : q != 0) (h1 : q - q⁻¹ != 0) (n : N) :
        (q + q⁻¹) ^ n
          = sum j in Finset.range (n + 1),
              ((ballot n j : Z) : R) * qint q (n + 1 - 2 * j)

Base case n = 0: range 1, ballot 0 0 = 1, qint q 1 = 1 (needs h1).

Induction step, in the order the Finset lemmas want it:
  1. pow_succ, then ih, then Finset.mul_sum -- pushes (q + q⁻¹) inside.
  2. Per term: for 2j <= n the index is (n - 2j) + 1, so qint_three_term
     rewrites (q+q⁻¹) * qint(n+1-2j) = qint(n+3-2j) + qint(n-1-2j)... CAREFUL,
     write it as m = n - 2j and use qint(m+2) + qint(m) = (q+q⁻¹) qint(m+1).
     For 2j > n the factor qint(n+1-2j) is qint 0 = 0 and the term dies.
  3. Split the sum in two; reindex the lower half by j -> j+1
     (Finset.sum_range_succ' is the lemma that shifts the base, not the top).
  4. Recombine with ballot_succ_succ; the j = 0 term uses ballot_zero on both
     sides. The surplus top term is killed by ballot_boundary_zero (even n) or
     is absent (odd n) -- and with the natural-subtraction form it is killed by
     qint 0 = 0 as well, so the parity split may not even be needed. TRY WITHOUT
     IT FIRST.

That last remark is the payoff of the natural-subtraction trick and is worth
testing before writing any parity case analysis.


## 2026-08-24 — the highest-leverage item is now unobstructed

This bean's headline item is wiring Mathlib's Artin–Wedderburn into an instance
of the Wedderburn class. Measured today, that was **blocked by the class
itself**, not merely unstarted: `QOU.Hecke.WedderburnDecomp` carried a
`trace_decomp` field which, together with the *derived* `trace_exhaustive` in
the same file, forced `(1 − y_μ) · tr_M(π_μ) = 0` for every block — so no
instance with the intended nontrivial `y_λ` could exist. Machine-checked in
`9e8b712fa2`; the field is replaced by an honest `block_scaling` hypothesis in
`722761c0eb`, and `trace_decomposition` is now derived.

Also worth correcting in this catalogue: it says *"`QOU.Hecke.Wedderburn`'s
class has NO INSTANCE (qou-luq7)"* — still true — but the reason given, that
"the two halves have never been put together", was not the whole story.

Unchanged: the four Mathlib gaps G1–G4 and the mis-priced G5.
