# Covariance-kernel epic (`qou-x631`) — M₁>0 Track D: the Fulman Stein error-term route does NOT close the finite-n sign

**Date:** 2026-08-28 · **Branch:** `claude/m1-fulman-stein-finite-n-2026-08-28` · **PR:** #5887 ·
**Tier:** scope-(a) NEGATIVE (route as posed does not close the sign; reason is a logical
insufficiency, not a weak constant) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`;
L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## The task (Track D)

After the 2026-08-22 one-sided reframing
([audit](2026-08-22-covariance-kernel-M1-onesided-reframing.md)) the all-`n` positivity of
`M₁ = Cov_Planch(Σ□ h, Σ□ c²)` reduces to

> `M₁(n) > 0 ∀n  ⟸  (a) exact M₁ > 0 for n ≤ 12  ∧  (b) κ_n ≥ κ for all n ≥ 13`,

with `κ_n := M₁/n^{5/2}`, `κ := 128/(225π²)`, crossing pinned exactly at `n₀ = 13` (verified
`κ_n > κ` exactly `13 ≤ n ≤ 60`). Part (a) is done. Part (b) — the **one-sided sign of the
second-order correction** — is the sole remaining analytic task.

Track D asks: does **Fulman's error-term machinery** (*Stein's Method and Plancherel Measure of the
Symmetric Group*, `arxiv-math-0305423`, TAMS 2005 — the in-corpus PDF at
`library/arxiv-math-0305423v3/`) — whose transposition-character CLT carries the explicit
`40.1·n^{-1/4}` constant — bound `κ_n − κ` from below by 0 for `n ≥ N₀` with an explicit `N₀`?

## What Fulman actually proves (extracted verbatim from the PDF)

For the **normalized transposition character ratio**
`W(λ) = (n−1)/√2 · χ^λ(12)/dim(λ)` and the up-down chain `J` on Young diagrams:

- **Thm 1.1 (Kerov).** `W` is asymptotically `N(0,1)`.
- **Thm 1.2 (PROVED, the headline error term).**
  > `sup_{x₀} | P(W ≤ x₀) − Φ(x₀) | ≤ 40.1·n^{-1/4}`  — a **Kolmogorov distance**.
- **Thm 1.3 (Stein).** For an exchangeable pair with `E_W(W*) = (1−τ)W`,
  > `sup_{x₀}|P(W≤x₀)−Φ(x₀)| ≤ 2·√(E[1 − (1/2τ)·E_W(W*−W)²]²) + (2π)^{-1/4}·√((1/τ)·E|W*−W|³)`.
- **Prop 4.1.** `E_W(W*) = (1 − 2/(n+1))·W` (`W` is a `J`-eigenfunction, τ = 2/(n+1)).
- **Prop 4.3 (EXACT).** `E_λ((W*)²) = (1−1/n) + [2(n−1)(n−2)²/(n(n+1))]·χ^λ(123)/dim + [(n−1)(n−2)(n−3)²/(2n(n+1))]·χ^λ((12)(34))/dim`.
- **Cor 4.4 (EXACT).** `Var(W) = 1 − 1/n`.
- **Prop 4.5 (EXACT).** `E[(−1 + (n+1)/4·E_λ(W*−W)²)²] = (3n²−5n+6)/(4n³)` — the "variance-of-conditional-second-moment" Stein term, `O(1/n)`.
- **Prop 4.6 (bound).** `E|W*−W|³ ≤ (4e√2/√n)³ + 2e^{−2e√n}(2√2)³` — the third-moment smoothness term, `O(n^{-3/2})`. This is "the crudest term" and is what produces the `n^{-1/4}` rate (via `√((1/τ)·O(n^{-3/2})) ~ √(n·n^{-3/2}) = n^{-1/4}`).
- **Conjectured (UNPROVEN in Fulman).** A `C·n^{-1/2}` rate.

## Why the route WALLS — three reasons

### (1) TYPE MISMATCH — fatal and n-independent

Thm 1.2/1.3 bound a **Kolmogorov distance** `sup_x|F_n(x) − Φ(x)|` between the CDF of the **marginal**
`W` and the standard normal CDF. The target `(b)` is the **sign of a second-order covariance
correction** `κ_n − κ`. These are different kinds of object, and the gap between them is not a
matter of a better constant:

- **A magnitude/error bound is two-sided; the target is one-sided.** Even a perfect moment bound
  `|κ_n − κ| ≤ B_n` yields only `κ_n ≥ κ − B_n`, which is `< κ`. It can **never** certify
  `κ_n − κ ≥ 0`. Proving the one-sided sign requires the **sign** of the leading correction — an
  intrinsically second-order-CLT statement, not an error-term output.
- **A CDF-distance bound does not even control a moment.** `sup_x|F_n − Φ| ≤ ε` does not bound the
  difference of any fixed moment without extra uniform-integrability input, and never its sign. So
  Fulman's output does not, in principle, produce a bound of the **type** `(b)` needs.

This reason is independent of `n` and of every constant; it is why no sharpening of `40.1` (not even
the conjectured `C·n^{-1/2}`) can help.

### (2) WRONG STATISTIC — Σh is outside Λ*

`W ~ Σc` is (up to scale) the transposition central character, an element of the Kerov–Olshanski
algebra `Λ*` and a `J`-eigenfunction. `M₁ = Cov(Σh, Σc²)` pairs `Σc² → ω₃` (in `Λ*`, eigenvalue
`β₃ = (n−2)/(n+1)`) with **`Σh`, which is not in `Λ*` and is not a `J`-eigenfunction** — the "wall"
already recorded in `qou-k5r5` (the middle `i`-weighted term of `2Σh = p₂(λ) + p₂(λ')` is the
non-`Λ*` obstruction). Fulman's exact moment identities (Prop 4.3/4.5) are for `W` and its powers;
none reaches a covariance with `Σh`. Adapting the machinery would require the analogue for a
statistic outside `Λ*` — which Fulman does not supply and which is precisely the open problem.

### (3) VACUOUS CONSTANT at the n₀=13 crossing

Measured exactly (probe below; exact `Fraction` covariance, mpmath 60 dps for the bounds):

| n | `κ_n − κ` (exact margin) | Thm 1.2 `40.1 n^{-1/4}` | Thm 1.3 assembled | bound / margin |
|---|---|---|---|---|
| 13 | 1.346×10⁻⁴ | 21.12 | 15.17 | 1.57×10⁵ |
| 18 | 1.117×10⁻³ | 19.47 | 13.82 | 1.74×10⁴ |
| 24 | 1.471×10⁻³ | 18.12 | 12.76 | 1.23×10⁴ |
| 30 | 1.543×10⁻³ | 17.13 | 12.00 | 1.11×10⁴ |

The exact margin to certify positive is `~10⁻⁴–10⁻³` and **shrinks toward 0** as `n → ∞` (both
`κ_n, κ → κ`). Fulman's bound is `~15–21` at the crossing — larger than the margin by `~10⁴–10⁵`.
The counterfactual `N₀` at which each bound would first drop below even the *peak* margin
(`≈ 1.54×10⁻³`, the most generous fixed target — the real target is smaller):

| bound | rate | `N₀` |
|---|---|---|
| Thm 1.2 (PROVED) | `40.1·n^{-1/4}` | `≈ 4.6×10¹⁷` |
| Thm 1.3 (assembled Stein) | mixed | `≈ 9.3×10¹⁶` |
| conj. (UNPROVEN) `C=40.1` | `C·n^{-1/2}` | `≈ 6.8×10⁸` |
| conj. (optimistic) `C=1` | `C·n^{-1/2}` | `≈ 4.2×10⁵` |

Every `N₀` is astronomically past `n₀ = 13`. (This reason is secondary to (1)/(2): even a constant
of 1 would not repair the type mismatch; but it independently rules out any brute reinterpretation.)

## Explicit N₀ — honest statement

**There is no `N₀`.** The route does not produce a bound of the required type at all:

- By (1), a Fulman-style bound gives `|κ_n − κ| ≤ B_n`, never `κ_n − κ ≥ 0`; so the set of `n` on
  which it certifies `(b)` is **empty for every `n`**, i.e. `N₀ = ∞`.
- The counterfactual `N₀ ≈ 4.6×10¹⁷` (Thm 1.2) is what one would get *if* the Kolmogorov error
  magically bounded the moment gap — which it does not — and even then it is `≫ 13`.

So the honest verdict is not "closes for `n ≥ N₀` with `N₀` too large to meet `13`". It is stronger:
**the error-term machinery is the wrong tool by type; the finite-n sign is not derivable from it.**

## What IS reusable vs what is NOT

- **Reusable (already on `main`, PR #5416 / the 2026-08-21 reduction):** the exact exchangeable-pair
  **covariance identity** `Cov(f, ω₃) = 1/(2(1−β₃))·E[Δf·Δω₃] = (n+1)/6·Σ_edges 2w·Δf·Δω₃`. This is
  the *identity* half of Stein's method and it is exact and valuable — but it is **circular** for the
  all-n sign, since it merely recomputes `M₁` (which we already have exactly to `n ≤ 60`).
- **Not reusable:** the **error term** (Thm 1.2/1.3, Prop 4.5/4.6). It answers a distributional
  question about the marginal `W`, not the sign of the `Σh–ω₃` covariance correction.

## Where the finite-n sign must come from

The sign of `κ_n − κ` is a **second-order free-cumulant / genus-1** fact (Śniady
`arxiv-math-0411647`, sec 4.5; Dołęga–Féray). The one-sided reframing already localised it to the
structural target *"`N` (the `ΣD²`-spread covariance) converges to its VKLS limit slower than `P`
(the `|c|`-spread covariance)"* — a second-order rate comparison. That is precisely the Track A/B
Śniady tool, **not** Fulman's first-order Berry–Esseen. Track D's contribution is to remove the
Fulman error term from the candidate-tool list with a proved reason, not merely a weak number.

## Compute

- Probe: [`wlambda_covariance_epic_M1_fulman_stein_finite_n_bound.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_fulman_stein_finite_n_bound.py)
  (exit 0; exact `Fraction` `M₁`/`κ_n`, mpmath 60 dps for the Fulman bounds and `κ = 128/(225π²)`;
  no float64; emits no witness; nothing wired). Log: `/tmp/fulman_stein_probe.log`.

## Cross-references

- One-sided reframing (the target `(b)`): [`2026-08-22-covariance-kernel-M1-onesided-reframing.md`](2026-08-22-covariance-kernel-M1-onesided-reframing.md)
- Fulman exchangeable-pair reduction (`M₁ = P − N`; the *identity* half): [`2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)
- Route 1 (Fulman-analogue for the 3-cycle; Dirichlet-form sign): [`2026-07-24-covariance-kernel-route1-exchangeable-pair.md`](2026-07-24-covariance-kernel-route1-exchangeable-pair.md)
- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Fulman, *Stein's Method and Plancherel Measure* (`math/0305423`, TAMS 2005); gap bean `qou-k5r5`.
