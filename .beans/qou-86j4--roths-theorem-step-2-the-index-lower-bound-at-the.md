---
# qou-86j4
title: 'Roth''s theorem step 2: the index lower bound at the rational point'
status: in-progress
type: task
created_at: 2026-08-30T03:22:03Z
updated_at: 2026-08-30T03:22:03Z
---

Step 1 (auxiliary polynomial) is done in qou-qi0t. Step 2: if P has large index at (alpha,...,alpha) and p_h/q_h approximate alpha very well, then P has a substantial index at the rational point too. Mechanism: the Taylor coefficients of P at (p_1/q_1,...,p_m/q_m) have denominators dividing prod q_h^r_h, and are small because the index at alpha is large; small plus bounded denominator forces zero. RothHeightBound has the one-variable case and points the other way (vanishing implies height), so the multivariate denominator bound is new. Child of qou-br3w.

## 2026-08-30 -- arithmetic half landed

QOU/Mathlib/RothRationalIndex.lean, seven declarations, all axiom-clean
[propext, Classical.choice, Quot.sound], built with the .olean deleted first:

  * eq_zero_of_abs_lt_of_den -- a rational with denominator dividing D is 0 or >= 1/D;
  * exists_int_sum -- a finite sum of integer-valued rationals is an integer;
  * exists_int_mul_translateMatrix -- (prod_h q_h^{n_h}) * translateMatrix (p/q) i n is in Z,
    by peeling one X_j at a time, exactly as the height bound peels;
  * translateMatrix_half_witness -- = 1/4 at beta = 1/2, n = 2, so the prod q_h^{n_h} scaling
    is ATTAINED and could not have been lowered;
  * exists_int_mul_coeff_translate -- the degree bound r converts the per-monomial scaling
    into one scaling for the whole polynomial;
  * coeff_translate_eq_zero_of_abs_lt -- small forces vanishing;
  * le_index_of_abs_lt -- and enough vanishing is a lower bound on the index.

The analytic half (Taylor smallness) is split out as qou-jm52 and is stated there in full,
including which normalisation it needs. Splitting first was deliberate: it gives the
bookkeeping a fixed target instead of letting it be invented alongside its own consumer,
which is how correction 26 (Theta-form halves that did not compose) got in.

TWO THINGS THIS DOES NOT CLAIM.
  1. Coefficients are rational integers, P : MvPolynomial (Fin m) Z. The step-1 auxiliary
     polynomial has coefficients in O_K. For that case "small implies zero" is |N(x)| >= 1
     for a non-zero algebraic integer, not |z| >= 1 for a rational integer, and it needs the
     conjugates of beta as well. Not proved, not conflated with the Z case.
  2. Nothing here evaluates a derivative of P; the index is used only through
     le_index_iff_coeff_eq_zero.

