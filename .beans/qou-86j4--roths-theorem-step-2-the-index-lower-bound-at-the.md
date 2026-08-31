---
# qou-86j4
title: 'Roth''s theorem step 2: the index lower bound at the rational point'
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:22:03Z
updated_at: 2026-08-30T07:18:41Z
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

## 2026-08-30 -- the Z-coefficient case of step 2 is complete end to end

qou-jm52 delivered the analytic half and is closed. Composed with this bean's arithmetic half,
step 2 now runs end to end FOR RATIONAL-INTEGER COEFFICIENTS:

  le_index_rational_of_taylor (RothIndexGap) : P over Z with large index at alpha, p_h/q_h close
  to alpha, and one numeric inequality  ==>  the index at the rational point is at least nu.

Non-vacuity checked by le_index_rational_of_taylor_witness. The numeric inequality is qou-ujl8.

WHAT IS LEFT ON THIS BEAN is exactly the coefficient ring. Step 1's auxiliary polynomial has
coefficients in O_K, and the denominator argument used here -- a non-zero rational integer has
absolute value at least 1 -- becomes |N(x)| >= 1 for a non-zero algebraic integer, which needs
beta's conjugates as well as beta. That is a different proof, not a generalisation of this one,
and it has been kept unconflated with the Z case from the start.

## 2026-08-30 -- the O_K case is done. QOU/Mathlib/RothAlgebraicInteger.lean

Eight declarations, all axiom-clean, .olean deleted first, registered in QOU.lean.

WHY IT IS A DIFFERENT THEOREM, not a generalisation. Over Z the whole argument rests on "a
non-zero integer has absolute value at least 1", so smallness at the one place forces vanishing.
Over O_K that is FALSE -- an algebraic integer can be as small as you like at a given archimedean
place. What survives is the product over all places, |N(x)| >= 1, and the consequence changes
shape: x may be tiny at phi_0 and enormous elsewhere with the product still at least 1. Vanishing
needs smallness at phi_0 AND a bound at every OTHER conjugate, traded quantitatively as

    ||phi_0 x|| * M^{d-1} < 1  ==>  x = 0     (eq_zero_of_norm_mul_pow_lt_one)

So the O_K argument takes an input the Z argument does not. Keeping them as two theorems with
different hypotheses was the right call from the start; a single statement covering both would
have had to carry the conjugate bound vacuously in the Z case.

WHAT MATHLIB HAD AND WHAT IT DID NOT. Algebra.norm_eq_prod_embeddings gives N(x) = prod_sigma
sigma(x) over K ->a[Q] C, and Algebra.norm_ne_zero_iff gives N(x) /= 0. Neither the product over
K ->+* C -- the indexing house is stated against -- nor 1 <= prod_phi ||phi x|| is available;
prod_norm_embeddings_eq_abs_norm and one_le_prod_norm_embeddings build them.
NumberField.InfinitePlace.prod_eq_abs_norm is the same identity re-indexed by infinite places with
multiplicities, which is the wrong shape here: house is a max over EMBEDDINGS, so re-indexing by
places would have to be undone immediately. Checked before writing rather than after.

norm_le_house is the bridge from step 1's height estimate (stated with house) to the
per-embedding bounds the vanishing criterion consumes -- so the conjugate bound the O_K case needs
is exactly what step 1 already produces, and no new estimate is required.

THE DENOMINATOR ARGUMENT IS REUSED VERBATIM. The rational-point translateMatrix entries are
rational, so exists_int_mul_translateMatrix (proved for the Z case) applies unchanged;
exists_ringOfIntegers_mul_coeff_translate only changes what those integers are multiplied against.
le_index_of_norm_lt is then step 2's index lower bound over O_K.

## Summary of Changes

Step 2 of Roth's theorem, both halves and both coefficient rings.

  * ARITHMETIC HALF over Z (QOU/Mathlib/RothRationalIndex.lean): denominator dividing
    prod q_h^{r_h}, small implies zero, index lower bound. translateMatrix_half_witness shows the
    scaling is attained.
  * ANALYTIC HALF (RothTaylorBound, RothIndexGap; bean qou-jm52, closed): Taylor about alpha, the
    per-coordinate size bound after the single-G form proved true and useless, the height budget,
    and S = exp(-K(mu-nu)) from r_h T_h >= K. le_index_rational_of_taylor with a non-vacuity
    witness.
  * O_K COEFFICIENTS (RothAlgebraicInteger, this entry): |N(x)| >= 1 in place of |z| >= 1, and
    le_index_of_norm_lt.

## Deferred, with a home

le_index_of_norm_lt takes the per-embedding smallness as a hypothesis, exactly as its Z sibling
takes |coeff| < 1/prod q^r. Supplying it for the O_K case means running the Taylor estimate at
phi_0 and the trivial house bound at the other conjugates -- mechanical given RothTaylorBound and
norm_le_house, but it is assembly, and assembly is qou-br3w.

