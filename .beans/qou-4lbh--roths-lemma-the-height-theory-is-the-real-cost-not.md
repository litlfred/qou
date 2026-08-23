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

---

## 2026-08-23 — the statement is written, `m = 1` is proved, and the indexing question is settled

New module `QOU/Mathlib/RothLemmaStatement.lean`. All declarations axiom-clean, seventeen arc
modules rebuilt with `.olean`s deleted, exit 0, no linter output.

```
pUnitAlgEquiv_map        pUnitAlgEquiv commutes with coefficient maps
symm_map_pUnitAlgEquiv   recovers the shape RothBaseCase expects
RothGrowth               the ω growth condition, read along an ordering equiv
RothLemmaUniform         ⚠ a def, NOT a theorem
rothLemmaUniform_one     the m = 1 case — PROVED
```

### ⚠ Three things that must not be misread

1. **`RothLemmaUniform` is a `def`.** Nothing proves it for `m ≥ 2`. It is a statement, written
   so every hypothesis has to elaborate and so the base case has something to be an instance
   *of*. It is not a formalisation of Roth's lemma.
2. **It is not true for every `ω`.** The growth condition is a real hypothesis: for `m ≥ 2` and
   small `ω` the statement is false. `ω` is left a parameter deliberately — finding `ω(m, ε)`
   is part of the unfinished work, and baking in an unverified constant would hide that. At
   `m = 1` the condition is vacuous, which is why `rothLemmaUniform_one` holds for *every* `ω`.
3. **It is a uniform-`E` variant**, not verbatim Bombieri–Gubler 6.3.4, where the exponent
   varies with `j` (`qⱼ^{dⱼ} ≥ q₁^{d₁}`, `q₁^{ε d₁} ≥ H(P)`). A single `E` is a *stronger*
   hypothesis, so this statement is *weaker*. Whoever proves the general case should check the
   uniform form still suffices downstream.

### The indexing question, settled

Two earlier entries argued `Fin m` versus `Unit ⊕ τ`, and the second overstated its case
(corrected the same day). **Neither is right.** Keep the variable type `σ` general and carry
the ordering as an `Equiv σ (Fin m)`:

* the growth condition reads off the equiv — nothing lost against `Fin m`;
* the base case instantiates at `σ = Unit`, so `RothBaseCase.lean` applies **with no transport
  at all**;
* the recursion can still split `σ` as `Unit ⊕ τ` for the separated machinery, via
  `index_rename_equiv`.

**The evidence is that `rothLemmaUniform_one` uses no reindexing lemma.** Under `Fin m` it
would have needed `Fin 1 ≃ Unit` transport for both index and height.

### What writing it down caught

An earlier draft of the statement **omitted `∀ j, degreeOf j P ≤ d j`** — the hypothesis that
makes `d` a degree vector rather than an arbitrary weight. It was easy to miss because the
`m = 1` proof does not use it. That is the sixth thing this arc's audit habit has caught, and
the first caught by writing a statement rather than by checking a claim.

A satisfiability witness is landed with it: one variable, `P = 1`, `d = 1`, `p/q = 1/2`,
`B = 1`, `E = 0`, `ε = 1`. Every hypothesis holds and the conclusion is a real bound
(`index ≤ 1`), not `⊤` — so the theorem is not true merely because nothing satisfies it.

### Open

**`m ≥ 2` is entirely open.** What exists is the machinery the step consumes:
`RothInductionStep` (separated factorisation), `WronskianHeight` / `WronskianIndex`,
`BoundedOrderWronskian` (non-vanishing), and this module's base case to terminate the
recursion. What does not exist: the choice of `ω(m, ε)`, the construction of the separated
representation, and the recursion itself.

With the statement written, the audit that has caught six errors here can now be run against
it directly — for each hypothesis, name the theorem that supplies or consumes it.

---

## 2026-08-23 — the audit against the statement: separated representations were missing

Ran the audit the previous entry called for — matching each hypothesis of `RothLemmaUniform`
against a named theorem. **Both predicted-empty entries came back empty, and one of them was a
missing construction rather than a missing constant.**

### The finding

Every piece of the separated machinery — `RothInductionStep`, `SeparatedIndex`,
`SeparatedHeight`, `det_separated_wronskian` — *takes* a separated representation
`∑ₖ rename inl (φ k) * rename inr (ψ k)` as **given**. Nothing produced one. Confirmed by grep
before writing: no `exists_separated…` of any kind in the corpus.

That is easy to miss precisely because the arc kept checking that the pieces *compose*. They
do — the composition test in `RothInductionStep` passed. But composing lemmas that all take
the same object as input never reveals that nothing constructs it.

New module `QOU/Mathlib/SeparatedRepresentation.lean`, five declarations, all axiom-clean:

```
monomial_sumElim_eq / _eq'                a monomial on σ ⊕ τ splits as a product
exists_separated_representation           crude: one term per monomial of P
exists_separated_representation_monomial  grouped by x-part: the φ are DISTINCT monomials
linearIndependent_monomial                distinct monomials are independent
```

### ⚠ What it does and does not supply

The grouped version gives **linearly independent `φ`** — the half the bounded-order Wronskian
criterion needs on the `x` side.

⚠ It does **not** give independent `ψ`. Roth's induction wants a *minimal-length*
representation in which **both** families are independent; extracting one is a rank argument
and is not here. ⚠ It is also `Finset (σ →₀ ℕ)`-indexed while `det_separated_wronskian` wants
`Fin r →`; bridging is `Finset.equivFin` and is not written. **This module is not a drop-in
for the induction step**, and the header says so.

### The other empty entry: `ω(m, ε)`

Nothing supplies or constrains the growth constant, and nothing can until the recursion is
written — `ω` is whatever the recursion's error terms force it to be. That is the one open
item that is genuinely mathematical rather than mechanical, and it is why
`RothLemmaUniform` leaves `ω` a parameter rather than pretending to a value.

### Audit result, in full

| hypothesis of `RothLemmaUniform` | supplied / consumed by |
|---|---|
| `d j ≠ 0` | `RothBaseCase.index_le_of_abs_leadingCoeff_le` (needs `d ≠ 0`) |
| `RothGrowth o ω d` | **nothing** — see above |
| `P ≠ 0` | base case; and `BoundedOrderWronskian` for non-vanishing |
| `degreeOf j P ≤ d j` | `MvGenWronskian.degreeOf_mvGenWronskian_le` |
| `|coeff n P| ≤ B` | `WronskianHeight.abs_coeff_mvGenWronskian_le` |
| `2 ≤ qd j`, `IsCoprime` | base case |
| `B ≤ qd j ^ E`, `E ≤ ε·d j` | base case |
| separated representation | **was nothing** — now this module |

Verification: all **eighteen** arc modules rebuilt with `.olean`s deleted — exit 0, no linter
output.

### Both gaps in `SeparatedRepresentation` are closed

The module was landed with two recorded gaps. Both are now shut, in the same module:

```
exists_separated_representation_fin    Fin r-indexed, φ independent
exists_shorter_of_psi_dep              a dependence among ψ shortens the representation
exists_shorter_of_phi_dep              the mirror, for φ
exists_indep_representation            structural induction on r
exists_separated_representation_indep  BOTH families independent   ← the goal
```

**The `Fin r` reindexing** is `Finset.equivFin`; independence transports because
`equivFin.symm` is injective.

**Minimality** is the rank argument. From `∑ₖ cₖψₖ = 0` with `c j ≠ 0`, solve for `ψⱼ` and
substitute: the `j`-th term is absorbed into the others by replacing `φₖ` with
`φₖ − (cₖ/cⱼ)·φⱼ`, giving a representation of length `r−1`. Same argument mirrored for `φ`.
`Fin.sum_univ_succAbove` does all the index surgery — it splits `∑_{k : Fin (n+1)}` as
`f j + ∑_{i : Fin n} f (j.succAbove i)`, which is exactly "the `j`-th term plus the rest".

⚠ **The minimal version needs a field**, because the reduction divides by `cⱼ`. The crude and
grouped versions hold over any `CommRing`; this one does not. Roth's lemma works over `ℚ`, so
it costs nothing there — but it is a real hypothesis change and the module says so.

A note on structure worth keeping: the first plan was `Nat.find` over achievable lengths, which
drags in dependent rewriting (`φ`'s *type* mentions the length). Restructuring as a plain
induction on `r` — "given any representation of length `r`, produce an independent one" —
removes the dependent `subst` entirely. Six lines instead of a fight.

### The induction step can now be fed end to end

`exists_separated_representation_indep` produces the representation,
`det_separated_wronskian` factors its Wronskian, `BoundedOrderWronskian` turns the two
independences into non-vanishing Wronskians, and `RothInductionStep` splits the index and the
height.

⚠ That is the *step's inputs*, not the recursion. `ω(m, ε)` remains the one open item, and it
cannot be settled until the recursion is written.

---

## 2026-08-23 — the induction step's key INEQUALITY, and a bridge that was missing

Setting out to write the recursion turned up one more absent piece, found the same way as the
last three: by trying to use what exists.

### The gap

`sum_index_le_index_mvGenWronskian_add` bounds the index of `mvGenWronskian D f` — a
determinant with **one operator list per row and one function per column**. But
`det_separated_wronskian` builds something else: a matrix whose `(i,j)` entry is a **mixed**
operator `Dx i ++ Dy j` applied to a **single** polynomial `P`. Those are different shapes, and
nothing covered the second.

That matters because the second is the one Roth's lemma actually forms.

`sum_index_le_index_det_pderivList_add` (in `WronskianIndex.lean`) covers it — same proof
shape as the family version: evaluate `index_det_ge`'s infimum at a permutation attaining it,
then bound each entry with `index_le_index_pderivList_add`.

### The key inequality

`sum_index_le_index_sepW_add` (in `RothInductionStep.lean`):

```
r · index P  ≤  index U + index V + r·C
```

for `P = ∑ₖ φₖ(x)ψₖ(y)`, `U = mvGenWronskian Dx φ`, `V = mvGenWronskian Dy ψ`, and `C` a bound
on the per-entry differentiation cost.

**This is what the recursion runs on.** Differentiating `P` into its separated Wronskian costs
at most `C` of index per entry, and the Wronskian's index splits *exactly* between the two
factors — so a large index for `P` forces a large index for one of `U`, `V`, which the
induction hypothesis contradicts.

Additive rather than `r·index P − r·C ≤ …` because `WithTop ℚ` has no subtraction, and `⊤`
must survive: a zero `P` gives `⊤` on the left and the statement stays true.

⚠ Worth noting **how** it composes: `sepW` *is* that determinant, so the bridge is `rfl`. That
the composition is definitional is the check that `WronskianIndex` and `RothInductionStep`
were built to the same shape — had either drifted, this would not have been one line.

### Open

Only the **recursion**: choosing `ω(m, ε)`, choosing bounded-order operator families `Dx`, `Dy`,
and the arithmetic that turns the key inequality plus the induction hypothesis into a
contradiction.

Everything it consumes now exists: `exists_separated_representation_indep` builds the
representation with both families independent, `BoundedOrderWronskian` converts independence
into non-vanishing Wronskians, `sum_index_le_index_sepW_add` supplies the index inequality,
`abs_coeff_le_of_sepW_left/_right` the height control, and `rothLemmaUniform_one` terminates.

⚠ That list is a claim about inputs, not about the argument. The argument is not written, and
this arc's record is that a list of available pieces is not evidence that they assemble.

Verification: all eighteen arc modules rebuilt with `.olean`s deleted — exit 0, no linter
output.

---

## ⚠ 2026-08-23 — SIXTH CORRECTION: "the inequality the recursion runs on" was an overclaim

Last entry landed `sum_index_le_index_sepW_add` and called it "the inequality the recursion
runs on". Making the cost **concrete** this turn showed that claim is not established.

### The new lemmas

```
sum_map_inv_le_length_div        ∑_{k∈l} 1/dₖ ≤ |l| / D   when D ≤ dₖ
sum_map_inv_append_sumElim       cost splits across the two variable groups
cost_bound_of_bounded_order      per-entry cost ≤ r/D₁ + r/D₂
sum_index_le_index_sepW_concrete r·index P ≤ index U + index V + r²(1/D₁ + 1/D₂)
```

All axiom-clean; eighteen arc modules rebuilt with `.olean`s deleted, exit 0, no linter output.

### ⚠ What the concrete form exposes

`r` is the length of a **minimal** separated representation, so `r ≤ (number of distinct
x-monomials of P) ≤ d₁ + 1`. Then `r²/D₁ ≈ d₁`, and the error term is of the same order as the
trivial bound on the index itself. **In that regime the inequality is true but useless.**

The classical proof does not have this problem, and the reason is specific: it measures the
Wronskian's index against the **Wronskian's own** degree vector. `W` has degree `≤ r·d₁` in
`x`, so `index W` is taken with weights `r·d`, not `d`. **Every statement in this arc uses one
degree vector `d` throughout** — `index_sepW`, `sum_index_le_index_sepW_add`, and the concrete
form all inherit that.

So the honest status: the inequality is **proved and correct**, and it is **not established**
that it is the form Roth's lemma needs. Supplying the rescaling — an `index (r • d) …` variant,
or a lemma relating `index d` to `index (r • d)` — is unfinished work the recursion will force.

### Why this one is different from the previous five

The first five corrections were all *missing pieces* found by asking "what supplies this?".
This one is a **wrong constant regime** in a piece that exists and is correct. No audit of
names or shapes would have caught it: `sum_index_le_index_sepW_add` typechecks, composes by
`rfl`, and has a tight validation instance. What caught it was **instantiating the abstract
parameter** — replacing `C` by an actual formula and then reading the magnitude.

That suggests a sixth habit alongside the others: when a statement carries an abstract
constant, compute it before believing the statement is usable. A hypothesis named `C` hides
whether the theorem says anything.

### Open

* The **degree rescaling** — newly identified, and a prerequisite rather than a detail.
* The **recursion**: `ω(m, ε)`, the choice of bounded-order `Dx`, `Dy`, and the arithmetic.

⚠ Nothing here should be read as "the index side of the induction step is done". The module
docstrings now say so at the two places the claim was made.

---

## 2026-08-23 — the degree rescaling, as a tool

The previous entry identified the missing rescaling as a prerequisite. Three lemmas in
`RothIndex.lean`, all axiom-clean:

```
idxWeight_scale_degree     idxWeight (c·d) i = idxWeight d i / c
le_index_scale_degree_iff  θ ≤ index_{c·d} P  ↔  c·θ ≤ index_d P
index_scale_degree_le_iff  index_{c·d} P ≤ θ  ↔  index_d P ≤ c·θ
```

Both directions are needed and they are used differently: the induction *hypothesis* supplies
**upper** bounds on the factors' indices (`index_scale_degree_le_iff`), while the assumption
being contradicted is a **lower** bound on `index P` (`le_index_scale_degree_iff`).

Stated as iffs on bounds rather than as `index_{c·d} = index_d / c`, because `WithTop ℚ` has no
usable division and `⊤` has to survive. The upper-bound one goes through `Finset.inf_le_iff`,
which needs the bound below `⊤` — a coerced rational always is.

`idxWeight_scale_degree` needs **no hypothesis on `c`**: at `c = 0` both sides are `0`, since
`x / 0 = 0` in `ℚ`. The two index versions do need `c ≠ 0`.

The scale factor is pinned by `degreeOf_mvGenWronskian_le`: a Wronskian of `r` functions of
degree `≤ d` has degree `≤ r·d`, so it is exactly `r`.

### ⚠ Available is not applied

**This is a tool, not a fix.** No statement in the arc is yet phrased in rescaled weights —
`index_sepW`, `sum_index_le_index_sepW_add` and `sum_index_le_index_sepW_concrete` all still
use a single `d` throughout. So the sixth correction stands: it is still **not established**
that the induction step's inequality is in the form Roth's lemma needs.

Both places in `RothInductionStep.lean` that discuss the gap now say "available, not applied"
rather than implying it is closed. Writing a "tool exists" note as though it were a fix would
be the same move this arc has had to correct six times.

### Open

* **Apply** the rescaling: restate the step's inequality with the Wronskian's index measured
  against `r·d`, and check the error term is then small. This is where the sixth correction
  gets resolved or confirmed.
* The **recursion**: `ω(m, ε)`, the choice of bounded-order `Dx`, `Dy`, the arithmetic.

Verification: all eighteen arc modules rebuilt with `.olean`s deleted — exit 0, no linter
output.

---

## ⚠ 2026-08-23 — the rescaling is APPLIED, and it CONFIRMS the sixth correction

`index_le_of_rescaled_factor_bounds` in `RothInductionStep.lean`, axiom-clean:

> Given upper bounds `εU`, `εV` on the two factors' indices **in their own degree vectors** —
> the shape the induction hypothesis produces — and a lower bound `θ` on `index P`:
>
> `θ ≤ εU + εV + (r/D₁ + r/D₂)`

The rescaling is what makes `εU`, `εV` come out un-divided: without it the induction
hypothesis simply does not apply to `U` and `V`, because they have degree `r·d`, not `d`.

### The error term improved by a factor `r` — and is still too large

Down from `r²(1/D₁ + 1/D₂)` to `r(1/D₁ + 1/D₂)`. But `r` is the length of a minimal separated
representation, bounded by the number of distinct monomials in the split-off group — of order
`D₁`. So `r/D₁` is of order **1**, while Roth's lemma needs `index ≤ m·ε` with `ε` small. And
`r/D₂` is worse: under the growth condition the two degree scales differ by `ω`, so that term
is of order `ω`.

⚠ Two honesty points about that estimate:

* **`r ≲ D₁` is not proved here.** It is a plausible bound on minimal-representation length,
  and the whole magnitude argument rests on it. I did not formalise it.
* **The theorem is correct regardless.** What is in question is whether it is *strong enough* —
  a statement about constants, not validity.

### Why this is a stopping point rather than another lemma

Every step in the chain is **tight given only "operators have order at most `r`"**:
`sum_map_inv_le_length_div` is tight when all degrees equal the floor; `cost_bound_of_bounded_order`
is tight when every list has full length; `index_det_ge` is tight at the minimising permutation.
So the loss is **structural**, not a slack constant to be shaved — it has to be repaired
upstream of these statements.

I tried to reconstruct the classical bookkeeping and could not, and I record the attempts
rather than a guess:

* splitting off the **first** (largest-degree) variable gives `r ≤ d₁+1` and `r/d₂ ≈ d₁/d₂ ≥ ω`
  — catastrophic;
* splitting off the **last** (smallest-degree) variable gives `r ≤ dₘ+1` and `r/dₘ ≈ 1` —
  still order 1.

Neither yields a small error, so the actual proof must differ structurally from what this arc
has built — a different choice of operators, or the index measured against something other
than these weights. **Determining which needs the source text, not more Lean.**

### Open

1. ⚠ **Consult the actual proof of Roth's lemma** and identify where this arc's structure
   diverges. That is now the blocking item, and it is a reading task.
2. The recursion proper (`ω(m, ε)`, choice of `Dx`, `Dy`, arithmetic) — blocked on (1).

The seven corrections so far were all found by measurement inside Lean. This one is the first
that measurement can only *detect*, not *fix*.

Verification: all eighteen arc modules rebuilt with `.olean`s deleted — exit 0, no linter
output.

---

## ⚠ 2026-08-23 — THE SOURCE ARRIVED (commit `ca1ae1a2eb`), and it diagnoses the sixth correction

Four PDFs uploaded to `uploads/`. **They are not all about the same theorem**, and the
distinction matters enough to record first.

### ⚠ Two different "Roth's theorems"

| paper | theorem |
|---|---|
| `roth_lemma.pdf` — Mahler, *Lectures on Diophantine Approximations*, Ch. 5 | Roth's **lemma** (Diophantine) — **this arc** |
| `2111.12409v4.pdf` — Dolce–Zucconi, adelic curves | Roth's **approximation** theorem, generalised |
| `2605.19310v1.pdf` — Lewko, "A Fourier-free density-increment proof" | Roth on **3-term arithmetic progressions** |
| `noniterativeroth2.pdf` — Croot–Sisask | Roth on **3-term arithmetic progressions** |

The last two are **density Ramsey theory** (1953): every positive-density subset of `[N]`
contains a 3-AP. This arc is Roth's **approximation** theorem (1955): irrationality measure 2.
Same author, unrelated results, no shared machinery. Fourier-free proofs of the 3-AP theorem
do not transfer here.

### Mahler Ch. 5 diagnoses the sixth correction precisely

The blocking item was "consult the source". Doing so:

**What this arc got right.**
* The cost bound is right. Mahler §13's operators `Λ_μν` have total order `≤ μ−1` in
  `x₁..x_{m−1}` and exactly `ν−1` in `x_m`; summed over a permutation that is
  `≈ n²/(2r_{m−1}) + n²/(2r_m)` — matching `cost_bound_of_bounded_order`'s `r²(1/D₁+1/D₂)` up
  to a factor 2.
* **The rescaling is exactly right.** §12 sets `p_h = n·r_h` and uses
  `J(W; r) = n·J(W; p)` — literally `le_index_scale_degree_iff` /
  `index_scale_degree_le_iff` from the previous entry.
* Property (C), `J(A_{j}) ≥ max(0, J(A) − ∑ j_h/p_h)`, is `index_le_index_pderivList_add`.
* Property (A), `J(A±B) ≥ min(J(A),J(B))`, is `index_add_ge`.

**What this arc got wrong — and it is not the constant.**
`index_le_of_rescaled_factor_bounds` combines the pieces **linearly** and divides through by
`r`. Mahler does not. §13 introduces `N = ⌊(J(A)−t)·r_m⌋ + 1` and **splits on `n ≤ N` versus
`n > N`**, yielding

    J(A) ≤ t + 2·max( √(J(W)/n), … )

— a **square root**, with `t` a free parameter (`0 < t ≤ 1`) optimised at the end, and
`c_m = 2^m − 3` accumulating over the induction. A linear combination cannot produce that, so
the previous entry's "the error term is of order 1, therefore unusable" was measuring the
wrong quantity: the argument never divides through.

**A concrete lemma this arc is missing.** Mahler's property (B) is
`J(AB) = J(A) + J(B)` — an **equality**. This arc has only `index_mul_ge` (`≥`), plus
`index_separated` (equality, but only for *disjoint* variable groups). §12 uses the equality.
Over a domain it should hold generally: the index is the order of vanishing in an auxiliary
variable, and orders add.

**Structure of the split.** `(x₁,…,x_{m−1})` versus `(x_m)` alone — `V` is **univariate**.
This arc's `σ ⊕ τ` machinery covers it, with `τ = Unit`.

### ⚠ Pre-Archimedean — the answer is in Mahler's own footnote

> "Put `w(A) = e^{−J(A)}` … `w(A)` is a **non-archimedean valuation** on the ring of
> polynomials."

Properties (A) and (B) are exactly the ultrametric and multiplicativity axioms. So the entire
Roth's-lemma layer **is already non-Archimedean** — which independently confirms the third
correction, that the Mahler-measure machinery (`MahlerJensen.lean`, circle averages, `ℂ[X]`)
is not needed by it. That module remains proved and axiom-clean, and remains unused.

For a genuinely place-uniform treatment, `2111.12409v4` (Chen–Moriwaki adelic curves) is the
framework: a field plus a measure space of places with a product formula, Archimedean and
non-Archimedean handled together. That is a different and much larger project than finishing
Roth's lemma.

### Revised open list

1. **`index_mul_eq`** — upgrade `index_mul_ge` to an equality over a domain. Mahler's (B),
   used by §12. Concrete and provable.
2. **Redo the induction step non-linearly** — the `n ≤ N` / `n > N` case split and the
   square-root bound. This replaces `index_le_of_rescaled_factor_bounds` as the step's
   conclusion.
3. `ω(m, ε)` and `c_m = 2^m − 3` then come out of the recursion rather than being guessed.

⚠ The sixth correction is now **explained, not repaired**: the inequality is still linear and
still too weak. What changed is that the fix is known and local, rather than unknown.
