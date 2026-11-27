# The per-down-strand self term of the categorical Lagrangian

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-down-strand-self-energy-2026-11-27`
**Beans:** `qou-myts`, `qou-99qc`
**Lean:** `QOU/Nuclear/NucleonDownStrandSelfEnergy.lean`, with `self_cartan_lt_gibbs_cell` (uses `Real.log`) split off behind the transcendental boundary into `QOU/Transcendental/Nuclear/NucleonDownStrandSelfEnergyGibbsCell.lean`, same namespace (lean-direct `-DautoImplicit=false -s 65536`, exit 0; axioms propext, Classical.choice, Quot.sound)
**Probe:** `computations/probes/nucleon_down_strand_self_energy/` (pre-registration, probe, witness; exact sympy over ℚ(q) for n = 2..5, then 80 dps)

## 1. Question

Owner: *"self energy for each down strand, not a crossing term. look at new reformulation of
energy from lagrangian and trace it through the na-stokes evaluation/mass calculation. see
where missing term is coming from"*; *"dont look at leading term only"*; *"work on all strands on
the full tower"*.

## 2. Where a self term sits in the chain

Lagrangian `ℒ = 𝒟² + ψ*·𝒟ψ`, `𝒟 = q⁻¹∇ + (1 − q⁻¹)·Reeb`. The energy reformulation
(`QOU.Core.CategoricalHamiltonianLegendre`, 2026-11-24) splits `ℒ` by degree in the Reeb field:
`reebSq` (degree 2), `reebLinear` (degree 1: the gyroscopic cross term and the Reeb-matter term
`(1 − q⁻¹)ψ*ψ·Reeb`), `spatialZero` (degree 0).

On a product weight state of `V^{⊗n}` a vector field acts by the Leibniz rule, `R = Σ_s R_s`:

| degree | self part (one strand) | crossing part (two strands) | flavour dependence of the self part |
|---|---|---|---|
| 2 (`R²`) | `Σ_s R_s²` | `Σ_{s≠t} R_s R_t` (Stokes: crossing curvature) | none if `R` is the Cartan: `H_s² = 1` (Weyl-even) |
| 1 (`ψ*ψR`) | `Σ_s ⟨ψ_s, R_s ψ_s⟩` | **none** (a derivation has no pair term in degree 1) | Weyl-odd: `c·w_s`, `w_u = +1`, `w_d = −1` |
| 0 (`ψ*ψ∇`) | `⟨ψ_s, ∇ψ_s⟩` | — | none if `∇` is flavour-equivariant (the `hHoriz` hypothesis) |

So the per-strand self energy is **structurally present**, and its only flavour-dependent piece
is the **degree-1 Reeb-matter term**, which is purely self (no crossing) and equals
`(1 − q⁻¹)·c·(n_u − n_d)`. Each down strand moves it by `−2c(1 − q⁻¹)` (`selfSum_flip_down`).
Full tower: `H_tot = Σ_s H_s` commutes with every Hecke generator on `V^{⊗n}` (checked exactly,
symbolic `q`, n = 2..5), so the self term is `n − 2n_d` on every weight space and hence on every
Wedderburn block `λ ⊢ n`, at every order in `q` — no truncation is involved.

Scope (b), invariant = Weyl reflection `u ↔ d`: every Weyl-even one-strand term (degree 2 with the
Cartan, degree 0 with an equivariant `∇`) is flavour-blind (`selfSum_flavour_blind_of_weyl_even`).
A d-heavier self energy can therefore only come from the Weyl-odd degree-1 term.

## 3. Through the Legendre transform

* **Velocity form** `H_vel = reebSq − spatialZero`: the degree-1 term cancels exactly
  (`categoricalHamiltonianVel_eq`). With shared `𝒟` and shared horizontal matter trace the two
  nucleons have equal velocity energy (`trace_hamiltonianVel_eq_of_shared`). **This is where the
  self term is dropped.** Scope (b) for this map.
* **Canonical form at unit clock** `H = a₂ − a₁ + a₁²/(4a₂) − a₀`: the term survives as minimal
  coupling `−a₁` plus recoil `a₁²/(4a₂)`. On a weight state `a₂ = a₁²`, so `4H = (2a₁ − 1)²`
  exactly (`canonical_unit_clock_weight_state`) — all orders, nothing truncated.
  * Cartan reading `a₁ = ±h`, `h = 1 − q⁻¹`: `m_n − m_p = 2h·E` (`canonical_diff_cartan`).
  * Charge reading (`Q = w/2 + 1/6`): the neutron has `a₁ = a₂ = 0`, where the canonical
    Hamiltonian is singular (`canonicalHamiltonian_zero`); its continuous extension gives
    `(h − h²)·E`.
* `2(1 − q⁻¹) < 2 log q` (`self_cartan_lt_gibbs_cell`). The canonical Cartan self term is the
  first term of `log q = Σ_k h^k/k`: it is the **same Cartan weight** that the Gibbs cell
  `2E₀ log q` already exponentiates (`K = q^H`), not an independent new term.

## 4. Numbers (proton q₀ = 1.10997858275138…, comparison only at the last column)

| variant | E = E₀ (order zero) | E = E₀ (tower) | ratio to CODATA 1.29333 (order zero) |
|---|---|---|---|
| V0 velocity | 0 | 0 | 0 |
| V1 canonical, Cartan | 0.829508 MeV | 0.837733 MeV | 0.641 |
| V2 canonical, charge (extension) | 0.373660 MeV | 0.377364 MeV | 0.289 |
| Vref Gibbs cell `2 log q` (existing) | 0.873537 MeV | 0.882197 MeV | 0.675 |

## 5. Verdict

* Scope (b): within the product-weight-state model with `u, d` weights of one `V`, no Weyl-even
  self term splits the nucleons, and the only Weyl-odd self term is linear in the Cartan weight.
  It is the per-strand origin of the existing K-weight cell, not a missing extra term.
* Scope (a): none of V0–V2 closes the gap; V1 sits **below** the Gibbs cell. The missing ~32 %
  is not supplied by a per-down-strand self term of this Lagrangian under either Legendre form.
* What would change this: a one-strand operator that is neither Weyl-even nor linear in the
  weight — i.e. `u` and `d` not related by the Weyl reflection of one `V` (different objects, or
  the up quark as an unknot strand and the down quark as something else). That is a change of
  model and an owner call; recorded as fork F1.

## 6. Forks (not decided here)

* **F1** Is the down strand the same object as the up strand? The owner ruling makes the up quark
  an unknot strand; if the down strand carries its own framing/twist (`θ_d ≠ θ_u`), the Weyl
  invariant no longer applies and a genuine flavour self energy is allowed.
* **F2** Velocity vs canonical Legendre form for the scoreboard energy (V0 vs V1/V2).
* **F3** Reeb eigenvalue: Cartan weight (V1) or electric charge (V2, singular for the neutron).

## 7. Reproduce

    python3 -u computations/probes/nucleon_down_strand_self_energy/nucleon_down_strand_self_energy_probe.py
    lean -DautoImplicit=false -s 65536 folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonDownStrandSelfEnergy.lean
    lean -DautoImplicit=false -s 65536 folio/quantum-observable-universe/lean/QOU/Transcendental/Nuclear/NucleonDownStrandSelfEnergyGibbsCell.lean
