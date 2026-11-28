# A pre-registered EM ring factor μ from the photon vertex pair (gap G3)

Date: 2026-11-27. Bean: `qou-tcl3` (under `qou-s028`). Follows PR #9839 (the ring ledger:
any reading gives `ε·(a + bT_z + cT_z²)` with `ε = ρ(μ)`).
Lean: `QOU/Nuclear/CoulombRingMu.lean` (sorry-free, generic field).
Probe: `computations/probes/coulomb_ring_mu/coulomb_ring_mu_probe.py` (mpmath 50 dps, 2/2 checks).

## 1. Route, fixed before any number was computed

One Coulomb pair is one photon exchanged between two proton blocks, so one chirality-summed
vertex pair. PR #9841 proves that pair is the scalar `−h²` (`h = q − q⁻¹`) at any two
generators, and that each pair in the polarisation chain carries one `α`. So

    μ₁ = 1 − α h²            (one exchange; pre-registered primary)
    μ_lad = 1/(1 + α h²)     (ladder; differs at O(α²))

with `α` the corpus-derived `α_EM` (`_alpha_em_inv_derived`, conditional on the Witten-κ Gram
`sorry`). No alternative `μ` was tried.

## 2. What is proved

| statement | Lean |
|---|---|
| `μ₁(1) = 1`: invisible at `q = 1`, like the γγ bonds in the energy reading (#9793) | `mu1_at_one` |
| `q·D h = [2]` for the Euler operator | `euler_h` |
| energy reading `ε_U = 2αh[2]/(1 − αh²)` | `energy_mu1` |
| mirror split at `A = 3` is exactly `ε` | `mirror_A3_mu1` |

## 3. Numbers at the proton `q₀` (conditional on `α`)

`h = 0.2090603`, `[2] = 2.0108969`, `1/α = 137.0359351`, tower `E₀ = 4.2274834` MeV,
`U_e = 2.4846281` (unit `m_e/U_e`, as in #9793).

| factor | `ε_log = E₀·(−ln μ)` | `ε_U = (m_e/U_e)·U(μ)` |
|---|---|---|
| `μ₁` | 1.3485 keV | 1.2623 keV |
| `μ_lad` | 1.3481 keV | 1.2615 keV |

The two readings agree within 7 %, and the ladder changes the fourth digit.

**Comparison only** (AME2020 mirror splits from the #9691 table; `ε` needed `= 2ΔB/(A − 1)`):

| pair | ε needed (MeV) | needed / ε_log | needed / ε_U | needed · A^{1/3} |
|---|---|---|---|---|
| ³H/³He | 0.7638 | 566 | 605 | 1.10 |
| ⁷Li/⁷Be | 0.5480 | 406 | 434 | 1.05 |
| ¹⁵N/¹⁵O | 0.5052 | 375 | 400 | 1.25 |
| ⁴¹Ca/⁴¹Sc | 0.3639 | 270 | 288 | 1.25 |

## 4. Reading the result

1. **Scope (a) negative.** The vertex-pair factor on its own gives `ε ≈ 1.3 keV`, which is
   about 570 times too small at `A = 3`. It does not exclude the factor from a closure.
2. **The missing piece is a size, not a coupling.** The needed `ε` falls like `A^{−1/3}` (the
   last column is roughly flat, 1.05 to 1.30). `μ₁` is a contact factor and has no `A`
   dependence. The gap is `ħc/r` against `E₀h²`, i.e. the same energy-to-length map that #9691
   left open (`r_rms`, beans `qou-mbfv`, `qou-usft`). Deriving `μ` from the vertex algebra alone
   cannot close it.
3. **What the route does settle.** On the ring, the EM factor has the right shape: `μ(1) = 1`,
   both readings give the same `ε` to 7 %, and the ledger's rank ratios are untouched.

Nothing was fitted or selected. No measured value is in any proof.
