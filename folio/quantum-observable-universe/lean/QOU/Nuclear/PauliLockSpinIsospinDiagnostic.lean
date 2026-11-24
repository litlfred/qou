import QOU.Nuclear.InterfaceScalar
import QOU.Nuclear.GramSignature
import QOU.BraidsAndKnots.S5SO3FiberAction

/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
set_option autoImplicit false

/-!
# Diagnostic Algebra and Representation Obstructions for the Pauli-Lock Interface (`qou-o43i`)

Bean `qou-o43i` establishes that the Pauli-lock S-wave separability lemma has zero non-circular
corpus instantiation sites: the isospin projector scalar pair is constructed on `H₂` / `H₃`,
whereas no corpus spin carrier constructs a two-channel spin projector scalar pair (`BringFiberAction`
maps `A5Irrep → IcosahedralRotation`, and `SpinFromSo3Fiber` constrains `levelCoeff : ℕ → R` on the
three-strand Borromean expansion).

This module supplies the exact generic algebraic and representation-theoretic foundations behind
that diagnosis, without positing a circular `fSpin := fIso` instantiation:

1. **Necessary and sufficient scalar equality under unit-sum normalization**
   (`unit_sum_channel_diff_eq`, `unit_sum_channel_degenerate_iff_equal_scalars`):
   whenever both two-channel projector pairs partition unity (`sPlus + sMinus = 1` and
   `isoPlus + isoMinus = 1`), the opposite-channel difference reduces linearly to
   `sPlus * isoMinus - sMinus * isoPlus = sPlus - isoPlus`. Over an integral domain at nonzero
   orbital weight `fEll ≠ 0`, channel degeneracy holds **if and only if** `sPlus = isoPlus` and
   `sMinus = isoMinus`. Thus the equal-scalars hypothesis is not merely sufficient; for normalized
   projector pairs it is equivalent to S-wave channel degeneracy.
2. **Reciprocal rescaling invariance and unit-sum product deficit**
   (`reciprocal_rescale_preserves_product`, `unit_sum_product_deficit_eq_sq_diff`):
   generic ring/field core of the two-channel product invariant `(μp * t) * (μm / t) = μp * μm`
   and the exact deficit identity `1 - 4 * (μp * μm) = (μp - μm) ^ 2`.
3. **Corpus isospin projector scalars and two-row `SU(2)` closed forms**
   (`isoMuPlus`, `isoMuMinus`, `isoMu_eq_h2_weights`, `isoMu_eq_h3_branching_of_radical`,
   `isoMu_disjoint_from_admissible_bond`, `isoMuPlus_twoRow_closed_form`,
   `isoMuMinus_twoRow_closed_form`, `pauliLockedProduct_twoRow_closed_form`,
   `isoMu_twoRow_product_deficit`, `isoMu_twoRow_prod_lt_quarter`):
   ties the projector scalars directly to `QOU.QBeta.InterfaceScalar` and `QOU.QBeta.GramSignature`
   and derives the exact rational closed forms at the two-row `SU(2)` Markov parameter
   `z = q ^ 3 / (q ^ 2 + 1)`:
   `μ₊(q) = (q⁴ + q² + 1) / (q² + 1)²`, `μ₋(q) = q² / (q² + 1)²`, and
   `1 - 4 μ₊(q) μ₋(q) = (q⁴ + 1)² / (q² + 1)⁴ > 0`.
4. **Spin-side `SO(3)` / `A₅` vs `2I` spinor obstruction and classical-spin mismatch**
   (`a5Irrep_no_two_dim_spinor`, `binaryIcosahedral_two_dim_spinors`, `spinor_square_dim_decomp`,
   `classicalSpin_eq_twoRowIso_iff_q_sq_eq_one`):
   `A₅ ≅ I ⊂ SO(3)` has zero 2-dimensional irreps (`dims = [1, 3, 3, 4, 5]`), whereas its binary
   icosahedral spin cover `2I ⊂ SU(2)` carries two 2-dimensional spinor irreps whose tensor square
   splits dimensionally as `1 + 3 = 4` (`A ⊕ T₁`). On that undeformed `1 ⊕ 3` decomposition, the
   normalized spin weights `(3/4, 1/4)` agree with `(μ₊(q), μ₋(q))` **if and only if** `q² = 1`,
   with exact discrepancy `(q² - 1)² / (4 (q² + 1)²)`.

Base ring (§7c): purely generic (`CommRing`, `IsDomain`, `Field`, ordered `Field`) plus discrete
`ℕ` representation dimensions — zero `ℝ` specialization.
-/

namespace QOU.Nuclear.PauliLockSpinIsospinDiagnostic

open QOU.BraidsAndKnots

section SeparableChannelAlgebra

/-- Difference of opposite-channel separable products factors through the common orbital weight. -/
theorem channel_product_diff_factor {R : Type*} [CommRing R]
    (sPlus sMinus isoPlus isoMinus fEll : R) :
    (sPlus * isoMinus * fEll) - (sMinus * isoPlus * fEll)
      = (sPlus * isoMinus - sMinus * isoPlus) * fEll := by
  ring

/-- Under unit-sum normalization on both channels (`sPlus + sMinus = 1` and
`isoPlus + isoMinus = 1`), the antisymmetrized cross-product collapses linearly to `sPlus - isoPlus`. -/
theorem unit_sum_channel_diff_eq {R : Type*} [CommRing R]
    (sPlus sMinus isoPlus isoMinus : R)
    (hs : sPlus + sMinus = 1) (hi : isoPlus + isoMinus = 1) :
    sPlus * isoMinus - sMinus * isoPlus = sPlus - isoPlus := by
  linear_combination sPlus * hi - isoPlus * hs

/-- **Converse of the equal-scalars condition under unit-sum normalization.**
Over an integral domain at nonzero S-wave orbital factor `fEll ≠ 0`, two unit-sum channel scalar
pairs produce equal S-wave separable products **if and only if** the two scalar pairs coincide
componentwise (`sPlus = isoPlus ∧ sMinus = isoMinus`). -/
theorem unit_sum_channel_degenerate_iff_equal_scalars {R : Type*} [CommRing R] [IsDomain R]
    (sPlus sMinus isoPlus isoMinus fEll : R)
    (hs : sPlus + sMinus = 1) (hi : isoPlus + isoMinus = 1) (hf : fEll ≠ 0) :
    sPlus * isoMinus * fEll = sMinus * isoPlus * fEll ↔
      (sPlus = isoPlus ∧ sMinus = isoMinus) := by
  constructor
  · intro hdeg
    have hfac : (sPlus * isoMinus - sMinus * isoPlus) * fEll = 0 := by
      linear_combination hdeg
    have hzero : sPlus * isoMinus - sMinus * isoPlus = 0 :=
      (mul_eq_zero.mp hfac).resolve_right hf
    rw [unit_sum_channel_diff_eq sPlus sMinus isoPlus isoMinus hs hi] at hzero
    have hp : sPlus = isoPlus := sub_eq_zero.mp hzero
    have hm : sMinus = isoMinus := by linear_combination hs - hi - hp
    exact ⟨hp, hm⟩
  · rintro ⟨rfl, rfl⟩
    ring

/-- Reciprocal rescaling `(μp, μm) ↦ (μp * t, μm / t)` preserves the product `μp * μm` for every
nonzero `t`. -/
theorem reciprocal_rescale_preserves_product {R : Type*} [Field R]
    (μp μm t : R) (ht : t ≠ 0) :
    (μp * t) * (μm / t) = μp * μm := by
  have h1 : (μp * t) * (μm / t) = (μp * μm) * (t / t) := by ring
  rw [h1, div_self ht, mul_one]

/-- Whenever `μp + μm = 1`, the deficit from the `1 / 4` balanced product ceiling equals the
squared channel split `(μp - μm) ^ 2` in division-free form `1 - 4 * (μp * μm) = (μp - μm) ^ 2`. -/
theorem unit_sum_product_deficit_eq_sq_diff {R : Type*} [CommRing R]
    (μp μm : R) (hsum : μp + μm = 1) :
    1 - 4 * (μp * μm) = (μp - μm) ^ 2 := by
  linear_combination (μp + μm + 1) * (-hsum)

end SeparableChannelAlgebra

section IsospinProjectorScalars

/-- The symmetric (`T = 1`) Hecke projector scalar `(z + q⁻¹) / (q + q⁻¹)` of `InterfaceScalar`. -/
def isoMuPlus {R : Type*} [Field R] (q z : R) : R :=
  (z + q⁻¹) / (q + q⁻¹)

/-- The antisymmetric (`T = 0`) Hecke projector scalar `(q - z) / (q + q⁻¹)` of `InterfaceScalar`. -/
def isoMuMinus {R : Type*} [Field R] (q z : R) : R :=
  (q - z) / (q + q⁻¹)

/-- `isoMuPlus` and `isoMuMinus` sum to `1` (`InterfaceScalar.mu_sum_eq_one`). -/
theorem isoMu_sum_eq_one {R : Type*} [Field R] (q z : R) (hs : q + q⁻¹ ≠ 0) :
    isoMuPlus q z + isoMuMinus q z = 1 :=
  QOU.QBeta.InterfaceScalar.mu_sum_eq_one q z hs

/-- **Corpus `H₂` identification**: the two-strand Wedderburn weights `(y₂, y₁₁)` determined by
`y₂ + y₁₁ = 1` and `y₂ * q + y₁₁ * (-q⁻¹) = z` coincide with `(isoMuPlus q z, isoMuMinus q z)`. -/
theorem isoMu_eq_h2_weights {R : Type*} [Field R] (q y₂ y₁₁ z : R)
    (hs : q + q⁻¹ ≠ 0)
    (hnorm : y₂ + y₁₁ = 1)
    (htr : y₂ * q + y₁₁ * (-q⁻¹) = z) :
    y₂ = isoMuPlus q z ∧ y₁₁ = isoMuMinus q z := by
  have hz := QOU.QBeta.InterfaceScalar.markov_param_determined q y₂ y₁₁ z hnorm htr
  have hy2 : y₂ = isoMuPlus q z :=
    QOU.QBeta.InterfaceScalar.weight_eq_proj_scalar q y₂ z hs hz
  have hsum := isoMu_sum_eq_one q z hs
  have hy11 : y₁₁ = isoMuMinus q z := by
    linear_combination hnorm - hsum - hy2
  exact ⟨hy2, hy11⟩

/-- **Corpus `H₃` radical-quotient identification**: when the alternating `(1,1,1)` weight vanishes
on `H₃`, `isoMuMinus q z = y₂₁` and `isoMuPlus q z = 1 - y₂₁` (`GramSignature`). -/
theorem isoMu_eq_h3_branching_of_radical {R : Type*} [Field R]
    (q z y₃ y₂₁ : R) (hs : q + q⁻¹ ≠ 0)
    (hone : y₃ + 2 * y₂₁ + 0 = 1)
    (hz : q * y₃ + (q - q⁻¹) * y₂₁ + (-q⁻¹) * 0 = z) :
    isoMuMinus q z = y₂₁ ∧ isoMuPlus q z = 1 - y₂₁ :=
  ⟨QOU.QBeta.GramSignature.mu_singlet_eq_y21_of_radical q z y₃ y₂₁ hs hone hz,
   QOU.QBeta.GramSignature.mu_triplet_eq_one_sub_y21_of_radical q z y₃ y₂₁ hs hone hz⟩

/-- **Band disjointness (`GramSignature.interface_never_equals_isospin_weight`)**: no single-bond
admissible interface scalar `z + d` (`d ∈ [-h, 0]`) equals either `isoMuMinus q z` or
`isoMuPlus q z` whenever the band-separation inequalities hold. -/
theorem isoMu_disjoint_from_admissible_bond
    {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (q z h d : R) (hs : 0 < q + q⁻¹)
    (hlo : q - z < (z - h) * (q + q⁻¹)) (hhi : z * (q + q⁻¹) < z + q⁻¹)
    (hd_lo : -h ≤ d) (hd_hi : d ≤ 0) :
    z + d ≠ isoMuMinus q z ∧ z + d ≠ isoMuPlus q z :=
  QOU.QBeta.GramSignature.interface_never_equals_isospin_weight q z h d hs hlo hhi hd_lo hd_hi

/-- Exact rational closed form of `isoMuPlus` at the two-row `SU(2)` Markov parameter
`z = q ^ 3 / (q ^ 2 + 1)`: `isoMuPlus q (q³/(q²+1)) = (q⁴ + q² + 1) / (q² + 1)²`. -/
theorem isoMuPlus_twoRow_closed_form {R : Type*} [Field R]
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    isoMuPlus q (q ^ 3 / (q ^ 2 + 1)) = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  unfold isoMuPlus
  have hs : q + q⁻¹ ≠ 0 := by
    intro h0
    apply hq2
    have hmul : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [h0, mul_zero] at hmul
    exact hmul.symm
  field_simp
  ring

/-- Exact rational closed form of `isoMuMinus` at the two-row `SU(2)` Markov parameter
`z = q ^ 3 / (q ^ 2 + 1)`: `isoMuMinus q (q³/(q²+1)) = q² / (q² + 1)²`. -/
theorem isoMuMinus_twoRow_closed_form {R : Type*} [Field R]
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    isoMuMinus q (q ^ 3 / (q ^ 2 + 1)) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  unfold isoMuMinus
  have hs : q + q⁻¹ ≠ 0 := by
    intro h0
    apply hq2
    have hmul : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [h0, mul_zero] at hmul
    exact hmul.symm
  field_simp
  ring

/-- Exact rational closed form of the Pauli-locked equal-scalar product `μ₊(q) · μ₋(q)` at
`z = q ^ 3 / (q ^ 2 + 1)`. -/
theorem pauliLockedProduct_twoRow_closed_form {R : Type*} [Field R]
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    isoMuPlus q (q ^ 3 / (q ^ 2 + 1)) * isoMuMinus q (q ^ 3 / (q ^ 2 + 1))
      = q ^ 2 * (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 4 := by
  rw [isoMuPlus_twoRow_closed_form q hq hq2, isoMuMinus_twoRow_closed_form q hq hq2]
  field_simp

/-- Exact sum-of-squares product deficit at `z = q ^ 3 / (q ^ 2 + 1)`:
`1 - 4 * (μ₊(q) * μ₋(q)) = (q⁴ + 1)² / (q² + 1)⁴`. -/
theorem isoMu_twoRow_product_deficit {R : Type*} [Field R]
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    1 - 4 * (isoMuPlus q (q ^ 3 / (q ^ 2 + 1)) * isoMuMinus q (q ^ 3 / (q ^ 2 + 1)))
      = (q ^ 4 + 1) ^ 2 / (q ^ 2 + 1) ^ 4 := by
  rw [pauliLockedProduct_twoRow_closed_form q hq hq2]
  have hden : (q ^ 2 + 1) ^ 4 ≠ 0 := pow_ne_zero 4 hq2
  field_simp
  ring

/-- Over any strict ordered field, `μ₊(q) * μ₋(q) < 1 / 4` strictly for every `q ≠ 0` at
`z = q ^ 3 / (q ^ 2 + 1)` — the balanced point `1 / 4` is never attained. -/
theorem isoMu_twoRow_prod_lt_quarter
    {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : q ≠ 0) :
    isoMuPlus q (q ^ 3 / (q ^ 2 + 1)) * isoMuMinus q (q ^ 3 / (q ^ 2 + 1)) < 1 / 4 := by
  have hq2nn : 0 ≤ q ^ 2 := sq_nonneg q
  have hden : 0 < q ^ 2 + 1 := by linarith
  have hq4nn : 0 ≤ (q ^ 2) ^ 2 := sq_nonneg (q ^ 2)
  have hq4 : 0 < q ^ 4 + 1 := by nlinarith
  have hdef := isoMu_twoRow_product_deficit q hq (ne_of_gt hden)
  have hpos : 0 < (q ^ 4 + 1) ^ 2 / (q ^ 2 + 1) ^ 4 := by positivity
  linarith

end IsospinProjectorScalars

section SpinFiberObstruction

/-- **Representation-dimension obstruction on `BringFiberAction`'s domain (`A5Irrep`)**:
none of the five irreducible representations of `A₅ ≅ I ⊂ SO(3)` (`dims = [1, 3, 3, 4, 5]`) is
2-dimensional, so `A5Irrep` hosts no fundamental spin-`1/2` doublet without passing to the binary
icosahedral double cover `2I ⊂ SU(2)`. -/
theorem a5Irrep_no_two_dim_spinor :
    (∀ r : A5Irrep, r.dim ≠ 2) ∧ IcosahedralIrrepDims.count 2 = 0 := by
  refine ⟨?_, by decide⟩
  intro r
  cases r <;> decide

/-- **Spinor irreps live in the binary icosahedral cover `2I ⊂ SU(2)`**:
`binaryIcosahedralIrrepDims` contains exactly two 2-dimensional spinor irreps, and the spinorial
complement of `IcosahedralIrrepDims` inside `2I` accounts for `120 - 60 = 60` of Burnside `Σ dim²`. -/
theorem binaryIcosahedral_two_dim_spinors :
    binaryIcosahedralIrrepDims.count 2 = 2 ∧
    (binaryIcosahedralIrrepDims.map (· ^ 2)).sum - (IcosahedralIrrepDims.map (· ^ 2)).sum = 60 := by
  decide

/-- The tensor square of a 2-dimensional `2I` spinor decomposes dimensionally into the trivial
singlet `A` (`dim = 1`, `S = 0`) plus the vector triplet `T₁` (`dim = 3`, `S = 1`): `1 + 3 = 2²`. -/
theorem spinor_square_dim_decomp :
    A5Irrep.A.dim + A5Irrep.T₁.dim = 2 ^ 2 ∧
    A5Irrep.A.dim = 1 ∧ A5Irrep.T₁.dim = 3 := by
  decide

/-- Exact discrepancy between `isoMuPlus` at `z = q ^ 3 / (q ^ 2 + 1)` and the undeformed
spin-triplet trace share `3 / 4` on `1 ⊕ 3`: `(q² - 1)² / (4 (q² + 1)²)`. -/
theorem classicalSpin_vs_twoRowIso_plus_diff {R : Type*} [Field R] [CharZero R]
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    isoMuPlus q (q ^ 3 / (q ^ 2 + 1)) - 3 / 4
      = (q ^ 2 - 1) ^ 2 / (4 * (q ^ 2 + 1) ^ 2) := by
  rw [isoMuPlus_twoRow_closed_form q hq hq2]
  have h4 : (4 : R) ≠ 0 := by norm_num
  have hden : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp
  ring

/-- Exact discrepancy between the undeformed spin-singlet trace share `1 / 4` on `1 ⊕ 3` and
`isoMuMinus` at `z = q ^ 3 / (q ^ 2 + 1)`: `(q² - 1)² / (4 (q² + 1)²)`. -/
theorem classicalSpin_vs_twoRowIso_minus_diff {R : Type*} [Field R] [CharZero R]
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    1 / 4 - isoMuMinus q (q ^ 3 / (q ^ 2 + 1))
      = (q ^ 2 - 1) ^ 2 / (4 * (q ^ 2 + 1) ^ 2) := by
  rw [isoMuMinus_twoRow_closed_form q hq hq2]
  have h4 : (4 : R) ≠ 0 := by norm_num
  have hden : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp
  ring

/-- **Undeformed spin `(3/4, 1/4)` equals `q`-deformed two-row isospin `(μ₊(q), μ₋(q))` iff `q² = 1`.**
Away from the classical limit `q² = 1`, an undeformed `SO(3)` / `2I` spin projector pair cannot
satisfy the Pauli-lock equal-scalars hypothesis against `isoMuPlus` / `isoMuMinus`: by
`unit_sum_channel_degenerate_iff_equal_scalars`, matching them at `q² ≠ 1` requires a genuinely
`q`-deformed spin projector construction not present in `BringFiberAction` or `SpinFromSo3Fiber`. -/
theorem classicalSpin_eq_twoRowIso_iff_q_sq_eq_one {R : Type*} [Field R] [CharZero R]
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    (isoMuPlus q (q ^ 3 / (q ^ 2 + 1)) = 3 / 4 ∧
      isoMuMinus q (q ^ 3 / (q ^ 2 + 1)) = 1 / 4) ↔ q ^ 2 = 1 := by
  constructor
  · rintro ⟨hp, _⟩
    have hdiff := classicalSpin_vs_twoRowIso_plus_diff q hq hq2
    rw [hp, sub_self] at hdiff
    have h4 : (4 : R) * (q ^ 2 + 1) ^ 2 ≠ 0 :=
      mul_ne_zero (by norm_num) (pow_ne_zero 2 hq2)
    have hsq : (q ^ 2 - 1) ^ 2 = 0 :=
      (div_eq_zero_iff.mp hdiff.symm).resolve_right h4
    exact sub_eq_zero.mp (pow_eq_zero hsq)
  · intro hq1
    have hzero : (q ^ 2 - 1) ^ 2 / (4 * (q ^ 2 + 1) ^ 2) = 0 := by
      rw [hq1]; norm_num
    have hp := (classicalSpin_vs_twoRowIso_plus_diff q hq hq2).trans hzero
    have hm := (classicalSpin_vs_twoRowIso_minus_diff q hq hq2).trans hzero
    exact ⟨sub_eq_zero.mp hp, (sub_eq_zero.mp hm).symm⟩

end SpinFiberObstruction

end QOU.Nuclear.PauliLockSpinIsospinDiagnostic
