import Mathlib.Combinatorics.Enumerative.Catalan
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import QOU.InformationTheory.UnifiedClockScaleLayers
import QOU.InformationTheory.FiniteRieffelQuantumMetric
import QOU.AlgebraicSubstrate.PlanckStepAtomicity
import QOU.AlgebraicSubstrate.OqSU2ModularNakayama

/-!
# Reeb Length/Time Reconciliation, Causal Cone `c_q`, `L_cal` Boundary Torsor, and Light-Cone (`LCQ`) Horizon Channel Entropy

Generic base-ring / ordered-field (§7c, zero `ℝ`, zero empirical inputs) formalization for
bean `qou-slfm` (with upstream threads `qou-mumr`, `qou-5uj7`, `qou-jfx8`, `qou-apma`, and
`UnifiedClockScaleLayers` / `FiniteRieffelQuantumMetric`):

1. **Layer-I Reeb Length, Computation Time, Lieb–Robinson Causal Cone `c_q`, and `𝔈 = 𝔪 c_q²`:**
   - Reconciles the per-step Reeb share `hbarQ q = 1 - q⁻¹`, the full-circuit tick
     `planckTick q = (hbarQ q)⁻¹ = q / (q - 1)`, and the unit-normalised Reeb circuit
     `normalisedCircuitLength q = hbarQ q * planckTick q = 1` (`ℓ_P = 1`, `qou-mumr`).
   - Along `steps = d_Reeb(γ) ∈ ℕ` elementary `f_q`-iterations, Reeb computation time is
     `reebCompTime q steps = steps * hbarQ q`, horizontal `D_∇` reach is
     `horizConeRadius q steps = steps * q⁻¹`, and their ratio is the causal cone speed
     `causalSpeed q = (q - 1)⁻¹ = q⁻¹ / hbarQ q = planckTick q - 1`
     (`lieb_robinson_cone_slope`: `horizConeRadius q steps = causalSpeed q * reebCompTime q steps`).
   - Categorical energy `categoricalEnergy q m = m * (causalSpeed q) ^ 2 = m / (q - 1) ^ 2`
     (`qou-91w7`), operational/cell entropy `cellEntropyG q = (q - 1) ^ 2 / q ^ 3`, and
     gravitational coupling `gravCouplingG q = q ^ 2 / (q - 1) ^ 4` satisfy **both**
     `gravCouplingG q * (hbarQ q / causalSpeed q) ^ 2 = 1` (`G_Planck = 1` over any field `K`)
     **and** `hbarQ q * gravCouplingG q / (causalSpeed q) ^ 3 = q` (from `hbarQ q * causalSpeed q = q⁻¹`).

2. **KMS Modular Computation Time vs Traciality Obstruction (`kms-length-dynamics` & `OqSU2`):**
   - Any tracial state `φ(x y) = φ(y x)` satisfying the KMS grading swap on a unit `u` with
     `φ(1) = 1` forces trivial modular factor `ω = 1` (`tracial_kms_grading_trivial`), and
     the inhomogeneous Hecke quadratic `T_s² = h T_s + 1` (`h ≠ 0`) admits no non-trivial
     multiplicative length-grading character (`hecke_quadratic_grading_trivial`).
   - Conversely, a non-tracial density-weighted state `φ_D(x) = τ(D x)` (`D ∈ Aˣ`) satisfies
     the exact discrete KMS swap `φ_D(x * (D * y * D⁻¹)) = φ_D(y * x)` (`density_weighted_discrete_kms`),
     realized on Woronowicz's `O_q(SU(2))` by `nuAlgEquiv q` with modular step ratio `q²`
     (`oqsu2_haar_modular_clock`).

3. **Layer-II/III Rieffel Step-Cost Split & `L_cal` Boundary Unit-Conversion Invariance:**
   - Under `D_∇ = q⁻¹ ∇_hor + ℏ_q ι_ξ ∇`, `N` paired horizontal + Reeb steps accumulate
     exact dimensionless cost `N * q⁻¹ + N * hbarQ q = N` (`dirac_split_step_cost_identity`).
   - Laboratory calibration `L_cal > 0` enters **only** at the Layer-III comparison boundary:
     rescaling a `LipSeminorm` by `L_cal⁻¹` scales dual Rieffel–Kantorovich distance bounds
     linearly by `L_cal` (`rescaleInv_dualBound_iff`) while cancelling identically from all
     dimensionless ratios, `causalSpeed q`, and `A / (4 ℓ_P²)` (`calibration_cancels_in_observables`).

4. **Light-Cone (`LCQ`) Horizon Crossing Channel Counting & Honest Rule-13a Area Conjecture:**
   - On a discrete causal horizon cut pierced by `nPunct` minimal `TL_{nPunct}(q)` / spin-`1/2`
     punctures: odd `nPunct = 2m + 1` has zero singlet sector (`tlSingletDim_odd`), while even
     `nPunct = 2m` has exact singlet dimension `tlSingletDim (2 * m) = catalan m`, satisfying
     `(m + 2) * catalan (m + 1) = 2 * (2 * m + 1) * catalan m` and two-sided exponential bounds
     `4 ^ m ≤ (m + 1) ^ 2 * catalan m` and `catalan m ≤ 4 ^ m` (`catalan_two_sided_exponential_bounds`,
     pinning the combinatorial entropy rate to `ln 2` per puncture with the `-3/2 ln N_Σ`
     Kaul–Majumdar subleading term).
   - Over `[CommRing R]` (`q : Rˣ`), the `TL_n(q)` loop fugacity `qTwo q = q + q⁻¹` and Jones
     index `jonesSubfactorIndex q = [2]_q²` satisfy `[2]_q² = 1 + [3]_q` and the 4-puncture
     Clebsch–Gordan identity `[2]_q⁴ = catalan 2 * 1 + 3 * [3]_q + [5]_q` (`qTwo_fourth_clebsch_gordan`),
     alongside Woronowicz Haar single-puncture weights `q² / (1 + q²)` and `1 / (1 + q²)`.
   - **Honest Bekenstein–Hawking Lock Diagnosis:** `S = A / (4 ℓ_P²)` holds **iff** the
     dimensionless puncture area quantum satisfies `a0 = 4 * s_punct` (`horizon_quarter_area_lock_iff`),
     which **fails** for un-tuned `a0 = 1` whenever `s_punct ≠ 1 / 4` (`unit_puncture_area_misses_quarter_law`).
     The unproved Lorentzian CR / Light-Cone null-focusing bridge (Bisognano–Wichmann `2π`
     modular boost entropy + Einstein–Raychaudhuri `8π G / c³` null focusing) is isolated as
     the **zero-instance primary conjecture class** `LCQHorizonPunctureAreaConjecture` (Rule 13a,
     §3b-cond), from which both `S = A / (4 ℓ_{P,grav}²)` and `a0 = 4 * s_punct` are derived
     sorry-free (`bekenstein_hawking_and_puncture_lock_of_lcq`).
-/

-- Ref: [leitner2026] information-theory, rem:spacetime-length-distance-layers
-- Ref: [leitner2026] gravity-spacetime, cr-structure-lorentzian-lift
-- Ref: [bekenstein1973] Bekenstein, Phys. Rev. D 7 (1973), 2333–2346.
-- Ref: [hawking1975] Hawking, Commun. Math. Phys. 43 (1975), 199–220.
-- Ref: [jacobson1995] Jacobson, Phys. Rev. Lett. 75 (1995), 1260–1263.
-- Ref: [temperley-lieb1971] Temperley & Lieb, Proc. R. Soc. Lond. A 322 (1971), 251–280.
-- Ref: [woronowicz1987] Woronowicz, Publ. RIMS 23 (1987), 117–181.
namespace QOU.GravitySpacetime.ReebLengthTimeAndLightConeEntropy

open scoped BigOperators
open QOU.InformationTheory.UnifiedClockScaleLayers
open QOU.InformationTheory.FiniteRieffelQuantumMetric
open QOU.AlgebraicSubstrate.SubstrateClock
open QOU.AlgebraicSubstrate

/-! ## 1. Layer-I Reeb Length, Computation Time, Causal Cone `c_q`, `𝔈 = 𝔪 c_q²`, and `G_Planck` -/

section ReebLengthTimeAndCausalCone

variable {K : Type*} [Field K]

/-- Normalised full-circuit Reeb/Planck displacement `ℓ_P(q) = ℏ_q · t_P(q)`. -/
def normalisedCircuitLength (q : K) : K :=
  hbarQ q * planckTick q

/-- Over any field `K` (`q ≠ 1`), one full Reeb circuit has unit normalised length `ℓ_P(q) = 1`. -/
theorem normalisedCircuitLength_eq_one {q : K} (hq1 : q ≠ 1) :
    normalisedCircuitLength q = 1 :=
  hbarQ_mul_planckTick hq1

/-- Reeb phase / modular computation time `Δt_comp(N, q) = N · ℏ_q` accumulated over
`steps = d_Reeb(γ) ∈ ℕ` elementary `f_q`-iterations. -/
def reebCompTime (q : K) (steps : ℕ) : K :=
  (steps : K) * hbarQ q

/-- Horizontal `D_∇` causal cone radius `Δx_cone(N, q) = N · q⁻¹` reached over `steps`
elementary `f_q`-iterations. -/
def horizConeRadius (q : K) (steps : ℕ) : K :=
  (steps : K) * q⁻¹

/-- Generic-field causal / Lieb–Robinson cone speed `c_q(q) = (q - 1)⁻¹`. -/
def causalSpeed (q : K) : K :=
  (q - 1)⁻¹

/-- `c_q(q)` is the exact ratio of the horizontal `D_∇` coupling `q⁻¹` to the vertical
Reeb share `ℏ_q = 1 - q⁻¹`. -/
theorem causalSpeed_eq_ratio {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    causalSpeed q = q⁻¹ / hbarQ q := by
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have hhb : hbarQ q ≠ 0 := hbarQ_ne_zero hq1
  unfold causalSpeed hbarQ
  field_simp [hq0, hsub, hhb]

/-- Exact Layer-I relation `c_q(q) + 1 = t_P(q)` (`1 / (q - 1) + 1 = q / (q - 1)`). -/
theorem causalSpeed_add_one_eq_planckTick {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    causalSpeed q + 1 = planckTick q := by
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  rw [planckTick_eq_div hq0 hq1]
  unfold causalSpeed
  field_simp [hsub]
  ring

/-- Product of Reeb share and causal speed in native `q`-connection units:
`ℏ_q · c_q(q) = q⁻¹` (approaching `1` only in the classical limit `q → 1`). -/
theorem hbarQ_mul_causalSpeed {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    hbarQ q * causalSpeed q = q⁻¹ := by
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  unfold hbarQ causalSpeed
  field_simp [hq0, hsub]

/-- **Lieb–Robinson / Braid Causal Cone Reconciliation:**
After `steps = d_Reeb(γ) ∈ ℕ` discrete iterations, the horizontal cone radius equals
`causalSpeed q` times the Reeb computation time: `Δx_cone(N, q) = c_q(q) · Δt_comp(N, q)`. -/
theorem lieb_robinson_cone_slope {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) (steps : ℕ) :
    horizConeRadius q steps = causalSpeed q * reebCompTime q steps := by
  unfold horizConeRadius reebCompTime
  calc (steps : K) * q⁻¹
      = (steps : K) * (hbarQ q * causalSpeed q) := by rw [hbarQ_mul_causalSpeed hq0 hq1]
    _ = causalSpeed q * ((steps : K) * hbarQ q) := by ring

/-- Categorical mass-energy relation `𝔈(q, 𝔪) = 𝔪 · c_q(q)²` (`def:mass-energy`, `qou-91w7`). -/
def categoricalEnergy (q m : K) : K :=
  m * (causalSpeed q) ^ 2

/-- Closed rational form `𝔈(q, 𝔪) = 𝔪 / (q - 1)²` and share-scaled identity
`𝔈(q, 𝔪) · ℏ_q² = 𝔪 · (q⁻¹)²` over any field `K` (`q ≠ 0`, `q ≠ 1`). -/
theorem categoricalEnergy_identities {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) (m : K) :
    categoricalEnergy q m = m / (q - 1) ^ 2 ∧
      categoricalEnergy q m * (hbarQ q) ^ 2 = m * (q⁻¹) ^ 2 := by
  refine ⟨?_, ?_⟩
  · unfold categoricalEnergy causalSpeed
    rw [div_eq_mul_inv, inv_pow]
  · unfold categoricalEnergy
    calc m * (causalSpeed q) ^ 2 * (hbarQ q) ^ 2
        = m * (hbarQ q * causalSpeed q) ^ 2 := by ring
      _ = m * (q⁻¹) ^ 2 := by rw [hbarQ_mul_causalSpeed hq0 hq1]

/-- Generic-field operational entropy `η_q = (2q - 1) / q³`. -/
def operationalEntropyG (q : K) : K :=
  (2 * q - 1) / q ^ 3

/-- Generic-field cumulative jet-tower cell entropy `S_cell(q) = η_q · ℏ_q² / (1 - ℏ_q²)`. -/
def cellEntropyG (q : K) : K :=
  operationalEntropyG q * (hbarQ q) ^ 2 / (1 - (hbarQ q) ^ 2)

/-- Generic-field gravitational coupling `G_q = c_q³ · ℏ_q / S_cell(q)`. -/
def gravCouplingG (q : K) : K :=
  (causalSpeed q) ^ 3 * hbarQ q / cellEntropyG q

/-- Exact algebraic simplification `S_cell(q) = (q - 1)² / q³` over any field `K`
(`q ≠ 0`, `2q - 1 ≠ 0`). -/
theorem cellEntropyG_closed_form {q : K} (hq0 : q ≠ 0) (h2q : 2 * q - 1 ≠ 0) :
    cellEntropyG q = (q - 1) ^ 2 / q ^ 3 := by
  unfold cellEntropyG operationalEntropyG hbarQ
  have h1mb : 1 - (1 - q⁻¹) ^ 2 = (2 * q - 1) / q ^ 2 := by
    field_simp [hq0]
    ring
  rw [h1mb]
  field_simp [hq0, h2q]

/-- Exact closed form `G_q = q² / (q - 1)⁴` over any field `K` (`q ≠ 0`, `q ≠ 1`, `2q - 1 ≠ 0`). -/
theorem gravCouplingG_closed_form {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) (h2q : 2 * q - 1 ≠ 0) :
    gravCouplingG q = q ^ 2 / (q - 1) ^ 4 := by
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  unfold gravCouplingG causalSpeed
  rw [cellEntropyG_closed_form hq0 h2q]
  unfold hbarQ
  field_simp [hq0, hsub]

/-- **Dual Substrate Gravitational Normalisations (`G_Planck = 1` vs `ℏ_q G_q / c_q³ = q`):**
Over any field `K` (`q ≠ 0`, `q ≠ 1`, `2q - 1 ≠ 0`):
1. `G_q · (ℏ_q / c_q)² = 1` (the `def:gravitational-constant` Planck identity, proved here
   without `ℝ` or ordering), and
2. `ℏ_q · G_q / c_q³ = ℏ_q² / S_cell(q) = q` (differing from `1` by `(ℏ_q · c_q)⁻¹ = q`). -/
theorem gravCoupling_planck_units_and_newton_area {q : K}
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) (h2q : 2 * q - 1 ≠ 0) :
    gravCouplingG q * (hbarQ q / causalSpeed q) ^ 2 = 1 ∧
      hbarQ q * gravCouplingG q / (causalSpeed q) ^ 3 = q ∧
      (hbarQ q) ^ 2 / cellEntropyG q = q := by
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  rw [gravCouplingG_closed_form hq0 hq1 h2q, cellEntropyG_closed_form hq0 h2q]
  unfold hbarQ causalSpeed
  refine ⟨?_, ?_, ?_⟩
  · field_simp [hq0, hsub]
  · field_simp [hq0, hsub]
  · field_simp [hq0, hsub]

end ReebLengthTimeAndCausalCone

/-! ## 2. KMS Modular Computation Time vs Traciality Obstruction -/

section KMSModularClockVsTraciality

/-- **Tomita–Takesaki Traciality Obstruction (`kms-length-dynamics`):**
Over any commutative ring `R` and `R`-algebra `A`, if a linear functional `φ : A →ₗ[R] R`
is normalized (`φ 1 = 1`), then any scalar KMS factor `ω : R` satisfying
`φ(u⁻¹ * (ω • u)) = φ(u * u⁻¹)` on a unit `u : Aˣ` (as forced by traciality
`φ(u⁻¹ * u) = φ(u * u⁻¹)`) must equal `1` (zero modular inverse temperature `β = 0`). -/
theorem tracial_kms_grading_trivial {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (φ : A →ₗ[R] R) (h1 : φ 1 = 1)
    (u : Aˣ) (ω : R)
    (hkms : φ ((↑u⁻¹ : A) * (ω • (u : A))) = φ ((u : A) * (↑u⁻¹ : A))) :
    ω = 1 := by
  have lhs : φ ((↑u⁻¹ : A) * (ω • (u : A))) = ω := by
    rw [mul_smul_comm, Units.inv_mul, LinearMap.map_smul, h1, smul_eq_mul, mul_one]
  have rhs : φ ((u : A) * (↑u⁻¹ : A)) = 1 := by
    rw [Units.mul_inv, h1]
  exact lhs.symm.trans (hkms.trans rhs)

/-- **Hecke Inhomogeneous Quadratic Grading Obstruction:**
Over any field `K`, if the Hecke deformation parameter `h = q - q⁻¹` is non-zero (`h ≠ 0`),
no scalar grading factor `ω ≠ 1` can simultaneously scale `T_s ↦ ω T_s` and preserve the
inhomogeneous quadratic relation `T_s² = h T_s + 1` (`ω² * h = ω * h` and `ω² = 1`). -/
theorem hecke_quadratic_grading_trivial {K : Type*} [Field K]
    {h ω : K} (hh : h ≠ 0) (hlin : ω ^ 2 * h = ω * h) (hconst : ω ^ 2 = 1) :
    ω = 1 := by
  have hmul : ω * h = 1 * h := by
    rw [← hlin, hconst]
  exact mul_right_cancel₀ hh hmul

/-- **Non-Tracial Density-Weighted Discrete KMS Clock:**
For any tracial `R`-linear functional `τ : A →ₗ[R] R` (`∀ a b, τ(a * b) = τ(b * a)`) and
any invertible modular density element `D : Aˣ`, the non-tracial state
`φ_D(x) := τ((D : A) * x)` and inner modular step `σ_mod(y) := D * y * D⁻¹` satisfy the
exact discrete KMS swap `φ_D(x * σ_mod(y)) = φ_D(y * x)` for all `x, y : A`. -/
theorem density_weighted_discrete_kms {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (τ : A →ₗ[R] R) (htr : ∀ a b : A, τ (a * b) = τ (b * a))
    (D : Aˣ) (x y : A) :
    τ ((D : A) * (x * ((D : A) * y * (↑D⁻¹ : A)))) = τ ((D : A) * (y * x)) := by
  calc τ ((D : A) * (x * ((D : A) * y * (↑D⁻¹ : A))))
      = τ ((((D : A) * x * ((D : A) * y)) * (↑D⁻¹ : A))) := by simp only [mul_assoc]
    _ = τ ((↑D⁻¹ : A) * ((D : A) * x * ((D : A) * y))) := htr _ (↑D⁻¹ : A)
    _ = τ ((((↑D⁻¹ : A) * (D : A)) * x) * ((D : A) * y)) := by simp only [mul_assoc]
    _ = τ (x * ((D : A) * y)) := by rw [Units.inv_mul, one_mul]
    _ = τ (((D : A) * y) * x) := htr x ((D : A) * y)
    _ = τ ((D : A) * (y * x)) := by simp only [mul_assoc]

/-- **Woronowicz `O_q(SU(2))` Modular Clock Step (`OqSU2ModularNakayama` Bridge):**
Iterating Woronowicz's modular automorphism `nuAlgEquiv q` `n` times scales generator
`α q` by `((q : R) ^ 2) ^ n` (`n` discrete modular clock ticks of factor `q²`). -/
theorem oqsu2_modular_clock_iterate {R : Type*} [CommRing R] (q : Rˣ) (n : ℕ) :
    ((OqSU2.nuAlgEquiv (R := R) q)^[n]) (OqSU2.α q) =
      (((q : R) ^ 2) ^ n) • OqSU2.α (R := R) q := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply', ih, map_smul, OqSU2.nuAlgEquiv_alpha, smul_smul, ← pow_succ]

end KMSModularClockVsTraciality

/-! ## 3. Layer-II/III Rieffel Step-Cost Split & `L_cal` Boundary Unit-Conversion Torsor -/

section RieffelStepCostAndBoundaryCalibration

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
variable {A : Type*} [Ring A] [Algebra K A]

/-- Under `D_∇ = q⁻¹ ∇_hor + ℏ_q ι_ξ ∇`, `steps` paired horizontal + Reeb transitions
have combined cost `steps * q⁻¹ + steps * hbarQ q = steps`, reconciling the unit step count
with the `q⁻¹ / ℏ_q` convex split. -/
theorem dirac_split_step_cost_identity {q : K} (steps : ℕ) :
    horizConeRadius q steps + reebCompTime q steps = (steps : K) := by
  unfold horizConeRadius reebCompTime hbarQ
  ring

/-- Rescaling a `LipSeminorm K A` by `L_cal⁻¹` (`L_cal > 0`), modeling conversion from
dimensionless Layer-II substrate distance to laboratory length units `L_cal`. -/
def rescaleLipInv (L : LipSeminorm K A) (L_cal : K) (hL : 0 < L_cal) : LipSeminorm K A where
  toFun a := L_cal⁻¹ * L.toFun a
  nonneg a := mul_nonneg (inv_nonneg.mpr (le_of_lt hL)) (L.nonneg a)
  map_one := by rw [L.map_one, mul_zero]
  homog c a := by rw [L.homog]; ring
  subadd a b := by
    have hinv : 0 ≤ L_cal⁻¹ := inv_nonneg.mpr (le_of_lt hL)
    calc L_cal⁻¹ * L.toFun (a + b)
        ≤ L_cal⁻¹ * (L.toFun a + L.toFun b) := mul_le_mul_of_nonneg_left (L.subadd a b) hinv
      _ = L_cal⁻¹ * L.toFun a + L_cal⁻¹ * L.toFun b := by ring

/-- **Rieffel Distance Equivariance under `L_cal`:**
`L_cal * d` is a dual Rieffel–Kantorovich distance bound for `rescaleLipInv L L_cal hL`
iff `d` is a dual distance bound for the dimensionless substrate seminorm `L`. -/
theorem rescaleLipInv_dualBound_iff (L : LipSeminorm K A) {L_cal : K} (hL : 0 < L_cal)
    (φ ψ : UnitalState K A) (d : K) :
    IsDualBound (rescaleLipInv L L_cal hL) φ ψ (L_cal * d) ↔ IsDualBound L φ ψ d := by
  have hLne : L_cal ≠ 0 := ne_of_gt hL
  have hLinv_pos : 0 < L_cal⁻¹ := inv_pos.mpr hL
  constructor
  · intro hcal a ha
    have ha' : IsLipOne (rescaleLipInv L L_cal hL) (L_cal • a) := by
      unfold IsLipOne rescaleLipInv
      dsimp only
      rw [L.homog, abs_of_pos hL, ← mul_assoc, inv_mul_cancel₀ hLne, one_mul]
      exact ha
    have hbd := hcal (L_cal • a) ha'
    simp only [LinearMap.map_smul, smul_eq_mul, ← mul_sub, abs_mul, abs_of_pos hL] at hbd
    exact le_of_mul_le_mul_left hbd hL
  · intro hsub b hb
    unfold IsLipOne rescaleLipInv at hb
    dsimp only at hb
    have hb' : IsLipOne L (L_cal⁻¹ • b) := by
      unfold IsLipOne
      rw [L.homog, abs_of_pos hLinv_pos]
      exact hb
    have hbd := hsub (L_cal⁻¹ • b) hb'
    simp only [LinearMap.map_smul, smul_eq_mul, ← mul_sub, abs_mul, abs_of_pos hLinv_pos] at hbd
    have hmul := mul_le_mul_of_nonneg_left hbd (le_of_lt hL)
    rwa [← mul_assoc, mul_inv_cancel₀ hLne, one_mul] at hmul

/-- **`L_cal` Cancels Identically from All Comparison-Boundary Dimensionless Observables:**
For any non-zero calibration length `L_cal ≠ 0`:
1. Length ratios `(L_cal * x) / (L_cal * y) = x / y`,
2. Calibrated causal cone slope `(L_cal * horizConeRadius q N) / (L_cal * reebCompTime q N) = causalSpeed q` (`N ≠ 0`),
3. Calibrated Bekenstein–Hawking area ratio `(L_cal ^ 2 * A_sub) / (4 * (L_cal * ellP_sub) ^ 2) = A_sub / (4 * ellP_sub ^ 2)`. -/
theorem calibration_cancels_in_observables {L_cal q x y A_sub ellP_sub : K}
    (hL : L_cal ≠ 0) (hq0 : q ≠ 0) (hq1 : q ≠ 1) {N : ℕ} (hN : (N : K) ≠ 0) :
    (L_cal * x) / (L_cal * y) = x / y ∧
      (L_cal * horizConeRadius q N) / (L_cal * reebCompTime q N) = causalSpeed q ∧
      (L_cal ^ 2 * A_sub) / (4 * (L_cal * ellP_sub) ^ 2) = A_sub / (4 * ellP_sub ^ 2) := by
  have hhb : hbarQ q ≠ 0 := hbarQ_ne_zero hq1
  refine ⟨mul_div_mul_left x y hL, ?_, ?_⟩
  · rw [mul_div_mul_left _ _ hL, lieb_robinson_cone_slope hq0 hq1 N]
    unfold reebCompTime
    have hrt : (N : K) * hbarQ q ≠ 0 := mul_ne_zero hN hhb
    exact mul_div_cancel_right₀ (causalSpeed q) hrt
  · have h4 : 4 * (L_cal * ellP_sub) ^ 2 = L_cal ^ 2 * (4 * ellP_sub ^ 2) := by ring
    rw [h4, mul_div_mul_left A_sub (4 * ellP_sub ^ 2) (pow_ne_zero 2 hL)]

end RieffelStepCostAndBoundaryCalibration

/-! ## 4. Light-Cone (`LCQ`) Horizon Channel Counting & Rule-13a Area Conjecture -/

section LightConeHorizonChannelCountingAndConjecture

/-- Exact `U_q(𝔰𝔩₂)` / Temperley–Lieb singlet state-space dimension `dim ℋ_singlet(N_Σ)`
on a causal horizon cut pierced by `nPunct` spin-`1/2` punctures (at non-root-of-unity `q`):
`0` for odd `nPunct` (weight parity obstruction) and `catalan (nPunct / 2)` for even `nPunct`. -/
def tlSingletDim (nPunct : ℕ) : ℕ :=
  if nPunct % 2 = 0 then catalan (nPunct / 2) else 0

/-- Odd puncture count `2m + 1` admits zero `U_q(𝔰𝔩₂)` singlets. -/
theorem tlSingletDim_odd (m : ℕ) : tlSingletDim (2 * m + 1) = 0 := by
  unfold tlSingletDim
  have hmod : (2 * m + 1) % 2 = 1 := by omega
  simp [hmod]

/-- Even puncture count `2m` has exact singlet dimension `catalan m`. -/
theorem tlSingletDim_even (m : ℕ) : tlSingletDim (2 * m) = catalan m := by
  unfold tlSingletDim
  have hmod : (2 * m) % 2 = 0 := by omega
  have hdiv : (2 * m) / 2 = m := by omega
  simp [hmod, hdiv]

/-- Exact multiplicative recurrence `(m + 2) * catalan (m + 1) = 2 * (2 * m + 1) * catalan m`. -/
theorem catalan_step_recurrence (m : ℕ) :
    (m + 2) * catalan (m + 1) = 2 * (2 * m + 1) * catalan m := by
  have hc1 : (m + 2) * catalan (m + 1) = (m + 1).centralBinom :=
    succ_mul_catalan_eq_centralBinom (m + 1)
  have hc0 : (m + 1) * catalan m = m.centralBinom :=
    succ_mul_catalan_eq_centralBinom m
  have hstep : (m + 1) * ((m + 2) * catalan (m + 1)) =
      (m + 1) * (2 * (2 * m + 1) * catalan m) := by
    rw [hc1, Nat.succ_mul_centralBinom_succ m, ← hc0]
    ring
  exact Nat.eq_of_mul_eq_mul_left (Nat.succ_pos m) hstep

/-- Central binomial upper bound `m.centralBinom ≤ 4 ^ m` (the `U(1)` zero-magnetization
slice inside `2 ^ (2m) = 4 ^ m`). -/
theorem centralBinom_le_four_pow (m : ℕ) : m.centralBinom ≤ 4 ^ m := by
  induction m with
  | zero => simp
  | succ k ih =>
    have hmul : (k + 1) * (k + 1).centralBinom ≤ (k + 1) * 4 ^ (k + 1) := by
      rw [Nat.succ_mul_centralBinom_succ k, pow_succ]
      have hcoef : 2 * (2 * k + 1) ≤ (k + 1) * 4 := by omega
      calc 2 * (2 * k + 1) * k.centralBinom
          ≤ ((k + 1) * 4) * 4 ^ k := Nat.mul_le_mul hcoef ih
        _ = (k + 1) * (4 ^ k * 4) := by ring
    exact Nat.le_of_mul_le_mul_left hmul (Nat.succ_pos k)

/-- **Two-Sided Exponential Catalan Squeeze (`4^m / (m+1)² ≤ C_m ≤ 4^m`):**
Proves purely over `ℕ` that `tlSingletDim (2 * m) = catalan m` satisfies
`4 ^ m ≤ (m + 1) ^ 2 * catalan m` and `catalan m ≤ 4 ^ m` for every `m : ℕ`, pinning
the asymptotic microcanonical entropy per puncture to `(1/2) ln 4 = ln 2` with polynomial
prefactor deficit (sharpened by Stirling to Kaul–Majumdar's `-3/2 ln N_Σ`). -/
theorem catalan_two_sided_exponential_bounds (m : ℕ) :
    4 ^ m ≤ (m + 1) ^ 2 * catalan m ∧ catalan m ≤ 4 ^ m := by
  refine ⟨?_, ?_⟩
  · induction m with
    | zero => simp [catalan_zero]
    | succ k ih =>
      have hstep : (k + 1) * 4 ^ (k + 1) ≤ (k + 1) * ((k + 2) ^ 2 * catalan (k + 1)) := by
        calc (k + 1) * 4 ^ (k + 1)
            = 4 * (k + 1) * 4 ^ k := by rw [pow_succ]; ring
          _ ≤ 4 * (k + 1) * ((k + 1) ^ 2 * catalan k) :=
              Nat.mul_le_mul_left (4 * (k + 1)) ih
          _ = (4 * (k + 1) ^ 2) * ((k + 1) * catalan k) := by ring
          _ ≤ (2 * (k + 2) * (2 * k + 1)) * ((k + 1) * catalan k) := by
              apply Nat.mul_le_mul_right
              nlinarith
          _ = (k + 1) * ((k + 2) * (2 * (2 * k + 1) * catalan k)) := by ring
          _ = (k + 1) * ((k + 2) * ((k + 2) * catalan (k + 1))) := by
              rw [← catalan_step_recurrence k]
          _ = (k + 1) * ((k + 2) ^ 2 * catalan (k + 1)) := by ring
      exact Nat.le_of_mul_le_mul_left hstep (Nat.succ_pos k)
  · have hle : catalan m ≤ (m + 1) * catalan m :=
      Nat.le_mul_of_pos_left (catalan m) (Nat.succ_pos m)
    rw [succ_mul_catalan_eq_centralBinom] at hle
    exact le_trans hle (centralBinom_le_four_pow m)

/-- Balanced spin-`1/2` quantum dimension / `TL_n(q)` loop fugacity `[2]_q = q + q⁻¹`. -/
def qTwo {R : Type*} [CommRing R] (q : Rˣ) : R :=
  (q : R) + ((q⁻¹ : Rˣ) : R)

/-- Balanced spin-`1` / adjoint quantum dimension `[3]_q = q² + 1 + q⁻²`. -/
def qThree {R : Type*} [CommRing R] (q : Rˣ) : R :=
  (q : R) ^ 2 + 1 + ((q⁻¹ : Rˣ) : R) ^ 2

/-- Jones subfactor index `[M : N] = [2]_q²` of a minimal Temperley–Lieb strand inclusion. -/
def jonesSubfactorIndex {R : Type*} [CommRing R] (q : Rˣ) : R :=
  (qTwo q) ^ 2

/-- Two-puncture Clebsch–Gordan quantum-dimension identity `[2]_q² = 1 + [3]_q`
(`V_{1/2} ⊗ V_{1/2} ≅ V_0 ⊕ V_1`, singlet multiplicity `C_1 = 1`). -/
theorem qTwo_sq_eq_one_add_qThree {R : Type*} [CommRing R] (q : Rˣ) :
    jonesSubfactorIndex q = 1 + qThree q := by
  unfold jonesSubfactorIndex qTwo qThree
  have hqq : (q : R) * ((q⁻¹ : Rˣ) : R) = 1 := Units.mul_inv q
  linear_combination 2 * hqq

/-- Four-puncture Clebsch–Gordan quantum-dimension decomposition:
`[2]_q⁴ = catalan 2 · 1 + 3 · [3]_q + [5]_q` (`V_{1/2}^{⊗ 4} ≅ 2 V_0 ⊕ 3 V_1 ⊕ V_2`),
exhibiting the Catalan singlet multiplicity `catalan 2 = 2` inside `[2]_q⁴` over any `[CommRing R]`. -/
theorem qTwo_fourth_clebsch_gordan {R : Type*} [CommRing R] (q : Rˣ) :
    (qTwo q) ^ 4 =
      (catalan 2 : R) * 1 + 3 * qThree q +
        ((q : R) ^ 4 + (q : R) ^ 2 + 1 + ((q⁻¹ : Rˣ) : R) ^ 2 + ((q⁻¹ : Rˣ) : R) ^ 4) := by
  have hc2 : catalan 2 = 2 := by
    have h := catalan_step_recurrence 1
    rw [catalan_one] at h
    change 3 * catalan 2 = 6 at h
    omega
  rw [hc2]
  push_cast
  unfold qTwo qThree
  have hqq : (q : R) * ((q⁻¹ : Rˣ) : R) = 1 := Units.mul_inv q
  have hqq2 : (q : R) ^ 2 * ((q⁻¹ : Rˣ) : R) ^ 2 = 1 := by
    calc (q : R) ^ 2 * ((q⁻¹ : Rˣ) : R) ^ 2
        = ((q : R) * ((q⁻¹ : Rˣ) : R)) ^ 2 := by ring
      _ = 1 := by rw [hqq]; ring
  linear_combination (4 * (q : R) ^ 2 + 4 * ((q⁻¹ : Rˣ) : R) ^ 2) * hqq + 6 * hqq2

/-- Woronowicz Haar single-puncture modular spin-`1/2` weights `p_+ = q² / (1 + q²)` and
`p_- = 1 / (1 + q²)` satisfy `p_+ + p_- = 1`, `p_+ - p_- = (q - q⁻¹) / (q + q⁻¹)`, and
modular ratio `p_+ / p_- = q²` over any field `K` (`q ≠ 0`, `1 + q² ≠ 0`, `q + q⁻¹ ≠ 0`). -/
theorem woronowicz_haar_puncture_weights {K : Type*} [Field K] {q : K}
    (hq0 : q ≠ 0) (h1q2 : 1 + q ^ 2 ≠ 0) (hqsum : q + q⁻¹ ≠ 0) :
    let pPlus := q ^ 2 / (1 + q ^ 2)
    let pMinus := 1 / (1 + q ^ 2)
    pPlus + pMinus = 1 ∧
      pPlus - pMinus = (q - q⁻¹) / (q + q⁻¹) ∧
      pPlus / pMinus = q ^ 2 := by
  dsimp only
  refine ⟨?_, ?_, ?_⟩
  · field_simp [h1q2]
    ring
  · rw [div_sub_div_same, div_eq_div_iff h1q2 hqsum]
    field_simp [hq0]
    ring
  · field_simp [h1q2]

/-- **Exact Bekenstein–Hawking Puncture Area Lock Equivalence:**
Over any field `K` (`CharZero K`), for `nPunct ≠ 0` horizon punctures of elementary area
`ΔA = a0 * ellP²` (`A = nPunct * a0 * ellP²`, `ellP ≠ 0`, `a0 ≠ 0`) and extensive channel
entropy `S = nPunct * s_punct`, the Bekenstein–Hawking quarter-area law `S = A / (4 * ellP²)`
holds **if and only if** `a0 = 4 * s_punct`. -/
theorem horizon_quarter_area_lock_iff {K : Type*} [Field K] [CharZero K]
    {nPunct a0 ellP s_punct : K} (hN : nPunct ≠ 0) (hell : ellP ≠ 0) :
    nPunct * s_punct = (nPunct * a0 * ellP ^ 2) / (4 * ellP ^ 2) ↔ a0 = 4 * s_punct := by
  have h4 : (4 : K) ≠ 0 := by exact_mod_cast (by decide : (4 : ℕ) ≠ 0)
  have h4ell : 4 * ellP ^ 2 ≠ 0 := mul_ne_zero h4 (pow_ne_zero 2 hell)
  rw [eq_div_iff h4ell]
  constructor
  · intro h
    have hcancel : (nPunct * (4 * ellP ^ 2)) * (4 * s_punct) =
        (nPunct * (4 * ellP ^ 2)) * a0 := by
      linear_combination 4 * h
    exact (mul_left_cancel₀ (mul_ne_zero hN h4ell) hcancel).symm
  · intro ha0
    rw [ha0]
    ring

/-- **Honest Non-Tautology Refutation (`a0 = 1` Fails Quarter-Area Law Without Lock):**
If the elementary puncture area is set to the naive unit cell `a0 = 1`, then for every
channel entropy rate `s_punct ≠ 1 / 4` (including `ln 2`, `ln [2]_{q_0}`, and `ln [3]_{q_0}`),
`nPunct * s_punct ≠ (nPunct * 1 * ellP²) / (4 * ellP²)`. -/
theorem unit_puncture_area_misses_quarter_law {K : Type*} [Field K] [CharZero K]
    {nPunct ellP s_punct : K} (hN : nPunct ≠ 0) (hell : ellP ≠ 0) (hs : s_punct ≠ 1 / 4) :
    nPunct * s_punct ≠ (nPunct * 1 * ellP ^ 2) / (4 * ellP ^ 2) := by
  intro heq
  have hlock : (1 : K) = 4 * s_punct :=
    (horizon_quarter_area_lock_iff hN hell).mp heq
  apply hs
  have h4 : (4 : K) ≠ 0 := by exact_mod_cast (by decide : (4 : ℕ) ≠ 0)
  rw [eq_div_iff h4]
  linear_combination -hlock

/-- **Primary Conjecture Class (OPEN — ZERO instances; Rule 13a & §3b-cond):**
Isolates the two unproved Lorentzian CR / Light-Cone (`LCQ`) geometric premises required
to derive `S = A / (4 ℓ_{P,grav}²)` and fix `a0 = 4 * s_punct` without parameter tuning:
1. `modular_boost_entropy`: Bisognano–Wichmann / Unruh light-cone modular relation
   `S_hor(N) = (twoPi / hbar) * K_boost(N)` across the Rindler/null horizon cut (where
   `twoPi` denotes the Euclidean modular circle period `2π`), alongside microscopic
   puncture channel extensivity `S_hor(N) = N * s_punct`;
2. `raychaudhuri_null_focusing`: Einstein–Raychaudhuri null-sheet focusing on the Lorentzian
   lift of the CR structure (`cr-structure-lorentzian-lift`), `A_hor(N) = (4 * twoPi * G_grav / c³) * K_boost(N)`
   (where `4 * twoPi = 8π`).

Neither premise states the conclusion `S = A / (4 ℓ_P²)` or `a0 = 4 * s_punct`; both
conclusions are derived below by cancelling `twoPi` and `K_boost(N)`. -/
-- @conjecture: primary
class LCQHorizonPunctureAreaConjecture {K : Type*} [Field K]
    (twoPi hbar c G_grav s_punct : K)
    (S_hor A_hor K_boost : K → K) : Prop where
  /-- Microscopic extensive puncture channel count `S_hor(N) = N * s_punct`. -/
  microscopic_channel_entropy : ∀ nPunct : K, S_hor nPunct = nPunct * s_punct
  /-- Bisognano–Wichmann / Unruh modular horizon boost law `S_hor(N) = (2π / ℏ) K_boost(N)`. -/
  modular_boost_entropy : ∀ nPunct : K, S_hor nPunct = (twoPi / hbar) * K_boost nPunct
  /-- Einstein–Raychaudhuri null-sheet focusing law `A_hor(N) = (8π G / c³) K_boost(N)`. -/
  raychaudhuri_null_focusing : ∀ nPunct : K,
    A_hor nPunct = (4 * twoPi * G_grav / c ^ 3) * K_boost nPunct

/-- **Conditional Theorem (`§3b-cond` — derived from `LCQHorizonPunctureAreaConjecture`):**
Assuming `LCQHorizonPunctureAreaConjecture`, the modular boost period `twoPi` and boost
energy `K_boost(N)` cancel identically between `modular_boost_entropy` and
`raychaudhuri_null_focusing`, yielding:
1. `S_hor(N) = A_hor(N) / (4 * (hbar * G_grav / c³))` (`S = A / (4 ℓ_{P,grav}²)`), and
2. whenever `A_hor(N) = N * a0 * (hbar * G_grav / c³)` for `N ≠ 0`, the elementary puncture
   area quantum is uniquely locked to `a0 = 4 * s_punct`. -/
theorem bekenstein_hawking_and_puncture_lock_of_lcq {K : Type*} [Field K] [CharZero K]
    {twoPi hbar c G_grav s_punct : K} {S_hor A_hor K_boost : K → K}
    [hLCQ : LCQHorizonPunctureAreaConjecture twoPi hbar c G_grav s_punct S_hor A_hor K_boost]
    (htwoPi : twoPi ≠ 0) (hhbar : hbar ≠ 0) (hc : c ≠ 0) (hG : G_grav ≠ 0) :
    let ellP_sq := hbar * G_grav / c ^ 3
    (∀ nPunct : K, S_hor nPunct = A_hor nPunct / (4 * ellP_sq)) ∧
      (∀ nPunct a0 : K, nPunct ≠ 0 → A_hor nPunct = nPunct * a0 * ellP_sq →
        a0 = 4 * s_punct) := by
  dsimp only
  have h4 : (4 : K) ≠ 0 := by exact_mod_cast (by decide : (4 : ℕ) ≠ 0)
  have hc3 : c ^ 3 ≠ 0 := pow_ne_zero 3 hc
  have hell_sq : hbar * G_grav / c ^ 3 ≠ 0 :=
    div_ne_zero (mul_ne_zero hhbar hG) hc3
  have hquarter : ∀ nPunct : K,
      S_hor nPunct = A_hor nPunct / (4 * (hbar * G_grav / c ^ 3)) := by
    intro nPunct
    rw [hLCQ.modular_boost_entropy nPunct, hLCQ.raychaudhuri_null_focusing nPunct]
    field_simp [htwoPi, hhbar, hc3, hG, h4]
  refine ⟨hquarter, ?_⟩
  intro nPunct a0 hN hA
  have hS := hquarter nPunct
  rw [hLCQ.microscopic_channel_entropy nPunct, hA] at hS
  have h4ell : 4 * (hbar * G_grav / c ^ 3) ≠ 0 := mul_ne_zero h4 hell_sq
  rw [eq_div_iff h4ell] at hS
  have hcancel : (nPunct * (hbar * G_grav / c ^ 3)) * a0 =
      (nPunct * (hbar * G_grav / c ^ 3)) * (4 * s_punct) := by
    linear_combination -hS
  exact mul_left_cancel₀ (mul_ne_zero hN hell_sq) hcancel

end LightConeHorizonChannelCountingAndConjecture

end QOU.GravitySpacetime.ReebLengthTimeAndLightConeEntropy
