---
# qou-4lbh
title: 'Roth''s lemma: the height theory is the real cost, not the Wronskians'
status: completed
type: task
priority: normal
created_at: 2026-08-21T16:31:55Z
updated_at: 2026-08-29T19:34:43Z
---

**Roth's Lemma is proved** — `MvPolynomial.index_le_rothBound`, every arity, no hypotheses
beyond `Γ_m` itself, no `sorry`, standard axioms. Merged to main as PR #5737.

Child of `qou-br3w`. Successor to `qou-sq3h`, which is complete.

⚠ This summary read "what remains is the m=1 base case, blocked on height theory" until
2026-08-29 — a stale claim the arc carried for five days while landing twenty-six corrections,
three of which were *about* stale prose. The bean's own header was the last instance and the
one nothing checked. See `## Summary of Changes` at the end.

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

---

## 2026-08-23 — coefficient rings, audited; and §13's square-root bound, formalised

### Which ring is the arc over? (measured, not remembered)

| module | ring |
|---|---|
| `RothIndex`, `SeparatedHeight`, `SeparatedWronskian`, `WronskianIndex`, `MvPolynomialHeight` | general `[CommRing R]` |
| `SeparatedIndex`, `RothInductionStep`, `MvGenWronskian`, `RothHeightBound` | `[CommRing R]` **+ `IsDomain`** where used |
| `BoundedOrderWronskian`, `SeparatedRepresentation` (minimal version) | `[Field K]` |
| `MvPolynomialHeight`, `SeparatedHeight`, `WronskianHeight` (height side) | pinned to **`ℤ`** |
| `RothBaseCase`, `RothLemmaStatement` | `ℤ` with the index over **`ℚ`** |
| `MahlerJensen` | **`ℂ`** — and unused by everything else |

So: **general `CommRing` wherever it works**, with `IsDomain` added only where genuinely
needed (`index_separated`'s `≤` half, Gauss in `RothHeightBound`), `Field` where division is
needed (minimal representations, the bounded-order criterion), `ℤ`/`ℚ` for heights and the
statement, and `ℂ` **only** in the Mahler module — which nothing downstream uses. That last
row is the third correction showing up as a measurement.

### §13's arithmetic, formalised

New module `QOU/Mathlib/RothRecursionArith.lean` — pure `ℚ`, Mathlib-only, axiom-clean:

```
sum_range_div                Gauss's sum, divided through
sum_max_sub_ge               ∑_{ν<n} max(0, θ − ν/r) ≥ Kθ − K(K−1)/(2r)   for any K ≤ n
sq_mul_le_two_mul_of_sum_le  θ²·r ≤ 2S   given θr ≤ n and the sum ≤ S
```

The last is Mahler's second case, stated **squared** so no `Real.sqrt` is needed and
everything stays in `ℚ`. The cut-off is `K = ⌈θ·r⌉`: at most `n` by hypothesis, at least `θr`
by the ceiling property, at most `θr + 1` — which is exactly what makes the correction term
`K(K−1)/(2r)` at most half of `Kθ`.

⚠ **A misreading of the source, avoided.** The first case's conclusion `J ≤ t + S` holds
**unconditionally**, not only when `n ≤ N`: it is just the `ν = 0` term, since every term is
non-negative. So the case split's entire content is the second case. Reading the source as
"two cases, two bounds" would have suggested formalising a trivial one alongside the real one.

⚠ **Provenance.** Reconstructed from a partly illegible scan. The *structure* is legible;
several constants are not. What is landed is Lean-checked and therefore true — what is **not**
established is that its constants match Mahler's. The module header says so, and anyone wiring
it in should re-derive against a clean copy.

### Open

1. **Wire it in**: produce `∑_{ν<n} max(0, θ − ν/r)` from `index_det_ge` +
   `index_le_index_pderivList_add`, with `θ = index P − t` and `r` the split-off degree. This
   replaces `index_le_of_rescaled_factor_bounds`, whose linear shape the sixth correction
   rejected.
2. Then `ω(m, ε)` and `c_m = 2^m − 3` fall out of the recursion.

Verification: all nineteen arc modules rebuilt with `.olean`s deleted — exit 0, no linter
output.

---

## 2026-08-23 — the sixth correction is repaired: the bound is square-root, not linear

Open item 1 from the previous entry is done. The two halves that were proved separately are
now joined, so the arc no longer has an arithmetic lemma sitting beside an index lemma with
nothing between them.

### What landed

`QOU/Mathlib/WronskianIndex.lean` (index side, `WithTop ℚ`, general `[CommRing R]`):

```
coe_sum_withTop       (∑ f i : ℚ) ↑ = ∑ (f i)↑            — by Finset induction; WithTop ℚ
                                                            is not a semiring, so no map_sum
coe_sub_le_of_le_add  θ ≤ x + c  ⊢  θ − c ≤ x             — case split on x = ⊤
sum_max_le_index_det  ∑_{j<r} max(0, θ − t − j/rr)
                        ≤ index (det (∂_{D i j} P))       — the bridge
```

`QOU/Mathlib/RothInductionStep.lean` (the join):

```
sq_index_le_of_det_bound   (θ − t)² · rr ≤ 2S
```

from `sum_max_le_index_det` + `RothArith.sq_mul_le_two_mul_of_sum_le`.

### Why this is the repair and not another lemma

The sixth correction said `index_le_of_rescaled_factor_bounds` was too weak and that the loss
looked structural. It was not structural — it was in **dividing the summed inequality through
linearly**, which discards the fact that the per-column cost `t + ν/rr` *grows*. Columns past
the cut-off `(θ−t)·rr` contribute nothing but `index ≥ 0`; keeping that truncation is what
turns a bound on `θ − t` into a bound on `(θ − t)²`. The `max 0` in `sum_max_le_index_det` is
that truncation, and it is where the whole gain lives.

Two details worth recording, because both were places the proof could have gone wrong:

* `index_det_ge` bounds the determinant's index below by the `Finset.inf` over permutations,
  not by any particular diagonal. `sum_max_le_index_det` picks the minimising `p₀` with
  `Finset.exists_mem_eq_inf` and bounds *its* diagonal — sound only because the cost
  hypothesis `hc` is uniform in the row index `i`. A per-`(i,j)` cost that varied in `i`
  would not survive this step.
* The `max 0` cannot be dropped. `sum_max_truncation_active` computes both sums at
  `θ = 1, r = 1, n = 3`: truncated `= 1`, untruncated `= 0`. The untruncated one is *smaller*,
  which is the wrong direction — a version without `max` would not just be weaker, it would
  be estimating the wrong quantity.

### Non-vacuity

- `RothArith.sum_max_truncation_active` — the truncation changes the value (above).
- `RothArith.sq_mul_le_two_mul_witness` — hypotheses satisfiable at `θ=1, r=1, n=3, S=1`.
- `MvPolynomial.sq_index_le_of_det_bound_witness` — hypotheses jointly satisfiable at
  `σ = Fin 1`, `P = X₀`, `r = 1`. ⚠ Stated in its own docstring: this certifies
  satisfiability only; with `r = 1` there is one column and **nothing is clipped**, so it does
  not exercise the truncation. That is what the first witness is for.

### Status, stated honestly

What is now true: the arc has the **right shape** for §13's conclusion, Lean-checked, on the
standard axiom set. What is **not** established: that the constants close the induction. That
is a question about `ω(m, ε)`, and it is downstream of the provenance caveat below.

⚠ **Provenance, carried forward.** `RothRecursionArith`'s constants were reconstructed from a
partly illegible scan of Mahler §13. The structure — truncated sum, square-root conclusion —
is what the source shows and what is proved. The numeric bookkeeping is not established
against a clean copy, and no downstream constant should be asserted until it is.

### Open

1. Choose the operator families `Dx`, `Dy` so that `hc`'s per-column cost `t + j/rr` actually
   holds — a construction, not an estimate, and the last input `sq_index_le_of_det_bound`
   needs that the arc does not have.
2. `index_mul_eq` — Mahler's property (B) is an **equality** `J(AB) = J(A) + J(B)`; the arc
   has only `index_mul_ge` plus `index_separated` for the disjoint case. §12 appears to use
   only the disjoint case, so this may not be needed; check before proving it.
3. Then `ω(m, ε)` and `c_m = 2^m − 3`.

Verification: all nineteen arc modules rebuilt with `.olean`s deleted — exit 0, no errors and
no linter output. All seven new/underlying declarations `#print axioms`-clean on
`[propext, Classical.choice, Quot.sound]`.

---

## 2026-08-23 — §13 finished, and an eighth correction found by the vacuity audit

Read §13 of the source directly rather than working from the reconstruction. Three things it
settled, then the correction it produced.

### The source confirms the shape that was guessed

§13's determinant is `det(A_{μν} A)` where `A_{μν} = Δ_{j_{μ1},…,j_{μ,m−1}, ν−1}` with
`∑_{h<m} j_{μh} ≤ μ−1` and order exactly `ν−1` in the last variable. That is a matrix of
derivatives of a **single** polynomial — exactly `M i j = pderivList (D i j) P`, not a
Wronskian of `r` distinct functions. `sum_max_le_index_det` was written to the right shape.

It also confirms the detail that made the permutation step legal: the row index `μ` bounds
`∑_{h<m} j_{μh} ≤ t` and the column index `ν` contributes `(ν−1)/r_m`, so the cost is
**uniform in the row**. A cost varying in `i` would break `sum_max_le_index_det`, and the
source is the reason it does not.

And it confirms the constants: Mahler's case-2 conclusion `J(A) < t + 2√(J(W)/r_m)` is the
weakening of `θ − t ≤ √(2S/r_m)`, which is exactly `sq_mul_le_two_mul_of_sum_le`. The factor
`2` in place of `√2` is his, and costs nothing.

### ⚠ Eighth correction: Mahler's `max` is an artefact, and transcribing it produced a theorem that says nothing

§13 ends by combining its two cases as `J(A) < t + max(J(W), 2√(J(W)/r_m))`. That was written
here literally, as `θ ≤ t + 2 * max S q`, and built. Writing its non-vacuity witness is what
exposed it: for `0 ≤ S`, `2·max S q ≥ 2S ≥ S`, so the statement is **implied by
`index_le_add_of_det_bound`** (`θ ≤ t + S`) alone. It is a true theorem that carries no
information about determinants at all.

Mahler needs the `max` because he knows only that *one* of his two cases holds. Case (1) is
unconditional here — the `j = 0` term of `sum_max_le_index_det`, every other term
non-negative — so there is nothing to hedge against, and the `max` protects the branch that
never fails while discarding the branch that is strong.

`max_form_implied_by_case_one` is landed as the record: a one-line proof that the discarded
statement follows from case (1). Nothing else uses it.

This is the vacuity audit doing the job the previous seven corrections were found by hand.
Worth noting: the *build* was green for the max form. Nothing about `lake build` or
`#print axioms` would ever have caught it.

### What replaced it

```
index_le_add_of_det_bound   θ ≤ t + S                     — case (1), unconditional, r > 0
index_le_of_det_bound       θ ≤ t + 2q                    — given S ≤ q²·rr and S·rr ≤ r
```

The second is stronger than anything in the source's combined display. The gain is moving
the branch hypothesis off `θ`: `sq_index_le_of_det_bound` needs `(θ−t)·rr ≤ r`, which mentions
the quantity being bounded (Mahler's `n > N` has the same defect), but case (1) gives
`θ − t ≤ S`, so **`S·rr ≤ r` implies it**. A caller can discharge `S·rr ≤ r` without already
knowing the answer.

Non-vacuity: `index_le_of_det_bound_witness`, same `1 × 1` instance, labelled in its docstring
as certifying satisfiability only.

### Open — no longer inequalities

1. **The operator family.** Build §13's `D : Fin r → Fin r → List σ` and prove `hc` for it.
   A construction; the arc has none.
2. **The determinant is non-zero.** `hS` is unsatisfiable at `det = 0` (`index = ⊤`), so
   `BoundedOrderWronskian`'s non-vanishing is a real precondition, not bookkeeping.
3. **`S·rr ≤ r` in the recursion's regime** reads `Φ_m · r_m ≤ 1` with `S = nΦ_m`, `rr = r_m`,
   `r = n`. Unchecked against the parameter conditions — do not assume it.

⚠ Provenance narrows but does not close: §13's *structure* is now read directly and matches.
The surrounding parameter bookkeeping (`ω(m,ε)`, `c_m = 2^m − 3`) is still from the illegible
region and must be re-derived against a clean copy.

Verification: nineteen arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no
linter output. Four new declarations `#print axioms`-clean.

---

## 2026-08-23 — §13's operator family, constructed; the remaining input is now one statement

Open item 1 from the previous entry. New module `QOU/Mathlib/RothOperatorFamily.lean`
(20th in the arc, registered in `QOU.lean` so it is not an orphan).

### The bridge that made it short

```
sum_map_inv_eq_idxWeight   the "cost" in hc IS idxWeight of the operator's multi-index
idxWeight_le_of_sum_le     total order ≤ N and degrees ≥ D  ⟹  weight ≤ N/D
```

The first is the conceptual step. `index_le_index_pderivList_add` and `index_le_of_det_bound`
both speak of `∑_{k ∈ l} 1/d k`, and `idxWeight` speaks of `∑_j i_j/d_j`; saying they are the
same object makes `idxWeight`'s additivity do all the work. The second converts Mahler's row
constraint (a bound on *total order*) into a cost bound, which is the only place the degree
floor `D` is used.

### The family

```
rothOpFamily z L μ ν = L μ ++ List.replicate ν z
cost_rothOpFamily_le   cost ≤ t + ν/(d z)      given a UNIFORM row bound t
index_le_of_rothOpFamily   θ ≤ N/D + 2q        §13 with every hypothesis about the data
```

Design note worth keeping: the row part is a **list**, not a multi-index. The multi-index form
needs `exists_multiIndexOf_eq`, whose witness is a `Classical.choose` and therefore opaque —
no concrete instance can be evaluated through it, so no witness could be written.
`exists_rothOpFamily_of_idxWeight_le` recovers the multi-index form as a corollary, so nothing
is lost. I only noticed this because the witness would not go through.

Where the uniformity lives is the point: `ht` quantifies over rows with a single `t`. That is
not stylistic — `sum_max_le_index_det` picks the permutation minimising the diagonal sum, and
may only do so because the bound does not depend on which row it lands in. Mahler's shape
(`∑_{h<m} j_{μh} ≤ μ−1` on the rows, order exactly `ν−1` in the last variable on the columns)
has that property, and a family that put the growth in the row would not.

### A non-degenerate witness, at last

`index_le_of_rothOpFamily_two_witness`: `σ = Fin 1`, unit degree, `P = X₀²`, row lists
`![[], [x₀]]`, giving

```
⎡ P    ∂P  ⎤   ⎡ X²   2X ⎤
⎣ ∂P   ∂²P ⎦ = ⎣ 2X   2  ⎦      det = 2X² − 4X² = −2X²  ≠ 0
```

so `N = 1`, `S = 2`, `q = 3/2`, conclusion `2 ≤ 1 + 3`. This is the first witness in this part
of the arc with **distinct rows** and a **non-vanishing determinant** — the earlier `1 × 1`
ones certify satisfiability but cannot fail to have a non-zero determinant, so they say
nothing about the configuration the theorem exists for. Here the column cost genuinely grows.

⚠ Still not exercised by it: the truncation. `θ − t = 1`, `rr = 1`, so the cut-off is `1` in a
`2`-column matrix and `max 0` never fires. `RothArith.sum_max_truncation_active` remains the
guard for that, and the docstring says so.

Needed one new lemma upstream: `index_C_mul` (with `support_C_mul`) in `RothIndex.lean` — a
Wronskian of powers is always a *scalar multiple* of a monomial, and the scalar is an artefact
of differentiating, not part of the vanishing behaviour. `index_smul_units` covered only `ℤˣ`.

### Open — one statement, and it is not an inequality

⚠ **The determinant is non-zero.** `index_le_of_rothOpFamily`'s `hS` asserts
`index d α (det …) ≤ ↑S`, which is **unsatisfiable** when the determinant vanishes
(`index d α 0 = ⊤`). Nothing here supplies non-vanishing.

`BoundedOrderWronskian` has the criterion — linear independence ⟺ some bounded-order
generalized Wronskian is non-zero — but stated for `mvGenWronskian D f`, a Wronskian of `m`
**distinct functions**, whereas §13's matrix is derivatives of a **single** `P`. Relating the
two is §7 of the source, which this arc has not read. That is the next thing to read, not the
next thing to prove.

After that: `ω(m, ε)`, and the `S·rr ≤ r` check (`Φ_m·r_m ≤ 1`) that is still unverified
against the parameter conditions.

Verification: twenty arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no linter
output. Eleven declarations `#print axioms`-clean. Orphan gate re-run: 2037 modules, 1154
reachable (up one), 883 not built — the new module is reachable, so the inherited red did not
grow.

---

## 2026-08-23 — the determinant's non-vanishing: it was blocked on reading, not on proving

The item I called "the arc's remaining input" is closed, and the way it closed is the lesson.

### It was in §6, and every piece was already here

I had said the next step was to read §7 ("Majorants for U, V and W"). Wrong section — §13's
reference is to the *identity*, which is **§6**. And §6's argument needs nothing new:

* write `A = ∑ₖ Pₖ(x₁,…,x_{m−1}) Σₖ(x_m)` in a **minimum** representation;
* in a minimum representation both families are linearly **independent** (else you could
  shorten it — the source proves exactly this);
* Lemma 1 gives bounded-order Wronskians `U*`, `V**` that do not vanish;
* differentiating the representation with the *combined* operators `D_{μν} = D*_μ D**_ν`
  gives a matrix identity, and by the **multiplication law for determinants**

      det (D_{μν} A) = U*(x₁,…,x_{m−1}) · V**(x_m);

* a product of two non-zero polynomials over a domain is non-zero.

Mapped onto the arc: `exists_separated_representation_indep` **is** the minimum
representation, `exists_bounded_order_mvGenWronskian_ne_zero` **is** Lemma 1, `sepW_eq`
(`det_separated_wronskian`) **is** the multiplication law. `exists_sepW_ne_zero` is eleven
lines of composition.

⚠ Those pieces have been in place since `SeparatedRepresentation` landed. The item was
blocked on **reading the source**, not on proving anything — and I spent the previous turn
describing it as the hard remaining input. Recording that because it is the cheapest kind of
mistake to repeat: the arc's habit of composing existing lemmas is good, but it does not help
if the composition is never looked for.

### What landed

`QOU/Mathlib/RothOperatorFamily.lean`:

```
exists_sepW_ne_zero            some bounded-order family has non-vanishing determinant
exists_index_le_of_ne_zero     P ≠ 0 ⟹ ∃ S, index ≤ ↑S      (the form hS wants)
cost_sepW_le                   COLUMN-GRADED cost: ≤ r/D₁ + j/D₂
exists_index_le_of_separated   §13 for any non-zero P, every input discharged
```

`QOU/Mathlib/RothIndex.lean`: `translate_neg_translate`, `translate_injective`,
`translate_eq_zero_iff` — needed because `index_eq_top_iff` is stated in terms of
`translate α P = 0`, and nothing said that is the same as `P = 0`. ⚠ Deliberately **not**
`@[simp]`: `translate` appears unfolded in several proofs in this arc and a new rewrite rule
would change what `simp` does to them.

`cost_sepW_le` is worth naming separately: `cost_bound_of_bounded_order` already gave the
*uniform* bound `r/D₁ + r/D₂`, and the column-graded `r/D₁ + j/D₂` is the entire difference
between the linear conclusion the sixth correction rejected and §13's square root.

### ⚠ Status, stated carefully

§13 is **derived** — no gaps, no assumed inputs, standard axioms. It is **not** established
that its constants are good enough, and two things are open, of which the second is the sixth
correction in its final form:

1. **`S·D₂ ≤ r`, i.e. `Φ_m·r_m ≤ 1`.** A side condition the caller must discharge. Unchecked
   against Roth's lemma's parameter conditions. Test it first: if it fails in the intended
   regime the square-root branch never fires and the repair buys nothing.
2. **`t = r/D₁` versus the source's constant `t ≤ 1`.** `r` is the minimum representation
   length, `D₁` the degree floor. The source *chooses* `t` small; the arc *derives*
   `t = r/D₁`. Whether that is small enough is a statement about representation length versus
   degree, and the arc does not have it. This is exactly what the sixth correction was
   pointing at, now isolated to one ratio instead of diffused across the argument.
3. The recursion itself (§14) — `ω(m, ε)`, and feeding the `m−1` case back in.

⚠ Provenance narrows again: §6 and §13 have now both been read directly and match. §14 has
not been read, so `ω(m, ε)` and `c_m = 2^m − 3` remain unasserted.

Verification: twenty arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no linter
output. Nine declarations `#print axioms`-clean on the standard set. No `sorry`/`admit`/
`native_decide`.

---

## 2026-08-23 — ⚠ NINTH CORRECTION: the eighth was wrong, and the check that found it

I said the next step was to test the side condition `S·D₂ ≤ r` (`Φ_m·r_m ≤ 1`) against the
parameter conditions, because "if it fails in the intended regime the square-root branch never
fires and the repair buys nothing." **It fails.** Tracing why found a mis-transcription, and
that mis-transcription is what produced the eighth correction.

### What §13 actually says

The combined display is

    J(A) < t + 2 max( J(W)/n , √(J(W)/r_m) ).

I transcribed the first branch as `J(W)`, dropping the **`1/n`**. Correction 8 then observed —
correctly — that `θ ≤ t + 2·max S q` is implied by `θ ≤ t + S` and therefore says nothing, and
concluded that Mahler's `max` was an artefact of his case split and that the strong branch
should be extracted alone. That conclusion is **wrong**:

* with the `1/n` restored, the combined statement is **not** implied by `θ ≤ t + S`. `2S/n`
  can be far smaller than `S`, and in the application it is: `S` is of size `n·Φ_m`, so `2S/n`
  is of size `Φ_m` while `S` is of size `n·Φ_m`. The separating factor is the matrix size.
* so the `max` combines two *useful* bounds. It is not hedging.
* and because the two branches are complementary **by construction**, the combination needs no
  side condition at all.

Case (1) sharpened (`RothArith.le_two_mul_div_of_sum_le`): when `(n−1)/r ≤ θ` every term is
unclipped, so `J(W) ≥ nθ − n(n−1)/(2r)`, and `(n−1)/r ≤ θ` makes the correction term at most
`nθ/2`, leaving `J(W) ≥ nθ/2`. That is where the `2/n` comes from — Gauss's sum eating half.

### The cost of the error, and what it cost me

`index_le_of_det_bound` carries `S·rr ≤ r`, introduced **because** case (1) looked worthless
and the strong branch had to be forced. In the recursion's regime that reads `Φ_m·r_m ≤ 1`,
which is false — `Φ_m` is small but `r_m` is a large degree. So the theorem is sound and its
hypothesis is unsatisfiable exactly where it is wanted.

⚠ Two things about how this was caught, both worth keeping:

* **The check is what found it.** Carrying `S·rr ≤ r` as a documented caveat would have hidden
  a wrong theorem behind an honest-looking warning indefinitely. A side condition nobody tests
  is indistinguishable from a bug.
* **No witness could have found it.** All three non-vacuity witnesses sit at `r = 1` or
  `r = 2`, where `S·rr ≤ r` is perfectly satisfiable. The hypothesis only fails asymptotically.
  Finite examples test vacuity; they do not test *usefulness*, and this arc has now been bitten
  by the difference twice (correction 6 was the same species).

### What landed

`RothRecursionArith` (pure ℚ):

```
le_two_mul_div_of_sum_le   (n−1)/r ≤ θ  ⟹  θ ≤ 2S/n          — sharp case (1)
le_two_mul_max_of_sum_le   θ ≤ 2·max(S/n, q)  for S ≤ q²r     — combined, NO side condition
```

`RothInductionStep`: `index_le_two_mul_max_of_det_bound`, the index-side form, plus a witness.
`index_le_of_det_bound` and `max_form_implied_by_case_one` are **kept and relabelled** as the
record of the error rather than deleted.

`RothOperatorFamily`: `exists_index_le_of_separated` no longer takes `S·D₂ ≤ r`.

### Where the constants stand now

`S/r` is of size `Φ_m` and `q ≈ √(S/D₂) = √(nΦ_m/r_m) ≈ √Φ_m` since `n ≤ r_m + 1`. So §13's
conclusion is `θ ≤ t + 2·max(Φ_m, √Φ_m)` — **Mahler's Lemma 4**. The only remaining constant
question is `t`, and it now has a shape:

1. **Bound the minimum representation length**: `r ≤ d(split-off variable) + 1`, i.e. Mahler's
   `n ≤ r_m + 1`. True — expand `P` in powers of the split-off variable — but **not proved
   here**: `exists_separated_representation_fin` splits on the `σ`-monomials, so `r` is the
   number of those, and `exists_indep_representation` only shortens without recording by how
   much.
2. **Feed it to `RothGrowth`**, which makes the split-off variable's degree the *smallest*, so
   `D₁ ≥ ω·d(split-off)` and `t = r/D₁ ≲ 1/ω`. Choosing `ω ≥ 2/ε` gives `t ≤ ε/2`.

That would determine **`ω(m, ε)`** — the one entry `RothLemmaStatement`'s audit came back
empty on.

⚠ Provenance: §6 and §13 have now been read directly and match. §11 (property `Γ_m`) and §14
are in the illegible region and have **not** been read. Steps 1 and 2 are the arc's own
reconstruction of what the growth condition must be doing, not a transcription.

Verification: twenty arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no linter
output. Five new declarations `#print axioms`-clean.

---

## 2026-08-23 — Mahler's `n ≤ r_m + 1`: the length bound is a question of which side you group on

Open item 1 from the previous entry. The row cost `t = r/D₁` is made of the minimum
representation length, so bounding it bounds `t`.

### The finding

The arc had `exists_separated_representation_monomial`, which groups the monomials of `P` by
their **`x`**-part. That gives one term per `x`-monomial — a count of size `∏_{h<m}(r_h+1)`.
Mahler's bound is one term per **`y`**-monomial, which for a single split-off variable is
`d + 1`.

Those are not close, and no growth condition rescues the first. The two derivations are the
same proof with `.1` and `.2` exchanged; the arc simply had the one that does not help. Worth
recording as its own kind of gap: not a missing theorem, and not a wrong one — a theorem
proved on the wrong side of a symmetry, where the mirror image is the useful one.

### What landed

`SeparatedRepresentation`:

```
exists_separated_representation_monomial_right   group by the y-part; index set EXPLICIT
exists_separated_representation_fin_right        Fin-indexed, r = #{y-monomials}
card_image_snd_le_of_degreeOf                    τ = Unit: #{y-monomials} ≤ d + 1
exists_indep_representation                      now carries r' ≤ r
exists_separated_representation_indep_card_le    minimum representation, length bounded
exists_separated_representation_indep_le_degreeOf   Mahler's n ≤ r_m + 1
```

The index sets are stated **explicitly** rather than existentially, because the whole point is
to count them — an existential `∃ t : Finset _, …` cannot be bounded by the caller.

`RothOperatorFamily`: `exists_sepW_ne_zero_le_degreeOf` and
`exists_index_le_of_separated_le_degreeOf`, which carry the bound through the non-vanishing
argument and into §13's conclusion. **The `t` slot is now `(d+1)/D₁`** — a ratio of degrees,
not of a representation length.

### ⚠ Where the last constant question stands

`t = (d+1)/D₁` is the split-off variable's degree over the degree floor of the others. Turning
that into `1/ω` needs `RothGrowth` to order the degrees so the split-off one is smallest, which
would give `D₁ ≥ ω·d`. **Not proved.**

But note what changed about its character: `RothGrowth` is defined *in this arc*
(`RothLemmaStatement`), so step 2 is a statement entirely inside the formalisation — it can be
proved without reading anything further. That is the first time in this arc that the next
constant step has not been gated on the source.

⚠ It being provable inside the arc does **not** make it the source's argument. §11 (property
`Γ_m`) is in the illegible region and unread; if the source's growth condition differs from
`RothGrowth`, proving the implication proves something about the arc's statement, not about
Roth's lemma. Say which, when it lands.

### Notes from the build worth keeping

- The index-set-explicit statements need `[DecidableEq τ]` in the **statement** — `classical`
  in the proof cannot supply an instance the statement already required. And once it is a
  hypothesis, leaving `classical` in the proof introduces a *second* instance and the
  `Equiv.sum_comp` step fails on an instance mismatch. Removing `classical` fixed it.
- `rw [hP]` rewrote `P` inside `P.support.image …` in the goal's own index set, replacing it
  with the sum. `conv_lhs => rw [hP]` is the fix. The original proof was immune only because
  its index set was existentially bound.

Verification: twenty arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no linter
output. Eight declarations `#print axioms`-clean.

---

## 2026-08-23 — `t ≤ 2/ω`: what the growth condition was for

`RothGrowth` has been in `RothLemmaStatement` since the statement was written and **nothing
used it**. This is what it is for.

```
rothGrowth_antitone      ω ≥ 1 ⟹ degrees are non-increasing along the ordering
rothGrowth_mul_le        every earlier degree is ≥ ω times any later one
rothGrowth_row_cost_le   (d_last + 1) / d_earlier ≤ 2/ω
```

The last is the row cost of the induction step. The `+1` costs a factor `2` because
`d_last ≥ 1`; the `ω` is `rothGrowth_mul_le` directly. **So `ω ≥ 2/ε` forces `t ≤ ε`** — which
is what `ω(m, ε)` has to be, and the entry `RothLemmaUniform` left unconstrained.

`rothGrowth_mul_le` needs the chained (antitone) form, not just the single-step condition: the
degree floor `D₁` ranges over *all* the non-split variables, not only the one adjacent to the
split-off variable.

⚠ **This is the arc's own reconstruction, and it should not be quoted as the source's.**
Property `Γ_m` (§11) is in the illegible region and has not been read. What is proved is a
fact about `RothGrowth` **as this arc defines it**. If the source's condition differs, this
proves something about `RothLemmaUniform`, not about Roth's lemma. Both the module header and
the docstrings say so.

### Where this leaves things

§13 is derived; the row cost is bounded by `2/ω`; the two are **not yet composed** in Lean.
Composing them needs the degree floor as a natural number with `ω·d ≤ D₁ ≤ min_k d₁ k`, which
exists (take `⌈ω·d⌉`) but has not been written. Until it is, "`ω ≥ 2/ε` closes the constant
question" is a **prose** claim of exactly the kind correction 5 was about — two true theorems
that look like they fit. Do not repeat it as established until the elaborator has checked it.

Verification: twenty arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no linter
output. Three declarations `#print axioms`-clean.

---

## 2026-08-23 — the two halves joined: `index ≤ 2/ω + 2·max(S/r, q)`

The previous entry ended by saying "`ω ≥ 2/ε` closes the constant question" is a **prose**
claim of the kind correction 5 was about, and not to repeat it as established until the
elaborator had checked it. It has now checked it. `exists_index_le_of_rothGrowth`:

```
index (Sum.elim d₁ d₂) (Sum.elim α β) P  ≤  2/ω + 2·max(S/r, q)
```

given `RothGrowth`, an ordering in which the split-off variable comes last, and `P ≠ 0`. It
built first try, so the two halves did fit — but that was worth finding out from the compiler
rather than from the prose.

### The one piece of real work in the join

§13 wants a **natural** degree floor `D₁ ≤ d₁ k`; the growth condition supplies the
**rational** bound `ω·d ≤ d₁ k`. `⌈ω·d⌉` sits between them, and that is the only reason a
ceiling appears. Worth noting because it is the kind of gap that reads as bookkeeping in prose
and is a genuine (if small) construction in Lean.

### The sixth correction, closed

The row cost `t` is what correction 6 was about, and it is now bounded by the growth constant
alone. The path took three separate findings, each of which looked like the last one at the
time:

1. the loss was not structural but from **dividing through linearly**, discarding the
   truncation (→ the square-root branch);
2. the combined display's first branch is `J(W)/n`, not `J(W)`, so **both** branches are
   useful and no side condition is needed (correction 9);
3. `t` is a ratio of degrees, not of a representation length — provided the representation is
   grouped on the **`y`**-side.

None of those was visible from the one before it.

### ⚠ What this is, and is not

A fact about **`RothGrowth` as this arc defines it**. Property `Γ_m` (§11) is in the illegible
region and unread. If the source's condition differs, this is a theorem about
`RothLemmaUniform` and not about Roth's lemma. Stated in the module header, in the docstring,
and here.

### Open — structure, not constants

1. **Connect `RothLemmaUniform σ m ω ε` to `exists_index_le_of_rothGrowth`**, which is stated
   for `σ ⊕ Unit` — the `m → (m−1) + 1` split the induction performs. Turning an
   `o : σ ≃ Fin m` into that split and transporting the statement across it is the missing
   structural step.
2. `c_m = 2^m − 3`, from iterating with `rothLemmaUniform_one` as the base. Unasserted until
   §14 is read.

Verification: twenty arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no linter
output. `exists_index_le_of_rothGrowth` `#print axioms`-clean.

---

## 2026-08-23 — `S` is no longer existential: the form the recursion consumes

`exists_index_le_of_rothGrowth` left `S` — the bound on the determinant's index — existential
and unconstrained. Honest, but not usable: the recursion has to *know* `S` is small, and it
knows that because `index_sepW` splits the determinant's index into the two factors' indices,
which the induction hypothesis (the `x` side) and the base case (the single split-off variable)
bound.

```
index_le_of_rothGrowth_of_factor_bound :
    index P  ≤  2/ω + 2·max(Φ, q)        whenever (d+1)·Φ ≤ q²·D₂
```

where `hfac` is the assumption the induction hypothesis discharges: for **any** bounded-order
family realising a separated representation of `P`, the two Wronskians' indices sum to at most
`r·Φ`.

### ⚠ The factor `r` in `hfac` is not slack

It is the source's `J(W) ≤ n·Φ_m`, and it is what makes `S/r ≤ Φ`. Correction 9 is exactly the
observation that the conclusion depends on `S/r` and not on `S`; a hypothesis bounding the
factors by `Φ` *without* the `r` would be asking for something strictly stronger than the
recursion can deliver, and would look fine until the constants were checked.

So the `r` appears twice and cancels: once in `hfac` (from degree rescaling, the source's
`p_h = n·r_h`) and once in §13's `S/r`. Neither is decoration.

### Also landed

`exists_degree_floor` — the ceiling construction and its cost bound, factored out of
`exists_index_le_of_rothGrowth` now that both forms need it. §13 wants a **natural** degree
floor `D₁ ≤ d₁ k`; the growth condition supplies a **rational** `ω·d ≤ d₁ k`; `⌈ω·d⌉` sits
between them. Also `rothGrowth_split`, which reads the growth condition off for the split-off
variable.

### Open — `hfac`, and it decomposes

1. **The `x` side**: `RothLemmaUniform` at `m−1` bounds `index d₁ α (mvGenWronskian Dx φ)`
   given degree and height bounds on that Wronskian. Both exist —
   `degreeOf_mvGenWronskian_le`, `abs_coeff_mvGenWronskian_le`. What is missing is **transport**:
   this is stated for `σ ⊕ Unit`, `RothLemmaUniform` for an `o : σ ≃ Fin m`.
2. **The `y` side**: one variable, so `RothBaseCase` / `rothLemmaUniform_one` applies directly.
3. **The factor `r`**: from `index_scale_degree_le_iff` applied to each factor.
4. Then `c_m = 2^m − 3` by iterating.

⚠ Provenance unchanged: §5, §6, §13 read and matching; §11 and §14 not read; the `2/ω` bound
is the arc's own reconstruction; `c_m = 2^m − 3` unasserted.

Verification: twenty arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no linter
output. Four declarations `#print axioms`-clean. No `sorry`/`admit`/`native_decide`.

---

## 2026-08-23 — the chain now starts at the induction hypothesis's literal shape

`hfac` asked for the two Wronskians' indices summed at the **unscaled** degrees. What
`RothLemmaUniform` actually gives is a bound at a polynomial's *own declared* degrees, and in
the induction step the sub-problems carry the **rescaled** degrees `r·d`. So the hypothesis as
stated was one conversion away from what the recursion produces.

```
factor_bound_of_rescaled              rescaled bounds ⟹ Σ of unscaled indices ≤ r·(εU+εV)
index_le_of_rothGrowth_of_rescaled_bounds   index P ≤ 2/ω + 2·max(εU+εV, q)
```

`factor_bound_of_rescaled` is the **reusable half of `index_le_of_rescaled_factor_bounds`** —
the theorem correction 6 rejected. Its *rescaling* was always right (it is the source's
`p_h = n·r_h`); only the linear conclusion drawn from it was too weak. Isolating the rescaling
lets the good half be used without the bad one, and keeps the superseded theorem as the
record rather than as a dependency.

⚠ The factor `r` shows up twice and cancels: once here (from the rescaling) and once as §13's
`S/r`. Correction 9 is what makes the second one exist. Had that correction not been found,
this conversion would have introduced an `r` with nothing to cancel it, and the bound would
have been off by the matrix size — silently, since every witness in the branch is at `r ≤ 2`.

### The chain, end to end

```
hres  (bounds at the RESCALED degrees — what RothLemmaUniform gives)
  ↓  factor_bound_of_rescaled
hfac  (the two Wronskians' indices sum to ≤ r·Φ)
  ↓  index_le_of_rothGrowth_of_factor_bound
index P ≤ 2/ω + 2·max(εU + εV, q)
```

Everything above `hres` is proved.

### Open — `hres`, in two halves

1. **The `x` half is blocked on transport, not on mathematics.** `RothLemmaUniform` at `m−1`
   bounds `index (r·d₁) α (mvGenWronskian Dx φ)` given degree and height bounds on that
   Wronskian, and **both exist** (`degreeOf_mvGenWronskian_le`, `abs_coeff_mvGenWronskian_le`).
   The gap is that these theorems are stated for `σ ⊕ Unit` while `RothLemmaUniform` takes an
   `o : σ ≃ Fin m`. Bridging it is `Fin (n+1) ≃ Fin n ⊕ Unit` plus `index_rename_equiv`.
   ⚠ Worth noting against correction 7, which called `Fin m` transport "pure overhead": it is
   not overhead, but it is also not deep — this is the second time the indexing choice has cost
   real work.
2. **The `y` half.** One variable, so `RothBaseCase` applies directly; the work is matching its
   `ℤ`-coefficient, height-and-denominator hypotheses to what the step has.

Then `c_m = 2^m − 3` by iterating with `rothLemmaUniform_one` as the base.

Verification: twenty arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no linter
output. Two declarations `#print axioms`-clean.

---

## 2026-08-23 — the transport, and what it turns out was actually blocking

New module `QOU/Mathlib/RothVariableSplit.lean` (21st in the arc, registered in `QOU.lean`).

```
splitLast n            Fin (n+1) ≃ Fin n ⊕ Unit, sending Fin.last to the Unit component
splitOrder o           the variable equivalence σ ≃ Fin n ⊕ Unit an ordering induces
split_eq               a σ-indexed function becomes a Sum.elim on the split
index_splitOrder       the index, transported
rothGrowth_splitOrder  the growth condition, transported
splitLast_hlast        the split-off variable comes last
degreeOf_splitOrder    degreeOf, transported
index_le_of_rothGrowth_split   §13's conclusion, stated entirely in σ, o and d
```

`index_le_of_rothGrowth_split` is the shape `RothLemmaUniform` uses: the caller states degrees,
growth and the index bound in terms of `σ` alone, and everything about the `Fin n ⊕ Unit`
split is internal.

### ⚠ Against correction 7

Correction 7 called `Fin m` transport "pure overhead", on the strength of `index_rename_equiv`
being three lines. That lemma *is* three lines. What it does not do is produce the split,
transport the growth condition, or line up `degreeOf` — this module is about 150 lines. The
correction was right that transport is not deep and **wrong that it is free**. Second time the
indexing choice has cost real work; recording it so the third time is expected.

### ⚠ What was actually blocking, and it is not indexing

Writing the transport made the real obstacle visible, and it is one I had not named:
**integrality**.

`RothLemmaUniform` is about polynomials with **integer** coefficients — that is not incidental,
it is where the whole Diophantine content lives (`RothBaseCase` bounds an index by comparing a
leading coefficient against a power of a denominator, which needs integrality). But the
Wronskians `hres` speaks of are rational combinations of a minimum representation's factors,
and a minimum representation has no reason to be integral.

§6 of the source does exactly this reconciliation — Gauss's lemma gives rationals `μ, ν` with
`U = μU*` and `V = νV**` integral and `W = UV` — and `RothHeightBound` has the Gauss step. It
is **not wired in**. So `hres` remains a hypothesis and this module does not discharge it.

That is the last piece before the induction can be written, and naming it is the useful output
of this step: I had been treating the remaining gap as indexing, and indexing turned out to be
the cheap half.

Verification: twenty-one arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no
linter output. Seven declarations `#print axioms`-clean. No `sorry`/`admit`/`native_decide`.
Orphan gate re-run: 2038 modules, 1155 reachable (up one), 883 not built — the new module is
registered and the inherited red did not grow.

---

## 2026-08-23 — multivariate content over ℤ, because Mathlib has none

New module `QOU/Mathlib/SeparatedGauss.lean` (22nd in the arc). Mathlib-only imports.

### Why integrality is the blocker, precisely

§7's height step is `max(|U|, |V|) ≤ |W|`, and its argument is: any coefficient of `U` times
any coefficient of `V` **is** a coefficient of `W`, and a non-zero **integer** has absolute
value at least 1. That is `abs_coeff_le_of_mul_separated`, which the arc already has — over
`ℤ`. Over `ℚ` a coefficient of `V` can be arbitrarily small and the step is **false**.

So integrality is not bookkeeping there; it is the whole argument. And the minimum
representation lives over `ℚ` (shortening divides by a coefficient), so the induction
hypothesis — which is about integer polynomials — cannot reach its factors until §6's Gauss
step is done.

### ⚠ A genuine Mathlib gap

Mathlib has `Polynomial.content` and `Polynomial.IsPrimitive` for **one** variable. There is
no `MvPolynomial` counterpart — checked, not assumed. So:

```
exists_int_scaling        a rational polynomial has an integral multiple
intContent                the gcd of the coefficients
intContent_dvd_coeff, intContent_ne_zero
exists_primitive_part     p = content · q with q primitive
exists_primitive_scaling  ∃ l ≠ 0 and primitive integral U' with map U' = C l · U
```

Primitivity is stated as "**every common divisor of the coefficients is a unit**" rather than
by defining `IsPrimitive` for `MvPolynomial`. That is what the Gauss argument consumes, and it
avoids committing to a definition the arc would then have to maintain.

### The disjoint case is much easier than general Gauss

General Gauss needs unique factorisation. In *disjoint* variable groups it needs neither
factorisation nor Bézout: `coeff (i ⊞ j) (U·V) = uᵢ·vⱼ` exactly, so once `U` is primitive and
integral, the denominator of every `vⱼ` divides **every** coefficient of `U`, hence divides
their gcd, hence is `1`. One gcd argument.

⚠ Worth noting how the Bézout step was avoided. The first derivation used "gcd = 1 ⟹ ∃ integer
combination = 1" and then summed. The denominator argument is strictly simpler and needs no
finite-family Bézout — which Mathlib does not have in a convenient form either.

### Open

Part 4, the disjoint Gauss itself, stated in the module's `Next`. Given the above it is short;
it rests on `coeff_sumElim_rename_mul` from `SeparatedHeight`, which is why that part of the
module will not be Mathlib-only.

### Build notes worth keeping

- `IsLocalization (nonZeroDivisors ℤ) ℚ` needs `Mathlib.RingTheory.Localization.FractionRing`;
  `NormalizedGCDMonoid ℤ` needs `Mathlib.RingTheory.Int.Basic`. Neither comes with
  `MvPolynomial.Basic`, and `MvPolynomial.map` itself lives in `MvPolynomial.Eval`.
- `rw [← hq]` where `hq : C (intContent A) * q = A` rewrote `A` inside `intContent A` as well.
  `conv_rhs => rw [← hq]` is the fix — the same shape of mistake as the `rw [hP]` one two
  entries ago, so it is worth naming: **an equation whose right side is a bare variable will
  rewrite that variable everywhere, including inside the other side's own subterms.**

Verification: `lake build` with `.olean` deleted — exit 0, no errors, no linter output. Five
declarations `#print axioms`-clean. No `sorry`/`admit`/`native_decide`. Registered in `QOU.lean`.

---

## 2026-08-23 — §6's Gauss step, done

Part 4 from the previous entry. `exists_integral_separated_factors`: if `W` has integer
coefficients and factors over `ℚ` as a polynomial in the `x`-variables times one in the
`y`-variables, a single rational `l` rescales both factors to be integral.

The proof is six lines of substance, and needs **neither unique factorisation nor Bézout** —
both of which general Gauss needs. That is entirely a consequence of the groups being
disjoint: `coeff (i ⊞ j) (U·V) = uᵢ·vⱼ` exactly, so once `U` is scaled to be primitive and
integral, the denominator of each `vⱼ` divides *every* coefficient of `U'`, hence their gcd,
hence is `1`. In shared variables the coefficients mix and none of this is available.

Supporting: `den_dvd_of_mul_int` — if an integer multiple of a rational is an integer, the
rational's denominator divides the multiplier. Via `Rat.den_dvd`, with the `n = 0` case
handled separately since it makes the division meaningless and the conclusion trivial.

### ⚠ Where integrality is and is not needed — worth stating plainly

`index_C_mul` says rescaling does **not** move the index. So on the **index** side the `l` is
invisible and integrality was never needed. The *only* reason §6 does Gauss at all is the
**height** side: §7's `max(|U|, |V|) ≤ |W|` argument turns on "a non-zero integer has absolute
value at least 1", which is false over `ℚ`.

That is a sharper statement of the same shape as correction 3, which found that height and
index behave differently across the separated split. Three times now the useful move has been
to ask which of the two chains a step belongs to.

### Open — one commutation, not a new idea

1. **`map` commutes with the determinant of derivatives.** The arc's `sepW` is built over `ℚ`;
   the `W` this theorem wants is the *same* determinant built over `ℤ` from the integral
   auxiliary polynomial. Relating them is `map_det` plus
   `map (pderivList l P) = pderivList l (map P)`.
2. Then the induction hypothesis reaches the factors: `index_C_mul` for the index side,
   `abs_coeff_le_of_mul_separated` (= §7's height step) for the height side.

Verification: twenty-two arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no
linter output. Two declarations `#print axioms`-clean.

---

## 2026-08-23 — §6 and §7's height step, assembled

The commutation was the whole of it, and Mathlib had both halves.

```
map_pderivList        iterated differentiation commutes with a change of coefficient ring
map_det_pderivList    so does the determinant of derivatives          (MvGenWronskian)
exists_integral_separated_factorization   the factorisation is exact over ℤ: U'·V' = W
exists_integral_wronskian_factors         §6, assembled                (SeparatedGauss)
abs_coeff_integral_wronskian_factor_le    §7's height step: H(U') ≤ H(W)
```

`map_det_pderivList` is the identification that was missing: the arc's separated Wronskian is
built over `ℚ` (the representation lives there), while the `W` Gauss needs is the **same**
determinant formed over `ℤ` from the integer auxiliary polynomial. `pderiv_map` and
`RingHom.map_det` are both in Mathlib; only the iteration and the assembly were needed.

### The exactness is worth having separately

`exists_integral_separated_factors` gives integral factors up to a rational; the new
`exists_integral_separated_factorization` gives `U'·V' = W` **on the nose**. That is Mahler's
`W = UV`, and it is what `abs_coeff_le_of_mul_separated` consumes — the height step needs the
product to *be* `W`, not to agree with it up to a scalar. Proved by injectivity of
`map (Int.castRingHom ℚ)`, which is where the two rational scalings `l` and `l⁻¹` cancel.

### Open — bookkeeping across three modules, no new ideas

Assembling `hres` from the induction hypothesis. Every ingredient now exists:

1. **The index side is free.** `index_C_mul` says `index (C l * Wx) = index Wx`, so bounding
   the index of the *integral* factor `U'` — which is what `RothLemmaUniform` does — bounds
   the index of `Wx` itself. ⚠ The scaling is invisible here. It only ever mattered for
   heights, and saying so three times has been the useful thing about this stretch.
2. **The height side** is `abs_coeff_integral_wronskian_factor_le`, with
   `abs_coeff_mvGenWronskian_le` bounding the determinant's own height.
3. **The degree side** is `degreeOf_mvGenWronskian_le`, transported through `map` and the
   scaling.

It needs a home importing both `SeparatedGauss` and `RothLemmaStatement`.

Verification: twenty-two arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no
linter output. Five declarations `#print axioms`-clean.

---

## 2026-08-23 — ⚠ correction 5's pattern again, on the other chain

Assembling `hres` turned up a gap of exactly the shape the arc has been bitten by before, and
this time on the **height** side.

`WronskianHeight.abs_coeff_mvGenWronskian_le` is for `D : Fin m → List σ` — one operator list
per **row**, applied to a different function per column. Mahler §13's determinant is a
different shape: `D : Fin r → Fin r → List σ`, a different operator per **entry**, all applied
to the same `P`. The *index* side has that composite (`sum_max_le_index_det`); the height side
did **not**.

That is correction 5 with the chains exchanged — there the index side had no counterpart to a
height composite. It went unnoticed for the same reason both times: each side looks complete
from its own end, and nothing forces the comparison until something needs both.

`abs_coeff_det_pderivList_le` closes it, and is short — `abs_coeff_det_le` for the
determinant, `card_support_pderivList_le` and `abs_coeff_pderivList_le` for the entries. The
gap was in noticing, not in proving.

### Also landed — the transports the assembly needs

```
degreeOf_map_of_injective      a change of coefficient ring does not move degrees
degreeOf_integral_factor_le    degrees transport to the integral factor  (SeparatedGauss)
integral_factor_ne_zero        so does non-vanishing
rothGrowth_scale               rescaling the degree vector preserves the growth condition
```

⚠ `degreeOf_integral_factor_le` only needs `≤`, so `degreeOf_C_mul_le` suffices and the
scaling costs nothing — a third instance of the same theme: **the scaling `l` is free
everywhere except the height bound.** Index (`index_C_mul`), degree (`degreeOf_C_mul_le`),
non-vanishing — all indifferent to it. Only §7's "a non-zero integer has absolute value at
least 1" cares, and that is the one place §6 does work.

`rothGrowth_scale` is the source's `p_h = n·r_h` on the growth condition: the induction step
measures its sub-problems against `r·d`, and the condition survives because the factor `r`
appears on both sides.

### Open

The `hres` assembly itself. Every ingredient now exists and none of it is new:
`index_C_mul` (index side), `abs_coeff_integral_wronskian_factor_le` +
`abs_coeff_det_pderivList_le` (height side), `degreeOf_integral_factor_le` +
`degreeOf_mvGenWronskian_le` (degree side), `rothGrowth_scale` and `integral_factor_ne_zero`
for the remaining hypotheses of `RothLemmaUniform`. It needs a module importing
`SeparatedGauss`, `RothLemmaStatement` and `RothOperatorFamily`.

Verification: twenty-two arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no
linter output. Five declarations `#print axioms`-clean.

---

## 2026-08-23 — `hres`'s `x` half, discharged from the induction hypothesis

New module `QOU/Mathlib/RothInductionHypothesis.lean` (23rd in the arc).
`index_rescaled_wronskian_le` builds the `x` conjunct of `hres` out of `RothLemmaUniform` at
`m − 1`. It built first try, which — after the last three "purely bookkeeping" predictions
each turned something up — is worth recording as the one that actually was.

The chain:

* §6's Gauss (`exists_integral_wronskian_factors`) replaces the rational Wronskian
  `Wx = mvGenWronskian Dx φ` by an **integral** `U'` with `map U' = C l · Wx`;
* `RothLemmaUniform` applies to `U'`, because `U'` is an integer polynomial — its degree,
  non-vanishing and height hypotheses come from `degreeOf_integral_factor_le`,
  `integral_factor_ne_zero` and `abs_coeff_integral_wronskian_factor_le`, and its growth
  hypothesis from `rothGrowth_scale`;
* `index_C_mul` carries the bound back to `Wx` **unchanged**.

### ⚠ The theme, in its final form

The Gauss scaling `l` is free on the index side (`index_C_mul`), free on the degree side
(`degreeOf_C_mul_le`), free for non-vanishing — and costs something on exactly one side, the
**height**. That is why §6 does Gauss at all, and why §7's "a non-zero integer has absolute
value at least 1" is where integrality is load-bearing.

Stated four times now across this stretch, each time from a different direction. It is the
same instinct correction 3 came from: **ask which of the two chains a step belongs to.**

`hWy` deserves a note for the same reason. The `y`-Wronskian's non-vanishing appears in this
theorem, and it is needed for the **height** step and nothing else —
`abs_coeff_le_of_mul_separated` picks a non-zero coefficient of the other factor. It is
exactly what `BoundedOrderWronskian` supplies.

### Open

1. **The `y` half of `hres`**: one variable, so `RothBaseCase` applies to `mvGenWronskian Dy ψ`
   directly — through the same Gauss step, since that Wronskian is rational too and
   `RothBaseCase` is about integer polynomials.
2. Then `index_le_of_rothGrowth_of_rescaled_bounds` gives §13's conclusion outright and the
   induction can be written: `rothLemmaUniform_one` is the base, this is the step.
3. `c_m = 2^m − 3` from iterating. ⚠ §14 has **not** been read; it stays unasserted.

⚠ **Not yet guarded.** This is the largest hypothesis stack in the arc and it has **no
non-vacuity witness**. The hypotheses are satisfiable on paper — `σ = Unit`, `n = r = 1`,
`E = 0`, `B = 1`, `P = 1`, everything constant — but on paper is what correction 8 was, and
that was found *by writing the witness*. Writing it is the immediate next thing.

Verification: twenty-three arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no
linter output. `#print axioms`-clean. Orphan gate: 2040 modules, 1157 reachable (up two for
the two new modules), 883 not built — registered, and the inherited red did not grow.

---

## 2026-08-23 — the guard, written

`index_rescaled_wronskian_le_witness`. The previous entry flagged that the arc's largest
hypothesis stack had none, and that "satisfiable on paper" was exactly the state correction 8
was in when it was wrong.

Instance: one variable on each side, everything constant — `n = r = 1`, `d₁ ≡ 1`, `P = 1`,
`φ = ψ ≡ 1`, `p/q = 1/2`, `B = 1`, `E = 0`. The determinant is `1`, whose coefficients are `0`
and `1`, so `B = 1` works; `E = 0` makes `B ≤ q^E` read `1 ≤ 1`; and the induction hypothesis
is `rothLemmaUniform_one`, which is **proved** rather than assumed — so the witness does not
smuggle in an unproved `RothLemmaUniform` to make itself work.

**Result: the stack is jointly satisfiable.** No two side conditions quietly contradict.

⚠ And what it does *not* show, in its own docstring: finite witnesses test **vacuity, not
usefulness** — correction 9's lesson, where a hypothesis satisfiable at every small `r` failed
only asymptotically. This rules out one failure mode, the one a stack of eleven hypotheses
invites, and not the other.

⚠ The `hIH` choice is the part worth having been careful about. Instantiating with an
*assumed* `RothLemmaUniform` would have made the witness vacuous in precisely the way it
exists to detect — the theorem would have been shown satisfiable only relative to an
unproved hypothesis. `rothLemmaUniform_one` is the `m = 1` case and is proved outright.

Verification: twenty-three arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no
linter output. `#print axioms`-clean. No `sorry`/`admit`/`native_decide`.

---

## 2026-08-23 — ⚠ TENTH CORRECTION: "for every bounded-order family" is unsatisfiable

Supplying both halves of `hres` is what exposed it. The two halves each need the Wronskian
they bound to be **non-zero** — and `hres` gave them nowhere to get that from, because it
quantified over *every* bounded-order family realising a separated representation of `P`.

**That hypothesis is false for every `P`.** Take `Dx i = []` for all `i`. The order condition
`|Dx i| ≤ i` holds (`0 ≤ i`); the family realises the same representation, since it does not
touch `φ` or `ψ`; and for `r ≥ 2` the Wronskian matrix has all rows equal, so the determinant
is `0` and the index is `⊤`, below no finite bound. And every `P` admits a length-`2`
representation — pad a shorter one with zeros — so this is not an edge case.

`mvGenWronskian_nil_eq_zero` is that computation, landed as the record.

### The repair costs nothing

Carry `mvGenWronskian Dx φ ≠ 0` and `mvGenWronskian Dy ψ ≠ 0` into `hfac` and `hres`. The proof
only ever applies them to the family `exists_sepW_ne_zero_le_degreeOf` produces, **whose
Wronskians are non-zero by construction** — the `sepW ≠ 0` it returns had been discarded with
a `-`. The hypothesis had simply been stated more strongly than the argument used.

The type system then forced the same repair on `index_le_of_rothGrowth_split`, which is the
one piece of good news here: once the head was fixed, nothing downstream could silently keep
the broken form.

### ⚠ How it was found, and what could not have found it

It surfaced only when the halves were **supplied**. Not `lake build`, not `#print axioms`, and
— importantly — **not a witness at small `r`**: at `r = 1` a one-column determinant is `φ 0`,
which need not vanish, so the hypothesis is perfectly satisfiable there. The same asymptotic
blind spot as correction 9's `S·rr ≤ r`.

So the pattern, now twice: **a hypothesis nobody has had to discharge is indistinguishable
from a false one.** Correction 9 was found by testing a side condition; this one by supplying
one. Both times the theorem was sound and the hypothesis was the defect, and both times every
finite example agreed with it.

⚠ Worth noting against my own previous entry: I wrote that the `hres` assembly was "purely
bookkeeping" and that saying so was risky given the last three such predictions. It was risky.

### Where this leaves the arc

Both halves of `hres` are now supplied and the hypothesis they feed is satisfiable:

* `index_rescaled_wronskian_le` — the `x` half, from `RothLemmaUniform` at `m − 1`;
* `index_rescaled_wronskian_le_right` — the `y` half, from `rothLemmaUniform_one`, **proved**.

Open: quantify the two halves' auxiliary data (`B`, `E`, denominators) uniformly in the family
— `abs_coeff_det_pderivList_le` is what makes a uniform `B` available — assemble `hres`, and
iterate. Then `c_m = 2^m − 3`, still unasserted since §14 is unread.

Verification: twenty-three arc modules rebuilt with `.olean`s deleted — exit 0, no errors, no
linter output. Four declarations `#print axioms`-clean.

---

## 2026-08-24 — #5316 merged; follow-up restarted from main

PR #5316 merged as `dd6565ba51`. Verified on the remote, not from the merge response: our
commit is an ancestor of `origin/main` and all 23 arc modules are present there. Branch
restarted from the merged main per the merged-PR rule — a merged PR cannot track new work.

**The gate that had been withheld all along now passes.** Whole-library `lake build QOU`:
exit 0, 5769 jobs, no errors, against the merged tree — with all 23 arc modules rebuilt **from
source** (`.olean` deleted) inside that build and **zero linter output in any of them** (the
733 corpus warnings are all pre-existing elsewhere). Main had moved 1256 commits; the only
both-modified file was `QOU.lean`, which git auto-resolved, and the branch's delta on top of
main was exactly 26 files with no `computations/`, witness, or `.py` among them — so the
witness-drift refresh did not apply.

### Follow-up: the height bound, made uniform in the family

`abs_coeff_det_sepFamily_le`. `abs_coeff_det_pderivList_le` needs a bound `L` on the operator
lists' lengths; for the family the induction step forms — `D i j = (Dx i)⊞(Dy j)` with `Dx`,
`Dy` of bounded order — that bound comes from `r` alone, since `|Dx i| ≤ i < r` and
`|Dy j| ≤ j < r` give every entry length at most `2r`.

⚠ **This is what makes `hres` assemblable.** `hres` quantifies over the families realising a
separated representation, so its auxiliary data — the height bound `B` above all — must be
chosen *before* the family is known. A bound depending on the individual `D i j` is useless
there; one depending only on `r` and `P` is not. That is the same shape as correction 10: a
hypothesis about all families can only carry data that does not vary across them.

Verification: `lake build` with `.olean` deleted — exit 0, no errors, no linter output;
`#print axioms`-clean; downstream `RothInductionHypothesis` still builds.

---

## 2026-08-24 — the degree half of `hres` becomes family-uniform; and where the assembly bottoms out

Two theorems, and one finding about what "assemble `hres`" actually means.

```
linearIndependent_of_mvGenWronskian_ne_zero   Wronskian ≠ 0 ⟹ the family is independent
degreeOf_factor_le_of_indep                   factors' degrees ≤ P's, given the OTHER family
                                              is independent
```

### ⚠ Correction 10's repair handed over exactly what was missing

`hres` quantifies over families, so every hypothesis it carries must be statable *before* the
family is known. The `x` and `y` halves need `degreeOf j (φ k) ≤ d₁ j` — which looks
family-dependent, and **is false in general**: for `P = x₀y₀` the length-`2` representation
`φ = ![x₀ + x₀⁵, −x₀⁵]`, `ψ = ![y₀, y₀]` telescopes back to `P` while `φ 0` has degree `5`.

What rules that out is `ψ` being **dependent** — and after correction 10, `hres` already
carries `mvGenWronskian Dy ψ ≠ 0`, which forces independence. So the repair for correction 10
supplied precisely the hypothesis the next step needed. Recording that because the reverse is
the usual experience: a repair narrowing a statement usually costs something downstream.

The degree bound is then family-uniform — `degreeOf (Sum.inl j) P`, which does not vary.

### ⚠ Where the assembly bottoms out: §14, which is unread

Working out the rest of `hres`'s auxiliary data gives a definite answer to what remains, and it
is not more Lean.

`abs_coeff_det_sepFamily_le` makes the height bound uniform in `P`, but its value depends on
`r`: `B_r = r!·(S·(d^{2r}·B_P))^r`. The halves also need `B_r ≤ qd_j^{E_r}` and
`(E_r : ℚ) ≤ ε·(r·d_j)`. Taking logs and dividing by `r`, those two force

    [log r!/r + log S + 2r·log d + log B_P] / log qd  ≤  ε·d_j,

whose dominant term is `2r·log d / log qd`. Whether that holds is exactly the parameter
bookkeeping of §11 (property `Γ_m`) and §14 — **both unread**, and both in the illegible
region of the scan.

So "assemble `hres`" is not a bookkeeping step after all: it terminates in a numeric condition
the arc has consistently refused to assert. The honest shape for the assembly is to take that
condition as one named hypothesis — isolating §14 to a single place rather than diffusing it —
and that is what to write next.

⚠ Stated so the arc does not repeat correction 6's mistake in reverse: the condition above is
*derived from the arc's own theorems*, not read from the source. If §14's conditions differ, a
theorem proved against this one is about `RothLemmaUniform`, not about Roth's lemma.

Verification: twenty-three arc modules rebuilt with `.olean`s deleted — exit 0, 2819 jobs, no
errors, no linter output. Both declarations `#print axioms`-clean.

---

## 2026-08-24 — §11 and §14 read from the page scans; the eleventh correction

The two sections this arc had been reconstructing around are no longer unread. The PDF's OCR
text layer garbles exactly §11 and §14; extracting the **scanned page images** and reading
them visually worked where every text extraction had failed. (Doc page = PDF page + 76;
`pypdf` for the images, `pillow` to crop.) Recording the method because the arc lost several
turns to "this section is illegible" when what was illegible was one representation of it.

Three findings, two of them corrections.

### 1. `RothGrowth` **is** the source's condition — caveat withdrawn

Property `Γ_M`'s first clause is `max(s₂/s₁, …, s_M/s_{M−1}) ≤ t`, i.e. `s_h ≥ s_{h+1}/t` —
which is `RothGrowth o ω d` with **`ω = 1/t`**. The arc reconstructed that condition from what
the row-cost bound needed, and the reconstruction was right.

Every "this is a fact about `RothGrowth` as this arc defines it, not established as the
source's" caveat is now withdrawn — five of them, in `RothLemmaStatement`,
`RothOperatorFamily` (two) and `RothInductionStep` (two). What replaces them is narrower and
true: `Γ_M`'s **other two clauses** (`s_h log K_h ≥ s₁ log K₁` and
`K₁ ≥ 2^{(1/t)(M−1)M(2M+1)}`) are still carried nowhere, which makes this arc's statements
**stronger** than the source's, not weaker.

⚠ It also caught a conflation the arc had been making. `ω ≥ 2/ε` reads `ε ≥ 2t` under
`ω = 1/t`, and §14's `ε = t/m` does **not** satisfy it. The row cost and the height parameter
are separate quantities; `rothGrowth_row_cost_le`'s `t` is the former, §11's the latter. The
docstring saying `ω ≥ 2/ε` "is what `ω(m, ε)` has to be" was treating them as one.

### 2. ⚠ `c_m = 2^{m+1} − 3`, not `2^m − 3`

§14 gives `c₁ = 1` and `c_m = 2c_{m−1} + 3`, which closes to `2^{m+1} − 3`. Landed as
`rothConstant` with `rothConstant_one` and `rothConstant_rec` checked against each other.

⚠ **It is the base case, not the recurrence, that pins the constant** — and getting that
backwards is how the wrong value survived unchallenged. The recurrence's general solution is
`A·2^m − 3`, so the discarded value satisfies it too; `two_pow_sub_three_rec` checks that it
does, and `two_pow_sub_three_ne_one` shows where it actually fails. A check against the
recurrence alone would have passed the wrong constant.

That is worth generalising: this arc's habit is to check a claimed closed form against its
recurrence. On a linear recurrence that check is **necessary and not sufficient**, and the
homogeneous solution is exactly the error it cannot see.

### 3. ⚠ The conclusion is `Θ_m ≤ c_m·t^{2^{−(m−1)}}` — an exponent, not a linear factor

Iterating §13's *square-root* branch halves the exponent once per step. `RothLemmaUniform`'s
conclusion was `index ≤ m·ε`, **linear** in the small parameter, and no linear-in-`ε`
invariant can absorb a square root taken once per step — so the recursion could never have
closed on that statement's shape. This was not a slack constant; it was the wrong shape.

`rothBound_two_half` and `two_mul_lt_rothBound_two_witness` exhibit the gap at `m = 2`,
`t = 1/100`: §14 admits `θ = 1/2` where the linear form demanded `1/50`.

### The restatement

Three pieces rather than one, so that "what the statement says" and "what bound the source
achieves" stop being the same object:

```
RothBound m t θ            §14's bound, root-free: θ^{2^{m−1}} ≤ c_m^{2^{m−1}}·t
RothLemmaUniform … θ       the schema — θ is a parameter, so this is not a claim
RothLemmaMahler σ m t      the instance that IS Roth's lemma: ω = 1/t, ε = t/m, RothBound m t θ
```

`RothBound` is root-free because the index is `ℚ`-valued and `c_m·t^{2^{−(m−1)}}` is
irrational in general; raising both non-negative sides to `2^{m−1}` is equivalent by density.
It is also the shape the recursion is already in — §13's branch is a square root, so this
arc's arithmetic for it (`sq_index_le_of_det_bound`, `sq_mul_le_two_mul_of_sum_le`) is stated
squared. `rothBound_one` recovers §14's base case `Θ₁ ≤ t`, and `rothLemmaMahler_one`
discharges it.

Making `θ` a parameter is what forced the honest label: `RothLemmaUniform` is a **schema**,
trivially true for large `θ`, and quoting it alone overstates what it says.

### What this changes about "what remains"

The previous entry ended by saying the assembly bottoms out in a numeric condition §14 would
have to settle. §14 has now been read, so that condition is no longer a placeholder — and the
open parameter question has moved: it is `Γ_m`'s two omitted clauses, which an `m ≥ 2` proof
will have to reinstate rather than discover it can do without.

The recursion's obligation, in the new shape: from `RothBound (m−1) t θ'` for the two
sub-problems, derive `RothBound m t θ` for the assembled bound. `rothConstant_rec` is the
arithmetic half of exactly that step.

Verification: `RothLemmaStatement`, `RothInductionHypothesis`, `RothInductionStep` and
`RothOperatorFamily` each rebuilt with its `.olean` deleted — exit 0, no errors, no linter
output. All fourteen new and re-signed declarations `#print axioms`-clean.

### The §13 → §14 junction, and the numeric condition isolated

`rothBound_of_max_form` bridges the arc's §13 output — `index_le_two_mul_max_of_det_bound`,
which ends at `θ ≤ t + 2·max(S/r, q)` — to `rothBound_step`. Every linking hypothesis is now
named: `t ≤ Ψ` (from `Ψ = Θ_{m−1} + t` and `Θ_{m−1} ≥ 0`), and `A² ≤ Ψ`, `q² ≤ Ψ` for the two
branches of the max, stated squared so no root appears.

⚠ **The junction squeezes `q` from both sides, and that is the whole numeric content.** §13
needs `S ≤ q²·rr` — a **lower** bound, since `q` is its rational stand-in for `√(S/rr)`. The
step needs `q² ≤ Ψ` — an **upper** bound. Together (`le_mul_of_max_form_squeeze`) they force

    S ≤ Ψ·rr

and that single inequality is what the whole junction reduces to. The previous entry said the
assembly "terminates in a numeric condition the arc has consistently refused to assert"; this
is that condition, isolated to one named place rather than diffused through the recursion, and
now it can be asserted because §14 has been read.

⚠ Necessary, not sufficient. A rational `q` with `S/rr ≤ q² ≤ Ψ` exists whenever
`S/rr < Ψ` — rational squares are dense — but at equality only if `Ψ` is a rational square. The
strict form is what a caller should establish; that density argument is **not** proved.

### `Γ_m`'s missing clauses reinstated — and the numeric condition, fully explicit

`RothGamma` now bundles all three of §11's clauses, and `RothLemmaUniform` carries it in place
of `RothGrowth`. The arc had carried only clause 1 for its whole life, which made every
statement here **stronger** than the source's — and a theorem stronger than the one the source
proves is one nothing in the source will discharge.

Clause 2, `s_h·log K_h ≥ s₁·log K₁`, clears its logarithms to `K₁^{s₁} ≤ K_h^{s_h}` — which is
**exactly** Bombieri–Gubler 6.3.4's `qⱼ^{dⱼ} ≥ q₁^{d₁}`. The module header had been listing
that as a textbook condition this variant does *not* carry. Two independent sources agreeing on
a clause is better evidence than either reading alone.

Clause 3's exponent `ω(m−1)m(2m+1)` is rational, so `rothDenomFloor` rounds it **up**. That
makes the clause stronger than the source's and every statement carrying it weaker — the safe
direction for a hypothesis being reinstated, since it cannot let a claim here outrun §14's.

At `m = 1` the growth clause is vacuous and the other two follow from the standing `2 ≤ qⱼ`
(`rothDenomFloor_one` gives floor = 1), so `rothLemmaUniform_one` still holds for every `ω` and
both witnesses discharge `Γ_m` outright. `rothGamma_scale` is the companion to
`rothGrowth_scale`; clause 2 survives rescaling because raising `K₁^{s₁} ≤ K_h^{s_h}` to the
`r`-th power is monotone, clause 3 because it does not mention `d`.

### ⚠ Where `Γ_m` is finally *needed*

Chaining `index_le_of_rothGrowth_of_factor_bound`'s `(d₂+1)·Φ ≤ q²·D₂` with the junction's
`q² ≤ Ψ`, and substituting §14's `Ψ = Θ_{m−1} + t = Φ + t`, the whole condition rearranges to

    (d₂ + 1 − D₂)·Φ ≤ t·D₂,     which at D₂ = d₂ reads    Φ ≤ t·d₂

(`factor_bound_le_of_split_degree`, `factor_bound_le_of_split_degree_eq`). That is a
**largeness requirement on the split-off degree**, not a bookkeeping identity: `Φ ≈ Θ_{m−1} ≤
c_{m−1}·t^{2^{−(m−2)}}`, which for small `t` is much bigger than `t`, so `d₂` must be at least
`Φ/t`.

⚠ This is the first place in the arc where clauses 2 and 3 have to be used — which is exactly
why they went missing for so long. Nothing earlier needed them, so nothing earlier noticed.
That is the same failure mode as corrections 9 and 10 seen from the other side: there, a
hypothesis nobody had to discharge turned out to be false; here, a hypothesis nobody had to
*use* turned out to be absent.

Verification: whole-library `lake build QOU` — exit 0, 5770 jobs, no errors, zero warnings in
any Roth-arc module (722 corpus warnings, all pre-existing elsewhere). `RothLemmaStatement` and
`RothInductionHypothesis` each rebuilt with `.olean` deleted. All twelve new and re-signed
declarations `#print axioms`-clean.

### ⚠ Corrections twelve and thirteen — both from reading Lemma 4 and §14 in full

Two claims made in this arc's own source files in the last two entries were wrong. Both are
withdrawn, and both were caught by going back to the page scans rather than by more reasoning.

**Twelve.** `rothConstant_step`'s docstring said §14's constant `2c+3` *identifies* which
quantity `Ψ_m = Θ_{m−1} + t` refers to, because the row-cost reading would give a different
constant. False. §14's own split leads with the row cost (weakened `t → s`) and bounds the
square-root branch by the crude `2c+2`, where this arc's proof leads with `Ψ` and uses the
sharper `c+2`:

    §14:        1     + (2c+2)  =  2c+3
    this arc:   (c+1) + (c+2)   =  2c+3

`rothConstant_step_source` proves the second route, so the agreement is a **checked fact**.
Two splits reaching the same constant means reproducing it discriminates nothing.

⚠ Landing the second route also exposed a real difference: §14's needs no `s ≤ 1`, this arc's
does (for `s² ≤ s`). They are not notational variants of one argument.

**Thirteen.** `factor_bound_le_of_split_degree` presented `(d₂ + 1 − D₂)·Φ ≤ t·D₂` as the
arc's open parameter question. It is a cost of the arc's own §13 formulation, not a hypothesis
of Roth's lemma. **Lemma 4**, read verbatim:

> Let `m ≥ 2` and let `a; r₁,…,r_m; H₁,…,H_m` have property `Γ_m`. Then there exists an
> ordered system `b; ρ₁,…,ρ_{m−1}; H₁,…,H_{m−1}` with property `Γ_{m−1}` such that
> `Θ_m ≤ t + 2 max(Ψ_m, √Ψ_m)` where `Ψ_m = Θ_{m−1}(b; ρ; H) + t`.

The max is over **one** quantity and its square root — no `/n`, no `/r_m`, **no side
condition** — and the sub-system's `Γ_{m−1}` is *produced*, not assumed. The arc's
`index_le_two_mul_max_of_det_bound` has `max(S/r, q)` with `S ≤ q²·rr` instead, and that is
where the requirement comes from. Whatever it costs is discharged from `Γ_m` inside §13's
proof body, which has not been read.

### What reading Lemma 4 and §14 in full settled

- **`c_m = 2^{m+1} − 3` is printed explicitly** in the statement of Roth's Lemma. Correction 11
  is now read, not inferred.
- **§14's computation, verbatim**: both branches of the max come out to exactly `(c+1)s` —
  `Ψ ≤ cs² + t ≤ cs + s` and `√Ψ ≤ (c+1)s` via `c+1 ≤ (c+1)²` — which is why the `max`
  disappears. Landed as `rothConstant_step_lemma4`, the faithful step.
- **`c_{m−1} ≥ 1`** is Mahler's standing hypothesis in that computation (`rothConstant_one_le`).
- ⚠ **`0 < t ≤ 1` is Theorem 1's opening hypothesis and this arc had not carried it.**
  `RothLemmaMahler` now does. §14 uses it twice, for `s² ≤ s` and `t ≤ s`.
- **Theorem 1's four clauses match `RothGamma` exactly**, including that clause 2 runs over
  `h = 2,…,m` — which is the `∀ j k, (j : ℕ) = 0 → …` encoding, confirmed rather than guessed.

⚠ `0 ≤ w` came off `rothConstant_step_lemma4` for the third time in this pattern: the linter
flagged it unused, and it is genuinely not needed — a negative `w` only makes `s + 2w` smaller.
Three times now the linter has been the cheap version of the signal corrections 9 and 10 cost
real work to get.

### ⚠⚠ Correction fourteen — one wrong subscript, and the whole side condition evaporates

§13's body read. The display is

    J(A) ≤ t + 2·max( (1/n)·J(W) , √( (1/n)·J(W) ) )

— **both** branches over the *same* quantity. Correction 9 transcribed the second as
`√(J(W)/r_m)`, and that single wrong subscript is the entire origin of this arc's side
condition. `index_le_two_mul_max_of_det_bound` carries `q` as a stand-in for `√(S/rr)` with
`rr = D₂ ≈ r_m`, and needs `S ≤ q²·rr` to justify it. At the source's `rr = n = r` the
condition is **automatic** — take `q² = S/r`.

So the junction condition `S ≤ Ψ·rr`, at `rr = r` and `S = r·Φ`, is just `Φ ≤ Ψ`
(`le_mul_of_factor_le`). And §13's body gives

    Φ_m = Θ_{m−1}(b; ρ; H) + Θ₁(b; ρ_m; H_m),    Ψ_m = Θ_{m−1}(b; ρ; H) + t,

so `Φ ≤ Ψ` is exactly `Θ₁ ≤ t` (`factor_le_of_theta_one_le`) — which §13 proves from `Γ_m`:
§10 gives `Θ₁ ≤ log b/(ρ_m log H_m)`, clause 2 replaces the denominator (`ρ_h = n·r_h`, so
`r_m log H_m ≥ r₁ log H₁` lifts to `ρ_m log H_m ≥ ρ₁ log H₁`), and §11's
`b ≤ H₁^{(1/(m−1))ρ₁t}` bounds the numerator, giving `t/(m−1) ≤ t` for `m ≥ 2`. Landed as
`theta_one_le_of_gamma`.

**The "largeness requirement on the split-off degree" was an artifact.** Two turns were spent
isolating, naming and then explaining a condition that does not exist in the source. What
produced it was not faulty reasoning downstream — the arithmetic was right each time — but a
transcription error upstream that nothing downstream could see.

### What §13's body confirms

Two things exactly as this arc had them, which is worth recording because the same reading
overturned a third:

- `Φ_m = Θ_{m−1} + Θ₁` — the **sum of the two halves**, i.e. the arc's `Φ = εU + εV`;
- `J(W) ≤ n·Φ_m` — which is `factor_bound_of_rescaled` verbatim, `n` being the arc's `r`.

### ⚠ A pattern in the unused hypotheses

Four hypotheses now written down and found unused: `0 ≤ u`, `0 ≤ Φ`/`0 ≤ D₂`, `0 ≤ w`, and
`0 ≤ log b`. All four came from transcribing the **paper's proof route** rather than the route
Lean actually takes. `theta_one_le_of_gamma` is the clearest case: the source replaces the
denominator first, which needs `log b ≥ 0`; bounding the numerator and multiplying through
never forms that quotient. The linter is catching a specific habit, not random slack.

### `Γ_m` descends to `Γ_{m−1}` — the piece Lemma 4 asserts and the arc had nothing for

Lemma 4 does not merely conclude an inequality: it **produces** an ordered system
`b; ρ₁,…,ρ_{m−1}; H₁,…,H_{m−1}` *with property `Γ_{m−1}`*, and that is what lets the induction
apply its hypothesis at all. Nothing here supplied it. The gap went unnoticed because every
earlier step **consumed** a `Γ` and none had to produce one — the same blind spot as clauses 2
and 3 going missing, one level up.

`rothGamma_descend` (in `RothVariableSplit`, where the split machinery lives) takes §13's
sub-system — first `m−1` variables, degrees rescaled by `n` (`ρ_h = n·r_h`), denominators
unchanged — and carries all three clauses across:

- **growth**: restricting the consecutive-pair condition to a prefix loses nothing; the
  rescaling is `rothGrowth_scale`'s;
- **height**: clause 2 compares every `h` against `h = 1`, so a prefix keeps its own first
  element; raising to the `r`-th power is monotone given `2 ≤ qⱼ`;
- **floor**: `rothDenomFloor_mono` — the floor grows with the arity, so the *larger* floor
  `Γ_m` supplies implies the smaller one `Γ_{m−1}` asks for.

Only the arity moves; `ω = 1/t` is the same throughout, which is what makes this a
single-parameter induction.

### ⚠ Clause 3 bites, and no previous witness in this arc tested it

`rothDenomFloor_two : rothDenomFloor 2 1 = 1024`. So `Γ_2` demands `H₁ ≥ 1024` — a denominator
of `2` is **not** admissible at arity 2. `rothGamma_descend_witness` is built at `q = 1024` for
that reason.

Every other witness in this arc uses `q = 2`, and every one of them is at **arity 1**, where
`rothDenomFloor 1 ω = 1` and the clause is vacuous. So none of them tested clause 3, and none
of them was wrong to — but it means the arc's non-vacuity evidence for `Γ` is thinner than the
count of witnesses suggests. Worth knowing before the next one is quoted.

### ⚠⚠ Correction fifteen — correction fourteen was wrong, and how it went wrong is the point

**Correction fourteen said correction 9 mis-transcribed `√(J(W)/r_m)` for `√(J(W)/n)`. It did
not.** Display (2) on p. 95 reads

    J(A) ≤ t + √( (2/r_m)·J(W) ) ≤ t + 2·√( (1/n)·J(W) )    if n > N,
    because  n ≤ r_m + 1,  r_m/2 ≥ (r_m/(r_m+1))·(n/2) ≥ (1/2)·(n/2) = n/4.

**Both** forms are the source's. `r_m` is the sharp intermediate — and it is what this arc's
own `le_two_mul_max_of_sum_le` derives, independently. `n` is the packaged weakening, reached
by a *proved step*. Correction 9 transcribed the sharp form; correction fourteen read the
packaged one and called the other an error.

**What survives.** Fourteen's operative conclusion — the side condition moves to the `n`
normalisation and collapses there — is right, for a better reason than it gave. Not that `r_m`
was wrong, but that the source supplies the conversion and **this arc already has its
hypothesis**: `RothOperatorFamily`'s `hrle : r ≤ d₂ + 1` *is* `n ≤ r_m + 1`. What was missing
is the weakening, now landed as `radicand_weaken`. All it actually needs is `n ≤ 2·r_m`, which
`n ≤ r_m + 1` and `r_m ≥ 1` give at once.

**⚠ The methodological point.** Correction fourteen was made from **one display**, read without
the derivation above it. Correction 9 was made from the derivation without the packaging below
it. Both were confident; both were partial; each was precisely the other's blind spot.

Reading a display is not reading a proof. What settles a form is the *passage between* two
displays — the "because" line — and neither correction looked there. This session has now made
the same class of error in both directions within three turns, which is enough to call it a
habit rather than an accident: **when a transcribed formula matters, transcribe the step that
produces it, not the formula.**

⚠ It also means the arc's own arithmetic was right the whole time and was twice overruled by a
reading. `le_two_mul_max_of_sum_le` derives the `r_m` radicand from the truncated sum, which is
exactly display (2)'s left-hand side. That is the third independent confirmation of this arc's
§13 machinery against the source, alongside `Φ_m = εU + εV` and `J(W) ≤ n·Φ_m`.

### ⚠ The `√2 → 2` weakening is this arc's own, not the source's — and it is avoidable

Rewiring §13 to the `n` normalisation turned up a claim in `RothInductionStep`'s header:
"§13's structure has since been read directly and matches — the matrix shape, the uniform-in-row
cost, and the weakening of `√2` to `2` are all confirmed." **The third item is false.**

Display (2) reads `J(A) ≤ t + √((2/r_m)·J(W)) ≤ t + 2·√(J(W)/n)`. The `2` on the right is
`√4`, arriving through `2/r_m ≤ 4/n` — never through `√2 ≤ 2`. Mahler does not round a square
root up to twice itself anywhere in this step.

Where the arc's `√2` actually goes in is one line of `le_two_mul_max_of_sum_le`:

```
have hsq : θ ^ 2 ≤ (2 * q) ^ 2 := by nlinarith    -- from θ²r ≤ 2S ≤ 2q²r, so θ² ≤ 2q²
```

`θ² ≤ 2q²` is `θ ≤ √2·q`; rounding to `(2q)²` discards the factor. `sq_le_two_mul_max_of_sum_le`
keeps the disjunction with the second branch squared and loses nothing;
`sq_branch_strictly_sharper` exhibits `θ = 3/2` at `r = S = 1`, which the rounded branch admits
and the squared one does not.

**Why it matters, quantitatively.** Carried through §14, the rounded branch gives
`s + 2·(√2·(c+1))s`, and bounding `2√2 ≤ 3` yields `c_m = 3c_{m−1} + 4`, i.e. `c_m = 3^m − 2` —
against §14's `2^{m+1} − 3`. Qualitatively either constant proves Roth's lemma, but the arc had
landed `rothConstant` as *the source's* value while its own §13 could not reach it. That gap is
now closed at the arithmetic, not papered over at the statement.

`index_le_or_sq_of_det_bound` is the index-level form: the two branches kept apart, the second
squared, **no `q` and no side condition** — since the branches are complementary by
construction. A caller converts the squared branch with `radicand_weaken`, which is the
source's own `2/r_m ≤ 4/n` step.

⚠ Third claim of the form "confirmed against the source" that turned out to be the arc's own
reconstruction, after `RothGrowth` (which *was* right) and correction 15's radicand. The
pattern is not that the arc reconstructs badly — twice now the reconstruction was correct — but
that **"confirmed" gets written where "consistent with" is what was checked.**

### ⚠ `Γ_M` has four clauses and is a disjunction — and that relocates the last open item

§11 read in full. `Γ_M` is defined for `b, s₁,…,s_M, K₁,…,K_M` (with `0 < t ≤ 1`, `b ≥ 1` real,
the rest positive integers) as: **either**

    (i)   M = 1,  K₁ ≥ 2,  b ≤ K₁^{s₁t};
    (ii)  M ≥ 2  and  simultaneously
          1.  max(s₂/s₁, …, s_M/s_{M−1}) ≤ t
          2.  s_h·log K_h ≥ s₁·log K₁      (h = 1,…,M)
          3.  K₁ ≥ 2^{(1/t)(M−1)M(2M+1)}
          4.  b ≤ K₁^{(1/M)s₁t}

`RothGamma`'s docstring said "`Γ_m` (§11), all three clauses". Wrong twice: there are **four**,
and it is a **disjunction**. Corrected, with the map of where the rest lives — clause 4 is
`RothLemmaUniform`'s height condition (`∀ j, B ≤ qⱼ^E`, `E ≤ (t/m)dⱼ`), and case (i) is the
`m = 1` specialisation whose `K₁ ≥ 2` comes from the standing `2 ≤ qⱼ`. The aggregate matches;
the structure alone is not `Γ₁`.

⚠ **`K_h ≥ 2` is a consequence of `Γ_M`, not a hypothesis** — §11 derives it alongside
`s₁ ≥ … ≥ s_M` and `∑ s_h ≤ M·s₁`. `rothDenomFloor_two_le` and `rothGamma_first_two_le` recover
the first index's case: at `m ≥ 2` and `ω > 0` the floor's exponent is at least `10ω > 0`, so
the floor is at least `2`. `RothLemmaUniform`'s `2 ≤ qⱼ` is redundant there, not additional.

### ⚠ Where "the height chain" actually is

The last two turns ended by naming `b ≤ H₁^{(1/(m−1))ρ₁t}` as the one genuinely unbuilt piece,
"which `theta_one_le_of_gamma` consumes". That framing was wrong: **it is `Γ_{m−1}`'s clause
4.** `theta_one_le_of_gamma` consumes it *because* the sub-system has `Γ_{m−1}`, not because
some separate lemma supplies it.

Which sharpens the open item rather than dissolving it. `rothGamma_descend` produces clauses
1–3 from `Γ_m` and **cannot** produce clause 4: that clause constrains `b`, the sub-system's
**new** height — the Wronskian's — and `Γ_m` constrains `a`, the original. They are different
numbers. So the work is *produce clause 4 for the Wronskian*, which is `WronskianHeight`'s
business.

Recorded on `rothGamma_descend` itself, so the gap is visible where someone would try to use it
and find three fields where four are needed.

⚠ Also confirmed: §11's `(Θ₁)` estimate `Θ₁(a; r; H) ≤ log a/(r log H)` for `H ≥ 2` — the step
`theta_one_le_of_gamma` starts from — and `1 ≤ n ≤ r_m + 1` as an explicit hypothesis on `n`,
which is what `radicand_weaken` needs and `hrle` supplies.

### §11's height step — clause 4 descends, and clause 3 is calibrated exactly for it

§11's descent lemma defines the sub-system's height explicitly:

    b = 2^{2n(r₁+…+r_m)} · n! · a^n,      ρ_h = n·r_h,

and proves `b, ρ₁,…,ρ_{m−1}, H₁,…,H_{m−1}` has `Γ_{m−1}`. Its chain for clause 4:

    n ≤ r_m + 1 ≤ r₁ + 1 ≤ 2^{r₁},  hence  n! ≤ n^n ≤ 2^{n r₁} = 2^{ρ₁};
    a ≤ H₁^{(1/m)r₁t};   r₁ + … + r_m ≤ m r₁;
    therefore  b ≤ 2^{2n·m r₁}·2^{ρ₁}·a^n ≤ 2^{(2m+1)ρ₁}·H₁^{(1/m)ρ₁t} ≤ H₁^{(1/(m−1))ρ₁t}.

Landed as `height_descend_assemble` (the first two lines) and `height_descend_step` (the last),
in logs so everything stays in `ℚ`, and multiplied through by `m` or `m−1` so no division
appears.

### ⚠ Clause 3 fits with nothing to spare

The gap between the two exponents is `1/(m−1) − 1/m = 1/(m(m−1))`, so absorbing the accumulated
`2^{(2m+1)ρ₁}` requires

    t·log H₁ ≥ m(m−1)(2m+1)·log 2,

which **is** clause 3, `K₁ ≥ 2^{(1/t)(m−1)m(2m+1)}`, exactly. `m(m−1)` cancels the exponent gap;
`(2m+1)` matches what `2^{2mρ₁}·2^{ρ₁}` accumulates. That is why the floor's exponent has that
shape and not a rounder one.

This arc carried clause 3 for several turns with no use for it, and twice recorded that some
step would be "the first place clauses 2 and 3 have to be used". Both times that was a guess
about the junction; **this** is the place, and the fit is exact rather than generous. Worth
noting because an unused hypothesis with an oddly specific constant was evidence all along that
something downstream needed precisely it — the arc had the signal and read it as a puzzle
rather than a pointer.

### What is left

`rothGamma_descend` now has all four clauses available: 1–3 from `Γ_m` directly, 4 from
`height_descend_step ∘ height_descend_assemble`. Wiring them into one theorem needs the
Wronskian's actual height bound in the shape `hb` expects — `WronskianHeight`'s
`abs_coeff_det_sepFamily_le` gives `r!·(S·(d^{2r}·B_P))^r`, which is `b`'s shape with `n = r`,
so the remaining work is matching those two expressions, not proving a new estimate.

### Clause 4's descent, integral and exact — and a discipline that nearly cost the arc a theorem

Wiring the four clauses turned up an obstruction in the arc's own idiom, and then a way past it.

**The obstruction.** `RothLemmaUniform` avoids rational exponents by writing the height
condition as `B ≤ qⱼ^E` with `E : ℕ`. Clause 4 in that idiom needs `j`, the number of powers of
`K` that swallow `2^c`, to be a natural number in

    (2m+1)ρ₁ / F   ≤   j   ≤   ρ₁t / (m(m−1)),

and clause 3 makes those endpoints **equal** in the tight case — that is what "calibrated with
nothing to spare" means. A zero-length interval between two non-integers contains no integer,
so no `j` need exist. `height_descend_exp` is the rounded form and carries `j` as a hypothesis
rather than producing one.

⚠ This is intrinsic to the arc's `E : ℕ` device, **not** a gap in the source: §11 uses real
exponents, where `j` is simply `ρ₁t/(m(m−1))` and no rounding arises. The arc bought `ℚ`-only
arithmetic by rounding exponents up, and clause 3 is exactly tight, so the rounding has nowhere
to go.

**The way past.** Write `t = p/q`. Clause 4 `b ≤ K₁^{(1/M)s₁t}` raised to `Mq` is
`b^{Mq} ≤ K₁^{s₁p}` — a statement about integers. Descending from arity `m+1` to `m`, §11's
chain becomes

    b^{m(m+1)q} ≤ 2^{c·m(m+1)q}·(a^{(m+1)q})^{nm} ≤ K^{ρ₁p}·K^{ρ₁pm} = (K^{ρ₁p})^{m+1},

whose middle step needs `c·m(m+1)q ≤ F·ρ₁p` — which is `c ≤ (2m+3)ρ₁` times clause 3's
`q·m(m+1)(2m+3) ≤ F·p`. Both are `ℕ` inequalities, so the tightness that blocks the rounded
route **costs nothing here**. Landed as `height_descend_pq`, and it closes with nothing left
over.

`height_descend_pq_witness` sits exactly on the boundary: `2^F = K`, `c = (2m+3)ρ₁`, and
`q·m(m+1)(2m+3) = F·p` all hold with **equality**. That is the calibration made concrete.

⚠ **The near-miss worth recording.** The first instinct was to state the obstruction, recommend
the `p/q` route, and stop — the entry would have read as a finding. It is a finding only if the
route is not taken; taking it turns the same paragraph into a solved problem. The arc has now
twice written "two ways out, neither taken here" style prose where one of the ways was ten
minutes of work. **A recommendation in a docstring is a bet that nobody will check it.**

### §11's descent lemma, in full — all four clauses in one theorem

`RothGammaFull` is `Γ_M` case (ii) faithfully: `t = p/q`, so `ω = 1/t = q/p`, and **both**
clauses that had a rational exponent become `ℕ` inequalities with nothing rounded.

- clause 3 is `2^F ≤ K₁` plus `q·(M−1)M(2M+1) ≤ F·p` — the floor cleared of division, no
  `Nat.ceil` and so no slack to lose;
- clause 4 is `b^{Mq} ≤ K₁^{s₁p}`.

`rothGammaFull_descend` proves the whole of §11's descent lemma: from `Γ_{n+1}` and
`b ≤ 2^c·a^r`, the sub-system has `Γ_n`. This is what Lemma 4 asserts exists and what
`rothGamma_descend` supplied three quarters of.

### ⚠ Two independently derived inequalities turned out to be the same one

`height_descend_pq`'s hypothesis `hF` is `q·(n(n+1)(2n+3)) ≤ F·p`. `RothGammaFull`'s
`floorExp` at arity `n+1` is `q·((n+1−1)(n+1)(2(n+1)+1)) ≤ F·p`. Those are **literally the same
inequality** — the descent's clause-4 proof discharges `hF` with `hg.floorExp` and nothing else.

They were derived from different places: `hF` from §11's height chain (what it takes to absorb
`2^{(2m+1)ρ₁}`), `floorExp` from §11's floor clause (transcribed from `Γ_M`'s definition). That
they coincide is the strongest confirmation yet that clause 3's exponent is not a chosen
constant but a derived one — and it is now checked by the compiler rather than argued.

`rothGammaFull_descend_witness` satisfies the largest hypothesis stack in this arc. ⚠ Four of
its hypotheses hold with **equality** (`2^F = K`, `q·n(n+1)(2n+3) = F·p`, `c = (2n+3)ρ₁`,
`b = 2^c·a^r`), for the same reason: the calibration leaves no room.

### What is left

`RothGamma` (clauses 1–3, `ω : ℚ`) and `RothGammaFull` (all four, `p/q`) now coexist.
`RothLemmaUniform` still takes the former. Migrating it is a deliberate one-off that touches
every use site, and is worth doing on evidence — which `rothGammaFull_descend` now supplies:
the `p/q` idiom carries everything the `ω : ℚ` one does and clause 4 besides.

### ⚠ The migration is not mechanical — my own "next" understated it

Last entry ended: "Migrate `RothLemmaUniform` onto `RothGammaFull` and retire `RothGamma`.
Touches every use site, so worth doing as one deliberate pass." That framing was wrong in the
same way as the "height chain" one: it named the *count* of edits and missed the *kind*.

`RothLemmaUniform`'s height condition is `∀ j, B ≤ qⱼ^E` with `E : ℕ`, and the base case is
built on it — `RothBaseCase.index_le_of_abs_leadingCoeff_le` takes `|lead| ≤ q^e` and returns
`index ≤ e/d`. Clause 4 is `b^{Mq} ≤ K₁^{s₁p}`, a **different encoding**. Swapping it in means
`RothBaseCase` needs a variant taking a power bound, which is not a use-site edit at all.

Landed instead, both clean:

- `RothGammaFull.toRothGamma` — the full object implies the three-clause one at `ω = q/p`, so
  `rothGammaFull_descend` already feeds everything `RothGamma` feeds. The only content is
  clause 3: `rothDenomFloor` rounds `(q/p)(m−1)m(2m+1)` up, `floorExp` says `F` is already at
  least that, so the ceiling is at most `F`.
- `le_pow_of_pow_le_pow` — the bridge between the two height idioms, with the rounding as an
  explicit hypothesis (`S ≤ Q·e`) rather than a ceiling.

### ⚠ What the migration would cost, and why it is not obviously affordable

From `b^{Mq} ≤ K^{s₁p}` the smallest usable `e` is `⌈s₁p/(Mq)⌉`, so the base case yields
`index ≤ ⌈s₁p/(Mq)⌉/d` rather than `s₁p/(Mqd)`. The excess is at most `1/d`.

Whether `1/d` is affordable is **not obvious and not checked**. `d` is a large degree so it is
small — but clause 3's calibration is exactly tight (`height_descend_pq_witness` sits on the
boundary in *four* hypotheses at once), and this arc has twice found that small slack in a tight
place is exactly where the constants stop working: the `√2` in `le_two_mul_max_of_sum_le` cost
`2^{m+1}−3 → 3^m−2`, and the rounded `j` interval collapsed to empty.

So the check comes before the migration, not after. Recorded in the module rather than left as
a plan, because a plan that has not costed its own main step is the thing this arc keeps
catching itself writing.

### ⚠⚠ The `1/d` slack does not survive the recursion — and smallness is not the issue

The previous entry costed the migration at "at most `1/d`" and called affordability "not
obvious, and not checked". It is obvious once the recursion is written down, and the answer is
the **opposite** of the one smallness suggests.

`rothConstant_step_perturbed` carries the perturbation through one step: from
`Ψ ≤ (c+1)s² + v²` it gives `θ ≤ c_{m+1}·s + 2v`, both branches of the max still landing on
`(c+1)s + v`. Iterating, with `Θ_m ≤ c_m·s_m + κ_m` and `s_{m+1}² = s_m`:

    Ψ_{m+1} ≤ (c_m + 1)·s_{m+1}² + (κ_m + δ),      so   κ_{m+1} = 2·√(κ_m + δ).

**That map expands.** `2√x > x` exactly on `0 < x < 4` (`two_sqrt_expands`), so from any
`κ₁ ≥ 0` and **any** `δ > 0` the sequence increases strictly to the fixed point
`2 + 2√(1+δ) ≈ 4`. A bound of ≈ 4 on an index is worthless — Roth's indices are far below 1.

At `δ = 0` the recursion sits at its other fixed point, `κ = 0`, and stays: that is the
unperturbed argument working. So there is no threshold below which `1/d` becomes safe. The
recursion sends every positive perturbation to the same useless place.

**Consequence, decided.** Do *not* migrate `RothLemmaUniform` onto clause 4's `p/q` form
through the rounded bridge. `le_pow_of_pow_le_pow`'s `S ≤ Q·e` is usable only where `e` is
chosen so no rounding occurs. The version worth building is a `RothBaseCase` variant taking the
power bound **directly** — `|lead|^Q ≤ q^S` giving `index ≤ S/(Q·d)`, no ceiling anywhere.

⚠ This is the third time this arc has asked "is this small slack affordable?" and the second
time the answer was no. The `√2` in `le_two_mul_max_of_sum_le` cost `2^{m+1}−3 → 3^m−2`; the
rounded `j` interval collapsed to empty; and now `1/d` amplifies to ≈ 4. **A square root in the
recursion means slack does not shrink — it grows.** That is the general fact, and it should be
the default expectation rather than a per-case discovery.

### The base case with a power bound — the one route the amplification result leaves open

`index_le_of_pow_abs_leadingCoeff_le`: `|lead|^Q ≤ q^S` gives `index ≤ S/(Q·d)` **directly**, no
ceiling anywhere. That is the shape `RothGammaFull`'s clause 4 produces (`b^{Mq} ≤ K₁^{s₁p}`),
and going through `index_le_of_abs_leadingCoeff_le` instead would need `e : ℕ` with `S ≤ Q·e`,
whose rounding costs `1/d` — which `two_sqrt_expands` shows is fatal at any size.

The proof is the unpowered contradiction raised to the `Q`-th power:
`q^{n₀Q} = (q^{n₀})^Q ≤ |lead|^Q ≤ q^S` against `S < n₀Q`. The exponent only enters at the end,
which is why the generalisation was cheap once the shared half was factored out.

`exists_index_eq_div_and_pow_le` is that shared half — the one-variable index is `n₀/d` for a
natural `n₀`, with `q^{n₀} ≤ |lead|`. Both base-case theorems now derive from it rather than
repeating the `translate`-invertibility and infimum-attainment argument.

### `Θ_m` — the gap named, and §9 mis-estimated

§8 read. Everything in this arc up to here bounds the index of **one** polynomial; Roth's lemma
is about `Θ_m`, the **least upper bound** of `J(A; r; κ)` over two sets:

- `R(a; r₁,…,r_m)` — non-zero integer polynomials of degree `≤ rₕ` in `xₕ`, height `≤ a`;
- `Q(H₁,…,H_m)` — systems of `m` rationals `κₕ = Pₕ/Qₕ` in lowest terms, `max(|Pₕ|,|Qₕ|) ≤ Hₕ`.

⚠ **The previous entry recorded §9 as "Siegel's lemma plus a counting argument, the biggest
unbuilt piece". That is wrong.** Siegel's lemma appears nowhere in §9. What §9 establishes is:
both sets are **finite**, so the lub is **attained**; `Θ_m` is non-decreasing in `a`; and
`0 ≤ Θ_m ≤ m`. All elementary.

The mis-estimate came from reading a section **title** — "The upper bound `Θ_m(a; H; r)`" — and
inferring its content. Same failure as correction 14 (one display, no derivation) at a coarser
grain: a title is even less of a proof than a display.

### Options considered for the gap, and the one taken

- **(A) `Finset.sup'` over explicit finite sets.** Faithful; gives attainment, monotonicity in
  `a`, and `0 ≤ Θ ≤ m` for free from `Finset` lemmas. Costs a `Fintype` construction for
  bounded-degree bounded-height integer polynomials.
- **(B) `sSup`/`iSup` over a predicate.** Cheaper to state, but attainment then needs a separate
  argument — which *is* the finiteness. Defers the work without removing it, and §13 needs the
  maximiser, so it does not unblock anything.
- **(C) Characterise rather than construct.** `IsRothTheta a r H Θ` := upper bound + attained.
- **(D) Avoid `Θ_m`, keep bounding individual polynomials.** What the arc does now; it cannot
  state Lemma 4.

**Taken: (C), with (A) as the discharge.** `IsRothTheta` pins the value (`IsRothTheta.unique`),
so any later construction agrees with it and downstream statements need not wait. The existence
half is an **undischarged obligation** — but unlike corrections 9 and 10's hypotheses it is
*known satisfiable*, because the sets are finite. That distinction is the whole reason (C) is
acceptable here and was not there.

Landed: `InRothPolySet`, `InRothFracSet` (Lean's `ℚ` is reduced, so Mahler's coprimality is
carried by the type), `IsRothTheta`, `.unique`, `.nonneg`, and `idxWeight_le_card`.

⚠ `Θ_m ≤ m` is **not** yet available: `index` is an infimum over the *translated* support, and
`degreeOf_translate` does not exist in this arc. That is the remaining piece of §9's third
property and is the next concrete item.

### `degreeOf_translate`, and §9's three properties complete

Run as a workflow: four independent proof strategies in parallel, then four adversarial
verifiers, each rebuilding from scratch. All four strategies compiled; all four refutation
attempts failed. Three things came out of the fan-out that a single attempt would have missed:

- **`[DecidableEq σ]` and `[Nontrivial R]` are both unnecessary.** The `DecidableEq` is supplied
  by an internal `classical`; the `Nontrivial` is avoided by deriving the `X`-degree bound from
  `coeff_X'` rather than `degreeOf_X` (which carries it). Stating `degreeOf_X_le` against
  `(single i 1) j` instead of `if i = j then 1 else 0` keeps the instance out of the statement.
- **It is an equality, not just an inequality.** `degreeOf_translate_eq` follows by
  `le_antisymm` through `translate_neg_translate` — free, and strictly more useful.
- ⚠ **`MvPolynomial.induction_on` cannot prove this**, which was my first instinct. Its additive
  step would need `max (degreeOf j p) (degreeOf j q) ≤ degreeOf j (p + q)`, and that is **false**:
  take `p = X j`, `q = −X j`. The route that works decomposes `P` over its own support.

Also established by exhaustive search (two agents independently): **Mathlib has no general
`degreeOf` bound under `aeval`/`bind₁` substitution.** `Mathlib/Algebra/MvPolynomial/Monad.lean`
contains no occurrence of "degree" at all; the only substitution-vs-degree lemmas are for
`rename` and `map`. Neither `coeff_translate` nor `support_translate` exists at this pin.

**§9 is now complete.** All three properties hold:

| property | status |
|---|---|
| lub attained (finiteness) | carried by `IsRothTheta`'s second clause; construction still open |
| `Θ_m` non-decreasing in `a` | `IsRothTheta.mono_height` |
| `0 ≤ Θ_m ≤ m` | `IsRothTheta.nonneg`, `IsRothTheta.le_card` |

`Θ_m ≤ m` is what needed `degreeOf_translate`: the index is an infimum over the **translated**
support, so a degree hypothesis on `A` reaches it only because translation preserves degree.
That dependency is why the bound could not be stated two entries ago and can be now.

### §9's existence obligation, discharged — and a verifier that refused to sign off

Run as a workflow: four pieces built in parallel (finiteness of `R(a;r)`, finiteness of `Q(H)`,
non-emptiness, the assembly), then four adversarial verifiers. All four pieces compiled and
were axiom-clean.

⚠ **Three verifiers confirmed; the fourth returned `statementIsRight: false`, and was right.**
The assembly agent had produced

    exists_isRothTheta [Fintype σ] … (hfinA : …Finite) (hfinK : …Finite) (hneA …) (hneK …)

and its verifier observed: *given that `Fintype`, both finiteness hypotheses are derivable —
and the finiteness IS the obligation.* The theorem hypothesised away exactly the content it was
billed as discharging, while carrying the instance that would discharge it. It then went and
built the fully-discharged form itself. That is the version landed:

    exists_isRothTheta [Finite σ] (a r H) (ha : 1 ≤ a) (hH : ∀ h, 1 ≤ H h) : ∃ Θ, IsRothTheta a r H Θ

⚠ Both remaining hypotheses are **necessary**, not convenient: `a ≤ 0` empties `R(a;r)` (a
non-zero polynomial has a non-zero coefficient, so `1 ≤ |coeff| ≤ a`), and `Hₕ = 0` empties
`Q(H)` (every rational has `den ≥ 1`). An empty set has no maximum to attain.

This is the failure mode the arc has been recording all session — a hypothesis that quietly
does the work the theorem claims to do — caught here by an adversarial reader rather than three
turns later by a contradiction. **That is what the verify phase is for, and it is the first time
in this arc it has actually overturned something.**

### What the finiteness needed

Neither half had a ready-made Mathlib lemma:

- **Polynomial side.** The closest thing is `MvPolynomial.finite_setOf_bounded` in
  `Mathlib/RingTheory/MvPolynomial/Basic.lean` — **private**, and with a *uniform* degree bound
  rather than a per-variable one. Rebuilt as `finite_setOf_forall_le` (the exponent box) plus
  `finite_setOf_degreeOf_le_coeff_le`, the latter stated **without** `A ≠ 0` and **without** a
  sign hypothesis on `a`, because neither is used — at `a < 0` the set is empty and the proof
  never has to notice.
- **Rational side.** Nothing at all. `Finsupp.fintype` needs a finite codomain and `ℚ` is not
  one, so the finiteness comes entirely from the height bound, via `Rat.ext` injectivity of
  `q ↦ (q.num, q.den)`. Needed one extra import, `Mathlib.Data.Int.Interval`, for
  `LocallyFiniteOrder ℤ`.

⚠ Environment note recorded by a verifier: `Mathlib/Data/Finsupp/Interval.olean` is **not built**
in this checkout, so the `Finset.Iic`-on-Finsupps route the task prompt suggested is unusable
here — `failed to synthesize LocallyFiniteOrderBot (Fin 1 →₀ ℕ)`. The `Set.Finite.pi'` route
works and needs no `DecidableEq`.

`Θ_m` is now a characterised object that provably exists, and `IsRothTheta.unique` makes it
*the* `Θ_m`. §9 is complete: finiteness, attainment, monotonicity in `a`, and `0 ≤ Θ_m ≤ m`.

### Lemma 4 and Roth's Lemma, stated in `Θ_m` form — and the induction step proved

With `Θ_m` characterised and known to exist, the source's own two statements can finally be
written. Every statement in this arc before now bounded the index of **one** polynomial.

- `RothLemma4 σ n p q F` — §13's packaged conclusion: from `Γ_{n+1}` and `Θ_{n+1}`, there
  *exists* a sub-system with `Γ_n` and its own `Θ_n` such that `Θ_{n+1} ≤ t + 2·max(Ψ, √Ψ)`,
  with `Ψ = Θ_n + t` and the max encoded root-free as `w = Ψ ∨ w² = Ψ`.
- `RothLemmaTheta σ m p q F` — §14: `Γ_m` forces `RothBound m t Θ`.

⚠ Both are `def`s and neither is proved. What **is** proved is the implication between them:

`rothBound_succ_of_lemma4` — Lemma 4's conclusion plus `RothBound n t Θ'` gives
`RothBound (n+1) t Θ`. This is §14's induction step in `Θ` language, and it is the first
theorem in the arc whose statement is about Roth's lemma rather than about a polynomial.

The bookkeeping that makes it a single-parameter induction: **both levels sit at the same `t`**.
Level `n` uses the variable `s²`, level `n+1` uses `s`, and `(s²)^{2^{n−1}} = s^{2^n}`. So no
reparameterisation happens across the step — which is what `rothBound_pow_iff` was for.

⚠ Note the leading term is `t`, not `s`. Lemma 4 leads with the row cost; `t ≤ s` (from
`0 ≤ s ≤ 1` and `2 ≤ 2^n`) is what lets `rothConstant_step_lemma4` accept it. That is the same
`t`-vs-`s` distinction corrections 12 and 15 were about, now discharged mechanically rather
than argued.

`rothBound_succ_of_lemma4_witness` sits on the boundary in three hypotheses at once (`Θ' = t`,
`w = Ψ`, `Θ = t + 2w`).

### §14's induction, closed — and why it must name `s`

`rothConstant_chain` runs the whole induction: given the step at every level, `Θ_n ≤ c_n·s_n`
propagates from the base case up. `rothBound_chain` is the same in `RothBound` shape. The
sequence `sq` is `s_n`, each the square root of the previous (`sq (n+1)² = sq n`), which is what
keeps the entire chain at a **single** `t`.

⚠ **The chain needs the `s_n` to exist as rationals**, and for a general rational `t` they do
not — `s_n = t^{2^{−(n−1)}}` is irrational. So this closes the induction exactly for `t` a
perfect `2^{m−1}`-th power of a rational. That is a genuine restriction and it is the price of
staying in `ℚ`.

### ⚠ The root-free route fails at the first step

The obvious attempt is to induct directly on `RothBound`'s squared form, never naming `s`. With
`k = 2^{n−1}`, from `Θ'^k ≤ c_n^k·t`, `Θ ≤ t + 2w`, `w² = Θ' + t`, bounding
`(a+b)^k ≤ 2^k(a^k+b^k)` twice and using `t ≤ 1`:

    Θ^{2k} ≤ 4^k·(8^k·(c_n^k + 1) + 1)·t,

leading behaviour `(32c_n)^k`, so the route needs `32c_n ≤ (2c_n+3)²`. At `c_n = 1` that is
`32 ≤ 25` — **false** — and `c₁ = 1`, so it fails at the very first step
(`crude_chain_fails`).

⚠ This does not prove no root-free route exists; it shows the natural crude one loses too much.
Same `√`-slack failure as everywhere else in this arc — the fourth instance now, after the
`√2`, the rounded `j` interval, and `1/d`. **Every one of them was a place where a convenience
approximation met a constant that had no room.**

The chain naming `s` is therefore not a stylistic choice but the thing that makes the induction
go through, and `rothBound_pow_iff` — landed several turns ago as a convenience — turns out to
be the load-bearing conversion.

### ⚠⚠ Correction sixteen — `InRothFracSet` used `≤` where §9 says `=`, and that made the statement false

§9 defines `Q(H₁,…,H_m)` as the systems `κₕ = Pₕ/Qₕ` **of heights** `Hₕ = max(|Pₕ|,|Qₕ|)` — an
**equality**. My definition, landed three turns ago, used `≤`.

**That is not a weakening, it is a falsification.** `Θ_m` is a supremum over `Q(H)`; enlarging
the set enlarges the sup, and §10's bound then fails outright. Concretely at `H = 100`, `a = 2`,
`r = 1`: with `≤`, the point `κ = 1/1` has height `1 ≤ 100` and `A = x − 1` has index `1`,
against `log a/(r log H) = log 2/log 100 ≈ 0.15`. With the equality, `κ` must have height `100`,
so `A` would need `|lead| ≥ 100 > a` and the index is `0`.

Same failure mode as `Γ_m`'s missing clauses — a weakened hypothesis makes the statement
*stronger*, and a statement stronger than the source's is one the source will not prove. The
arc has now made this exact mistake three times (Γ's clauses 2–3, Γ's clause 4, and this), which
is enough to name it: **when transcribing a definition, check whether each bound is `≤` or `=`,
because the two differ only in a character and invert which direction the statement is safe in.**

Knock-on: `exists_inRothFracSet`'s witness can no longer be `κ ≡ 0` (height `1`); it is now
`κₕ = Hₕ`, an integer of height exactly `Hₕ`. `finite_rothFracSet` still holds, as a subset of
the `≤` version.

### ⚠ What §10 actually needs, and the half this arc lacks

§10's proof, read verbatim:

> `A(x) = (Qx − P)^j·B(x)` with `B` integral, hence the **lowest** and the **highest** non-zero
> coefficients of `A` are divisible by `P^j` and `Q^j` respectively. It follows that
> `H^j ≤ |A| ≤ a`.

This arc has only the `Q^j` half — `pow_le_abs_leadingCoeff_of_le_index` gives `q^k ≤ |lead|`,
the highest coefficient, divisible by the *denominator*. The `P^j | lowest` half is missing, and
without it one can only conclude `Q^j ≤ a`, never `H^j ≤ a`.

**That is precisely why this arc's base case is stated with `a ≤ q^E` rather than `a ≤ H^E`**,
and it is the concrete form of this bean's original headline: *the height theory is the real
cost, not the Wronskians*. Three months of Wronskian machinery, and the remaining gap is one
divisibility statement about a lowest coefficient.

⚠ The missing half should come by symmetry: reversing a polynomial swaps lowest and highest
coefficients and sends `κ ↦ 1/κ`, i.e. `P ↔ Q`. Recorded in `RothBaseCase` so the next attempt
starts from the reversal rather than from scratch. Not attempted here.

### §10's missing half — proved. And correction seventeen.

Both halves of §10 are now in `QOU/Mathlib/RothHeightBound.lean`, and §10's estimate itself is
`MvPolynomial.index_le_of_abs_coeff_le` in `QOU/Mathlib/RothBaseCase.lean`:

    a ≤ H^e,  H = max(|p|,|q|) ≥ 2,  |coeff n P| ≤ a,  gcd(p,q)=1,  P ≠ 0,  d ≠ 0
      ⟹  index_d(P; p/q)  ≤  e/d

Log-free by choice: taking logarithms gives Mahler's `Θ₁ ≤ log a/(d log H)`, but the recursion
is sensitive to rounding (`two_sqrt_expands` shows any positive perturbation is amplified to
≈ 4), so the exponential form is what gets carried.

**⚠⚠ Correction seventeen.** The previous entry above, and `RothHeightBound`'s own "Next" block,
called `pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero` *"the `m = 1` base case of Roth's
lemma, complete and with no analysis in it"*. The theorem is true. The label was the name of the
statement it was a **step toward** — and read back later, a label becomes a completion.

Same species as corrections 12 and 14, and it survived for the same reason both did: **nothing
in a green build objects to a docstring.** Every mechanical check this arc runs — `lake build`,
`#print axioms`, the linter — passes on a file whose prose claims twice what its theorems prove.
The only check that catches it is re-reading the source next to the Lean, which is what produced
17 of the 17.

**⚠ The recorded plan was wrong about the method.** It said the half "should come by symmetry:
reversing a polynomial swaps lowest and highest and sends `κ ↦ 1/κ`" and told the next attempt
to start there. Reversal works, but it is unnecessary: `Polynomial.trailingCoeff` is
multiplicative in a domain for exactly the reason `leadingCoeff` is, so `trailingCoeff_dvd_of_dvd`
+ `trailingCoeff_qX_sub_C` give the half **directly**, in four lines, with no reversal and no
reciprocal. The plan came from thinking about the *page* — where "the lowest and the highest …
respectively" invites a symmetry argument — rather than about the available API. Worth noting
because the plan was recorded as guidance for the next agent, and it would have cost them the
detour.

What the plan did get right is that the halves are **not** symmetric. `q > 0` is free (Lean's ℚ
keeps a positive denominator) but `p ≠ 0` is not, and at `κ = 0` Mahler's clause is *vacuous*
rather than false: `P^j = 0` divides only `0`. The assembled bound discharges that corner
separately, where coprimality forces `q = 1` and `H^j = 1`.

**Why the half was never a detail.** `H = max(|P|,|Q|)`, so the leading half bounds `|Q|^j` and
proves nothing whenever the numerator carries the height. Validated in Lean at the smallest such
point: `κ = 3/1`, `P = X − 3`, `d = 1`, `e = 1` — the new theorem gives `index ≤ 1`, which is the
true value, and `index_le_of_abs_leadingCoeff_le` (which needs `q ≥ 2`) does not apply at all.

**Refactors, because the same block had been written out twice and was about to be a third
time:** `exists_index_eq_div` (the index in one variable is literally `n₀/d` — and it needs *no*
hypothesis on `d`, since `idxWeight` reads `n/d` in ℚ where `n/0 = 0`), `taylor_coeff_eq_zero_of_index_eq`,
and `map_qX_sub_C_pow_dvd_of_taylor_coeff_eq_zero` (the ℚ-divisibility step both height halves
consume).

**Next:** `Θ₁ ≤ e/d` — feeding this into `IsRothTheta`'s attainment clause at `σ = Unit`. Needs a
naturality lemma (`pUnitAlgEquiv` commutes with coefficient maps) and `IsCoprime (num) (den)`
from `Rat.reduced`. Mechanical, but it is the base case *in Θ form*, which is what §13/§14's
recursion actually consumes.

### ⚠⚠ Correction eighteen — `K_h` is the HEIGHT `H_h`, not the denominator

Read from the page scan of §11 (doc p. 91), immediately after the abstract definition of `Γ_M`
on `b, s₁,…,s_M, K₁,…,K_M`:

> By way of application, let `m ≥ 2`; let the ordered system of numbers `a, r₁,…,r_m, H₁,…,H_m`
> have the property `Γ_m`

So `b = a`, `s_h = r_h`, **`K_h = H_h`**. §13's descent settles it beyond argument: the new
system is `b, ρ₁,…,ρ_{m−1}, H₁,…,H_{m−1}` — *the same heights, truncated* — and its clauses are
printed as `ρ_h log H_h ≥ ρ₁ log H₁` and `H₁ ≥ 2^{(1/t)(m−1)m(2m+1)}`, in `H` throughout.

This arc called the field `qd`, the definition `rothDenomFloor`, and the clauses "the first
*denominator*". Renamed to `Kh` / `rothHeightFloor`, with the correction recorded at the
definition. The structures themselves were already right — `RothGamma` is abstract in the
parameter and `rothGamma_descend` truncates it, which is exactly §13's descent — so nothing
proved was false. **What was false was an inference drawn from the name.**

**The inference, and why it mattered.** The record above says clause (i) is "the `m = 1`
specialisation whose `K₁ ≥ 2` comes from the standing `2 ≤ qⱼ`". Read with `K = H` that is a
different statement, and the consequence is sharp:

    clause (i) supplies   a ≤ H₁^{r₁t}
    the q-form of §10 gives   Θ₁ ≤ log a/(r log q)  ≤  t·log H/log q   ≥  t

so the `q`-form **cannot** close the base case — it lands on the wrong side of `t` by exactly
the factor `log H/log q ≥ 1`. Only the `H`-form does:

    a ≤ H₁^{r₁t}  and  Θ₁ ≤ log a/(r log H)   ⟹   Θ₁ ≤ t.

So the `P^j` half proved earlier this session was never optional and never a symmetry
nicety — **it is precisely the hypothesis `Γ₁` hands over.** The bean's own earlier note that
"that gap is exactly why this arc's base case is stated with `a ≤ q^E` rather than `a ≤ H^E`"
was right about the symptom and had not connected it to `Γ`.

**The arc was internally inconsistent and did not notice.** Two docstrings in
`RothLemmaStatement.lean` (around §13's `ρ_m log H_m ≥ ρ₁ log H₁` discussion) already wrote the
clause in `H`, while the structure they describe was named for `q`. Nothing checks prose against
prose. Corrections 17 and 18 are the same failure at one remove: **17 was a label read back as a
theorem, 18 was a name read back as an identification.**

Method note: 18 came from reading the page scan for a question the Lean could not raise —
"what does `K_h` denote?" is invisible to `lake build`, because the structure is abstract in it
and every theorem about it is true either way.

### The base case is closed — `Γ₁ ⟹ RothBound 1 t Θ₁`

`rothBound_one_of_gamma_one`. The chain, all `#print axioms`-clean:

    Γ₁ clause (i):  a^q ≤ H^{r·p}          (t = p/q, cleared of its exponent)
      → index_le_of_pow_abs_coeff_le       index ≤ S/(Q·d)
      → isRothTheta_le_of_gamma_one        Θ₁ ≤ t
      → rothBound_one_of_gamma_one         RothBound 1 t Θ₁

`RothBound` is the shape `rothBound_chain` and `rothConstant_chain` consume, so the base case
now *enters* the recursion rather than sitting beside it needing translation. Correction eleven
traced `c_m = 2^{m+1} − 3` to the base case rather than to the recurrence; this is that starting
value, proved from `Γ₁` instead of assumed.

The powered form is the one `Γ₁` delivers. Routing through the unpowered `a ≤ H^e` would need an
`e : ℕ` with `s₁p ≤ q·e`, and `two_sqrt_expands` says the recursion amplifies that `1/d` to `≈ 4`
however small it starts — the fourth time in this arc that a rounding step turned out to cost
more than it saved.

**Roadmap after today.** §9 done, §10 done (both halves, `Θ` form, `Γ₁` form). Remaining:

1. **§12** — `hfac` and `hres` are still *assumptions* in `index_le_of_rothGrowth_of_factor_bound`.
   This is now the largest open item.
2. **§13/§14 assembly** — `RothLemma4` and `RothLemmaTheta` are `def`s; nothing proves them for
   `m ≥ 2`.
3. **The induction step itself** — `RothLemmaUniform`/`RothLemmaMahler` remain `def`s proved only
   at `m = 1`.

### Correction eighteen, second consequence — `RothLemmaUniform` restated on heights

`RothLemmaUniform` quantified **one** function `qd : σ → ℤ` and used it in two incompatible
roles: as the denominator of the point (`index d (fun j => pn j / qd j)`, `IsCoprime (pn j) (qd j)`)
and as `Γ_m`'s `K_h` (`RothGamma o ω d qd`, `B ≤ qd j ^ E`). Under correction eighteen those are
different objects, and `H ≥ Q` with equality only when the denominator dominates.

The old form was **not false.** `B ≤ Q^E` implies `B ≤ H^E`, so it was a theorem with a stronger
hypothesis and a weaker conclusion. What it could not be is *fed from `Γ_m`*, which supplies only
`B ≤ H^E`. Since the induction consumes this schema at `m − 1` and `Γ` is what the induction
carries, the old form was unusable at exactly its point of use — the same defect as the base
case's, one level up, and from the same root.

Restated: the point is a rational `κ : σ → ℚ` (Lean's `ℚ` supplies lowest terms and a positive
denominator, so the coprimality clause §9 states is carried by the type and disappears), and
`Kh` is pinned to its height by `∀ j, max |(κ j).num| |((κ j).den : ℤ)| = Kh j` — the same shape
`InRothFracSet` took after correction sixteen. Two fewer hypotheses, one more, and strictly
stronger.

`rothLemmaUniform_one` now routes through `index_le_of_abs_coeff_le`, i.e. through **both**
halves of §10. It has to — the `Q^j` half cannot bound `B` by a power of the *height*. Updated
in step: `index_rescaled_wronskian_le`, `index_rescaled_wronskian_le_right`, both witnesses, and
the satisfiability example. All rebuild, standard axioms.

⚠ **Self-correction from this session:** the `Θ`-form work added `map_pUnitAlgEquiv`, which is
`pUnitAlgEquiv_map` — already sixty lines up in the same file, added earlier in this arc.
Removed. The lesson is the one `beans` already carries in a different domain: *check before you
create*. A duplicate lemma type-checks, so nothing objects.

**Both halves of `hres` now have the right shape.** `index_rescaled_wronskian_le` (the `x` half,
from the induction hypothesis) and `index_rescaled_wronskian_le_right` (the `y` half, from the
base case) are stated in `κ` and heights, so `Γ` can feed them. `hfac` in
`index_le_of_rothGrowth_of_factor_bound` is still an assumption — assembling the two halves into
it is the next step, and it is now a matter of composition rather than of a missing theorem.

### ⚠ A gap nothing had noticed: the separated representation carried no degree bound

`hres`'s `x` half is `index_rescaled_wronskian_le`, which needs `degreeOf j (φ k) ≤ d₁ j` before
`RothLemmaUniform` at `m − 1` can apply. **Nothing in the chain from `P` to `φ` supplied any
bound on the factors' degrees.** `exists_sepW_ne_zero_le_degreeOf` gave `0 < r`, `r ≤ d + 1`,
the operator-length bounds, the representation equation, and non-vanishing — and no degrees. So
`hres` was not merely un-discharged; it was **un-dischargeable** as the chain stood.

The arc had `n ≤ r_m + 1` from the *same* construction and not this, which is why it went
unnoticed: the construction was mined for the clause the recursion's row cost needed and not
for the clause the induction hypothesis needed. §7 supplies it on the source's side — "the
degrees of `U` in `x₁,…,x_{m−1}` do not exceed `ρ₁,…,ρ_{m−1}`".

Now proved and threaded through every level:

    exists_separated_representation_monomial_right   φ j is a sum of monomials whose exponents
                                                     are x-parts of P's own support
    exists_separated_representation_fin_right        + the ψ side (bare monomials)
    exists_shorter_of_{phi,psi}_dep                  shortening preserves any degree bound
    exists_indep_representation                      composition through the induction
    ..._indep_card_le, ..._indep_le_degreeOf         ∀ k x, degreeOf x (φ k) ≤ degreeOf (inl x) P
    exists_sepW_ne_zero_le_degreeOf                  both clauses, where the recursion reads them

The mathematics is cheap — the shortening steps replace `φ i` by `φ i − c·φ j`, and a degree
bound survives a linear combination. The clause is stated as *preservation*
(`∀ D, (∀ k x, degreeOf x (φ k) ≤ D x) → ∀ k x, degreeOf x (φ' k) ≤ D x`) rather than against a
fixed `D`, which is what lets it compose through the induction without threading `P` down.

**What this unblocks.** `hres` is now composable: both halves have the right shape (correction
18b) and the degrees they ask for are available (this). What is still missing before `hres` can
actually be built is §12's height estimate — a uniform `B` and `E` with `B ≤ H^E` and
`E ≤ ε·(r·d j)`, where `abs_coeff_det_pderivList_le` gives `B = r!·(S·(d^L·B₀))^r` and §12
computes `b = 2^{2n(r₁+…+r_m)}·n!·a^n`. That is doc pages 92–93, **not yet read**.

### §12's height estimate, read from the page scan (doc p. 92)

Verbatim, the tail of §11's descent proof:

    n ≤ r_m + 1 ≤ r₁ + 1 ≤ 2^{r₁},   hence   n! ≤ n^n ≤ 2^{n r₁} = 2^{ρ₁}
    and, by assumption,   a ≤ H₁^{(1/m) r₁ t},   r₁ + r₂ + … + r_m ≤ m r₁
    Therefore
      b ≤ 2^{2n·m r₁} · 2^{ρ₁} · a^n  ≤  2^{(2m+1)ρ₁} · H₁^{(1/m) ρ₁ t}  ≤  H₁^{(1/(m−1)) ρ₁ t}
    because
      H₁^{(1/(m−1))ρ₁t} / H₁^{(1/m)ρ₁t} = H₁^{(1/(m(m−1)))ρ₁t} ≥ 2^{(2m+1)ρ₁}

The last step is clause 3 exactly — `H₁ ≥ 2^{(1/t)(m−1)m(2m+1)}` raised to `ρ₁t/(m(m−1))` —
which this arc had already identified. The new content is the rest: `ρ₁ = n·r₁`, `n! ≤ 2^{ρ₁}`
via `n ≤ 2^{r₁}`, and `Σ r_h ≤ m r₁` (which is `Γ`'s derived `Σ s_h ≤ M s₁`). The conclusion
`b ≤ H₁^{ρ₁t/(m−1)}` is **clause 4 at arity `m−1`**, with `ε` moving `t/m → t/(m−1)`.

⚠⚠ **An open question, deliberately not recorded as a correction — §13 has not been read.**

`RothLemmaUniform` asks for a **single** `E` with `∀ j, B ≤ Kh j ^ E` *and* `∀ j, E ≤ ε·d j`.
§11 states clause 4 only at `h = 1` (`b ≤ K₁^{(1/M)s₁t}`); clause 2 (`K_h^{s_h} ≥ K₁^{s₁}`)
propagates it as `b ≤ K_h^{ε s_h}` — an exponent that **varies with `h`**. A single `E` bounded
by `ε·min_h d_h` does not follow: `E ≤ ε s_h` makes `K_h^E ≤ K_h^{ε s_h}`, so `b ≤ K_h^{ε s_h}`
is the wrong direction to give `b ≤ K_h^E`.

So the uniform-`E` form may be a hypothesis `Γ` cannot supply — the same defect as corrections
18 and 18b, a third time. **Or it may be exactly what §13's recursion produces**, in which case
the varying exponent is absorbed somewhere I have not read.

I do not know which, and the arc's own history says guessing here is how corrections 14 and 17
happened: 14 read one display without the derivation, 17 read a label without the theorem. The
answer is in §13 (doc pp. 93–95), which is the next thing to read — **before** any change to
`RothLemmaUniform`'s `E`.

### Correction nineteen — the uniform-`E` question, answered by §12, and my flag was aimed wrong

The previous entry flagged that `RothLemmaUniform`'s single `E` might not be suppliable from
`Γ`, and said §13 would settle it. §12 (doc p. 93) settles it, and the answer is sharper than
the question: **the induction never uses an `E` at all.** At the point of invocation Mahler
writes

    J(U; ρ₁,…,ρ_{m−1}; κ₁,…,κ_{m−1}) ≤ Θ_{m−1}(b; ρ₁,…,ρ_{m−1}; H₁,…,H_{m−1})
    J(V; ρ_m; κ_m)                    ≤ Θ₁(b; ρ_m; H_m)
    Φ_m = Θ_{m−1}(b;ρ;H) + Θ₁(b;ρ_m;H_m),   J(W;r;κ) ≤ n·Φ_m   (since ρ_h = n·r_h)

Both bounds are **the definition of `Θ`** — `U ∈ R(b;ρ)`, `κ ∈ Q(H)`, nothing else. The `Γ`
clauses enter *separately*: §11's descent proves `Γ_{m−1}` for the descended system, and that is
what lets the induction hypothesis bound `Θ_{m−1}`.

So `RothLemmaUniform` fuses two things the source keeps apart — set membership and `Γ` — into
one `∀`-statement sharing an `E`. The flagged arithmetic was right (clause 2 propagates clause 4
with an exponent that varies with `h`, so a single `E ≤ ε·min_h d_h` does not follow), but the
conclusion to draw is not "fix `E`": it is that the `E`-encoded schema is the wrong object.
**`RothLemmaTheta` — `Γ` as hypothesis, `IsRothTheta` for the sup, `RothBound` as conclusion,
no `E` — was already the right shape**, and `isRothTheta_le_of_gamma_one` (proved earlier this
session) is its `m = 1` case. The arc built the correct formulation without knowing it was the
correct one.

⚠ Worth naming: holding the question open one turn was the right call. Answering it from the
arithmetic alone would have produced a "fix" to `E` — plausible, self-consistent, and aimed at
the wrong object. That is correction fourteen's shape exactly.

### ⚠⚠ Correction twenty — `RothLemmaTheta` was FALSE at `m = 1`

`RothGammaFull` encodes `Γ_M`'s case **(ii)**, which requires `M ≥ 2`. At `M = 1` the source uses
case **(i)**: `M = 1, K₁ ≥ 2, b ≤ K₁^{s₁t}`. Nothing in case (ii) forces `K₁ ≥ 2` when `m = 1` —
clause 3a reads `q·((1−1)·1·3) ≤ F·p`, i.e. `0 ≤ 0`, so `F = 0` is admissible and clause 3b says
only `1 ≤ K₁`.

Counterexample, every clause checked by hand:

    σ = Unit,  m = 1,  p = 1,  q = 2  (t = 1/2),  F = 0,  a = 1,  r ≡ 1,  H ≡ 1
    growth       vacuous (one variable, no consecutive pair)
    height       1 ≤ 1
    floorExp     2·((1−1)·1·3) = 0 ≤ 0·1 = 0
    floor        2⁰ = 1 ≤ 1
    heightBound  1^(1·2) = 1 ≤ 1^(1·1) = 1
    Θ = 1        attained at A = x − 1, κ = 1 (height max(1,1) = 1, so κ ∈ Q(1)),
                 whose translate is x, support {1}, idxWeight 1/1 = 1
    conclusion   RothBound 1 (1/2) 1  asks  1 ≤ 1/2.          FALSE

A second, independent failure: `q = 0` makes `t = p/0 = 0` in `ℚ` while `heightBound` degenerates
to `1 ≤ K₁^{r₁p}`, so `Θ ≤ 0` is demanded — false at `a = 100`, `H = 2`, `A = 2x − 1`, `κ = 1/2`,
where `Θ ≥ 1`. §14's Theorem 1 opens with `0 < t ≤ 1`; `RothLemmaMahler` carried it and
`RothLemmaTheta` did not.

**Fixed** by adding to `RothGammaFull` the two clauses §11 actually carries —
`two_le : ∀ j, 2 ≤ Kh j` (§11's derived list "K₁ ≥ 2, K₂ ≥ 2, …, K_M ≥ 2"; a *consequence* at
`m ≥ 2`, where `(m−1)m(2m+1) ≥ 10` forces `F ≥ 1`, and case (i)'s *statement* at `m = 1`) and
`degPos : ∀ j, d j ≠ 0` (§11's "positive integers") — and by carrying `0 < t ≤ 1` on
`RothLemmaTheta`. `rothGammaFull_descend` drops its separate `hq2` hypothesis in exchange.

This is the **fifth** time in this arc that a missing clause in a hypothesis object made a
statement stronger than the source's. The list is now long enough to be a rule rather than an
anecdote: `Γ`'s clauses 2–3, `Γ`'s clause 4, `InRothFracSet`'s `≤` for `=`, `RothLemmaUniform`'s
fused `Kh`, and this. **Every one was found by re-reading the source, none by any mechanical
check** — a missing hypothesis type-checks perfectly.

### `RothLemmaTheta` is now proved at `m = 1`

`rothLemmaTheta_one`. `RothGammaFull.heightBound` at `m = 1` is `a^{1·q} ≤ K₁^{r₁p}`, which is
case (i) cleared of its exponent; `two_le` supplies case (i)'s `K₁ ≥ 2`; `isRothTheta_le_of_gamma_one`
gives `Θ ≤ t`; `rothBound_one` packages it. First instance of `RothLemmaTheta` proved, and the
starting value `c₁ = 1` that `rothConstant_chain` needs.

⚠ Also caught: the module's summary paragraph still read "Both are `def`s, and neither is
proved" after `rothLemmaTheta_one` landed. Correction seventeen's failure mode, twice in one
session. Fixed, and flagged in place.

⚠ `RothLemma4` has the same shape and has **not** been checked against correction twenty. Its
conclusion `Θ ≤ t + 2w` is weaker so the counterexample does not transfer directly, and none has
been sought. Recorded as unchecked rather than asserted either way.

### §12's step, in the shape §12 uses it

`index_rescaled_wronskian_le_theta` and `..._right_theta` — the two halves of `hres` consuming
`IsRothTheta`'s upper-bound clause directly instead of the `RothLemmaUniform` schema. Both
proved first try, with a witness.

The evidence that this is the right formulation is the hypothesis stack. Against the schema
versions these drop **`Kh`, `E`, coprimality, `2 ≤ Kh`, `RothGamma`, and `r ≠ 0`** — six
hypotheses — and prove in a third the lines. §12 asks for `U ∈ R(b;ρ)` and `κ ∈ Q(H)`; that is
all `IsRothTheta.1` wants, so nothing else has to be threaded through.

The `RothLemmaUniform` versions are **superseded, not wrong** — proved, true, and carrying a
stack the induction cannot produce. Kept until the recursion confirms nothing needs them.

**What is left for `hres`**, now that both halves and their degree bounds are in place:

1. §12's height estimate — a uniform `b` for the determinant. `abs_coeff_det_pderivList_le`
   gives `b = r!·(S·(d^L·B))^r`; §12 wants `b = 2^{2n(r₁+…+r_m)}·n!·a^n` and shows
   `b ≤ H₁^{ρ₁t/(m−1)}`. Read verbatim, not formalised.
2. `Γ_{m−1}` for the descended system — **`rothGammaFull_descend`, proved.**
3. `RothLemmaTheta` at `m−1` to turn `Θ_{m−1}` into a number — the induction itself, with
   `rothLemmaTheta_one` as its base and `rothBound_succ_of_lemma4` as its arithmetic.

So the chain is now: two proved halves, a proved descent, a proved base case, and a proved
step-arithmetic, with (1) the one genuinely unformalised link.

### ⚠⚠ Correction twenty-one — the Wronskian is built from the wrong derivative

**Read from §7 (doc pp. 85–86), verbatim.** Mahler bounds the auxiliary polynomial by a
*majorant*: `A ≪ a(1+x₁)^{r₁}…(1+x_m)^{r_m}`, differentiates it, and gets

    A_{j₁…j_m} ≪ a·binom(r₁,j₁)…binom(r_m,j_m)·(1+x₁)^{r₁−j₁}…(1+x_m)^{r_m−j_m}
    binom(r,j) ≤ Σ_j binom(r,j) = 2^r,   so   A_{j₁…j_m} ≪ 2^{r₁+…+r_m}·a·∏(1+x_h)^{r_h}
    Δ_{μν}A   ≪ 2^{r₁+…+r_m}·a·∏(1+x_h)^{r_h}
    W = Σ± Δ_{μ₁1}A…Δ_{μ_n n}A  (n! terms),  so  W ≪ n!·{2^{Σr_h}·a·∏(1+x_h)^{r_h}}^n

**The binomial with no `j!` is the tell.** For an *ordinary* derivative the coefficient of
`x^{i−j}` in `∂^j x^i` is `i!/(i−j)! = j!·binom(i,j)`; Mahler's factor is `binom(r_h,j_h)` alone.
So `A_{j₁…j_m}` — and hence `Δ_{μν}` — is the **divided (Hasse) derivative** `(1/j!)∂^j`, not
`∂^j`.

**This arc uses ordinary partials.** `mvWronskianMatrix D f i j = pderivList (D i) (f j)`, and
`pderivList` is a fold of `MvPolynomial.pderiv`. The module note defending that choice
(`MvGenWronskian.lean`) argues *characteristic*: ordinary partials are fine over number fields,
and the converse of the dependence criterion needs characteristic zero. **That is true and it is
about the wrong obligation.** The choice is free for the dependence argument and free for the
index (`index_C_mul` — scaling does not move the index). It is *not* free for the **height**,
which is the one place it bites.

**Size of the gap (my derivation, not read from the page).** For the operator-family
determinant the entry `(i,j)` is `∂^{Dx i ⊞ Dy j}P`, whose ratio to Mahler's `Δ_{μν}P` is
`(∏_h (Dx i).count h !)·(∏_k (Dy j).count k !)` — a product of a **row** factor and a **column**
factor. So

    det(arc) = (∏_i (Dx i)!)·(∏_j (Dy j)!)·det(Mahler)

— a single scalar, so the two Wronskians differ by an integer constant and the index is
unaffected. The height is not. With bounded order (`|Dx i| ≤ i`, `|Dy j| ≤ j`) the constant is up
to `(∏_{i<n} i!)²`, i.e. `2^{Θ(n² log n)}`.

**And §12's budget has no slack.** §12 spends exactly `2^{(2m+1)ρ₁}`: `2^{2n·Σr_h} ≤ 2^{2mρ₁}`
plus `n! ≤ 2^{ρ₁}`. Clause 3 is calibrated to that with **equality** at the floor —
`H₁ = 2^{(1/t)(m−1)m(2m+1)}` makes `H₁^{ρ₁t/(m(m−1))} = 2^{(2m+1)ρ₁}` exactly. An extra
`2^{Θ(n² log n)}` against a budget of `(2m+1)·n·r₁` fails once `n log₂ n` outgrows
`2(2m+1)r₁`; since `n ≤ r_m+1` and `r_m` shrinks with `t`, that needs `r₁` large, but `r₁` is
unbounded — Roth's lemma is *applied* at large degrees. So the ordinary-partial Wronskian
breaks §12's height estimate.

**This is why `abs_coeff_det_sepFamily_le` does not fit §12.** Its bound is
`n!·(S·(d^{2n}·B))^n`, carrying `d^{2n²}`; §12's is `2^{2n·Σr_h}·n!·a^n`. The `d^{2n²}` is not a
loose estimate to be sharpened — it is the factorials, and they are really there.

**The fix, and it is available.** Define the multivariate divided derivative on monomials,

    hasseList l (monomial i c) = (∏_h binom(i_h, l_h)) • monomial (i − l) c,   l_h = l.count h

prove `pderivList l = (∏_h (l.count h)!) • hasseList l`, and take the height bound on the
divided version: `binom(i_h,l_h) ≤ 2^{i_h} ≤ 2^{d_h}` gives `|coeff| ≤ 2^{Σ_h d_h}·B`, hence
`n!·(S·2^{Σd}·B)^n ≤ n!·2^{2nΣd}·B^n` using `S ≤ ∏(d_h+1) ≤ 2^{Σd_h}` — **§12's `b` exactly.**

⚠ Mathlib has `Polynomial.hasseDeriv` (univariate) and no multivariate analogue. This arc's own
inventory table lists "Hasse derivative, `MvPolynomial.pderiv` | **present**", which conflates
the two — `pderiv` is present, Hasse is not.

⚠ Note the shape: correction 21 is *not* another missing hypothesis. It is the first time this
arc has found a **construction** that is the wrong object rather than a **statement** that is too
strong. It was invisible for the same reason the others were — every theorem about
`mvGenWronskian` is true; none of them is about the height budget.

### First stone of correction 21's repair

`coeff_pderiv_iterate` and `abs_coeff_pderiv_iterate_le` in `WronskianHeight.lean`:

    coeff n (∂ⱼ^k g) = (n_j+1)(n_j+2)⋯(n_j+k) · coeff (n + k·eⱼ) g
                     = k! · binom(n_j+k, k) · coeff (n + k·eⱼ) g
    ⟹  |coeff n (∂ⱼ^k g)| ≤ k! · 2^d · B        (degreeOf j g ≤ d, |coeff · g| ≤ B)

via `Nat.ascFactorial_eq_factorial_mul_choose` and `Nat.choose_le_two_pow`. The `2^d` is §7's
`2^{r_h}`; the `k!` is the **entire** discrepancy with Mahler's divided derivative, and it is now
*visible* rather than buried inside `d^k`.

Compare `abs_coeff_pderivList_le`'s `d^k·B`. Neither dominates the other for all `k` — at `k = 1`
the crude bound `d` beats `2^d`; at `k ≈ d` the sharp one wins, `(2d/e)^d` against `d^d` — but
only the sharp form separates the factorial, and separating it is what lets the divided
derivative be recovered by dividing it out.

⚠ **Second self-duplication of the session.** The first draft re-proved `coeff_pderiv` from
scratch; the arc already had it in `MvGenWronskian.lean:253`, sixty lines of near-identical
proof. (The first was `map_pUnitAlgEquiv` = `pUnitAlgEquiv_map`.) Both type-checked. The `beans`
rule "check before you create" is stated for beans and applies verbatim to lemmas — and the
failure mode is the same one correction 17 named: nothing mechanical objects to redundancy.

**Remaining for correction 21:** lift the one-variable bound to `pderivList` (a product over the
variables, giving `∏_h (l.count h)! · 2^{Σ_h d_h} · B`), then to the determinant, where the row
and column factorials factor out of every permutation term uniformly and give
`det = C · (integral polynomial)` with `C = (∏_i (Dx i)!)(∏_j (Dy j)!)`. The quotient is the
object §12 measures, and its height bound is `n!·(S·2^{Σd}·B)^n ≤ n!·2^{2nΣd}·B^n` — §12's `b`.

### Correction 21's repair, entry level — done

`WronskianHeight.lean` now carries the whole per-entry story:

    listIdx, listFactor                  the multi-index and the integer ∂^l multiplies by
    coeff_pderivList                     coeff n (∂^l g) = listFactor l n · coeff (n + t) g
    listFactor_eq_prod                   listFactor l n = ∏_h ∏_{i<t_h} (n_h + 1 + i)
    listFactor_eq_factorial_mul          = (∏_h t_h!) · (∏_h binom(n_h+t_h, t_h))
    listFac_dvd_listFactor               ∏_h t_h!  ∣  listFactor l n
    listFactor_le                        listFactor l n ≤ (∏_h t_h!) · 2^{Σ_h d_h}
    listFac_dvd_coeff_pderivList         ∏_h t_h!  ∣  coeff n (∂^l g)
    abs_coeff_pderivList_le'             |coeff n (∂^l g)| ≤ (∏_h t_h!) · 2^{Σ_h d_h} · B

`listFactor_eq_factorial_mul` is correction 21 in one equation: the left factor is the entire
discrepancy with Mahler's divided derivative, the right is what §7 bounds by `2^{Σ r_h}`. The
divisibility says `∂^l = Fac(l)·Δ^l` **coefficientwise**, i.e. that `Δ` is integral — which is
what will let `det` be divided by `(∏_i (Dx i)!)(∏_j (Dy j)!)` and stay in `ℤ[x]`.

⚠ One thing worth recording because it looked like it would be the hard part and was not: **the
interleaving is invisible.** `listFactor` is defined by the order the list applies `∂`, but
applying `∂ⱼ` when `n` has already been shifted by `e_h` for `h ≠ j` still sees the same `n_j`,
so each variable's factors are consecutive regardless of interleaving. That is why a *list*
factor equals a *multiset* one, and why `pderiv` commutativity is never needed.

⚠ `listFactor_eq_prod` takes any `Finset s` containing the list's variables rather than requiring
`Fintype σ`. Cheaper for callers and it keeps the lemmas usable at `σ ⊕ Unit`.

**Next, and it is now bookkeeping rather than mathematics:** the determinant. Each permutation
term picks one entry per row and column, so `∏_i Fac(Dx i ⊞ Dy σ(i)) = (∏_i Fac(Dx i))·(∏_j Fac(Dy j))`
independently of `σ` — the constant factors out of the whole determinant uniformly. Divide it
out and the height bound becomes `n!·(S·2^{Σd}·B)^n ≤ n!·2^{2nΣd}·B^n`, which is §12's `b`.

### Correction 21 at the determinant: the constant divides, so Mahler's `W` is integral

    listIdx_append                  listIdx (l₁ ++ l₂) = listIdx l₁ + listIdx l₂
    listFac_mul_dvd_listFac_append  Fac(l₁)·Fac(l₂) ∣ Fac(l₁ ++ l₂)
    C_dvd_det_of_dvd_entries        C(a i · b j) ∣ M i j  ⟹  C((∏a)(∏b)) ∣ det M
    C_listFac_dvd_det_sepFamily     (∏_i Fac(Dx i))(∏_j Fac(Dy j)) ∣ det (∂^{Dx i ⊞ Dy j} P)

`C_dvd_det_of_dvd_entries` is the structural fact that makes the whole repair possible: the
discrepancy between `∂^l` and Mahler's `Δ^l` is a **row factor times a column factor**, and a
determinant is exactly the shape that turns such a thing into a single scalar — every
permutation term picks one entry per row and one per column, so `∏_i a_i·b_{σ(i)}` is `(∏a)(∏b)`
independently of `σ`.

⚠ `Fac(l₁)·Fac(l₂) ∣ Fac(l₁ ++ l₂)` needs **no disjointness** of the two lists' variables —
`m!·n! ∣ (m+n)!` per variable. Using divisibility rather than the equality that *would* need
disjointness makes the lemma cheaper and the hypothesis stack shorter. (The `x` and `y` lists
here *are* disjointly supported, so equality holds; it simply is not needed.)

So the quotient `det / C` is an integral polynomial, its index is unchanged (`index_C_mul`), and
its height is smaller by the `2^{Θ(n² log n)}` correction 21 identified. **That quotient is
Mahler's `W`.**

**What is left of correction 21:** the height bound on the quotient. `abs_coeff_det_le` assumes a
*uniform* per-entry bound and gives `n!·(S·B)^n`; here the per-entry bound is `a_i·b_j·2^{Σd}·B`,
and the product over a permutation is `C·(2^{Σd}B)^n` — so a variant of `abs_coeff_det_le` taking
factorised per-entry bounds gives `n!·S^{n−1}·C·(2^{Σd}B)^n`, and dividing by `C` leaves
`n!·S^{n−1}·(2^{Σd}B)^n`, which is §12's `b`. One lemma, and it is the same expansion
`abs_coeff_det_le` already does.

### Correction 21's repair — both sides of the determinant now match

    abs_coeff_prod_le'   |coeff n (∏ Fᵢ)| ≤ S^{#s}·∏ βᵢ           per-factor bounds
    abs_coeff_det_le'    |coeff n (det M)| ≤ (#ι)!·S^{#ι}·(∏aᵢ)(∏bⱼ)   when |coeff (M i j)| ≤ aᵢbⱼ

The size mirror of `C_dvd_det_of_dvd_entries`, and true for the same reason: a permutation term
picks one entry per row and one per column, so `∏_i a_{p i}·b_i` is `(∏a)(∏b)` independently of
`p`. **Together the two say a determinant whose entries carry a factorised row/column constant is
*that constant* times something both integral and small** — which is exactly the relationship
between this arc's `mvGenWronskian` and Mahler's `W`.

⚠ `abs_coeff_prod_le'` needs **no `1 ≤ S`**, unlike the uniform `abs_coeff_prod_le`: the empty
product is `1` and the bound is `S^0·1 = 1`, so nothing forces `S` up. A first draft carried
`1 ≤ S`, copied from the uniform version's signature without checking whether the general proof
uses it. The linter caught it. **Sixth unused hypothesis this arc has acquired by transcribing a
proof *route* rather than the proof** — and the only one of this arc's recurring failure modes
that a mechanical check reliably catches.

**Correction 21's repair is now structurally complete.** Instantiating `a i = Fac(Dx i)`,
`b j = Fac(Dy j)`, `S ≥ #supp`, and the entry bound `Fac(Dx i)·Fac(Dy j)·2^{Σd}·B` from
`abs_coeff_pderivList_le'` gives

    |coeff n (det)| ≤ n!·S^n·C·(2^{Σd}B)^n,    C ∣ det

so the quotient `det/C` — Mahler's `W` — is integral with `|coeff| ≤ n!·S^n·(2^{Σd}B)^n`. With
`S ≤ ∏(d_h+1) ≤ 2^{Σd}` that is `n!·2^{2nΣd}·B^n`: **§12's `b`, exactly.**

What is left is assembly: instantiate the two lemmas at the separated family, define the
quotient, and carry it into `abs_coeff_det_sepFamily_le`'s place in the chain. No new
mathematics — but the arc has mis-predicted "no new mathematics" four times, so that is a
prediction, not a result.

### ✅ Correction 21's repair is complete — §12's `b` is proved

`exists_divided_wronskian`:

    det (∂^{Dx i ⊞ Dy j} P) = C·W,   W integral,
    |coeff n W| ≤ r! · S^r · (2^{Σ_h d_h}·B)^r

With `S ≤ ∏_h (d_h+1) ≤ 2^{Σ_h d_h}` that is `r!·2^{2r·Σ_h d_h}·B^r` — **§12's
`b = 2^{2n(r₁+…+r_m)}·n!·a^n`, exactly.** `W` *is* Mahler's `W`: the same determinant built from
divided derivatives. Its index is the determinant's (`index_C_mul`), so nothing the index
calculus proves is lost, and its height is smaller by the `C ≈ 2^{Θ(r² log r)}` that §12's budget
has no room for.

The last piece was `listFac_append_map` — `Fac` splits across the `x`/`y` join as an **equality**,
because the two lists live in disjoint variables. `listFac_mul_dvd_listFac_append` gave only
divisibility and needed no disjointness; the divisibility side of the argument was happy with
that, the *size* side needs the equality, and the separated family supplies it. Two lemmas for
what looked like one because the two directions genuinely need different inputs.

**The full chain, all `#print axioms`-clean:**

    coeff_pderiv_iterate, coeff_pderivList        exact coefficient formulas
    listFactor_eq_factorial_mul                   ∂^l = Fac(l)·Δ^l, in one equation
    listFac_dvd_coeff_pderivList                  Δ^l is integral
    abs_coeff_pderivList_le'                      |coeff (∂^l g)| ≤ Fac(l)·2^{Σd}·B
    C_dvd_det_of_dvd_entries + abs_coeff_det_le'  row×column constants survive a determinant
    C_listFac_dvd_det_sepFamily                   C ∣ det
    exists_divided_wronskian                      det = C·W with §12's bound on W

**What this unblocks.** `hres`'s remaining input was "a uniform `B` and `E` from §12's estimate".
The `B` is now proved. What is left for `hres` is the `E` — the arithmetic
`b ≤ 2^{(2m+1)ρ₁}·a^n ≤ H₁^{ρ₁t/(m−1)}`, which is `height_descend_pq` plus the clause-3
calibration this arc already has (`rothGammaFull_descend` carries exactly that shape,
`hb : b ≤ 2^c * a^r` with `hc : c ≤ (2n+3)·(r·d₁)`).

So the pieces of the induction step are: this theorem for `b`, `rothGammaFull_descend` for
`Γ_{m−1}`, `index_rescaled_wronskian_le_theta` / `..._right_theta` for the two halves,
`rothLemmaTheta_one` for the base, `rothBound_succ_of_lemma4` for the arithmetic. **Every one is
proved.** What is not written is the recursion that composes them.

### Correction 22 — `RothLemma4` checked against 20, and it was defective

Correction twenty's *first* half (`K₁ ≥ 2`) is fixed for free by `RothGammaFull`'s new `two_le`.
The second half is not, and it bites at `n = 0` — arity `1`, where §13's Lemma 4 does not apply
at all (it assumes `m ≥ 2`), but where the `def`'s `Fin (n+1)` admits it.

At `n = 0` the sub-problem lives on `Fin 0`, where `idxWeight` sums over an empty support, so
every index is `0` and `IsRothTheta b ρ H' Θ'` forces `Θ' = 0` (and `b ≥ 1`, else `R(b;ρ)` is
empty and attainment fails). Then `w = Θ' + t = t` or `w² = t`. With `q = 0`, Lean's `ℚ` makes
`t = p/0 = 0`, so `w = 0` and the conclusion demands `Θ ≤ 0`. But

    σ = Unit, n = 0, p = 1, q = 0, F = 0, a = 100, r ≡ 1, H ≡ 2

satisfies every clause — growth vacuous, height `2 ≤ 2`, floorExp `0 ≤ 0`, floor `2⁰ = 1 ≤ 2`,
heightBound `100⁰ = 1 ≤ 2¹`, two_le `2 ≤ 2`, degPos `1 ≠ 0` — while `Θ = 1`, attained at
`A = 2x − 1`, `κ = 1/2` (height `max(1,2) = 2`), whose translate is `2x`.

Fixed the same way: carry §14's `0 < t ≤ 1`. With `q ≥ p ≥ 1` the `n = 0` case then asks only
`Θ ≤ 3t`, which `rothLemmaTheta_one`'s `Θ ≤ t` supplies.

### ⚠⚠ Correction 23 — `rothConstant_chain` / `rothBound_chain` were vacuous

`hsq` read `∀ n, sq (n+1)^2 = sq n` — for **every** `n`. Iterating, `sq 1 = sq(k+1)^{2^k}` for
every `k`, so `sq 1` is a `2^k`-th power **in `ℚ`** for every `k`. With `sq 1 = a/b` in lowest
terms, `a` and `b` are then `2^k`-th powers for every `k`, so every prime exponent in them is
divisible by every `2^k` and hence zero: `sq 1 = 1` (or `0`, forcing `sq ≡ 0` and `t ≤ 0`).

At `sq 1 = 1` the whole sequence is `1` and the conclusion is `Θ n ≤ c_n` — **no `t` in it at
all**, not §14's `Θ_m ≤ c_m·t^{2^{−(m−1)}}`. So the only instance was the constant one the
witness exhibits, and the witness's own note — "the interesting instances have `sq n = s^{2^{m−n}}`"
— describes a sequence undefined for `n > m`, which therefore never satisfied `hsq`.

**Fixed** by bounding the ranges to `n < M`: only `M` successive square roots are needed, so
`sq 1 = t` may be any `2^{M−1}`-th power of a rational.

⚠ The arithmetic above is elementary but **not formalised**. A Lean witness needs irrationality
of `√2` (`Mathlib.Data.Real.Irrational`), whose `.olean` is not in this project's built Mathlib
closure — importing it means compiling that module. Recorded as an argument, not a theorem.

⚠ The perfect-power restriction is an artifact of the **root-free rational encoding**, not of
§14: over `ℝ` every `t ≥ 0` has its roots. Removing it means proving the step in `ℝ` and
transferring back — the inequalities are all field-generic, so it should go through, but it is
not done.

### §14's recursion, one step — proved

`rothLemmaTheta_succ`: `RothLemma4` at arity `n+1` plus `RothLemmaTheta` at `n` gives
`RothLemmaTheta` at `n+1`. Four lines — Lemma 4 hands over a sub-problem with `Γ_n` and its `Θ'`,
the induction hypothesis turns that into a `RothBound`, and `rothBound_succ_of_lemma4` does §14's
arithmetic.

`s` appears as an explicit hypothesis so correction 23's restriction is **visible at every use**
rather than buried. Iterating from `1` to `m` needs such an `s` at every level, i.e. `t` a
`2^{m−1}`-th power in `ℚ`.

**With `rothLemmaTheta_one` as base, the §14 induction is now complete modulo `RothLemma4`
itself** — which is §13, and is the last unproved link.

### §14's recursion, iterated — `rothLemmaTheta_iterate`

`RothLemma4` at every arity from `1` to `M−1`, plus the base case, gives `RothLemmaTheta` at
every `m ≤ M`. The square-root sequence `s` with `s 0 = t` and `s(n+1)² = s n` supplies the `s`
each `rothLemmaTheta_succ` needs, via `s n ^ {2^n} = t`.

**⚠ I reproduced correction 23's own defect, one commit after fixing it.** The first draft of
`rothLemmaTheta_iterate` left `hsq` unbounded — `∀ n, s (n+1)^2 = s n` — which is exactly the
vacuous form I had just removed from `rothConstant_chain`. Nothing objected: it type-checks, the
theorem is true, and the hypothesis is simply unsatisfiable for any non-constant `s`.

That says something about the failure mode worth keeping: **the unbounded form is what one writes
by default.** It reads more natural, it is what the mathematics "means", and only asking *is this
hypothesis satisfiable?* exposes it. The arc's five missing-clause corrections are the mirror
image — there the default was to write too few hypotheses; here it was to write one too strong to
hold.

Then the bound was still one too loose. Reaching arity `M` needs `M − 1` successive roots, not
`M`: the last step is `M−1 → M` and needs `s_{M−1}` with `t = s_{M−1}^{2^{M−1}}`. Corrected to
`∀ n, n + 1 < M → …`, and only then does a witness exist —
`rothLemmaTheta_iterate_seq_witness` at `M = 3`, `t = 1/16 = (1/2)^{2²}`, sequence
`1/16, 1/4, 1/2`. **One more root would need `√(1/2)`.** The witness sits exactly at the
boundary, which is the concrete shape of correction 23's restriction.

**⚠ `hbase` is a hypothesis, and that is a real gap.** `rothLemmaTheta_one` proves
`RothLemmaTheta Unit 1 p q F`; the iteration needs it at `Fin 1`. Those are different
propositions — the schema quantifies over `σ → ℕ` data and `MvPolynomial σ ℤ` — and transporting
needs `index`, `InRothPolySet` and `InRothFracSet` carried along `MvPolynomial.rename` for a type
equivalence, which this arc does not have. Stated as a hypothesis so the gap is visible at the
use site rather than hidden. The `m = 1` chain is `Unit`-specific throughout (`pUnitAlgEquiv`),
so the fix is a `rename` transport for `index`, or a `Fin 1` copy of the base case.

**Where Roth's lemma now stands.** §14's induction is complete — base (`rothLemmaTheta_one`),
step (`rothLemmaTheta_succ`), iteration (`rothLemmaTheta_iterate`) — modulo two things:
`RothLemma4` itself, which is §13 and the last piece of real mathematics; and the `Fin 1`/`Unit`
transport, which is bookkeeping.

### ✅ The transport gap is closed — `rothLemmaTheta_iterate` is now unconditional

    InRothPolySet.rename_equiv   degrees via degreeOf_rename_of_injective,
                                 coefficients via coeff_rename_mapDomain
    InRothFracSet.rename_equiv   pointwise
    IsRothTheta.rename_equiv     both clauses, via index_rename_equiv
    RothGammaFull.rename_equiv   every clause is stated through o.symm j, so the
                                 equivalence composes into the ordering
    RothLemmaTheta.rename_equiv  the schema
    rothLemmaTheta_one_fin       the base case at Fin 1, via finOneEquiv

`rothLemmaTheta_iterate` no longer takes `hbase`; it uses `rothLemmaTheta_one_fin` directly.

⚠ Worth recording that carrying the gap as an explicit hypothesis for one turn was the right
call, and that "the variable type is incidental" — true — still cost **four** transport lemmas.
`RothIndex`'s own docstring had predicted the shape correctly: *"The height side is free —
Mathlib's `coeff_rename_mapDomain` already matches coefficients across a renaming."* It was.

### Where Roth's lemma stands

**§14's induction is complete and unconditional except for `RothLemma4`:**

    rothLemmaTheta_one / _one_fin   Θ₁ ≤ t, at Unit and at Fin 1
    rothLemmaTheta_succ             Lemma4 at n+1  +  Theta at n  ⟹  Theta at n+1
    rothLemmaTheta_iterate          Lemma4 at 1..M−1              ⟹  Theta at every m ≤ M

**Everything the induction step consumes is proved:**

    exists_divided_wronskian          §12's b (correction 21's repair, end to end)
    rothGammaFull_descend             Γ_{m−1} for the descended system
    index_rescaled_wronskian_le_theta the x half of hres, from the induction hypothesis
    ..._right_theta                   the y half, from the base case
    rothBound_succ_of_lemma4          §14's arithmetic
    exists_sepW_ne_zero_le_degreeOf   the separated representation, now with degree bounds

**What is left is `RothLemma4` — §13 — and nothing else.** It is not a gap in the scaffolding; it
is the remaining chapter of mathematics: the recursive inequality
`Θ_m ≤ Ψ_m + 2·max(Ψ_m/n, √(Ψ_m/r_m))` and the construction of the descended system that
realises it.

⚠ And correction 23's encoding restriction stands: `rothLemmaTheta_iterate` needs `t` to be a
`2^{M−1}`-th power in `ℚ`. That is an artifact of the root-free encoding, not of §14 — removing
it means proving `rothBound_succ_of_lemma4` in `ℝ` and transferring back.

### §13 read in full (doc pp. 93–95) — the argument, verbatim

**The per-entry index bound.** `Δ_{μν}A = A_{j_{μ1}…j_{μ,m−1} j_{νm}}`, so property (C) gives

    J(Δ_{μν}A) ≥ max(0, J(A) − Σ_{h<m} j_{μh}/r_h − j_{νm}/r_m)

and then, using `r₁ ≥ r₂ ≥ … ≥ r_m` and `μ−1 ≤ n−1 ≤ r_m ≤ t·r_{m−1}`,

    ≥ max(0, J(A) − (1/r_{m−1})Σ_{h<m} j_{μh} − j_{νm}/r_m)
    ≥ max(0, J(A) − (μ−1)/r_{m−1} − (ν−1)/r_m)
    ≥ max(0, J(A) − t − (ν−1)/r_m)

**Summed by properties (A) and (B):**   `J(W) ≥ Σ_{ν=1}^{n} max(0, J(A) − t − (ν−1)/r_m)`.

**The case split.** `N := ⌊{J(A)−t}·r_m⌋ + 1`, so `N−1 ≤ {J(A)−t}r_m < N`.

- `n ≤ N`: every term is non-negative, so `J(W) ≥ n{J(A)−t} − n(n−1)/(2r_m)`, giving (1).
- `n > N` (assuming `J(A) ≥ t`, so `N ≥ 1`): the terms vanish past `N`, so

      J(W) ≥ Σ_{ν=1}^{N} {J(A)−t−(ν−1)/r_m} = N{J(A)−t} − N(N−1)/(2r_m)
           ≥ N{J(A)−t} − (N/2){J(A)−t} = (N/2){J(A)−t} > (r_m/2){J(A)−t}²

  Solving for `J(A)`:

      (2):  J(A) ≤ t + √((2/r_m)·J(W)) ≤ t + 2√((1/n)·J(W))    if n > N

  the second step because `n ≤ r_m + 1` gives `r_m/2 ≥ (r_m/(r_m+1))·(n/2) ≥ n/4`.  ⚠ "In the
  case `J(A) < t` so far excluded this estimate is still valid."

**Both cases together:**

    J(A) ≤ t + 2·max( (1/n)J(W),  √((1/n)J(W)) )

and since `J(W) ≤ n·Φ_m` (§12),

    J(A) ≤ t + 2·max(Φ_m, √Φ_m),      Φ_m = Θ_{m−1}(b;ρ;H) + Θ₁(b;ρ_m;H_m)

with `A` chosen so that `J(A) = Θ_m(a; r; H)`.  **That is Lemma 4.**

⚠ This confirms correction 15 from the source's own page: display (2) really does carry *both*
`√((2/r_m)J(W))` and `2√((1/n)J(W))`, joined by `n ≤ r_m + 1`.

### ⚠ An open question about the arc's §13, deliberately not answered

**§13's leading term is `t`, once.**  `index_le_of_rothGrowth_of_factor_bound` /
`..._of_rescaled_bounds` conclude

    θ ≤ 2/ω + 2·max(εU + εV, q)

and with §11's `ω = 1/t` that leading term is **`2t`, not `t`**.  A factor of two there is not
free: `rothConstant_step_lemma4` consumes `θ ≤ s + 2w` and yields `c_{m+1} = 2c_m + 3`; a `2s`
leading term would need `c_{m+1} ≥ 2c_m + 4` and would move `c_m = 2^{m+1} − 3`, which correction
eleven pinned against §14.

**I have not read the arc's derivation of the `2/ω`,** only its statement — and this arc's own
history says that is exactly when to stop. Correction 14 was made by reading one display without
the derivation; correction 17 by reading a label without the theorem. The `2/ω` may be genuine
slack, or the arc's `ω` may not be `1/t` at that point, or `hθt : 2/ω ≤ θ` may be doing something
I am misreading.

**Resolving it is the first thing the next attempt at §13 should do**, before any assembly is
built on top of `index_le_of_rothGrowth_of_rescaled_bounds`.

### What `RothLemma4` still needs

Its arithmetic core exists (`RothRecursionArith`'s `sq_le_two_mul_max_of_sum_le` and friends are
exactly the two-case analysis above), and `index_le_of_rothGrowth_of_rescaled_bounds` is §13's
conclusion given `hres` — which the two `Θ`-form halves now supply. What is missing:

1. the `2t` / `t` question above;
2. the assembly: split `σ ≃ Fin (n+1)` into `σ' ⊕ Unit`, take `IsRothTheta`'s realising pair,
   feed it through, and package the descended system (`rothGammaFull_descend` + `exists_isRothTheta`)
   into `RothLemma4`'s existential.

(2) is plumbing of a size this arc has done before; (1) is not plumbing.

## Correction 24 — the `2t` was the arc's, not the source's

The question above is **answered, and the answer is that the arc was wrong**. The `2` was pure
slack, introduced in two places, neither of them in Mahler:

1. **`cost_sepW_le`** bounded `(Dx i).length ≤ (i : ℕ)` by `r`, via `le_of_lt i.isLt`. But
   `i : Fin r` gives `i ≤ r - 1`. One unit, thrown away for nothing.
2. **`exists_degree_floor`** then had to carry the numerator `d + 1` (from `r ≤ d + 1`) and
   bounded `(d+1)/⌈ωd⌉ ≤ 2/ω` — the factor `2` being `1 + 1/d ≤ 2`, the crude estimate at
   `d = 1`, in a regime where `d` is large.

§13's row term is `Σ_{h<m} j_{μh}/r_h ≤ (μ-1)/r_{m-1}`, numerator **`μ - 1`**. With `μ ≤ n` and
`n ≤ r_m + 1` that is `≤ r_m/r_{m-1} ≤ t`. The `+1` in `n ≤ r_m + 1` cancels against the `-1` in
`μ - 1`; the arc kept the first and dropped the second, and paid a factor of two for it.

Fixed: `cost_sepW_le`'s numerator is `r - 1`; `exists_degree_floor` concludes `dl/D₁ ≤ 1/ω`;
`exists_index_le_of_separated_le_degreeOf`'s row cost is `d/D₁`; and

    exists_index_le_of_rothGrowth
    index_le_of_rothGrowth_of_factor_bound
    index_le_of_rothGrowth_of_rescaled_bounds
    index_le_of_rothGrowth_split          (RothVariableSplit)

all now read `θ ≤ 1/ω + 2·max(…)`, i.e. **`t` under `ω = 1/t`** — §13's own leading term.
`rothGrowth_row_cost_le` likewise. All seven `#print axioms` clean; every module rebuilt with
the `.olean` deleted.

`rothConstant_step_lemma4`'s `θ ≤ s + 2w ⟹ c_{m+1} = 2c_m + 3` is therefore **fed the shape it
was written for**, and `rothConstant m = 2^{m+1} - 3` stands as correction 11 pinned it.

### What found it, and what did not

Not a build, not `#print axioms`, not a witness — every one of these statements was *true* at
`2/ω`, just weaker than needed, and a weaker true theorem is invisible to all three. What found
it was reading §13 line by line and **comparing its row term against the arc's, symbol by
symbol**. The `2` had survived eleven commits, one docstring that reasoned *from* it (and drew a
false conclusion, retracted separately), and correction 17's own re-read of the same file.

⚠ The retraction is worth its own note. A previous pass had already caught that
`exists_index_le_of_rothGrowth`'s docstring drew a bad conclusion from the `2/ω` ("so `ω ≥ 2/ε`
is what `ω(m, ε)` has to be") and rewrote the paragraph — correctly — while leaving the `2`
itself unexamined. **Correcting an inference from a premise is not checking the premise.**

## Correction 25 — `RothLemma4`'s `w` demanded a rational square root

`RothLemma4` encoded `max(Ψ, √Ψ)` root-free as

    (w = Θ' + t  ∨  w² = Θ' + t) ∧ Θ ≤ t + 2w.

The admissible `w` under that are `Ψ` and — **only when `Ψ` is a square in `ℚ`** — `±√Ψ`. So
whenever the `√` branch is the operative one, which is exactly the regime §14 runs in (`Ψ < 1`,
so `√Ψ > Ψ`), the `def` demands a rational square root of `Θ' + t`. Nothing produces one:
`Θ'` is an infimum over a finite set of indices and `t = p/q`.

With `≤` the admissible `w` are exactly `w ≤ max(Ψ, √Ψ)`, so the existential says **precisely**
`Θ ≤ t + 2·max(Ψ, √Ψ)` — the `≤` form is the faithful encoding and the `=` form was an
over-strengthening.

`lemma4_le_encoding_needed` (proved) makes it concrete at `Ψ = 1/2`, `t = 0`, `Θ = 7/5`:

* §13's second branch `(Θ − t)² ≤ 4Ψ` holds — `49/25 ≤ 2` — so this is a situation §13
  genuinely produces, the literal shape `index_le_or_sq_of_det_bound` returns;
* no rational `w` satisfies the `=` form (first disjunct gives `1 < 7/5`; second needs
  `w² = 1/2`, refuted by `not_isSquare_half` — elementary, `(w²).den = w.den²` and
  `(1/2).den = 2`, no irrationality import);
* `w = 7/10` satisfies the `≤` form, with `Θ = t + 2w` exactly.

Relaxed: `rothConstant_step_lemma4`, `rothConstant_step_perturbed`, `rothConstant_chain`,
`rothBound_chain`, `radicand_weaken` (`S/n ≤ w²`, with `0 ≤ S` now assumed rather than derived
from the equality), `rothBound_succ_of_lemma4`, and the `RothLemma4` def itself. All rebuilt
with the `.olean` deleted; all `#print axioms` clean.

### The consumers never wanted the equality

`rothConstant_step_lemma4` used `rw [h]` in both branches, and in both the rewrite was in the
`≤` direction only; `radicand_weaken` used `S/n = w²` only as `S/n ≤ w²`. So every theorem that
consumed the disjunction got **stronger** here (weaker hypothesis) and the only thing that
changed on the other side is that `RothLemma4` is now provable in principle.

⚠ Same shape as correction 9 and correction 10: **a hypothesis nobody has had to discharge is
indistinguishable from an unsatisfiable one.** Four instances now. The pattern is specific
enough to act on: whenever this arc writes a `def` or hypothesis that some *later* step must
produce, the production is the test, and until it is written the statement is untested no
matter how many theorems consume it. `rothBound_succ_of_lemma4_witness` consumed the `=` form
happily for eleven commits — because its `Ψ = 1/8` … no: because it took the *first* disjunct,
where the equality costs nothing.

## Correction 26 — correction 21 was never propagated to its consumers

Correction 21 established that §12's budget covers the **divided** Wronskian `W`, not the
determinant: `det = C c · W` with `c = ∏_i ∏_h (listIdx …)!` of size `2^{Θ(r² log r)}`, and
§11's clause `b ≤ 2^{c'}·a^r` has no room for that factor. `WronskianHeight`'s
`exists_divided_wronskian` proves exactly that, and it is the arc's only height bound on the
Wronskian.

But the two `Θ`-form halves of `hres` — `index_rescaled_wronskian_le_theta` and
`..._right_theta` — take `hB` as a bound on the **determinant**'s coefficients, because they
were written against `exists_integral_wronskian_factors`, which factors `det`.

**So the arc's only available height bound and the arc's only usable induction-hypothesis
halves do not compose.** Both are true; both are green; both have witnesses. Nothing in the
project objected, because nothing had ever put them next to each other.

Fixed with `exists_integral_wronskian_factors_div` (`SeparatedGauss`) and the two `_div` halves
(`RothInductionHypothesis`). The work is small — `exists_integral_separated_factorization` was
already stated for an arbitrary integral `W` whose map is a separated product, and

    map W = C c⁻¹ · (renₗ Wx · renᵣ Wy) = renₗ Wx · renᵣ (C c⁻¹ · Wy)

is that shape, with the constant parked on the `y` side so the `x` half keeps its exact
`C l · Wx`. The `y` half's constant is `l⁻¹·c⁻¹ ≠ 0`, and `index_C_mul` is indifferent.

The originals are kept — they are true, and a caller holding a determinant bound can use them.
What they cannot be is the induction's `hres`.

### What found it

Not a build, not `#print axioms`, not a witness. **Writing the assembly and discovering that
`hB`'s `b` had to be two different numbers at once.** That is the third distinct time in this
arc that the composition — not the components — was the test, and it is the strongest argument
for pushing the assembly through even where the pieces all look finished: an unexercised
interface between two green theorems is exactly as untested as an undischarged hypothesis.

⚠ Note the shape of the failure. Correction 21 was **correct and complete in the module where
it landed.** The defect is that a correction to a lemma is not a correction to its consumers,
and the arc had no mechanism that would notice. A green build after a correction says the
corrected file still compiles, not that anything downstream now means what it did before.

## Lemma 4 is proved, and §14 runs

`rothLemma4_of_one_le : 1 ≤ n → RothLemma4 σ n p q F` — no `sorry`, standard axioms, no
hypothesis beyond `0 < p ≤ q`, `1 ≤ n` and `Γ_{n+1}` itself.

The assembly, in the order it uses things:

* `IsRothTheta`'s **attainment** clause gives the realising pair `(A, κ)` — which is why §9's
  finiteness had to be *proved*; an inequality-only `Θ` would have had nothing to hand over;
* `exists_family_index_le_w_of_rothGrowth_split` runs §13 on `map A` and returns the separated
  representation, fixing the length `rr` — the whole reason the family had to be exposed;
* `exists_divided_wronskian_budget` bounds the divided Wronskian at that `rr` in §11's currency;
* `rothGammaFull_descend` turns `Γ_{n+1}` into `Γ_n`;
* `exists_isRothTheta` names `Θ'` and `Θ₁`; `isRothTheta_right_le_t` gives `Θ₁ ≤ t`;
* the two `_div` halves (correction 26) bound the Wronskians; `factor_bound_of_rescaled` turns
  that into §13's `J(W) ≤ n·Φ`;
* §13 returns `w` with `Φ = Θ' + Θ₁ ≤ Θ' + t = Ψ`.

Then `rothLemmaTheta_of_seq` discharges `rothLemmaTheta_iterate`'s `h4` at every arity, and
`rothLemmaTheta_three` is **Roth's Lemma with no hypothesis at all** beyond `m ≤ 3`: at
`t = 1/16 = (1/2)^{2²}` the ladder `1/16, 1/4, 1/2` lives in `ℚ`.

### Three things the assembly needed that no component knew about

1. **`Θ ≤ t` is a separate case.** §13's inequality needs `t ≤ θ` — there is nothing to bound
   otherwise — and the assembly cannot discharge it. It does not need to: at `Θ ≤ t` the
   conclusion holds with `w := 0`. ⚠ That branch is **unavailable** under correction 25's old
   `=` encoding, which admits `w = 0` only when `Ψ = 0`. So correction 25 was not merely
   tidying: without it this case has no witness either.
2. **`1 ≤ a`** is nowhere in `RothGammaFull`; it comes from `InRothPolySet`'s non-vanishing.
   Three lemmas wanted it and none of them could have stated it.
3. **`Fintype σ`** — `exists_divided_wronskian_budget` sums over the variables, and `σ` is
   finite only *because* `o : σ ≃ Fin (n+1)` exists. It is derived inside the proof, not
   assumed.

### What is still open

Correction 23's encoding restriction, unchanged: `rothLemmaTheta_of_seq` needs `t` to be a
`2^{M−1}`-th power in `ℚ`. Removing it means proving `rothBound_succ_of_lemma4` in `ℝ` and
transferring back; the inequalities are field-generic, so this is transport work, not
mathematics. `rothLemmaTheta_three` is an instance where the restriction is satisfied.

⚠ The stale-prose paragraph in `RothVariableSplit` has now been wrong **three times** in three
directions: "neither is proved" (correction 17), "`RothLemma4` is not proved at any arity", and
each time the build had no opinion. A docstring naming what is open is a claim about the whole
file and ages the moment anything below it lands.

## Correction 23 is closed — Roth's Lemma at every arity, no hypotheses

`rothLemmaTheta_all : ∀ m, 1 ≤ m → RothLemmaTheta (Fin m) m p q F`, for every `p q F`. And
`index_le_rothBound`, which says what that means on the index: under `Γ_m` with `t = p/q`, every
`A ∈ R(a;r)` has index at most `c_m·t^{2^{−(m−1)}}` at every `κ ∈ Q(H)`, with
`c_m = 2^{m+1} − 3`.

### Why the ladder could not simply be dropped

Correction 23 called the perfect-power restriction "an artifact of the root-free encoding".
That was right, but it understated the situation: **a root-free reformulation of the argument
does not exist at this constant.** Running §14's step on powers directly needs
`(a+b)^K ≤ 2^{K−1}(a^K + b^K)`, which turns `Θ ≤ 2Θ_n + 3t` into

    Θ^K ≤ 2^{K−1}(2^K·c_n^K + 3^K)·t,     K = 2^n

against a target of `(2c_n+3)^K ≈ 2^K c_n^K`. That is short by `≈ 2^{K−1}` once `c_n` is large,
and `c_n = 2^{n+1}−3` is large. The root is not a convenience; it is what stops the constant
compounding. I checked this before reaching for `ℝ`, and it is the reason the answer is `ℝ` and
not a cleverer `ℚ` argument.

### The fix

* `rothConstant_step_lemma4` was **already field-generic** — its proof is `nlinarith` and
  `le_of_pow_le_pow_left₀`. Generalising it from `ℚ` to
  `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` cost one edit and broke no caller.
* `Real.sqrt^[n]` supplies the `2^n`-th root (`sqrtIter_pow`, `_nonneg`, `_le_one`).
  `Real.rpow` would be one line but is not in this project's built Mathlib closure;
  `Mathlib.RingTheory.Real.Irrational` is, and carries `Real.sqrt`.
* `rothBound_succ_of_lemma4'` runs the step in `ℝ` at `u = t^{2^{−n}}` and casts back. Both
  endpoints are rational, so the excursion is invisible in the statement.

New module `QOU/Mathlib/RothRealLadder.lean`, registered in `QOU.lean`. All five
`#print axioms` clean.

⚠ The `ℝ`-free route is **kept**, not replaced: `rothLemmaTheta_of_seq` and
`rothLemmaTheta_three` still stand in `RothVariableSplit`, and a reader who wants Roth's Lemma
without an analysis import can have it at any `t` that is a `2^{M−1}`-th power.

## Arc status — Roth's Lemma is proved

**`MvPolynomial.index_le_rothBound`** (`QOU/Mathlib/RothRealLadder.lean`): if
`a; r₁,…,r_m; H₁,…,H_m` has property `Γ_m` with `t = p/q`, then every `A ∈ R(a;r)` has index at
most `c_m·t^{2^{−(m−1)}}` at every `κ ∈ Q(H)`, `c_m = 2^{m+1} − 3`. Every arity `m ≥ 1`, every
`p, q, F`. No `sorry`; `[propext, Classical.choice, Quot.sound]`.

Non-vacuous where it matters: `index_le_rothBound_witness` at `m = 2`, where clause 3 forces
`H ≥ 1024` — the one hypothesis every earlier witness in this arc dodged.

Twenty-six corrections. What the last six say about how the arc failed:

* **24** (`2t` vs `t`) — a weaker true theorem is invisible to a build, to `#print axioms`, and
  to every witness. Only reading the source's step symbol-by-symbol found it.
* **25** (`w² = Ψ`) — a hypothesis nobody has had to *discharge* is indistinguishable from an
  unsatisfiable one. Four instances now (9, 10, 22, 25).
* **26** (correction 21 unpropagated) — a correction to a lemma is not a correction to its
  consumers, and a green build after one says only that the corrected file still compiles.
* The **assembly itself** found 24, 25 and 26. Three separate defects that only appeared when
  two green theorems had to meet. An unexercised interface is exactly as untested as an
  undischarged hypothesis, and this arc now has three data points saying the composition is the
  experiment, not the components.
* **Correction 23's closure** needed a *negative* result first: I checked that a root-free
  reformulation loses a factor `2^{2^n}` before reaching for `ℝ`. "It's just an encoding
  artifact" was true about the restriction and false about the remedy.
* The status paragraph in `RothVariableSplit` was wrong **three times in one session**, in three
  directions. Prose that names what is open is a claim about the whole file.

## Summary of Changes

**Roth's Lemma is proved and merged.** PR #5737 → `bf0b7f63ae`. Rebuilt against main
(2065 jobs, no errors, no warnings, no `sorry`). Main has since touched one line in the arc —
a correct path update, `uploads/roth_lemma.pdf` → `library/roth-lemma/roth_lemma.pdf`.

Headline: `MvPolynomial.index_le_rothBound` (`QOU/Mathlib/RothRealLadder.lean`) — under `Γ_m`
with `t = p/q`, every `A ∈ R(a;r)` has index at most `c_m·t^{2^{−(m−1)}}` at every `κ ∈ Q(H)`,
`c_m = 2^{m+1} − 3`. Every arity, every `p, q, F`, no `sorry`, standard axioms. Non-vacuous at
`m = 2` (`index_le_rothBound_witness`), where clause 3 forces `H ≥ 1024`.

Twenty-six corrections. The last three were all found by **composing** green theorems, not by
testing them: 24 (`2t` vs `t`), 25 (`w² = Ψ` demanded a rational square root), 26 (correction 21
never propagated to its consumers).

## Reassessment against main — 2026-08-29

Main moved 1993 commits. Two things in it change how this arc should be read.

### 1. The new detector suite reports the Roth corpus clean — and that is blindness

Seventeen audit scripts landed, and `docs/audits/2026-08-15-detector-blindness-taxonomy.md`
now carries a 17-row table of what each was blind to. Two of the new detectors are the exact
two axes this arc's corrections fall on:

* `limit-claim-encoding-audit.py` — *is the statement weaker than its prose* (corrections 17, 24)
* `unbounded-quantifier-audit.py` — *is the statement stronger than the truth* (corrections 20, 22, 25)

Run over the 18 Roth/Wronskian/Separated modules, both report **0 candidates**. So do
`lean-vacuous-existential-audit.py` and `lean-self-assuming-audit.py` over all 169
`QOU/Mathlib` files.

⚠ **That clean is not evidence.** I reconstructed corrections 20 and 25 in their pre-fix form
and re-ran all three: still **0**. The detectors cannot see this arc's defects, so their silence
about the Roth corpus says nothing about it. Two rows for the taxonomy:

* **The defect is an ABSENT field.** Both criteria scan `class|structure … where` and key on a
  field that is *present and wrong*. `RothGammaFull` was defective (correction 20, and 16
  before it) because it **lacked** `two_le` and `degPos`; every field it had was correct. A
  missing clause is a *weaker hypothesis*, hence a *stronger theorem* — the direction this arc
  got wrong four times — and no field-shaped matcher can see an absence.
* **The carrier is a `def : Prop`.** `RothLemma4` and `RothLemmaTheta` are `def`s, which is how
  this corpus states Mahler's Lemma 4 and Roth's Lemma. Every field-keyed scan begins at
  `class|structure … where`, so a proposition-valued `def` is outside the tree the tools walk.
  This is taxonomy row 14 one level down: not a language never scanned, a *declaration form*
  never scanned.

### 2. Roth's **Lemma** is not Roth's **Theorem** — the parent bean is not dischargeable

`qou-br3w` wants `RothExponent : ∀ α, IsAlgebraic ℚ α → Irrational α → ∀ p > 2,
¬ LiouvilleWith p α`, which discharges `roth_separates`. Roth's Lemma is one of five steps:

| step | what | state |
|---|---|---|
| 1 | auxiliary polynomial, high index at `(α,…,α)`, bounded height | **not started** — engine exists: Mathlib `NumberTheory/SiegelsLemma.lean`, `NumberField/House.lean` |
| 2 | index at the rational point is **large** (Taylor + good approximations) | partial — `RothHeightBound`'s `max_abs_pow_le_of_abs_coeff_le` is the one-variable case |
| 3 | index at the rational point is **small** — Roth's Lemma | **DONE** (this bean) |
| 4 | contradiction: parameter bookkeeping (`m`, `r_h`, `δ`) | not started |
| 5 | `¬ LiouvilleWith p α` from "no `κ > 2` works" | not started |

### 3. The highest-risk remaining item: `Γ_m` has never been produced

`RothGammaFull` is *constructed* in exactly three places, and none of them is a production:
`rename_equiv` (transport), `rothGammaFull_descend` (takes a `Γ_{n+1}`), and two hand-built
structure literals at `m = 2`. So its seven clauses have **never been discharged from an actual
Diophantine setup at any `m ≥ 3`**.

That is correction 9's lesson at arc scale — *a hypothesis nobody has had to discharge is
indistinguishable from a false one* — and this arc has now hit that failure four times
(9, 10, 22, 25), each time in a hypothesis that looked settled. Step 1 above is what would
discharge `Γ_m` for real, and it is therefore both the next piece of work **and** the real test
of whether `Γ_m` is stated correctly. If `Γ_m` is wrong, everything in this bean is a true
theorem about the wrong hypothesis — which is exactly what correction 18 was.

**Recommendation: do step 1 next, and treat it as an audit of `Γ_m` rather than as construction
work.** Not because it is the easiest remaining piece — it is not — but because it is the only
one that can invalidate what is already done.
