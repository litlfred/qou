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

/-!
# Algebraic Characterization and Exact Obstructions for `[3]_q · [4]_q` (`§7c` Generic)

This module formalizes the pure algebraic (`[Monoid A]`, `[Field K]`, zero `ℝ`) results of
beans `qou-3l2l` and `qou-5ipv` (Issue `#9369`), separated from the archimedean `ℝ` module
`QOU.EightfoldWay.MesonKaonPionSchwingerBridge` per `AGENTS.md` §7c:

1. **Eightfold Way Split-Bundle `F = V₂ ⊕ W₃*` Quantum Dimensions (`splitBundle_sym2_w3_tensor_v2_eq_3x4`):**
   Proves over any field `K` (`q ≠ 0`, `q - q⁻¹ ≠ 0`, `q + q⁻¹ ≠ 0`) that:
   - the `W₃*` diquark square decomposes as `dim_q(Λ²_q W₃*) + dim_q(Sym²_q W₃*) = [3]_q + [3]_q[4]_q/[2]_q = [3]_q²`,
   - the `W₃ ⊗ W₃*` meson square decomposes as `dim_q(8) + 1 = [2]_q[4]_q + 1 = [3]_q²`, and
   - tensoring the symmetric diquark `Sym²_q W₃*` with the weak-isospin doublet `V₂` (`dim_q = [2]_q`)
     gives exact quantum dimension `dim_q(V₂ ⊗ Sym²_q W₃*) = [3]_q [4]_q = [2]_q + [4]_q + [6]_q`
     (matching the `j = 3` `U_q(sl₂)` quadratic Casimir `[3]_q [4]_q`), whereas the intra-octet
     kaon-to-pion multiplicity ratio is `[4]_q / [3]_q`.

2. **Exact Cyclotomic Curvature-Gap Identities for All `a · b = 12` Factorizations (`twelve_factorizations_cyclotomic_gaps`):**
   Proves over any field `K` (`q ≠ 0`, `q - q⁻¹ ≠ 0`) that among all three factorizations
   `(1, 12)`, `(2, 6)`, `(3, 4)` of `12`, the differences factor over `q + q⁻¹ - 2`:
   - `[2]_q [6]_q - [3]_q [4]_q = (q + q⁻¹ - 2) * [2]_q * [3]_q * ([2]_q + [3]_q)`,
   - `[1]_q [12]_q - [2]_q [6]_q = (q + q⁻¹ - 2) * [6]_q * ([2]_q + [3]_q) * ([3]_q + [4]_q)`.

3. **Hecke `q → 1` Odd-Clasp Collapse Obstruction (`involutive_odd_clasp_eq_sq`, `claspHecke21_pion_eq_kaon_at_one`):**
   Proves over any (possibly non-commutative) `[Monoid A]` that whenever `s₁² = 1` and `s₂² = 1`,
   `s₁ ^ (2 * k₁ + 1) * s₂ ^ (2 * k₂ + 1) * s₁ * s₂ = (s₁ * s₂) ^ 2` for all `k₁, k₂ : ℕ`, and
   specializes directly to `HyperbolicMesonClaspAndDiquarkSplit.claspHecke21` at `q = 1`:
   `claspHecke21 (1 : K) 3 3 = claspHecke21 (1 : K) 3 5` with trace `-1`. Thus bare `H₃(q)` linear
   functional / Markov-trace ratios between `(3, 5)` and `(3, 3)` collapse to `1 ≠ 12` at `q = 1`.

4. **Gell-Mann–Oakes–Renner Isospin Ratio & Dashen Equal-EM Ratio Identity (`gmor_isospin_quark_ratio_iff`, `dashen_equal_em_shift_identity`):**
   Proves `(1 + r_sd) / 2 = [3]_q [4]_q ↔ r_sd = 2 [3]_q [4]_q - 1` and
   `(R₀ * m₀_sq + dEM) / (m₀_sq + dEM) - R₀ = -(R₀ - 1) * dEM / (m₀_sq + dEM)`.
-/

set_option autoImplicit false

namespace QOU.EightfoldWay
namespace MesonThreeByFourCharacterization

open QOU.QInteger (qIntBal qIntBal_def)
open QOU.Eightfold.HyperbolicMesonClaspAndDiquarkSplit
  (claspHecke21 rho21_sigma0_pow3 rho21_sigma1_inv_pow3 rho21_sigma1_inv_pow5)
open QOU.QBeta.BorromeanFlavourPivotalUnification (rho21_sigma0_eq rho21_sigma1_inv_eq)

/-! ## Section 1: Split-Bundle `F = V₂ ⊕ W₃*` Quantum Dimensions & `12 = a · b` Curvature Gaps -/

section QuantumDimensionCharacterization

/-- Quantum `U_q(sl₃)` symmetric diquark `Sym²_q(W₃*)` (`6̄`) Weyl quantum dimension `[3]_q [4]_q / [2]_q`. -/
noncomputable def qDimSym2W3 {K : Type*} [Field K] (q : K) : K :=
  (qIntBal q 3 * qIntBal q 4) / qIntBal q 2

/-- Quantum `U_q(sl₃)` antisymmetric diquark `Λ²_q(W₃*)` (`3`) Weyl quantum dimension `[3]_q`. -/
noncomputable def qDimAlt2W3 {K : Type*} [Field K] (q : K) : K :=
  qIntBal q 3

/-- Explicit Laurent expansions of `qIntBal q n` for `n = 1, 2, 3, 4, 6` when `q ≠ 0` and `q - q⁻¹ ≠ 0`. -/
theorem qIntBal_small_laurent {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hqdiff : q - q⁻¹ ≠ 0) :
    qIntBal q 1 = 1 ∧
    qIntBal q 2 = q + q⁻¹ ∧
    qIntBal q 3 = q ^ 2 + 1 + q⁻¹ ^ 2 ∧
    qIntBal q 4 = q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3 ∧
    qIntBal q 6 = q ^ 5 + q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3 + q⁻¹ ^ 5 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [qIntBal_def, div_eq_iff hqdiff]; ring
  · rw [qIntBal_def, div_eq_iff hqdiff]; ring
  · rw [qIntBal_def, div_eq_iff hqdiff]; field_simp [hq]; ring
  · rw [qIntBal_def, div_eq_iff hqdiff]; field_simp [hq]; ring
  · rw [qIntBal_def, div_eq_iff hqdiff]; field_simp [hq]; ring

/-- **Split-Bundle `F = V₂ ⊕ W₃*` Diquark/Meson Decompositions and `V₂ ⊗ Sym²_q(W₃*)` Product**:
For any field `K` and `q : K` with `q ≠ 0`, `q - q⁻¹ ≠ 0`, and `q + q⁻¹ ≠ 0`:
1. `dim_q(Λ²_q W₃*) + dim_q(Sym²_q W₃*) = [3]_q²`,
2. `[2]_q [4]_q + 1 = [3]_q²` (`W₃ ⊗ W₃* = 8 ⊕ 1`),
3. `[2]_q * dim_q(Sym²_q W₃*) = [3]_q [4]_q` and `[3]_q [4]_q = [2]_q + [4]_q + [6]_q`. -/
theorem splitBundle_sym2_w3_tensor_v2_eq_3x4 {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hqdiff : q - q⁻¹ ≠ 0) (hqsum : q + q⁻¹ ≠ 0) :
    qDimAlt2W3 q + qDimSym2W3 q = (qIntBal q 3) ^ 2 ∧
    qIntBal q 2 * qIntBal q 4 + 1 = (qIntBal q 3) ^ 2 ∧
    qIntBal q 2 * qDimSym2W3 q = qIntBal q 3 * qIntBal q 4 ∧
    qIntBal q 3 * qIntBal q 4 = qIntBal q 2 + qIntBal q 4 + qIntBal q 6 := by
  obtain ⟨_, hb2, hb3, hb4, hb6⟩ := qIntBal_small_laurent q hq hqdiff
  have hb2_ne : qIntBal q 2 ≠ 0 := by rw [hb2]; exact hqsum
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold qDimAlt2W3 qDimSym2W3
    rw [hb2, hb3, hb4]
    apply mul_left_cancel₀ hqsum
    rw [mul_add, mul_div_cancel₀ _ hqsum]
    field_simp [hq]
    ring
  · rw [hb2, hb3, hb4]
    field_simp [hq]
    ring
  · unfold qDimSym2W3
    exact mul_div_cancel₀ _ hb2_ne
  · rw [hb2, hb3, hb4, hb6]
    field_simp [hq]
    ring

/-- **Exact Cyclotomic Curvature-Gap Identities Across All `a · b = 12` Factorizations**:
Over any field `K` with `q ≠ 0` and `q - q⁻¹ ≠ 0`, the gaps among `[3]_q [4]_q`, `[2]_q [6]_q`,
and `[1]_q [12]_q` factor explicitly into products of `(q + q⁻¹ - 2)` and lower quantum integers:
1. `[2]_q [6]_q - [3]_q [4]_q = (q + q⁻¹ - 2) * [2]_q * [3]_q * ([2]_q + [3]_q)`,
2. `[1]_q [12]_q - [2]_q [6]_q = (q + q⁻¹ - 2) * [6]_q * ([2]_q + [3]_q) * ([3]_q + [4]_q)`. -/
theorem twelve_factorizations_cyclotomic_gaps {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hqdiff : q - q⁻¹ ≠ 0) :
    qIntBal q 2 * qIntBal q 6 - qIntBal q 3 * qIntBal q 4 =
      (q + q⁻¹ - 2) * qIntBal q 2 * qIntBal q 3 * (qIntBal q 2 + qIntBal q 3) ∧
    qIntBal q 1 * qIntBal q 12 - qIntBal q 2 * qIntBal q 6 =
      (q + q⁻¹ - 2) * qIntBal q 6 * (qIntBal q 2 + qIntBal q 3) * (qIntBal q 3 + qIntBal q 4) := by
  obtain ⟨hb1, hb2, hb3, hb4, hb6⟩ := qIntBal_small_laurent q hq hqdiff
  refine ⟨?_, ?_⟩
  · rw [hb2, hb3, hb4, hb6]
    field_simp [hq]
    ring
  · apply mul_left_cancel₀ hqdiff
    have hb12 : (q - q⁻¹) * qIntBal q 12 = q ^ 12 - q⁻¹ ^ 12 := by
      rw [qIntBal_def, mul_div_cancel₀ _ hqdiff]
    rw [hb1, one_mul, mul_sub, hb12, hb2, hb3, hb4, hb6]
    field_simp [hq]
    ring

end QuantumDimensionCharacterization

/-! ## Section 2: Non-Commutative Hecke `q → 1` Odd-Clasp Collapse Obstruction -/

section HeckeClassicalCollapseObstruction

/-- Over any (possibly non-commutative) monoid `A`, an involutive generator `s` (`s ^ 2 = 1`)
satisfies `s ^ (2 * k + 1) = s` for every `k : ℕ`. -/
theorem involutive_pow_odd {A : Type*} [Monoid A] (s : A) (hs : s ^ 2 = 1) (k : ℕ) :
    s ^ (2 * k + 1) = s := by
  induction k with
  | zero => simp
  | succ m ih =>
    have heq : 2 * (m + 1) + 1 = (2 * m + 1) + 2 := by ring
    rw [heq, pow_add, ih, hs, mul_one]

/-- **Universal Odd-Clasp Collapse Theorem (`[Monoid A]`)**:
In any monoid `A` where `s₁ ^ 2 = 1` and `s₂ ^ 2 = 1` (including the `q = 1` symmetric-group
specialization `H_n(1) = ℤ[S_n]`, where `s₂⁻¹ = s₂`), every odd-winding 3-strand gluon-clasp
word `s₁ ^ (2 * k₁ + 1) * s₂ ^ (2 * k₂ + 1) * s₁ * s₂` equals `(s₁ * s₂) ^ 2`, completely
independent of the generation indices `(k₁, k₂)`. -/
theorem involutive_odd_clasp_eq_sq {A : Type*} [Monoid A]
    (s₁ s₂ : A) (hs1 : s₁ ^ 2 = 1) (hs2 : s₂ ^ 2 = 1) (k₁ k₂ : ℕ) :
    s₁ ^ (2 * k₁ + 1) * s₂ ^ (2 * k₂ + 1) * s₁ * s₂ = (s₁ * s₂) ^ 2 := by
  rw [involutive_pow_odd s₁ hs1 k₁, involutive_pow_odd s₂ hs2 k₂, sq]
  simp only [mul_assoc]

/-- **Concrete `H₃(1)` `S^{(2,1)}` Clasp Collapse on Pion `(3, 3)` vs Kaon `(3, 5)`**:
Directly on the imported `2 × 2` representation `claspHecke21`, setting `q = 1` collapses
the pion clasp `(3, 3)` and kaon clasp `(3, 5)` to the **identical** matrix `!![0, 1; -1, -1]`
of trace `-1`, proving their classical trace ratio is `(-1) / (-1) = 1 ≠ 12`. -/
theorem claspHecke21_pion_eq_kaon_at_one {K : Type*} [Field K] :
    claspHecke21 (1 : K) 3 3 = claspHecke21 (1 : K) 3 5 ∧
    (claspHecke21 (1 : K) 3 3).trace = -1 := by
  have h1 : (1 : K) ≠ 0 := one_ne_zero
  unfold claspHecke21
  rw [rho21_sigma0_pow3 h1, rho21_sigma1_inv_pow3 h1, rho21_sigma1_inv_pow5 h1,
    rho21_sigma0_eq, rho21_sigma1_inv_eq]
  refine ⟨?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two]
  · simp [Matrix.trace_fin_two]

end HeckeClassicalCollapseObstruction

/-! ## Section 3: Gell-Mann–Oakes–Renner Isospin Equivalence & Dashen Ratio Identity -/

section ChiralAndDashenIdentities

/-- **Isospin-Symmetric Gell-Mann–Oakes–Renner Quark-Ratio Equivalence**:
Over any field `K` with `2 ≠ 0`, `(1 + r_sd) / 2 = R₀ ↔ r_sd = 2 * R₀ - 1`. Specializing
`R₀ = qIntBal q 3 * qIntBal q 4` gives `m_s / m_d = 2 * [3]_q * [4]_q - 1`. -/
theorem gmor_isospin_quark_ratio_iff {K : Type*} [Field K]
    (h2 : (2 : K) ≠ 0) (r_sd R₀ : K) :
    (1 + r_sd) / 2 = R₀ ↔ r_sd = 2 * R₀ - 1 := by
  rw [div_eq_iff h2]
  constructor
  · intro h; linear_combination h
  · intro h; linear_combination h

/-- **Exact Dashen Equal-EM Ratio Shift Identity (`[Field K]`)**:
Adding an equal electromagnetic mass-squared shift `dEM` to both numerator `R₀ * m₀_sq` and
denominator `m₀_sq` (`m₀_sq + dEM ≠ 0`) shifts the ratio by `-(R₀ - 1) * dEM / (m₀_sq + dEM)`. -/
theorem dashen_equal_em_shift_identity {K : Type*} [Field K]
    (R₀ m₀_sq dEM : K) (hden : m₀_sq + dEM ≠ 0) :
    (R₀ * m₀_sq + dEM) / (m₀_sq + dEM) - R₀ =
      -((R₀ - 1) * dEM) / (m₀_sq + dEM) := by
  field_simp [hden]
  ring

end ChiralAndDashenIdentities

end MesonThreeByFourCharacterization
end QOU.EightfoldWay
