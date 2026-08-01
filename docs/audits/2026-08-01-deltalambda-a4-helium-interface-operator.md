# A=4 (⁴He) magnitude via the interface operator + s5-so3 geometric W_λ: BRACKETED, not closed — WALL(scope-(a))

**Date:** 2026-08-01
**Branch:** `claude/deltalambda-a4-helium-interface-operator-2026-08-01`
**Scope:** Option-E PROBE 2 (A=4 interface operator + `conj:s5-so3-fiber-action`), forward, 0-fit.
**Verdict:** **WALL(scope-(a))** — the s5-so3 geometric W_λ reweighting *brackets* both AME A=4 targets but hits neither, and the normalized-measure bound does **not** exclude the target (so it is **not** a scope-(b) exclusion). `free_parameters = 0`; nothing wired; μ₄/B(⁴He) never inverted.

## Motivation

#4378 (`HeliumBrunnianDeficitMeasured`) measured `τ_L₄ ≈ 1.000146 > 1` for the genuine
4-component Brunnian link `w₄ = [[A₀₁,A₁₂],A₂₃]`, so `c₄ = E₀·(1 − τ_L₄) < 0` is
**sign-compatible** with the derived `μ₄ = −4.591 < 0`. The Route-3 sign wall's antecedent
(`τ_L₄ ≤ 1`) is measured **false**; the A=4 **sign** is settled and the **magnitude** became
the live, open test (option-e ledger, 2026-07-26). This attacks that magnitude via the
interface operator + s5-so3 fiber action — the one A=4 route the ledger flags as
"reopened", and genuinely different territory from A=3 (which is now completely bracketed).

## The forward object (0-fit)

The `S₅ ↔ SO(3)` fiber action (`conj:s5-so3-fiber-action`) supplies the color-tube weight
`W_λ` over the ⁴He Wedderburn blocks (`λ ⊢ 12`), **normalized to `Σ_λ W_λ = 1`**
(`inter-nucleon-channel-color-tube.md`). The genuine geometric (Beasley–Witten /
WRT(S³/2I)) measure is `W_geom_λ = d_q(λ)²/D²`, `D² = Σ d_q²` (C1: `Σ W_geom = 1`, "NOT
`[n]_q!`" — `WLambdaMTCLocalizationObligation.lean`). This is the **identical** measure
#4392 forward-evaluated for A=3 (where it OVERSHOT μ₃ by ~30×).

Reweighting is done on the **canonical b0vf ⁴He `H₁₂` per-block character table**
(`chi-helium-4-h12-at-q0-50dps.witness.json`, 77 partitions of 12, colour-weighted
averaged-crossing convention, `tr_M = Σ y_λ χ_λ = 0.0553584`). Only the weight system is
changed (`y_λ → W_geom`); `χ_λ`, `q₀`, the word are the production table. No recompute.

Constants: `q₀ ≈ 1.1099786`, `E₀ = m_e/(q₀(q₀−1)) ≈ 4.18598 MeV` (same E₀ as ρ_F/#4392),
`max_λ|χ_λ| = 63.62` at `λ=(6,3,3)`.

## Result (forward, 0-fit; targets B(⁴He)=28.29566, |μ₄|=4.591 never inverted)

| object | value (MeV) | ×B(⁴He) | ×|μ₄| |
|---|---|---|---|
| production `E₀·Σ y_λ|χ_λ|` (undershoot) | `0.24275` | `0.0086` | `0.053` |
| geometric `E₀·Σ W_geom_λ|χ_λ|` (**overshoot**) | `60.32647` | `2.132` | `13.14` |
| normalized-W bound `E₀·max_λ|χ_λ|` | `266.3285` | `9.412` | `58.01` |

- `r_geom = (Σ W_geom|χ|)/(Σ y|χ|) = 248.5` (A=3 analog was 47.4, #4392) — the geometric
  measure concentrates on the super-exponentially large `d_q²` middle blocks even more
  strongly at `n=12`.
- Signed-sum diagnostics (not the canonical cluster form): `E₀·|Σ W_geom χ| = 7.49 MeV`
  (= 1.63× |μ₄|), `E₀·|Σ W χ sgn| = 0.555`, `E₀·|Σ W χ sgn·dim| = 7719` (272× B(⁴He)).
  These span 3+ orders of magnitude across natural character forms — none is a landing.

## Reading — WALL(scope-(a)), not (b)

The two canonical 0-fit reweightings **bracket** both AME targets:
`0.243 < 4.591 < 60.33` and `0.243 < 28.296 < 60.33` — production undershoots, geometric
overshoots — but **neither equals a target**. The normalized-measure bound
`E₀·max|χ| = 266 MeV` lies **above** both targets, so the target is **reachable in
principle by some normalized `W`**: this is **NOT a scope-(b) structural exclusion**. An
*exact* hit requires an intermediate weight between production and geometric that is not
fixed by either canonical form — a **tuned weight = FIT**, declined. So the s5-so3
interface operator does **not** supply the A=4 magnitude as-is (this construction alone).

This mirrors the completely-bracketed A=3 magnitude: the geometric W_λ overshoots there
too (#4392), and the missing structure is a *coefficient* the canonical measures do not
pin. The pre-existing `a4_option_e_color_tube_closure.py` applies an ad-hoc `10³`
"color-tube scale" chosen to land on AME — that is a **FIT** and is **not** used here.

## Formalization (lean-direct exit 0, sorry-free, v4.24.0)

`QOU/MassTheory/GeometricWLambdaA4Helium.lean`:

- `normalized_reweight_abs_le_bound` — the structural invariant: `Σ W_i = 1`, `W_i ≥ 0`,
  `|x_i| ≤ B` ⇒ `|Σ W_i x_i| ≤ B` (a normalized reweighting is a weighted average, bounded
  by the max block). This is why the s5-so3 magnitude is bounded by `E₀·max_λ|χ_λ|`.
- `bracket_B4He`, `bracket_absMu4` — both targets sit strictly between the production and
  geometric 0-fit endpoints.
- `geom_ne_targets`, `prod_ne_targets` — neither canonical endpoint equals a target.
- `targets_within_bound` — `t < E₀·max|χ|` for both targets ⇒ not excluded (not (b)).
- `a4_magnitude_bracketed_not_closed_not_excluded` (capstone) — bracket ∧ no-closure ∧
  not-excluded for both targets.

Base ring `ℝ` (§7c: archimedean ordering/`abs`). No `μ₄`/`B(⁴He)` in any proof term as a
derived quantity — they appear only as `def` targets in the ordering facts.

## Artifacts

- Probe: `computations/deltalambda/s5so3_geometric_wlambda_a4_helium_probe.py`
- Witness: `computations/deltalambda/s5so3-geometric-wlambda-a4-helium.witness.json`
- Lean: `content/quantum-observable-universe/lean/QOU/MassTheory/GeometricWLambdaA4Helium.lean`
- Input cache (unchanged): `computations/chi-helium-4-h12-at-q0-50dps.witness.json` (bean b0vf)

## Open (bean)

The A=4 magnitude remains **open**: neither the bare Brunnian-deficit cluster (79× short
at cabled H₁₂, #4378) nor the s5-so3 geometric reweighting (2.1× over at H₁₂, this work)
supplies it 0-fit. The target is *reachable in span* — the missing object is a **derived**
weight between production and geometric, or a derived per-block coefficient. Not a fit.
