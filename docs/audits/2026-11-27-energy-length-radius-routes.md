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
