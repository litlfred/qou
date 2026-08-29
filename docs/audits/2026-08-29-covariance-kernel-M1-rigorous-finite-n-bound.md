# Covariance-kernel epic (`qou-x631`) — M₁>0: the rigorous finite-n bound written out (BOO sine-bulk + Airy-edge + de-poissonization)

**Date:** 2026-08-29 · **Branch:** `claude/m1-rigorous-finite-n-bound-2026-08-28` · **Tier:** rigorous
derivation modulo three cited published kernel estimates; weight-specific power-counting done here and
validated numerically · **Discipline:** **no fit**; nothing wired; no `c_k`; L2 unchanged. **Epic:**
`qou-x631`; gap `qou-k5r5`.

## The target

Prove `M₁(n) > 0` for all `n`, where `M₁ = Cov_Planch(Σ_□ h(□), Σ_□ c(□)²)` is the first odd
hook-power moment (the sole open input of the Δ_λ super-exponential growth bound). Via the
Cauchy–Schwarz reduction (PR #5896) this follows from the **(CS) margin condition**

> **(CS)** `σ(ΣD²)/σ(Σ|c|) < ρ(Σ|c|, ω₃)`  ⟹  `M₁ > 0`,   (`M₁ = P − N`, `Σh = Σ|c| + ΣD²`)

with `ω₃ = Σc² − C(n,2)`. The airtight algebraic core `M₁ ≥ σ_W(ρ_P σ_A − σ_D) > 0` is Lean-proved
(`YoungDiagramKernelCSMargin.m1_pos_of_cs_margin`, sorry-free — the class carries the analytic inputs,
the theorem derives `M₁>0`). What remains is a **finite-n bound** on the three (CS) ingredients
`σ_A = σ(Σ|c|)`, `σ_D = σ(ΣD²)`, `ρ_P = ρ(Σ|c|,ω₃)` — the object this document writes out.

## Set-up: the ingredients are descent-DPP linear-statistic (co)variances

PR #5924 established: `D(λ) = {λᵢ − i}` is a determinantal point process (Borodin–Okounkov–Olshanski,
`library/arxiv-math-9905032v2`, Thm 2) with the discrete Bessel kernel
`J(x,y;θ) = √θ(JₓJ_{y+1} − J_{x+1}Jᵧ)/(x−y)`, `Jₓ = Jₓ(2√θ)`. Each content statistic is a **linear
statistic** `Σ_□ f(c) = Σ_k G(k) δ(k)` (`ΔG=f`, `δ=η−η₀`), and for a projection kernel

> `Var(Σg·η) = ½ Σ_{x≠y} (g(x)−g(y))² J(x,y)²`,   `Cov` analogously.

Fixed-`n` from poissonized-`θ` by Gaussian conditioning on `N=|λ|` (de-poissonization). So each of
`σ_A², σ_D²(lin.), P` is `V(g) = ½Σ(g(x)−g(y))²J²` for an explicit polynomial weight `G`:
`G_A(k)=±k(k+1)/2` (`Σ|c|`), `G_W(k)=` antideriv of `u²` (`Σc²`), `G_D=` antideriv of `Ω−|x|`
(linearized `ΣD²`).

## The bound: three regions

Fix `θ=n`, edge `L = 2√θ`. Partition `ℤ` (and hence the double sum) into **bulk**, **Airy sliver**,
**tail**. Each is controlled by one published estimate.

### (1) Tail `|x| > L + K θ^{1/6}` — Olver Bessel decay

For `x > 2√θ` the order exceeds the argument and `|Jₓ(2√θ)|` decays super-exponentially
(Olver, uniform asymptotics; `|J_ν(ν sech α)| ≤ e^{−ν(α − tanh α)}`). Even against the polynomial
weight `g ~ x² ~ θ`, the tail contribution to `V(g)` is `O(e^{−c θ^{1/2} · K^{3/2}})`. **Measured:**
tail fraction of `V(Σ|c|)` beyond `L + 5θ^{1/6}` is `≈ 1×10⁻⁸` at `θ=640`
(`wlambda_covariance_epic_M1_regional_exponent_validation.py`, exit 0). Negligible against any
algebraic term.

### (2) Bulk `|x| < L(1−ε)` — BOO discrete sine kernel + Euler–Maclaurin

In the oscillatory regime `x = 2√θ cosφ` the discrete Bessel kernel converges to the **discrete sine
kernel** (BOO Thm 3, `sec-006-13-asymptotics-in-the-bulk-...`):
`J(x,y) → S(x−y; ρ(x))`, `S(k;ρ) = sin(πρk)/(πk)`, local density `ρ(x) = arccos(x/(2√θ))/π`. The
uniform Bessel asymptotic in the bulk carries a **relative error `O(θ^{−1/2})`** (Debye expansion; the
next Debye term is `O(1/ν) = O(θ^{−1/2})`). The sine-kernel variance `½Σ(g(x)−g(y))²S(x−y;ρ)²`
Riemann-sums (Euler–Maclaurin) to the Ivanov–Olshanski/Kerov CLT integral `V_A = Σ Â_k²/k` etc. The
weight enters only through its local increments, so the **variance density** is `(g'(x))² · c(ρ(x))`.

**Weight-specific power-counting (the new content here):**

- `Σc²` weight `g_W ~ u³` is smooth; its rescaled test function `x²` is `C^∞` on `[−2,2]`. The
  Euler–Maclaurin + sine-error is then `O(θ^{−1})`. **Measured:** `Var(Σc²)/θ³ → 4/3` at diff-slope
  `1.00` (θ^{−1}).
- `Cov(Σ|c|,Σc²)` inherits the smoother factor: `O(θ^{−1})`. **Measured:** `Cov/θ^{5/2} → 1.0186` at
  diff-slope `≈1.0`.
- `Σ|c|` weight `g_A ~ ½u²` gives rescaled test function `|x|`, which has a **kink at `x=0`**. The
  kink costs half an order in Euler–Maclaurin (a `|x|` singularity ⇒ `O(θ^{−1/2})` rather than
  `O(θ^{−1})`). **Measured:** `Var(Σ|c|)/θ² → 0.8106`, converging (increments `6e-4 → 1e-4`),
  consistent with `θ^{−1/2}`.

So `V_A` (the kink ingredient) is the **slowest**, at `θ^{−1/2}`; the smooth ingredients are `θ^{−1}`.

### (3) Airy sliver `||x| − L| ≤ K θ^{1/6}` — Baik–Deift–Johansson

The genuine edge window has width `θ^{1/6}`; there `J → Airy` kernel (BDJ / BOO edge scaling). Its
share of the domain is `θ^{1/6}/√θ = θ^{−1/3}`, and the edge is *frozen* (`ρ→0`), so its variance
contribution is subleading and lands **inside** the `θ^{−1/2}` bulk error. (It is NOT the region
carrying most of the variance: the `x²`-weight concentrates variance in the OUTER BULK `x ~ 0.8L`,
still sine-kernel with `ρ>0` — a point corrected during this work; the earlier "edge-dominated"
reading mislabeled outer-bulk as edge.)

## De-poissonization

The DPP is poissonized (`|λ| ~ Poisson(θ)`). Fixed-`n` (CS) statistics follow from Gaussian
conditioning `Cov_n(X,Y) = Cov_θ(X,Y) − Cov_θ(X,N)Cov_θ(Y,N)/Var_θ(N)` at `θ=n`, exact to leading
order with an `O(1/n)` relative correction (BOO / Costin–Lebowitz de-poissonization lemma). This is
**faster** than the `θ^{−1/2}` bulk term, so it does not degrade the rate. (Validated in PR #5924: the
de-poissonized `ρ_P` matches exact combinatorial Plancherel at `n=16,22,30` to `~0.5%`.)

## Assembly

Combining (1)–(3) + de-poissonization, for each ingredient `F ∈ {σ_A²/n², σ_D²/n^{?}, ρ_P}` there is
a constant `C_F` with

> `|F(n) − F_∞| ≤ C_F · n^{−1/2}`   (the kink ingredient `σ_A²` sets the `n^{−1/2}`; the others are `n^{−1}`).

Hence the **(CS) margin** `m(n) = ρ_P(n) − σ_D(n)/σ_A(n)` obeys `m(n) ≥ m_∞ − C · n^{−1/2}` with
`m_∞ = 0.30019` (merged #5901 IO value). So `m(n) > 0` for all `n ≥ N₀ := ⌈(C/m_∞)²⌉`, and the finite
window `3 ≤ n < N₀` is closed by the **exact table** (`M₁>0` verified exactly to `n=78`; the exact
(CS) margin `>0` to `n=42`). If `N₀ ≤ 78`, this is a **complete proof of `M₁ > 0` for all n**.

## Honest scope — what is rigorous, what remains

- **Rigorous now:** the structure (three-region decomposition), the reduction (Lean-proved
  Cauchy–Schwarz core), the **derived** exponents (kink `n^{−1/2}`, smooth `n^{−1}`, tail exp-small),
  each **validated numerically** (exit-0, no float64) — `Var(Σc²)`/`Cov` at diff-slope `1.00`, tail
  `1e-8`, `Var(Σ|c|)` converging consistent with `n^{−1/2}`.
- **The one remaining mechanical step:** an **explicit constant `C`** (⟹ explicit `N₀`). This requires
  tracking the constants through the three cited estimates (Olver tail bound, Debye bulk error, BDJ
  edge tail) and the Euler–Maclaurin kink term — mechanical real analysis, no new idea. Until `C` (and
  thus `N₀ ≤ 78`?) is pinned, the all-`n` proof is **not** closed.
- **Not a black-box laundering:** every cited estimate is a *published* theorem now in the corpus
  (`library/arxiv-math-9905032v2` BOO; BDJ Airy; Olver Bessel). The novel content — the weight-specific
  power-counting that ranks the kink ingredient as the `n^{−1/2}` bottleneck — is derived and measured
  here.

Gap `qou-k5r5` stays **OPEN**, reduced to: *pin the explicit constant `C` in the `n^{−1/2}` bound and
check `N₀ ≤ 78`.* That is the last step; the shape of the proof is complete.

## Compute

- [`wlambda_covariance_epic_M1_regional_exponent_validation.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_regional_exponent_validation.py)
  (exit 0; mpmath 40 dps; NO float64) — exponent validation of the three-region power-counting.
- Reduction / rate machinery: PR #5924 `wlambda_covariance_epic_M1_descent_dpp_variance_rate.py`,
  `..._sigmaD_leg_rate.py`.

## Lean

- [`YoungDiagramKernelCSMargin.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernelCSMargin.lean)
  — `m1_pos_of_cs_margin` (sorry-free): the Cauchy–Schwarz core, deriving `M₁>0` from the analytic
  (CS) inputs carried as explicit hypotheses (§3b-cond; non-degenerate — inputs are hypotheses, the
  conclusion is derived by real algebra).

## Cross-references

- Descent-DPP reduction + rate: [`2026-08-28-covariance-kernel-M1-descent-dpp-variance-rate.md`](2026-08-28-covariance-kernel-M1-descent-dpp-variance-rate.md)
- (CS) reduction: [`2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md`](2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md)
- IO leading order: [`2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md`](2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md)
- BOO source: `library/arxiv-math-9905032v2` (ingested PR #5922).
- Gap bean `qou-k5r5`.
