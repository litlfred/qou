# Covariance-kernel epic (`qou-x631`) — `M₁` antidiagonal reformulation + proof route

**Date:** 2026-08-21 · **Bean:** `qou-ogrk` (A2) · **Discipline:** scope-(a); no fit; nothing wired;
no `c_k`; L2 unchanged.

## Result

The first odd moment `M₁ = Cov_Planch(Σ_□ h, Σ_□ h²)` — the open base case of odd-moment positivity
(even moments proved; odd non-polynomial with no uniform mechanism) — is reformulated into a clean,
geometric, transpose-even shape, and the proof route is pinned.

## The reformulation (exact, verified n ≤ 17)

The odd-moment audit reduced `M₁ = 2·Cov(n_λ, Σc²)` with `n_λ = Σ_i i·λ_i`. Writing the **antidiagonal
index** `b(□) = i+j` and content `c(□) = j−i`, and using `Σ_□ i = n_λ`, `Σ_□ j = n_λ'`:

$$
M_1 \;=\; \mathrm{Cov}_{\text{Planch}}\!\Big(\textstyle\sum_\square (i{+}j),\ \sum_\square (j{-}i)^2\Big)
     \;=\; \mathrm{Cov}_{\text{Planch}}(\Sigma b,\ \Sigma c^2).
$$

So **`M₁ > 0` ⟺ the antidiagonal spread `Σ(i+j)` positively correlates with the diagonal spread
`Σc²`**. `Σb` is transpose-*even* (invariant under `(i,j)↦(j,i)`) yet still `∉` the shifted-symmetric
algebra `A` — precisely why `M₁` is non-polynomial while `Σc² ∈ A`. Verified equal to `2·Cov(n_λ,Σc²)`
and to `Cov(Σh, Σh²)` for every `n ≤ 17` (exact `Fraction`).

## Facts supporting the positivity proof (exact, n ≤ 19)

- `Cov(Σb, Σc²) > 0` robustly; correlation `ρ = Cov/√(Var Σb · Var Σc²) ≈ 0.85–0.92`, converging to
  ~0.92 — a **near-perfect** correlation: `Σb` and `Σc²` are almost proportional as fluctuating
  statistics.
- `Var(Σc²) = |C₃| = n(n−1)(n−2)/3` **exactly** (the `ω₃` variance).
- `M₁` is **not** a harmonic-augmented polynomial (`poly₄` and `n²H_n + poly₃` fits both fail) — no
  cheap closed form; the proof is analytic, not algebraic.

## Proof route (Kerov CLT)

`Σb` and `Σc²` are both **quadratic-in-position moments**, hence linear functionals of the diagram
profile `ω`. By Kerov's CLT (Ivanov–Olshanski, [`math/0304010`](https://arxiv.org/abs/math/0304010))
the profile fluctuation is a Gaussian field `Δ` with an explicit covariance kernel `K_Δ`, and

$$
\mathrm{Cov}(\Sigma b, \Sigma c^2) \;=\; \iint \varphi(x)\,\psi(y)\, K_\Delta(x,y)\, dx\, dy,
$$

a quadratic form against `K_Δ` with explicit even test functions `φ` (for `Σb`) and `ψ` (for `Σc²`).
The measured `ρ ≈ 0.9` says `φ` and `ψ` are nearly proportional, so the form is nearly a pure
variance — its positivity (hence `Cov > 0` asymptotically, with an explicit constant) is robust; the
exact `n ≤ 19` data covers the finite-`n` tail. **Executing that integral is the open next step.**

## Honesty / scope

A reformulation + verified supporting facts + a concrete proof route — **not** a proof of `M₁ > 0`
(hence not of odd-moment positivity, A2, or the kernel; all open). The value is (i) the clean geometric
form, and (ii) reducing the proof to one explicit Gaussian-field integral with strong evidence it is
positive.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_M1_antidiagonal_reformulation.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_antidiagonal_reformulation.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-M1-antidiagonal-reformulation.witness.json`

## Cross-references

- Odd-moment structure: [`2026-07-25-covariance-kernel-A2-odd-moment-structure.md`](2026-07-25-covariance-kernel-A2-odd-moment-structure.md)
- Even moments proved: [`2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md`](2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md)
- Epic map: [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`.
