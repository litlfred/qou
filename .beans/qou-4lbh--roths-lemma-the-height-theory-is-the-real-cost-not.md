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

### Addendum 2 — the entries are grounded, the determinant is not

`MvPolynomial.abs_coeff_pderiv_le` in `QOU/Mathlib/MvGenWronskian.lean`:
`H(∂ⱼ g) ≤ degⱼ(g)·H(g)` over `ℤ`. Placed there, not in `SeparatedHeight.lean`, so that both
modules keep the "Mathlib imports only, liftable verbatim" property — it depends on
`coeff_pderiv`, which is itself a measured Mathlib gap (`Mathlib/Algebra/MvPolynomial/PDeriv.lean`
has no coefficient formula for `pderiv`).

It falls straight out of `coeff_pderiv` being an **identity**: `coeff γ (∂ⱼ g) = (γⱼ+1)·coeff (γ+eⱼ) g`.
The factor `γⱼ+1` is unbounded in `γ`, but it only ever multiplies a coefficient at exponent
`γⱼ+1` in the `j`-th variable, so past `degⱼ(g)` that coefficient is zero and the product
vanishes. Those are the proof's two cases.

⚠ **This grounds the entries of a generalized Wronskian, not the determinant.** Leibniz
expands the determinant into `m!` signed products of `m` entries; bounding those needs
`abs_coeff_mul_le` applied `m−1` times, which drags in a bound on the support size of each
partial product — and that is not written. So `abs_coeff_le_of_mul_separated` is still being
handed a `B` that nothing establishes for the Wronskian. The chain is sound but not grounded
end to end, and a stack of true lemmas should not be allowed to read as a finished argument.

Verification for this addendum: all eight arc modules (`RothIndex`, `MvGenWronskian`,
`LineRestriction`, `DirectionalWronskian`, `BoundedOrderWronskian`, `SeparatedWronskian`,
`RothHeightBound`, `MahlerJensen`, `SeparatedHeight`) rebuilt with their `.olean`s deleted
first — exit 0, no linter output. Downstream importers of `MvGenWronskian` were rebuilt
explicitly, since a per-module build cannot see breakage in a module that imports it.

---

## 2026-08-22 — the determinant height bound; the links are all proved, the chain is not walked

New module `QOU/Mathlib/MvPolynomialHeight.lean` (5 declarations), plus
`card_support_pderiv_le` in `MvGenWronskian.lean`. All axiom-clean.

```
abs_coeff_mul_le            H(f·g)      ≤ #supp(f)·H(f)·H(g)      (moved here)
abs_coeff_multiset_prod_le  H(∏ t)      ≤ (S·B)^{card t}
abs_coeff_prod_le           H(∏_{i∈s})  ≤ (S·B)^{#s}
abs_coeff_det_le            H(det M)    ≤ m!·(S·B)^m
card_support_pderiv_le      #supp(∂ⱼ g) ≤ #supp(g)
```

`abs_coeff_mul_le` **moved** out of `SeparatedHeight.lean`. That module is named for the
disjoint case; general product and determinant bounds do not belong under that name, and a
reader looking for "height of a determinant" would not find it there. Both modules stay
Mathlib-only and liftable.

### What the bounds actually say

A product costs a factor of the **support size**, not only the heights, because
`coeff n (f·g)` is a sum over the antidiagonal and up to `#supp f` summands survive. That
factor is precisely what disjointness removes — hence `abs_coeff_mul_separated_le` has none.
Both `1 ≤ S` and `0 ≤ B` are needed to state the product bound as a clean `k`-th power; the
sharp form shaves one `S`, since the recursion never puts a *partial* product in the first
slot, but carrying `S^{k-1}` costs more than it buys.

The determinant is Leibniz plus counting: `m!` signed products of `m` entries, the sign a unit
of `ℤ` so it does not move the absolute value at all.

### ⚠ Do not read this as "the Wronskian's height is bounded"

Every **link** is proved. The **chain has not been walked.** There is no statement anywhere
bounding `H(mvGenWronskian D f)` in terms of `H(f)` and the degrees: that needs the
`pderivList` iteration actually performed — `abs_coeff_pderiv_le` and `card_support_pderiv_le`
composed along a list — and then `abs_coeff_det_le` applied with the resulting `S` and `B`.
Neither step is written.

This is the same failure mode this bean has hit three times, in a new costume: a stack of true
lemmas that *looks* like a finished argument. It is recorded in `SeparatedHeight.lean`'s
`### Next` as well, so the note travels with the code rather than only with the bean.

### Open, in order

1. **Compose the chain** — `H(pderivList D g)` from `H(g)`, then `H(mvGenWronskian D f)`.
   Mechanical, and the first thing that should be done.
2. **Assemble the induction** on the number of variables. Still the real gap.
3. Roth's lemma proper, then Roth's theorem.

---

## 2026-08-22 — the chain is walked: H(mvGenWronskian D f) ≤ m!·(S·(d^L·B))^m

New module `QOU/Mathlib/WronskianHeight.lean`, three declarations plus a non-vacuity guard,
all `[propext, Classical.choice, Quot.sound]`:

```
card_support_pderivList_le    #supp(pderivList l g) ≤ #supp(g)
abs_coeff_pderivList_le       H(pderivList l g)     ≤ d^{|l|}·H(g)
abs_coeff_mvGenWronskian_le   H(mvGenWronskian D f) ≤ m!·(S·(d^L·B))^m
```

**This closes the gap the previous entry flagged.** That entry warned the arc had become "a
stack of true lemmas that *looks* like a finished argument" — every link proved, no statement
anywhere actually bounding a Wronskian. There is one now, and `SeparatedHeight.lean`'s note
saying otherwise has been corrected in place rather than left to rot.

Where each factor comes from:

* `d^L` — each `pderiv` multiplies a coefficient by an exponent bounded by the degree. The
  *same* `d` works at every step, because `degreeOf` does not grow under differentiation
  (`degreeOf_pderivList_le`, already in the corpus). Without that the bound would degrade
  along the list.
* `S` — the antidiagonal cost of each Leibniz multiplication. Support does not grow under
  differentiation either, so entries inherit `S` from `f` unchanged.
* `m!` — the permutation count.

⚠ **Not Mathlib-liftable on its own.** It imports `MvGenWronskian` and `MvPolynomialHeight`;
both of those are Mathlib-only, so the three lift together, but `mvGenWronskian` is not a
Mathlib notion. Recorded in the module header.

The theorem carries eight hypotheses, so a worked instance (`m=1`, `f=X`, `D=![[]]`,
`S=d=B=1`, `L=0`) is landed with it as an `example`: the premises are jointly satisfiable and
the statement is not vacuously true.

### The height side of Roth's lemma is closed end to end

| link | where |
|---|---|
| `H(f)`, degrees, supports → `H(∂ⱼ f)`, `#supp(∂ⱼ f)` | `MvGenWronskian.lean` |
| → `H(pderivList l f)` | `WronskianHeight.lean` |
| → `H(mvGenWronskian D f)` | `WronskianHeight.lean` |
| → `H(U)`, `H(V)` for the separated factors | `SeparatedHeight.lean` |
| Mahler bridges (Jensen form, `M ≤ ‖·‖₁`, `H ≤ 2^d·M`) | `MahlerJensen.lean` — proved, not needed by the above |

### ⚠ What is open

**Only the assembly**: the statement of Roth's lemma and the induction from `m` variables to
`1` and `m−1`. That is structural, not quantitative.

I predict no further height machinery is needed. **Treat that as a claim to be measured.**
This bean has now mis-predicted the location of the remaining cost three times — onto the
`m=1` base case, onto bare-hands-vs-upstream Mahler, and onto Gelfond for the induction step —
and each time the prediction was confident and wrong.

---

## 2026-08-23 — the index splits too: index(U(x)·V(y)) = index U + index V

New module `QOU/Mathlib/SeparatedIndex.lean`, nine declarations plus a discriminating
validation example, all `[propext, Classical.choice, Quot.sound]`, built by name with the
`.olean` deleted, no linter output.

```
translate_rename_inl / _inr    translate commutes with the variable injections
idxWeight_sumElim              idxWeight (i ⊞ j) = idxWeight i + idxWeight j
idxWeight_mapDomain_inl / _inr
index_rename_inl / _inr        injecting into the larger variable set preserves the index
index_separated                index (U(x)·V(y)) = index U + index V
index_X_sq_weight_two          validation input
```

This is the **index analogue of last turn's height result**, and it is the other half of what
Roth's induction splits on. The separated Wronskian factors as `W = U(x)·V(y)`; the induction
hypothesis bounds `index U` and `index V` separately; `index_separated` is what turns those
two bounds into a bound on `index W`. Without it the recursion has nothing to recurse on.

### ⚠ Where `IsDomain` does real work — and it is only one of the two directions

* **`≥`** is `index_mul_ge` (already in `RothIndex.lean`) plus the new rename-invariance
  lemmas. True over any `CommRing`. Nothing new.
* **`≤`** is the new content and is **false in general without `IsDomain`**. The proof picks
  multi-indices `i₀, j₀` realising each index and needs `i₀ ⊞ j₀` to actually occur in the
  product. Its coefficient there is exactly `coeff i₀ (translate α U) · coeff j₀ (translate β V)`
  — a product of two non-zero elements, which is non-zero only in a domain. Over a ring with
  zero divisors that monomial can cancel, the realising index need not occur, and the
  inequality can be strict.

So the equality is not a formality: half of it was already free, and the half that costs
something is precisely the half that constrains the coefficient ring. That is recorded at the
single `mul_ne_zero` in the proof as well as in the module header.

The combinatorial reason the index is *exactly* additive rather than merely superadditive is
`idxWeight_sumElim`: the support of `sumElim i j` is the **disjoint** sum of the two supports,
so the defining sum splits with no overlap.

### The validation is discriminating, not decorative

`RothIndex.lean` sets the standard — it pins the *value* of `index` on `X` and `X²` because a
wrong definition would satisfy every structural lemma. The same risk applies here: with
`σ = τ`, a version of `index_separated` attaching `d₁` to the wrong factor still typechecks.
So the example uses **different weights on the two sides** (`1` left, `2` right) with `X` left
and `X²` right, giving `1 + 1 = 2`; the mis-attached version would give `1/2 + 2 = 5/2`.

### Open

Both halves the induction splits on — index and height — are now exactly additive/controlled
across the separated factorization. What remains is the **statement of Roth's lemma itself**
and the recursion: parameter bookkeeping (`dⱼ/dⱼ₊₁` growth, `ε`, the `qⱼ` conditions) and the
argument feeding the `m = 1` case (`RothHeightBound.lean`) and the `m−1` case back into the
`m` case.

⚠ None of that is index or height machinery. **Last turn I predicted exactly this, and this
time the prediction held** — which is one data point against three failures, not a reason to
start trusting predictions from this arc.

### Addendum — index of a determinant, and a lesson about scratchpad verification

Four more declarations in `RothIndex.lean` (the generic index lemmas belong beside `index`,
not in the separated module):

```
index_sum_ge      inf over summands ≤ index (∑)
index_prod_ge     ∑ of indices        ≤ index (∏)
index_smul_units  index (u • P) = index P   for u : ℤˣ
index_det_ge      inf over permutations of ∑ᵢ index (M (p i) i) ≤ index (det M)
```

`index_det_ge` is the index counterpart of `abs_coeff_det_le`. **Note the direction:** heights
are bounded from *above* by their parts, indices from *below* — vanishing to high order is
preserved by sums and *added* by products — so every statement here is a lower bound. Getting
that backwards would produce plausible-looking but useless lemmas.

⚠ It says nothing about the entries. Relating `index (pderivList D (f j))` back to
`index (f j)` is `index_le_index_iterate_pderiv_add`, already in the file, and that is where
the differentiation cost enters.

#### ⚠ Lesson: a scratchpad proof is not verified until it builds *in the module*

All four went through first try in the scratchpad and then **two of them failed on landing**:

* `index_det_ge` — `Matrix.det` needs `CommRing (MvPolynomial σ R)`, whose *instance* lives in
  `Mathlib/Algebra/MvPolynomial/CommRing.lean`. `RothIndex.lean` never imported it, because
  everything else in the file only ever needs `CommSemiring`. `[CommRing R]` being in scope is
  not the same as the instance being importable.
* `index_smul_units` — `simp [index, translate]` closed the `u = -1` case in the scratchpad and
  not in the module, because the scratchpad's import closure was wider and supplied
  `support_neg`. Now spelled out explicitly so it does not depend on what happens to be
  imported.

This is the same family as the earlier `funext`-resolves-to-`Polynomial.funext` trap: the
scratchpad's *context* differs from the module's, so a scratchpad pass is evidence, not proof.
Both fixes are recorded at the site rather than silently patched.

Verification: all **thirteen** arc modules rebuilt with their `.olean`s deleted — exit 0, no
linter output. `RothIndex`'s import closure changed, so every downstream module was rebuilt
rather than trusted.

---

## ⚠ 2026-08-23 — FOURTH CORRECTION: the `m = 1` base case was not complete

This bean recorded, on 2026-08-22, "**the `m = 1` base case is COMPLETE**", citing
`pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero`, and added:

> With Roth's hypothesis `H(P) ≤ q^{εd}` this gives `q^{θd} ≤ q^{εd}`, i.e. the index `θ ≤ ε`
> — which **is** the base case.

**That last step was prose, not Lean.** What was proved is a statement about *Taylor
coefficients*: if every coefficient of the translate below `k` vanishes then `q^k ≤ |lead P|`.
The induction does not consume that — it consumes a bound on `index`. Nothing anywhere
related the two, because `index` lives on `MvPolynomial` and the height bound on `Polynomial`.

New module `QOU/Mathlib/RothBaseCase.lean`, five declarations plus a validation example, all
`[propext, Classical.choice, Quot.sound]`:

```
coeff_pUnitAlgEquiv                 coefficients correspond along n ↦ single () n
pUnitAlgEquiv_translate             translate ↔ Polynomial.taylor
taylor_coeff_eq_zero_of_le_index    index ≥ k/d kills Taylor coefficients below k
pow_le_abs_leadingCoeff_of_le_index the height bound, restated against index
index_le_of_abs_leadingCoeff_le     |lead P| ≤ q^e ⟹ index ≤ e/d
```

With `e = εd` the last reads `index ≤ ε`, which **is** the base case — now as a theorem.

### Why the gap was easy to miss, and what it says

The arc had a correct height calculus and a correct index calculus and no theorem relating
them. Each side looked finished from its own end. This is the same failure the 2026-08-22
determinant entry flagged in a different costume — a stack of true lemmas reading as a
finished argument — and it survived a round of that very warning.

Two details worth keeping:

* **`q ≥ 2`, not `q > 0`.** The proof is by contradiction on the *realised* index: in one
  variable every support element is `single () n`, so the index is literally `n₀/d` for some
  natural `n₀`, and `e/d < index` forces `e < n₀`, hence `(e+1)/d ≤ index`, hence
  `q^{e+1} ≤ |lead P| ≤ q^e`. With `q = 1` the powers do not separate and the argument gives
  nothing.
* **Universe trap.** `pUnitAlgEquiv` is stated for `PUnit.{u+1}`; a statement written with an
  unannotated `PUnit` gets an auto-bound universe and will not unify with `index` elsewhere.
  The error is an inscrutable `index.{u_2, 0}` vs `index.{0, 0}` mismatch. Every statement in
  the module pins `Unit`.

The validation is not a satisfiability check: with `P = 1`, `p/q = 1/2`, `d = 1`, `e = 0` the
theorem gives `index ≤ 0`, which with `index_nonneg` **pins** the index of a non-zero constant
to exactly `0`.

### Open

Only the **induction on the number of variables**: the parameter conditions (`dⱼ/dⱼ₊₁` growth,
`ε`, the `qⱼ` hypotheses) and the step feeding this theorem and the `m−1` case back into the
`m` case. Everything that step needs from the index and height calculus is proved —
`index_separated` and `abs_coeff_le_of_mul_separated` split the separated Wronskian,
`abs_coeff_mvGenWronskian_le` and `index_det_ge` bound it, and this terminates the recursion.
What is not written is the recursion itself.

⚠ I have now said "only the assembly remains" four times, and twice it turned out a *named*
piece was missing rather than merely unassembled. Before budgeting from that claim again,
someone should write the statement of Roth's lemma down in Lean and check each hypothesis
against an existing theorem — not against a bean entry.

---

## ⚠ 2026-08-23 — FIFTH CORRECTION, found by the audit this bean asked for

Last entry's closing instruction was: *before budgeting from "only the assembly remains"
again, check each claim against a named theorem rather than a bean entry.* Doing that
immediately found a false claim — **one I had written in the same commit as the warning.**

`RothBaseCase.lean` said, in prose:

> `abs_coeff_mvGenWronskian_le` and `index_det_ge` bound it

**The index half was false.** `index_det_ge` bounds `index (det M)` by the indices of the
matrix *entries*. For a generalized Wronskian the entries are `pderivList (D i) (f j)`, and
nothing related those back to `index (f j)`. The height side had exactly that composite
(`abs_coeff_mvGenWronskian_le` in `WronskianHeight.lean`); the index side had no counterpart
module at all, and the asymmetry went unnoticed because each half looked complete from its own
end.

New module `QOU/Mathlib/WronskianIndex.lean`, four declarations, all axiom-clean, built by
name with the `.olean` deleted, no linter output:

```
nsmul_coe_withTop                     WithTop ℚ is not a semiring; nsmul_eq_mul does not apply
index_le_index_pderivList_add         index P ≤ index (pderivList l P) + ∑_{j∈l} 1/dⱼ
sum_index_le_index_mvGenWronskian_add ∑ᵢ index (f i) ≤ index (mvGenWronskian D f) + m·C
sum_index_mvGenWronskian_bound_tight  the bound is attained
```

Read the main result as "differentiating `m` times costs at most `m·C` of index". It is stated
additively because `WithTop ℚ` has no subtraction, and `⊤` must survive — a zero `f i`
contributes `⊤` on the left and the statement stays true.

⚠ **Note the direction, opposite to the height file:** heights are bounded from *above* by
their parts, indices from *below*.

### The validation is tight, and that is the point

The risk here is not the shape of the bound but the **cost factor**: a version with `2·m·C`,
or with the cost dropped, would still be true in many instances and would still typecheck.
`sum_index_mvGenWronskian_bound_tight` pins it — `m = 1`, `f = X`, one derivative, unit weight
at the origin: `index X = 1` on the left; the Wronskian is `∂₀X = 1` with index `0`, so the
right side is `0 + 1·1 = 1`. Both sides are `1`, so a smaller cost factor makes the theorem
false at this very instance.

### What this says about the arc

That is **five** instances of the same failure: a stack of true lemmas reading as a finished
argument. The list is now:

1. the `m = 1` base case is "the analytic half" — wrong;
2. bare-hands Gelfond beats filling Mathlib upstream — wrong;
3. Gelfond is needed for the induction step's height half — wrong;
4. the `m = 1` base case is "COMPLETE" — it was a Taylor-coefficient statement, not an index one;
5. `index_det_ge` "bounds" the Wronskian — it bounds a determinant by its entries.

Note that (5) was written in the same commit that warned about exactly this pattern. **The
warning is not self-executing; only the audit is.** The lesson is procedural, not
mathematical: prose in a module docstring or a bean entry is not evidence, and the cheap check
— naming the theorem that supplies each claim — finds these in minutes.

### Open

Only the **recursion**: Roth's lemma's statement with its parameter conditions
(`dⱼ/dⱼ₊₁` growth, `ε`, the `qⱼ` hypotheses) and the step feeding `RothBaseCase` and the `m−1`
case back into the `m` case.

Both halves of what that step needs from a Wronskian are now composites rather than fragments:
`abs_coeff_mvGenWronskian_le` bounds its height, `sum_index_le_index_mvGenWronskian_add` its
index, and `index_separated` / `abs_coeff_le_of_mul_separated` carry both across the separated
factorization.

⚠ The next person to claim the remaining work is "just assembly" should write the statement of
Roth's lemma in Lean and match every hypothesis to a named theorem. That is what found this
one.

### Addendum — the induction step's interface, composed and checked

Continuing the audit rather than stopping at the fifth correction. Two more claims checked:

**(a) Does `det_separated_wronskian` fit `abs_coeff_le_of_mul_separated`?** I first read the
`SeparatedWronskian` variable line as `[Field K]` and flagged a mismatch with the ℤ-valued
height bound. **That was my misreading** — the constraint is `[CommRing K]`, so it applies at
`ℤ`. Reading is not the audit either.

**(b) Do the pieces actually compose?** New module `QOU/Mathlib/RothInductionStep.lean` writes
the compositions down and lets the elaborator decide:

```
sepW                          the separated Wronskian, named
sepW_eq                       = rename inl (mvGenWronskian Dx φ) * rename inr (mvGenWronskian Dy ψ)
index_sepW                    index splits EXACTLY across the factorisation
abs_coeff_le_of_sepW_left     H(x-Wronskian) ≤ H(separated Wronskian)
abs_coeff_le_of_sepW_right    H(y-Wronskian) ≤ H(separated Wronskian)
```

`index_sepW` is `rw [sepW, det_separated_wronskian, index_separated]` — one line. **That is the
point**: if the claimed interface were real the composition would be trivial, and if it were
not it would not typecheck. Both halves composed unchanged, so the claim survives its first
actual test.

The audit also cashed a deferred item. `SeparatedHeight.lean` had said of the symmetric bound
`H(V) ≤ H(U·V)`: *"not written here because nothing yet calls for it. Add it when something
does, rather than on speculation."* The induction step bounds **both** factors, so it calls
for it — `abs_coeff_le_of_mul_separated_right` is now written and that note corrected.

⚠ This module is the step's **interface, not its proof.** The recursion — parameter conditions
and the argument feeding `RothBaseCase` and the `m−1` case back into the `m` case — is
untouched.

Verification for this addendum: all **sixteen** arc modules rebuilt with `.olean`s deleted —
exit 0, no linter output; every declaration `[propext, Classical.choice, Quot.sound]`.

---

## 2026-08-23 — index transport, and a DESIGN finding: the induction should not be indexed by `Fin m`

Setting out to write Roth's lemma's statement in Lean — the check this bean asked for — turned
up a structural decision worth recording before anyone writes it.

### The transport lemma

`RothIndex.lean` gains three declarations, all axiom-clean:

```
translate_rename_of_injective     translate α (rename f P) = rename f (translate (α∘f) P)
idxWeight_mapDomain_of_injective  idxWeight d (mapDomain f i) = idxWeight (d∘f) i
index_rename_of_injective         index d α (rename f P) = index (d∘f) (α∘f) P
```

Reindexing the variables does not change the index, provided the weights **and** the base
point are transported with them. Injectivity is what keeps the support sum term-for-term.

**Subsumption checked, not asserted.** `SeparatedIndex.lean`'s `index_rename_inl` and
`index_rename_inr` are now one-line specialisations
(`index_rename_of_injective Sum.inl Sum.inl_injective _ _ _`) rather than direct proofs. If
the general lemma did not really cover them, those lines would not compile.

That left `idxWeight_mapDomain_inl` and `idxWeight_mapDomain_inr` with **no consumers** — they
existed only to support the old direct proofs. Both **deleted**. Verified by grep over the
whole `QOU/` corpus that nothing else referenced them; keeping trivially-derivable dead
theorems next to the general lemma they duplicate is clutter, not API.

### ⚠ The design finding: `Unit ⊕ τ`, not `Fin m`

The natural first instinct is to state Roth's lemma over `MvPolynomial (Fin m) ℤ`, since the
parameter conditions (`dⱼ/dⱼ₊₁ ≥ ω`) want the variables ordered. **That fights every piece
this arc has built.**

* The separated machinery — `index_separated`, `abs_coeff_le_of_mul_separated`,
  `det_separated_wronskian`, `RothInductionStep` — is stated for `σ ⊕ τ`. The induction
  *already* has the shape "one variable group plus the rest".
* The base case, `RothBaseCase.lean`, is stated at `Unit`, because `MvPolynomial.pUnitAlgEquiv`
  is what carries one variable to `Polynomial`.

So the recursion should be structured as `Unit ⊕ τ → τ`, and then **no reindexing is needed
anywhere**: the base case lands at `Unit` exactly as proved, and the step consumes the `σ ⊕ τ`
lemmas exactly as proved.

Choosing `Fin m` instead would require, at minimum: `Fin 1 ≃ Unit` transport (that is what
`index_rename_of_injective` was proved for), `pUnitAlgEquiv` commuting with `Polynomial.map`,
and `Fin (m+1) ≃ Unit ⊕ Fin m` transport for both index and height. All provable, all pure
overhead, and none of it needed by the `Unit ⊕ τ` formulation.

⚠ **This is a prediction about a statement nobody has written yet.** It is better founded than
the four wrong predictions above — it is about which existing theorems compose, and that is
checkable — but it should still be checked by writing the statement, not adopted on this
entry's say-so. The ordering condition is the part that will resist: `Unit ⊕ τ` carries no
order, so the `dⱼ/dⱼ₊₁ ≥ ω` hypothesis has to be carried as data through the recursion rather
than read off the index type. That is the real design question and it is **not** settled here.

Verification: all sixteen arc modules rebuilt with `.olean`s deleted — exit 0, no linter
output.

### ⚠ Correction to the entry immediately above — I overstated the cost of `Fin m`

The design finding I just recorded said an `m`-indexed formulation would need "`Fin 1 ≃ Unit`
transport, `pUnitAlgEquiv` commuting with `Polynomial.map`, and `Fin (m+1) ≃ Unit ⊕ Fin m`
transport for both index and height — all provable, all **pure overhead**".

I then measured it instead of leaving the claim standing. `index_rename_equiv`, now in
`RothIndex.lean`:

```lean
theorem index_rename_equiv (e : σ ≃ τ) (d : τ → ℕ) (α : τ → R) (P : MvPolynomial τ R) :
    index d α P = index (d ∘ e) (α ∘ e) (rename e.symm P) := by
  classical
  have h := index_rename_of_injective (e : σ → τ) e.injective d α (rename e.symm P)
  rwa [rename_rename, Equiv.self_comp_symm, rename_id_apply] at h
```

**Three lines**, given the transport lemma. `Fin (m+1) ≃ Unit ⊕ Fin m` already exists in
Mathlib as `(finSuccEquiv m).trans (Equiv.optionEquivSumPUnit _) |>.trans (Equiv.sumComm _ _)`
— checked, it elaborates. And the height side is free: Mathlib's `coeff_rename_mapDomain`
already matches coefficients across a renaming.

So the honest comparison is:

| | transport cost | ordering condition |
|---|---|---|
| `Fin m` | ~3 small lemmas, all cheap | free — the index type carries the order |
| `Unit ⊕ τ` | none | must be carried as data through the recursion |

**Neither is a landslide, and I called it one.** The decision should turn on which makes the
`dⱼ/dⱼ₊₁ ≥ ω` bookkeeping cleaner, and I have not determined that. What I can say is that the
transport objection to `Fin m` is not a real obstacle.

⚠ Worth noting how this one was caught: the overstated claim and its correction are **one
commit apart**, because I tested my own prediction instead of shipping it. That is the whole
method — and it is cheap, three lines of Lean against a paragraph of confident prose.

(Also recorded: `finSuccEquiv` inside `namespace MvPolynomial` resolves to
`MvPolynomial.finSuccEquiv`, not the `Fin` one — `_root_.finSuccEquiv` is required. Same
namespace-shadowing trap as `funext` → `Polynomial.funext` earlier in this arc.)
