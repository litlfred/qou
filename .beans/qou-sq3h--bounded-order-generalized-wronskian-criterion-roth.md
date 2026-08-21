---
# qou-sq3h
title: Bounded-order generalized Wronskian criterion (Roth's lemma blocker)
status: todo
type: task
created_at: 2026-08-21T15:21:57Z
updated_at: 2026-08-21T15:21:57Z
---

Roth's lemma needs a generalized Wronskian whose operators have bounded order; the criterion proved in qou-br3w supplies none. Route: generic line + the univariate criterion already proved. See body.

Child of `qou-br3w`. Blocks Roth's lemma; nothing else in that epic can proceed past it.

## What is needed

> `f₁ … f_m ∈ K[x₁…x_n]` linearly independent over `K` (char 0) ⟹ there is a generalized
> Wronskian `det (Δᵢ fⱼ) ≠ 0` with **`ord (Δᵢ) < i`**.

`QOU/Mathlib/MvGenWronskian.lean` proves the criterion **without** the order bound
(`linearIndependent_iff_exists_mvGenWronskian_ne_zero`). Roth's lemma consumes the bounded
version, because the order bound is what ties the Wronskian's degree to the degrees of the
auxiliary polynomial. Without it the index estimate has nothing to bound.

## ⚠ The existing proof cannot be sharpened into this — witnessed, not asserted

`exists_mvGenWronskian_ne_zero` argues *the Wronskian is non-zero because it is non-zero at
the origin*. Two computations in that file show the technique is structurally incapable of
producing bounded-order families:

- `mvGenWronskian_pow_five_six` — for `(x⁵, x⁶)` the **order-one** family `(id, ∂/∂x₀)`
  gives Wronskian `x¹⁰ ≠ 0`. So the bound is achievable.
- `mvGenWronskian_pow_five_six_constantCoeff` — that same Wronskian is **zero at the
  origin**. So the origin argument cannot return it; it must reach for operators of order
  ≥ 5 to see the `x⁵` coefficient.

Do not attempt to patch the coefficient/origin proof. A different argument is required.

## The classical route, and what it needs

Restrict to a **generic line**: `gⱼ(t) = fⱼ(a + tc)`.

1. For generic `(a, c)` the `gⱼ` stay linearly independent over `K`. Needs: a non-zero
   polynomial over an **infinite** field has a point where it does not vanish. Applied to
   the finitely many non-zero combinations that must survive.
2. The **univariate** criterion is then the engine, and it is already proved —
   `genWronskian_eq_zero_iff` in `QOU/Mathlib/GenWronskian.lean`. Its operators are
   `dⁱ⁻¹/dtⁱ⁻¹`, which already carry the order bound.
3. `d/dt` pulls back to `Dᶜ = ∑ᵢ cᵢ ∂ᵢ`, of order exactly one, so `Dᶜ^{i-1}` has order
   `i-1` — the bound, for free.
4. Expand `det (Dᶜ^{i-1} fⱼ)` by multilinearity of `det` over the monomials of `Dᶜ^{i-1}`;
   some term is non-zero, and each term is a bounded-order generalized Wronskian.

So the missing pieces are the genericity argument (1) and the multilinear expansion (4);
(2) and (3) are in hand.

**Measured, not assumed:** the genericity input for (1) is already in Mathlib —
`MvPolynomial.funext` / `funext_iff` (`Mathlib/Algebra/MvPolynomial/Funext.lean`), for
polynomials over an **infinite integral domain**. Its contrapositive is exactly "a non-zero
polynomial has a point where it does not vanish". So (1) is a matter of applying it to the
right finite family, not of building the machinery.

⚠ A definitional mismatch to plan for in (4): `Dᶜ^{i-1}` is a *linear combination* of
monomial operators, whereas `mvGenWronskian` takes `D : Fin m → List σ`, i.e. monomial
operators only. The expansion is what converts one to the other; it is not optional
book-keeping, it is how the result lands in the committed shape.

## Already available

- `genWronskian_eq_zero_iff` — the univariate criterion, both directions.
- `eq_C_of_pderiv_eq_zero` — a polynomial killed by every partial is constant (char 0).
  Mathlib gap, proved in `MvGenWronskian.lean`.
- `coeff_pderiv`, `coeff_pderiv_of_pos`, `pderivList`, `multiIndexOf` and friends.

## An easier sub-target, if the full induction stalls

`m = 2` bounded order: `f₁, f₂` independent ⟹ `∃ j, f₁ ∂ⱼf₂ − f₂ ∂ⱼf₁ ≠ 0` (order ≤ 1).
Provable directly via the UFD structure of `MvPolynomial σ K` (Mathlib has the instance for
arbitrary `σ`): divide by the gcd, coprimality forces `p ∣ ∂ⱼp`, degree forces `∂ⱼp = 0`,
and `eq_C_of_pderiv_eq_zero` finishes.

`degreeOf_pderiv_lt` (`degreeOf j (pderiv j p) < degreeOf j p`) was the missing sub-lemma
and is now **proved** in `MvGenWronskian.lean` — another measured Mathlib gap, filled.

⚠ What that sub-target still needs, and it is not small: `p ∣ r` with `r ≠ 0` implies
`degreeOf j p ≤ degreeOf j r`, which needs `degreeOf j (f*g) = degreeOf j f + degreeOf j g`
over a domain. Mathlib has only `degreeOf_mul_le`, the wrong direction. Plus the UFD
coprimality step (`p ∣ q * r`, `gcd p q = 1` ⟹ `p ∣ r`) — note `IsCoprime` in Mathlib is
Bezout-flavoured and **does not hold** for `x, y` in `MvPolynomial`, so this must go through
`UniqueFactorizationMonoid`, not `IsCoprime`.
