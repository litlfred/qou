import QOU.Core.CategoricalHamiltonianLegendre
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.Information.energy — Mass–Energy Equivalence via the Causal-Cone Legendre Transform

Derives `prop:mass-energy` (`𝔈 = 𝔪 · c_q² = 𝔪 / (q - 1)²`) from `def:categorical-hamiltonian`
(`QOU.Core.CategoricalHamiltonianLegendre`):
1. Unconditionally over `ℝ` (`1 < q`, `|v| < c_q`), the relativistic worldline Lagrangian
   `L(v) = -m_in c_q √(c_q² - v²)` on the `𝒟_∇` causal cone `c_q = 1 / (q - 1)` has calculus
   conjugate momentum `p(v) = ∂L/∂v` (`worldline_momentum_hasDerivAt`), Legendre energy
   `E(v) = m_in c_q² / √(1 - v² / c_q²)` (`worldline_legendre_energy`), rest value
   `E(0) = m_in c_q² = energy q m_in` (`worldline_rest_eq_energy`), and mass-shell relation
   `E(v)² - p(v)² c_q² = (energy q m_in)²` (`worldline_mass_shell`).
2. Conditional on `[BraidBoostInertialEquivalence]` equating boosted kinematic inertia `m_in(β)`
   with static Frobenius–Hopf holonomy mass `𝔪(β)` (`def:mass-identity`), `braidRestEnergy`
   evaluates to `energy q (holonomyMass β) = 𝔪(β) / (q - 1)²` (`braidRestEnergy_eq_energy_of_boost_equiv`).
3. As `q → 1`, `speedOfLightSq q = 1 / (q - 1)² → ∞` (`massEnergy_classical_limit`).

LaTeX label: `prop:mass-energy`

**Ground ring**: `ℝ` (archimedean specialisation: `Real.sqrt`, sub-lightcone ordering `|v| < c_q`,
and the `ε`-`δ` limit as `q → 1`).

## References
- [leitner2026] Ch. 2 (`def:categorical-hamiltonian`) & Ch. 20 (`prop:mass-energy`)
-/

set_option autoImplicit false

namespace QOU.Information

open QOU.Core.CategoricalHamiltonianLegendre

/-- Squared causal-cone speed `c_q² = 1 / (q - 1)²`. -/
-- Ref: [leitner2026] Ch. 20, prop:mass-energy
noncomputable def speedOfLightSq (q : ℝ) : ℝ :=
  1 / (q - 1) ^ 2

/-- Rest energy functional `𝔈(q, m) = m · c_q² = m / (q - 1)²`. -/
-- Ref: [leitner2026] Ch. 20, prop:mass-energy
noncomputable def energy (q m : ℝ) : ℝ :=
  m * speedOfLightSq q

/-- Compatibility between `speedOfLightSq q` and `(lightconeSpeed q)²`. -/
theorem speedOfLightSq_eq_lightconeSpeed_sq (q : ℝ) :
    speedOfLightSq q = lightconeSpeed q ^ 2 := by
  unfold speedOfLightSq lightconeSpeed
  rw [div_pow, one_pow]

/-- **Exact Calculus Conjugate Momentum (`∂L/∂v = p`)** on the `c_q` causal cone. -/
theorem worldline_momentum_hasDerivAt (m_in q v : ℝ)
    (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    HasDerivAt (worldlineLagrangian m_in q) (worldlineMomentum m_in q v) v :=
  worldlineLagrangian_hasDerivAt_momentum m_in q v hq hv

/-- **Worldline Legendre Energy Formula (`E(v) = m_in c_q² / √(1 - v² / c_q²)`).** -/
theorem worldline_legendre_energy (m_in q v : ℝ)
    (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    worldlineEnergy m_in q v =
      m_in * lightconeSpeed q ^ 2 / Real.sqrt (1 - v ^ 2 / lightconeSpeed q ^ 2) :=
  worldlineEnergy_lorentz_gamma m_in q v hq hv

/-- **Rest-Frame Legendre Derivation (`v = 0`):**
`worldlineEnergy m_in q 0 = energy q m_in = m_in / (q - 1)²`. -/
theorem worldline_rest_eq_energy (m_in q : ℝ) (hq : 1 < q) :
    worldlineEnergy m_in q 0 = energy q m_in ∧
      energy q m_in = m_in / (q - 1) ^ 2 := by
  obtain ⟨h1, h2⟩ := worldlineEnergy_rest m_in q hq
  have heq : energy q m_in = m_in * lightconeSpeed q ^ 2 := by
    unfold energy
    rw [speedOfLightSq_eq_lightconeSpeed_sq]
  exact ⟨h1.trans heq.symm, heq.trans (h1.symm.trans h2)⟩

/-- **Worldline Mass-Shell Identity:**
`E(v)² - p(v)² c_q² = (energy q m_in)²` for all `|v| < c_q` (`1 < q`). -/
theorem worldline_mass_shell (m_in q v : ℝ)
    (hq : 1 < q) (hv : |v| < lightconeSpeed q) :
    (worldlineEnergy m_in q v) ^ 2 - (worldlineMomentum m_in q v) ^ 2 * lightconeSpeed q ^ 2 =
      (energy q m_in) ^ 2 := by
  rw [worldline_mass_shell_identity m_in q v hq hv]
  unfold energy
  rw [speedOfLightSq_eq_lightconeSpeed_sq]

/-- **Conditional Braid Mass–Energy Equivalence (`§3b-cond` via `BraidBoostInertialEquivalence`):**
Assuming `[BraidBoostInertialEquivalence]` equating boosted kinematic inertia `inertialMass β`
with static holonomy mass `holonomyMass β` (`def:mass-identity`), the rest-frame Legendre energy
of `β` equals `energy q (holonomyMass β) = holonomyMass β / (q - 1)²`. -/
theorem braidRestEnergy_eq_energy_of_boost_equiv
    {BraidClass : Type*} {inertialMass holonomyMass : BraidClass → ℝ}
    [BraidBoostInertialEquivalence BraidClass inertialMass holonomyMass]
    (q : ℝ) (hq : 1 < q) (β : BraidClass) :
    braidRestEnergy inertialMass q β = energy q (holonomyMass β) ∧
      braidRestEnergy inertialMass q β = holonomyMass β / (q - 1) ^ 2 := by
  obtain ⟨h1, h2⟩ := braidRestEnergy_eq_holonomyMass_div_sq_of_boost_equiv
    (inertialMass := inertialMass) (holonomyMass := holonomyMass) q hq β
  refine ⟨?_, h2⟩
  rw [h1]
  unfold energy
  rw [speedOfLightSq_eq_lightconeSpeed_sq]

/-- At `q → 1`, `speedOfLightSq q = 1 / (q - 1)²` diverges to `+∞`, recovering the classical
Galilean limit `c_q → ∞`. -/
-- Ref: [leitner2026] Ch. 20, prop:mass-energy
theorem massEnergy_classical_limit :
    ∀ ε > 0, ∃ δ > 0, ∀ q : ℝ, 0 < |q - 1| → |q - 1| < δ →
    1 / ε < speedOfLightSq q := by
  intro ε hε
  refine ⟨Real.sqrt ε, Real.sqrt_pos.mpr hε, ?_⟩
  intro q hq_ne hq_lt
  unfold speedOfLightSq
  have h_sq_pos : (0 : ℝ) < (q - 1) ^ 2 := by
    rw [← sq_abs]
    exact pow_pos hq_ne 2
  have hlt : (q - 1) ^ 2 < ε :=
    calc (q - 1) ^ 2 = |q - 1| ^ 2 := by rw [sq_abs]
      _ < (Real.sqrt ε) ^ 2 := by
          apply sq_lt_sq'
          · linarith [abs_nonneg (q - 1)]
          · exact hq_lt
      _ = ε := Real.sq_sqrt (le_of_lt hε)
  exact one_div_lt_one_div_of_lt h_sq_pos hlt

end QOU.Information
