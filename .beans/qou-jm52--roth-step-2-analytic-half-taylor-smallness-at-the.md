---
# qou-jm52
title: 'Roth step 2, analytic half: Taylor smallness at the rational point'
status: todo
type: task
created_at: 2026-08-30T03:33:40Z
updated_at: 2026-08-30T03:33:40Z
---

`le_index_of_abs_lt` (QOU/Mathlib/RothRationalIndex.lean) discharges the arithmetic half of
step 2 and takes the smallness of the low-weight translated coefficients as a HYPOTHESIS:

    |coeff i (translate beta P)| < 1 / prod_h q_h^{r_h}   for all i with idxWeight r i < mu.

This bean supplies it. The route is the Taylor identity

    translate beta P = translate (beta - alpha) (translate alpha P),

so coeff i (translate beta P) = sum over n of coeff n (translate alpha P) * translateMatrix
(beta - alpha) i n. The index hypothesis at alpha kills every n with idxWeight r n < mu, and
translateMatrix (beta - alpha) i n vanishes unless i <= n; so the surviving terms all have
sum_h (n_h - i_h)/r_h >= mu - idxWeight r i > 0.

What each surviving term costs:
  * |coeff n (translate alpha P)| <= (height of P) * 2^{sum r_h}   -- the translate of a
    bounded-height polynomial, the multivariate version of WronskianHeight's budget;
  * the binomials prod_h C(n_h, i_h) <= 2^{sum r_h};
  * the number of terms <= prod_h (r_h + 1) <= 2^{sum r_h};
  * prod_h |beta_h - alpha|^{n_h - i_h} <= prod_h q_h^{-(2+delta)(n_h - i_h)}, which under the
    standard normalisation r_h * log q_h ~ L is <= exp(-(2+delta) L (mu - idxWeight r i)).

So the whole thing needs real logarithms and the r_h * log q_h ~ L bookkeeping -- the same
normalisation RothGammaProducer already builds for the Gamma_m clauses, which is why the two
should be written against a shared parameter record rather than each inventing its own.

NOT started. Blocked on nothing; it is simply the next sizeable piece. Child of qou-86j4.

## 2026-08-30 -- the two hard-edged pieces landed

QOU/Mathlib/RothTaylorBound.lean, seven declarations, all axiom-clean, .olean deleted first:

  * translate_translate / coeff_translate_add -- Taylor's theorem in the only form the
    argument needs. The coefficients at alpha+gamma are a translateMatrix gamma-combination
    of the coefficients at alpha, so an index hypothesis at alpha simply deletes the
    low-weight terms of the expansion.
  * seminorm_translateMatrix_le_pow -- f(T(i,n)) <= 2^{|n|} * G^{|n| - |i|} for f o gamma
    <= G <= 1, with truncated subtraction. abs_translateMatrix_le_pow is the real instance.
  * abs_coeff_translate_add_le -- the two composed, as a single sum bound so the index
    hypothesis can be applied to it directly.

NOT reusing seminorm_translateMatrix_le was the point. Its (2B)^{|n|} is right for step 1
(alpha fixed, matrix small) and wrong here: step 2's entire content is that gamma = beta -
alpha is TINY, and (2G)^{|n|} discards that by not separating the |i| that the gamma^{n-i}
factor does not carry. Same peeling, different quantity tracked through it -- exactly where
"reuse the lemma, it's about the same object" would have cost the argument its exponent.

G <= 1 is load-bearing, not cosmetic: without it the induction fails at |i| = |n|, where the
truncated exponent has collapsed to G^0 and the step needs 1 + G <= 2 instead of the equality
it gets below the collapse. The alternative is a second induction proving the entry vanishes
for |i| > |n|; G <= 1 is free in every application.

mul_pow_sub_le was written with 0 <= G and the linter reported it unused. It is: below the
collapse the two sides are EQUAL, so no sign condition is needed. Stronger statement kept.

WHAT REMAINS on this bean:
  1. bound |coeff n (translate alpha P)| by the height of P times 2^{sum r_h} -- the
     multivariate analogue of WronskianHeight's budget;
  2. bound the number of surviving terms by prod_h (r_h + 1);
  3. turn sum_h (n_h - i_h)/r_h >= mu - idxWeight r i into
     prod_h |beta_h - alpha|^{n_h - i_h} <= exp(-(2+delta) L (mu - idxWeight r i))
     under r_h * log q_h ~ L -- this is the piece that needs real logarithms;
  4. compare the product against 1/prod q_h^{r_h} and feed le_index_of_abs_lt.

Steps 1-2 are elementary and unblocked. Step 3 is the parameter bookkeeping and should share
a record with RothGammaProducer rather than inventing its own normalisation.

