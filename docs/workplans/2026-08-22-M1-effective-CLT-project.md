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

### Sub-result (1) — the `Λ*` side. **CLOSED 2026-08-22 — vanishes exactly.**
Outcome (better than planned; [audit](../audits/2026-08-22-covariance-kernel-M1-lambda-star-orthogonality.md)):
decomposing `Σh = p₂^#_sym + T` (with `p₂^#_sym ∈ Λ*` the shifted-power part and `T = Σ□(i+j)−n`
the non-`Λ*` co-content statistic), **`Cov(p₂^#_sym, ω₃) = 0` exactly** — because `p₂^#_sym` is
`Λ*`-degree 2 and `Cov(Σ₂, Σ₃) = 0` (= the exact `Cov(R₃,R₄)=0`; `ω₃ = Σ₃/3`). Hence
**`M₁ = Cov(T, ω₃)` exactly** (n≤11), proving the PR #5366 antidiagonal reformulation exact. **No
Śniady genus computation is needed** — there is no integer-power `Λ*` contamination term; the whole
`n^{5/2}` leader lives in the single non-`Λ*` statistic `T`. Probe:
`computations/deltalambda/wlambda_covariance_epic_M1_sniady_lambda_star_orthogonality.py`.

> Note: Śniady `arxiv-math-0411647` §4.5 (genus expansion) would only have re-derived `Λ*`×`Λ*`
> covariances (already exact here); it does not reach the non-`Λ*` `T`. So the effort moves directly
> to sub-result (2), now the *sole* remaining piece.

> **REFRAMED 2026-08-22 → one-sided; no explicit `C` needed**
> ([audit](../audits/2026-08-22-covariance-kernel-M1-onesided-reframing.md)). Exact `κ_n = M₁/n^{5/2}`
> satisfies `κ_n < κ` for `n ≤ 12` and **`κ_n > κ` for every `13 ≤ n ≤ 46`** (crossing `n₀ = 13`). So
> `M₁>0` all-n ⟸ **(a)** exact `M₁>0` for `n ≤ 12` (done) **∧ (b)** `κ_n ≥ κ` for `n ≥ 13`, i.e.
> `Cov(T,ω₃) ≥ κn^{5/2}` — the **sign** of the correction (`κ_n → κ` from above), not an explicit
> `C`. Sub-result (2) below is now exactly part (b): the one-sided sign.

### Sub-result (2) — the non-`Λ*` piece (`Σh`'s deviation from `n∫Ω dΔ`); now the ONE-SIDED sign of part (b).
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
