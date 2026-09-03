# Covariance-kernel epic (`qou-x631`) — M₁>0 reduces to a MARGIN-RICH bound (not the delicate rate)

**Date:** 2026-08-28 · **Branch:** `claude/m1-cauchy-schwarz-margin-reduction-2026-08-28` · **Tier:**
structural reduction (scope-(a); softens the target — no proof of the reduced condition) ·
**Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap
`qou-k5r5`.

## The reframing: the sign is NOT knife-edge

The arc framed `M₁>0` as needing the sign of the finite-n correction `κ_n − κ` — a *delicate rate*
whose margin vanishes in the exponent (measured effective exponent still rising at n≤67). **The Fulman
P−N split shows the positivity is instead robust.** With (all exact, on `main`):

- `P = Cov_Planch(Σ|c|, ω₃) ≥ 0`, `N = −Cov_Planch(ΣD², ω₃) ≥ 0`, `D(u)` = diagonal lengths,
- `Σh = ΣD² + Σ|c|` (exact) ⟹ `M₁ = Cov(Σh, ω₃) = P − N`,

the exact ratio is `N/P ≈ 0.55 → 0.66` (limit `N_lead/P_lead = 0.112125/0.169765 = 0.6605`), i.e.
**`M₁ = P·(1 − N/P) ≈ 0.34·P`, a robust positive with margin `1−N/P ≈ 0.37`.** The corpus's "delicate
/ partial cancellation of two `~n^{5/2}` terms" framing is misleading — the two terms do **not** nearly
cancel (`N` is ~2/3 of `P`, not ~`P`).

## The Cauchy–Schwarz sufficient condition (airtight)

Write each covariance as correlation × std × std, sharing `σ_W = σ(ω₃)`:

- `P = ρ_P · σ_A · σ_W`, `ρ_P = corr(Σ|c|, ω₃)`, `σ_A = σ(Σ|c|)`;
- `N = ρ_N · σ_D · σ_W`, `ρ_N = |corr(ΣD², ω₃)| ≤ 1`, `σ_D = σ(ΣD²)`.

`M₁ > 0 ⟺ N < P ⟺ ρ_N σ_D < ρ_P σ_A` (the common `σ_W` cancels). Cauchy–Schwarz gives `ρ_N ≤ 1` for
free, so `N ≤ σ_D σ_W`, yielding the clean **sufficient condition** (C-S on `N`, exact on `P`):

> **(CS)  `σ(ΣD²) / σ(Σ|c|) < ρ(Σ|c|, ω₃)`  ⟹  `M₁ > 0`.**

Measured exactly (`Fraction`; `wlambda_covariance_epic_M1_cauchy_schwarz_margin.py`, exit 0, NO
float64), for every `4 ≤ n ≤ 32`:

| ingredient | value | trend |
|---|---|---|
| `σ(ΣD²)/σ(Σ|c|)` | `≈ 0.65 – 0.68` | stable, `< 1` with margin `≈ 0.33` |
| `ρ(Σ|c|, ω₃)` | `≈ 0.96 – 0.98` | stable, near 1 (`Σ|c|` and `ω₃ = Σc²−C(n,2)` are both content statistics) |
| **(CS) margin** `ρ_P − σ_D/σ_A` | `≈ 0.25 – 0.31` | **does not vanish** |

(CS) holds with a stable `≈ 0.30` margin throughout; `M₁ > 0` confirmed for all `3 ≤ n ≤ 32`.

## Why this is a better target than the rate

The sharp rate `κ_n ≥ κ` needs the *exact leading correction's sign* — margin → 0 in the exponent,
and three literature tools fail to deliver it (genus: `Σh∉A`; Fulman: marginal, not covariance-sign;
Dołęga–Féray: limit not rate). **(CS) needs only two crude, non-vanishing-margin estimates:**

1. **`σ(ΣD²) / σ(Σ|c|) < 1`** — a variance-ratio bound (asymptotically `≈ 0.67`); a crude upper bound
   `< 0.9` suffices.
2. **`ρ(Σ|c|, ω₃) > σ_D/σ_A`** — a lower bound on one correlation (asymptotically `≈ 0.98`, and
   `Σ|c|`, `ω₃` are near-deterministically linked content statistics); a crude lower bound `> 0.9`
   suffices.

A crude bound is provable where a sharp asymptotic is not. This is the softer route the "genuine
analysis project" verdict did not consider.

## Honest scope

- This is a **reduction**, not a proof: (CS) is **verified exact for `n ≤ 32`** and asymptotically
  clear, but **not proved for all n**. `σ_A`, `σ_D`, `ρ_P` involve `Σ|c|` and `ΣD²` — **non-`A`**
  statistics (absolute value / diagonal lengths), so bounding them is still Plancherel asymptotics —
  but now *crude* bounds on variances/one correlation, not the sharp covariance rate.
- Gap `qou-k5r5` stays **OPEN**. Nothing wired; no fit; the reduced condition (CS) is the new,
  softer target.
- Complements — does not contradict — the "bespoke rate" verdict: it offers an alternative that
  **avoids** the rate entirely.

## The strategic point: (CS)'s ingredients are LEADING-order, unlike the rate

The reason the rate `κ_n − κ` resisted all three tools is that it is a **finite-n correction** to a
limiting covariance. **The (CS) ingredients are not** — `σ(Σ|c|)`, `σ(ΣD²)` and `ρ(Σ|c|, ω₃)` are
**leading-order fluctuation quantities** (variances and one correlation), exactly the objects the IO
Kerov CLT delivers — the same machinery that already produced `κ = Ω̂₃/3`. So:

- **(CS) asymptotically is a leading-order IO computation**, not a rate: expand the profile
  representations of `Σ|c|` (a `∫|x|dμ`-type linear statistic) and `ΣD²` in the IO Chebyshev-mode
  basis, read off the two variances and the correlation from the diagonal covariance. The asymptotic
  values (`σ_D/σ_A → ≈0.67`, `ρ_P → ≈0.98`) are leading-order numbers, within reach of the tool that
  works.
- **A leading-order proof of (CS) already almost closes the problem.** Leading-order (CS) gives
  `M₁ > 0` for `n ≥ N₀`; the exact check covers `13 ≤ n < N₀` (verified to **n = 77** and counting).
  If the leading (CS) margin is as robust as measured (`≈0.30`) and `N₀ ≤ 77`, that is a **complete
  proof of `M₁ > 0` for all n** — no rate ever needed.

**Caveat (honest):** `Σ|c|` and `ΣD²` are non-smooth linear statistics (`|x|` has a kink at the
Plancherel content centre; `D(u)` is the diagonal-length representation), so the IO expansion needs
care at the kink — not automatic, but leading-order-CLT territory, not the intractable rate.

## Next

Execute the IO leading-order computation of the two (CS) ingredients: (1) `σ(ΣD²)/σ(Σ|c|)` (asymptotic
`≈0.67`) via the Chebyshev-mode variances, (2) `ρ(Σ|c|, ω₃)` lower bound (asymptotic `≈0.98`). Then find
`N₀` from the exact table (have it to n=77) — if `N₀ ≤ 77`, `M₁ > 0` for all n is **proved** via the
soft route, sidestepping the rate entirely.

## Compute

- [`wlambda_covariance_epic_M1_cauchy_schwarz_margin.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_cauchy_schwarz_margin.py)
  (exit 0; exact `Fraction` covariances/variances; mpmath only for `sqrt`/display; NO float64).

## Cross-references

- Σh ∉ A obstruction / tool survey: [`2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md`](2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md)
- Fulman P−N reduction: [`2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)
- Revised workplan: [`../workplans/2026-08-28-M1-arc-revised-workplan.md`](../workplans/2026-08-28-M1-arc-revised-workplan.md)
- Gap bean `qou-k5r5`.
