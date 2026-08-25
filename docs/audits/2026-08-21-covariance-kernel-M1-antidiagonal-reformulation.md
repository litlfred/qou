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

## Further structure + resolution status (2026-08-21, "dull analysis")

Attempting to *resolve* `M₁ > 0` (not just reformulate), the following exact facts were established
(exact `Fraction`, n ≤ 24):

- **Cleaner exact form:** `M₁ = Cov(Σᵢ λᵢ², Σc²)` (squared row-lengths vs squared contents), via
  `Σh = n_λ+n_{λ'}+n` and `Σᵢ C(λᵢ,2) = (Σᵢλᵢ² − n)/2`. **Lean-formalized** (`decide`, k≤5):
  `m1_eq_cov_rowSq_contentSq_of_le_five`, with the per-partition `Σh² = Σc² + n²`
  (`hookSqSum_eq_contentSq_add_sq_card_of_le_eight`, k≤8).
- **`Cov(p₂*, Σc²) = 0` exactly** (the shifted power sum `p₂*` is Plancherel-uncorrelated with `Σc²`);
  since `Σᵢλᵢ² = p₂* + 2ñ_λ − n`, the non-polynomiality of `M₁` is carried entirely by the non-shifted-
  symmetric part — traceable to the **number of parts** `ℓ(λ)`.
- **Geometric decomposition:** `M₁ = Cov(Σ|c|, Σc²) + Cov(Σ_c h(c)², Σc²)`, the first **positive**
  (dominant), the second **negative** — a **partial cancellation** of two `~n^{5/2}` terms with ratio
  `Cov(Σh²,Σc²)/Cov(Σ|c|,Σc²) → −0.62`. So `M₁ ≈ 0.38 ×` (a positive `n^{5/2}` term).
- **Asymptotic:** `Cov(Σb,Σc²) → κ·n^{5/2}`, `κ ≈ 0.0591` (clean exponent 5/2); correlation
  `ρ(Σb,Σc²) → ~0.93`.
- **No simple closed form:** `M₁ ≠ poly(n) + {E[ℓ], E[ℓ²], E[λ₁], ℓ·poly}` combinations (all exact
  fits fail, n ≤ 19). The denominators carry every prime ≤ n — a genuinely complex Plancherel
  expectation.

**Resolution status: `M₁ > 0` remains OPEN.** The Kerov-CLT route gives *asymptotic* positivity (the
`n^{5/2}` constant `κ > 0`), but a rigorous all-`n` proof requires either (i) an exact closed form
(none found), or (ii) a rigorous Kerov-CLT constant **plus a finite-`n` error bound** controlling the
`±n^{5/2}` cancellation (`ratio > −1` uniformly). Both are genuine analysis; this is the "same
difficulty class as the open kernel" the odd-moment audit named, now made precise. **Not resolved; not
laundered.** The *identity* is Lean-proved (finitely many `n`); the *positivity* is not.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_M1_antidiagonal_reformulation.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_antidiagonal_reformulation.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-M1-antidiagonal-reformulation.witness.json`

## Cross-references

- Odd-moment structure: [`2026-07-25-covariance-kernel-A2-odd-moment-structure.md`](2026-07-25-covariance-kernel-A2-odd-moment-structure.md)
- Even moments proved: [`2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md`](2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md)
- Epic map: [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`.
