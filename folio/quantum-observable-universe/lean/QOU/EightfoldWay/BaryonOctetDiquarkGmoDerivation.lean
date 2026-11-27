/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import HeckeTemperleyLieb.QIntegerCanonical
import QOU.EightfoldWay.HyperbolicMesonClaspAndDiquarkSplit
import QOU.EightfoldWay.MesonThreeByFourCharacterization

/-!
# Baryon Octet `Λ⁰–Σ⁰` Diquark Exchange, `U_q(sl₃)` Schur–Weyl Cube, and 2nd-Order GMO / Decuplet Curvature (`§7c` Generic)

This module formalizes the representation-theoretic, Temperley–Lieb diquark-exchange, and
quantum-Casimir baryon multiplet theorems for `qou-8fw2`, `qou-d7h1`, and `qou-wyy9` (Issue `#9375`),
strictly over generic `[CommRing R]` and `[Field K]` (`AGENTS.md` §7c: zero `ℝ`, zero empirical
literals, zero `sorry`, zero custom axioms):

1. **Section 1 — 3-Variable Schur Polynomial Cube & `U_q(sl₃)` Weyl Quantum-Dimension Identity (`[CommRing R]` / `[Field K]`):**
   - Proves over any `[CommRing R]` that the three 3-variable Schur characters
     `schur3_sym` (`10` monomials), `schur3_mix` (`8` weights, with multiplicity `2` on `x₁ x₂ x₃`
     corresponding to `Λ⁰ ⊕ Σ⁰`), and `schur3_alt` (`1` monomial) satisfy
     `schur3_sym x₁ x₂ x₃ + 2 * schur3_mix x₁ x₂ x₃ + schur3_alt x₁ x₂ x₃ = (x₁ + x₂ + x₃) ^ 3`,
     evaluating at `(1, 1, 1)` to `(10, 8, 1)` (`10 + 2 * 8 + 1 = 27`) (`schur3_cube_decomposition`).
   - Specializing `(x₁, x₂, x₃) = (q², 1, q⁻²)` over `[Field K]` proves the canonical `qIntBal`
     Weyl quantum-dimension formulas:
     `s_{(3)}(q², 1, q⁻²) = [4]_q [5]_q / [2]_q = [3]_q [4]_q [5]_q / ([2]_q [3]_q)`,
     `s_{(2,1)}(q², 1, q⁻²) = [2]_q [4]_q = [3]_q² - 1`, `s_{(1,1,1)}(q², 1, q⁻²) = 1`, and
     `[4]_q [5]_q / [2]_q + 2 * ([2]_q [4]_q) + 1 = [3]_q³` (`uq_sl3_weyl_qdim_cube_identity`).

2. **Section 2 — Temperley–Lieb `(u, d)` Diquark Exchange `e₁₂` & `Λ⁰–Σ⁰` Degeneracy Breaking (`[Field K]`):**
   - Defines `tlExchange12 q = q • 1 - rho21_sigma0 q` on the mixed-symmetry Hecke module `S^{(2,1)}`
     and proves `e₁₂² = [2]_q • e₁₂`, exact annihilation `e₁₂ * P_{Σ⁰} = 0` on the `I = 1` symmetric
     diquark (`Sym²_q V₂`, `dim_q = [3]_q`), exact eigenvalue `e₁₂ * P_Λ = [2]_q • P_Λ` on the
     `I = 0` antisymmetric diquark (`Λ²_q V₂`, `dim_q = 1`), exact hyperfine trace splitting
     `tr(P_{Σ⁰} H_hf) - tr(P_Λ H_hf) = κ_hf * [2]_q` on `H_hf = M_uds • 1 - κ_hf • e₁₂`, and the
     `U_q(sl₂)` diquark quantum-dimension excess `[3]_q - 1 = q² + q⁻² = [2]_q² - 2`
     (`tlExchange12_diquark_eigenvalues_and_hyperfine_split`).

3. **Section 3 — First-Order Baryon GMO Cancellation & 2nd-Order Quantum Casimir Decuplet Asymmetry (`[Field K]`):**
   - Proves `2 * (M_N + M_Ξ) - (3 * M_Λ + M_Σ) = 0`, `M_Σ - M_Λ = 2 * b`, and decuplet equal spacing
     on `M(I, Y) = M₀ + a * Y + b * (I * (I + 1) - Y² / 4)` (`firstOrder_baryon_gmo_and_decuplet_equal_spacing`).
   - Evaluates the square-root-free rational quantum Casimir `d_q(I, Y) = [I]_q [I+1]_q - [Y/2]_q²`
     across all four decuplet states `Δ(3/2, +1), Σ*(1, 0), Ξ*(1/2, -1), Ω⁻(0, -2)`, proving exact
     `q = 1` recovery `(7/2, 2, 1/2, -1)` and proving that at `q ≠ 1` it breaks the classical
     polynomial identity `spacingUpper = spacingLower` with parameter-free ratio
     `(M_{Ω⁻} - 2 M_{Ξ*} + M_{Σ*}) / (M_{Ξ*} - 2 M_{Σ*} + M_Δ) = 1 / (q + 1 + q⁻¹)`
     (`qCasimir_decuplet_second_differences_and_ratio`).
-/

set_option autoImplicit false

namespace QOU.EightfoldWay
namespace BaryonOctetDiquarkGmoDerivation

open QOU.QInteger (qIntBal qIntBal_def)
open QOU.Eightfold.HyperbolicMesonClaspAndDiquarkSplit
  (projDiquarkLambda projDiquarkSigma0 projDiquarkLambda_eq projDiquarkSigma0_eq)
open QOU.QBeta.BorromeanFlavourPivotalUnification (rho21_sigma0 rho21_sigma0_eq)
open QOU.EightfoldWay.MesonThreeByFourCharacterization (qIntBal_small_laurent)

/-! ## Section 1: 3-Variable Schur Polynomial Cube & `U_q(sl₃)` Weyl Quantum-Dimension Identity -/

section SchurWeylCube

/-- Complete homogeneous / Schur polynomial `s_{(3)}(x₁, x₂, x₃)` of the `10`-dimensional symmetric
decuplet `Sym³(W₃)`. Note `x₁ x₂ x₃` enters with multiplicity `1` (`Σ*⁰`). -/
def schur3_sym {R : Type*} [CommRing R] (x₁ x₂ x₃ : R) : R :=
  x₁ ^ 3 + x₂ ^ 3 + x₃ ^ 3 +
    x₁ ^ 2 * (x₂ + x₃) + x₂ ^ 2 * (x₁ + x₃) + x₃ ^ 2 * (x₁ + x₂) +
    x₁ * x₂ * x₃

/-- Mixed-symmetry Schur polynomial `s_{(2,1)}(x₁, x₂, x₃)` of the `8`-dimensional baryon octet.
Note the zero-weight monomial `x₁ x₂ x₃` enters with multiplicity `2` (`Λ⁰ ⊕ Σ⁰`). -/
def schur3_mix {R : Type*} [CommRing R] (x₁ x₂ x₃ : R) : R :=
  x₁ ^ 2 * (x₂ + x₃) + x₂ ^ 2 * (x₁ + x₃) + x₃ ^ 2 * (x₁ + x₂) +
    2 * x₁ * x₂ * x₃

/-- Elementary symmetric / Schur polynomial `s_{(1,1,1)}(x₁, x₂, x₃) = x₁ x₂ x₃` of the
`1`-dimensional antisymmetric flavour singlet `Λ³(W₃)`. -/
def schur3_alt {R : Type*} [CommRing R] (x₁ x₂ x₃ : R) : R :=
  x₁ * x₂ * x₃

/-- **Universal 3-Variable Schur–Weyl Cube Identity (`[CommRing R]`)**:
Over any commutative ring `R`, `s_{(3)} + 2 s_{(2,1)} + s_{(1,1,1)} = (x₁ + x₂ + x₃)³`, and at
`(1, 1, 1)` the three Schur polynomials evaluate to `(10, 8, 1)` (`10 + 2 * 8 + 1 = 27`). -/
theorem schur3_cube_decomposition {R : Type*} [CommRing R] (x₁ x₂ x₃ : R) :
    schur3_sym x₁ x₂ x₃ + 2 * schur3_mix x₁ x₂ x₃ + schur3_alt x₁ x₂ x₃ =
      (x₁ + x₂ + x₃) ^ 3 ∧
    schur3_sym (1 : R) 1 1 = 10 ∧
    schur3_mix (1 : R) 1 1 = 8 ∧
    schur3_alt (1 : R) 1 1 = 1 := by
  unfold schur3_sym schur3_mix schur3_alt
  refine ⟨by ring, by ring, by ring, by ring⟩

/-- **Canonical `U_q(sl₃)` Weyl Quantum-Dimension Cube Identity (`3_q^{⊗3} = 10_q ⊕ 8_q ⊕ 8_q ⊕ 1_q`)**:
Over any field `K` with `q ≠ 0`, `q - q⁻¹ ≠ 0`, `q + q⁻¹ ≠ 0`, and `[3]_q ≠ 0`, specializing
`(x₁, x₂, x₃) = (q², 1, q⁻²)` proves:
1. `s_{(3)}(q², 1, q⁻²) = [4]_q [5]_q / [2]_q = [3]_q [4]_q [5]_q / ([2]_q [3]_q)`,
2. `s_{(2,1)}(q², 1, q⁻²) = [2]_q [4]_q = [3]_q² - 1`,
3. `s_{(1,1,1)}(q², 1, q⁻²) = 1`, and
4. `[4]_q [5]_q / [2]_q + 2 * ([2]_q [4]_q) + 1 = [3]_q³`. -/
theorem uq_sl3_weyl_qdim_cube_identity {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hqdiff : q - q⁻¹ ≠ 0) (hqsum : q + q⁻¹ ≠ 0) (hb3_ne : qIntBal q 3 ≠ 0) :
    schur3_sym (q ^ 2) 1 (q⁻¹ ^ 2) = (qIntBal q 4 * qIntBal q 5) / qIntBal q 2 ∧
    (qIntBal q 3 * qIntBal q 4 * qIntBal q 5) / (qIntBal q 2 * qIntBal q 3) =
      (qIntBal q 4 * qIntBal q 5) / qIntBal q 2 ∧
    schur3_mix (q ^ 2) 1 (q⁻¹ ^ 2) = qIntBal q 2 * qIntBal q 4 ∧
    qIntBal q 2 * qIntBal q 4 = (qIntBal q 3) ^ 2 - 1 ∧
    schur3_alt (q ^ 2) 1 (q⁻¹ ^ 2) = 1 ∧
    (qIntBal q 4 * qIntBal q 5) / qIntBal q 2 + 2 * (qIntBal q 2 * qIntBal q 4) + 1 =
      (qIntBal q 3) ^ 3 := by
  obtain ⟨_, hb2, hb3, hb4, _⟩ := qIntBal_small_laurent q hq hqdiff
  have hb2_ne : qIntBal q 2 ≠ 0 := by rw [hb2]; exact hqsum
  have hb5 : qIntBal q 5 = q ^ 4 + q ^ 2 + 1 + q⁻¹ ^ 2 + q⁻¹ ^ 4 := by
    rw [qIntBal_def, div_eq_iff hqdiff]; field_simp [hq]; ring
  have hsym : schur3_sym (q ^ 2) 1 (q⁻¹ ^ 2) = (qIntBal q 4 * qIntBal q 5) / qIntBal q 2 := by
    rw [hb2, hb4, hb5, eq_div_iff hqsum]
    unfold schur3_sym
    field_simp [hq]
    ring
  have hweyl10 :
      (qIntBal q 3 * qIntBal q 4 * qIntBal q 5) / (qIntBal q 2 * qIntBal q 3) =
        (qIntBal q 4 * qIntBal q 5) / qIntBal q 2 := by
    rw [div_eq_div_iff (mul_ne_zero hb2_ne hb3_ne) hb2_ne]
    ring
  have hmix : schur3_mix (q ^ 2) 1 (q⁻¹ ^ 2) = qIntBal q 2 * qIntBal q 4 := by
    rw [hb2, hb4]
    unfold schur3_mix
    field_simp [hq]
    ring
  have hoct : qIntBal q 2 * qIntBal q 4 = (qIntBal q 3) ^ 2 - 1 := by
    rw [hb2, hb3, hb4]
    field_simp [hq]
    ring
  have halt : schur3_alt (q ^ 2) 1 (q⁻¹ ^ 2) = 1 := by
    unfold schur3_alt
    field_simp [hq]
  have hcube :
      (qIntBal q 4 * qIntBal q 5) / qIntBal q 2 + 2 * (qIntBal q 2 * qIntBal q 4) + 1 =
        (qIntBal q 3) ^ 3 := by
    have hc := (schur3_cube_decomposition (q ^ 2) (1 : K) (q⁻¹ ^ 2)).1
    rw [hsym, hmix, halt] at hc
    rw [hc, hb3]
  exact ⟨hsym, hweyl10, hmix, hoct, halt, hcube⟩

end SchurWeylCube

/-! ## Section 2: Temperley–Lieb `(u, d)` Diquark Exchange `e₁₂` & `Λ⁰–Σ⁰` Hyperfine Splitting -/

section DiquarkTemperleyLiebExchange

/-- Temperley–Lieb `(u, d)` diquark exchange operator `e₁₂ = q • I₂ - σ₁` on `S^{(2,1)}`
(since `(σ₁ - q)(σ₁ + q⁻¹) = 0`, `e₁₂` projects onto the `-q⁻¹` antisymmetric singlet `Λ⁰` with
scale `[2]_q = q + q⁻¹` and annihilates the `+q` symmetric triplet `Σ⁰`). -/
def tlExchange12 {K : Type*} [Field K] (q : K) : Matrix (Fin 2) (Fin 2) K :=
  q • (1 : Matrix (Fin 2) (Fin 2) K) - rho21_sigma0 q

/-- Diquark colour-magnetic / Hecke hyperfine Hamiltonian `H_hf = M_uds • I₂ - κ_hf • e₁₂`
on the `(u, d, s)` mixed-symmetry space `S^{(2,1)}`. -/
def hyperfineDiquarkHamiltonian {K : Type*} [Field K] (q M_uds κ_hf : K) :
    Matrix (Fin 2) (Fin 2) K :=
  M_uds • (1 : Matrix (Fin 2) (Fin 2) K) - κ_hf • tlExchange12 q

/-- **Temperley–Lieb Relation, Exact `(0, [2]_q)` `Σ⁰/Λ⁰` Eigenvalues, and Hyperfine Splitting**:
Over any field `K` with `q ≠ 0`, `q - q⁻¹ ≠ 0`, and `q + q⁻¹ ≠ 0`:
1. `e₁₂² = [2]_q • e₁₂`,
2. `e₁₂ * P_{Σ⁰} = 0` and `tr(P_{Σ⁰} * e₁₂) = 0`,
3. `e₁₂ * P_Λ = [2]_q • P_Λ` and `tr(P_Λ * e₁₂) = [2]_q`,
4. `tr(P_{Σ⁰} * H_hf) - tr(P_Λ * H_hf) = κ_hf * [2]_q`, and
5. `[3]_q - 1 = q² + q⁻² = [2]_q² - 2` (`dim_q(Sym²_q V₂) - dim_q(Λ²_q V₂)`). -/
theorem tlExchange12_diquark_eigenvalues_and_hyperfine_split {K : Type*} [Field K]
    (q M_uds κ_hf : K) (hq : q ≠ 0) (hqdiff : q - q⁻¹ ≠ 0) (hqsum : q + q⁻¹ ≠ 0) :
    tlExchange12 q * tlExchange12 q = (qIntBal q 2) • tlExchange12 q ∧
    tlExchange12 q * projDiquarkSigma0 q = 0 ∧
    (projDiquarkSigma0 q * tlExchange12 q).trace = 0 ∧
    tlExchange12 q * projDiquarkLambda q = (qIntBal q 2) • projDiquarkLambda q ∧
    (projDiquarkLambda q * tlExchange12 q).trace = qIntBal q 2 ∧
    (projDiquarkSigma0 q * hyperfineDiquarkHamiltonian q M_uds κ_hf).trace -
      (projDiquarkLambda q * hyperfineDiquarkHamiltonian q M_uds κ_hf).trace =
      κ_hf * qIntBal q 2 ∧
    qIntBal q 3 - 1 = q ^ 2 + q⁻¹ ^ 2 ∧
    q ^ 2 + q⁻¹ ^ 2 = (qIntBal q 2) ^ 2 - 2 := by
  obtain ⟨_, hb2, hb3, _, _⟩ := qIntBal_small_laurent q hq hqdiff
  have hid' : (q + q⁻¹) * (q + q⁻¹)⁻¹ = 1 := mul_inv_cancel₀ hqsum
  have htl : tlExchange12 q = !![q + q⁻¹, 1; 0, 0] := by
    unfold tlExchange12
    rw [rho21_sigma0_eq]
    ext i j; fin_cases i <;> fin_cases j <;> simp [sub_neg_eq_add]
  have htl_sq : tlExchange12 q * tlExchange12 q = (qIntBal q 2) • tlExchange12 q := by
    rw [htl, hb2]
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [Matrix.mul_apply, Fin.sum_univ_two]; try ring)
  have hsig_ann : tlExchange12 q * projDiquarkSigma0 q = 0 := by
    rw [htl, projDiquarkSigma0_eq hqsum]
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two, hid']
  have htr_sig : (projDiquarkSigma0 q * tlExchange12 q).trace = 0 := by
    rw [projDiquarkSigma0_eq hqsum, htl]
    simp [Matrix.trace_fin_two]
  have hlam_eig : tlExchange12 q * projDiquarkLambda q = (qIntBal q 2) • projDiquarkLambda q := by
    rw [htl, projDiquarkLambda_eq hqsum, hb2]
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two]
  have htr_lam : (projDiquarkLambda q * tlExchange12 q).trace = qIntBal q 2 := by
    rw [projDiquarkLambda_eq hqsum, htl, hb2]
    simp [Matrix.trace_fin_two]
  have hhf :
      (projDiquarkSigma0 q * hyperfineDiquarkHamiltonian q M_uds κ_hf).trace -
        (projDiquarkLambda q * hyperfineDiquarkHamiltonian q M_uds κ_hf).trace =
        κ_hf * qIntBal q 2 := by
    have htr_sig1 : (projDiquarkSigma0 q).trace = 1 := by
      rw [projDiquarkSigma0_eq hqsum]
      simp [Matrix.trace_fin_two]
    have htr_lam1 : (projDiquarkLambda q).trace = 1 := by
      rw [projDiquarkLambda_eq hqsum]
      simp [Matrix.trace_fin_two]
    unfold hyperfineDiquarkHamiltonian
    simp only [mul_sub, Matrix.mul_smul, mul_one, Matrix.trace_sub, Matrix.trace_smul,
      htr_sig1, htr_lam1, htr_sig, htr_lam, smul_eq_mul]
    ring
  have hdim_exc1 : qIntBal q 3 - 1 = q ^ 2 + q⁻¹ ^ 2 := by
    rw [hb3]; ring
  have hdim_exc2 : q ^ 2 + q⁻¹ ^ 2 = (qIntBal q 2) ^ 2 - 2 := by
    rw [hb2]; field_simp [hq]; ring
  exact ⟨htl_sq, hsig_ann, htr_sig, hlam_eig, htr_lam, hhf, hdim_exc1, hdim_exc2⟩

end DiquarkTemperleyLiebExchange

/-! ## Section 3: First-Order Baryon GMO & 2nd-Order Quantum Casimir Decuplet Asymmetry -/

section FirstOrderGmoAndQuantumDecuplet

/-- First-order `SU(3)_f`-breaking hadron mass formula
`M(I, Y) = M₀ + a * Y + b * (I * (I + 1) - Y² / 4)` over `[Field K]`. -/
def firstOrderHadronMass {K : Type*} [Field K] (M₀ a b I_val Y_val : K) : K :=
  M₀ + a * Y_val + b * (I_val * (I_val + 1) - Y_val ^ 2 / 4)

/-- **First-Order Baryon Octet GMO Cancellation, `Σ–Λ` Split `2b`, & Decuplet Equal Spacing**:
Over any field `K` with `(2 : K) ≠ 0`:
1. `M_Σ - M_Λ = 2 * b`,
2. `2 * (M_N + M_Ξ) - (3 * M_Λ + M_Σ) = 0`, and
3. `(M_{Σ*} - M_Δ, M_{Ξ*} - M_{Σ*}, M_{Ω⁻} - M_{Ξ*}) = (-a - 3b/2, -a - 3b/2, -a - 3b/2)`. -/
theorem firstOrder_baryon_gmo_and_decuplet_equal_spacing {K : Type*} [Field K]
    (h2 : (2 : K) ≠ 0) (M₀ a b : K) :
    let mN := firstOrderHadronMass M₀ a b ((1 : K) / 2) 1
    let mXi := firstOrderHadronMass M₀ a b ((1 : K) / 2) (-1)
    let mLam := firstOrderHadronMass M₀ a b 0 0
    let mSig := firstOrderHadronMass M₀ a b 1 0
    let mDel := firstOrderHadronMass M₀ a b ((3 : K) / 2) 1
    let mSigS := firstOrderHadronMass M₀ a b 1 0
    let mXiS := firstOrderHadronMass M₀ a b ((1 : K) / 2) (-1)
    let mOm := firstOrderHadronMass M₀ a b 0 (-2)
    mSig - mLam = 2 * b ∧
    2 * (mN + mXi) - (3 * mLam + mSig) = 0 ∧
    mSigS - mDel = -a - (3 : K) / 2 * b ∧
    mXiS - mSigS = -a - (3 : K) / 2 * b ∧
    mOm - mXiS = -a - (3 : K) / 2 * b := by
  dsimp only [firstOrderHadronMass]
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by ring
    rw [e]; exact mul_ne_zero h2 h2
  refine ⟨by ring, ?_, ?_, ?_, ?_⟩
  · field_simp [h2, h4]; ring
  · field_simp [h2, h4]; ring
  · field_simp [h2, h4]; ring
  · field_simp [h2, h4]; ring

/-- Rational square-root-free quantum Casimir `d_q(3/2, +1) = [3/2]_q [5/2]_q - [1/2]_q²` on `Δ`. -/
def qCasimirDecupletDelta {K : Type*} [Field K] (q : K) : K :=
  (q ^ 6 + 2 * q ^ 5 + 3 * q ^ 4 + 2 * q ^ 3 + 3 * q ^ 2 + 2 * q + 1) /
    (q ^ 2 * (q + 1) ^ 2)

/-- Rational quantum Casimir `d_q(1, 0) = q + q⁻¹` on `Σ*`. -/
def qCasimirDecupletSigmaStar {K : Type*} [Field K] (q : K) : K :=
  q + q⁻¹

/-- Rational quantum Casimir `d_q(1/2, -1) = (q + q⁻¹) / (q + 2 + q⁻¹)` on `Ξ*`. -/
def qCasimirDecupletXiStar {K : Type*} [Field K] (q : K) : K :=
  (q + q⁻¹) / (q + 2 + q⁻¹)

/-- Rational quantum Casimir `d_q(0, -2) = -[1]_q² = -1` on `Ω⁻`. -/
def qCasimirDecupletOmega {K : Type*} [Field K] (_q : K) : K :=
  -1

/-- Decuplet mass operator `M(I, Y) = M₀ + a * Y + c * d_q(I, Y)` under the rational quantum Casimir. -/
def qDecupletMass {K : Type*} [Field K] (M₀ a c dVal Y : K) : K :=
  M₀ + a * Y + c * dVal

/-- **Quantum Casimir Decuplet Second-Difference Asymmetry Theorem (`[Field K]`)**:
Unlike the classical 2nd-order polynomial ansatz (`GellMannOkuboSecondOrder.decuplet_second_differences_equal`,
where `spacingUpper = spacingLower`), the `U_q(sl₃)` / `U_q(sl₂)` rational quantum Casimir
`d_q(I, Y) = [I]_q [I+1]_q - [Y/2]_q²` satisfies:
1. Classical `q = 1` recovery: `(d_Δ(1), d_{Σ*}(1), d_{Ξ*}(1), d_Ω(1)) = (7/2, 2, 1/2, -1)`.
2. Exact lower second difference:
   `M_{Ξ*} - 2 M_{Σ*} + M_Δ = c * ((q - 1) / (q + 1)) ^ 2 * (q + 1 + q⁻¹) ^ 2`.
3. Exact upper second difference:
   `M_{Ω⁻} - 2 M_{Ξ*} + M_{Σ*} = c * ((q - 1) / (q + 1)) ^ 2 * (q + 1 + q⁻¹)`.
4. Universal `(M₀, a, c)`-free asymmetry ratio (`c ≠ 0, q - 1 ≠ 0, q + 1 + q⁻¹ ≠ 0`):
   `(M_{Ω⁻} - 2 M_{Ξ*} + M_{Σ*}) / (M_{Ξ*} - 2 M_{Σ*} + M_Δ) = 1 / (q + 1 + q⁻¹)` (`= 1/3` as `q → 1`). -/
theorem qCasimir_decuplet_second_differences_and_ratio {K : Type*} [Field K]
    (M₀ a c q : K) (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (hqp1 : q + 1 ≠ 0)
    (hc : c ≠ 0) (hqm1 : q - 1 ≠ 0) (htri : q + 1 + q⁻¹ ≠ 0) :
    let mDel := qDecupletMass M₀ a c (qCasimirDecupletDelta q) 1
    let mSigS := qDecupletMass M₀ a c (qCasimirDecupletSigmaStar q) 0
    let mXiS := qDecupletMass M₀ a c (qCasimirDecupletXiStar q) (-1)
    let mOm := qDecupletMass M₀ a c (qCasimirDecupletOmega q) (-2)
    (qCasimirDecupletDelta (1 : K) = (7 : K) / 2 ∧
      qCasimirDecupletSigmaStar (1 : K) = 2 ∧
      qCasimirDecupletXiStar (1 : K) = (1 : K) / 2 ∧
      qCasimirDecupletOmega (1 : K) = -1) ∧
    mXiS - 2 * mSigS + mDel = c * ((q - 1) / (q + 1)) ^ 2 * (q + 1 + q⁻¹) ^ 2 ∧
    mOm - 2 * mXiS + mSigS = c * ((q - 1) / (q + 1)) ^ 2 * (q + 1 + q⁻¹) ∧
    (mOm - 2 * mXiS + mSigS) / (mXiS - 2 * mSigS + mDel) = 1 / (q + 1 + q⁻¹) := by
  dsimp only [qDecupletMass]
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by ring
    rw [e]; exact mul_ne_zero h2 h2
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have hm_den : q * (q + 2 + q⁻¹) = (q + 1) ^ 2 := by linear_combination hqi
  have hdenq : q + 2 + q⁻¹ ≠ 0 := by
    intro h0
    have hsq0 : (q + 1) ^ 2 = 0 := hm_den.symm.trans (by rw [h0, mul_zero])
    exact pow_ne_zero 2 hqp1 hsq0
  have hq1_vals :
      qCasimirDecupletDelta (1 : K) = (7 : K) / 2 ∧
      qCasimirDecupletSigmaStar (1 : K) = 2 ∧
      qCasimirDecupletXiStar (1 : K) = (1 : K) / 2 ∧
      qCasimirDecupletOmega (1 : K) = -1 := by
    refine ⟨?_, ?_, ?_, rfl⟩
    · unfold qCasimirDecupletDelta
      have h11 : (1 : K) ^ 2 * (1 + 1) ^ 2 = 4 := by ring
      rw [h11, div_eq_div_iff h4 h2]; ring
    · unfold qCasimirDecupletSigmaStar; ring
    · unfold qCasimirDecupletXiStar
      have h14 : (1 : K) + 2 + (1 : K)⁻¹ = 4 := by ring
      rw [h14, div_eq_div_iff h4 h2]; ring
  have hxi_rat : qCasimirDecupletXiStar q = (q ^ 2 + 1) / (q + 1) ^ 2 := by
    unfold qCasimirDecupletXiStar
    rw [div_eq_div_iff hdenq (pow_ne_zero 2 hqp1)]
    field_simp [hq]
    ring
  have hlow :
      M₀ + a * (-1) + c * qCasimirDecupletXiStar q -
          2 * (M₀ + a * 0 + c * qCasimirDecupletSigmaStar q) +
          (M₀ + a * 1 + c * qCasimirDecupletDelta q) =
        c * ((q - 1) / (q + 1)) ^ 2 * (q + 1 + q⁻¹) ^ 2 := by
    rw [hxi_rat]
    unfold qCasimirDecupletSigmaStar qCasimirDecupletDelta
    field_simp [hq, hqp1]
    ring
  have hupp :
      M₀ + a * (-2) + c * qCasimirDecupletOmega q -
          2 * (M₀ + a * (-1) + c * qCasimirDecupletXiStar q) +
          (M₀ + a * 0 + c * qCasimirDecupletSigmaStar q) =
        c * ((q - 1) / (q + 1)) ^ 2 * (q + 1 + q⁻¹) := by
    rw [hxi_rat]
    unfold qCasimirDecupletOmega qCasimirDecupletSigmaStar
    field_simp [hq, hqp1]
    ring
  refine ⟨hq1_vals, hlow, hupp, ?_⟩
  rw [hupp, hlow]
  have hfac_ne : c * ((q - 1) / (q + 1)) ^ 2 ≠ 0 :=
    mul_ne_zero hc (pow_ne_zero 2 (div_ne_zero hqm1 hqp1))
  rw [div_eq_div_iff (mul_ne_zero hfac_ne (pow_ne_zero 2 htri)) htri]
  ring

end FirstOrderGmoAndQuantumDecuplet

end BaryonOctetDiquarkGmoDerivation
end QOU.EightfoldWay
