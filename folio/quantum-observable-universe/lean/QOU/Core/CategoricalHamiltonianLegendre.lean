import QOU.Core.QDifferentialGeometry
import QOU.Core.CategoricalLagrangianTwoTermBridge
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Categorical Hamiltonian, Phase-Space Legendre Transform, Worldline `E = m c_q²`, and LP Shadow-Price Bridge

Unifies the primitive definition of energy in the Quantum Observable Universe (`def:categorical-hamiltonian`)
from `QOU.CategoricalDiracOperator` and `QOU.CategoricalLagrangian` (`QOU.Core.QDifferentialGeometry`,
`QOU.Core.CategoricalLagrangianTwoTermBridge`) across four layers:

1. **Operator Reeb-Velocity Legendre Transform (`[CommRing R]`, Preadditive `R`-Linear Monoidal Category `C`):**
   - `lagrangian_reeb_degree_decomposition`: decomposes `L.lagrangian = reebSqTerm L + reebLinearTerm L + spatialZeroTerm L`
     by degree `(2, 1, 0)` in `L.dirac.reeb`, without assuming `2` is invertible or that `nablaEndo` and `reeb` commute.
   - `CategoricalHamiltonianVel` & `categoricalHamiltonianVel_eq`: defines the Euler directional Legendre transform
     `(2 : R) • reebSqTerm L + reebLinearTerm L - L.lagrangian` along the Reeb velocity `L.dirac.reeb` and proves
     exact cancellation of the degree-`1` gyroscopic/Berry and Reeb-matter terms:
     `CategoricalHamiltonianVel L = reebSqTerm L - spatialZeroTerm L`.

2. **Phase-Space Canonical Reeb-Momentum Legendre Transform (`[Field K]` & Ordered Field):**
   - `lagrangianClock` & `canonicalHamiltonian`: for traced Reeb clock polynomial
     `L_clock(ω) = a₂ ω² + a₁ ω + a₀`, proves `p_reeb = 2 a₂ ω + a₁ ↔ ω = (p_reeb - a₁) / (2 a₂)` and
     `p_reeb * ω - L_clock(ω) = (p_reeb - a₁)² / (4 a₂) - a₀`.
   - `fenchel_legendre_le_canonicalHamiltonian` & `fenchel_legendre_eq_iff`: over an ordered field with
     `0 < a₂`, proves `∀ ω, p_reeb * ω - L_clock(ω) ≤ canonicalHamiltonian a₂ a₁ a₀ p_reeb` with equality iff
     `ω = (p_reeb - a₁) / (2 a₂)`.
   - `canonicalHamiltonian_unit_clock` & specializations: proves the unit-clock expansion at `p_reeb = 2 a₂`,
     `canonicalHamiltonian a₂ a₁ a₀ (2 * a₂) = a₂ - a₁ + a₁² / (4 * a₂) - a₀`, together with its rest-frame,
     minimal-coupling + Darwin/recoil, and shared-spatial nucleon difference corollaries.

3. **Causal-Cone Speed `c_q = 1 / (q - 1)` & Relativistic Worldline Legendre Derivation of `E = m_in c_q²`:**
   - `dirac_lightcone_speed_eq_cq`: proves `α_space / α_time = q⁻¹ / (1 - q⁻¹) = 1 / (q - 1) = c_q`.
   - `worldlineLagrangian_hasDerivAt_momentum`, `worldlineEnergy_eq`, `worldlineEnergy_lorentz_gamma`,
     `worldlineEnergy_rest`, & `worldline_mass_shell_identity`: over `ℝ` (`1 < q`, `|v| < c_q`), proves
     the exact calculus conjugate momentum `p = ∂L/∂v = m_in c_q v / √(c_q² - v²)`, the Newtonian kinetic
     recovery identity, the Legendre energy `E(v) = p v - L(v) = m_in c_q³ / √(c_q² - v²) = m_in c_q² / √(1 - v² / c_q²)`,
     the rest-frame theorem `E(0) = m_in c_q² = m_in / (q - 1)²`, and the exact mass-shell relation
     `E(v)² - p(v)² c_q² = (m_in c_q²)²`.
   - `BraidBoostInertialEquivalence` & `braidRestEnergy_eq_holonomyMass_div_sq_of_boost_equiv`:
     isolates the identification of boosted kinematic inertia `m_in(β)` with static Frobenius–Hopf
     holonomy mass `𝔪(β)` (`def:mass-identity`) as an honest zero-instance `§3b-cond` hypothesis class,
     yielding `braidRestEnergy β = 𝔪(β) / (q - 1)²`.

4. **Kantorovich / Fenchel LP-Dual Shadow-Price Theorem & Three-Unit-Chart Bridge:**
   - `kantorovich_lp_weak_duality`, `kantorovich_lp_eq_of_complementary_slackness`, &
     `kantorovich_lp_attained_on_min_sector`: proves `y₀ ≤ ∑ ρ_i H_i` for normalized sector weights
     `∑ d_i ρ_i = 1` with shadow prices `u_i = H_i / d_i - y₀ ≥ 0`, with equality on minimum-attaining sectors.
   - `three_unit_chart_bridge`: proves `(m_e * c_q²) / t_P = m_e * c_q² * ħ_q = m_e / (q * (q - 1)) = E₀`.

## References
- [leitner2026] Ch. 2 (`def:categorical-hamiltonian`) & Ch. 20 (`prop:mass-energy`)
- [connes1994] Noncommutative Geometry
- [kantorovich1939] Mathematical Methods of Organizing and Planning Production
-/

set_option autoImplicit false

open scoped CategoryTheory CategoryTheory.MonoidalCategory BigOperators
open CategoryTheory

namespace QOU.Core.CategoricalHamiltonianLegendre

universe u v

/-! ## 1. Operator Reeb-Velocity Legendre Transform (`[CommRing R]`) -/

section OperatorVelocityLegendre

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
  [Preadditive C] [Linear R C]
variable {fh : FrobeniusHopfData C}

/-- Degree-`2` component of `L.lagrangian` in the Reeb contraction `L.dirac.reeb`:
`((1 - q⁻¹)²) • (reeb ≫ reeb)`. -/
def reebSqTerm (L : CategoricalLagrangian R C fh) : fh.obj ⟶ fh.obj :=
  ((1 - L.dirac.qinv) * (1 - L.dirac.qinv)) • (L.dirac.reeb ≫ L.dirac.reeb)

/-- Degree-`1` component of `L.lagrangian` in `L.dirac.reeb`: the bosonic horizontal–Reeb
anticommutator cross-term plus the Reeb-contracted fermionic matter coupling. -/
def reebLinearTerm (L : CategoricalLagrangian R C fh) : fh.obj ⟶ fh.obj :=
  (L.dirac.qinv * (1 - L.dirac.qinv)) •
      (L.dirac.nablaEndo ≫ L.dirac.reeb + L.dirac.reeb ≫ L.dirac.nablaEndo) +
    (1 - L.dirac.qinv) • (L.costate ≫ L.state ≫ L.dirac.reeb)

/-- Degree-`0` (purely horizontal/spatial) component of `L.lagrangian` independent of `L.dirac.reeb`. -/
def spatialZeroTerm (L : CategoricalLagrangian R C fh) : fh.obj ⟶ fh.obj :=
  (L.dirac.qinv * L.dirac.qinv) • (L.dirac.nablaEndo ≫ L.dirac.nablaEndo) +
    L.dirac.qinv • (L.costate ≫ L.state ≫ L.dirac.nablaEndo)

/-- **Degree-`(2, 1, 0)` Reeb decomposition of `L.lagrangian`:**
`L.lagrangian = reebSqTerm L + reebLinearTerm L + spatialZeroTerm L` in `fh.obj ⟶ fh.obj`,
holding over any commutative ring `R` with zero commutativity assumptions between `nablaEndo`
and `reeb`. -/
theorem lagrangian_reeb_degree_decomposition (L : CategoricalLagrangian R C fh) :
    L.lagrangian = reebSqTerm L + reebLinearTerm L + spatialZeroTerm L := by
  rw [QOU.CategoricalLagrangianTwoTermBridge.lagrangian_five_term_expansion L]
  unfold reebSqTerm reebLinearTerm spatialZeroTerm
  abel

/-- **Operator Reeb-Velocity Legendre Transform (`D_v L[v] - L` along `v = L.dirac.reeb`):**
Defined over any commutative ring `R` without dividing by `2`. -/
def CategoricalHamiltonianVel (L : CategoricalLagrangian R C fh) : fh.obj ⟶ fh.obj :=
  (2 : R) • reebSqTerm L + reebLinearTerm L - L.lagrangian

/-- **Exact Degree-`1` Cancellation in Velocity Variables:**
`CategoricalHamiltonianVel L = reebSqTerm L - spatialZeroTerm L`; the linear gyroscopic/Berry
anticommutator and Reeb-matter coupling cancel identically in velocity variables. -/
theorem categoricalHamiltonianVel_eq (L : CategoricalLagrangian R C fh) :
    CategoricalHamiltonianVel L = reebSqTerm L - spatialZeroTerm L := by
  unfold CategoricalHamiltonianVel
  rw [two_smul R (reebSqTerm L), lagrangian_reeb_degree_decomposition L]
  abel

/-- **Traced Operator Velocity Hamiltonian Identity** under any `R`-linear trace functional
`τ : (fh.obj ⟶ fh.obj) →ₗ[R] R`. -/
theorem trace_categoricalHamiltonianVel_eq
    (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R) (L : CategoricalLagrangian R C fh) :
    τ (CategoricalHamiltonianVel L) = τ (reebSqTerm L) - τ (spatialZeroTerm L) := by
  rw [categoricalHamiltonianVel_eq L, map_sub]

end OperatorVelocityLegendre

/-! ## 2. Phase-Space Canonical Reeb-Momentum Legendre Transform (`[Field K]` & Ordered Field) -/

section PhaseSpaceCanonicalLegendre

/-- Scalar Reeb-clock polynomial `L_clock(ω) = a₂ ω² + a₁ ω + a₀` obtained by scaling
`L.dirac.reeb ↦ ω • L.dirac.reeb` and applying an `R`-linear trace `τ`. -/
def lagrangianClock {R : Type*} [CommRing R] (a₂ a₁ a₀ ω : R) : R :=
  a₂ * ω ^ 2 + a₁ * ω + a₀

/-- **Phase-Space Canonical Categorical Hamiltonian (`def:categorical-hamiltonian`):**
`H_can(a₂, a₁, a₀; p_reeb) = (p_reeb - a₁)² / (4 a₂) - a₀`, where `p_reeb = ∂L_clock/∂ω = 2 a₂ ω + a₁`
is the canonical Reeb conjugate momentum (retaining `a₁` inside the minimal-coupling shift `p_reeb - a₁`). -/
def canonicalHamiltonian {K : Type*} [Field K] (a₂ a₁ a₀ p_reeb : K) : K :=
  (p_reeb - a₁) ^ 2 / (4 * a₂) - a₀

/-- Scaling `L.dirac.reeb` by a clock rate `ω : R` produces `lagrangianClock` under any
`R`-linear trace functional `τ`. -/
theorem trace_scaled_reeb_eq_lagrangianClock
    {R : Type*} [CommRing R]
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
    [Preadditive C] [Linear R C] {fh : FrobeniusHopfData C}
    (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R) (L : CategoricalLagrangian R C fh) (ω : R) :
    τ ((ω ^ 2) • reebSqTerm L + ω • reebLinearTerm L + spatialZeroTerm L) =
      lagrangianClock (τ (reebSqTerm L)) (τ (reebLinearTerm L)) (τ (spatialZeroTerm L)) ω := by
  unfold lagrangianClock
  simp only [map_add, LinearMap.map_smul, smul_eq_mul]
  ring

/-- **Conjugate Reeb Momentum Inversion (`2 ≠ 0`, `a₂ ≠ 0`):**
`p_reeb = 2 a₂ ω + a₁ ↔ ω = (p_reeb - a₁) / (2 a₂)`. -/
theorem conjugate_momentum_iff {K : Type*} [Field K]
    (a₂ a₁ p_reeb ω : K) (h2 : (2 : K) ≠ 0) (ha₂ : a₂ ≠ 0) :
    p_reeb = 2 * a₂ * ω + a₁ ↔ ω = (p_reeb - a₁) / (2 * a₂) := by
  have h2a : 2 * a₂ ≠ 0 := mul_ne_zero h2 ha₂
  constructor
  · intro hp
    rw [eq_div_iff h2a]
    linear_combination -hp
  · intro hω
    have hmul : ω * (2 * a₂) = p_reeb - a₁ := (eq_div_iff h2a).mp hω
    linear_combination -hmul

/-- **Exact Phase-Space Legendre Identity (`2 ≠ 0`, `a₂ ≠ 0`):**
At `p_reeb = 2 a₂ ω + a₁`, `p_reeb * ω - lagrangianClock a₂ a₁ a₀ ω = canonicalHamiltonian a₂ a₁ a₀ p_reeb`. -/
theorem phase_space_legendre_identity {K : Type*} [Field K]
    (a₂ a₁ a₀ p_reeb ω : K) (h2 : (2 : K) ≠ 0) (ha₂ : a₂ ≠ 0)
    (hp : p_reeb = 2 * a₂ * ω + a₁) :
    p_reeb * ω - lagrangianClock a₂ a₁ a₀ ω = canonicalHamiltonian a₂ a₁ a₀ p_reeb := by
  have h4 : (4 : K) ≠ 0 := by
    have h4eq : (4 : K) = 2 * 2 := by ring
    rw [h4eq]
    exact mul_ne_zero h2 h2
  have h4a : 4 * a₂ ≠ 0 := mul_ne_zero h4 ha₂
  unfold lagrangianClock canonicalHamiltonian
  subst hp
  field_simp [h4, ha₂, h4a]
  ring

/-- **Exact Fenchel–Legendre Quadratic Deficit Identity (`2 ≠ 0`, `a₂ ≠ 0`):**
For every trial clock velocity `ω : K`,
`canonicalHamiltonian a₂ a₁ a₀ p_reeb - (p_reeb * ω - lagrangianClock a₂ a₁ a₀ ω) = a₂ * (ω - (p_reeb - a₁) / (2 * a₂))²`. -/
theorem fenchel_legendre_gap_eq_sq {K : Type*} [Field K]
    (a₂ a₁ a₀ p_reeb ω : K) (h2 : (2 : K) ≠ 0) (ha₂ : a₂ ≠ 0) :
    canonicalHamiltonian a₂ a₁ a₀ p_reeb - (p_reeb * ω - lagrangianClock a₂ a₁ a₀ ω) =
      a₂ * (ω - (p_reeb - a₁) / (2 * a₂)) ^ 2 := by
  have h2a : 2 * a₂ ≠ 0 := mul_ne_zero h2 ha₂
  have h4 : (4 : K) ≠ 0 := by
    have h4eq : (4 : K) = 2 * 2 := by ring
    rw [h4eq]
    exact mul_ne_zero h2 h2
  have h4a : 4 * a₂ ≠ 0 := mul_ne_zero h4 ha₂
  unfold canonicalHamiltonian lagrangianClock
  field_simp [h2, h4, ha₂, h2a, h4a]
  ring

/-- **Fenchel–Legendre Supremum Inequality (`0 < a₂`):**
Over any ordered field `K` with `0 < a₂`,
`p_reeb * ω - lagrangianClock a₂ a₁ a₀ ω ≤ canonicalHamiltonian a₂ a₁ a₀ p_reeb` for every `ω : K`. -/
theorem fenchel_legendre_le_canonicalHamiltonian
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (a₂ a₁ a₀ p_reeb ω : K) (ha₂ : 0 < a₂) :
    p_reeb * ω - lagrangianClock a₂ a₁ a₀ ω ≤ canonicalHamiltonian a₂ a₁ a₀ p_reeb := by
  have h2 : (2 : K) ≠ 0 := by linarith [one_pos (α := K)]
  have ha₂_ne : a₂ ≠ 0 := ne_of_gt ha₂
  have hgap := fenchel_legendre_gap_eq_sq a₂ a₁ a₀ p_reeb ω h2 ha₂_ne
  have hnonneg : 0 ≤ a₂ * (ω - (p_reeb - a₁) / (2 * a₂)) ^ 2 :=
    mul_nonneg (le_of_lt ha₂) (sq_nonneg _)
  linarith

/-- **Fenchel–Legendre Supremum Attainment Characterization (`0 < a₂`):**
Equality `p_reeb * ω - lagrangianClock a₂ a₁ a₀ ω = canonicalHamiltonian a₂ a₁ a₀ p_reeb` holds if and
only if `ω = (p_reeb - a₁) / (2 * a₂)`. -/
theorem fenchel_legendre_eq_iff
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (a₂ a₁ a₀ p_reeb ω : K) (ha₂ : 0 < a₂) :
    p_reeb * ω - lagrangianClock a₂ a₁ a₀ ω = canonicalHamiltonian a₂ a₁ a₀ p_reeb ↔
      ω = (p_reeb - a₁) / (2 * a₂) := by
  have h2 : (2 : K) ≠ 0 := by linarith [one_pos (α := K)]
  have ha₂_ne : a₂ ≠ 0 := ne_of_gt ha₂
  have hgap := fenchel_legendre_gap_eq_sq a₂ a₁ a₀ p_reeb ω h2 ha₂_ne
  constructor
  · intro heq
    have hzero : a₂ * (ω - (p_reeb - a₁) / (2 * a₂)) ^ 2 = 0 := by linarith
    have hsq : (ω - (p_reeb - a₁) / (2 * a₂)) ^ 2 = 0 :=
      (mul_eq_zero.mp hzero).resolve_left ha₂_ne
    exact sub_eq_zero.mp (sq_eq_zero_iff.mp hsq)
  · intro hω
    subst hω
    simp only [sub_self, ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, mul_zero] at hgap
    linarith

/-- **Master Unit-Clock Expansion (`p_reeb = 2 a₂`):**
Evaluating `canonicalHamiltonian` at the canonical unit-clock momentum `p_reeb = 2 * a₂` yields
`a₂ - a₁ + a₁² / (4 * a₂) - a₀`, exhibiting why `-a₁` (spin-orbit & Reeb-matter Coulomb coupling)
and `+a₁² / (4 a₂)` (second-order recoil) survive in canonical momentum variables even though `a₁`
cancelled in velocity variables. -/
theorem canonicalHamiltonian_unit_clock {K : Type*} [Field K]
    (a₂ a₁ a₀ : K) (h2 : (2 : K) ≠ 0) (ha₂ : a₂ ≠ 0) :
    canonicalHamiltonian a₂ a₁ a₀ (2 * a₂) = a₂ - a₁ + a₁ ^ 2 / (4 * a₂) - a₀ := by
  have h4 : (4 : K) ≠ 0 := by
    have h4eq : (4 : K) = 2 * 2 := by ring
    rw [h4eq]
    exact mul_ne_zero h2 h2
  have h4a : 4 * a₂ ≠ 0 := mul_ne_zero h4 ha₂
  unfold canonicalHamiltonian
  field_simp [h4, ha₂, h4a]
  ring

/-- **Specialization (i) — Pure Rest-Frame Recovery (`a₁ = 0`, `a₀ = 0`):**
`canonicalHamiltonian a₂ 0 0 (2 * a₂) = a₂`. -/
theorem canonicalHamiltonian_unit_clock_rest {K : Type*} [Field K]
    (a₂ : K) (h2 : (2 : K) ≠ 0) (ha₂ : a₂ ≠ 0) :
    canonicalHamiltonian a₂ 0 0 (2 * a₂) = a₂ := by
  rw [canonicalHamiltonian_unit_clock a₂ 0 0 h2 ha₂]
  ring

/-- **Specialization (ii) — Minimal Reeb Coupling + Darwin/Recoil (`a₀ = 0`):**
`canonicalHamiltonian a₂ a₁ 0 (2 * a₂) = a₂ - a₁ + a₁² / (4 * a₂)`. -/
theorem canonicalHamiltonian_unit_clock_minimal_coupling {K : Type*} [Field K]
    (a₂ a₁ : K) (h2 : (2 : K) ≠ 0) (ha₂ : a₂ ≠ 0) :
    canonicalHamiltonian a₂ a₁ 0 (2 * a₂) = a₂ - a₁ + a₁ ^ 2 / (4 * a₂) := by
  rw [canonicalHamiltonian_unit_clock a₂ a₁ 0 h2 ha₂]
  ring

/-- **Specialization (iii) — Shared-Spatial Nucleon Canonical Hamiltonian Difference:**
When two configurations share the horizontal/spatial background `a₀`, it cancels identically from
`canonicalHamiltonian a₂n a₁n a₀ (2 * a₂n) - canonicalHamiltonian a₂p a₁p a₀ (2 * a₂p)`, leaving the
Reeb-spin difference `a₂n - a₂p`, the minimal-coupling Reeb-matter difference `-(a₁n - a₁p)`, and
the second-order recoil difference `a₁n² / (4 a₂n) - a₁p² / (4 a₂p)`. -/
theorem canonicalHamiltonian_unit_clock_shared_spatial_diff {K : Type*} [Field K]
    (a₂n a₁n a₂p a₁p a₀ : K)
    (h2 : (2 : K) ≠ 0) (ha₂n : a₂n ≠ 0) (ha₂p : a₂p ≠ 0) :
    canonicalHamiltonian a₂n a₁n a₀ (2 * a₂n) - canonicalHamiltonian a₂p a₁p a₀ (2 * a₂p) =
      (a₂n - a₂p) - (a₁n - a₁p) + (a₁n ^ 2 / (4 * a₂n) - a₁p ^ 2 / (4 * a₂p)) := by
  rw [canonicalHamiltonian_unit_clock a₂n a₁n a₀ h2 ha₂n,
    canonicalHamiltonian_unit_clock a₂p a₁p a₀ h2 ha₂p]
  ring

end PhaseSpaceCanonicalLegendre

/-! ## 3. Causal-Cone Speed `c_q = 1 / (q - 1)` & Relativistic Worldline Legendre Derivation of `E = m c_q²` -/

section WorldlineLegendreMassEnergy

/-- Spatial weight `α_space(q) = q⁻¹` in `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇`. -/
def diracSpaceWeight {K : Type*} [Field K] (q : K) : K := q⁻¹

/-- Temporal (Reeb) weight `α_time(q) = 1 - q⁻¹ = ħ_q` in `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇`. -/
def diracTimeWeight {K : Type*} [Field K] (q : K) : K := 1 - q⁻¹

/-- Causal-cone / Lieb–Robinson lightcone speed `c_q = 1 / (q - 1)`. -/
def lightconeSpeed {K : Type*} [Field K] (q : K) : K := 1 / (q - 1)

/-- **Dirac Causal-Cone Speed Theorem (`α_space / α_time = c_q`):**
Over any field `K` (`q ≠ 0`, `q ≠ 1`), the ratio of spatial to Reeb weights in `CategoricalDiracOperator`
equals `1 / (q - 1) = lightconeSpeed q`. -/
theorem dirac_lightcone_speed_eq_cq {K : Type*} [Field K] {q : K}
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    diracSpaceWeight q / diracTimeWeight q = lightconeSpeed q := by
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have htime : 1 - q⁻¹ ≠ 0 := by
    intro h
    have hqinv : q⁻¹ = 1 := by linear_combination -h
    exact hq1 (inv_eq_one.mp hqinv)
  unfold diracSpaceWeight diracTimeWeight lightconeSpeed
  field_simp [hq0, hsub, htime]

/-- Direct instantiation on a `CategoricalDiracOperator K C fh` (`D.q ≠ 0`, `D.q ≠ 1`):
`D.qinv / (1 - D.qinv) = lightconeSpeed D.q` follows from `D.q_unit` alone. -/
theorem categoricalDirac_weight_ratio_eq_cq
    {K : Type*} [Field K]
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
    [Preadditive C] [Linear K C] {fh : FrobeniusHopfData C}
    (D : CategoricalDiracOperator K C fh)
    (hq0 : D.q ≠ 0) (hq1 : D.q ≠ 1) :
    D.qinv / (1 - D.qinv) = lightconeSpeed D.q := by
  have hqinv : D.qinv = D.q⁻¹ := eq_inv_of_mul_eq_one_right D.q_unit
  rw [hqinv]
  exact dirac_lightcone_speed_eq_cq hq0 hq1

/-- Strict positivity `0 < lightconeSpeed q` for `1 < q` over `ℝ`. -/
theorem lightconeSpeed_pos {q : ℝ} (hq : 1 < q) : 0 < lightconeSpeed q := by
  unfold lightconeSpeed
  exact one_div_pos.mpr (sub_pos.mpr hq)

/-- Strict positivity `0 < lightconeSpeed q ^ 2 - v ^ 2` inside the causal cone `|v| < c_q`. -/
theorem lightcone_cone_interior_pos {q v : ℝ} (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    0 < lightconeSpeed q ^ 2 - v ^ 2 := by
  have hcq : 0 < lightconeSpeed q := lightconeSpeed_pos hq
  have hv_sq : v ^ 2 < lightconeSpeed q ^ 2 := by
    rw [← sq_abs v, ← sq_abs (lightconeSpeed q), abs_of_pos hcq]
    exact sq_lt_sq' (by linarith [abs_nonneg v]) hv
  linarith

/-- Relativistic worldline Lagrangian `L(v) = -m_in c_q √(c_q² - v²)` on the `D_∇` causal cone
`|v| < c_q`, normalized so `L(v) - L(0) = (1/2) m_in v² + O(v⁴ / c_q²)`. -/
noncomputable def worldlineLagrangian (m_in q v : ℝ) : ℝ :=
  -m_in * lightconeSpeed q * Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2)

/-- Canonical worldline conjugate momentum `p(v) = ∂L/∂v = m_in c_q v / √(c_q² - v²)`. -/
noncomputable def worldlineMomentum (m_in q v : ℝ) : ℝ :=
  m_in * lightconeSpeed q * v / Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2)

/-- Relativistic worldline Hamiltonian / energy `E(v) := p(v) · v - L(v)` via the Legendre transform. -/
noncomputable def worldlineEnergy (m_in q v : ℝ) : ℝ :=
  worldlineMomentum m_in q v * v - worldlineLagrangian m_in q v

/-- **Exact Calculus Conjugate-Momentum Derivative (`∂L/∂v = p`):**
For `1 < q` and `|v| < lightconeSpeed q`, `worldlineLagrangian m_in q` has exact scalar
derivative `worldlineMomentum m_in q v` at `v`. -/
theorem worldlineLagrangian_hasDerivAt_momentum (m_in q v : ℝ)
    (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    HasDerivAt (worldlineLagrangian m_in q) (worldlineMomentum m_in q v) v := by
  have hcone : 0 < lightconeSpeed q ^ 2 - v ^ 2 := lightcone_cone_interior_pos hq hv
  have hid : HasDerivAt (fun x : ℝ => x) 1 v := hasDerivAt_id v
  have hsq : HasDerivAt (fun x : ℝ => x ^ 2) (2 * v) v := by
    simpa only [sq, one_mul, mul_one, ← two_mul] using hid.fun_mul hid
  have hinner : HasDerivAt (fun x : ℝ => lightconeSpeed q ^ 2 - x ^ 2) (0 - 2 * v) v :=
    (hasDerivAt_const v (lightconeSpeed q ^ 2)).sub hsq
  have hsqrt : HasDerivAt (fun x : ℝ => Real.sqrt (lightconeSpeed q ^ 2 - x ^ 2))
      ((0 - 2 * v) / (2 * Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2))) v :=
    hinner.sqrt (ne_of_gt hcone)
  have hmul := hsqrt.const_mul (-m_in * lightconeSpeed q)
  have hval : (-m_in * lightconeSpeed q) *
      ((0 - 2 * v) / (2 * Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2))) =
      worldlineMomentum m_in q v := by
    unfold worldlineMomentum
    have hrt : Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) ≠ 0 :=
      ne_of_gt (Real.sqrt_pos.mpr hcone)
    field_simp [hrt]
    ring
  rw [hval] at hmul
  exact hmul

/-- **Exact Newtonian Kinetic Recovery Identity (`L(v) - L(0)`):**
`(L(v) - L(0)) * (√(c_q² - v²) + c_q) = m_in * c_q * v²`, confirming that as `v → 0`
(`√(c_q² - v²) + c_q → 2 c_q`), `L(v) - L(0) = (1/2) m_in v² + O(v⁴ / c_q²)`. -/
theorem worldlineLagrangian_newtonian_kinetic_identity (m_in q v : ℝ)
    (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    (worldlineLagrangian m_in q v - worldlineLagrangian m_in q 0) *
        (Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) + lightconeSpeed q) =
      m_in * lightconeSpeed q * v ^ 2 := by
  have hcq : 0 ≤ lightconeSpeed q := le_of_lt (lightconeSpeed_pos hq)
  have hcone : 0 ≤ lightconeSpeed q ^ 2 - v ^ 2 :=
    le_of_lt (lightcone_cone_interior_pos hq hv)
  unfold worldlineLagrangian
  have h0 : Real.sqrt (lightconeSpeed q ^ 2 - 0 ^ 2) = lightconeSpeed q := by
    simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, sub_zero,
      Real.sqrt_sq hcq]
  rw [h0]
  have hsq : Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) *
      Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) = lightconeSpeed q ^ 2 - v ^ 2 :=
    Real.mul_self_sqrt hcone
  linear_combination -m_in * lightconeSpeed q * hsq

/-- **Exact Worldline Legendre Transform (`E(v) = m_in c_q³ / √(c_q² - v²)`):**
Inside the causal cone (`1 < q`, `|v| < c_q`),
`worldlineEnergy m_in q v = m_in * lightconeSpeed q ^ 3 / Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2)`. -/
theorem worldlineEnergy_eq (m_in q v : ℝ) (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    worldlineEnergy m_in q v =
      m_in * lightconeSpeed q ^ 3 / Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) := by
  have hcone : 0 < lightconeSpeed q ^ 2 - v ^ 2 := lightcone_cone_interior_pos hq hv
  have hrt : Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) ≠ 0 :=
    ne_of_gt (Real.sqrt_pos.mpr hcone)
  have hsq : Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) ^ 2 = lightconeSpeed q ^ 2 - v ^ 2 :=
    Real.sq_sqrt (le_of_lt hcone)
  unfold worldlineEnergy worldlineMomentum worldlineLagrangian
  rw [eq_div_iff hrt]
  have hmul : (m_in * lightconeSpeed q * v / Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) * v -
      -m_in * lightconeSpeed q * Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2)) *
      Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) =
      m_in * lightconeSpeed q * v ^ 2 +
      m_in * lightconeSpeed q * Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) ^ 2 := by
    field_simp [hrt]
    ring
  rw [hmul, hsq]
  ring

/-- **Standard Lorentz-Factor Form (`E(v) = m_in c_q² / √(1 - v² / c_q²)`):** -/
theorem worldlineEnergy_lorentz_gamma (m_in q v : ℝ)
    (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    worldlineEnergy m_in q v =
      m_in * lightconeSpeed q ^ 2 / Real.sqrt (1 - v ^ 2 / lightconeSpeed q ^ 2) := by
  have hcq_pos : 0 < lightconeSpeed q := lightconeSpeed_pos hq
  have hcq_ne : lightconeSpeed q ≠ 0 := ne_of_gt hcq_pos
  have hcone : 0 < lightconeSpeed q ^ 2 - v ^ 2 := lightcone_cone_interior_pos hq hv
  have h1mv : 0 < 1 - v ^ 2 / lightconeSpeed q ^ 2 := by
    have hdiv : (lightconeSpeed q ^ 2 - v ^ 2) / lightconeSpeed q ^ 2 =
        1 - v ^ 2 / lightconeSpeed q ^ 2 := by
      field_simp [hcq_ne]
    rw [← hdiv]
    exact div_pos hcone (sq_pos_of_pos hcq_pos)
  have hsplit : lightconeSpeed q ^ 2 - v ^ 2 =
      lightconeSpeed q ^ 2 * (1 - v ^ 2 / lightconeSpeed q ^ 2) := by
    field_simp [hcq_ne]
  rw [worldlineEnergy_eq m_in q v hq hv, hsplit,
    Real.sqrt_mul (sq_nonneg (lightconeSpeed q)), Real.sqrt_sq (le_of_lt hcq_pos)]
  have hrt1 : Real.sqrt (1 - v ^ 2 / lightconeSpeed q ^ 2) ≠ 0 :=
    ne_of_gt (Real.sqrt_pos.mpr h1mv)
  field_simp [hcq_ne, hrt1]

/-- **Rest-Frame Mass–Energy Theorem (`v = 0`):**
At rest (`v = 0`), the Legendre energy equals `m_in * c_q² = m_in / (q - 1)²`. -/
theorem worldlineEnergy_rest (m_in q : ℝ) (hq : 1 < q) :
    worldlineEnergy m_in q 0 = m_in * lightconeSpeed q ^ 2 ∧
      worldlineEnergy m_in q 0 = m_in / (q - 1) ^ 2 := by
  have hcq_pos : 0 < lightconeSpeed q := lightconeSpeed_pos hq
  have hv0 : |(0 : ℝ)| < lightconeSpeed q := by simpa only [abs_zero] using hcq_pos
  have hrest : worldlineEnergy m_in q 0 = m_in * lightconeSpeed q ^ 2 := by
    rw [worldlineEnergy_lorentz_gamma m_in q 0 hq hv0]
    simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, zero_div, sub_zero,
      Real.sqrt_one, div_one]
  refine ⟨hrest, ?_⟩
  rw [hrest]
  unfold lightconeSpeed
  have hsub : q - 1 ≠ 0 := ne_of_gt (sub_pos.mpr hq)
  field_simp [hsub]

/-- **Exact Relativistic Mass-Shell Identity (`E² - p² c_q² = (m_in c_q²)²`):**
Holds identically for every sub-lightcone velocity `|v| < c_q` (`1 < q`). -/
theorem worldline_mass_shell_identity (m_in q v : ℝ)
    (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    (worldlineEnergy m_in q v) ^ 2 - (worldlineMomentum m_in q v) ^ 2 * lightconeSpeed q ^ 2 =
      (m_in * lightconeSpeed q ^ 2) ^ 2 := by
  have hcone : 0 < lightconeSpeed q ^ 2 - v ^ 2 := lightcone_cone_interior_pos hq hv
  have hrt : Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) ≠ 0 :=
    ne_of_gt (Real.sqrt_pos.mpr hcone)
  have hsq : Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) ^ 2 = lightconeSpeed q ^ 2 - v ^ 2 :=
    Real.sq_sqrt (le_of_lt hcone)
  rw [worldlineEnergy_eq m_in q v hq hv]
  unfold worldlineMomentum
  have hfrac :
      (m_in * lightconeSpeed q ^ 3 / Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2)) ^ 2 -
        (m_in * lightconeSpeed q * v / Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2)) ^ 2 *
          lightconeSpeed q ^ 2 =
      m_in ^ 2 * lightconeSpeed q ^ 4 * (lightconeSpeed q ^ 2 - v ^ 2) /
        Real.sqrt (lightconeSpeed q ^ 2 - v ^ 2) ^ 2 := by
    field_simp [hrt]
  rw [hfrac, hsq]
  have hcone_ne : lightconeSpeed q ^ 2 - v ^ 2 ≠ 0 := ne_of_gt hcone
  field_simp [hcone_ne]

/-- **Primary Conditional Hypothesis Class (`§3b-cond`, Rule 13a — ZERO global instances):**
Axiomatises the dynamical boost-invariance identification equating a braid class `β`'s boosted
worldline kinematic inertia `inertialMass β` (`m_in(β)`) with its static Frobenius–Hopf holonomy
mass `holonomyMass β` (`𝔪(β)` from `def:mass-identity`). -/
-- @conjecture: primary
class BraidBoostInertialEquivalence (BraidClass : Type*)
    (inertialMass holonomyMass : BraidClass → ℝ) : Prop where
  /-- Boosted worldline kinematic inertia coincides with static Frobenius–Hopf holonomy mass. -/
  inertial_eq_holonomy : ∀ β : BraidClass, inertialMass β = holonomyMass β

/-- Rest-frame worldline Legendre energy of a braid class `β` carrying kinematic inertia `inertialMass β`. -/
noncomputable def braidRestEnergy {BraidClass : Type*}
    (inertialMass : BraidClass → ℝ) (q : ℝ) (β : BraidClass) : ℝ :=
  worldlineEnergy (inertialMass β) q 0

/-- **Conditional Braid Rest-Energy Theorem (`prop:mass-energy`, `§3b-cond`):**
Combining the unconditional worldline Legendre rest theorem (`worldlineEnergy_rest`) with
`[BraidBoostInertialEquivalence]` yields `𝔈(β) = 𝔪(β) · c_q² = 𝔪(β) / (q - 1)²`. -/
theorem braidRestEnergy_eq_holonomyMass_div_sq_of_boost_equiv
    {BraidClass : Type*} {inertialMass holonomyMass : BraidClass → ℝ}
    [hBoost : BraidBoostInertialEquivalence BraidClass inertialMass holonomyMass]
    (q : ℝ) (hq : 1 < q) (β : BraidClass) :
    braidRestEnergy inertialMass q β = holonomyMass β * lightconeSpeed q ^ 2 ∧
      braidRestEnergy inertialMass q β = holonomyMass β / (q - 1) ^ 2 := by
  unfold braidRestEnergy
  rw [hBoost.inertial_eq_holonomy β]
  exact worldlineEnergy_rest (holonomyMass β) q hq

/-- **Conditional Braid Dispersion / Mass-Shell Relation (`§3b-cond`):**
Under `[BraidBoostInertialEquivalence]`, a braid class boosted to velocity `|v| < c_q` satisfies
`E(v)² - p(v)² c_q² = (𝔪(β) / (q - 1)²)²`. -/
theorem braidWorldline_mass_shell_of_boost_equiv
    {BraidClass : Type*} {inertialMass holonomyMass : BraidClass → ℝ}
    [hBoost : BraidBoostInertialEquivalence BraidClass inertialMass holonomyMass]
    (q v : ℝ) (hq : 1 < q) (hv : |v| < lightconeSpeed q) (β : BraidClass) :
    (worldlineEnergy (inertialMass β) q v) ^ 2 -
        (worldlineMomentum (inertialMass β) q v) ^ 2 * lightconeSpeed q ^ 2 =
      (holonomyMass β / (q - 1) ^ 2) ^ 2 := by
  rw [hBoost.inertial_eq_holonomy β, worldline_mass_shell_identity (holonomyMass β) q v hq hv]
  unfold lightconeSpeed
  have hsub : q - 1 ≠ 0 := ne_of_gt (sub_pos.mpr hq)
  field_simp [hsub]

end WorldlineLegendreMassEnergy

/-! ## 4. Kantorovich / Fenchel LP-Dual Shadow-Price Theorem & Three-Unit-Chart Bridge -/

section KantorovichShadowPriceAndUnitCharts

/-- Reduced cost / LP-dual shadow price `u_i = H_i / d_i - y₀` of sector `i` relative to dual
threshold `y₀` (`def:knot-operator-energy`). -/
def lpShadowPrice {K : Type*} [Field K] {ι : Type*} (H d : ι → K) (y₀ : K) (i : ι) : K :=
  H i / d i - y₀

/-- Dual feasibility `y₀ ≤ H_i / d_i` is equivalent to non-negativity of the shadow price `0 ≤ u_i`. -/
theorem lpShadowPrice_nonneg_iff {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {ι : Type*} (H d : ι → K) (y₀ : K) (i : ι) :
    0 ≤ lpShadowPrice H d y₀ i ↔ y₀ ≤ H i / d i :=
  sub_nonneg

/-- **Exact Kantorovich–Fenchel Duality-Gap Decomposition:**
For any finite sector set `s : Finset ι` with `d i ≠ 0` (`∀ i ∈ s`) and normalized density weights
`∑ i ∈ s, d i * ρ i = 1`, the primal–dual gap decomposes into the convex combination of shadow prices:
`∑ i ∈ s, ρ i * H i - y₀ = ∑ i ∈ s, (d i * ρ i) * lpShadowPrice H d y₀ i`. -/
theorem kantorovich_lp_duality_gap_decomp {K : Type*} [Field K] {ι : Type*}
    (s : Finset ι) (ρ d H : ι → K) (y₀ : K)
    (hd : ∀ i ∈ s, d i ≠ 0)
    (hnorm : ∑ i ∈ s, d i * ρ i = 1) :
    ∑ i ∈ s, ρ i * H i - y₀ = ∑ i ∈ s, (d i * ρ i) * lpShadowPrice H d y₀ i := by
  have hterm : ∀ i ∈ s, (d i * ρ i) * lpShadowPrice H d y₀ i = ρ i * H i - y₀ * (d i * ρ i) := by
    intro i hi
    unfold lpShadowPrice
    have hdi : d i ≠ 0 := hd i hi
    field_simp [hdi]
  rw [Finset.sum_congr rfl hterm, Finset.sum_sub_distrib, ← Finset.mul_sum, hnorm, mul_one]

/-- **Kantorovich / Fenchel LP Weak Duality Theorem:**
Over any ordered field `K`, if `ρ_i ≥ 0`, `d_i > 0`, `∑ d_i ρ_i = 1`, and `y₀ ≤ H_i / d_i` on `s`,
then `y₀ ≤ ∑ i ∈ s, ρ i * H i`. -/
theorem kantorovich_lp_weak_duality
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {ι : Type*}
    (s : Finset ι) (ρ d H : ι → K) (y₀ : K)
    (hρ : ∀ i ∈ s, 0 ≤ ρ i)
    (hd : ∀ i ∈ s, 0 < d i)
    (hnorm : ∑ i ∈ s, d i * ρ i = 1)
    (hdual : ∀ i ∈ s, y₀ ≤ H i / d i) :
    y₀ ≤ ∑ i ∈ s, ρ i * H i := by
  have hd_ne : ∀ i ∈ s, d i ≠ 0 := fun i hi => ne_of_gt (hd i hi)
  have hgap := kantorovich_lp_duality_gap_decomp s ρ d H y₀ hd_ne hnorm
  have hsum_nonneg : 0 ≤ ∑ i ∈ s, (d i * ρ i) * lpShadowPrice H d y₀ i := by
    apply Finset.sum_nonneg
    intro i hi
    exact mul_nonneg (mul_nonneg (le_of_lt (hd i hi)) (hρ i hi))
      ((lpShadowPrice_nonneg_iff H d y₀ i).mpr (hdual i hi))
  linarith

/-- **Complementary-Slackness Zero-Gap Theorem:**
When every active sector (`ρ_i ≠ 0`) attains zero shadow price (`H_i / d_i = y₀`) under
`∑ d_i ρ_i = 1`, primal energy equals the dual bound: `∑ i ∈ s, ρ i * H i = y₀`. -/
theorem kantorovich_lp_eq_of_complementary_slackness {K : Type*} [Field K] {ι : Type*}
    (s : Finset ι) (ρ d H : ι → K) (y₀ : K)
    (hd : ∀ i ∈ s, d i ≠ 0)
    (hnorm : ∑ i ∈ s, d i * ρ i = 1)
    (hslack : ∀ i ∈ s, ρ i ≠ 0 → H i / d i = y₀) :
    ∑ i ∈ s, ρ i * H i = y₀ := by
  have hgap := kantorovich_lp_duality_gap_decomp s ρ d H y₀ hd hnorm
  have hzero : ∑ i ∈ s, (d i * ρ i) * lpShadowPrice H d y₀ i = 0 := by
    apply Finset.sum_eq_zero
    intro i hi
    by_cases hρ0 : ρ i = 0
    · simp [hρ0]
    · unfold lpShadowPrice
      rw [hslack i hi hρ0, sub_self, mul_zero]
  rw [hzero] at hgap
  exact sub_eq_zero.mp hgap

/-- **Minimum-Sector Attainment Witness (`def:knot-operator-energy`):**
Concentrating density `ρ_min(i) := if i = i₀ then (d i₀)⁻¹ else 0` on an attaining minimum sector
`i₀ ∈ s` (`y₀ = H i₀ / d i₀`, `d i₀ ≠ 0`) satisfies `∑ d_i ρ_i = 1` and achieves `∑ ρ_i H_i = y₀`. -/
theorem kantorovich_lp_attained_on_min_sector {K : Type*} [Field K] {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (d H : ι → K) (y₀ : K) (i₀ : ι)
    (hi₀ : i₀ ∈ s) (hdi₀ : d i₀ ≠ 0) (hy₀ : y₀ = H i₀ / d i₀) :
    let ρ : ι → K := fun i => if i = i₀ then (d i₀)⁻¹ else 0
    ∑ i ∈ s, d i * ρ i = 1 ∧ ∑ i ∈ s, ρ i * H i = y₀ := by
  dsimp only
  refine ⟨?_, ?_⟩
  · have hsum : ∑ i ∈ s, d i * (if i = i₀ then (d i₀)⁻¹ else 0) =
        ∑ i ∈ s, if i = i₀ then d i * (d i₀)⁻¹ else 0 := by
      refine Finset.sum_congr rfl fun i _ => ?_
      split_ifs <;> ring
    rw [hsum, Finset.sum_ite_eq' s i₀, if_pos hi₀, mul_inv_cancel₀ hdi₀]
  · have hsum : ∑ i ∈ s, (if i = i₀ then (d i₀)⁻¹ else 0) * H i =
        ∑ i ∈ s, if i = i₀ then (d i₀)⁻¹ * H i else 0 := by
      refine Finset.sum_congr rfl fun i _ => ?_
      split_ifs <;> ring
    rw [hsum, Finset.sum_ite_eq' s i₀, if_pos hi₀, hy₀]
    field_simp [hdi₀]

/-- Full Reeb-circuit Planck tick `t_P(q) = q / (q - 1) = ħ_q⁻¹`. -/
def planckTickChart {K : Type*} [Field K] (q : K) : K := q / (q - 1)

/-- Per-step Reeb share / quantum Planck constant `ħ_q = 1 - q⁻¹`. -/
def hbarChart {K : Type*} [Field K] (q : K) : K := 1 - q⁻¹

/-- Electronic / hadronic per-tick energy scale `E₀(q) = m_e / (q * (q - 1))`. -/
def hadronicScaleChart {K : Type*} [Field K] (m_e q : K) : K := m_e / (q * (q - 1))

/-- **Three-Unit-Chart Bridge Theorem (`E₀ = (m_e c_q²) / t_P = m_e c_q² ħ_q = m_e / (q (q - 1))`):**
Proves over any field `K` (`q ≠ 0`, `q ≠ 1`) that dividing the causal-cone rest energy `m_e * c_q²`
by the Planck circuit tick `t_P = q / (q - 1)` (equivalently multiplying by `ħ_q = 1 - q⁻¹`) recovers
the hadronic energy scale `E₀ = m_e / (q * (q - 1))` (`CategoricalLagrangianTwoTermBridge.hadronicScale`). -/
theorem three_unit_chart_bridge {K : Type*} [Field K] (m_e q : K)
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    (m_e * lightconeSpeed q ^ 2) / planckTickChart q = m_e * lightconeSpeed q ^ 2 * hbarChart q ∧
      m_e * lightconeSpeed q ^ 2 * hbarChart q = hadronicScaleChart m_e q ∧
      hadronicScaleChart m_e q = QOU.CategoricalLagrangianTwoTermBridge.hadronicScale m_e q := by
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  refine ⟨?_, ?_, rfl⟩
  · unfold lightconeSpeed planckTickChart hbarChart
    field_simp [hq0, hsub]
  · unfold lightconeSpeed hbarChart hadronicScaleChart
    field_simp [hq0, hsub]

end KantorovichShadowPriceAndUnitCharts

end QOU.Core.CategoricalHamiltonianLegendre
