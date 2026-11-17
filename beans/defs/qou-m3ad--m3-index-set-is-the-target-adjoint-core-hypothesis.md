---
# qou-m3ad
title: 'M3: H_Ad is the dtMin projection (R1 is dtMax) -- not a re-description; but support is ONE data point and rival H_floor survives'
status: in-progress
type: task
priority: high
tags:
    - g3-aomega
    - route-c
    - reorg-2026-10-04
created_at: 2026-08-18T21:00:00Z
updated_at: 2026-10-04T15:11:01Z
parent: b9cj
---

## The reframing (the main contribution)

M2 showed the closed-sector BPS spectrum would be ABELIAN — every Borel ray distinct,
trivial Davison-Meinhardt plethystic log, dim BPS_d = |Omega_d|, all multiplicities 1.
CONSEQUENCE: a direct sum of 1-dimensional spaces carries no information beyond WHICH
RAYS EXIST. So M3's real target is NOT "build a cohomological Hall algebra" (the
original Route C framing) but **derive the index set Omega**. That is a materially
sharper and more tractable goal, and it is what qou-rtec's M3 rung should now read.

## H_Ad — the hypothesis (NOT a derivation; do not upgrade without a proof)

The knot-INDEPENDENT core of the index set is the weight set of the ADJOINT rep of
sl_2: for meridian eigenvalues (m,1/m) and x=m^2, Ad has eigenvalues (x,1,1/x), so
chi_Ad(x) = x + 1 + 1/x = s(x) exactly and chi_Ad(1) = 3 = dim sl_2.

MECHANISM (why not numerology): in complex Chern-Simons the Borel singularities are
differences of complex volumes of flat connections, and the deformation theory of a
flat connection is governed by H^1(M, Ad rho) — the adjoint local system is the
CANONICAL coefficient object, not a chosen one. In QOU terms Ad = Sym^2 V = S^(2)(C^2), the SCHUR-WEYL PARTNER of the
partition-(2) Hecke block (partner, NOT the block -- see Part 3), so it is
expressible in Hecke language.

## What was tested (probe: computations/probes/aomega_m3_adjoint_index_set.py, 4/4)

 T1 chi_Ad reproduces M2's s(x) exactly — exponents AND multiplicities, no free parameter.
 T2 H_Ad PREDICTS knot-independence; observed (same s(x) governs 5_2, GGM 239/277/307).
    This is the fact that defeated every knot-specific reading (Driver14's eight + R1).
 T3 ADVERSARIAL: H_Ad FAILS as a scalar — knot-independent gives (3,3) vs certified
    (3,4), exactly like blockCountH3. So its content is the GRADING, not the count.
    Recorded so H_Ad cannot be mis-sold as a counting answer.
 T4 ADVERSARIAL: the 3-element palindromic SHAPE is generic ({a,0,-a} for any a), so
    the shape proves nothing; H_Ad rests entirely on its mechanism + the a=1
    normalization forced by x=m^2.

## Lean (QOU/QBeta/AdjointIndexSetM3.lean, core Int, lean-direct exit 0, sorry-free)

 adjoint_multiplicity_free / adjoint_dim_three / adjoint_palindromic / s_at_one_eq_three
 knot_independent_core_forces_unit_remainder  <- THE LOAD-BEARING ONE: any
     knot-independent core forces a knot-DEPENDENT remainder differing by exactly 1.
 adjoint_core_pins_remainder  -> under H_Ad the remainder is pinned to (0, 1).
 no_purely_knot_independent_count -> H_Ad alone is PROVABLY incomplete (derived, not
     conceded).

This converts the otherwise-unfalsifiable move "add one more state for 5_2" into a
structural requirement with a definite value.

## Part 2 (2026-08-18): is H_Ad just R1 again? -- answered, both ways

The adversarial objection was that H_Ad might be a re-description of Route A's
surviving reading R1 (DT integer = #boundary-parabolic SL_2(C) flat connections =
A-polynomial L-degree), since both hand back 3 for 4_1. Settled, using the certified
chirality-split data (4_1 amphichiral -> (S+,S-)=(3,3); 5_2 chiral -> (4,3)):

 NO, IT IS NOT (T5). R1 is the dtMax projection; H_Ad's core is dtMin. Different
   halves of the same datum. And the PAIR reconstructs the 2-element set {3,4} --
   which is NOT in tension with no_scalar_matches_chirality_split_datum, because that
   theorem excludes ONE scalar equalling a 2-set, not two scalars naming it between
   them. This is the sharpest positive structural statement M3 has produced.

 BUT THE EVIDENCE IS ONE DATA POINT (T6). 4_1's amphichirality collapses dtMin onto
   dtMax, so 4_1 gives NO evidence for H_Ad independent of R1. The entire support for
   "the core is knot-independently 3" is the single observation S-(5_2) = 3.

 AND A RIVAL SURVIVES (T7). H_floor: the core is the {0, g, gbar} triple that EVERY
   hyperbolic knot carries -- i.e. R1's own universal floor, with no sl_2 anywhere.
   Its core is also 3, so it imposes identical constraints and makes identical
   predictions; and its Chern-Simons values {0,+V,-V} give a palindromic 3-element
   grading too, so T4's shape screen cannot arbitrate either. The data CANNOT
   separate H_Ad from H_floor. Only the grading VARIABLE could (meridian x=m^2 vs
   Chern-Simons value); GGM's s(x) is written in the meridian variable, which weakly
   favours H_Ad -- "weakly" is the honest word.

 SELF-CORRECTIONS made at source (probe + Lean):
   - T2's note claimed R1 "fails precisely here" (knot-independence). WRONG, retracted.
     R1 hits the dtMax vector (3,4) exactly; its proved failure is single-valuedness
     against a set-valued datum. Conflating the two failure modes would have hidden T5.
   - The previously-proposed completion ("5_2 has one extra flat connection") IS R1.
     So that completion composes two imported readings; it derives nothing from Hecke
     data. Recorded so it is not later mis-sold as a derivation.

Lean added (same file, core Int, lean-direct exit 0, sorry-free): dtPlus / dtMinus /
dtMin / dtMax, r1_is_the_dtmax_projection, h_ad_is_the_dtmin_projection,
min_max_pair_reconstructs_datum, two_scalars_name_what_one_cannot,
fourone_is_a_degenerate_observation, h_ad_and_h_floor_are_indistinguishable,
palindromic_shape_does_not_arbitrate. Probe now 7/7 (T5/T6/T7 added).

## Part 3 (2026-08-18): route (b) DELIVERED -- the meridian grading is derived

Part 2 left exactly one discriminator between H_Ad and H_floor: the grading VARIABLE
(H_Ad grades by meridian eigenvalue x = m^2, H_floor by Chern-Simons value). Route
(b) -- get the meridian grading out of QOU-native Schur-Weyl data -- now lands:

 T9 The shape-(2) SEMISTANDARD Young tableaux over {1,2} are {11, 12, 22}, and their
    m-weights are (2, 0, -2) = exactly TWICE the adjoint x-exponents (1, 0, -1) --
    i.e. precisely the substitution x = m^2. So s(x) = x + 1 + 1/x is the character
    of S^(2)(C^2) IN THE MERIDIAN VARIABLE, read off Young-tableau combinatorics with
    nothing fitted. H_floor (Chern-Simons-graded) has no route to this.
 T10 The three tableaux carry three DISTINCT weights, so M2's sMultiplicities =
    [1,1,1] is now combinatorial rather than asserted.

SCOPE (a), stated plainly: this gives H_Ad a mechanism H_floor lacks. It does NOT
exclude H_floor -- "one hypothesis has a derivation the other lacks" is weaker and
different from "the other is refuted", and no exclusion is claimed.

 SECOND SELF-CORRECTION forced by doing this: Ad is the SCHUR-WEYL PARTNER of the
   partition-(2) Hecke block, NOT the block. #SYT((2)) = 1 (the H_2(q) block is
   ONE-dimensional); #SSYT((2)) = 3 (the partner S^(2)(C^2) on the U_q(sl_2) side of
   V^(x)2 = sum_lam S^lam(V) (x) M_lam). Earlier text in the Lean docstring, the
   probe docstring and this bean said "the partition-(2) Wedderburn block of H_2(q)"
   -- a conflation of the two sides of Schur-Weyl duality, corrected at all three
   sources. Both dimensions are now DERIVED in Lean (from the weakly- vs
   strictly-increasing filling conditions), so the distinction cannot be lost again.

Lean added: shapeTwoFillings / ssytShapeTwo / sytShapeTwo, ssyt_from_weakly_increasing,
syt_from_strictly_increasing, hecke_block_one_schur_partner_three,
ssyt_meridian_weights_are_twice_adjoint, ssyt_weights_nodup. Probe now 10/10.

## Part 4 (2026-08-18): the remainder is DERIVED -- and it goes AGAINST H_Ad

Went looking for third-knot Stokes data. Found something better and worse: the third
knot is already in the corpus, and it hands the count to the RIVAL.

Garoufalidis-Zagier (library/arxiv-2111.06645v3/2111.06645v3.pdf S2.1, glyph-verified) tabulate P_K, the
boundary-parabolic SL_2(C) reps, for three knots:

  K          reduced trace algebra              real  pairs  |P_K|  core  remainder
  4_1        Q(sqrt(-3)), imag. quadratic         0     1      3      3      0
  5_2        cubic, disc -23, signature (1,1)     1     1      4      3      1
  (-2,3,7)   Q(xi) x Q(eta), eta totally real    1+3    1      7      3      4

 |P_K| = 3,4,7 reproduces R1's (4_1,5_2)->(3,4) from a source INDEPENDENT of the
   A-polynomial, and extends it to a third knot.
 The remainder is the count of REAL EMBEDDINGS of the reduced trace algebra. 4_1's
   trace field is imaginary quadratic -> none -> remainder 0. 5_2's disc -23 cubic has
   exactly one -- GZ even name it, the root with zero imaginary part -> remainder 1.
 So the "+1" that Part 1's Lean could only FORCE (and that I wrote "any completion
   must derive independently") IS NOW DERIVED -- by H_floor, from arithmetic, with no
   sl_2 anywhere. H_floor explains the number AND the remainder; H_Ad's surviving
   distinct content is only the Part-3 meridian grading. Scored honestly: this is a
   point against my own hypothesis.

THIRD SELF-CORRECTION -- route (a) as I stated it last commit is WRONG, retracted.
I said a knot with MORE than 3 boundary-parabolic connections would break H_floor. It
would not: H_floor's core is the universal FLOOR {s0,g,gbar} = 3 for EVERY hyperbolic
knot, exactly as H_Ad's is dim sl_2 = 3. No third knot separates them at the core --
now PROVED on all three (core_is_three_on_all_three). What a third knot actually buys:
(i) a second non-degenerate data point against T6's one-observation problem, and
(ii) a ONE-SIDED falsification test of H_Ad's POLYNOMIAL claim -- if a rank-6 knot's
Stokes entries are not built from x+1+1/x, H_Ad breaks while H_floor cannot.

LITERATURE STATUS (measured, not assumed). All 371 corpus PDFs text-extracted and
swept; 47 mention "Stokes". GGM 2012.00062 and GGMW 2111.04763 treat ONLY 4_1 and 5_2
-- GGMW S1.4 is literally "Illustration with the two simplest hyperbolic knots", and
every 6_1/7_2 string in both is a page number. GZ 2111.06645 covers (-2,3,7) but for
perturbative series / quantum modularity: two occurrences of "Stokes", no matrices.
=> NO q->0 Stokes matrix for a third hyperbolic knot exists in the corpus. The
(-2,3,7) count 7 is therefore a PREDICTION of R1/H_floor, not a check.

Lean added: PKnot, realEmbeddings, complexPairs, pkSize, floorCore, floorRemainder,
pk_sizes_three_four_seven, remainder_is_arithmetic,
forced_remainder_is_the_real_embedding_count, pretzel_is_a_new_data_point,
core_is_three_on_all_three. Probe now 13/13.

## NEXT STEP (the open piece)

The old route (a) is retracted (see Part 4). What remains:
1. FALSIFY-OR-KEEP H_Ad's polynomial. Get the q->0 Stokes entries of a rank-6 knot
   ((-2,3,7) is the natural target, P_K already known). If they are not built from
   s(x) = x + 1 + 1/x, H_Ad is dead and H_floor is untouched. This is a ONE-SIDED
   test and it is the only cheap thing left that can move H_Ad. It is a LITERATURE
   ask that the corpus does NOT answer (see Part 4) -- it needs a source outside the
   371 uploads, i.e. real outbound search, which this sandbox's proxy currently
   denies (arxiv export API returns 403 CONNECT).
2. H_floor now outscores H_Ad on the count. If the aim is the best available account
   of the DT index set rather than defending H_Ad, the honest move is to develop
   H_floor's arithmetic rule (remainder = real-embedding count) and test its
   (-2,3,7) prediction of 7. Second remaining piece, unchanged: the extra 5_2 ray is R1,
so composing H_Ad with it derives nothing from Hecke data -- a genuine derivation
still needs the ray to come out of the Hecke side.

Until one lands: HYPOTHESIS ONLY, with a NAMED RIVAL that the data cannot exclude,
and no derivation of the DT spectrum from Hecke data claimed.

## Part 5 (2026-09-07): H_floor's inputs DERIVED for 4_1 and 5_2 (not a discriminator)

Part 4's rule (remainder = real-embedding count of the trace field) ran on GZ's transcribed table. The two fields this corpus derives itself (two_bridge_layered_nz_probe.py, #6985: x^2-x+1 for 4_1 from the Farey word R, theta^3-theta+1 for 5_2 from RL) now supply the signatures by proof: no real root (nlinarith) and exactly one real root (IVT on (-2,-1) + strict monotonicity below -1), QOU/QBeta/FloorRemainderFromDerivedShapeFields.lean, sorry-free; link theorems say AdjointIndexSetM3.realEmbeddings' 4_1/5_2 entries ARE those counts. Probe aomega_m3_floor_remainder_from_derived_shape_fields_probe.py (13/13) adds the Chern-Simons value sets of the Galois-conjugate structures by pushing every shape through every embedding: {+V,-V} for 4_1, {0,+V,-V} for 5_2 with the real embedding at volume exactly 0.

Scored honestly: this is PROVENANCE, not discrimination. Core is still 3 under both H_Ad and H_floor; (-2,3,7) is still not derived; nothing Hecke-side. It closes the "imported" caveat on Part 4 for the two knots the corpus owns. Audit: 2026-09-06-two-bridge-layering-from-farey-word.md §3c.

## Part 6 (2026-09-07): the THIRD knot's inputs DERIVED — Part 4's "prediction 7" is now a check

The ptolemy DB is still 403, but the (-2,3,7) N=2 ptolemy variety (SnapPy census m016 = K12n242 = Culler K3_1, 3 tets) has two obstruction classes of 3 variables each, and sympy's lex Groebner basis reduces them to c^3-c-1 (disc -23 = the 5_2 field Q(xi), one real root) and c^3+4c^2+3c-1 (disc 49, splits over Q(eta), three real roots). So |P_K| = 7, real embeddings 4, one complex pair, remainder 4 — GZ §2.1 reproduced from a held triangulation + exact algebra; R1's 7 = Culler L-degree 6 + 1 (K3_1 irreducible: one curve carries both fields). Probe aomega_m3_pretzel_remainder_from_ptolemy_probe.py (10/10); Lean PretzelRemainderFromPtolemy.lean (real-root counts proved, linked to realEmbeddings pretzel237 = 4). Audit §3e of 2026-09-06-two-bridge-layering-from-farey-word.md.

NEXT STEP unchanged in substance: item 1 (a rank-6 knot's q->0 Stokes entries) is STILL not held — GZ 2111.06645 §4.2 say they cannot give explicit Habiro formulas for (-2,3,7); GGM 2012.00062 §1.5 note its level is 2 (entries in q^{1/2}), so the s(x) test must be restated at level 2 before it can be run. An external plan claiming GZ print 6x6 Habiro matrices for the pretzel was checked against the held text and is wrong; the pretzel has six non-abelian reps, not five.

## Part 7 (2026-09-07, owner "2y"): the pretzel's Stokes data, derived as far as GGM's conjecture allows

GGM 2012.00062 §1.4 (held): S^+(x;q) is the rotated-index matrix (Ind^rot(j-i, q^{(j+i)/2}x; q)) only UP TO GL(r, Z(x,q)) on both sides; S^+_{sigma1 sigma1}(x;q) = Ind^rot(0,x;q) exactly. The corpus GHHR engine on SnapPy's m004/m015/m016 reproduces GGM (102) for 5_2 exactly (gate; convention e = meridian, m = longitude; read two orders below the computed order or the top order lies: 91 vs 90). The pretzel family Ind^rot(m,zeta;q), m=-2..2, is DERIVED to q^3 (probe aomega_m3_rotated_index_three_knots_probe.py, 17/17). In s = zeta+1+1/zeta the m=0 coefficients are: q^1: -(s-1)(s+1) / -s(s+1) / -2(s+1) for 4_1 / 5_2 / (-2,3,7); q^2: -s^2 / s(s^2-2s-2) / s^2-s-3; q^3: s^2(s^2-2s-1) / s^4-2s-1 / 5s^2+2s-1.

CONSEQUENCE FOR ITEM 1: "are the Stokes entries built from s(x)?" is a statement about entries in GGM's holomorphic-block basis, which the pretzel lacks in print; the derivable object is the family up to GL(r,Z(x,q)). So item 1 CANNOT BE RUN AS POSED. Replacement (open): a basis-invariant restatement of H_Ad — a property of the Z(x,q)-module generated by the rotated-index family, or of the exact sigma1sigma1 entry — that reduces to s(x) at 4_1/5_2. The (s+1) common factor at order q^1 is recorded, not interpreted (it fails to persist at q^2 for 4_1). Audit §3f.

## Part 8 (2026-09-07): CORRECTION of Part 7's framing, and the tranche that actually answers item 1

Part 7 said item 1 is "not GL-invariant as posed" (also PR #7101's title, audit §3f's first draft, and my rtec append). Overstated: S^+(x;q) is canonical once the Borel rays are ordered by volume, so "are its q->0 entries built from s(x)?" is well-posed. What is NOT invariant is Conjecture 4's identification index-matrix -> S^+ (up to GL(r,Z(x,q)) both sides); for unipotent S^+ every Fitting invariant is trivial, so the index fixes only the exact sigma1-sigma1 entry. Correct statement: the question is well-posed; the INDEX route cannot answer it; the BLOCK route can — Ind^rot(m,zeta;q) = sum_alpha B^alpha(q^{m/2}zeta;q) B^alpha(q^{m/2}/zeta;1/q) (GGM eq 19), with the blocks from the state integral of the triangulation. For m016 that is a 2-dim state integral at level 2 (GZ §4.2 declined the closed form). Held method: Garoufalidis-Kashaev arxiv-1304.2705 (state integrals -> q-series), arxiv-1411.6062; corpus instance for 4_1: qbeta_m1_rotated_index_from_blocks.py. Audit §3f corrected in place. Contamination list: PR #7101 title/body (merged; cannot edit the commit), issue #7100 (noted), bean qou-rtec (append), this bean's Part 7.

Part 9 (2026-09-08): the sister hypothesis (pretzel = (1,3) member of the GK 1-dim family, q<->q~ swap of 5_2) is REFUTED in the 5_2 configuration by the derived index — the swap is invisible in sigma1-sigma1, so the candidate reproduces 5_2's index, not the pretzel's. Item 1 still needs the pretzel's blocks; the 1-dim shortcut is closed in this configuration. qou-x3iv, audit §3g.

Part 10 (2026-09-13): the pretzel's state integral is one-dimensional with factor vector (1,1,2) (one dilogarithm at doubled argument) — derived from DG 2.7/5.2 + SnapPy; explains Part 9's refutation and GGM's level 2. Route to item 1 is now concrete: reduce, residue-evaluate, certify against the index. qou-x3iv Parts 11-12; audit §3h.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 57 Progress (PR litlfred/qou#8286)
- Status updated to `in-progress` (`litlfred/qou#8286`, C1 `6c7a20f3289e7e0671ce65ef402e1a06fd77c443`, C2 `dce9c51d4a6cd8f2253c078180b4b77a6f7c1ed0`).
