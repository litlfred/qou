# Radius routes on the energy-to-length map

**Date:** 2026-11-27 · **Branch:** `claude/energy-length-radius-routes-2026-11-27` · **Builds on:** PR #9697 (`QOU/InformationTheory/EnergyLengthMap.lean`)

## 1. Claim

The map `ℓ_q(E) = ℏ_q c_q / E` is forced (#9697), and in CAL units every model length is
`r = D · (m_e/E) · ƛ_e`. Here `ƛ_e` (CAL-1) is the only measured length, and it enters only at the comparison.
This document asks whether information-theoretic principles fix the dimensionless factor `D = r / ℓ_q(E)` for a bound state.

They do not fix it. Both routes give **lower bounds** on `D`. The sibling SU_q(2) Casimir route
(q-Bessel thread) gives an equality, but only under an assumption. All three routes reduce to one missing model ratio, `ε = K/E`: a kinetic or gap energy over the rest energy.

## 2. Route A: Bekenstein form with the Haar entropy

`R ≥ S · ℓ_q(E) / 2π` (Lean: `radius_ratio_ge_of_bekenstein`). We take `S` to be the Woronowicz Haar modular entropy per strand,
`S₁ = H(p₊)` with `p₊ = q²/(1+q²)` (`OqSU2HaarModularEntanglement`), and three strands.

| quantity | value at q₀ (mpmath, 30 dps) |
|---|---|
| `p₊` | 0.55198249 |
| `S₁` (nats) | 0.68773304 (ln 2 = 0.69314718) |
| `D_A = 3 S₁ / 2π` | 0.328368 |

Saturation (`BekensteinSaturationConjecture`) would give `D = 0.328`. **Scope (a):** this construction alone does not give the radius. Section 5 shows the bound is far from saturated, as it is for ordinary matter. The bound itself holds.
Reaching the comparison value would need `S ≈ 25` nats. No derived state count on record gives that, and choosing one to match would be selection against the target.

## 3. Route B: Fisher information (Stam / Heisenberg in three dimensions)

`⟨r²⟩⟨p²⟩ ≥ 9ℏ²/4`. So `D ≥ (3/2) / (p_rms c / E)`. The ratio `p_rms c / E` is a
kinetic share. The corpus derives no such share for a nucleon strand, and a bound state needs the potential that this route leaves out. So route B is a lower bound
parameterised by `ε_B = p_rms c / E`, with nothing chosen.

## 4. Route C (q-Bessel thread, for comparison): SU_q(2) Casimir

`r_rms = √(q/(1+q²)) · √(λ₁/2) · ℏ_q c_q / √(Mc² · E₁)` with `λ₁ = q² + 1`, so
`D_C = √(q/2) / √ε_C` with `ε_C = E₁/Mc²`. Setting `ε_C = 1` (assumed) gives `D_C = √(q/2) ≈ 0.745`.

## 5. Comparison boundary (data enters only here)

| | value |
|---|---|
| measured `r_p` / `ƛ_p` (CODATA 0.8409 fm / 0.21031 fm) | ≈ 4.00 |
| route A, saturated | 0.328 (≈ 12× short) |
| route C, `ε_C = 1` | 0.745 (≈ 5.4× short) |

The value 4.00 is a known coincidence. No route was tuned toward it, and a route that lands near it would need a derived `ε`, not a selected one.

## 6. What this establishes

- The **map** is derived. The **shape factor `D`** is not.
- Routes B and C share one unknown: a model energy ratio `ε` (a kinetic or gap energy over the rest energy). Route A instead needs a principle that the bound is saturated, and the numbers argue against one.
- The next derivation target is therefore `ε`, from the model's own spectrum (for example the first Hecke / Casimir gap in units of the nucleon rest energy). It is not a new length scale.

Nothing is adopted and nothing is wired.

## 7. First derived ε: the isospin block gap (added the same day)

Probe: [`isospin_gap_radius_probe.py`](../../computations/probes/energy_length_map/isospin_gap_radius_probe.py) (mpmath 50 dps, proton pin).

The gap is taken blind to any radius from corpus definitions only:
- **Block weights.** Convention D on `V^{⊗3}`, `V = ℂ²` (isospin), gives `y_(3) = [4]/[2]³` and `y_(2,1) = [2]/[2]³`. Clebsch–Gordan, `[2]³ = [4] + 2[2]`, is checked in the probe.
- **Energies.** The `β = ln q` dictionary (`QBetaEnergyDictionary`) turns weights into energies, in the unit of the quantum temperature `k_B T_q = E₀ = m_e/(q(q−1))` (`def:quantum-temperature`, `SpectatorEnergyMap.e0`).
- **The gap.** `E₁ = E₀ · ln([4]/[2]) = E₀ · ln(q² + q⁻²)`, and `ε = E₁ / M` with `M` the model proton mass.

| quantity | value |
|---|---|
| `q² + q⁻²` | 2.04370620853 |
| `|E₁| / m_e` | 5.85518358785 |
| `ε` | 0.00318883265 |
| `D_C = √(q/2)/√ε` | **13.1925** |

**The sign is reversed.** The symmetric block `(3)` has the larger weight, so the dictionary puts it *below* `(2,1)`. If `(3)` is read as the isospin-3/2 state, the order is opposite to the nucleon being the ground state.

**Comparison boundary:** `|E₁| = 2.99 MeV` against `Δ − N ≈ 293 MeV`, and `r_rms = 2.77 fm` against `r_p = 0.8409 fm`.

**Scope (a):** this gap, alone and in this energy unit, does not give the radius. It is too small by about 98×, which makes the radius about 3.3× too large, and the sign is reversed. Two things could change the result:
- a different energy unit, which is the open "which multiple of `E₀`" question recorded in `SpectatorEnergyMap`;
- a different gap operator, such as the Casimir insertion `h²C` on the charge sectors (`BlockChargeSectorTrace`).

Choosing among those to match would be selection. Each needs its own derivation.

## 8. The E₀ multiple is the open electron weight, and neither corpus unit helps

The "which multiple of `E₀`" question is not new. `docs/audits/2026-11-22-energy-scale-cal-map.md` and `ElectronUnitSplit.lean` already pin it to a single open input: the electron's categorical weight `w_e`.
- **The calibrations cannot decide it.** The Lean results `Chart.matches_rescale` and `Chart.calibration_does_not_fix_unit` prove this.
- **The β-dictionary unit is not a second ambiguity.** The `β = ln q` dictionary unit is `E₀·ln q` (`SpectatorEnergyMap.dictionary_unit`), and both temperature readings describe one Gibbs state (`same_weight_iff`). So a gap read from weights is `E₀·ln(y-ratio)` in either reading. The only freedom left is `w_e`.

The corpus holds two electron weights. I computed both and chose neither.

| unit | electron weight | `|E₁|` / m_e | `ε` | `D` |
|---|---|---|---|---|
| mass formula | `ℏ_q²` (CAL-1 placed by hand, `product_weight_ne`) | 5.8552 | 3.19e-3 | 13.19 |
| trace pipeline | `τ_e = q³ y₍₃₎` (derived from the ruled electron word) | 0.08317 | 4.53e-5 | 110.69 |

The units differ by `R = τ_e/ℏ_q² = 70.404`. Two consequences:
- **The derived unit makes the miss larger.** At the comparison boundary, `r_rms` is 23.3 fm against 2.77 fm in the mass-formula unit, and both are far above 0.84 fm. So the unit is not the lever that closes the gap.
- **The isospin block gap is not the right gap.** Read through the `β = ln q` dictionary, it is below Δ − N by two to four orders of magnitude, and its sign is reversed. The next candidate is a different operator, for example the Casimir insertion. Both units are carried along, and neither is selected.
