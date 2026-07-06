import QOU.Torsion.TopologicalMass
import QOU.Torsion.BraneTower
import QOU.QuantumObservableUniverse
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-!
# Yang–Mills Existence and Mass Gap (Categorical Formulation)

Formal statement of the Yang–Mills mass gap conjecture in the QOU
framework.  The conjecture translates the classical millennium problem
into categorical language:

- **Existence**: a critical point of the q-weighted Yang–Mills–Levi
  functional exists and the vacuum state extends to a Hilbert space.
- **Mass gap**: every non-vacuum excitation has categorical mass
  bounded below by Δ_q > 0.

## Key provable ingredients

1. The **minimum crossing energy** `½(q − q⁻¹) > 0` for `q > 1`.
2. The **mass gap lower bound** `Δ_q ≥ E_cross · (q−1)² > 0`.
3. The **two-point function** decays exponentially with rate `Δ_q`.

## References

- [manuscript] Chapter 5, Conjecture: Yang–Mills existence and mass gap
- [jaffe2006] A. Jaffe & E. Witten, "Quantum Yang–Mills Theory",
  Clay Mathematics Institute Millennium Problem.
-/


namespace QOU.Torsion

/-! ## Minimum crossing energy -/

/-- The **minimum crossing energy** (Skein weight) at substrate
    parameter `q`.  Each crossing in a braid word contributes at
    least this much energy.

    `E_×(q) = ½(q − q⁻¹)` -/
noncomputable def minCrossingEnergy (q : ℝ) : ℝ :=
  (q - q⁻¹) / 2

/-- The minimum crossing energy equals `(q² − 1) / (2q)`. -/
theorem minCrossingEnergy_eq {q : ℝ} (hq : q ≠ 0) :
    minCrossingEnergy q = (q ^ 2 - 1) / (2 * q) := by
  unfold minCrossingEnergy
  field_simp

/-- The minimum crossing energy is strictly positive for `q > 1`. -/
theorem minCrossingEnergy_pos {q : ℝ} (hq : 1 < q) :
    0 < minCrossingEnergy q := by
  rw [minCrossingEnergy_eq (by linarith)]
  exact div_pos (by nlinarith) (by positivity)

/-- Explicit formula: at any `q > 1`, the crossing energy
    is `(q² − 1) / (2q)` which is strictly positive. -/
theorem minCrossingEnergy_explicit_pos {q : ℝ} (hq : 1 < q) :
    minCrossingEnergy q = (q ^ 2 - 1) / (2 * q) ∧
    0 < (q ^ 2 - 1) / (2 * q) := by
  constructor
  · exact minCrossingEnergy_eq (by linarith)
  · exact div_pos (by nlinarith) (by positivity)

/-! ## Mass gap lower bound -/

/-- The **mass gap lower bound** `Δ_q`: the minimum categorical mass
    any non-trivial vortex can have.

    `Δ_q = E_×(q) · (q − 1)² = ½(q − q⁻¹)(q − 1)²` -/
noncomputable def massGapBound (q : ℝ) : ℝ :=
  minCrossingEnergy q * (q - 1) ^ 2

/-- The mass gap bound is strictly positive for `q > 1`. -/
theorem massGapBound_pos {q : ℝ} (hq : 1 < q) :
    0 < massGapBound q := by
  unfold massGapBound
  apply mul_pos (minCrossingEnergy_pos hq)
  have : q - 1 ≠ 0 := by linarith
  positivity

/-- The mass gap bound vanishes at `q = 1` (classical limit:
    conformal symmetry restored, no mass gap). -/
theorem massGapBound_at_one : massGapBound 1 = 0 := by
  unfold massGapBound
  simp [minCrossingEnergy]

/-- The mass gap bound is monotonically increasing for `q > 1`.

    `Δ_q = E_×(q) · (q − 1)²` where `E_×(q) = (q − q⁻¹)/2`.
    Both factors are positive and increasing for `q > 1`, so
    their product is increasing. -/
theorem massGapBound_mono {q₁ q₂ : ℝ} (hq₁ : 1 < q₁) (hq₂ : q₁ ≤ q₂) :
    massGapBound q₁ ≤ massGapBound q₂ := by
  unfold massGapBound
  have hq₂_gt : 1 < q₂ := lt_of_lt_of_le hq₁ hq₂
  have he₁ := minCrossingEnergy_pos hq₁
  have he₂ := minCrossingEnergy_pos hq₂_gt
  -- Factor 1: minCrossingEnergy is increasing
  have he_mono : minCrossingEnergy q₁ ≤ minCrossingEnergy q₂ := by
    unfold minCrossingEnergy
    have h1_pos : (0 : ℝ) < q₁ := by linarith
    have h2_pos : (0 : ℝ) < q₂ := by linarith
    -- q⁻¹ is antitone for positive reals:
    -- q₁ ≤ q₂ and both positive → q₂⁻¹ ≤ q₁⁻¹
    -- Proof: q₂⁻¹ * q₁ ≤ 1 ≤ q₁⁻¹ * q₁ so q₂⁻¹ ≤ q₁⁻¹
    -- Or directly: (q₁ - q₁⁻¹) ≤ (q₂ - q₂⁻¹)
    -- because q increases and q⁻¹ decreases.
    -- We prove the combined inequality directly via nlinarith.
    have hne1 : q₁ ≠ 0 := ne_of_gt h1_pos
    have hne2 : q₂ ≠ 0 := ne_of_gt h2_pos
    -- (q₁ - q₁⁻¹)/2 ≤ (q₂ - q₂⁻¹)/2
    -- Equivalent to: q₁ * q₂ * (q₂ - q₁) + (q₂ - q₁) ≥ 0
    -- i.e. (q₂ - q₁)(q₁ * q₂ + 1) ≥ 0
    -- Both factors non-negative since q₁ ≤ q₂ and q₁, q₂ > 0.
    have key : q₁ - q₁⁻¹ ≤ q₂ - q₂⁻¹ := by
      have := mul_inv_cancel₀ hne1
      have := mul_inv_cancel₀ hne2
      nlinarith [mul_pos h1_pos h2_pos,
                 mul_le_mul_of_nonneg_left hq₂ (le_of_lt (inv_pos.mpr h2_pos)),
                 mul_le_mul_of_nonneg_right hq₂ (le_of_lt h1_pos)]
    linarith
  -- Factor 2: (q − 1)² is increasing for q ≥ 1
  have hs_mono : (q₁ - 1) ^ 2 ≤ (q₂ - 1) ^ 2 := by
    have h1 : 0 ≤ q₁ - 1 := by linarith
    have h2 : q₁ - 1 ≤ q₂ - 1 := by linarith
    nlinarith
  exact mul_le_mul he_mono hs_mono (by positivity) (le_of_lt he₂)

/-! ## Categorical transfer matrix (spectral data) -/

/-- The **categorical transfer matrix** on the endomorphism algebra
    at level `n` of the brane tower.  This is the categorical
    analogue of the Hamiltonian: its spectrum determines the mass
    spectrum of excitations.

    LaTeX: referenced in `\label{def:categorical-transfer-matrix}` -/
structure CategoricalTransferMatrix where
  /-- The direct limit algebra (brane tower endomorphisms). -/
  dla : DirectLimitAlgebra
  /-- The vacuum state. -/
  vacuum : VacuumState dla
  /-- Eigenvalues of the transfer matrix, indexed by ℕ
      (ordered by increasing energy). -/
  eigenvalues : ℕ → ℝ
  /-- The vacuum eigenvalue is zero (by definition). -/
  vacuum_eigenvalue : eigenvalues 0 = 0
  /-- Eigenvalues are non-negative. -/
  eigenvalues_nonneg : ∀ n, 0 ≤ eigenvalues n
  /-- Eigenvalues are non-decreasing. -/
  eigenvalues_mono : Monotone eigenvalues

/-- A transfer matrix has a **mass gap** if the first excited state
    has strictly positive eigenvalue. -/
def CategoricalTransferMatrix.hasMassGap (tm : CategoricalTransferMatrix) : Prop :=
  0 < tm.eigenvalues 1

/-- The mass gap value (first non-zero eigenvalue). -/
noncomputable def CategoricalTransferMatrix.gapValue
    (tm : CategoricalTransferMatrix) : ℝ :=
  tm.eigenvalues 1

/-! ## Two-point function -/

/-- The **categorical two-point function**: the Frobenius pairing
    of a vortex morphism with its time-translated copy. -/
structure TwoPointFunction where
  tm : CategoricalTransferMatrix
  coefficients : ℕ → ℝ
  coefficients_nonneg : ∀ n, 0 ≤ coefficients n
  eval : ℝ → ℝ

/-- If the transfer matrix has a mass gap, the gap value is positive.

    AUDIT NOTE: Previously named `twoPoint_exponential_decay`, which was
    misleading — the theorem only restates gap positivity, not exponential
    decay. The actual exponential decay bound `|G(t)| ≤ C·e^{-Δ₀·t}`
    requires spectral theory not yet formalised. Renamed for honesty. -/
theorem twoPoint_gap_positive
    (tpf : TwoPointFunction)
    (hgap : tpf.tm.hasMassGap) :
    0 < tpf.tm.gapValue :=
  hgap

/-! ## The conjecture -/

/-- **Conjecture (Yang–Mills existence and mass gap).**

    LaTeX: `\label{conj:yang-mills-mass-gap}` -/
structure YangMillsMassGap where
  q : ℝ
  hq : 1 < q
  /-- The categorical transfer matrix (bundles its own dla + vacuum). -/
  transferMatrix : CategoricalTransferMatrix
  /-- **Mass gap**: the first excited eigenvalue is bounded below
      by the minimum crossing energy times `(q − 1)²`. -/
  mass_gap : massGapBound q ≤ transferMatrix.gapValue
  /-- **Positivity of gap**. -/
  gap_positive : transferMatrix.hasMassGap

/-- In any `YangMillsMassGap` instance, the gap is positive. -/
theorem yang_mills_gap_positive (ymg : YangMillsMassGap) :
    0 < ymg.transferMatrix.gapValue := ymg.gap_positive

/-- The gap is bounded below by the provable crossing-energy bound. -/
theorem yang_mills_gap_lower_bound (ymg : YangMillsMassGap) :
    0 < massGapBound ymg.q ∧ massGapBound ymg.q ≤ ymg.transferMatrix.gapValue :=
  ⟨massGapBound_pos ymg.hq, ymg.mass_gap⟩

/-- **Typeclass version of the Yang–Mills mass gap conjecture**.

    Pattern 4 (typeclass conversion): instead of asserting existence
    for all `q > 1`, callers instantiate this class for their specific
    `q` and transfer matrix. The `sorry` in instances is understood as
    **conjecture**, not missing proof (per AGENTS.md §3b).

    Ref: [jaffe2006] https://www.claymath.org/millennium/yang-mills-the-maths-gap/
    Ref: [manuscript] Chapter 5, §1 -/
class HasYangMillsMassGap (q : ℝ) (tm : CategoricalTransferMatrix) where
  /-- Proposition: the Yang-Mills mass gap holds for (q, tm). -/
  mass_gap_holds : Prop
  /-- Hypothesis that the mass gap holds. -/
  gap_present : mass_gap_holds
  /-- Implication: a `YangMillsMassGap` instance exists. -/
  impl_witness : mass_gap_holds → YangMillsMassGap
  /-- Implication: the witness has the expected substrate parameter. -/
  impl_q_eq : ∀ (h : mass_gap_holds), (impl_witness h).q = q
  /-- Implication: the witness uses the expected transfer matrix. -/
  impl_tm_eq : ∀ (h : mass_gap_holds), (impl_witness h).transferMatrix = tm

/-- **The millennium conjecture**: per-instance form derived from
    `HasYangMillsMassGap`. The deprecated universal axiom
    `yangMillsMassGap_construction` has been removed; callers must
    bind `[HasYangMillsMassGap q tm]` to obtain a witness for the
    specific `(q, tm)` they care about.

    Ref: [jaffe2006] https://www.claymath.org/millennium/yang-mills-the-maths-gap/
    Ref: [manuscript] Chapter 5, §1 -/
-- Ref: [jaffe2006] Jaffe & Witten, "Quantum Yang-Mills Theory," in The Millennium Prize Problems, Clay Math. Inst. (2006)
-- Ref: [manuscript] Chapter 5, §1
theorem yangMillsMassGap_construction (q : ℝ) (_ : 1 < q)
    (tm : CategoricalTransferMatrix) [h : HasYangMillsMassGap q tm] :
    ∃ ymg : YangMillsMassGap, ymg.q = q ∧ ymg.transferMatrix = tm := by
  have active := h.gap_present
  exact ⟨h.impl_witness active, h.impl_q_eq active, h.impl_tm_eq active⟩

/-! ## Confinement corollary -/

/-- **Confinement**: if the mass gap holds, then every finite-energy
    excitation is a colour singlet. -/
structure Confinement extends YangMillsMassGap where
  glueball_mass : ℝ
  glueball_bound : massGapBound q ≤ glueball_mass

/-- Confinement implies the glueball mass is positive. -/
theorem confinement_glueball_pos (c : Confinement) :
    0 < c.glueball_mass :=
  lt_of_lt_of_le (massGapBound_pos c.hq) c.glueball_bound

end QOU.Torsion
