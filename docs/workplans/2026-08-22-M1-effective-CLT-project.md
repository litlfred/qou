# Workplan — effective-CLT proof of `M₁ > 0` (all n)

**Date:** 2026-08-22 · **Bean:** `qou-k5r5` (gap), epic `qou-x631` (covariance kernel) ·
**Status:** planning doc for the remaining gap · **Discipline:** scope-(a); no fit; nothing wired;
no `c_k`; L2 unchanged.

## 0. Where this sits

`M₁ = Cov_Planch(Σ□ h, Σ□ c²)` is the **first odd hook-power moment** of the covariance kernel
`cov(k) = Σ_λ (f^λ)³ ω₃(λ) ≤ 0` — the sole open input of the Δ_λ growth chain (per-isotope binding
`B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`). The **even** moments are already proved positive
([`2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md`](../audits/2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md),
Lean `threeM4_pos`/`M6_pos`). `M₁>0` is the first odd brick.

**Already on `main` (this session):**

- **Leading constant DERIVED:** `M₁ = κ·n^{5/2}(1+o(1))`, `κ = 128/(225π²) = 0.0576404955832 > 0`
  ([`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](../audits/2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)),
  via the exact identity `Σ□ h = Σ_u D(u)² + Σ|c|`, the IO field `Δ(2cosθ)=(1/π)Σ_{k≥2}(ξ_k/√k)sin kθ`,
  a calibration that exactly reproduces `Var(Σc²)=n(n−1)(n−2)/3`, and `φ_h = Ω` (VKLS shape).
- **All-n reduced to `N/P<1`** ([`2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md`](../audits/2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)):
  `M₁ = P − N`, `P = Cov(Σ|c|,ω₃) ≥ 0`, `N = −Cov(ΣD²,ω₃) ≥ 0` (both per-edge manifest via the
  up-down chain, eigenvalue `β₃ = (n−2)/(n+1)`). `N/P = E_ω[ratio_e]`, `ratio_e = 2(d_a−d_r+1)/(r−a)`.
  Verified `N/P ≤ 0.613` for n≤22, rising to the proved limit `0.6605 < 1`; `M₁>0` exact to n≤50.
- **Elementary routes refuted:** per-edge (`ratio_e` reaches 4, via the proved 1-Lipschitz lemma
  `|D(u+1)−D(u)|≤1`) and weight-suppression (weight sits on distant moves, ~15% on `ratio_e≥1`).

## 1. The target theorem

> **Effective lower bound.** There exist explicit `κ = 128/(225π²)` and `C < ∞` with
> `M₁(n) ≥ κ·n^{5/2} − C·n²` for all `n ≥ 3`.

Then `M₁(n) > 0` for `n > (C/κ)²`, and the finite tail `n ≤ (C/κ)²` is the exact `Fraction` check
(have it to n≤50; extend as needed). The leader `κn^{5/2}` is proved; **the entire remaining work is
the `C·n²` error term** — a Berry–Esseen-grade second-order estimate, not a new idea.

Equivalent `N/P` form: prove `N/P ≤ 1 − ε` uniformly, i.e. bound the `O(n²)` corrections to `P` and
`N`, not just their `n^{5/2}` leaders.

## 2. Sub-results and corpus sources

### Sub-result (1) — effective leading term (the `Λ*` side). **Start here.**
`Σc²`, `R₄`, `ω₃` are shifted-symmetric ⇒ their moments are *exact polynomials* (have `Var(ω₃)`
exactly). Need the second-order term of the content-functional covariances.
- **Source: Śniady `arxiv-math-0411647` §4.5**, Thm 4.13/4.14 (genus-1 / second-order free-cumulant
  expansion). Genus-0 = `κ`; genus-1 = the `C·n²` correction. This paper's genus expansion is the
  right machine and is fully in-corpus (`library/arxiv-math-0411647v2/`).
- Deliverable: an explicit `O(n²)` bound (or exact form) for the content-side pieces of `Cov(Σh,ω₃)`.

### Sub-result (2) — the non-`Λ*` piece (`Σh`'s deviation from `n∫Ω dΔ`).
`Σh = Σ_uD(u)² + Σ|c| ∉ Λ*`. Need the `O(n²)` variance/covariance corrections beyond the leading
profile-field term.
- **Source: Fulman `arxiv-math-0305423` §3** (exact finite-n moments via the exchangeable pair —
  Prop 4.3/4.5 give *exact*, not asymptotic, second moments: the finite-n control this piece needs).
  Plus IO `arxiv-math-0304010` (the field itself, already used).
- **Corroborating: Dołęga–Féray `arxiv-1402.4615`, Dołęga–Śniady `arxiv-1704.02352`** — polynomiality
  + explicit-order structure that turns "there is an `O(n²)` term" into "it is bounded by explicit `C`".

### Sub-result (3) — finite check. **Have it.**
Exact `Fraction` covariance, `M₁>0` verified n≤50 (`wlambda_covariance_epic_M1_kerov_clt_leading_kappa.py`).
Extend to `(C/κ)²` once `C` is explicit.

## 3. In-repo assets already built (reusable)

- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean` — carrier.
- Exact facts (Lean-formalizable): `Σh = Σ_uD(u)² + Σ|c|`; `β₃ = (n−2)/(n+1)`;
  `ΣD²(μ)−ΣD²(λ) = 2(d_a−d_r+1)`; 1-Lipschitz `|D(u+1)−D(u)|≤1`.
- Probes: `wlambda_covariance_epic_M1_{kappa_analytic_IO, fulman_exchangeable_pair, edge_ratio_structure, IO_mode_decomposition, kerov_clt_leading_kappa}.py`.
- Audits: the three `2026-08-21-covariance-kernel-M1-*.md`.

## 4. Effort / risk

- **Effort:** substantial. Sub-result (1) (Śniady genus-1) is the load-bearing computation — doable
  from the in-corpus paper, several hours; making `C` *explicit* (not just `O(n²)`) is the part most
  likely to balloon.
- **Risk `M₁>0` is false:** very low (κ>0 proved, exact to n≤50).
- **Risk a clean explicit `C` is hard:** moderate. Fallback: non-effective `M₁ ≥ κn^{5/2}(1−o(1))`
  proves it for `n ≥ n₀` with `n₀` non-explicit ⇒ "all but finitely many, verified up to X".
- **Best first step:** extract Śniady §4.5's genus-1 correction to the `Cov(Σc²,ω₃)`-family
  (self-contained), to see whether the `n²` constant is tractable before the harder piece (2).

## 5. Discipline notes

Pure structure/formalization — nothing touches production, no fit, `L2` untouched. The two arxiv
sources are verified genuine in-corpus documents (anti-fabrication). Any Lean lands sorry-free or as a
cited-`sorry` conditional per the repo's zero-sorry-default rules.
