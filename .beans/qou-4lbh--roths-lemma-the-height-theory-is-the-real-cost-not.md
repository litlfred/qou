---
# qou-4lbh
title: 'Roth''s lemma: the height theory is the real cost, not the Wronskians'
status: in-progress
type: task
created_at: 2026-08-21T16:31:55Z
updated_at: 2026-08-22T00:00:00Z
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

---

## Progress, 2026-08-21 — the algebra is done; only the analytic half remains

Thirteen declarations landed (`086d15e0a7`).

**`RothIndex.lean`** gained the direction it lacked. Every index result in the file bounded
the index from *above*; Roth's lemma also needs the other way, because the auxiliary
polynomial is **constructed** to vanish to high order and the index is what that buys.

- `le_idxWeight`, `le_index_of_forall_le_support`
- `monomial_one_dvd_iff_support`, `X_pow_dvd_iff_support`, `le_index_of_X_pow_dvd_translate`

`X_pow_dvd_iff_support` is a measured Mathlib gap: Mathlib has the univariate
`Polynomial.X_pow_dvd_iff` and only the first-power `X_dvd_iff_modMonomial_eq_zero`
multivariately.

**New module `SeparatedWronskian.lean`** — the factorization driving the induction on the
number of variables. For `P = ∑ₖ φₖ(x)ψₖ(y)` with the groups disjoint, the mixed generalized
Wronskian factors into an `x`-Wronskian times a `y`-Wronskian, which is exactly what reduces
`m` variables to `1` and `m−1`. Ten declarations, ending in `det_separated_wronskian`.

The split is modelled as `σ ⊕ τ` with `rename Sum.inl`/`Sum.inr`, so "involves only this
group" is a statement about `vars` rather than a side condition threaded everywhere.

### Where Roth's lemma now stands

| step | status |
|---|---|
| index lower bound from high-order vanishing | **done** |
| divisibility ↔ support ↔ index | **done** |
| Wronskian factorization for separated `P` | **done** |
| bounded-order independence certificate | done (`qou-sq3h`) |
| Wronskian degree bound | done |
| **`m = 1` base case** | **BLOCKED — the two absent Mahler bridges** |
| assembling the induction | not started |

⚠ **The blocker is untouched and is now the whole remaining cost.** `m = 1` needs
`M(P) = ‖lead‖·∏max(1,‖root‖)` (Jensen form) and `M(P) ≤ √(deg+1)·H(P)` (Landau). Mathlib's
`mahlerMeasure` is `ℂ[X]`-only and proves multiplicativity — the hard part — but neither
bridge. The decision (fill upstream vs. bare-hands Gelfond on `ℤ[X]`) is still open and
should be made deliberately rather than drifted into.

### A tactic trap, recorded in the source

`gcongr` discharges its side goal from the local context when the fact is a hypothesis, and
leaves it when it is not. The identical `k/dⱼ ≤ iⱼ/dⱼ` step **needs** a follow-up
`exact_mod_cast` in `le_index_of_forall_le_support` and must **not** have one in
`le_index_of_X_pow_dvd_translate`. Both spellings are correct in their own context; copying
either into the other fails.

---

## ⚠ CORRECTION, 2026-08-21 — the base case is NOT blocked, and this bean's title is misleading

This bean was opened on the finding that Roth's lemma's remaining cost is height theory, and
that the `m = 1` base case is "the analytic half of the theorem", blocked on two absent
Mahler-measure bridges. **That is wrong for the base case.**

`QOU/Mathlib/RothHeightBound.lean` proves the bound the base case actually needs, with no
analysis at all:

```
(qX − p)^k ∣ P  in ℤ[X],  P ≠ 0   ⟹   q^k ≤ |lead P|
```

because `lead((qX − p)^k) = q^k` and in a domain a divisor's leading coefficient divides the
dividend's. One line of algebra.

### Why the earlier assessment went wrong

Mahler measure / Gelfond's inequality bounds the heights of **factors** in terms of the
height of a product — from `H(P)` *down to* `H(φ)`, `H(ψ)`. That is the **induction step**,
where `P = ∑ₖ φₖ(x)ψₖ(y)` is split and the factors' heights must be controlled.

The **base case** goes the other way — from a *divisor* up to the dividend — and that
direction is free. Conflating the two produced the wrong blocker. The measured Mathlib
inventory in this bean is still accurate; what was wrong is *which step needs it*.

### Revised status

| step | status |
|---|---|
| index lower bound, divisibility ↔ support ↔ index | done |
| Wronskian factorization for separated `P` | done |
| bounded-order certificate, degree bound | done |
| **`m = 1` height bound** | **done — elementary, no Mahler** |
| index → divisibility in one variable, + Gauss into `ℤ[X]` | **open, but ordinary algebra** — Mathlib has `IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` |
| **induction step: heights of the factors** | **open — THIS is where Gelfond/Mahler is needed** |

So the analytic blocker is real but sits one level up from where this bean placed it. The
title ("the height theory is the real cost") is still roughly right; "not the Wronskians" is
right; but the base case is not the expensive part.

---

## 2026-08-22 — the `m = 1` base case is COMPLETE

`QOU/Mathlib/RothHeightBound.lean`, `pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero`:

> `P ∈ ℤ[X]` vanishes to order `k` at `p/q` (every coefficient of the translate below `k` is
> zero), `p, q` coprime, `q > 0`, `P ≠ 0`  ⟹  `q^k ≤ |lead P|`.

With Roth's hypothesis `H(P) ≤ q^{εd}` this gives `q^{θd} ≤ q^{εd}`, i.e. index `θ ≤ ε` —
which **is** the base case. **There is no analysis anywhere in it.**

Three steps, each landed:

1. `pow_le_abs_leadingCoeff_of_linear_pow_dvd` — `lead((qX−p)^k) = q^k` and a divisor's
   leading coefficient divides.
2. `dvd_of_isPrimitive_of_map_dvd_map` — one-sided Gauss. Mathlib's version wants *both*
   polynomials primitive; splitting off the content removes that.
3. `sub_C_pow_dvd_iff_X_pow_dvd_taylor` — vanishing to order `k` at `a` is exactly `X^k`
   dividing `taylor a P`, hence `(X − a)^k ∣ P`.

### This bean's founding premise is now fully corrected

It was opened on "the `m = 1` base case is the analytic half, blocked on two absent
Mahler bridges". The base case is **done, elementary, and needed neither bridge**. The
correction and its cause (confusing the divisor→dividend direction with the
product→factor direction) are recorded in the module header.

### What actually remains

**Only the induction step**, and only its height half: bounding `H(φₖ)`, `H(ψₖ)` in terms of
`H(P)` for a separated `P = ∑ₖ φₖ(x)ψₖ(y)`. That is the product→factor direction, and it is
where Gelfond's inequality / Mahler multiplicativity is genuinely required. The
factorization itself is proved (`det_separated_wronskian`).

So the Mahler decision — fill the bridges upstream vs. a bare-hands Gelfond inequality on
`ℤ[X]` — is now the *single* remaining question, and it is scoped to one step rather than
to the whole base case.

---

## ⚠ 2026-08-22 — the Mahler recommendation was wrong; upstream is the cheap route

Last recorded recommendation: prefer a **bare-hands Gelfond inequality on `ℤ[X]`** over
filling Mathlib's missing Mahler bridges, to avoid `ℂ[X]` and circle averages.

**Measuring reversed it, on two counts:**

1. **Gelfond's standard proof goes *through* the Mahler measure.** "Bare-hands" is not a
   route around it — it is a re-derivation of it. Preferring it traded a known path for an
   unknown one of at least equal length.
2. **Mathlib already has the hard analytic content.**
   `circleAverage_log_norm_sub_const_eq_posLog`
   (`Mathlib/Analysis/SpecialFunctions/Integrals/PosLogEqCircleAverage.lean`) *is* Jensen's
   formula for a single root. What was missing was only its connection to `mahlerMeasure`.

That connection is now proved — `QOU/Mathlib/MahlerJensen.lean`:

```
M(X − a) = max(1, ‖a‖)
```

### Revised route to the last open step

| piece | status |
|---|---|
| `M(X − a) = max(1,‖a‖)` (Jensen, one root) | **done** |
| `mahlerMeasure_mul` (multiplicativity) | present in Mathlib |
| factorization of `ℂ[X]` into linear factors | present in Mathlib |
| **Jensen form** `M(P) = ‖lead‖·∏max(1,‖root‖)` | assembly of the above — *not analysis* |
| **Landau** `M(P) ≤ √(deg+1)·H(P)` | **still absent** — the other bridge |
| Gelfond, then factor-height control | follows from both bridges |

⚠ **Do not read this as "the blocker is gone".** The Jensen form is one of *two* bridges.
Landau's inequality — the one that turns a Mahler bound into a *coefficient* bound — is
still absent and is untouched by the above. Gelfond needs both directions.

---

## 2026-08-22 — the coefficient bridge, and ⚠ it is NOT Landau

`QOU/Mathlib/MahlerJensen.lean` gained five declarations giving

```
M(p) ≤ max(1, ‖p‖₁)      for p ∈ ℂ[X]
M(q) ≤ ‖q‖₁             for 0 ≠ q ∈ ℤ[X]   (mahlerMeasure_le_sum_int)
```

`norm_eval_le_sum_norm_coeff`, `mahlerMeasure_le_max_one_sum_norm_coeff`,
`mahlerMeasure_le_sum_norm_coeff`, `one_le_sum_norm_coeff_map_int`,
`mahlerMeasure_le_sum_int`. All six declarations in the module axiom-check to
`[propext, Classical.choice, Quot.sound]`.

### ⚠ Do not record this as "Landau: done"

The row above in the 2026-08-22 table says **Landau** `M(P) ≤ √(deg+1)·H(P)`. What is proved
is **weaker**, on purpose:

* proved: `M(p) ≤ sup_{|z|=1}‖p(z)‖ ≤ ‖p‖₁`, the crude sup bound on the circle.
* Landau: `M(p) ≤ ‖p‖₂`, which needs Parseval plus Jensen's inequality for `exp`.
* Since `‖p‖₁ ≤ (deg+1)·H(p)` and `‖p‖₂ ≤ √(deg+1)·H(p)`, the bound proved loses a factor
  `√(deg+1)` against Landau.

**It is nevertheless enough for the use downstream.** Gelfond then reads
`∏ H(pᵢ) ≤ 2^{deg}(deg+1)·H(p)` instead of `2^{deg}√(deg+1)·H(p)`, and that extra polynomial
factor is invisible beside the exponential constants Roth's lemma already carries. Sharpening
to Landau proper is worth doing only as an upstream contribution, not to unblock this arc.

### The `max 1` is forced, not slack

The pointwise step `log‖p(z)‖ ≤ log ‖p‖₁` **fails** at a zero of `p` on the unit circle when
`‖p‖₁ < 1`, because Mathlib's `Real.log 0 = 0`, which exceeds `log ‖p‖₁ < 0`. Bounding by
`max(1, ‖p‖₁)` makes the inequality hold at *every* point of the circle, so
`circleAverage_mono_on_of_le_circle` applies directly and no a.e. argument is needed. Over
`ℤ` the `max` costs nothing: the leading coefficient of a non-zero integer polynomial already
contributes at least one to the sum.

### ⚠ What is still missing is the OTHER direction

| bridge | status |
|---|---|
| `M(X − a) = max(1,‖a‖)` (Jensen, one root) | done |
| `M(p) ≤ ‖p‖₁` over `ℤ` (coefficient bound) | **done — this entry** |
| **Jensen form** `M(P) = ‖lead‖·∏max(1,‖root‖)` | assembly; not started |
| **`H(p) ≤ 2^{deg p}·M(p)`** (Vieta, from the Jensen form) | **ABSENT — the real gap now** |
| Gelfond, then factor-height control | needs the two rows above |

Gelfond bounds `∏H(pᵢ)` by `H(p)`, so it consumes both directions: `H(pᵢ) ≤ 2^{deg}M(pᵢ)`
going up from each factor's Mahler measure, and `M(p) ≤ ‖p‖₁` coming down from the product's
height. Only the second is now in hand. `H(p) ≤ 2^{deg}·M(p)` follows from the Jensen form by
Vieta and is the next thing to prove — it is not analysis, but it is not yet written.

---

## 2026-08-22 — the Jensen form is done; ONE bridge remains

`QOU/Mathlib/MahlerJensen.lean`:

```
mahlerMeasure_eq_leadingCoeff_mul_prod_roots :
    M(p) = ‖lead p‖ · ∏_{a ∈ roots p} max(1, ‖a‖)
mahlerMeasure_C_mul_X_sub_C  (q ≠ 0) :  M(qX − a) = max(‖q‖, ‖a‖)
```

Eight declarations in the module, all `[propext, Classical.choice, Quot.sound]`.

It was assembly, as predicted: `mahlerMeasure_X_sub_C` for a single factor, Mathlib's
`prod_mahlerMeasure_eq_mahlerMeasure_prod` for the product, and
`C_leadingCoeff_mul_prod_multiset_X_sub_C` for the factorization, which applies over `ℂ`
because it is algebraically closed. No new analysis. The estimate held.

`M(qX − a) = max(‖q‖,‖a‖)` was listed as ABSENT in this bean's measured inventory; it is now
present, as the Jensen form at one root.

Two details worth keeping:

* The Jensen form needs **no `p ≠ 0` hypothesis** — at `p = 0` the left side is `0` by
  definition and the right side is `‖0‖ · 1 = 0`, since `(0 : ℂ[X]).roots` is empty.
* The `IsAlgClosed ℂ` instance lives in `Mathlib/Analysis/Complex/Polynomial/Basic.lean`
  (the fundamental theorem of algebra) — importing `FieldTheory.IsAlgClosed.Basic` gives the
  class but not the instance, and the failure is a bare `failed to synthesize`.

### The inventory, current

| bridge | status |
|---|---|
| `M(X − a) = max(1,‖a‖)` | done |
| **Jensen form** `M(p) = ‖lead‖·∏max(1,‖root‖)` | **done — this entry** |
| `M(qX − a) = max(‖q‖,‖a‖)` | **done — this entry** |
| `M(p) ≤ ‖p‖₁` over `ℤ` | done (⚠ weaker than Landau; see above) |
| **`H(p) ≤ 2^{deg p}·M(p)`** | **ABSENT — the last one** |
| Gelfond, then factor-height control | needs the row above |

`H(p) ≤ 2^{deg p}·M(p)` now follows from the Jensen form by Vieta: each coefficient is
`lead p` times an elementary symmetric function of the roots, so `‖coeff j‖ ≤ C(n,j)·M(p)`,
and `∑ⱼ C(n,j) = 2ⁿ`. Mathlib has Vieta (`Polynomial.coeff_eq_esymm_roots_of_card`), so this
is bookkeeping over it rather than analysis — but it is not yet written, and until it is,
Gelfond has only one of its two directions.

---

## 2026-08-22 — the last bridge is closed; every Mahler prerequisite is now in hand

`QOU/Mathlib/MahlerJensen.lean`, four more declarations:

```
Multiset.norm_prod            ‖t.prod‖ = ∏ ‖a‖                    (any NormedField)
Multiset.norm_esymm_le        ‖esymm s j‖ ≤ C(card s, j) · ∏ max(1,‖a‖)
norm_coeff_le_choose_mul_mahlerMeasure   ‖coeff k p‖ ≤ C(n, n−k) · M(p)
norm_coeff_le_two_pow_mul_mahlerMeasure  ‖coeff k p‖ ≤ 2^{deg p} · M(p)
```

Twelve declarations in the module, all `[propext, Classical.choice, Quot.sound]`, module
built by name with the `.olean` deleted first, no linter output.

The last row **is** `H(p) ≤ 2^{deg p}·M(p)`: `H` is the supremum of `‖coeff k p‖` over `k`,
so the per-coefficient statement is the height bound. It is stated per coefficient on
purpose — that avoids committing to a definition of `H` in this module and is the form
Gelfond consumes. It carries **no hypothesis on `k`**: above the degree the coefficient is
zero and the bound is free.

It was bookkeeping over Mathlib's Vieta, as predicted. `coeff_eq_esymm_roots_of_card` writes
`coeff k p` as `lead p · (−1)^{n−k} · esymm (roots p) (n−k)`, and the Jensen form writes
`M(p)` as `‖lead p‖ · ∏max(1,‖root‖)`. The two share `‖lead p‖`, so the whole content is
`Multiset.norm_esymm_le`, whose two slacknesses are both deliberate: bound each subset
product termwise by `∏max(1,‖a‖)`, then *extend* the product from the subset to the whole
multiset — legal exactly because every extra factor is `≥ 1`. With every summand bounded by
the same quantity, the sum over `powersetCard j` costs `card = C(card s, j)`, and
`Nat.choose_le_two_pow` finishes.

### The measured inventory is now complete

| bridge | status |
|---|---|
| `M(X − a) = max(1,‖a‖)` | done |
| Jensen form `M(p) = ‖lead‖·∏max(1,‖root‖)` | done |
| `M(qX − a) = max(‖q‖,‖a‖)` | done |
| `M(p) ≤ ‖p‖₁` over `ℤ` | done (⚠ weaker than Landau) |
| `H(p) ≤ 2^{deg p}·M(p)` | **done — this entry** |
| `mahlerMeasure_mul` | present in Mathlib |

⚠ **This does not mean Roth's lemma is done, or even that Gelfond is done.** What is done is
the *inventory*: every Mahler-measure fact the height argument was blocked on is now proved.
Two things remain, and neither is analysis:

1. **Gelfond itself** — `∏ₖ H(pₖ) ≤ 2^{deg}(deg+1)·H(p)`. Multiplicativity of `M` carries
   `∏ₖ M(pₖ) = M(p)` exactly (heights are not multiplicative; Mahler measures are), the
   reverse bridge takes each factor up, the coefficient bound brings the product down.
   The real cost is **moving between `ℤ[X]` and `ℂ[X]`** along `map (Int.castRingHom ℂ)`
   while tracking `natDegree` and `coeff`. `natDegree_map_eq_of_injective` makes it routine;
   `one_le_sum_norm_coeff_map_int` is a worked example of the pattern.
2. **The induction step of Roth's lemma** — applying Gelfond to the factors `φₖ, ψₖ` of a
   separated `P = ∑ₖ φₖ(x)ψₖ(y)`. The factorization itself is proved
   (`det_separated_wronskian`); this is the height half.

Recording the prediction so it can be checked: (1) is a day of `ℤ`-to-`ℂ` bookkeeping, (2) is
where the remaining difficulty actually sits. This bean has mis-placed the difficulty twice
already — once onto the `m = 1` base case, once onto "bare-hands vs upstream" — so treat
that prediction as a claim to be measured, not a plan.

---

## ⚠ 2026-08-22 — THIRD CORRECTION: the induction step does not need Gelfond

This bean's standing prediction — repeated in the entry above — is that the height half of the
induction step needs Gelfond's inequality. **For the step this repo has actually formalised,
that is wrong.**

New module `QOU/Mathlib/SeparatedHeight.lean`, five declarations plus two non-vacuity
examples, all `[propext, Classical.choice, Quot.sound]`, built by name with the `.olean`
deleted, no linter output:

```
coeff_sumElim_rename_mul     coeff (i ⊞ j) (U·V) = coeff i U * coeff j V
abs_coeff_mul_separated_le   H(U·V) ≤ H(U)·H(V)
abs_coeff_le_of_mul_separated  H(U) ≤ H(U·V)   for V ≠ 0 over ℤ
```

### Why Gelfond is the wrong tool here

Gelfond bounds the heights of factors of a product **in shared variables**, where the
coefficient of a monomial is a *sum* over many splittings and cancellation is possible. That
is what makes it an inequality with a `2^{deg}` in it, and what makes it need the Mahler
measure.

The separated-Wronskian factorization `W = U(x)·V(y)` (`det_separated_wronskian`) is not that.
The variable groups are **disjoint**, so the monomials `x^i y^j` are pairwise distinct and the
coefficient of `x^i y^j` in the product **is** `uᵢvⱼ` — one term, no sum, no cancellation.
Height is therefore *exactly* multiplicative, and `H(U) ≤ H(W)` follows from nothing more than
"a non-zero integer has absolute value at least one":

```
|uᵢ| ≤ |uᵢ|·|vⱼ| = |coeff (i ⊞ j) W| ≤ H(W)     for any j in the support of V.
```

The middle step is an identity, not an estimate.

### ⚠ How far this goes, and how far it does not

It says Gelfond is unnecessary **for this step**. It does **not** say Gelfond is unnecessary
for Roth's lemma. Whether some other step needs it is **unmeasured**, and given that this bean
has now mis-placed the difficulty three times, it should be measured rather than asserted:

1. onto the `m = 1` base case (wrong — that direction is free algebra);
2. onto "bare-hands Gelfond vs upstream Mahler" (wrong — upstream was cheaper);
3. onto the induction step's height half (wrong — disjoint variables don't mix).

The Mahler machinery in `MahlerJensen.lean` is proved, axiom-clean, and costs nothing to
keep; several of its results (`M(qX−a) = max(‖q‖,‖a‖)` in particular) are independently
useful. What should not be kept is the claim that a *named* step is blocked on it.

### Revised open list

| step | status |
|---|---|
| index, Wronskians, bounded-order certificate, degree bound | done |
| `m = 1` base case | done |
| separated-Wronskian factorization | done |
| **heights of the separated factors** | **done — this entry, and elementary** |
| Mahler bridges (Jensen form, coefficient bound, `H ≤ 2^d M`) | done, but not needed above |
| **assembling the induction on the number of variables** | **open — and now the real gap** |
| Roth's lemma proper, then Roth's theorem | open |

The next thing to measure is the assembly itself: what quantitative statement the induction
carries, and whether every ingredient it names is present. That is a scoping task, not a
proving one, and it should come before more Mahler work.

### Addendum — the shared-variable easy direction

`abs_coeff_mul_le` (same module): `H(f·g) ≤ #supp(f)·H(f)·H(g)` for `f, g` in the **same**
variables. Six declarations in `SeparatedHeight.lean` now, all axiom-clean.

It is here because it is the contrast that makes the Gelfond point precise. Going **up** —
factors' heights to the product's — is elementary either way: at most `#supp f` antidiagonal
terms survive, since `b = n − a` is determined by `a`. Disjointness removes even that factor,
because exactly one term survives. Gelfond is the direction that comes **down**, and only in
shared variables.

It is also the tool the next step needs: `mvGenWronskian D f` is a determinant in iterated
`pderiv`s of `P`, so its height follows from `abs_coeff_mul_le` along the Leibniz expansion,
given a bound on `|coeff n (pderiv i P)|`. ⚠ Until that exists, `abs_coeff_le_of_mul_separated`
is being fed a hypothesis nothing yet establishes — the chain is sound but not yet grounded.
