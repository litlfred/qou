# One scale for masses: the Euler derivative bridges the log chart and the mass chart

**Date:** 2026-11-27 · **Branch:** `claude/energy-scale-bridge-2026-11-27`
**Builds on:** #9718 (log chart, k = 0), #9725 (its wiring), #9733 (mass chart, k = 1, open), #9717 / #9727 (n − p), #9675 (ruled bond letters).
**Lean:** `QOU/Observations/EnergyScaleBridge.lean` (generic ordered field, no `log`),
`QOU/Transcendental/MassTheory/EnergyScaleBridge.lean` (`Real.log`, `HasDerivAt`). Sorry-free; axioms `propext`, `Classical.choice`, `Quot.sound` only.
**Probe:** `computations/probes/energy_scale_bridge/scale_bridge_probe.py` (mpmath 50 dps, 11/11).

## 1. Question

Two CAL-1 charts are on record, and the corpus mixes them:

| chart | reading of a trace weight `τ_X` | CAL-1 unit at q₀ | used for |
|---|---|---|---|
| log, `k = 0` (#9718) | `E₀(X) = m_e · L_X / L_e`, `L = log τ` | `m_e/(−ln τ_e)` = 2.7073 m_e per nat | n − p cell, Δ − N gap → radius `D`, ruled binding law (#9725) |
| mass, `k = 1` (#9692, #9733) | `E₁(X) = m_e · w_X / w_e`, `w = q ∂_q log τ` | `m_e/w_e` = 0.31216 m_e per Euler unit | the mass formula (muon carrier) |

How do they relate, and which one should a mass difference use?

## 2. The bridge (proved)

With `β = ln q`, the Euler operator `δ = q ∂_q` is `∂_β`, and `w = δ L` (`euler_reading_of_log`). So the mass chart is the β-derivative of the log chart. By the quotient rule (`ratio_flow_eq`, `chart_gap`, `chart_gap_real`):

  **E₁(X) − E₀(X) = m_e · (L_e / w_e) · δ(L_X / L_e).**

- The charts agree on `X` exactly when the log-chart ratio `L_X / L_e` is stationary in `q` (`charts_agree_iff`).
- The Legendre partner `S = L − β w` is additive as well (`legendre_additive`). In heat-trace language `L = log Z` and `w = ∂_β log Z`. The log chart reads a free energy, the mass chart reads a mean energy, and `S` is the entropy between them.

**The mass-difference rule.** A binding energy, the n − p split and the Δ − N gap are differences of masses. The masses come from the mass formula, whose rule is `k = 1` (#9692, #9733). So on one scale these differences are `k = 1` readings. Reading them in the log chart while the masses come from the mass chart mixes the charts, which is the reduction #9727 §7 already pointed to.

## 3. The sign theorem (proved)

The electron has `L_e < 0` (`τ_e < 1`, `electron_log_neg`) and `w_e > 0` (#9733: `w_e = 3 + …`). Because these have opposite signs, the two charts disagree in sign on many objects:

- `sign_agree_iff`: `E₀(X)` and `E₁(X)` have the same sign iff `L_X · w_X < 0`, that is, iff `X` behaves like the electron (weight below 1 and rising in `q`, or above 1 and falling).
- `pure_power_sign_flip`: every pure power `q^k`, `k ≠ 0`, gets opposite signs. The ratio is `E₁/E₀ = L_e/(β w_e)` for every `k` (`pure_power_ratio`).
- `np_cell_charts_disagree`: the n − p cell `τ_n = q⁻² τ_p` puts the neutron above the proton in the log chart and **below** it in the mass chart.
- `bond_unbinds_log_chart`, `bond_unbinds_mass_chart`: a bond letter with `f < 1` that grows with `q` adds mass in both charts, so `B = −E(f) < 0`. The ruled letters `z − h/2` and `z + d_pn` are such letters at q₀ (probe).
- `ruled_law_opposite`: the ruled law `B = T·log(tr_free/tr_atom)` with `T > 0` (2026-11-25 ruling) has the opposite sign to the CAL-1 log-chart reading of the same letters. The law is bound because it uses `T = |c| > 0`. The CAL-1 unit itself is `c = m_e/ln τ_e < 0` (#9718 `derived_unit_neg`), and that negative unit is what makes the n − p cell come out positive.

## 4. Numbers at q₀ (model only)

Bond letters: `f_like = z − h/2` = 0.508158, `f_pn` = 0.508230; `δ ln f_like` = 0.30744, `δ ln f_pn` = 0.31271.

| quantity | ruled law, `T = 8G·m_e` (production) | log chart, CAL-1 signed | mass chart, CAL-1 |
|---|---|---|---|
| B(²H) | +2.534 MeV | −0.936 MeV | −0.0499 MeV |
| B(⁴He) | +7.604 MeV | −2.809 MeV | −0.148 MeV |
| n − p | | +0.2887 MeV | **−0.3190 MeV** |
| Δ − N | | **−0.9888 MeV** | +0.0656 MeV |
| radius factor `D` (from `|Δ − N|`) | | 22.95 | 89.08 |

The magnitude of the #9733 n − p cell, 0.319 MeV, is right. Its sign, read with the same CAL-1 orientation that gives the electron positive mass, is negative. #9733 reports it as `2/w_e` without the sign.

## 5. Comparison boundary (data enter only here)

| | measured | log chart | mass chart |
|---|---|---|---|
| sign of n − p | + | + | − |
| sign of Δ − N | + | − | + |
| sign of B (bond letters) | + | − | − |
| muon carrier `1/ℏ_q²` pole | needed | cannot carry it (#9718) | carries it (#9733) |
| B(²H) / AME | | −0.42 | −0.022 |
| n − p / 1.29333 | | +0.223 | −0.247 |
| r_rms from `D` (0.8409 fm) | | 4.83 fm | 18.7 fm |

**Scope (a).** No single CAL-1 chart gives the correct sign to all three mass differences with the current letters. The log chart gets n − p right and Δ − N wrong; the mass chart does the reverse; both give the ruled bond letters negative binding. The production binding is positive only because the ruled law runs with `T = |c|`, the orientation opposite to CAL-1 (`ruled_law_opposite`).

**What is structural (scope (b), cited invariant).** The sign flips are not numerical accidents. They follow from `L_e < 0 < w_e` (`sign_agree_iff`), which holds on all of `1 < q ≤ 6/5` and in the classical limit (`τ_e(1) = 1/2`, `w_e(1) = 3`). Re-solving q₀ (the CAL-2 card) does not change them.

## 6. What this settles and what it does not

- **Settled:** how the two scales relate (the Euler derivative, with the explicit gap and the sign criterion above), and that a mass difference must be read in the chart of its masses.
- **Not settled:** the orientation. Either the letters (`τ_n/τ_p = q^{−2}`, the bond letters `f < 1`) or the energy dictionary's sign carries a convention that is not yet derived. Candidates worth a derivation front: the bar involution `q ↦ q⁻¹` (it reverses `δ`), the convention C / D choice behind `markov_forces_K`, and the 2026-11-25 law's `T > 0`.
- **Not adopted.** Nothing is wired. The production mass table, scorecard and radius probes are unchanged.

## 7. Orientation: framing against the bar-even part (owner decision A)

Carl chose "derive the orientation first". Lean:
`QOU/Observations/EnergyScaleOrientation.lean` (sorry-free, lean-direct exit 0, axioms
`propext, Classical.choice, Quot.sound`). Probe:
`computations/probes/energy_scale_bridge/orientation_probe.py` (19/19).

The electron trace factors as `τ_e = q³ · y₃` with `y₃ = (q⁴+1)/(q²+1)²`. Here `3` is the
writhe of `σ₀σ₁σ₀`, and `y₃` is the framing-corrected trace.

- `y₃` is bar-invariant (`y3_bar`). Its Euler weight `ω = q∂_q log y₃` is bar-odd
  (`omega_bar`).
- So `L_e = ℓ_e + 3β` and `w_e = ω_e + 3`, with `ℓ_e = log y₃` bar-even.
- `unit_signs_iff` shows where each unit gets its sign. The log-chart unit takes it from the
  framing-free part `ℓ_e`. The mass-chart unit takes it from the writhe.
- The values at q₀ are `ℓ_e = −0.6824`, `3β = 0.3130`, `ω_e = 0.2035`. In the log chart
  `|ℓ_e| > 3β`, and in the mass chart `3 > |ω_e|`.
- At `q = 1`, `ℓ_e = −ln 2` and `ω_e = 0`, so the conflict is already present in the
  classical limit (`split_at_classical_limit`). It is not an accident of q₀.
- The log-chart unit changes sign only where `τ_e = 1`, at `q* = 1.2414`, which is above q₀.
- If both charts use `y₃`, the log chart keeps `L < 0` and the mass chart gets `ω > 0`.
  So framing correction does not remove the conflict (`L·ω = −0.139`). The mass-chart unit
  `ω` also vanishes at `q = 1`.

What decides the orientation is therefore one question: does the sign of energy come from the
electron's framing (its writhe) or from its framing-free part? In a TQFT, framing is a gauge
choice, which argues for the framing-free reading (the log chart sign). But the mass chart's
positivity comes entirely from the writhe. This is stated here and not decided.

The n−p cell `τ_n = q⁻² τ_p` is a pure power. If that power were a framing difference, then any
framing-free chart would give n−p = 0 (`framing_cell_zero`). Under the ruled γγ word it is not
one: both nucleons have writhe 0 (`QOU.Mass.GammaGammaWordSelection.borromean_writhe`;
`2026-11-22-coulomb-all-q-and-nucleon-writhe.md` §2). So the `q⁻²` is not framing, and the
framing route does not remove the n−p sign conflict.
