import QOU.FluidDynamics.q_ns_haar_field_invariance_full

/-!
# QOU.FluidDynamics.q_ns_haar_budget_full — the Haar budget identity on all of `O_q(SU(2))`

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), point 1: identify the budget
integrands with terms of an energy budget, now on the whole algebra.

`OqSU2BudgetLittleQJacobi` proved the off-diagonal budget `h(X₊a · X₋b) = −q⁻² h(a · L b)`
on the Cartan block `K[ζ]` only, and `q_ns_block_viscous_dissipation` turned it into the
energy rate of `u̇ = −νLu` there. `q_ns_haar_field_invariance_full` (#9731) now gives
`h ∘ X₊ = h ∘ X₋ = h ∘ X₀ = 0` on the whole algebra through the PBW basis. This file draws the
consequences, for `q` not a root of unity.

Write `T = θ_{q⁻¹, q}` for the twist of the twisted Leibniz rule
`X(fg) = Xf · T g + f · Xg`, `σ = θ_{q⁻², 1}` for the Haar modular automorphism, and
`L = X₊ ∘ X₋`.

## Results (sorry-free)

* `haarState_ibp_plus`, `haarState_ibp_minus`, `haarState_ibp_zero`: integration by parts,
  `h(X f · T g) = −h(f · X g)` for every `f, g` and `X ∈ {X₊, X₋, X₀}`.
* `lap_torus`: `L` commutes with every torus automorphism (the two scalars cancel).
* `haarState_budget_full`: **the budget identity on all of `O_q(SU(2))`**,
  `h(a · L b) = −q² · h(X₊a · X₋(T b))`. On `K[ζ]`, `T b = b` and this is the old identity.
* `haarState_lap_mul`: `h(L u · u) = h(u · L(σ u))` (Haar modularity, `L σ = σ L`).
* `energy_rate_full`: for `u̇ = −νLu`, the rate of `h(u · u)` is
  `ν q² · (h(X₊u · X₋(T u)) + h(X₊u · X₋(T σ u)))` on the whole algebra.
* `energy_rate_full_of_fixed`: if `T u = u` and `σ u = u`, the rate is `2νq² h(X₊u · X₋u)`.
  With `haarState_plusMinus_nonpos` (`OqSU2BudgetSign`) that is `≤ 0` for `u* = u`, `ν ≥ 0`,
  `0 < q ≠ 1`. That last step is not stated here: `OqSU2BudgetSign` imports
  `OqSU2HaarPositivity`, which declares `mono`, `mono_nat`, `beta_alpha`, `gamma_alpha`,
  `gamma_beta` in the same namespace as `OqSU2PBW`, so the two cannot be imported together
  until one side is renamed.

## Reading in the PBW basis

`θ_{u,v}` scales the PBW monomial of index `(a, b, c)` by `u^a v^(b−c)` (`torus_mono`). So on
a weight-homogeneous `u` of weight `(a, b − c)`, `T u = q^{(b−c)−a} u` and `σ u = q^{−2a} u`,
and the budget pairs block `w` with block `−w`. The fixed case is the weight-zero block
`span{β^b γ^b} = K[ζ]`. This is not stated as a separate theorem here.

## Not established

* Any identification of `L` with the corpus's `Δ_q`, or of `ν` with `ν_q = (1 − q⁻¹)/2`:
  `d_q`, `δ_q`, `∇_q` are not defined on `O_q(SU(2))` in the corpus.
* The Cartan scale. The Cartan field `c⁻¹(ε − χ_{s²})` of `OqSU2BudgetSign` has its sign
  for every `s` and `c`, and the twist `s² = q⁻¹` here is the one the off-diagonal fields
  carry. Nothing in this budget fixes `c`, so nothing here selects `ħ_q`.
* Part A, and any triad transfer rate.

Everything is algebraic, so the file stays out of `QOU/Transcendental/`. No empirical
value enters any proof.

-- Ref: [woronowicz1987-twisted-su2]
-- Ref: [leitner2026] (`conj:regularity-breakdown`)
-/

namespace QOU.FluidDynamics.HaarBudgetFull

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2
open QOU.FluidDynamics.HaarFieldInvarianceFull

section Ring

variable {R : Type*} [CommRing R] (q : Rˣ)

/-- `L` commutes with every torus automorphism. -/
theorem lap_torus (u v : Rˣ) (x : OqSU2 R q) :
    torusScaleAlgHom q u v (lap q x) = lap q (torusScaleAlgHom q u v x) := by
  rw [lap_apply, lap_apply, torus_fieldPlus, torus_fieldMinus, map_smul, smul_smul]
  have h : (u : R) * ((v⁻¹ : Rˣ) : R) * ((v : R) * ((u⁻¹ : Rˣ) : R)) = 1 := by
    calc (u : R) * ((v⁻¹ : Rˣ) : R) * ((v : R) * ((u⁻¹ : Rˣ) : R))
        = ((u : R) * ((u⁻¹ : Rˣ) : R)) * (((v⁻¹ : Rˣ) : R) * (v : R)) := by ring
      _ = 1 := by rw [Units.mul_inv, Units.inv_mul, one_mul]
  rw [h, one_smul]

end Ring

variable {K : Type*} [Field K] (q : Kˣ)

local notation "T" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

section Budget

variable (hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1)
include hq

/-- Integration by parts for `X₊` on the whole algebra. -/
theorem haarState_ibp_plus (f g : OqSU2 K q) :
    haarState q (fieldPlus q f * T g) = -haarState q (f * fieldPlus q g) := by
  have h := haarState_fieldPlus_eq_zero q hq (f * g)
  rw [field_leibniz, map_add] at h
  linear_combination h

/-- Integration by parts for `X₋` on the whole algebra. -/
theorem haarState_ibp_minus (f g : OqSU2 K q) :
    haarState q (fieldMinus q f * T g) = -haarState q (f * fieldMinus q g) := by
  have h := haarState_fieldMinus_eq_zero q hq (f * g)
  rw [field_leibniz, map_add] at h
  linear_combination h

/-- Integration by parts for the Cartan field `X₀` on the whole algebra. -/
theorem haarState_ibp_zero (f g : OqSU2 K q) :
    haarState q (fieldZero q f * T g) = -haarState q (f * fieldZero q g) := by
  have h := haarState_fieldZero_eq_zero q hq (f * g)
  rw [field_leibniz, map_add] at h
  linear_combination h

/-- **The budget identity on all of `O_q(SU(2))`.** `h(a · L b) = −q² h(X₊a · X₋(T b))`. -/
theorem haarState_budget_full (a b : OqSU2 K q) :
    haarState q (a * lap q b) = -((q : K) * q) * haarState q (fieldPlus q a * fieldMinus q (T b)) := by
  have h := haarState_ibp_plus q hq a (fieldMinus q b)
  rw [torus_fieldMinus, mul_smul_comm, map_smul, smul_eq_mul] at h
  rw [lap_apply]
  simp only [inv_inv] at h
  linear_combination h

/-- `h(L u · u) = h(u · L(σ u))`. -/
theorem haarState_lap_mul (u : OqSU2 K q) :
    haarState q (lap q u * u) = haarState q (u * lap q (modularAut q u)) := by
  rw [haarState_modular q (qSqNum_ne_zero_of_not_root q hq), modularAut, lap_torus]

/-- **Energy rate on the whole algebra.** For `u̇ = −νLu`,
`h(u̇ u) + h(u u̇) = ν q² (h(X₊u · X₋(T u)) + h(X₊u · X₋(T σ u)))`. -/
theorem energy_rate_full (ν : K) (u : OqSU2 K q) :
    haarState q ((-ν) • lap q u * u) + haarState q (u * ((-ν) • lap q u)) =
      ν * ((q : K) * q) * (haarState q (fieldPlus q u * fieldMinus q (T u)) +
        haarState q (fieldPlus q u * fieldMinus q (T (modularAut q u)))) := by
  rw [smul_mul_assoc, mul_smul_comm, map_smul, map_smul, smul_eq_mul, smul_eq_mul,
    haarState_lap_mul q hq, haarState_budget_full q hq, haarState_budget_full q hq]
  ring

/-- On `u` fixed by `T` and `σ` (the weight-zero block), the rate is `2νq² h(X₊u · X₋u)`. -/
theorem energy_rate_full_of_fixed (ν : K) (u : OqSU2 K q) (hT : T u = u)
    (hσ : modularAut q u = u) :
    haarState q ((-ν) • lap q u * u) + haarState q (u * ((-ν) • lap q u)) =
      2 * ν * ((q : K) * q) * haarState q (fieldPlus q u * fieldMinus q u) := by
  rw [energy_rate_full q hq, hσ, hT]
  ring

end Budget

end QOU.FluidDynamics.HaarBudgetFull
