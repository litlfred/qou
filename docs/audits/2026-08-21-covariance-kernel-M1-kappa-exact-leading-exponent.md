# Covariance-kernel epic (`qou-x631`) — M₁ leading term: exponent 5/2 confirmed, κ NOT pinned (√2/24 refuted as confirmed)

**Date:** 2026-08-21 · **Branch:** `claude/m1-sniady-kerov-clt-leading-term-2026-08-21` ·
**Tier:** exact-arithmetic anchor + structural setup for the Kerov-CLT leading term ·
**Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`;
attack `qou-ogrk` (A2); gap `qou-k5r5`.

## What this settles, and what it does not

The first odd hook-power moment `M₁ = Cov_Planch(Σ□ h, Σ□ c²) = ⅓·Cov(Σ□ h, R₄)` is the open
input of the Δ_λ growth chain. Its asymptotics were believed to be `M₁ ~ κ·n^{5/2}`, `κ > 0`, with
a prior **float64** reading `κ ≈ 0.0591` "trending slightly above `√2/24 ≈ 0.058926`". That reading
was an artifact of catastrophic cancellation in `E[XY] − E[X]E[Y]`.

Recomputing the covariance in **exact `Fraction` arithmetic** (Plancherel weight
`w_λ = (f^λ)²/n!` is an exact rational; `Σh`, `Σc²` are exact integers) and dividing by `n^{5/2}` in
mpmath at 60 dps — the only irrational step — gives a clean, cancellation-free `κ_n`. Three results:

| # | Result | Status |
|---|---|---|
| 1 | **Leading exponent is 5/2.** Effective exponent `a_n = ln(Cov_n/Cov_{n−1})/ln(n/(n−1)) → 2.500` (2.4999 by n=38). | solid |
| 2 | **`Cov(Σh, Σc²) > 0` for every `3 ≤ n ≤ 50`**, exact. | solid (finite range) |
| 3 | **`κ_n` is NON-MONOTONE.** It rises, peaks at **n=32, `κ₃₂ = 0.0591961`**, then *descends* smoothly (n=44: 0.0591309; n=50: 0.0590862; ≈ −7·10⁻⁶/step, still drifting). | **κ NOT pinned** |

**Consequence for `√2/24`:** the tail sits ~0.4 % above `√2/24` and is *falling toward it from above*,
but the descent has not stabilised by n=50, so **no clean constant is confirmed** — `√2/24`,
`1/17 = 0.058824`, and neighbours are all within the still-moving window. The prior "trends above
√2/24" statement is **withdrawn**: it was reading the pre-peak overshoot. Low-order Richardson
(`κ + a n^{−1/2} + b n^{−1}`) is invalid here — its 3-point extrapolants bounce (0.063 → 0.055 over
n=45–50) because the sequence is non-monotone.

This is a **scope-(a)** clarification: it does not refute `κ > 0` (positivity is manifest to n=50 and
the exponent is a clean 5/2); it refutes the *claim that numerics pin κ*, and kills a false lead.

## The structural setup (why Σh is outside the shifted-symmetric algebra)

Two exact identities (both verified for every `λ ⊢ n`, `n ≤ 12`; id1 is Lean-formalizable, cf.
`hookSum_eq_nLambda_add_conj_add_card_of_le_seven` already in `YoungDiagramKernel.lean`):

- **`2·Σ□ h(□) = p₂(λ) + p₂(λ′)`**, `p₂(λ) := Σᵢ λᵢ²`. So `Σh = ½(p₂(λ)+p₂(λ′))` and, by
  transpose-invariance of Plancherel with `R₄` transpose-even, `M₁ = ⅓Cov(Σh,R₄) = ⅓Cov(p₂(λ),R₄) =
  Cov(p₂(λ), Σc²)`.
- **`p₂(λ) = Σᵢ (λᵢ − i)² + 2·Σᵢ i(λᵢ − i) + Σᵢ i²`.** The middle term `2Σᵢ i(λᵢ−i)` carries an
  **explicit row-index weight `i`** — it is *not* a shifted power sum `Σᵢ[(λᵢ−i+½)ᵏ − (−i+½)ᵏ]`.
  This is precisely why `Σh ∉ Λ*` (the Kerov–Olshanski algebra of polynomial functions of free
  cumulants): the `i`-weighting is the obstruction, and it couples `Σh` to the row count `ℓ(λ)` and
  the edge part `λ₁`.

**Order accounting** (bulk-Gaussian leading, edge subleading):

- `E[Σh] ~ c·n^{3/2}` (limit shape); the *fluctuation* `sd(Σh) ~ n` (bulk CLT).
- `sd(Σc²) = sd(R₄/3) ~ (√3/3)·n^{3/2}` (Kerov CLT: `Var(R₄) = 3n(n−1)(n−2)`, exact).
- `Cov(Σh, Σc²) ~ κ·n^{5/2}` saturates `sd(Σh)·sd(Σc²) ~ n^{5/2}` up to the correlation `ρ ≈ 0.93`.
- The edge/`λ₁²` contribution to `sd(Σh)` is `~ n^{2/3}` (Tracy–Widom: `λ₁ ≈ 2√n + n^{1/6}·TW`),
  strictly **subleading** to the bulk `n`. So the *leading* κ is a **bulk-Gaussian** covariance;
  the edge (and the `i`-weighting's coupling to it) is the natural candidate for the **non-monotone
  correction** seen in Result 3.

## The honest gap (κ needs the IO kernel, not more n)

The leading constant κ is the covariance of two linear statistics of the Plancherel-random profile —
`Σc²` (in `Λ*`, ↔ `R₄`) and `Σh` (**outside** `Λ*`, via the `i`-weighting). The standard Kerov-CLT
covariance `Cov(R_a,R_b) → δ_{ab}(a−1)n^{a−1}` (exact-verified here: `Var R₃ = 2n(n−1)`,
`Var R₄ = 3n(n−1)(n−2)`, `Cov(R₃,R₄)=0`) diagonalises the `Λ*` side but **not** `Σh`. Computing κ
requires the full **Ivanov–Olshanski Gaussian-field kernel** applied to the non-`Λ*` statistic `Σh`
(bulk term via the VKLS limit shape + Chebyshev-mode covariance). That is the genuine analysis step;
it is **not** closeable by exact enumeration (Result 3 shows why — the sequence is still moving at
n=50), and it must **not** be replaced by fitting a constant to the drifting tail.

Roadmap (unchanged, now with a sharpened target): the two in-corpus tools are
**Śniady `arxiv-math-0411647` §4.5** (2nd-order free-cumulant expansion → the bulk κ) and
**Fulman `arxiv-math-0305423` §2–3** (Stein exchangeable pair → the finite-n bound controlling the
±n^{5/2} cancellation and the edge correction). The exact anchor here is what any analytic κ must
reproduce — and it must reproduce a **non-monotone** approach, not a monotone one.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_M1_kerov_clt_leading_kappa.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_kerov_clt_leading_kappa.py)
  (exit 0; exact `Fraction` covariance, mpmath extrapolation, both identity checks). No witness — a
  diagnostic probe; NO float64 (precision gate clean).

## Cross-references

- Reformulation + identity Lean-formalized (merged): PR #5366; free-cumulant reframing (merged): #5392.
- Epic synthesis: [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md).
- Even-moment positivity (proved): [`2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md`](2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md).
- Gap bean `qou-k5r5`; literature roadmap PR #5416.
