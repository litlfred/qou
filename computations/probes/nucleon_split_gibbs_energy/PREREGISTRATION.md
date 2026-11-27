# Pre-registration: the Gibbs map as free energy vs internal energy (nucleon split)

**Date:** 2026-11-27 · **Beans:** `qou-myts`, `qou-99qc` · **Branch:** `claude/nucleon-split-gibbs-energy-2026-11-27`

Written before the probe computed any MeV value. (While setting up the Lean, rough mental
estimates of two variants were made; no variant below is chosen or dropped because of them.)

## The corpus reading being tested

`SpectatorEnergyMap`: the nucleon value is `ε_N = K_N·t(q)/D(q)`, `K_p = q`, `K_n = q⁻¹`, `t`
the common weight-space trace (`HeckeWeightSpaceSymmetry`), and `m = −E₀·log ε` with
`k_BT_q = E₀` (`kT_eq_e0`). `prop:beta-eq-ln-q-dictionary` reads the trace as a partition
function at `β = ln q`, with energies `E_λ = −ln y_λ/ln q` that themselves depend on `q`.
`m = −kT log Z` is therefore the Helmholtz free energy `F`.

## Variants (all reported, none selected)

| id | function | temperature parametrisation `β = b(q)` | energy unit |
|---|---|---|---|
| F | `ΔF = −Δlog Z/β` | any (unit-covariant) | `E₀·ln q` (dictionary) = MeV via `m_e` |
| U-D | `ΔU = −dΔlog Z/dβ` | `b = ln q` (dictionary) | dictionary unit, converted at `q₀` |
| U-nat | same | `b = q/(q−1)` (`def:quantum-temperature`, natural units) | `m_e c_q²`, converted at `q₀` |
| U-T0 | same | `b = 1/E₀ = q(q−1)` (route T, CAL-1 unit held fixed) | `m_e` |
| U-Ttw | same | `b = 1/E₀^tower = (q−1)(2q−1)/q` | `m_e` |
| F-tw | `ΔF` with `kT = E₀^tower` | — | `m_e` |
| TS | `TΔS = ΔU − ΔF` for each U variant | | |

"Full tower": `Δlog Z = −2 ln q` holds for every common factor `s(q)` (all orders in q), and the
common factor is a common factor at level `n` iff `tr_{W_μ} = tr_{W_{−μ}}` there; checked exactly
for `n = 3, 5, 7` by `tower_weight_symmetry_check.py`. The tower enters the numbers only through
`E₀` vs `E₀^tower`.

## Rules

- No variant is adopted, ranked or dropped by its distance to CODATA `m_n − m_p` or `Q_β`.
- The physical argument for which `β` is "the" temperature is stated in the audit as an argument
  and, where it is not forced by a corpus artifact, as an open fork.
- Comparison to CODATA is reported only in a final comparison table.
