# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: the one open step is a *rate* for the discrete-Bessel→sine-kernel convergence, and the corpus cites only the rate-free limit

**Date:** 2026-08-29 · **Branch:** `claude/m1-k5r5-bessel-rate-citation-2026-08-29` · **Tier:**
corpus-grep + primary-source reading + exact finite-n measurement · **Discipline:** no fit; no fake
closure — this sharpens the gap and names the exact missing citation, it does **not** close it.
**Epic:** `qou-h315`/`qou-x631`; gap `qou-k5r5`.

## What is now established (and what is not)

The proof of `M₁ = Cov_Planch(Σh, ω₃) > 0` for **all n** reduces (PR #5896) to the Cauchy–Schwarz
sufficient condition **(CS)** `σ_D/σ_A < ρ_P`, equivalently the margin `m(n) = ρ_P(n) − σ_D(n)/σ_A(n) > 0`.

**Done (this arc):**
- **Leading order** (#5901, and closed forms in PR #5969 / `qou-po72`): `ρ_P → 2√6/5 = 0.9797959`,
  `σ_D/σ_A → √(V_D/V_A) = 0.6796096`, so `m∞ = 0.3001861 > 0`. Constants exact:
  `V_A = 8/(9π²)`, `Var(ω₃)` leading `1/3`, `P = 8/(15π)`, `ρ_P = 2√6/5`; `V_D = 0.04159748…`.
- **Exact finite n** (`wlambda_covariance_epic_M1_finite_n_cs_margin.py`, exact `Fraction`): `m(n) > 0`
  for **every 4 ≤ n ≤ 40**, minimum `m(4) = 0.20025`. The margin **oscillates** around `0.30019` with
  **decreasing** amplitude (≈0.008 at n=40), the damped-oscillation finite-n signature. It does **not**
  approach the limit monotonically.
- **Rate of the leading ingredient** (`qou-tvok`, #5959): the poissonized `V_A(θ)/θ² → 8/π²` at rate
  `θ^{−1}`.

**The one open step (unchanged, now sharpened):** because the finite-n tail is *oscillatory, not
monotone*, "exact-check-small-n + leading-order-large-n" does **not** cover all n on its own. Closing
it needs an **effective (quantitative) variance bound**
> `|Var_n(Σ g·η)/n² − V_g| ≤ C_g · n^{−a}` (any `a > 0`, `C_g` explicit) for `g ∈ {G_A, G_D, x²}`,
large enough that the `0.30` leading margin absorbs it for `n > 40`. A crude rate suffices — the
margin only has to stay positive, and the deviation at n=40 is already ~0.008 against a 0.30 budget.

## The missing ingredient is a kernel-convergence RATE, and the corpus has only the rate-free limit

The content statistics are exact linear statistics of the descent determinantal point process with
the discrete Bessel kernel `J(x,y;θ)` (BOO, `library/arxiv-math-9905032v2`), and their variance is the
exact projection-kernel sum `Var = ½Σ_{x≠y}(g(x)−g(y))²J(x,y)²`. The effective bound above is
therefore an **effective rate for `J(x,y;θ)` converging to the discrete sine kernel in the bulk (and
the Airy kernel at the edge).**

**Primary-source finding (corpus-grep path 5, read at the source):** BOO's bulk-asymptotics result,
**Theorem 3** (`sec-006-13-asymptotics-in-the-bulk-of-the-spectrum-given.md`), states this convergence
as a **bare limit** —
> `lim_{n→∞} ϱ(n, X(n)) = det[S(d_ij, a)]` (the discrete sine kernel),

with **no error term and no rate**. The edge (Airy) statement is likewise a limit. So the exact
theorem the descent-DPP route relies on gives *convergence*, not *speed of convergence* — which is
precisely the ingredient the finite-n bound needs.

**Corpus does not supply the rate elsewhere.** A whole-library grep
(`library/*/sections/`) for `olver` / `uniform asymptotic` / `error term` / `rate of convergence` /
`berry-esseen` / `second-order freeness` / `edgeworth` returns only unrelated domains or tools already
ruled out for this statistic:
- **Fulman, Stein's method** (`library/arxiv-math-0305423v3`) gives a *marginal Berry–Esseen* rate —
  ruled out already (it bounds a single statistic's CDF, not the *joint* variance ratio the (CS)
  margin needs; noted in `finite_n_cs_margin.py`).
- **Second-order freeness / Śniady genus expansion** (`library/arxiv-1402.4615v3`) applies to
  *polynomial* functions of the diagram; `Σh` and `Σ|c|` are **not** polynomial (the whole reason this
  gap exists — `descent_dpp_variance_rate.py`).

So the "Olver-Bessel wall" is **not an in-corpus oversight** — it is a genuine external-citation gap.
The precise missing citation is:

> **An effective (error-bounded) form of the discrete Bessel → discrete sine kernel convergence** for
> the Plancherel descent process — e.g. Olver-type uniform asymptotics of `J_x(2√θ)` in the bulk
> `x = a√θ`, `|a| < 2`, or a Riemann–Hilbert / Deift–Its–Krasovsky treatment of the associated
> Toeplitz/Fredholm determinant — of the shape `|J(x,y;θ) − S(x−y; a)| ≤ c·θ^{−b}` uniformly on the
> bulk, plus the classical super-exponential Bessel tail bound past the edge `x > 2√θ + O(θ^{1/6})`.

The tail half is classical and Olver-free (super-exponential decay of `J_x(2√θ)` for `x` past the
edge); the **bulk** half is what needs the uniform asymptotics. That decomposition is the honest state
of the wall: one half is in reach, the other half is the named citation above.

## Why not fake it

The leading margin `0.30`, the exact positivity through n=40, and the decreasing oscillation make
`M₁ > 0` all-n *morally certain*. It is **not proved**: a rigorous all-n statement requires the
effective kernel rate above, and asserting the bound with a *measured* constant (as `qou-tvok`'s
`c₁ ≈ 0.068` or the n=40 amplitude ≈0.008) would be a measured `C`, not a proved `C` — the exact
distinction the anti-laundering discipline forbids blurring. The gap stays **OPEN**; what this record
adds is that its remaining content is a single, named, external analytic lemma, and that the corpus
has been checked at the source and does not already contain it.

## Compute + sources

- Exact finite-n margin: [`wlambda_covariance_epic_M1_finite_n_cs_margin.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_finite_n_cs_margin.py) (exit 0; exact `Fraction`; `m(n)>0`, 4≤n≤40).
- Leading closed forms: [`2026-08-29-covariance-kernel-M1-po72-leading-constants.md`](2026-08-29-covariance-kernel-M1-po72-leading-constants.md) (merged #5969).
- `V_A` rate `θ^{−1}`: [`2026-08-29-covariance-kernel-M1-tvok-remainder-rate.md`](2026-08-29-covariance-kernel-M1-tvok-remainder-rate.md) (merged #5959).
- BOO bulk limit (rate-free): `library/arxiv-math-9905032v2/sections/sec-003-13-asymptotics-in-the-bulk-of-the-spectrum.md`, Theorem 3.
- Fulman Stein's method: `library/arxiv-math-0305423v3`; Śniady–Dołęga: `library/arxiv-1402.4615v3`.

## Cross-references

- Epic `qou-h315`/`qou-x631`; gap `qou-k5r5`; machinery `qou-tvok` (rate), `qou-po72` (leading constants).
