/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.MassTheory.ProtonQ3SchurElement

/-!
# Skew-Howe `(1³)_c ⊗ (3)_f` Higman–Schur Norm vs Convention-D Markov Weight (`qou-2eg2`)

Formalizes `NF-P4` (bean `qou-2eg2`, epic `qou-qzvs`) over a generic field `K` (§7c, zero `ℝ`,
zero empirical literals, zero `sorry`), building directly on `QOU.MassTheory.ProtonQ3Schur`:

1. **Symmetric Tensor-Product Schur Factors Cancel `/q³` (`tensorSchurSingletSym_bar_invariant`).**
   Under `U_q(𝔤𝔩₃) × U_q(𝔤𝔩₂)` skew-Howe duality at `n = 3` (`ColourFlavourMirror`), the colour
   singlet `(1³)_c` pairs with the totally symmetric flavour sector `(3)_f` (while `(2,1)_c` pairs
   with `(2,1)_f`):
   - Multiplying both factors' Schur elements on `(1³)_c ⊗ (3)_f` gives
     `c_{(1³)}(q) · c_{(3)}(q) = ([3]_q!/q³) · (q³ [3]_q!) = ([3]_q!)²`
     (`tensorSchurSingletSym_eq_sq`), which is **strictly bar-invariant** (`q⁻³ · q³ = 1` cancels
     `q^{±3}` identically).
   - Multiplying both Schur elements on `(2,1)_c ⊗ (2,1)_f` gives `c_{(2,1)}(q)² = [3]_q²`, also
     strictly bar-invariant (`tensorSchurReflRefl_bar_invariant`).

2. **Convention-D Flavour Markov Weights `y_λ(q)` Are Individually Bar-Symmetric.**
   At `z_D = q³/(q² + 1)`:
   - `y_{(1³)}(q) = tr_{z_D}(x₋) / c_{(1³)}(q) = 0` (`markovWeightSign_zD_eq_zero`);
   - `y_{(3)}(q) = tr_{z_D}(x₊) / c_{(3)}(q) = (q⁴ + 1)/(q² + 1)²` (`markovWeightTriv_zD_eq`),
     because the `q³` factor inside `tr_{z_D}(x₊)` cancels the `q³` inside `c_{(3)}(q) = q³[3]_q!`;
   - `y_{(2,1)}(q) = q²/(q² + 1)² = [2]_q⁻²` (`markovWeightRefl_sum_one`);
   - Both `y_{(3)}(q)` and `y_{(2,1)}(q)` are strictly bar-invariant (`markovWeightTriv_bar`,
     `markovWeightRefl_bar`).

3. **Exact Condition for `/q³` Survival vs Cancellation (`colourSignSchur_mul_trMBorromean`).**
   Evaluating the Frobenius/Schur element `c_{(1³)}(q) = [3]_q!/q³` on the colour singlet **alone**
   while closing the flavour factor `(3)_f` (or full `H₃` flavour trace `tr_M(β_Bor)`) with the
   Convention-D Markov weight `y_λ` yields `c_{(1³)}(q) · y_{(3)}(q)` (and `c_{(1³)}(q) · tr_M =
   fBor q`), retaining the exact `/q³` factor (`mirror ratio = q⁶`). Choosing between symmetric
   colour×flavour Schur pairing (which cancels `/q³`) and asymmetric colour-Schur × flavour-Markov
   pairing (which yields `fBor q`) is an explicit structural distinction, stated here without
   overclaiming a derivation from the axioms alone.

-- Ref: [leitner2026] beans qou-2eg2, qou-24w9, qou-qzvs
-- Ref: [geckpfeiffer2000] Characters of Finite Coxeter Groups and Iwahori–Hecke Algebras, Ch. 8–9
-/

namespace QOU.MassTheory.SkewHoweProtonSchurNorm

open QOU.MassTheory.PoincareCentering
open QOU.MassTheory.ProtonQ3Schur

section GenericField

variable {K : Type*} [Field K]

/-- Generic-field Convention-D Markov parameter `z_D = q³ / (q² + 1)`. -/
def zDGen (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- Tensor-product Higman–Schur factor `c_{(1³)}(q) · c_{(3)}(q)` on the skew-Howe colour-singlet
slice `(1³)_c ⊗ (3)_f`. -/
def tensorSchurSingletSym (q : K) : K := schurSign q * schurTriv q

/-- Tensor-product Higman–Schur factor `c_{(2,1)}(q) · c_{(2,1)}(q)` on `(2,1)_c ⊗ (2,1)_f`. -/
def tensorSchurReflRefl (q : K) : K := schurRefl q * schurRefl q

/-- Convention-D Markov weight `y_{(3)}(q) = (q⁴ + 1) / (q² + 1)²` of the symmetric `(3)` block. -/
def markovWeightTriv (q : K) : K := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- Convention-D Markov weight `y_{(2,1)}(q) = q² / (q² + 1)²` of the reflection `(2,1)` block. -/
def markovWeightRefl (q : K) : K := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- **Cancellation of `q^{±3}` in the symmetric skew-Howe Schur product:**
`c_{(1³)}(q) · c_{(3)}(q) = ([3]_q!)²`. -/
theorem tensorSchurSingletSym_eq_sq (q : K) (hq : q ≠ 0) :
    tensorSchurSingletSym q = qFactThreeBalanced q ^ 2 := by
  unfold tensorSchurSingletSym
  rw [mul_comm, schurTriv_mul_schurSign q hq]

/-- **Strict bar-invariance of `c_{(1³)}(q) · c_{(3)}(q)` on `(1³)_c ⊗ (3)_f`.** -/
theorem tensorSchurSingletSym_bar_invariant (q : K) (hq : q ≠ 0) :
    tensorSchurSingletSym q⁻¹ = tensorSchurSingletSym q := by
  rw [tensorSchurSingletSym_eq_sq q⁻¹ (inv_ne_zero hq), tensorSchurSingletSym_eq_sq q hq,
    ← balanced_is_bar_symmetric q hq]

/-- `c_{(2,1)}(q) = q² + 1 + q⁻²` is bar-invariant. -/
theorem schurRefl_bar_invariant (q : K) :
    schurRefl q⁻¹ = schurRefl q := by
  unfold schurRefl
  rw [inv_inv]
  ring

/-- **Strict bar-invariance of `c_{(2,1)}(q)²` on `(2,1)_c ⊗ (2,1)_f`.** -/
theorem tensorSchurReflRefl_bar_invariant (q : K) :
    tensorSchurReflRefl q⁻¹ = tensorSchurReflRefl q := by
  unfold tensorSchurReflRefl
  rw [schurRefl_bar_invariant]

/-- **Convention D kills the `(1³)` Markov weight:** `tr_{z_D}(x₋) = 0`. -/
theorem trXMinus_zDGen_eq_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trXMinus q (zDGen q) = 0 := by
  rw [trXMinus_factor q (zDGen q) hq]
  unfold zDGen
  field_simp
  ring

/-- Hence `y_{(1³)}(q) = tr_{z_D}(x₋) / c_{(1³)}(q) = 0`. -/
theorem markovWeightSign_zD_eq_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trXMinus q (zDGen q) / schurSign q = 0 := by
  rw [trXMinus_zDGen_eq_zero q hq hq2, zero_div]

/-- **Exact closed form of `tr_{z_D}(x₊)`:**
`tr_{z_D}(x₊) = (q⁴ + q² + 1)(q⁴ + 1)² / ...` — specifically
`tr_{z_D}(x₊) = (q⁴ + q² + 1)(q⁴ + 1) / (q² + 1)`? Let us prove the exact rational formula
`tr_{z_D}(x₊) = (q⁴ + q² + 1) * (q⁴ + 1) / (q² + 1)`? Wait: check `q³ z_D + q z_D + 1`:
`(q³ + q) * q³ / (q² + 1) + 1 = q⁴ + 1`, and `q z_D + 1 = (q⁴ + q² + 1) / (q² + 1)`! -/
theorem trXPlus_zDGen_eq (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trXPlus q (zDGen q) = (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + 1) / (q ^ 2 + 1) := by
  rw [trXPlus_factor q (zDGen q) hq]
  unfold zDGen
  field_simp
  ring

/-- **Convention-D Markov weight `y_{(3)}(q) = tr_{z_D}(x₊) / c_{(3)}(q) = (q⁴ + 1)/(q² + 1)²`.**
Notice that `q³` inside `c_{(3)}(q) = q³ [3]_q!` cancels against `tr_{z_D}(x₊)`, leaving a
bar-symmetric rational function. -/
theorem markovWeightTriv_zD_eq (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hP : 1 + 2 * q ^ 2 + 2 * q ^ 4 + q ^ 6 ≠ 0) :
    trXPlus q (zDGen q) / schurTriv q = markovWeightTriv q := by
  rw [trXPlus_zDGen_eq q hq hq2]
  unfold schurTriv poincareS3
  have hfac : (1 + 2 * q ^ 2 + 2 * q ^ 4 + q ^ 6 : K) = (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) := by
    ring
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by
    intro hz
    apply hP
    rw [hfac, hz, mul_zero]
  rw [hfac, div_div, div_eq_iff (mul_ne_zero hq2 (mul_ne_zero hq2 hq4))]
  unfold markovWeightTriv
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp

/-- **`y_{(3)}(q)` is strictly bar-invariant.** -/
theorem markovWeightTriv_bar (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    markovWeightTriv q⁻¹ = markovWeightTriv q := by
  unfold markovWeightTriv
  have e : (q⁻¹) ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by field_simp; ring
  rw [e]
  field_simp
  ring

/-- **`y_{(2,1)}(q) = [2]_q⁻²` and is strictly bar-invariant.** -/
theorem markovWeightRefl_eq_inv_qd2_sq (q : K) (hq : q ≠ 0) :
    markovWeightRefl q = 1 / (q + q⁻¹) ^ 2 := by
  unfold markovWeightRefl
  have e : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [e]
  field_simp

theorem markovWeightRefl_bar (q : K) (hq : q ≠ 0) :
    markovWeightRefl q⁻¹ = markovWeightRefl q := by
  rw [markovWeightRefl_eq_inv_qd2_sq q⁻¹ (inv_ne_zero hq), markovWeightRefl_eq_inv_qd2_sq q hq,
    inv_inv, add_comm q⁻¹ q]

/-- **Partition of unity of the Convention-D Markov weights on `H₃(q)`:**
`1 · y_{(3)}(q) + 2 · y_{(2,1)}(q) + 1 · 0 = 1`. -/
theorem markovWeight_partition_of_unity (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    markovWeightTriv q + 2 * markovWeightRefl q = 1 := by
  unfold markovWeightTriv markovWeightRefl
  field_simp
  ring

/-- **Asymmetric colour-Schur × flavour-Markov pairing on `(1³)_c ⊗ (3)_f`:**
pairing the colour-singlet Frobenius/Schur element `c_{(1³)}(q) = [3]_q!/q³` with the Convention-D
flavour Markov weight `y_{(3)}(q)` preserves the `/q³` normaliser. -/
theorem colourSignSchur_mul_flavourMarkovTriv (q : K) (hq : q ≠ 0) :
    schurSign q * markovWeightTriv q =
      (qFactThreeBalanced q / q ^ 3) * ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) := by
  rw [fBor_normaliser_eq_schurSign q hq]
  rfl

/-- **Exact `F_Bor` factorisation via asymmetric colour-Schur × flavour-Markov pairing:**
- Pairing colour `c_{(1³)}(q)` with flavour `trMBorromean q` yields `fBor q = tr_M · [3]_q! / q³`;
- Pairing colour `c_{(3)}(q)` with flavour `trMBorromean q` yields `fBor q⁻¹ = q⁶ · fBor q`;
- Pairing the symmetric skew-Howe Schur product `c_{(1³)}(q) · c_{(3)}(q)` with `trMBorromean q`
  yields the strictly bar-invariant `([3]_q!)² · tr_M`. -/
theorem colourSchur_flavourMarkov_dichotomy (q : K) (hq : q ≠ 0) :
    schurSign q * trMBorromean q = fBor q ∧
    schurTriv q * trMBorromean q = fBor q⁻¹ ∧
    tensorSchurSingletSym q * trMBorromean q = qFactThreeBalanced q ^ 2 * trMBorromean q := by
  refine ⟨?_, ?_, ?_⟩
  · unfold fBor
    rw [← fBor_normaliser_eq_schurSign q hq]
    ring
  · rw [fbor_mirror_ratio q hq, schurTriv_eq q hq]
    unfold fBor
    field_simp
  · rw [tensorSchurSingletSym_eq_sq q hq]

end GenericField

end QOU.MassTheory.SkewHoweProtonSchurNorm
