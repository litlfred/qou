/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.LiftingDescent.SweedlerJet
import QOU.LiftingDescent.SweedlerJetIso
import QOU.QBeta.FlavourWeightSplit
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Sweedler `toJet` Charged-Current Bridge and 9-Strand Left-Coupled `Q_β` Dressing (`qou-gtv6`)

Formalizes the algebraic core of `NF-P1` (bean `qou-gtv6`, epic `qou-qzvs`) over generic
commutative rings and fields (§7c, zero `ℝ`, zero empirical literals, zero `sorry`):

1. **Sweedler `toJet` Embedding into Two-Strand Matrix Algebras (`Matrix (Fin 4) (Fin 4) R`).**
   - *Faithful 4D single-strand weak jet (`faithfulSweedlerHom`, `faithfulJetHom`):*
     With total Cartan parity `G_tot = diag(1, -1, -1, 1)` (`G_tot² = 1`) and single-strand
     isospin raising `X_single = h • (E ⊗ 1)` (`X_single² = 0`, `X_single G_tot = -G_tot X_single`),
     `Sweedler.lift` composed with `(Sweedler.jetEquiv R).symm` embeds the noncommutative first jet
     `R[ℤ/2] ⋉ Ω¹_u(R[ℤ/2])` into `Matrix (Fin 4) (Fin 4) R`, and is **injective** whenever `2 ≠ 0`
     and `h ≠ 0` (`faithfulSweedlerHom_injective`, `faithfulJetHom_injective`).
   - *Chiral 3D strand-tracked crossing quotient (`chargedCurrentHom`, `chargedCurrentJetHom`):*
     With left-strand Cartan parity `G_left = diag(1, 1, -1, -1)` and strand-tracked weak exchange
     `X_+ = h • (E ⊗ F)` (`du ↦ ud`), `Sweedler.lift` yields a `k`-algebra homomorphism from
     `R[ℤ/2] ⋉ Ω¹_u(R[ℤ/2])` with `X_+² = 0` (chiral selectivity), `(1 - G_left) X_+ = 0` (exact
     left-handed projection), and `X_+ ≠ 0 ↔ h ≠ 0` (`chargedCurrentHom_X_ne_zero_iff`).

2. **9-Strand Left-Coupled `γγ` Pair + Nucleon Cartan Dressing (`rCondPairPos_one = 7/8`).**
   - Closing a right-hand block leaves a scalar `c` on the nucleon weight spaces, scaling
     `epsFlavourV3` by `c` (`epsFlavourDressed_scalar`, leaving conditioned `Q_β/m_e` unchanged).
   - Closing the 6-strand `γγ` pair word `W_pair = V₀V₁V₂V₀V₃` (`≡ σ₀²σ₁⁻¹σ₄⁻¹`) placed **to the
     left** of `V_nuc³ = (σ₆σ₇⁻¹)³` across a positive crossing `σ₅` injects the conditioned Cartan
     weights `d₀(q) = (2q⁴ - 1)/(q(q² + 1))`, `d₁(q) = -q(q⁴ - q² - 1)/(q² + 1)` onto the nucleon's
     first strand, breaking `NucleonWeightSpaceTraces.trace_word_eq` and yielding exact rational
     closed form `rCondPairPos q` (`rCondPairPos_eq`) with classical `q = 1` value **`7/8`**
     (`rCondPairPos_one`), strictly exceeding the isolated 3-strand `3/4` bound of
     `QOU.QBeta.QBetaErrorBudget` (`rCondPairPos_one_ne_three_quarters`).

-- Ref: [leitner2026] beans qou-gtv6, qou-qzvs
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §III (Sweedler 4-dimensional Hopf algebra)
-/

namespace QOU.QBeta.SweedlerChargedCurrentBridge

open Matrix
open QOU.LiftingDescent
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.QBeta.FlavourWeightSplit

/-! ## Section 1: Sweedler `H₄ ≃ R[ℤ/2] ⋉ Ω¹_u` Homomorphisms into Two-Strand Matrices -/

section SweedlerMatrix

local macro "mat4_ring" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> ring))

section CommRing

variable {R : Type*} [CommRing R]

/-- Total two-strand Cartan parity `G_tot = diag(1, -1, -1, 1)` on basis `uu, ud, du, dd`. -/
def parityTot : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0; 0, -1, 0, 0; 0, 0, -1, 0; 0, 0, 0, 1]

/-- Single-strand weak raising operator `E ⊗ 1` (`du ↦ uu`, `dd ↦ ud`). -/
def singleRaise : Matrix (Fin 4) (Fin 4) R :=
  !![0, 0, 1, 0; 0, 0, 0, 1; 0, 0, 0, 0; 0, 0, 0, 0]

/-- Scaled single-strand weak raising jet `h • (E ⊗ 1)`. -/
def singleJetX (h : R) : Matrix (Fin 4) (Fin 4) R := h • singleRaise

/-- Left-strand Cartan parity `G_left = diag(1, 1, -1, -1)` (`2 T₃^{(1)}` on `uu, ud, du, dd`). -/
def parityLeft : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, -1, 0; 0, 0, 0, -1]

/-- Strand-tracked neutral-total-charge raising exchange `E ⊗ F` (`du ↦ ud`). -/
def weakEF : Matrix (Fin 4) (Fin 4) R :=
  !![0, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 0; 0, 0, 0, 0]

/-- Strand-tracked single-crossing weak transition `X_+ = h • (E ⊗ F)`. -/
def weakXPlus (h : R) : Matrix (Fin 4) (Fin 4) R := h • weakEF

theorem parityTot_mul_self : (parityTot : Matrix (Fin 4) (Fin 4) R) * parityTot = 1 := by
  simp only [parityTot]; mat4_ring

theorem singleJetX_mul_self (h : R) : singleJetX h * singleJetX h = 0 := by
  simp only [singleJetX, singleRaise]; mat4_ring

theorem singleJetX_mul_parityTot (h : R) :
    singleJetX h * parityTot = -(parityTot * singleJetX h) := by
  simp only [singleJetX, singleRaise, parityTot]; mat4_ring

/-- Canonical `R`-algebra homomorphism `Sweedler R →ₐ[R] Matrix (Fin 4) (Fin 4) R` sending
`G ↦ G_tot` and `X ↦ h • (E ⊗ 1)`. -/
noncomputable def faithfulSweedlerHom (h : R) : Sweedler R →ₐ[R] Matrix (Fin 4) (Fin 4) R :=
  Sweedler.lift parityTot (singleJetX h)
    parityTot_mul_self (singleJetX_mul_self h) (singleJetX_mul_parityTot h)

/-- Composition with `(Sweedler.jetEquiv R).symm`: `R[ℤ/2] ⋉ Ω¹_u →ₐ[R] Matrix (Fin 4) (Fin 4) R`. -/
noncomputable def faithfulJetHom (h : R) :
    TrivSqZeroExt (Sweedler.KZ2 R) (Sweedler.OmegaU R) →ₐ[R] Matrix (Fin 4) (Fin 4) R :=
  (faithfulSweedlerHom h).comp (Sweedler.jetEquiv R).symm.toAlgHom

@[simp] theorem faithfulSweedlerHom_G (h : R) :
    faithfulSweedlerHom h (Sweedler.G R) = parityTot :=
  Sweedler.lift_G ..

@[simp] theorem faithfulSweedlerHom_X (h : R) :
    faithfulSweedlerHom h (Sweedler.X R) = singleJetX h :=
  Sweedler.lift_X ..

theorem parityLeft_mul_self : (parityLeft : Matrix (Fin 4) (Fin 4) R) * parityLeft = 1 := by
  simp only [parityLeft]; mat4_ring

/-- **Chiral selectivity (`X_+² = 0`):** double charged-current raising on the same crossing
vanishes identically over any commutative ring. -/
theorem weakXPlus_mul_self (h : R) : weakXPlus h * weakXPlus h = 0 := by
  simp only [weakXPlus, weakEF]; mat4_ring

/-- **Cartan anticommutation (`X_+ G_left = -G_left X_+`).** -/
theorem weakXPlus_mul_parityLeft (h : R) :
    weakXPlus h * parityLeft = -(parityLeft * weakXPlus h) := by
  simp only [weakXPlus, weakEF, parityLeft]; mat4_ring

/-- **Sweedler charged-current homomorphism:** `Sweedler R →ₐ[R] Matrix (Fin 4) (Fin 4) R`
sending `G ↦ G_left` and `X ↦ h • (E ⊗ F)`. -/
noncomputable def chargedCurrentHom (h : R) : Sweedler R →ₐ[R] Matrix (Fin 4) (Fin 4) R :=
  Sweedler.lift parityLeft (weakXPlus h)
    parityLeft_mul_self (weakXPlus_mul_self h) (weakXPlus_mul_parityLeft h)

/-- **Noncommutative first-jet charged-current homomorphism:**
`R[ℤ/2] ⋉ Ω¹_u(R[ℤ/2]) →ₐ[R] Matrix (Fin 4) (Fin 4) R`. -/
noncomputable def chargedCurrentJetHom (h : R) :
    TrivSqZeroExt (Sweedler.KZ2 R) (Sweedler.OmegaU R) →ₐ[R] Matrix (Fin 4) (Fin 4) R :=
  (chargedCurrentHom h).comp (Sweedler.jetEquiv R).symm.toAlgHom

@[simp] theorem chargedCurrentHom_G (h : R) :
    chargedCurrentHom h (Sweedler.G R) = parityLeft :=
  Sweedler.lift_G ..

@[simp] theorem chargedCurrentHom_X (h : R) :
    chargedCurrentHom h (Sweedler.X R) = weakXPlus h :=
  Sweedler.lift_X ..

/-- **Chiral left-projection identity:** `(1 - G_left) X_+ = 0` and `G_left X_+ = X_+`. -/
theorem parityLeft_mul_weakXPlus (h : R) :
    parityLeft * weakXPlus h = weakXPlus h := by
  simp only [parityLeft, weakXPlus, weakEF]; mat4_ring

/-- **Nontriviality of the weak differential:** `chargedCurrentHom h (X)` is nonzero iff `h ≠ 0`. -/
theorem chargedCurrentHom_X_ne_zero_iff (h : R) :
    chargedCurrentHom h (Sweedler.X R) ≠ 0 ↔ h ≠ 0 := by
  rw [chargedCurrentHom_X]
  constructor
  · intro hne hh
    apply hne
    simp [weakXPlus, hh]
  · intro hh hzero
    have h12 := congrFun (congrFun hzero 1) 2
    simp [weakXPlus, weakEF] at h12
    exact hh h12

/-- Universal differential `dg` inside `R[ℤ/2] ⋉ Ω¹_u` maps to `X_+ = h • (E ⊗ F)`. -/
theorem chargedCurrentJetHom_inr_dg (h : R) :
    chargedCurrentJetHom h (TrivSqZeroExt.inr (Sweedler.dg R)) = weakXPlus h := by
  have hjet : Sweedler.jetEquiv R (Sweedler.X R) = TrivSqZeroExt.inr (Sweedler.dg R) := by
    change Sweedler.jetMap R (Sweedler.X R) = _
    simp [Sweedler.jetMap, Sweedler.toJet_X]
  rw [← hjet]
  simp [chargedCurrentJetHom]

end CommRing

section FaithfulField

variable {K : Type*} [Field K]

/-- **Faithfulness of the 4D Sweedler two-strand embedding:** when `2 ≠ 0` and `h ≠ 0`,
`faithfulSweedlerHom h : Sweedler K →ₐ[K] Matrix (Fin 4) (Fin 4) K` is injective. -/
theorem faithfulSweedlerHom_injective {h : K} (h2 : (2 : K) ≠ 0) (hh : h ≠ 0) :
    Function.Injective (faithfulSweedlerHom h) := by
  rw [injective_iff_map_eq_zero]
  intro s hs
  obtain ⟨a, b, c, d, rfl⟩ := Sweedler.exists_coords K s
  simp only [map_add, map_smul, map_mul, map_one,
    faithfulSweedlerHom_G, faithfulSweedlerHom_X] at hs
  have e00 := congrFun (congrFun hs 0) 0
  have e11 := congrFun (congrFun hs 1) 1
  have e02 := congrFun (congrFun hs 0) 2
  have e13 := congrFun (congrFun hs 1) 3
  simp [parityTot, singleJetX, singleRaise] at e00 e11 e02 e13
  have ha2 : 2 * a = 0 := by linear_combination e00 + e11
  have hb2 : 2 * b = 0 := by linear_combination e00 - e11
  have ha : a = 0 := (mul_eq_zero.mp ha2).resolve_left h2
  have hb : b = 0 := (mul_eq_zero.mp hb2).resolve_left h2
  have hcd_add : h * (c + d) = 0 := by linear_combination e02
  have hcd_sub : h * (c - d) = 0 := by linear_combination e13
  have h_add : c + d = 0 := (mul_eq_zero.mp hcd_add).resolve_left hh
  have h_sub : c - d = 0 := (mul_eq_zero.mp hcd_sub).resolve_left hh
  have hc2 : 2 * c = 0 := by linear_combination h_add + h_sub
  have hd2 : 2 * d = 0 := by linear_combination h_add - h_sub
  have hc : c = 0 := (mul_eq_zero.mp hc2).resolve_left h2
  have hd : d = 0 := (mul_eq_zero.mp hd2).resolve_left h2
  simp [ha, hb, hc, hd]

/-- **Faithfulness on the noncommutative first jet `K[ℤ/2] ⋉ Ω¹_u(K[ℤ/2])`.** -/
theorem faithfulJetHom_injective {h : K} (h2 : (2 : K) ≠ 0) (hh : h ≠ 0) :
    Function.Injective (faithfulJetHom h) :=
  (faithfulSweedlerHom_injective h2 hh).comp (Sweedler.jetEquiv K).symm.injective

end FaithfulField

end SweedlerMatrix

/-! ## Section 2: 9-Strand Left-Coupled Cartan Dressing & Classical `7/8 > 3/4` Survivor -/

section NineStrandDressing

variable {F : Type*} [Field F]

/-- Left-traced Cartan operator `D_eff ⊗ 1 ⊗ 1` restricted to the proton `(2,1)` weight space
(`001, 010, 100`, where the first nucleon strand carries `0, 0, 1`). -/
def leftCartanA (d₀ d₁ : F) : Matrix (Fin 3) (Fin 3) F :=
  !![d₀, 0, 0; 0, d₀, 0; 0, 0, d₁]

/-- Left-traced Cartan operator `D_eff ⊗ 1 ⊗ 1` restricted to the neutron `(1,2)` weight space
(`011, 101, 110`, where the first nucleon strand carries `0, 1, 1`). -/
def leftCartanB (d₀ d₁ : F) : Matrix (Fin 3) (Fin 3) F :=
  !![d₀, 0, 0; 0, d₁, 0; 0, 0, d₁]

/-- Left-dressed Convention-D flavour split `ε_n(D_B V_n³) - ε_p(D_A V_p³)`. -/
def epsFlavourDressed (q d₀ d₁ : F) : F :=
  epsN q (leftCartanB d₀ d₁ * borromeanV3B q) - epsP q (leftCartanA d₀ d₁ * borromeanV3A q)

/-- **Right-closure / scalar-weight invariance:** when `d₀ = d₁ = c` (such as right-strand closure
`c = q²` in `WeightedTraceSide.rightTrace_R`), the dressed flavour split is `c * epsFlavourV3 q`,
so conditioning by `c` leaves the isolated 3-strand `Q_β` curve unchanged. -/
theorem epsFlavourDressed_scalar (q c : F) :
    epsFlavourDressed q c c = c * epsFlavourV3 q := by
  have hA : leftCartanA c c = c • (1 : Matrix (Fin 3) (Fin 3) F) := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [leftCartanA]
  have hB : leftCartanB c c = c • (1 : Matrix (Fin 3) (Fin 3) F) := by
    ext i j; fin_cases i <;> fin_cases j <;> simp [leftCartanB]
  unfold epsFlavourDressed epsFlavourV3 epsN epsP
  rw [hA, hB, smul_mul_assoc, one_mul, smul_mul_assoc, one_mul, trace_smul, trace_smul]
  simp only [smul_eq_mul]
  ring

/-- Conditioned `0`-weight on nucleon strand 6 from left-tracing `W_pair · σ₅` (`pair_std + C1_pos`)
and dividing by `τ_D^{(6)}(W_pair) = (q⁴ + 1)/(q²(q² + 1)³)`. -/
def pairPosD0 (q : F) : F := (2 * q ^ 4 - 1) / (q * (q ^ 2 + 1))

/-- Conditioned `1`-weight on nucleon strand 6 from left-tracing `W_pair · σ₅` (`pair_std + C1_pos`)
and dividing by `τ_D^{(6)}(W_pair)`. -/
def pairPosD1 (q : F) : F := -q * (q ^ 4 - q ^ 2 - 1) / (q ^ 2 + 1)

/-- Full tower energy scale divided by `m_e`: `1 / (q (q - 1) (1 - (1 - q⁻¹)²))`. -/
def e0FullOverMe (q : F) : F := 1 / (q * (q - 1) * (1 - (1 - q⁻¹) ^ 2))

/-- Closed-form rational function for `R_cond(q)` of the 9-strand word `W_pair · σ₅ · V_nuc³`. -/
def rCondPairPos (q : F) : F :=
  -(q + 1) *
    (3 * q ^ 12 - 7 * q ^ 10 + 6 * q ^ 8 - 8 * q ^ 6 - 2 * q ^ 4 + 2 * q ^ 2 - 1) /
    ((2 * q - 1) * (q ^ 2 + 1) ^ 4)

/-- Explicit trace of `leftCartanA d₀ d₁ * borromeanV3A q` on the proton `(2,1)` weight space. -/
theorem trace_leftCartanA_V3 (q d₀ d₁ : F) (hq : q ≠ 0) :
    trace (leftCartanA d₀ d₁ * borromeanV3A q) =
      nfBorC1 q * (2 * d₀ + d₁) +
      nfBorCs0 q * (q * d₀ + (q - q⁻¹) * d₁) +
      nfBorCs1 q * ((q - q⁻¹) * d₀ + q * d₁) +
      (nfBorCLplus q + nfBorCLminus q) * (q * (q - q⁻¹) * d₁) := by
  rw [borromeanV3A_nf_expansion q hq]
  simp [leftCartanA, A₁, A₂, mul_add, Matrix.trace_fin_three]
  ring

/-- Explicit trace of `leftCartanB d₀ d₁ * borromeanV3B q` on the neutron `(1,2)` weight space. -/
theorem trace_leftCartanB_V3 (q d₀ d₁ : F) (hq : q ≠ 0) :
    trace (leftCartanB d₀ d₁ * borromeanV3B q) =
      nfBorC1 q * (d₀ + 2 * d₁) +
      nfBorCs0 q * ((q - q⁻¹) * d₁ + q * d₁) +
      nfBorCs1 q * (q * d₀ + (q - q⁻¹) * d₁) +
      (nfBorCLplus q + nfBorCLminus q) * (q * (q - q⁻¹) * d₁) := by
  rw [borromeanV3B_nf_expansion q hq]
  simp [leftCartanB, B₁, B₂, mul_add, Matrix.trace_fin_three]
  ring

/-- **Exact plain-trace splitting under left-Cartan dressing:** `L₊ + L₋` cancels identically
between `W_n` and `W_p`, leaving `(d₁ - d₀) * (nfBorC1 q + q * nfBorCs0 q - q⁻¹ * nfBorCs1 q)`. -/
theorem trace_leftCartan_diff_V3 (q d₀ d₁ : F) (hq : q ≠ 0) :
    trace (leftCartanB d₀ d₁ * borromeanV3B q) - trace (leftCartanA d₀ d₁ * borromeanV3A q) =
      (d₁ - d₀) * (nfBorC1 q + q * nfBorCs0 q - q⁻¹ * nfBorCs1 q) := by
  rw [trace_leftCartanB_V3 q d₀ d₁ hq, trace_leftCartanA_V3 q d₀ d₁ hq]
  field_simp
  ring

/-- **Exact closed form of `R_cond(q)` on `W_pair · σ₅ · V_nuc³` over any field.** -/
theorem rCondPairPos_eq (q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (_h2q : 2 * q - 1 ≠ 0) :
    e0FullOverMe q * (-epsFlavourDressed q (pairPosD0 q) (pairPosD1 q)) = rCondPairPos q := by
  unfold epsFlavourDressed epsN epsP
  rw [trace_leftCartanA_V3 q (pairPosD0 q) (pairPosD1 q) hq,
    trace_leftCartanB_V3 q (pairPosD0 q) (pairPosD1 q) hq]
  unfold qd2 e0FullOverMe rCondPairPos pairPosD0 pairPosD1
    nfBorC1 nfBorCs0 nfBorCs1 nfBorCLplus nfBorCLminus
  have hd : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  have ht : 1 - (1 - q⁻¹) ^ 2 = (2 * q - 1) / q ^ 2 := by field_simp; ring
  rw [hd, ht]
  field_simp
  ring

/-- **Classical `q = 1` value of `W_pair · σ₅ · V_nuc³` is `7/8`**, escaping the isolated
3-strand `3/4` ceiling of `QOU.QBeta.QBetaErrorBudget`. -/
theorem rCondPairPos_one (h2 : (2 : F) ≠ 0) :
    rCondPairPos (1 : F) = 7 / 8 := by
  unfold rCondPairPos
  have h8 : (8 : F) ≠ 0 := by
    rw [show (8 : F) = 2 ^ 3 by norm_num]; exact pow_ne_zero 3 h2
  have h16 : (16 : F) ≠ 0 := by
    rw [show (16 : F) = 2 ^ 4 by norm_num]; exact pow_ne_zero 4 h2
  norm_num
  field_simp
  ring

/-- **`7/8 ≠ 3/4` over any field of characteristic `≠ 2`.** -/
theorem rCondPairPos_one_ne_three_quarters (h2 : (2 : F) ≠ 0) :
    rCondPairPos (1 : F) ≠ 3 / 4 := by
  rw [rCondPairPos_one h2]
  intro h
  have h8 : (8 : F) ≠ 0 := by
    rw [show (8 : F) = 2 ^ 3 by norm_num]; exact pow_ne_zero 3 h2
  have h4 : (4 : F) ≠ 0 := by
    rw [show (4 : F) = 2 ^ 2 by norm_num]; exact pow_ne_zero 2 h2
  have h1 : (1 : F) = 0 := by
    have hm : (8 : F) * (7 / 8) = (8 : F) * (3 / 4) := congrArg (fun x : F => 8 * x) h
    have lhs : (8 : F) * (7 / 8) = 7 := by field_simp
    have rhs : (8 : F) * (3 / 4) = 6 := by field_simp; ring
    rw [lhs, rhs] at hm
    linear_combination hm
  exact one_ne_zero h1

end NineStrandDressing

end QOU.QBeta.SweedlerChargedCurrentBridge
