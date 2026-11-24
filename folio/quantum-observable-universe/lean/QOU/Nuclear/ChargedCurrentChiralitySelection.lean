import TwistedFrobeniusHopf.SweedlerJet
import TwistedFrobeniusHopf.SweedlerJetIso
import QOU.Nuclear.FlavourWeightSplit
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Left-Coupled Crossing Chirality Selection, Signed Action Readouts, and `k ≥ 1` `Ppos` Two-Term Jets (`qou-gtv6`)

Formalizes Gate 1 (`qou-gtv6` follow-up on PR `#9203` and `#9198`) over generic commutative rings
and fields (§7c: zero `ℝ`, zero empirical literals, zero `sorry`):

1. **Left-Lepton `⊗` Right-Quark Crossing Chirality Selection (`C2_neg` vs `C1_pos`).**
   By `WeightedTraceSide.rightTrace_R` / `rightTrace_Rinv`, placing a spectator / `γγ` lepton block
   to the right of the 3-strand nucleon `V_nuc³` inserts a scalar Cartan weight (`d₀ = d₁`),
   forcing left-block placement (`strand 5 = lepton`, `strand 6 = nucleon quark`). On basis
   `(00, 01, 10, 11)` (`0 = u / ν`, `1 = d / e⁻`), `β⁻` decay raises the right-hand nucleon quark
   `d₆ → u₆` while lowering the left-hand lepton `ν₅ → e⁻₅` (`|0₅ 1₆⟩ ↦ |1₅ 0₆⟩`, operator `F ⊗ E`):
   - Under positive boundary crossing `C1_pos` (`σ₅`), `P Ř₊ - R₀₊ = h (E ⊗ F)`, whose `β⁻`
     projection `Π_{R,+} (P Ř₊ - R₀₊) Π_{L,+}` vanishes identically (`betaMinusProj_pos_eq_zero`).
   - Under negative boundary crossing `C2_neg` (`σ₅⁻¹`), `P Ř₋ - R₀₋ = -h (F ⊗ E)`, whose `β⁻`
     projection equals `-h (F ⊗ E)` (`betaMinusProj_neg_eq`), nonzero iff `h ≠ 0`, and induces a
     canonical `R`-algebra homomorphism from Sweedler's first jet `R[ℤ/2] ⋉ Ω¹_u(R[ℤ/2])` into
     `Matrix (Fin 4) (Fin 4) R` via `G ↦ G_right`, `dg ↦ -h (F ⊗ E)` (`rightQuarkJetHom`).

2. **Affine-Linear Extensivity Obstruction vs Spectator-Cancelling Ratio & `C2_neg` Closed Forms.**
   - Any affine-linear trace functional `E_aff(τ) = E₀ (τ - 1)` fails additivity on multiplicative
     product traces with exact defect `E₀ (τ₁ - 1)(τ₂ - 1)` (`affineTraceEnergy_mul_defect`), while
     trace ratios `(τ_spec τ_n)/(τ_spec τ_p) = τ_n / τ_p` cancel `τ_spec ≠ 0` identically
     (`spectator_cancels_in_trace_ratio`, feeding `skein-binding-lagrangian`'s `ln |τ|` action).
   - Proves exact `ℚ(q)` closed forms for 9-strand `bare + C2_neg` and `pair_std + C2_neg`, showing
     that signed linear `F2` is negative at `q = 1` (`-5/8` and `-7/8`), whereas the plain trace
     ratio `tr_plain_n / tr_plain_p` has negative `q = 1` slope (`-4/3` and `-8/3`), making signed
     Placement-C logarithmic `Q_β = -E₀ ln(tr_plain_n / tr_plain_p)` strictly positive (`+4/3`, `+8/3`).

3. **`k ≥ 1` `Ppos` Transient Two-Term Jet & Spin-Spin Magnetic Sign Opposition.**
   - Under derived `[2]_q⁻³ K^{⊗3}` quantum-trace weighting, covariant `Q_pair` has identically
     vanishing `k ≥ 1` connected jet (`qTraceDiff_allPairs_connected_eq_zero`), while adjacent
     `Q₁₂ + Q₂₃` has exact `O((q - 1)⁴)` connected `Ppos` jet
     `(q - 1)⁴(q + 1)⁴(q² + 2)(2q⁴ + 1) / (9 q⁴ (q² + 1)³)` (`qTraceDiff_adj_connected_eq`).
   - Contrasts the negative `SU(6)` pointlike nucleon dipole difference `(-2/3)² - 1 = -5/9` with the
     positive `SU(6)` `56`-plet constituent Breit–Fermi hyperfine difference `(-1) - (-4/3) = +1/3`,
     exact opposite of static electric `Q_pair(n - p) = -1/3` (`breitFermi_add_static_QPair_eq_zero`).

-- Ref: [leitner2026] beans qou-gtv6, qou-qzvs
-- Ref: [jimbo1986] A q-analogue of U(gl(N+1)), Hecke algebra, and the Yang-Baxter equation
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §III
-/

namespace QOU.QBeta.ChargedCurrentChiralitySelection

open Matrix
open QOU.LiftingDescent
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.QBeta.FlavourWeightSplit

/-! ## Section 1: Left-Lepton `⊗` Right-Quark Crossing Chirality & Sweedler Jet Lift -/

section ChiralitySelection

local macro "mat4_ring" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> ring))

section CommRing

variable {R : Type*} [CommRing R]

/-- Tensor-factor permutation `P` on `(00, 01, 10, 11)`. -/
def swapMat : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0; 0, 0, 1, 0; 0, 1, 0, 0; 0, 0, 0, 1]

/-- Left-strand Cartan parity `G_left = diag(1, 1, -1, -1)` (`2 T₃` on strand 5). -/
def parityLeft : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, -1, 0; 0, 0, 0, -1]

/-- Right-strand Cartan parity `G_right = diag(1, -1, 1, -1)` (`2 T₃` on strand 6). -/
def parityRight : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0; 0, -1, 0, 0; 0, 0, 1, 0; 0, 0, 0, -1]

/-- Left-strand up-state (`ν₅`) projector `diag(1, 1, 0, 0)`. -/
def projLeftUp : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 0, 0; 0, 0, 0, 0]

/-- Right-strand up-state (`u₆`) projector `diag(1, 0, 1, 0)`. -/
def projRightUp : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0; 0, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 0]

/-- Left-raising, right-lowering exchange `E ⊗ F` (`|1₅ 0₆⟩ ↦ |0₅ 1₆⟩`). -/
def weakEF : Matrix (Fin 4) (Fin 4) R :=
  !![0, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 0; 0, 0, 0, 0]

/-- Left-lowering, right-raising `β⁻` exchange `F ⊗ E` (`|0₅ 1₆⟩ = |ν₅ d₆⟩ ↦ |1₅ 0₆⟩ = |e⁻₅ u₆⟩`). -/
def weakFE : Matrix (Fin 4) (Fin 4) R :=
  !![0, 0, 0, 0; 0, 0, 0, 0; 0, 1, 0, 0; 0, 0, 0, 0]

/-- Right-quark `β⁻` Sweedler differential `X_- = -h • (F ⊗ E)`. -/
def rightBetaX (h : R) : Matrix (Fin 4) (Fin 4) R := (-h) • weakFE

theorem two_projLeftUp_eq :
    (2 : R) • (projLeftUp : Matrix (Fin 4) (Fin 4) R) = 1 + parityLeft := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [projLeftUp, parityLeft] <;> ring

theorem two_projRightUp_eq :
    (2 : R) • (projRightUp : Matrix (Fin 4) (Fin 4) R) = 1 + parityRight := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [projRightUp, parityRight] <;> ring

theorem parityRight_mul_self :
    (parityRight : Matrix (Fin 4) (Fin 4) R) * parityRight = 1 := by
  simp only [parityRight]; mat4_ring

theorem rightBetaX_mul_self (h : R) :
    rightBetaX h * rightBetaX h = 0 := by
  simp only [rightBetaX, weakFE]; mat4_ring

theorem rightBetaX_mul_parityRight (h : R) :
    rightBetaX h * parityRight = -(parityRight * rightBetaX h) := by
  simp only [rightBetaX, weakFE, parityRight]; mat4_ring

/-- Outgoing right-quark chirality identity `(1 - G_right) X_- = 0`. -/
theorem right_chiral_annihilates_rightBetaX (h : R) :
    ((1 : Matrix (Fin 4) (Fin 4) R) - parityRight) * rightBetaX h = 0 := by
  simp only [parityRight, rightBetaX, weakFE]; mat4_ring

/-- Sweedler `H₄` homomorphism into `Matrix (Fin 4) (Fin 4) R` for left-lepton `⊗` right-quark `C2_neg`. -/
noncomputable def rightQuarkChargedCurrentHom (h : R) :
    Sweedler R →ₐ[R] Matrix (Fin 4) (Fin 4) R :=
  Sweedler.lift parityRight (rightBetaX h)
    parityRight_mul_self (rightBetaX_mul_self h) (rightBetaX_mul_parityRight h)

/-- Composition with `(Sweedler.jetEquiv R).symm` on the noncommutative first jet `R[ℤ/2] ⋉ Ω¹_u`. -/
noncomputable def rightQuarkJetHom (h : R) :
    TrivSqZeroExt (Sweedler.KZ2 R) (Sweedler.OmegaU R) →ₐ[R] Matrix (Fin 4) (Fin 4) R :=
  (rightQuarkChargedCurrentHom h).comp (Sweedler.jetEquiv R).symm.toAlgHom

@[simp] theorem rightQuarkChargedCurrentHom_G (h : R) :
    rightQuarkChargedCurrentHom h (Sweedler.G R) = parityRight :=
  Sweedler.lift_G ..

@[simp] theorem rightQuarkChargedCurrentHom_X (h : R) :
    rightQuarkChargedCurrentHom h (Sweedler.X R) = rightBetaX h :=
  Sweedler.lift_X ..

theorem rightQuarkJetHom_inr_dg (h : R) :
    rightQuarkJetHom h (TrivSqZeroExt.inr (Sweedler.dg R)) = rightBetaX h := by
  have hjet : Sweedler.jetEquiv R (Sweedler.X R) = TrivSqZeroExt.inr (Sweedler.dg R) := by
    change Sweedler.jetMap R (Sweedler.X R) = _
    simp [Sweedler.jetMap, Sweedler.toJet_X]
  rw [← hjet]
  simp [rightQuarkJetHom]

theorem rightQuarkChargedCurrentHom_X_ne_zero_iff (h : R) :
    rightQuarkChargedCurrentHom h (Sweedler.X R) ≠ 0 ↔ h ≠ 0 := by
  rw [rightQuarkChargedCurrentHom_X]
  constructor
  · intro hne hh
    apply hne
    simp [rightBetaX, hh]
  · intro hh hzero
    have e21 := congrFun (congrFun hzero 2) 1
    simp [rightBetaX, weakFE] at e21
    exact hh e21

end CommRing

section FieldCrossing

variable {F : Type*} [Field F]

/-- Positive Jimbo crossing `Ř₊ = σ₅` (`C1_pos`). -/
def jimboPos (q : F) : Matrix (Fin 4) (Fin 4) F :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- Negative Jimbo crossing `Ř₋ = σ₅⁻¹` (`C2_neg`). -/
def jimboNeg (q : F) : Matrix (Fin 4) (Fin 4) F :=
  !![q⁻¹, 0, 0, 0; 0, -(q - q⁻¹), 1, 0; 0, 1, 0, 0; 0, 0, 0, q⁻¹]

/-- Neutral diagonal core of `P Ř₊`. -/
def diagPos (q : F) : Matrix (Fin 4) (Fin 4) F :=
  !![q, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, q]

/-- Neutral diagonal core of `P Ř₋`. -/
def diagNeg (q : F) : Matrix (Fin 4) (Fin 4) F :=
  !![q⁻¹, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, q⁻¹]

theorem jimboPos_mul_jimboNeg (q : F) (hq : q ≠ 0) :
    jimboPos q * jimboNeg q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [jimboPos, jimboNeg, Matrix.mul_apply, Fin.sum_univ_four] <;>
    field_simp

/-- Strand-tracked positive crossing `P σ₅ = diag(q, 1, 1, q) + (q - q⁻¹)(E ⊗ F)`. -/
theorem strandTracked_pos (q : F) :
    (swapMat : Matrix (Fin 4) (Fin 4) F) * jimboPos q = diagPos q + (q - q⁻¹) • weakEF := by
  simp only [swapMat, jimboPos, diagPos, weakEF]; mat4_ring

/-- Strand-tracked negative crossing `P σ₅⁻¹ = diag(q⁻¹, 1, 1, q⁻¹) - (q - q⁻¹)(F ⊗ E)`. -/
theorem strandTracked_neg (q : F) :
    (swapMat : Matrix (Fin 4) (Fin 4) F) * jimboNeg q = diagNeg q + rightBetaX (q - q⁻¹) := by
  simp only [swapMat, jimboNeg, diagNeg, rightBetaX, weakFE]; mat4_ring

/-- **Chirality selection (exclusion of `C1_pos`):** on `(lepton₅ ⊗ quark₆)`, the `β⁻`
right-quark raising projection of `P σ₅ - diagPos` is identically zero. -/
theorem betaMinusProj_pos_eq_zero (q : F) :
    (projRightUp : Matrix (Fin 4) (Fin 4) F) *
      (swapMat * jimboPos q - diagPos q) * projLeftUp = 0 := by
  rw [strandTracked_pos]
  simp only [projRightUp, projLeftUp, weakEF]
  mat4_ring

/-- **Chirality selection (selection of `C2_neg`):** on `(lepton₅ ⊗ quark₆)`, the `β⁻`
right-quark raising projection of `P σ₅⁻¹ - diagNeg` is `-(q - q⁻¹)(F ⊗ E)`. -/
theorem betaMinusProj_neg_eq (q : F) :
    (projRightUp : Matrix (Fin 4) (Fin 4) F) *
      (swapMat * jimboNeg q - diagNeg q) * projLeftUp = rightBetaX (q - q⁻¹) := by
  rw [strandTracked_neg]
  simp only [projRightUp, projLeftUp, rightBetaX, weakFE]
  mat4_ring

theorem betaMinusProj_neg_ne_zero_iff (q : F) :
    (projRightUp : Matrix (Fin 4) (Fin 4) F) *
      (swapMat * jimboNeg q - diagNeg q) * projLeftUp ≠ 0 ↔ q - q⁻¹ ≠ 0 := by
  rw [betaMinusProj_neg_eq]
  constructor
  · intro hne hh
    apply hne
    simp [rightBetaX, hh]
  · intro hh hzero
    have e21 := congrFun (congrFun hzero 2) 1
    simp [rightBetaX, weakFE] at e21
    apply hh
    linear_combination -e21

end FieldCrossing

end ChiralitySelection

/-! ## Section 2: Affine-Linear Non-Additivity vs Spectator Cancellation & `C2_neg` Closed Forms -/

section ActionReadoutAndNineStrandC2

/-- Affine-linear trace energy `E_aff(τ) = E₀ (τ - 1)` vanishing at the unknot `τ = 1`. -/
def affineTraceEnergy {R : Type*} [CommRing R] (E₀ τ : R) : R := E₀ * (τ - 1)

/-- **Extensivity obstruction for linear trace readouts:** on a product trace `τ₁ τ₂` of two
uncoupled sub-braids, `E_aff` fails additivity by `E₀ (τ₁ - 1)(τ₂ - 1)`. -/
theorem affineTraceEnergy_mul_defect {R : Type*} [CommRing R] (E₀ τ₁ τ₂ : R) :
    affineTraceEnergy E₀ (τ₁ * τ₂) - affineTraceEnergy E₀ τ₁ - affineTraceEnergy E₀ τ₂ =
      E₀ * (τ₁ - 1) * (τ₂ - 1) := by
  unfold affineTraceEnergy
  ring

theorem affineTraceEnergy_not_additive {F : Type*} [Field F] {E₀ τ₁ τ₂ : F}
    (hE : E₀ ≠ 0) (h1 : τ₁ ≠ 1) (h2 : τ₂ ≠ 1) :
    affineTraceEnergy E₀ (τ₁ * τ₂) ≠ affineTraceEnergy E₀ τ₁ + affineTraceEnergy E₀ τ₂ := by
  intro heq
  have hdef : affineTraceEnergy E₀ (τ₁ * τ₂) - affineTraceEnergy E₀ τ₁ - affineTraceEnergy E₀ τ₂ = 0 := by
    linear_combination heq
  rw [affineTraceEnergy_mul_defect] at hdef
  exact mul_ne_zero (mul_ne_zero hE (sub_ne_zero.mpr h1)) (sub_ne_zero.mpr h2) hdef

/-- **Spectator cancellation in trace ratios:** any nonzero uncoupled left-block trace `τ_spec`
cancels identically in `(τ_spec τ_n) / (τ_spec τ_p) = τ_n / τ_p` (feeding `-E₀ ln |τ|`). -/
theorem spectator_cancels_in_trace_ratio {F : Type*} [Field F] (τ_spec τ_n τ_p : F)
    (hspec : τ_spec ≠ 0) :
    (τ_spec * τ_n) / (τ_spec * τ_p) = τ_n / τ_p :=
  mul_div_mul_left τ_n τ_p hspec

section NineStrandC2ClosedForms

variable {F : Type*} [Field F]

/-- Left-traced Cartan operator `D_eff ⊗ 1 ⊗ 1` on proton `(2,1)` weight space (`001, 010, 100`). -/
def leftCartanP (d₀ d₁ : F) : Matrix (Fin 3) (Fin 3) F :=
  !![d₀, 0, 0; 0, d₀, 0; 0, 0, d₁]

/-- Left-traced Cartan operator `D_eff ⊗ 1 ⊗ 1` on neutron `(1,2)` weight space (`011, 101, 110`). -/
def leftCartanN (d₀ d₁ : F) : Matrix (Fin 3) (Fin 3) F :=
  !![d₀, 0, 0; 0, d₁, 0; 0, 0, d₁]

/-- Full tower energy scale divided by `m_e`: `1 / (q (q - 1) (1 - (1 - q⁻¹)²))`. -/
def e0FullOverMe (q : F) : F := 1 / (q * (q - 1) * (1 - (1 - q⁻¹) ^ 2))

/-- Conditioned `0`-weight on nucleon strand 6 for `bare_spectator + C2_neg` (`σ₅⁻¹`). -/
def bareNegD0 (q : F) : F := q / (q ^ 2 + 1)

/-- Conditioned `1`-weight on nucleon strand 6 for `bare_spectator + C2_neg` (`σ₅⁻¹`). -/
def bareNegD1 (q : F) : F := -(q ^ 4 - q ^ 2 - 1) / (q * (q ^ 2 + 1))

/-- Conditioned `0`-weight on nucleon strand 6 for `pair_std + C2_neg` (`W_pair · σ₅⁻¹`). -/
def pairStdNegD0 (q : F) : F := q ^ 3 / (q ^ 2 + 1)

/-- Conditioned `1`-weight on nucleon strand 6 for `pair_std + C2_neg` (`W_pair · σ₅⁻¹`). -/
def pairStdNegD1 (q : F) : F := -(q ^ 6 - q ^ 2 - 1) / (q * (q ^ 2 + 1))

/-- Exact signed linear `F2` rational curve for `bare_spectator + C2_neg`. -/
def f2SignedBareNeg (q : F) : F :=
  (q + 1) * (2 * q ^ 14 - 5 * q ^ 12 + 6 * q ^ 10 - 9 * q ^ 8 + 2 * q ^ 6 + q ^ 4 - 3 * q ^ 2 + 1) /
    (q ^ 4 * (2 * q - 1) * (q ^ 2 + 1) ^ 4)

/-- Exact signed linear `F2` rational curve for `pair_std + C2_neg`. -/
def f2SignedPairStdNeg (q : F) : F :=
  (q + 1) * (2 * q ^ 16 - 4 * q ^ 14 + 4 * q ^ 12 - 6 * q ^ 10 - 2 * q ^ 8 + q ^ 4 - 3 * q ^ 2 + 1) /
    (q ^ 4 * (2 * q - 1) * (q ^ 2 + 1) ^ 4)

/-- Exact plain trace ratio `tr_plain_n / tr_plain_p` for `bare_spectator + C2_neg`. -/
def plainRatioBareNeg (q : F) : F :=
  -(q ^ 16 - 4 * q ^ 14 + 6 * q ^ 12 - 7 * q ^ 10 + 7 * q ^ 8 - 2 * q ^ 4 + 3 * q ^ 2 - 1) /
    (q ^ 14 - 3 * q ^ 12 + 5 * q ^ 10 - 8 * q ^ 8 + 4 * q ^ 6 - q ^ 4 - 2 * q ^ 2 + 1)

private theorem trace_leftCartanP_V3_nf (q d₀ d₁ : F) (hq : q ≠ 0) :
    trace (leftCartanP d₀ d₁ * borromeanV3A q) =
      nfBorC1 q * (2 * d₀ + d₁) +
      nfBorCs0 q * (q * d₀ + (q - q⁻¹) * d₁) +
      nfBorCs1 q * ((q - q⁻¹) * d₀ + q * d₁) +
      (nfBorCLplus q + nfBorCLminus q) * (q * (q - q⁻¹) * d₁) := by
  rw [borromeanV3A_nf_expansion q hq]
  simp [leftCartanP, A₁, A₂, mul_add, Matrix.trace_fin_three]
  ring

private theorem trace_leftCartanN_V3_nf (q d₀ d₁ : F) (hq : q ≠ 0) :
    trace (leftCartanN d₀ d₁ * borromeanV3B q) =
      nfBorC1 q * (d₀ + 2 * d₁) +
      nfBorCs0 q * ((q - q⁻¹) * d₁ + q * d₁) +
      nfBorCs1 q * (q * d₀ + (q - q⁻¹) * d₁) +
      (nfBorCLplus q + nfBorCLminus q) * (q * (q - q⁻¹) * d₁) := by
  rw [borromeanV3B_nf_expansion q hq]
  simp [leftCartanN, B₁, B₂, mul_add, Matrix.trace_fin_three]
  ring

/-- **Exact closed form of signed linear `F2` on `bare_spectator + C2_neg`.** -/
theorem f2SignedBareNeg_eq (q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (_h2q : 2 * q - 1 ≠ 0) :
    e0FullOverMe q *
      (epsN q (leftCartanN (bareNegD0 q) (bareNegD1 q) * borromeanV3B q) -
        epsP q (leftCartanP (bareNegD0 q) (bareNegD1 q) * borromeanV3A q)) =
      f2SignedBareNeg q := by
  unfold epsN epsP
  rw [trace_leftCartanN_V3_nf q (bareNegD0 q) (bareNegD1 q) hq,
    trace_leftCartanP_V3_nf q (bareNegD0 q) (bareNegD1 q) hq]
  unfold qd2 e0FullOverMe f2SignedBareNeg bareNegD0 bareNegD1
    nfBorC1 nfBorCs0 nfBorCs1 nfBorCLplus nfBorCLminus
  have hd : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  have ht : 1 - (1 - q⁻¹) ^ 2 = (2 * q - 1) / q ^ 2 := by field_simp; ring
  rw [hd, ht]
  field_simp [hq, hq1, hq2]
  ring

/-- **Signed linear `F2` on `bare_spectator + C2_neg` has negative classical limit `-5/8`.** -/
theorem f2SignedBareNeg_one (h2 : (2 : F) ≠ 0) :
    f2SignedBareNeg (1 : F) = -5 / 8 := by
  unfold f2SignedBareNeg
  have h8 : (8 : F) ≠ 0 := by
    rw [show (8 : F) = 2 ^ 3 by norm_num]; exact pow_ne_zero 3 h2
  have h16 : (16 : F) ≠ 0 := by
    rw [show (16 : F) = 2 ^ 4 by norm_num]; exact pow_ne_zero 4 h2
  norm_num
  field_simp
  ring

/-- **Exact closed form of signed linear `F2` on `pair_std + C2_neg`.** -/
theorem f2SignedPairStdNeg_eq (q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (_h2q : 2 * q - 1 ≠ 0) :
    e0FullOverMe q *
      (epsN q (leftCartanN (pairStdNegD0 q) (pairStdNegD1 q) * borromeanV3B q) -
        epsP q (leftCartanP (pairStdNegD0 q) (pairStdNegD1 q) * borromeanV3A q)) =
      f2SignedPairStdNeg q := by
  unfold epsN epsP
  rw [trace_leftCartanN_V3_nf q (pairStdNegD0 q) (pairStdNegD1 q) hq,
    trace_leftCartanP_V3_nf q (pairStdNegD0 q) (pairStdNegD1 q) hq]
  unfold qd2 e0FullOverMe f2SignedPairStdNeg pairStdNegD0 pairStdNegD1
    nfBorC1 nfBorCs0 nfBorCs1 nfBorCLplus nfBorCLminus
  have hd : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  have ht : 1 - (1 - q⁻¹) ^ 2 = (2 * q - 1) / q ^ 2 := by field_simp; ring
  rw [hd, ht]
  field_simp [hq, hq1, hq2]
  ring

/-- **Signed linear `F2` on `pair_std + C2_neg` has negative classical limit `-7/8`.** -/
theorem f2SignedPairStdNeg_one (h2 : (2 : F) ≠ 0) :
    f2SignedPairStdNeg (1 : F) = -7 / 8 := by
  unfold f2SignedPairStdNeg
  have h8 : (8 : F) ≠ 0 := by
    rw [show (8 : F) = 2 ^ 3 by norm_num]; exact pow_ne_zero 3 h2
  have h16 : (16 : F) ≠ 0 := by
    rw [show (16 : F) = 2 ^ 4 by norm_num]; exact pow_ne_zero 4 h2
  norm_num
  field_simp
  ring

/-- **Plain trace ratio on `bare_spectator + C2_neg`:** equals `1` at `q = 1` with first-order
factorization `plainRatioBareNeg q - 1 = -q²(q - 1)(q + 1) * (...)` whose `q = 1` slope is `-4/3`
(giving positive signed Placement-C logarithmic limit `+4/3`). -/
theorem plainRatioBareNeg_one (h3 : (3 : F) ≠ 0) : plainRatioBareNeg (1 : F) = 1 := by
  unfold plainRatioBareNeg
  norm_num
  field_simp [h3]

theorem plainRatioBareNeg_sub_one_factor (q : F)
    (hden : q ^ 14 - 3 * q ^ 12 + 5 * q ^ 10 - 8 * q ^ 8 + 4 * q ^ 6 - q ^ 4 - 2 * q ^ 2 + 1 ≠ 0) :
    plainRatioBareNeg q - 1 =
      -q ^ 2 * (q - 1) * (q + 1) *
        (q ^ 12 - 2 * q ^ 10 + q ^ 8 - q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 - 1) /
        (q ^ 14 - 3 * q ^ 12 + 5 * q ^ 10 - 8 * q ^ 8 + 4 * q ^ 6 - q ^ 4 - 2 * q ^ 2 + 1) := by
  unfold plainRatioBareNeg
  generalize hD :
      q ^ 14 - 3 * q ^ 12 + 5 * q ^ 10 - 8 * q ^ 8 + 4 * q ^ 6 - q ^ 4 - 2 * q ^ 2 + 1 = D at hden ⊢
  field_simp [hden]
  subst hD
  ring

end NineStrandC2ClosedForms

end ActionReadoutAndNineStrandC2

/-! ## Section 3: `k ≥ 1` `Ppos` Transient Two-Term Jet & Spin-Spin Magnetic Opposition -/

section TwoTermTransientAndMagnetic

variable {F : Type*} [Field F]

/-- Derived `[2]_q⁻³ K^{⊗3}` quantum-trace `(n - p)` insertion functional on `V³`. -/
def qTraceDiffV3 (q : F) (Xp Xn : Matrix (Fin 3) (Fin 3) F) : F :=
  (q⁻¹ * trace (Xn * borromeanV3B q) - q * trace (Xp * borromeanV3A q)) / qd2 q ^ 3

/-- **Covariant all-pairs `Q_pair` has identically zero `k ≥ 1` `Ppos` connected jet on `V³`.** -/
theorem qTraceDiff_allPairs_connected_eq_zero (q : F) :
    qTraceDiffV3 q QPairP (QPairN - (-1 / 3 : F) • (1 : Matrix (Fin 3) (Fin 3) F)) = 0 := by
  have hzeroN : (QPairN : Matrix (Fin 3) (Fin 3) F) - (-1 / 3 : F) • 1 = 0 := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [QPairN]
  have hzeroP : (QPairP : Matrix (Fin 3) (Fin 3) F) = 0 := rfl
  unfold qTraceDiffV3
  rw [hzeroN, hzeroP]
  simp

/-- **Adjacent `Q₁₂ + Q₂₃` connected `k = 4` `Ppos` transient jet closed form:**
under derived `[2]_q⁻³ K^{⊗3}` quantum-trace weighting, subtracting the `k = 0` static scalar
`(-2/9) I₃` on `W_n` yields `(q - 1)⁴(q + 1)⁴(q² + 2)(2q⁴ + 1) / (9 q⁴ (q² + 1)³)`. -/
theorem qTraceDiff_adj_connected_eq (q : F) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h3 : (3 : F) ≠ 0) :
    qTraceDiffV3 q (Q12p + Q23p)
        ((Q12n + Q23n) - (-2 / 9 : F) • (1 : Matrix (Fin 3) (Fin 3) F)) =
      (q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 2 + 2) * (2 * q ^ 4 + 1) /
        (9 * q ^ 4 * (q ^ 2 + 1) ^ 3) := by
  have h9 : (9 : F) = 3 * 3 := by ring
  have hconnN :
      trace (((Q12n + Q23n) - (-2 / 9 : F) • (1 : Matrix (Fin 3) (Fin 3) F)) * borromeanV3B q) =
        trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : F) * trace (borromeanV3B q) := by
    rw [Matrix.sub_mul, Matrix.smul_mul, Matrix.one_mul, Matrix.trace_sub, Matrix.trace_smul,
      smul_eq_mul]
    ring
  unfold qTraceDiffV3
  rw [hconnN, trace_QAdjn_borromeanV3_connected q hq h3, trace_QAdjp_borromeanV3 q hq h3]
  unfold qd2
  have hd : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [hd, h9]
  field_simp [hq, hq2, h3]
  ring

/-- Pointlike `SU(6)` magnetic dipole squared difference `(μ_n / μ_p)² - 1 = (-2/3)² - 1 = -5/9`. -/
def su6DipoleSqDiffRatio : F := (-2 / 3 : F) ^ 2 - 1

theorem su6DipoleSqDiffRatio_eq (h3 : (3 : F) ≠ 0) :
    (su6DipoleSqDiffRatio : F) = -5 / 9 := by
  have h9 : (9 : F) = 3 * 3 := by ring
  unfold su6DipoleSqDiffRatio
  rw [h9]; field_simp [h3]; ring

/-- Constituent `SU(6)` `56`-plet Breit–Fermi spin-spin matrix element `-∑_{i<j} q_i q_j (σ_i · σ_j)`
on the proton (`uud`: like-pair `S=1` gives `+1`, two `ud` pairs give `-4` total). -/
def su6BreitFermiProton : F := -((2 / 3 : F) ^ 2 * 1 + (2 / 3 : F) * (-1 / 3 : F) * (-4))

/-- Constituent `SU(6)` `56`-plet Breit–Fermi spin-spin matrix element on the neutron (`udd`). -/
def su6BreitFermiNeutron : F := -((-1 / 3 : F) ^ 2 * 1 + (2 / 3 : F) * (-1 / 3 : F) * (-4))

theorem su6BreitFermiProton_eq (h3 : (3 : F) ≠ 0) :
    (su6BreitFermiProton : F) = -4 / 3 := by
  unfold su6BreitFermiProton; field_simp [h3]; ring

theorem su6BreitFermiNeutron_eq (h3 : (3 : F) ≠ 0) :
    (su6BreitFermiNeutron : F) = -1 := by
  unfold su6BreitFermiNeutron; field_simp [h3]; ring

/-- **Positive `(n - p)` sign of constituent magnetic hyperfine (`+1/3`) and exact `k = 0`
cancellation against static electric `Q_pair(n - p) = -1/3`.** -/
theorem su6BreitFermi_np_diff_eq (h3 : (3 : F) ≠ 0) :
    (su6BreitFermiNeutron : F) - su6BreitFermiProton = 1 / 3 := by
  rw [su6BreitFermiNeutron_eq h3, su6BreitFermiProton_eq h3]
  field_simp [h3]; ring

theorem breitFermi_add_static_QPair_eq_zero (h3 : (3 : F) ≠ 0) :
    ((su6BreitFermiNeutron : F) - su6BreitFermiProton) + (-1 / 3 : F) = 0 := by
  rw [su6BreitFermi_np_diff_eq h3]
  ring

end TwoTermTransientAndMagnetic

end QOU.QBeta.ChargedCurrentChiralitySelection
