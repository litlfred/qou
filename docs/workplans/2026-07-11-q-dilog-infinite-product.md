# Workplan — genuine infinite quantum dilogarithm Φ_q (analytic layer)

**Branch:** `claude/q-dilog-infinite-product-2026-07-11`
**Depends on:** the merged finite backbone `QOU.MathlibExt.QuantumDilogarithm`
(PR #3500 — `qPochProd`, `qPochProd_add` cocycle, `qPochProd_functional`).

## Goal (as requested)

Formalize the *genuine* compact quantum dilogarithm — the infinite object of
which the merged finite product is the truncation:

$$\Phi_q(x) \;=\; \Bigl(\prod_{n=0}^{\infty}\bigl(1 + q^{2n+1}x\bigr)\Bigr)^{-1},$$

and its functional equation `Φ_q(q²x) = (1 + qx)·Φ_q(x)`.

## The subtlety that forks the target (read first)

The `x^k` coefficient of the finite product `P_N(q,x)` is the elementary
symmetric polynomial

$$[x^k]\,P_N \;=\; e_k\bigl(q, q^3, q^5, \dots, q^{2N-1}\bigr).$$

As `N → ∞` this is `e_k(q, q³, q⁵, …)`, a **geometric-type series in `q`**.

- Its lowest term is `q^{1+3+···+(2k-1)} = q^{k²}`, and **each power of `q`
  appears with finite multiplicity** (partitions of `m` into `k` distinct odd
  parts). ⇒ It is a well-defined **formal** power series in `q`.
- But as an **analytic** function it converges iff `|q| < 1`.

**The physical substrate anchor is `q₀ ≈ 1.10998 > 1`.** So the naive infinite
product *diverges analytically at the physical point* — the Faddeev/compact
quantum dilogarithm at `|q| ≥ 1` is defined by a contour integral / modular
double, **not** by this product. This means "the infinite product" is not one
target but three:

| # | Target ring / regime | Product status | Mathlib support | Effort |
|---|----------------------|----------------|-----------------|--------|
| **T1** | **Bi-formal `R[[q]][[x]]`** (formal in *both* `q` and `x`) | **well-defined** — each `[x^k]` is a legit formal `q`-series (`q^{k²}` + finite mult.) | `MvPowerSeries`; infinite-product/summability machinery is thin — likely custom `HasProd`-in-`x`-adic-then-`q`-adic argument | medium–high |
| **T2** | **Analytic `|q| < 1`** over `ℝ`/`ℂ` — the classical `q`-Pochhammer `(x;q)_∞` | convergent | `Multipliable`/`tprod` in a Banach algebra; some `q`-series in Mathlib | medium; **but excludes the physical q₀ > 1** |
| **T3** | **Faddeev integral / `\|q\|=1` modular double** — the object physics actually uses at `q₀` | product form invalid; needs the contour-integral definition | essentially none in Mathlib | very high (research-grade) |

Prerequisite for **all three**: `Mathlib.RingTheory.PowerSeries.{Basic,Inverse}`
(and `MvPowerSeries` for T1) oleans — **not in the current sandbox cache**; a
Mathlib source clone + from-source build of that cone is needed first.

## Recommendation

**T1 (bi-formal `R[[q]][[x]]`).** It is the honest home that matches the file's
stated "formal power series" scope, is fully rigorous with **no analytic
convergence**, contains the finite backbone as literal truncations, and its
functional equation is a clean corollary of `qPochProd_functional` in the
limit. T2 is cleaner in Mathlib but formalizes an object that **excludes the
physical anchor**, so it cannot connect to the consumers. T3 is the physically
correct object at `q₀` but is a multi-session research formalization.

## Plan (once target chosen)

1. Build the `PowerSeries`/`MvPowerSeries` oleans (Mathlib source clone +
   from-source build; seed the `lake-cache` branch afterward).
2. Scaffold the chosen infinite object + its `x^k`-coefficient formula.
3. Prove the limiting functional equation from `qPochProd_functional`.
4. Wire `QuantumDilogarithm.lean`'s "Infinite limit — deferred" note to the
   new theorems.
