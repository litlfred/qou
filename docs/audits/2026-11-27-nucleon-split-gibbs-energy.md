# The Gibbs map for the nucleon split: free energy or internal energy?

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-split-gibbs-energy-2026-11-27` · follows #9475
**Beans:** `qou-myts`, `qou-99qc` · **Owner:** *"Gibbs - explore"*, *"dont look at leadgin term only"*,
*"make sure you work on all strands on the full tower"*
**Lean:** [`QOU/Nuclear/NucleonSplitGibbsEnergy.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitGibbsEnergy.lean)
  The rational `uSplit` closed forms (`uNat_eq`, `uNat_neg`, `uT_eq`, `uTower_eq`, over any ordered field) stay there; `log Z`, `fSplit`, `tsSplit`, the derivatives and the `log q` comparisons (`logZ_split`, `logZ_split_hasDerivAt`, `dictionary_U_eq_F`, `uT_lt_fT`, `uTower_lt_fTower`) are behind the transcendental boundary in [`QOU/Transcendental/Nuclear/NucleonSplitGibbsEnergyAnalytic.lean`](../../folio/quantum-observable-universe/lean/QOU/Transcendental/Nuclear/NucleonSplitGibbsEnergyAnalytic.lean), same namespace.
**Pre-registration:** [`computations/probes/nucleon_split_gibbs_energy/PREREGISTRATION.md`](../../computations/probes/nucleon_split_gibbs_energy/PREREGISTRATION.md)
**Probe:** `nucleon_split_gibbs_energy_probe.py` → `nucleon-split-gibbs-energy.witness.json` (80 dps);
`tower_weight_symmetry_check.py` (exact, `n = 3, 5, 7`)

## 1. Short answer

- The map `m = −E₀·log ε` (#9475, `SpectatorEnergyMap.routeT_cell`) is the **Helmholtz free
  energy** `F = −log Z/β` of the nucleon sector read as a partition function
  (`prop:beta-eq-ln-q-dictionary`). That is the corpus's own reading.
- **All orders in q and up the tower:** `log Z_n − log Z_p = −2 ln q` for every positive common
  factor `s(q)` — trace, normalisation, tower factor, spectator strands (`logZ_split`), and its
  `q`-derivative is `−2/q` for every `s` (`logZ_split_hasDerivAt`). The common factor is common at
  level `n` because `tr_{W_μ} = tr_{W_{−μ}}` there: proved at `H₃` for every element
  (`HeckeWeightSpaceSymmetry`), checked exactly here for 108 random words with inverses at
  `n = 3, 5, 7`, all weights `μ`, with a negative control that does break it. So nothing beyond the
  leading term is dropped: the split is exact, and the only places the tower enters are the
  temperature and its parametrisation.
- **In the corpus's own temperature `β = ln q`, F and U coincide:** `ΔU = ΔF = 2` dictionary units
  and `TΔS = 0` (`dictionary_U_eq_F`). The K-weight energies `−μ` are `q`-independent there, so the
  split is a genuine energy-eigenvalue difference with no entropy term at any order. In MeV this is
  `2E₀·ln q`, the #9475 cell.
- **U is not unit-covariant; F is.** `ΔU = 2/(q·b'(q))` depends on which function of `q` plays
  `β`. The corpus has three more: natural units `β = q/(q−1)` (`def:quantum-temperature`), and the
  route-T temperature in the fixed CAL-1 unit `m_e`, `β = 1/E₀ = q(q−1)` or with the tower
  `E₀`, `β = (q−1)(2q−1)/q`. They give different `U` (table). The dictionary's energy unit
  (`E₀·ln q·m_e`) and the natural unit (`c_q²·m_e`) both move with `q`; only `m_e` is fixed.

## 2. Closed forms (Lean, all `q > 1`)

| reading | `ΔF` | `ΔU` | `TΔS = ΔU − ΔF` |
|---|---|---|---|
| dictionary `β = ln q` | 2 | 2 | 0 |
| natural `β = q/(q−1)` | `2(q−1)ln q/q` | `−2(q−1)²/q` (< 0, `uNat_neg`) | < 0 |
| CAL-1, `β = 1/E₀` | `2 ln q/(q(q−1))` | `2/(q(2q−1))` | < 0 (`uT_lt_fT`) |
| CAL-1, `β = 1/E₀^tw` | `2q ln q/((q−1)(2q−1))` | `2q/(2q²−1)` | < 0 (`uTower_lt_fTower`) |

Every derivative `b'(q)` is a checked `HasDerivAt`. `ΔF` is the same physical quantity `2E₀ ln q`
in each reading (in each reading's unit); `ΔU` is not.

## 3. Numbers, proton q₀ = 1.10997858275138… (MeV; muon anchor agrees to 7 digits)

`E₀ = 4.18598136329`, `E₀^tower = 4.22748335563` (closed form matches `qbeta_e0.canonical` to 1e-78).

| variant | split | `TΔS` |
|---|---|---|
| F, `kT = E₀` (= U dictionary) | 0.873536621 | 0 (dictionary) |
| F, `kT = E₀^tower` | 0.882197317 | — |
| U natural units | −0.920736596 | −1.79427 |
| U CAL-1, `E₀` | 0.754728626 | −0.11881 |
| U CAL-1, `E₀^tower` | 0.774804985 | −0.10739 |

## 4. Comparison boundary (CODATA 2022; comparison only)

| variant | vs `m_n − m_p` 1.293332 | vs `Q_β` 0.782334 |
|---|---|---|
| F, `E₀` | −32.46 % | +11.66 % |
| F, `E₀^tower` | −31.79 % | +12.76 % |
| U natural | −171.2 % | −217.7 % |
| U CAL-1, `E₀` | −41.64 % | −3.53 % |
| U CAL-1, `E₀^tower` | −40.09 % | −0.96 % |

**Warning, recorded so nobody adopts it as evidence:** the U-CAL-1-tower variant lands within 1 %
of `Q_β`. It was pre-registered as one of six, it is not singled out by any corpus artifact, and
the tower `E₀` is itself one of two on-record `E₀`. Choosing it because of that 1 % would be a
selection against the target (AGENTS.md §NO FITTING). None of the six reaches `m_n − m_p`.

## 5. Scope

- **(b), structural, cited invariant:** within the Gibbs-map family no thermodynamic correction
  (entropy, temperature-derivative, higher order in q, higher tower level) changes the split in the
  dictionary reading — `logZ_split` holds for every common factor, and `ΔU = ΔF` there. "The
  leading-term truncation is what is missing" is excluded for this reading. The tower statement
  rests on the exact `n = 3, 5, 7` check, not on a general-`n` Lean proof.
- **(a):** F, U-natural and the two U-CAL-1 variants each, alone, do not reproduce `m_n − m_p`.

## 6. Open forks (owner)

1. **Is a mass `F` or `U`?** The corpus map is `F`. A rest energy is usually `U`; at a ground
   state they agree. In the dictionary reading the question is moot (`ΔU = ΔF`).
2. **Which β is the temperature when `U` is taken?** The dictionary (`β = ln q`) is the only corpus
   artifact that writes a partition function with a β; there `U = F`. Holding the CAL-1 unit fixed
   argues for `β = 1/E₀` instead (an argument, not a corpus artifact), and that variant is split
   again by the `E₀` vs `E₀^tower` fork. Default if unanswered: the corpus reading (`F` = dictionary
   `U`, 0.87354 MeV) stands and nothing is adopted.

## 7. Reproduce

```bash
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitGibbsEnergy.lean \
  folio/quantum-observable-universe/lean/QOU/Transcendental/Nuclear/NucleonSplitGibbsEnergyAnalytic.lean
python3 computations/probes/nucleon_split_gibbs_energy/tower_weight_symmetry_check.py
python3 -u computations/probes/nucleon_split_gibbs_energy/nucleon_split_gibbs_energy_probe.py
```
