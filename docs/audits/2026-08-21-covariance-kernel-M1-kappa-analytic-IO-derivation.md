# Covariance-kernel epic (`qou-x631`) — M₁ leading constant DERIVED: κ = 128/(225π²)

**Date:** 2026-08-21 · **Branch:** `claude/m1-sniady-kerov-clt-leading-term-2026-08-21` ·
**Tier:** analytic derivation of the leading constant (rigorous modulo the Ivanov–Olshanski CLT
theorem), verified to 40 digits + exact calibration cross-check · **Discipline:** scope-(a) POSITIVE
(a derivation, not a refutation); **no fit** (the constant is an analytic integral, not fitted to
data); nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Result

The first odd hook-power moment `M₁ = Cov_Planch(Σ□ h, Σ□ c²) = ⅓Cov(Σh, R₄)` has leading asymptotics

> **`M₁ = κ · n^{5/2} · (1 + o(1))`,  with  `κ = 128/(225π²) = 0.0576404955832…`  > 0.**

This is **derived**, not conjectured or fitted: it is an explicit Chebyshev-mode integral against the
Vershik–Kerov–Logan–Shepp (VKLS) limit shape, evaluated in closed form and verified by independent
quadrature to 1e-42. The prior status was "κ ≈ 0.059, non-monotone, √2/24 not confirmed"
([exact-anchor audit](2026-08-21-covariance-kernel-M1-kappa-exact-leading-exponent.md)); the derived
value `0.05764` is **below** √2/24 = 0.058926 — consistent with the exact `κ_n` descending past its
n≈32 peak toward it (the finite-n data never reaches it because the corrections are large; see §5).

## Derivation

**Step 1 — an exact identity moving Σh onto the diagonal-length function** (verified for every
`λ⊢n`, `n≤14`; the one load-bearing combinatorial step, Lean-formalizable):

> **`Σ□ h(□) = Σ_u D(u)² + Σ□ |c(□)|`,  `D(u) := #{□ : c(□)=u}`** (diagonal lengths).

(Proof: on diagonal `c=u`, the `D(u)` boxes have anti-diagonal `b=i+j` summing to `D(u)²+(|u|−1)D(u)`;
sum over `u` and use `Σh = Σ□(i+j)+n`.) Both `Σ_u D(u)²` and `Σ|c|` are transpose-even, and
`Σc = ½(p₂(λ)−p₂(λ'))` is transpose-odd, so with `Σc² = Σ_u u²D(u)`:

> `M₁ = Cov(Σ_u D(u)² + Σ|c|, Σ_u u² D(u))` — a covariance of functionals of the **single** function
> `D(u)`. The quadratic `Σ_u D(u)²` linearises at leading order: `δ(ΣD²) = 2Σ_u ⟨D(u)⟩ δD(u) + O(√n)`
> (the dropped `Σ(δD)²` is order `√n`, subleading to the linear order `n`).

**Step 2 — the Ivanov–Olshanski Kerov-CLT field** ([`arxiv-math-0304010`](https://arxiv.org/abs/math/0304010),
eq 0.3 / Thm 7.1). Rescaling contents by `√n`, the profile fluctuation is the generalized Gaussian
field

> `Δ(2cosθ) = (1/π) Σ_{k≥2} (ξ_k/√k) sin(kθ)`,  `ξ_k` iid `N(0,1)`,

with `∫h dΔ = Σ_{k≥2}(ξ_k/√k) ĥ_k`, `ĥ_k = (2/π)∫₀^π h(2cosθ)sin(kθ)sinθ dθ`, and
`Cov(∫f dΔ,∫g dΔ) = Σ_{k≥2} ĥ_k... = Σ_k f̂_k ĝ_k / k`.

**Step 3 — calibration (exactly cross-checked).** With `D(√n x) = √n D_∞(x) + δD`, `δD(√n x) = Δ(x)`,
and `Σ_u = √n∫dx`, a content statistic `Σ_u g(u)D(u)` has `δ = n^{(deg g+1)/2}∫g dΔ`. For `g=x²`:
`x² = 2+2cos2θ ⟹ x̂²_k = δ_{k,1}+δ_{k,3}` (the `k=1` mode is frozen — it is the conserved `R₂=n`), so
`δΣc² = n^{3/2}·(ξ₃/√3)` and **`Var(Σc²)/n³ → 1/3`**. This **matches the known exact
`Var(Σc²)=n(n−1)(n−2)/3`** — a non-trivial confirmation that the field normalisation is correct.

**Step 4 — Σh's test function is the limit shape itself.** The linearised `Σh` has test function

> `φ_h(x) = 2D_∞(x) + |x| = 2·(Ω(x)−|x|)/2 + |x| = Ω(x)` (VKLS),

so `δΣh = n∫Ω dΔ`. Hence

> `M₁ = Cov(δΣh, δΣc²) = n^{5/2} · Σ_{k≥2}(1/k) Ω̂_k x̂²_k = n^{5/2} · (1/3) Ω̂₃`,

since `x̂²` is supported on `k=3` alone. With `Ω(2cosθ) = (4/π)(cosθ(π/2−θ)+sinθ)`:

> `Ω̂₃ = (2/π)∫₀^π Ω(2cosθ)sin3θ sinθ dθ = (8/π²)·(16/75) = 128/(75π²)`,
> **`κ = Ω̂₃/3 = 128/(225π²)`.**

## Verification (all exact / high-precision, NO float64)

| check | result |
|---|---|
| `Ω̂₃` closed form vs quadrature | agree to **1e-42** (`= 128/(75π²)`) |
| calibration `Var(Σc²)/n³` | `→ 1/3` exactly (matches known `n(n−1)(n−2)/3`) |
| independent cross-check `Var(Σh)/n² = Σ_k Ω̂_k²/k` | `→ 0.0099743` (only odd `k`; `k=3` gives 99.9 %) |
| leading correlation `ρ(Σh,Σc²) = κ/√(…)` | `→ 0.99965` (Σh is almost pure `R₄` mode) |
| exact identity `Σh = ΣD²+Σ|c|` | holds `∀λ⊢n, n≤14` |
| mode-decomposition (transition-measure free cumulants, `R₂=n` verified ∀λ) | `R₄`-explained-% of `Var(Σh)` rises toward 100 %, `R₆`-% falls — matches `ρ→1` |

## Scope and honesty

- **This derives the LEADING term** `M₁ ~ κn^{5/2}`, `κ>0`. It is rigorous **modulo the IO CLT**
  (a published theorem, cited not re-proved) and the standard leading-order linearisation of `ΣD²`
  (justified: the quadratic correction is order `√n ≪ n`).
- **Not a fit.** `κ = 128/(225π²)` is an analytic integral; the exact finite-`n` data sits at
  `κ_n ≈ 0.0591` (n≤50) — *different* from `0.05764`, so it was demonstrably not fitted. §5 of the
  probe shows `κ_n > κ` with the residual turning over at the n≈32 peak and `Var(Σh)/n²` descending
  toward `0.00997`; the convergence is **slow** (corrections large at accessible `n`), so numerics
  are *consistent with* but do **not tightly pin** κ. The rigour is in the derivation + the exact
  calibration, not the extrapolation.
- **Does NOT yet prove `M₁ > 0` for all finite `n`.** κ>0 gives *asymptotic* positivity; the all-`n`
  statement additionally needs a finite-`n` bound controlling the `±n^{5/2}` cancellation — the
  **Fulman** Stein-exchangeable-pair route ([`arxiv-math-0305423`](https://arxiv.org/abs/math/0305423)
  §2–3, roadmap PR #5416). With κ>0 now **derived** and exact positivity verified to `n≤50`, the
  remaining gap is exactly that finite-`n` bound.
- No `c_k`; nothing wired to production; L2 unchanged. Gap `qou-k5r5` moves from "leading term
  unknown" to "**leading term derived (κ>0); finite-n bound remaining**".

## Compute

- Derivation + verification: [`wlambda_covariance_epic_M1_kappa_analytic_IO.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_kappa_analytic_IO.py) (exit 0)
- Mode decomposition (transition-measure free cumulants): [`wlambda_covariance_epic_M1_IO_mode_decomposition.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_IO_mode_decomposition.py) (exit 0)
- Exact anchor: [`wlambda_covariance_epic_M1_kerov_clt_leading_kappa.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_kerov_clt_leading_kappa.py) (exit 0)

## Cross-references

- Exact-anchor audit (exponent 5/2, non-monotone κ_n): [`2026-08-21-covariance-kernel-M1-kappa-exact-leading-exponent.md`](2026-08-21-covariance-kernel-M1-kappa-exact-leading-exponent.md)
- Literature roadmap (Śniady + Fulman): PR #5416; reformulation + identity Lean (merged): PR #5366; free-cumulant reframing (merged): PR #5392.
- Epic synthesis: [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md); gap bean `qou-k5r5`.
