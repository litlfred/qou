# The electron's categorical weight: additivity forces the log of its trace

**Date:** 2026-11-27 · **Branch:** `claude/electron-categorical-weight-2026-11-27`
**Beans:** `qou-91w7` (𝔈 → MeV), the energy-scale bean of the L2 1-ppQ work; feeds the radius factor `D`
(`docs/audits/2026-11-27-energy-length-radius-routes.md` §8–9).
**Lean:** `QOU/Observations/ElectronWeightAdditivity.lean` (ordered field, no `Real.log`),
`QOU/Transcendental/MassTheory/ElectronCategoricalEnergy.lean` (uses `Real.log` and one limit).
**Probe:** `computations/probes/electron_weight/electron_log_weight_probe.py` (mpmath 50 dps, 5/5).

## 1. Question

Which electron weight sets the energy unit? Two candidates were on record, and neither was chosen:

| candidate | status before this note | `D` (β-gap) |
|---|---|---|
| `ℏ_q²` (mass formula) | placed by hand: the formula's own rule gives the electron `0` (`product_weight_ne`) | 13.19 |
| `τ_e = q³ y₍₃₎` (trace of `σ₀σ₁σ₀`) | derived (#9645) | 110.7 |

Both are used as **linear** weights: `m(X) = Λ·w(X)`, so `Λ = m_e/w_e`.

## 2. Result

Neither linear weight is consistent. The derived categorical energy of the electron is

  **𝔈_e = −log_q τ_e = −3 + 𝔈(y₍₃₎)**

(the dictionary energy of its trace: writhe plus the one-row block). Once CAL-1 is imposed, every trace-derived energy is

  **E(y) = m_e · ln y / ln τ_e**,

and nothing is left to choose: no unit Λ, no "multiple of `E₀`", no `ln q`.

### The argument (premises are the corpus's own)

1. The convention-D trace is multiplicative on disjoint strand sets (`SpectatorEnergyMap.trace_kron`).
2. Energy is additive over non-interacting parts. The corpus already uses this to derive spectator invariance (`spectator_of_additive`).
3. **A linear chart breaks (2).** Two disjoint electrons have trace `τ_e²` and mass `2m_e`. `Λτ_e² = 2Λτ_e` holds only if `τ_e = 2` (`linear_chart_additive_iff`). But `τ_e < 1` on `1 ≤ q ≤ 6/5` (`tauE_lt_one`), so the linear trace chart is not additive there (`linear_trace_chart_not_additive`). The mass-formula weight `ℏ_q²` is not the value of any rule (#8 of the 2026-11-22 audit). So neither candidate survives as a linear weight.
4. **Additivity and continuity force the logarithm, with no constant** (`additive_eq_log`). Spectator invariance alone leaves `c·log + d`, and then CAL-1 cannot fix both `c` and `d`. Additivity gives `Φ(1) = 0`, so the empty diagram has energy 0 and `d = 0`.
5. **CAL-1 then fixes `c` uniquely** (`cal1_unique`, with existence from `derived_map_additive`, `derived_map_cal1`): `c = m_e / ln τ_e`.
6. In the `β = ln q` dictionary this is the audit-2026-11-22 `calMap` `Φ(𝔈) = m_e·𝔈/𝔈_e` with `𝔈_e = −log_q τ_e` (`derived_dictionary_form`). The `ln q` cancels.

### Consequences proved

- **Sign.** On `1 < q ≤ 6/5` the per-nat unit `c` is negative (`derived_unit_neg`). So the n–p log cell puts the neutron above the proton (`derived_cell_pos`). This sign is an output: it was required independently (`log_cell_pos_iff`) and was not imposed. The cell is `2 m_e ln q / (−ln τ_e)` (`derived_cell_eq`).
- **Multiple of `E₀`.** `|c| = E₀ · q(q−1)/(−ln τ_e)` (`derived_unit_eq_mul_e0`). This is a derived function of `q`, not a chosen constant.
- **Classical limit.** `|c|/m_e → 1/ln 2` (`derived_unit_classical_limit`). At `q = 1` the electron's mass is `|c|·ln 2`, one bit at the derived temperature. `E₀` has a pole at `q = 1`, but this unit is finite there.

## 3. Numbers at `q₀` (proton pin)

| quantity | value |
|---|---|
| `τ_e` | 0.691166478 |
| `𝔈_e = −log_q τ_e` | 3.540081 |
| per-nat unit `|c|/m_e = 1/(−ln τ_e)` | 2.707279 |
| `|c|/E₀` | **0.330488** |

The unit gaps of the radius audit, recomputed. The first two rows are the old candidates and are shown only for comparison:

| gap | unit per nat | gap / m_e | `D` |
|---|---|---|---|
| β-dictionary `ln([4]/[2])` | `E₀` (`ℏ_q²`) | 5.855 | 13.19 |
| | `E₀/R` (linear `τ_e`) | 0.0832 | 110.7 |
| | **derived `1/(−ln τ_e)`** | **1.935** | **22.95** |
| Casimir `C`, read per nat | `E₀` | 24.93 | 6.39 |
| | `E₀/R` | 0.354 | 53.6 |
| | **derived** | **8.240** | **11.12** |

The Casimir row assumes, as #9708 did, that a Casimir eigenvalue is an energy per nat. That reading is not derived here. Only the β-dictionary row is a trace-derived energy in the sense of §2.

## 4. Comparison boundary (data enters only here)

| | derived unit | measured |
|---|---|---|
| β-gap | 0.989 MeV | Δ − N ≈ 293 MeV |
| β-gap `r_rms` | 4.83 fm | 0.841 fm |
| Casimir `r_rms` | 2.34 fm | 0.841 fm |
| n–p cell | 0.289 MeV | 1.293 MeV |

**Scope (a).** The derived unit does not close the radius or the n–p splitting. Its errors are larger than those of the hand-placed `E₀` for every row, and that comparison is reported, not acted on. The unit was fixed by additivity and CAL-1 before these numbers were computed. Choosing `E₀` back because it is closer would be selection against the target.

## 5. What this settles and what it does not

- **Settled (given the corpus premises 1–2):** for any energy read from Hecke/trace weights, the electron's weight is `−ln τ_e`, and the energy unit is not a free choice. The "which multiple of `E₀`" question of `SpectatorEnergyMap` has the answer `q(q−1)/(−ln τ_e)`.
- **Not settled:** the mass-formula chart `m_e·Vol·ρ/ℏ_q²`. It is additive (volume adds), but its electron weight is still placed by hand. The muon carrier lives there. In the log chart, every finite-trace mass ratio `ln τ_X / ln τ_e` has a finite limit at `q = 1`, so the carrier's `1/ℏ_q²` pole still needs a transcendental object, in agreement with #9692.
- **Not settled:** whether a Casimir eigenvalue is an energy per nat or per q-step. That needs its own derivation before the Casimir route uses this unit.
- **Not adopted.** Nothing is wired into the mass table or the radius pipeline. Wiring the derived unit is an owner decision.

## 7. The electron's weight on the mass-formula scale (added the same day)

Lean: `QOU/Observations/ElectronMassChartWeight.lean` (generic field), `QOU/Transcendental/MassTheory/ElectronMassChartWeight.lean`. Probe: `computations/probes/electron_weight/electron_mass_chart_weight_probe.py` (5/5).

**The mass formula's own rule.** §2's uniqueness covers maps that depend on the trace *value*. The mass formula does not: its muon weight is `G = q∂_q log P` (#9692), a derivative. Derivatives of `log` are also additive (`energyReading_mul`, Leibniz), so the additive local readings are `(q∂_q)^k log Z`. The order `k` is fixed by the pole:

- `hbar_pole_raise`: `q∂_q ℏ_q⁻ⁿ = −n q⁻¹ ℏ_q^{−(n+1)}`. Each `q∂_q` raises the pole at `q = 1` by exactly one.
- `log P ~ −Li₂/ℏ_q` has order 1, and the carrier `Vol/ℏ_q²` has order 2. So `k = 1`.
- `k = 0` is §2's value chart. It gives finite ratios at `q = 1`, so it cannot carry the muon.

**The electron, by the same rule** (`electron_energy_reading`, `q_mul_dTauE`):

  **w_e(q) = q∂_q log τ_e = 3 + 4q²(q²−1)/((q⁴+1)(q²+1))**, with `w_e(1) = 3` (writhe) and `w_e(q⁻¹) = 6 − w_e(q)`.

This replaces the hand-placed weight `1` of the unit `m_e/ℏ_q²`. With CAL-1 the mass-chart unit is `m_e/w_e(q)`, so the formula reads `m(K) = m_e·Vol(K)·ρ(K)/(ℏ_q²·w_e(q))`.

**Two charts, two rules, no conflict.** The β-dictionary energies (radius gaps, log binding law) are `k = 0` readings and use §2's unit. Masses on the mass-formula scale are `k = 1` readings and use `m_e/w_e`. Each unit is fixed by CAL-1 within its own chart. Neither is placed by hand any more.

**n–p cell in the mass chart** (`np_cell_energy_reading`, `hasDerivAt_inv_sq_mul`). With `ε_n = q⁻²ε_p`, the two readings differ by exactly `−2` for any `ε_p`. So the cell is `2/w_e(q)` electron masses: 0.6243 m_e at q₀, and `2/3` at `q = 1`.

| at q₀ (proton pin) | value |
|---|---|
| `w_e(q₀)` | 3.203481 (hand-placed: 1) |
| `W_μ = 2 Im G` | 207.2446 |
| `m_μ/m_e = W_μ/w_e` | 64.694 |
| n–p cell | 0.6243 m_e |

**Comparison boundary.**
- `m_μ/m_e` is 64.69 against 206.77 (0.313×). This is #9692's "Vol/3", now with the exact `w_e(q₀)`.
- The n–p cell is 0.319 MeV against 1.293 MeV (4.05× short).
- CAL-2 defines q₀ through the carrier with the hand-placed weight. If CAL-2 were re-solved with `w_e`, then `W_μ(q)/w_e(q) = m_μ/m_e` gives **q₀' = 1.059529** (ℏ = 0.05618, against q₀ = 1.109979, ℏ = 0.09908). This is computed for comparison only and **not adopted**: re-solving q₀ moves every number in the corpus and is an owner decision.

**Scope.** Given the corpus's own premises (additivity; the carrier's `ℏ_q⁻²` order), the electron's mass-chart weight is derived, not placed. What this does not do: say why the carrier's coefficient should be `Vol` and not `Vol/w_e(1) = Vol/3`. That question returns to CAL-2's definition of q₀.
