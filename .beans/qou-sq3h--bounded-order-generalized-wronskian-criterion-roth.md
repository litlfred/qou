---
# qou-sq3h
title: Bounded-order generalized Wronskian criterion (Roth's lemma blocker)
status: completed
type: task
priority: normal
created_at: 2026-08-21T15:21:57Z
updated_at: 2026-08-21T16:24:08Z
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

---

## Progress, 2026-08-21 — steps 2 and 3 done, the gap is now one sentence

Two new modules, both sorry-free on the standard axiom set:

- `QOU/Mathlib/LineRestriction.lean` — `lineRestrict`, `dirDeriv`, the chain rule
  `d/dt f(a+tc) = (Dᶜf)(a+tc)` and its iterate, `eval_zero_lineRestrict`,
  `exists_lineRestrict_ne_zero`.
- `QOU/Mathlib/DirectionalWronskian.lean` — `dirGenWronskian c f = det ((Dᶜ)ⁱ fⱼ)`, the
  pullback across `lineRestrict`, and the equivalence below.

### The result that reshapes the problem

```
dirGenWronskian c f ≠ 0  ↔  ∃ a, the restrictions along t ↦ a + tc are independent over K
```

Both directions proved. **The base point drops out of the problem.** Step 1 of the route as
originally written asked for a generic *line* — a base point and a direction. It only ever
needed the direction:

```
f independent over K   ⟹   ∃ c, dirGenWronskian c f ≠ 0
```

The reverse direction needed `exists_lineRestrict_ne_zero`, and the shape of that lemma is
the reason the base point is free: the constant term of `lineRestrict a c P` is `P(a)`, so
**any** `a` off the zero set of `P` works, in **every** direction. Genericity was only ever
needed in `c`.

### ⚠ What is open, stated honestly

Finding a good direction is a genericity statement over the space of directions, and the
naive argument does not close it. For each *fixed* non-zero `p ∈ span f` the set of bad `c`
is a proper subspace — but `span f` is infinite, so there is no finite union to take. This
needs a real argument (a dimension count, or an induction on the number of variables), not
an assembly of what is already here.

### Then, still

**Multilinear expansion.** `(Dᶜ)ⁱ` is a linear combination of monomial operators of order
`i`, whereas `mvGenWronskian` takes `D : Fin m → List σ` — monomial operators only. The
useful direction is the contrapositive (if every bounded-order generalized Wronskian
vanishes then `dirGenWronskian c f = 0` for every `c`), which needs only multilinearity of
`det` in its rows — **not** a multinomial theorem for `(∑ cᵢ ∂ᵢ)ⁱ`. Worth noting because the
multinomial route looks necessary and is not.

---

## 2026-08-21, later — `m = 2` is done, and there are now TWO routes

`QOU/Mathlib/BoundedOrderWronskian.lean`:

```
f, g independent over K  ⟹  ∃ k, mvGenWronskian ![[], [k]] ![f, g] ≠ 0
```

The family `(id, ∂ₖ)` has orders `0, 1` — exactly `ord (Δᵢ) ≤ i`. So the bounded-order
criterion, in the committed shape, **holds outright at `m = 2`**.

### ⚠ Route B, which avoids genericity, and is probably the one to try

The `m = 2` case is not just a sub-target — it is *precisely the base case* that the
univariate general-`m` converse already in this repo is built on.
`Polynomial.exists_dependence_of_genWronskian_eq_zero` runs:

1. kernel vector from the vanishing determinant,
2. derivative descent (`sum_derivative_of_forall_sum_eq_zero`),
3. the Wronskian combination `c_l ∂c_j − c_j ∂c_l` — kills one entry **without dividing**,
4. the `m = 2` converse, consumed at step 3's output,
5. substitution.

Every step has a bounded-order multivariate analogue. The reason it should go through: the
contradiction hypothesis is *"**every** bounded-order Wronskian vanishes"*, which is exactly
what makes the cofactor expansion valid for an **arbitrary** last operator `Δ` with
`ord Δ ≤ m−1`. Descent then works because `ord (∂ₖ ∘ Δ) ≤ m−1` whenever `ord Δ ≤ m−2`.

**This route needs no genericity at all** — no generic direction, no generic point, no
infinite-field argument.

⚠ Written down as a plan, not a theorem. The analogy could fail where the univariate proof
uses the canonical operator `dⁱ/dxⁱ` while the multivariate family is chosen. Try it before
Route A.

### Route A (generic direction) — still recorded, now the fallback

`DirectionalWronskian` reduces it to `∃ c, dirGenWronskian c f ≠ 0`, with the base point
already eliminated. Still blocked on a genericity statement over the space of directions.
Keep it: if Route B's analogy breaks, this is where to return.

### Newly available

- `exists_bounded_order_mvGenWronskian_two` — the base case.
- `totalDegree_pderiv_lt` **and** `degreeOf_pderiv_lt`. Not duplication: `totalDegree` is the
  one that pairs with Mathlib's `totalDegree_mul_of_isDomain`, which has no `degreeOf`
  counterpart.
- `eq_C_of_pderiv_eq_zero`, `coeff_pderiv`, `coeff_pderiv_of_pos`.

⚠ **`IsCoprime` is the wrong notion** for any of this. It is Bézout-flavoured and is **false**
for `x, y` in `MvPolynomial` despite their sharing no non-unit factor. Everything must go
through `UniqueFactorizationMonoid` / `IsRelPrime`. Reaching for `IsCoprime` is the natural
first move and it does not work.

---

## Summary of Changes — DONE, 2026-08-21

```
LinearIndependent K f  ↔  ∃ D, (∀ i, |D i| ≤ i) ∧ mvGenWronskian D f ≠ 0
```

Both directions, characteristic zero. This is the certificate Roth's lemma consumes, and it
is what this bean was opened for. `QOU/Mathlib/BoundedOrderWronskian.lean`, 11 declarations,
sorry-free, standard axiom set.

**Route B is the one that worked**, transposing the univariate general-`m` converse:
`m = 2` base case → derivative descent → Wronskian combination → collapse to constants → the
induction.

### ⚠ The doubt recorded against Route B was wrong, and the reason matters

The earlier note warned the analogy might fail where the univariate proof uses the canonical
operator `dⁱ/dxⁱ` while the multivariate family is chosen. It does not fail. The hypothesis
is that **every** bounded-order Wronskian vanishes, so the cofactor expansion is available
for an **arbitrary** last operator with `ord ≤ m−1` — and being free to vary that operator is
exactly what replaces canonicity. Descent then works because
`ord (∂ₖ ∘ Δ_l) = |l| + 1 ≤ m−1` whenever `|l| ≤ m−2`.

### Route A was not needed

**No genericity is used anywhere** — no generic direction, no generic point, no
infinite-field argument. The open statement Route A was blocked on
(`f independent ⟹ ∃ c, dirGenWronskian c f ≠ 0`) never had to be settled.

`QOU/Mathlib/DirectionalWronskian.lean` is **kept, not deleted**: the equivalence it proves
(a non-zero directional Wronskian iff some line has independent restrictions) is
independently meaningful — it is what showed the base point drops out — and it is the natural
home for anything later needing the line-restriction machinery. It is no longer on the
critical path for Roth.

### Follow-up

Roth's lemma itself is now unblocked; it stays on the parent bean `qou-br3w`.
