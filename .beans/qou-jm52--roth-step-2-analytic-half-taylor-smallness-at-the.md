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
