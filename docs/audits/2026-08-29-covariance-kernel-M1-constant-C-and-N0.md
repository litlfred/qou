# Covariance-kernel epic (`qou-x631`) — M₁>0: pinning the constant `C` and `N₀` — landscape + honest verdict

**Date:** 2026-08-29 · **Branch:** `claude/m1-constant-C-N0-2026-08-29` · **Tier:** feasibility
measurement + rigorous reduction of `C` to explicit literature constants; **honest negative on a
*verified* number this session** · **Discipline:** no fit; nothing wired; no `c_k`; L2 unchanged.
**Epic:** `qou-x631`; gap `qou-k5r5`.

## What "pin `C`, verify `N₀ ≤ 78`" actually requires

The rigorous finite-n bound (PR #5929) is `|m(n) − m_∞| ≤ C·n^{−1/2}`, `m_∞ = 0.300186614` (merged
#5901 IO value), `m(n) = ρ_P(n) − σ_D(n)/σ_A(n)` the (CS) margin. Closing `M₁>0` for all n needs the
tail `n > 78` (the finite part is **already rigorous**: exact `Fraction` gives `M₁>0` for **n≤78**,
Track B, no rounding). So the whole remaining gap is:

> an **explicit `C`** with `N₀ := ⌈(C/m_∞)²⌉ ≤ 79`, i.e. **`C ≤ m_∞·√79 = 2.668`**, and the asymptotic
> valid from `n ≤ 79`.

## The landscape is favorable — 13–30× headroom (measured)

`wlambda_covariance_epic_M1_constant_C_landscape.py` (exit 0; exact `Fraction`; NO float64) measures
the **empirical** envelope `C_emp(N) = max_{n≥N} |m(n)−m_∞|·√n`:

| from `N` | `C_emp(N)` | `N₀_emp = (C_emp/m_∞)²` |
|---|---|---|
| n≥4 | 0.1999 (n=4 dominates) | 0.44 |
| n≥6 | 0.0871 | 0.084 |
| n≥13 | 0.0580 | 0.037 |

The envelope **decreases** with `n` (0.087→0.058→0.050→0.038 over n=6→44): the true deviation decays
*faster* than `n^{−1/2}`, so `|m(n)−m_∞|·√n → 0`. The rigorous target is `C ≤ 2.668`; the empirical
floor is `≈ 0.087`. **A rigorous `C` within ~13–30× of the truth still gives `N₀ ≤ 79`.** So the
approach has large headroom — the question is purely whether the *constant-tracking* stays inside it.

## The rigorous `C` reduces to explicit literature constants

`C` is the propagation of the three-region variance bounds through `m(n) = ρ_P − σ_D/σ_A`. Each region
carries a **published, explicit** error constant:

1. **Tail** `|x| > 2√θ + Kθ^{1/6}` — **pinnable now.** Olver's uniform Bessel error bound (DLMF
   §10.41.10) gives `|J_ν(2√θ)| ≤ C₀·exp(−ν(α−tanh α))/√(2πν tanh α)` explicitly; against the `x²`
   weight the tail of `V(g)` is `O(e^{−cθ^{1/2}})`, **measured ~1e-8** at θ=640. Explicit and
   negligible against the `n^{−1/2}` term.
2. **Sine-series truncation** — **pinnable now.** `Â_k, Ω̂_k ~ 1/k²` (the `|x|`/`Ω` kinks), so
   `V_A = Σ Â_k²/k`, `V_D = Σ(Ω̂_k−Â_k)²/k` have tails `Σ_{k>K} 1/k⁵ ≤ 1/(4K⁴)` — explicit.
3. **Bulk sine-kernel error** — **the binding constant, NOT pinned here.** The uniform Bessel→sine
   approximation `J(x,y) = S(x−y;ρ(x)) + R(x,y;θ)` has `R = O(θ^{−1/2})` with an *explicit* remainder
   bound (Olver DLMF §10.41 / Debye expansion coefficient `u₁`), but carrying that explicit `R` through
   `|V(g)/n² − v| = ½|Σ(g(x)−g(y))²(J²−S²)|` — with the `x²` weight and the `ρ(x)→0` outer-bulk
   behaviour — to a single number is a multi-page estimate.
4. **De-poissonization** — explicit `O(1/n)` (BOO / Costin–Lebowitz), faster than `n^{−1/2}`, does not
   set `C`.
5. **Ratio propagation** `m = ρ_P − σ_D/σ_A`: Lipschitz in the three ingredients given explicit
   lower bounds `σ_A, σ_W ≥ c·n^{...} > 0` (available from the leading IO constants), so
   `C = f(C_A, C_W, C_P)` with `f` explicit once the ingredient constants are.

So `C` **is** an explicit finite number in principle — every ingredient bound is a published
theorem now in the corpus (`library/arxiv-math-9905032v2` BOO; Olver DLMF; BDJ). What is missing is the
**bulk constant (item 3)**: carrying Olver's explicit `θ^{−1/2}` remainder through the `x²`-weighted
bulk sum to a verified `C_A` (and thence `C`).

## Honest verdict (this session)

- **Certified:** `M₁>0` for all `n ≤ 78` (exact `Fraction`, Track B) — the entire finite part.
- **Measured:** 13–30× headroom; the empirical margin deviation decays *faster* than `n^{−1/2}`, so
  `N₀ ≤ 79` is very likely reachable once `C` is pinned.
- **Not done, not faked:** a **verified explicit `C`**. Pinning it is the item-3 bulk constant-tracking
  (Olver remainder → `x²`-weighted bulk sum → `C_A` → ratio), a genuine multi-page hard-analysis
  computation. Asserting a specific `C` without carrying that through would be laundering an estimate;
  the honest state is that `C` is *explicit in principle*, the headroom is large, and the computation
  is the remaining work.

Gap `qou-k5r5` stays **OPEN**, now reduced to a single named estimate: **the explicit Olver/Debye
bulk-remainder constant `C_A` for `Var(Σ|c|)`**, everything else (tail, truncation, de-poissonization,
ratio propagation) being pinnable from published explicit bounds. The finite part (`n≤78`) is done.

## Compute

- [`wlambda_covariance_epic_M1_constant_C_landscape.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_constant_C_landscape.py)
  (exit 0; exact `Fraction`; NO float64) — empirical envelope + implied `N₀`, target `C ≤ 2.668`.

## Cross-references

- Rigorous finite-n bound: [`2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md`](2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md)
- Descent-DPP reduction: [`2026-08-28-covariance-kernel-M1-descent-dpp-variance-rate.md`](2026-08-28-covariance-kernel-M1-descent-dpp-variance-rate.md)
- Gap bean `qou-k5r5`.
