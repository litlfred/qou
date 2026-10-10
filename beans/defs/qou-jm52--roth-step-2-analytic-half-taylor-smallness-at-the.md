---
# qou-jm52
title: 'Roth step 2, analytic half: Taylor smallness at the rational point'
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:33:40Z
updated_at: 2026-08-30T06:20:42Z
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

## 2026-08-30, same day -- CORRECTION to the entry above: one G is not enough

seminorm_translateMatrix_le_pow bounds the entry by 2^{|n|} * G^{|n| - |i|}: a SINGLE G, and the
UNWEIGHTED degree difference. I wrote it, landed it, and it cannot feed the argument.

The index hypothesis at alpha gives idxWeight r n >= mu, and the conclusion is wanted for
idxWeight r i < nu. idxWeight is weighted by 1/r_h. In Roth's regime the r_h are wildly unequal
BY CONSTRUCTION -- RothGrowth forces r_{h+1} much smaller than r_h, that is the whole point of
the ladder -- so a lower bound on the WEIGHTED difference gives no lower bound whatever on
sum_h (n_h - i_h). The statement is true; it is useless.

seminorm_translateMatrix_le_prod is the same induction tracking prod_h G_h^{n_h - i_h}, one G_h
per coordinate, which is what pairs with |beta_h - alpha| <= q_h^{-(2+delta)} and r_h log q_h ~ L.
abs_translateMatrix_le_prod and abs_coeff_translate_add_le_prod are the real instances.

The weaker lemma is KEPT, with the reason recorded in the module header. Deleting it would hide
that the first attempt at this estimate produced something true and unusable -- which is the same
failure mode as correction 24 (a weaker-but-true bound that cost an exponent) and correction 26
(halves that were each correct and did not compose). The build was green, the axioms were clean,
and no witness would have caught it; what caught it was writing down what the consumer needs
before writing the consumer.

Item 3 of the remaining list is unchanged and is now the only real obstacle: turning the weighted
index gap into prod_h q_h^{-(2+delta)(n_h - i_h)} under r_h log q_h ~ L. Items 1-2 (height budget,
term count) remain elementary and unblocked.

## 2026-08-30 -- items 1 and 2 done; only the logarithms remain

abs_coeff_translate_le -- the height budget for a translate: |coeff n (translate alpha P)| <=
prod_h (r_h + 1) * H * (2B)^{sum r_h}, the multivariate analogue of WronskianHeight's budget.
That subsumed item 2 (the term count) rather than needing it separately: the count enters as
card_support_le_prod_succ, which existed for MvPolynomial sigma Z and is now generalised to an
arbitrary CommSemiring -- nothing in its proof was arithmetic, it is a statement about which
multi-indices can occur. All seven dependent modules rebuilt clean.

abs_coeff_translate_add_le_index -- everything folded in: the index hypothesis at alpha restricts
the sum, the degree bound counts it, the height bound sizes each term, and S is a uniform bound
on prod_h G_h^{n_h - i_h} over the surviving multi-indices, taken as a hypothesis.

WHAT IS LEFT is exactly one thing: produce S. Under r_h log q_h ~ L and G_h <= q_h^{-(2+delta)},
sum_h (n_h - i_h)/r_h >= mu - idxWeight r i gives S ~ exp(-(2+delta) L (mu - idxWeight r i)).
That is the only piece of step 2 that needs real logarithms, and it is where the parameter
record shared with RothGammaProducer should live. Then S is compared against
1/prod q_h^{r_h} and fed to le_index_of_abs_lt, and step 2 closes.

## 2026-08-30 -- S produced; step 2 closes. QOU/Mathlib/RothIndexGap.lean

Eight declarations, all axiom-clean, .olean deleted first.

THE ONE CONVERSION. Two weightings meet and neither dominates the other on its own. The index
gap is weighted by 1/r_h: idxWeight r n >= mu and idxWeight r i <= nu give
sum_h (n_h - i_h)/r_h >= mu - nu, and NOTHING about sum_h (n_h - i_h). The sizes are weighted by
log q_h: prod_h G_h^{n_h - i_h} = exp(-sum_h (n_h - i_h) T_h) with T_h = -log G_h. The hypothesis
r_h * T_h >= K is exactly the bridge:

  sum_h (n_h-i_h) T_h = sum_h [(n_h-i_h)/r_h] (r_h T_h) >= K sum_h (n_h-i_h)/r_h >= K(mu-nu).

So S = exp(-K(mu-nu)) -- prod_pow_le_exp. This is Roth's normalisation r_h log q_h ~ L in the
only form the estimate needs, and it is why the degrees must be chosen FROM the heights rather
than freely; the same fact RothGammaProducer discharges for Gamma_m's growth clause.

Truncated subtraction turned out to be free: translateMatrix's exponents are n_h - i_h truncated,
truncation only RAISES them, and G_h <= 1 makes a larger exponent a smaller product. Worth
recording because the opposite is easy to assume -- had the estimate needed an upper bound on the
exponents, truncation would have been an obstruction rather than a convenience.

le_index_rational_of_taylor is step 2 with ONE hypothesis left, and that hypothesis is a numeric
inequality between explicit quantities -- no polynomial, no index, no expansion in it. The
ZZ -> QQ -> RR transfer (coeff_translate_cast) is what lets the RR-side estimate feed the QQ-side
denominator argument of le_index_of_abs_lt.

NON-VACUITY CHECKED. le_index_rational_of_taylor_witness discharges all twelve hypotheses at
m = 1, r = (1), P = x, alpha = 0, p/q = 0/1, K = 8, mu = 1, nu = 1/2, where hfinal comes down to
16 e^{-4} < 1. Twelve hypotheses several of which are inequalities between constructed quantities
is exactly the shape in which a theorem is true because nothing satisfies it.

WHAT THE WITNESS DOES NOT SHOW: gamma = beta - alpha is 0 there, so the Taylor machinery is not
exercised. A gamma /= 0 witness is NOT available at small m -- I checked: at m = 1 with
P = 2x - 1, alpha = 1/2, beta = 0 the constants give 32 e^{-K(1-nu)} with K <= log 2, so the left
side is >= 16 and never beats 1. The constants only fall below prod q_h^{-r_h} when m is large
and the approximation exceptionally good, which IS Roth's inequality and hence step 4's business.
Recorded rather than papered over.

REMAINING for step 2 as a whole: only the coefficient ring. This file is ZZ-coefficient; the
step-1 auxiliary polynomial is over O_K, where "small implies zero" is |N(x)| >= 1 for a non-zero
algebraic integer and needs beta's conjugates. Tracked on qou-86j4, not conflated with this.

## Summary of Changes

The analytic half of step 2 is delivered. QOU/Mathlib/RothTaylorBound.lean (14 declarations) and
QOU/Mathlib/RothIndexGap.lean (8 declarations), all axiom-clean, each built with the .olean
deleted first, both registered in QOU.lean.

  * translate_translate / coeff_translate_add -- Taylor about alpha in the form the argument needs.
  * seminorm_translateMatrix_le_prod -- the per-coordinate size bound, after the single-G form
    turned out to be true and useless against a 1/r_h-weighted index (correction kept in place,
    not deleted).
  * abs_coeff_translate_le -- the height budget; card_support_le_prod_succ generalised from Z to
    any CommSemiring to serve it.
  * prod_pow_le_exp -- S = exp(-K(mu-nu)), from r_h T_h >= K. This is the one conversion the
    whole step turns on.
  * le_index_rational_of_taylor -- step 2, with a single numeric hypothesis left over, now
    tracked as qou-ujl8.
  * le_index_rational_of_taylor_witness -- all twelve hypotheses discharged at m = 1, so the
    bundle is satisfiable and the conclusion non-vacuous. Its limits are stated in its docstring
    rather than left implicit: gamma = 0 there, and no gamma /= 0 witness exists at small m.

Deferred, both with homes: the numeric inequality -> qou-ujl8 (step 4); the O_K coefficient ring
-> qou-86j4, where "small implies zero" becomes |N(x)| >= 1 and needs beta's conjugates.

