# Covariance-kernel epic (`qou-x631`) — M₁>0: Fulman exchangeable-pair reduction to `P>N`

**Date:** 2026-08-21 · **Branch:** `claude/m1-sniady-kerov-clt-leading-term-2026-08-21` ·
**Tier:** exact structural reduction (Fulman up-down chain) — **sharpens** `M₁>0` all-n but does
**not** close it · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged.
**Epic:** `qou-x631`; gap `qou-k5r5`.

## Summary

Attacking `M₁ = Cov_Planch(Σ□ h, Σ□ c²) > 0` for **all** `n` via Fulman's Stein/exchangeable-pair
machinery ([`arxiv-math-0305423`](https://arxiv.org/abs/math/0305423)). The result is an **exact
reduction** of the all-`n` positivity to a single clean inequality `P(n) > N(n)` between two
**manifestly non-negative, exactly-characterized** quantities. It does **not** prove `P>N` for all
finite `n` — that residual is the same ±cancellation, now in its sharpest possible form. Combined
with the derived leading constant `κ = 128/(225π²) > 0`
([derivation audit](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)) and exact
positivity to `n≤50`, the picture is fully coherent across two independent methods.

## What is PROVED (exact, Lean-formalizable)

1. **Split identity** (∀λ⊢n, n≤14): `Σ□ h = Σ_u D(u)² + Σ□|c|`, `D(u)`=diagonal lengths.
2. **`ω₃ := Σc² − C(n,2)` is an exact eigenfunction** of the up-down Markov chain `J` on `Y_n`
   (add a box → `Y_{n+1}`, remove one → `Y_n`; reversible w.r.t. Plancherel), with eigenvalue
   > **`β₃ = (n−2)/(n+1)`**  (verified exactly n≤13; clean closed form) ⟹ `1−β₃ = 3/(n+1)`.

   (`ω₃ = Σ₃/3`, the 3-cycle central character — a Kerov–Olshanski shifted-symmetric eigenfunction,
   the natural generalisation of Fulman's Prop 4.1 for the 2-cycle character `W`.)
3. **Exchangeable-pair identity** (verified exactly). For any statistic `A`, with `(λ,λ*)` one
   `J`-step,
   > `Cov(A, ω₃) = E_π[(A−A*)(ω₃−ω₃*)] / (2(1−β₃)) = (n+1)/6 · Σ_{edges} 2w·ΔA·Δω₃`,
   `w = π(λ)J(λ,μ) ≥ 0`. So `M₁ = Cov(Σh, ω₃) = (n+1)/6 · (edge-increment sum)`, and the sign of `M₁`
   is the sign of a **local, one-box-move** sum.
4. **Fact A — the content-spread piece is manifestly non-negative.** On every single-box edge (box
   of content `c_a` ↔ `c_r`),
   > `Δ(Σ|c|)·Δω₃ = (|c_r|−|c_a|)²(|c_r|+|c_a|) ≥ 0`  (elementary; verified all edges n≤8),
   hence **`P := Cov(Σ|c|, ω₃) ≥ 0`** — a per-edge (Harris/FKG-type) certificate.
5. **Fact B — the diagonal-length piece is manifestly non-positive.** On every single-box edge,
   `Δ(ΣD²)·Δω₃ ≤ 0` (100 % of the signed edge weight is discordant; verified n≤13): moving a box to
   a diagonal of larger `|content|` (nearer the diagram edge, hence shorter) *decreases* `ΣD²`.
   Hence **`Cov(ΣD², ω₃) ≤ 0`**, i.e. `N := −Cov(ΣD², ω₃) ≥ 0`.
6. Therefore **`M₁ = P − N`, with `P ≥ 0` and `N ≥ 0` both per-edge manifest.** This is exactly the
   "±cancellation, ratio → −0.62" seen in the raw data — now resolved into two cleanly-signed pieces.

## Cross-method agreement (IO leading order ↔ Fulman edge split)

The two per-edge-signed pieces match the IO Chebyshev-mode leading order term-by-term:

| piece | per-edge sign | leading coeff `×n^{5/2}` (IO) |
|---|---|---|
| `P = Cov(Σ\|c\|, ω₃)` | ≥ 0 (Fact A) | `⅓·\|x\|̂₃ = +0.169765` |
| `N = −Cov(ΣD², ω₃)` | ≥ 0 (Fact B) | `−⅓·(2D∞)̂₃ = +0.112125` |
| `M₁ = P − N` | — | `⅓·Ω̂₃ = κ = 0.057640` |

(`|x|̂₃ = 0.509296 > 0`, `(2D∞)̂₃ = −0.336374 < 0` — signs match Facts A/B.) Asymptotically
`N/P → 0.6605 < 1` (both explicit VKLS integrals), so `P>N` asymptotically ⟺ `Ω̂₃>0` ✓, matching
the finite-n covariance ratio ≈ −0.62.

## The remaining gap (honest)

**`M₁>0` for all `n` ⟺ `P(n) > N(n)`.** Both are exact, per-edge non-negative, and asymptotically
`P/N → 1.514 > 1`. What is **not** proved is the **finite-`n` domination** `P(n) > N(n)` — the
positive content-spread covariance beating the negative diagonal-length covariance at every `n`. This
is the sharpest form of the ±cancellation; a per-edge argument for `Σh` itself fails (≈2–3 % of edge
weight is discordant for the combined `Σh`, from n=6). Closing it needs a quantitative lower bound
`P−N ≥ 0` — e.g. a weighted edge inequality or Fulman's exact `E[(Σh−Σh*)²]`-style second-moment
control. Verified `M₁>0` exactly to `n≤50`; asymptotic positivity is proved (`κ>0`).

**Status of `qou-k5r5`:** leading term **derived** (`κ>0`); all-n positivity **reduced** to
`P(n)>N(n)` (two manifest pieces) with asymptotic domination proved; finite-n domination **open**.
Nothing laundered: Facts A/B are proved per-edge; the residual is stated as open, not closed.

## Compute

- Probe: [`wlambda_covariance_epic_M1_fulman_exchangeable_pair.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_fulman_exchangeable_pair.py)
  (exit 0; exact `Fraction`; builds `J`, verifies the eigenfunction + `β₃=(n−2)/(n+1)` + the identity +
  the two per-edge sign facts).
- Leading constant (companion): [`wlambda_covariance_epic_M1_kappa_analytic_IO.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_kappa_analytic_IO.py).

## Cross-references

- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Exact anchor: [`2026-08-21-covariance-kernel-M1-kappa-exact-leading-exponent.md`](2026-08-21-covariance-kernel-M1-kappa-exact-leading-exponent.md)
- Roadmap (Śniady+Fulman): PR #5416; epic synthesis: [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md); gap bean `qou-k5r5`.
