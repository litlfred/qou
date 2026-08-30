/-
  Phase transitions as S³ boundary actions.

  Critical temperatures from the Hecke algebra representation theory:
  - Gas-liquid: T_q^{g→l} = S_q^{∂} / [2]_q
  - Liquid-solid: T_q^{l→s} = S_q^{∂} / ([2]_q · [n_K]_q)
  - Sublimation: no mechanism (bean `qou-zut2`, 2026-08-24)

  The block previously read sublimation off `Ext¹_{H_n(q)}(V_asym, V_sym) ≠ 0`.
  That group is zero: `H_n(q)` is semisimple away from roots of unity, so every
  short exact sequence of its modules splits
  (`QOU.Mathlib.ExtensionClass.isSplit_of_isSemisimpleRing`), and the sym/asym
  pair splits on the Hecke quadratic alone once `[2]_q` is a unit
  (`QOU.Mathlib.ExtensionClass.heckeSES_isSplit`) — the same `[2]_q` the two
  critical temperatures above divide by.  `SublimationCondition` below keeps a
  bare `Prop` field for the condition and asserts nothing about its content.

**Ground ring**: archimedean specialisation over `ℝ` (AGENTS.md §7c).
The critical-temperature proofs use ordering, division, and positivity,
so they live over `ℝ`; the underlying combinatorial content stays generic
to any commutative ring with the same `q`-data.  `R_q := ℝ` is the
substrate specialisation `ι : ℤ[q, q⁻¹] → ℝ, q ↦ q₀`.
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.GCongr

namespace QOU.Information

noncomputable section

/-- Ground ring: archimedean specialisation `R_q := ℝ` (AGENTS.md §7c).
    The numerical substrate value `q₀ ≈ 1.1097` lives in `ℝ`. -/
abbrev R_q := ℝ

/-- **S³ boundary action**: the restriction of the categorical action
    to ∂(S³_q) ≅ S².  This is the energy cost of threading a knot
    through the fibre boundary.
    Label: prop:phase-transition-boundary -/
noncomputable def s3BoundaryAction {M : Type*} (sp : SubstrateParameter M)
    (p : M) : R_q :=
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
      have : (sp.field p)⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
      linarith
    exact mul_pos heta hhbar
  · -- [2]_q = q + q⁻¹ > 0
    have hq_pos : (0 : R_q) < sp.field p := by linarith
    have hinv : (0 : R_q) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
    linarith

/-- The liquid-solid critical temperature is below the gas-liquid
    critical temperature when [n_K]_q > 1. -/
theorem liquidSolid_lt_gasLiquid {M : Type*} (sp : SubstrateParameter M)
    (p : M) (qIntNK : R_q) (hq : sp.field p > 1) (hnk : 1 < qIntNK) :
    liquidSolidCriticalTemp sp p qIntNK <
    gasLiquidCriticalTemp sp p := by
  unfold liquidSolidCriticalTemp gasLiquidCriticalTemp
  have hS := (gasLiquidCriticalTemp_pos sp p hq)
  unfold gasLiquidCriticalTemp at hS
  have hq_pos : (0 : R_q) < sp.field p := by linarith
  have hinv : (0 : R_q) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
  have h2q : 0 < sp.field p + (sp.field p)⁻¹ := by linarith
  have hnum : 0 < s3BoundaryAction sp p := by
    have := mul_pos hS h2q
    rwa [div_mul_cancel₀ _ (ne_of_gt h2q)] at this
  -- s/([2]q · nK) < s/[2]q  since nK > 1, s > 0, [2]q > 0
  gcongr
  nlinarith

/-- **Sublimation condition** (type-level): the shell-and-parity pattern
    `rem:composite-crossing-sublimation-criteria` records, with the condition
    it implies left abstract.

    The `sublimes` field is a bare `Prop` supplied by the instantiator. It was
    once documented as "the Hecke extension is non-split"; that reading is
    withdrawn (bean `qou-zut2`, 2026-08-24) because `Ext¹_{H_n(q)}` vanishes
    identically away from roots of unity. Nothing here asserts what the
    condition *is*, so the structure survives the withdrawal unchanged in
    content — only in name and documentation. -/
structure SublimationCondition (M : Type*) where
  sp : SubstrateParameter M
  point : M
  /-- Crossing number of the composite atom. -/
  crossingNumber : ℕ
  /-- Number of valence electrons beyond last closed shell. -/
  valenceElectrons : ℕ
  /-- Capacity of the valence shell. -/
  shellCapacity : ℕ
  /-- The atom sublimes. Left abstract: this file supplies no mechanism. -/
  sublimes : Prop
  /-- Half-filled shell with odd `Z` is the recorded sublimation pattern. -/
  halfFilled_implies_sublimes :
    2 * valenceElectrons = shellCapacity →
    crossingNumber % 2 = 1 →
    sublimes

end

end QOU.Information
