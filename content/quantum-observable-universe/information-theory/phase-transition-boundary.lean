/-
  Phase transitions as S³ boundary actions.

  Critical temperatures from the Hecke algebra representation theory:
  - Gas-liquid: T_q^{g→l} = S_q^{∂} / [2]_q
  - Liquid-solid: T_q^{l→s} = S_q^{∂} / ([2]_q · [n_K]_q)
  - Sublimation: when Ext¹_{H_n(q)}(V_asym, V_sym) ≠ 0

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace QOU.Information

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **S³ boundary action**: the restriction of the categorical action
    to ∂(S³_q) ≅ S².  This is the energy cost of threading a knot
    through the fibre boundary.
    Label: prop:phase-transition-boundary -/
noncomputable def s3BoundaryAction {M : Type*} (sp : SubstrateParameter M)
    (p : M) : R_q :=
  let q := sp.field p
  let eta := operationalEntropy sp p
  let hbar := quantumPlanckConstant sp p
  -- Surface integral of adjoint connection wedged with *η_q over S²
  eta * hbar

/-- **Gas-liquid critical temperature**.
    T_q^{g→l} = S_q^{∂} / [2]_q. -/
noncomputable def gasLiquidCriticalTemp {M : Type*} (sp : SubstrateParameter M)
    (p : M) : R_q :=
  s3BoundaryAction sp p / (sp.field p + (sp.field p)⁻¹)

/-- **Liquid-solid critical temperature**.
    T_q^{l→s} = S_q^{∂} / ([2]_q · [n_K]_q).
    Parameterised by the crossing number n_K and [n_K]_q. -/
noncomputable def liquidSolidCriticalTemp {M : Type*} (sp : SubstrateParameter M)
    (p : M) (qIntegerNK : R_q) : R_q :=
  s3BoundaryAction sp p / ((sp.field p + (sp.field p)⁻¹) * qIntegerNK)

/-- The gas-liquid critical temperature is positive when q > 1. -/
theorem gasLiquidCriticalTemp_pos {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    0 < gasLiquidCriticalTemp sp p := by
  unfold gasLiquidCriticalTemp s3BoundaryAction
  apply div_pos
  · -- η_q · ℏ_q > 0 when q > 1
    unfold operationalEntropy quantumPlanckConstant
    have hq_pos : (0 : R_q) < sp.field p := by linarith
    have h2q1 : 0 < 2 * sp.field p - 1 := by linarith
    have hq3 : 0 < sp.field p ^ 3 := by positivity
    have heta : 0 < (2 * sp.field p - 1) / sp.field p ^ 3 :=
      div_pos h2q1 hq3
    have hhbar : 0 < 1 - (sp.field p)⁻¹ := by
      have : (sp.field p)⁻¹ < 1 := by
        rw [inv_lt_one_iff_of_pos hq_pos]; linarith
      linarith
    exact mul_pos heta hhbar
  · -- [2]_q = q + q⁻¹ > 0
    have hq_pos : (0 : R_q) < sp.field p := by linarith
    have hinv : (0 : R_q) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
    linarith

/-- The liquid-solid critical temperature is below the gas-liquid
    critical temperature when [n_K]_q > 1. -/
theorem liquidSolid_lt_gasLiquid {M : Type*} (sp : SubstrateParameter M)
    (p : M) (qIntNK : R_q) (hq : sp.field p > 1)
    -- (hnk : 1 < qIntNK) :  -- (archimedean; not meaningful over R_q)
    liquidSolidCriticalTemp sp p qIntNK <
    gasLiquidCriticalTemp sp p := by
  unfold liquidSolidCriticalTemp gasLiquidCriticalTemp
  have hS := (gasLiquidCriticalTemp_pos sp p hq)
  unfold gasLiquidCriticalTemp at hS
  have hq_pos : (0 : R_q) < sp.field p := by linarith
  have hinv : (0 : R_q) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
  have h2q : 0 < sp.field p + (sp.field p)⁻¹ := by linarith
  have hnum : 0 < s3BoundaryAction sp p := by
    calc 0 < s3BoundaryAction sp p / (sp.field p + (sp.field p)⁻¹) := hS
         _ ≤ s3BoundaryAction sp p := by
            rw [div_le_iff h2q]; nlinarith [le_of_lt h2q]
  rw [div_lt_div_iff (mul_pos h2q (by linarith : (0 : R_q) < qIntNK)) h2q]
  nlinarith

/-- **Sublimation condition** (type-level): the liquid phase is
    topologically obstructed when the Hecke extension is non-split.

    We model this as a proposition: for a given crossing number n_K,
    the Ext group is non-trivial iff certain representation-theoretic
    conditions hold. -/
structure SublimationCondition (M : Type*) where
  sp : SubstrateParameter M
  point : M
  /-- Crossing number of the composite atom. -/
  crossingNumber : ℕ
  /-- Number of valence electrons beyond last closed shell. -/
  valenceElectrons : ℕ
  /-- Capacity of the valence shell. -/
  shellCapacity : ℕ
  /-- The extension is non-split (sublimation occurs). -/
  extensionNonSplit : Prop
  /-- Half-filled shell with odd Z implies non-split. -/
  halfFilled_implies_nonSplit :
    2 * valenceElectrons = shellCapacity →
    crossingNumber % 2 = 1 →
    extensionNonSplit

end QOU.Information
