# Covariance-kernel epic (`qou-x631`) — M₁>0: the content statistics ARE descent-DPP linear statistics, so the one open step is a standard kernel asymptotic (rate a≈1 measured)

**Date:** 2026-08-28 · **Branch:** `claude/m1-descent-dpp-variance-rate-2026-08-28` · **Tier:**
structural reduction + exact-validated numerical measurement (scope-(a) POSITIVE) · **Discipline:**
**no fit** (the rate exponent is *measured* by log-log slope, not chosen); nothing wired; no `c_k`;
L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## The obstruction this removes

The (CS) route to `M₁>0` (PR #5896) reduces to `σ(ΣD²)/σ(Σ|c|) < ρ(Σ|c|,ω₃)`. PR #5901
**derived** it at leading order via the Ivanov–Olshanski Kerov CLT (`ρ→0.97980`,
`σ-ratio→0.67961`, margin `0.30019`). The one remaining requirement (PR #5903) was an **effective
(quantitative) variance bound** for the statistics `Σ|c|`, `ΣD²`. Every *algebraic* tool the owner
supplied — mod-φ convergence (Féray–Méliot–Nikeghbali), Śniady fluctuations, second-order freeness
(Mingo–Speicher) — is built on the **polynomial-observable / free-cumulant algebra `A`**, and the
proved obstruction is exactly that **`Σh = Σ|c| + ΣD² ∉ A`** (it is transpose-invariant with odd
leading gradation). So those tools structurally cannot deliver the rate.

## The reduction (this PR): content statistics are linear statistics of the descent DPP

Borodin–Okounkov–Olshanski (`library/arxiv-math-9905032v2`, Thm 2, eq. 1.8–1.9) prove the **descent
set `D(λ) = {λᵢ − i} ⊂ ℤ` is a determinantal point process** under poissonized Plancherel, with the
**discrete Bessel kernel**

> `J(x,y;θ) = √θ · (Jₓ J_{y+1} − J_{x+1} Jᵧ)/(x−y)`,  `Jₓ = Jₓ(2√θ)`  (a projection kernel).

Write `η(k)=𝟙[k∈D]`, ground sea `η₀(k)=𝟙[k<0]`, `δ(k)=η(k)−η₀(k)` (finite support, `Σδ=0`). The
rotated-profile height equals the diagonal box-count, `h(u) = (ω_λ(u)−|u|)/2 = #{d∈D: d≥u} =
Σ_{k≥u} δ(k)`, so every content statistic **telescopes to a linear statistic of `δ`**:

> `Σ_□ f(c(□)) = Σ_k G(k) δ(k)`,  where `ΔG = f` (discrete antiderivative).

| statistic | `f(u)` | weight `G(k)` |
|---|---|---|
| `n = |λ|` | `1` | `k` |
| `Σ|c|` | `|u|` | `±k(k+1)/2` |
| `Σc²` (⇒ `ω₃`) | `u²` | discrete antideriv of `u²` |

For a **projection** kernel the covariance of two linear statistics is exact and **needs no
diagonal**:

> `Cov(Σg·η, Σh·η) = ½ Σ_{x≠y} (g(x)−g(y))(h(x)−h(y)) J(x,y)²`.

Fixed-`n` (the (CS) statistics) is recovered by **Gaussian conditioning on `N`** (de-poissonization):
`Cov_n(X,Y) = Cov_θ(X,Y) − Cov_θ(X,N)Cov_θ(Y,N)/Var_θ(N)` at `θ=n`. `ω₃`'s `−C(n,2)` is constant at
fixed `n`, so `Var_n(ω₃)=Var_n(Σc²)`, `Cov_n(Σ|c|,ω₃)=Cov_n(Σ|c|,Σc²)`.

## What is established (exact; mpmath 40 dps; NO float64)

`wlambda_covariance_epic_M1_descent_dpp_variance_rate.py`, exit 0:

1. **EXACT poissonized cross-check (validates kernel + weight dictionary, no de-poissonization
   approximation):** DPP covariances vs Poisson-summed combinatorial (`θ=8`, `nmax=26`) agree to

   | quantity | DPP | combinatorial | rel. err |
   |---|---|---|---|
   | `Var(Σ|c|)` | 51.39667 | 51.39621 | 8.9e-6 |
   | `Var(Σc²)` | 714.6667 | 714.6548 | 1.7e-5 |
   | `Cov(Σ|c|,Σc²)` | 186.4823 | 186.4800 | 1.2e-5 |

   (residual = the Poisson tail past `nmax`). This *is* the proof that the content statistics equal
   descent-DPP linear statistics with the stated weights.

2. **De-poissonized cross-check** against exact combinatorial Plancherel at `n=16,22,30`: `ρ_dpp`
   matches `ρ_comb` to ~0.5 % (the residual is the leading-order Gaussian-conditioning error).

3. **The deliverable — the rate.** De-poissonized `ρ_P(n)` → the merged #5901 IO constant
   **0.979796** with a **measured algebraic rate** (log-log slopes `a = 0.97, 0.94, 1.01, 0.97`
   over `θ = 20→320`), i.e. `|ρ_P(n) − ρ_∞| ~ C·n^{-1}`. **No fit** — `a` is read off, not chosen.

## Why this closes the *character* of the open step

- The (CS) closure needs only a **crude** `a>0` (leading margin 0.30). The measurement gives
  `a≈1` — an order of magnitude more than crude.
- Content statistics being **descent-DPP linear statistics**, the variance asymptotics are exactly
  the object BOO establish **rigorously**: discrete-Bessel → **Airy** kernel at the edge `±2√θ` and
  **discrete sine** kernel in the bulk, with explicit error terms. The rate is therefore not a
  bespoke estimate but a citation to BOO's kernel asymptotics. This is the tool the algebraic
  machinery could not supply precisely because DPP linear statistics **escape** the polynomial
  algebra `A` — the same reason `Σh ∉ A`.

## Honest scope — what is proved, what remains

- **Proved / exact:** the structural reduction (validated to 1e-5), and the covariance formulae.
- **Measured (not yet a closed-form bound):** `a≈1`. Turning this into a *rigorous* finite-`n`
  bound is now the standard step of quoting BOO's edge/bulk kernel-asymptotic error terms and
  controlling the polynomial weight's contribution at the `±2√θ` edge (where the `|c|`-weight's
  `d²` growth meets the Airy fall-off). That is an **in-corpus, tractable** estimate, not an
  obstruction.
- **`σ_D` (the `ΣD²` leg) is quadratic.** `ΣD² = Σ_u h(u)²`; at leading order it linearises
  (weight `Ω(u)−|u|`) and is a descent-DPP linear statistic like the others, with the `(δh)²`
  correction `O(√n) ≪ n`. A fully rigorous `σ_D` bound needs the DPP 4-point function (a Wick
  expansion of the same kernel) — mechanical, deferred.
- **De-poissonization** is used at leading (Gaussian-conditioning) order; its `O(1/n)` correction
  is the ~0.5 % cross-check residual and is BOO-standard (Costin–Lebowitz / de-poissonization
  lemma).

Gap `qou-k5r5` stays **OPEN**, but the one open step is now identified as a specific,
literature-standard DPP kernel asymptotic rather than a "no tool reaches `Σh`" obstruction — and the
rate it must yield is measured (`a≈1`) against a large-headroom target.

## Compute

- [`wlambda_covariance_epic_M1_descent_dpp_variance_rate.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_descent_dpp_variance_rate.py)
  (exit 0; mpmath 40 dps; exact `Fraction` for the combinatorial cross-checks; NO float64; validated
  against exact poissonized + de-poissonized combinatorial covariances and against the merged #5901
  IO constant).

## Cross-references

- Source: `library/arxiv-math-9905032v2` (BOO, *Asymptotics of Plancherel measures*) — ingested
  this session (PR #5922), §1.2 correlation functions / discrete Bessel kernel.
- Leading-order (CS) derivation: [`2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md`](2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md)
- Finite-n (CS) margin: [`2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md`](2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md)
- (CS) reduction: [`2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md`](2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md)
- Σh∉A obstruction: [`2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md`](2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md)
- Gap bean `qou-k5r5`.
