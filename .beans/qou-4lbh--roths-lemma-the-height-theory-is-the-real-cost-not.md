---
# qou-4lbh
title: 'Roth''s lemma: the height theory is the real cost, not the Wronskians'
status: todo
type: task
created_at: 2026-08-21T16:31:55Z
updated_at: 2026-08-21T16:31:55Z
---

The index and Wronskian machinery for Roth's lemma is done. What remains is the m=1 base case, which is blocked on height theory Mathlib has only partially. See body for the measured inventory.

Child of `qou-br3w`. Successor to `qou-sq3h`, which is complete.

## The headline

Every piece of the **index / Wronskian** machinery Roth's lemma needs is now proved and
sorry-free. The remaining cost is almost entirely **height theory**, and Mathlib has it only
partially. That is the opposite of where this arc expected the difficulty to sit, so it is
worth stating before anyone budgets the work.

## What is in hand

| piece | where |
|---|---|
| index at a point, `index_mul_ge` | `QOU/Mathlib/RothIndex.lean` |
| index under differentiation, single and iterated | `RothIndex.lean` |
| `translate_pderiv` (chain rule for translation) | `RothIndex.lean` |
| generalized Wronskians, univariate, dependence iff | `GenWronskian.lean` |
| generalized Wronskians, several variables, both directions | `MvGenWronskian.lean` |
| **bounded-order** criterion, general `m`, both directions | `BoundedOrderWronskian.lean` |
| **degree bound** `deg_{xᵢ} (mvGenWronskian D f) ≤ m·d` | `MvGenWronskian.lean` |
| line restriction + chain rule; directional Wronskian | `LineRestriction.lean`, `DirectionalWronskian.lean` |

The degree bound is what makes the certificate *quantitative*: Roth's lemma does not merely
need some non-zero Wronskian, it needs one whose degree is controlled by the degrees of the
auxiliary polynomial, because the index estimate is measured against those degrees.

## ⚠ Measured inventory of the height side

Checked against Mathlib this session — measured, not assumed.

| needed for `m = 1` | Mathlib status |
|---|---|
| Siegel's lemma | **present** — `exists_ne_zero_int_vec_norm_le` |
| house of an algebraic number | **present** — `NumberField.house` |
| Gauss's lemma / content | **present** — `Polynomial.content_mul`, `IsPrimitive.mul` |
| Mahler measure, and **multiplicativity** | **present** — `mahlerMeasure_mul` |
| `M(P) = ‖lead‖ · ∏ max(1,‖root‖)` (Jensen form) | **ABSENT** |
| `M(P) ≤ √(deg+1) · H(P)` (Landau) | **ABSENT** |
| `M(qX − p) = max(‖p‖,‖q‖)` | **ABSENT** (follows from the Jensen form) |

⚠ Mathlib's `mahlerMeasure` is defined **only for `ℂ[X]`**, as a circle average
(`Mathlib/Analysis/Polynomial/MahlerMeasure.lean`). Multiplicativity is proved there, which is
the hard part — but *neither* bridge is: not the one to root products, and not the one to
coefficient heights. Both are needed to turn "`(qx−p)^k` divides `P`" into a bound on `q^k`
in terms of `H(P)`, which is the entire content of the `m = 1` case.

So the `m = 1` case is **not** a small warm-up. It is the analytic half of the theorem and it
needs Mathlib-gap work in complex analysis, not in polynomial algebra.

## Decomposition, in order

1. **`Xⱼ^k ∣ Q ↔ ∀ i ∈ supp Q, k ≤ i j`** for `MvPolynomial`. Mathlib has the univariate
   `Polynomial.X_pow_dvd_iff` but only `X_dvd_iff_modMonomial_eq_zero` multivariately. Cheap,
   and it is what connects `index` to divisibility.
2. **The `m = 1` case**: index ≥ θ ⟹ `(qx−p)^{θd} ∣ P` ⟹ height bound. Blocked on the two
   absent Mahler bridges above.
3. **The induction step**: the Wronskian of a separated `P = ∑ₖ φₖ(x) ψₖ(y)` factors, because
   `Δᵢ Δ'ⱼ P = ∑ₖ (Δᵢφₖ)(Δ'ⱼψₖ)` makes the matrix a product, so `det` splits by
   `Matrix.det_mul`. Needs the variable-splitting infrastructure
   (`MvPolynomial (σ ⊕ τ) K ≃ MvPolynomial σ (MvPolynomial τ K)`), not new mathematics.
4. **Roth's lemma** proper, then **Roth's theorem** by the auxiliary-polynomial contradiction
   using Siegel's lemma.

## Honest scoping

Step 3 is bookkeeping over existing infrastructure. Step 2 is not: it is a genuine
Mathlib-gap project in its own right, and whoever picks this up should decide whether to fill
the Mahler-measure bridges upstream or to route around them with a bare-hands Gelfond
inequality on ℤ[X].
