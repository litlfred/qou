# Pre-registration: the per-down-strand self term of the categorical Lagrangian

**Date:** 2026-11-27 · **Beans:** `qou-myts`, `qou-99qc` · written before any MeV was computed.

## Observable

`Δ_self = m_n − m_p` contributed by the **self** (one-strand, no crossing) part of the
categorical Lagrangian `ℒ = 𝒟² + ψ*·𝒟ψ`, `𝒟 = q⁻¹∇ + (1 − q⁻¹)·Reeb`, after the energy is
taken by the Legendre transform of `QOU.Core.CategoricalHamiltonianLegendre`. Crossing
(two-strand) terms are excluded by construction; they are other fronts.

## Structural model (fixed before numbers)

* The nucleon state is a product of strand weight vectors `ψ = ψ₁ ⊗ … ⊗ ψ_n` in `V^{⊗n}`,
  `V` the fundamental 2-dim module, `u` of Cartan weight `+1`, `d` of weight `−1`
  (proton `K`-weight `q`, neutron `q⁻¹`, as in `NucleonWeightSpaceTwoTerm`).
* A degree-1 operator (the Reeb field, a vector field) acts on `V^{⊗n}` by the Leibniz rule,
  `R = Σ_s R_s`. A one-strand operator is either Weyl-even or Weyl-odd under `u ↔ d`.
* The self term of a strand of flavour `f` is `ε(f) = ⟨ψ_f, X ψ_f⟩` for `X` the strand operator.

## Variants (all reported; none selected by closeness to CODATA)

| id | energy map | Reeb eigenvalue on a strand | prediction form |
|---|---|---|---|
| V0 | velocity Legendre `H_vel = reebSq − spatialZero` | any | `Δ_self = 0` (degree 1 cancels) |
| V1 | canonical, unit clock, `H = a₂ − a₁ + a₁²/(4a₂) − a₀` | Cartan weight `w = ±1` | `2(1 − q⁻¹)·E` |
| V2 | same | electric charge `Q = w/2 + 1/6` | `(1 − q⁻¹)q⁻¹·E` |
| Vref | Gibbs `m = −E log τ`, own-sector `K = q^H` (existing cell, sibling front; reference only) | — | `2 log q·E` |

with `a₂ = ⟨R²⟩`, `a₁ = ⟨R⟩` on the product weight state (so `a₂ = a₁²`, state norm 1).
Scales `E`: order-zero `E₀` and tower `E₀` (`qbeta_e0.order_zero` / `qbeta_e0.canonical`),
proton `q₀`. Comparison: CODATA `m_n − m_p = 1.29333 MeV`, reported as a ratio only.

## Kill / pass criteria

* If a Weyl-even one-strand operator is shown flavour-blind, the degree-0 and degree-2 self
  terms are excluded as a source of the split (scope (b), invariant: Weyl reflection).
* The degree-1 self term is reported in every variant. None is promoted on its ratio to CODATA.
