# Covariance-kernel epic (`qou-x631`) — M₁ effective-CLT sub-result (1): the `Λ*` part is `ω₃`-orthogonal

**Date:** 2026-08-22 · **Branch:** `claude/m1-effective-clt-project-2026-08-22` · **Tier:** exact
structural result (closes sub-result (1) of the effective-CLT project) · **Discipline:** scope-(a);
no fit; nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Result

Sub-result (1) of the [effective-CLT workplan](../workplans/2026-08-22-M1-effective-CLT-project.md)
asked: what is the shifted-symmetric (`Λ*`) contribution to `M₁ = Cov_Planch(Σ□ h, ω₃)`, and does it
need a Śniady genus computation? Answer: **the `Λ*` part contributes exactly zero.**

Decompose `Σh` through the shifted power sum `p₂^#` (which *is* in `Λ*`):

> `p₂(λ) = Σᵢ λᵢ² = p₂^#(λ) + 2Σᵢ i·λᵢ − n`,  `p₂^#(λ) = Σᵢ λᵢ(λᵢ−2i+1)`  (verified ∀λ, n≤12),

so with `Σh = ½(p₂(λ)+p₂(λ'))`,

> `Σh = p₂^#_sym + T`,  `p₂^#_sym = ½(p₂^#(λ)+p₂^#(λ')) ∈ Λ*`,  `T = Σ□(i+j) − n` (non-`Λ*`).

Then, **exactly for all n≤11**:

> **`Cov(p₂^#_sym, ω₃) = 0`**  ⟹  **`M₁ = Cov(Σh, ω₃) = Cov(T, ω₃)`.**

## Why the `Λ*` part vanishes (provable, not just numeric)

`p₂^#_sym` is a **degree-2** element of `Λ*` — a combination of `Σ₂` (the 2-cycle central character),
`n²`, and `n`. Against `ω₃ = Σ₃/3` (`Σ₃` = 3-cycle central character):

- `Cov_Planch(Σ₂, Σ₃) = 0` — the exact orthogonality of distinct central characters under Plancherel.
  In our free-cumulant coordinates this is precisely the already-verified `Cov(R₃, R₄) = 0`
  (`Σ₂ = R₃`, `Σ₃ = R₄ + R₂`, `R₂ = n` constant).
- `Cov(n², ω₃) = Cov(n, ω₃) = 0` (`n` is deterministic).

So *any* degree-≤2 `Λ*` element is `ω₃`-orthogonal, and `Cov(p₂^#_sym, ω₃) = 0` holds identically — a
degree-0 polynomial in `n`, no genus-1 correction. **Sub-result (1) is closed with no computation to
carry forward.**

## Consequences

1. **The antidiagonal reformulation (PR #5366) is now proved exact:** `M₁ = Cov(Σ□(i+j), Σ□ c²)` (the
   `−n` and `−C(n,2)` constants drop from the covariance). The #5366 probe showed this numerically;
   here it is a consequence of the `Λ*`-orthogonality.
2. **The effective bound refocuses entirely on `T`.** Since `Λ*`×`Λ*` covariances are integer-power
   polynomials in `n` while `M₁ ~ κn^{5/2}` (half-integer), the leader *had* to come from the
   non-`Λ*` part — and now we know the `Λ*` part is not merely lower-order but **identically zero**.
   The target `M₁ ≥ κn^{5/2} − Cn²` therefore needs **only** the effective control of `Cov(T, ω₃)`
   (sub-result (2)); there is no `Λ*` contamination term to bound.
3. `T = Σ□(i+j) − n` and `ω₃ = Σ□(j−i)² − C(n,2)` are both **additive box statistics** (co-content
   `b=i+j` linear; content `c=j−i` quadratic), which is the clean starting form for the sub-result-(2)
   profile-field / Fulman second-moment analysis.

## Compute

- Probe: [`wlambda_covariance_epic_M1_sniady_lambda_star_orthogonality.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_sniady_lambda_star_orthogonality.py)
  (exit 0; exact `Fraction`; identity + `Cov(p₂^#_sym,ω₃)=0` + `M₁=Cov(T,ω₃)` verified).

## Cross-references

- Workplan: [`2026-08-22-M1-effective-CLT-project.md`](../workplans/2026-08-22-M1-effective-CLT-project.md)
- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Fulman reduction: [`2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)
- Gap bean `qou-k5r5`; antidiagonal reformulation PR #5366.
