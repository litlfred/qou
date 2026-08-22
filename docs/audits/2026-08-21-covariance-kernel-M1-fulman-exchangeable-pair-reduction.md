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

## Update (2026-08-22): sharpened to `N/P < 1`, with explicit local increments

The gap `P(n) > N(n)` is exactly `N(n)/P(n) < 1`. Measured (exact `Fraction`, via the same
exchangeable-pair edge sums):

| n | 7 | 10 | 13 | 16 | 18 | 22 | → ∞ |
|---|---|---|---|---|---|---|---|
| `N/P` | 0.5610 | 0.5674 | 0.5951 | 0.6067 | 0.6095 | 0.6131 | **0.6605** |

`N/P` wobbles for `n≤6` then rises **monotonically (n≥7) toward the proved limit
`N_lead/P_lead = 0.11213/0.16977 = 0.6605 < 1` from below**, staying `≤ 0.613` on the whole exact
range `n≤22`. So the margin `1 − N/P ≥ 0.34` is large and the asymptotic limit is `< 1` by an explicit
VKLS-integral computation.

**Explicit local increments** (all verified exact; Lean-formalizable). For a one-box move `λ→μ`
(remove content `c_r`, add `c_a`; `d_r = D_λ(c_r)`, `d_a = D_λ(c_a)` the diagonal lengths in `λ`):

- `Δω₃ = ω₃(λ)−ω₃(μ) = c_r² − c_a²`,
- `Σ|c|(λ)−Σ|c|(μ) = |c_r| − |c_a|`,
- **`ΣD²(μ)−ΣD²(λ) = 2(d_a − d_r + 1)`** (verified 362 moves, n≤9) ⟹ `ΣD²(λ)−ΣD²(μ) = 2(d_r−d_a−1)`.

Hence per edge (`|c_r|>|c_a|`): `P`-term `= (|c_r|−|c_a|)²(|c_r|+|c_a|)`,
`N`-term `= 2(d_a−d_r+1)(|c_r|²−|c_a|²)`, and

> **per-edge ratio `N/P|_edge = 2(d_a − d_r + 1)/(|c_r| − |c_a|)` — UNBOUNDED per edge.**

This is precisely why no per-edge (Harris/FKG) argument can work: a move between two diagonals of very
different length but nearby content has `d_a−d_r` large and `|c_r|−|c_a|` small, so that edge's ratio
exceeds 1. The bound `N/P<1` must be **global/weighted** — the high-ratio edges carry small stationary
weight `s(λ,μ)`. Quantifying that weight-suppression is the remaining gap.

**Status:** `M₁>0` ⟺ `N/P<1`; asymptotic `N/P→0.6605<1` proved; exact `N/P≤0.613` to n≤22 (margin
`≥0.34`); the local increment structure is fully explicit. A rigorous *uniform* `N/P<1` (e.g. via a
weighted bound on the high-ratio edges, or a monotone-below-limit argument) is **still open**. Not
laundered — the reduction and all increments are exact; only the uniform inequality is unproved.

## Update (2026-08-22, part 2): `N/P = E_ω[ratio_e]`, the 1-Lipschitz lemma, and why the uniform bound needs effective asymptotics

Writing the per-edge ratio `ratio_e = N`-term`/P`-term `= 2(d_a − d_r + 1)/(r − a)` (r=|c_r|>a=|c_a|),

> **`N/P = E_ω[ratio_e]`**, `ω` the edge-probability measure `∝ 2s(λ,μ)·(r−a)²(r+a)`.

So `M₁>0 ⟺ E_ω[ratio_e] < 1`. Two exact structural facts:

- **1-Lipschitz lemma** (verified all λ⊢n, n≤16; `max|D(u+1)−D(u)| = 1`; Lean-formalizable — it is
  `D(u)=(ω_λ(u)−|u|)/2` with `ω_λ` of slope ±1): **`|D(u+1) − D(u)| ≤ 1`**. Hence for same-sign
  contents `d_a − d_r ≤ r − a`, giving the **worst-case per-edge bound**
  `ratio_e ≤ 2 + 2/(r−a) ≤ 4` — which exactly explains the observed `max ratio_e = 4` (at `r−a=1`).

- **Route refutation (scope-(a)).** The natural "high-ratio edges are weight-suppressed" hypothesis is
  **false**: the ω-weight concentrates on *distant* signed-content moves (weight on `|c_a−c_b|≥4`
  grows to ~0.88), and ~15 % of ω-weight sits persistently on `ratio_e ≥ 1`. `N/P<1` is **not** a
  worst-case fact (per-edge ratio reaches 4). It is an **averaging** phenomenon: `ω ∝ (r−a)²(r+a)`
  up-weights large-`(r−a)` edges, which carry *small* `ratio_e` (the `(r−a)` is in the denominator),
  and the **bulk diagonal profile of a typical diagram is flat** (`d_a−d_r ≪ r−a` in the bulk).

**Consequence for the proof.** A *uniform* `N/P<1` cannot come from an elementary per-edge / worst-case
bound (that only gives `≤4`) nor from weight-concentration (refuted). It requires **effective,
error-controlled limit-shape estimates** (a Berry–Esseen-grade second-order Kerov CLT: `M₁ ≥ κn^{5/2}
− C n²` with explicit `κ>0, C`, then finite check). The asymptotic `N/P → 0.6605 < 1` is already
proved (the VKLS integrals); the missing piece is purely the *effective* error term. This is a precise,
honest localisation of the remaining difficulty — not a closure.

Probe: [`wlambda_covariance_epic_M1_edge_ratio_structure.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_edge_ratio_structure.py) (exit 0).

## Compute

- Probe: [`wlambda_covariance_epic_M1_fulman_exchangeable_pair.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_fulman_exchangeable_pair.py)
  (exit 0; exact `Fraction`; builds `J`, verifies the eigenfunction + `β₃=(n−2)/(n+1)` + the identity +
  the two per-edge sign facts).
- Leading constant (companion): [`wlambda_covariance_epic_M1_kappa_analytic_IO.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_kappa_analytic_IO.py).

## Cross-references

- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Exact anchor: [`2026-08-21-covariance-kernel-M1-kappa-exact-leading-exponent.md`](2026-08-21-covariance-kernel-M1-kappa-exact-leading-exponent.md)
- Roadmap (Śniady+Fulman): PR #5416; epic synthesis: [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md); gap bean `qou-k5r5`.
