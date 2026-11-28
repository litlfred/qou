/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import QOU.Nuclear.C1DeterminantRelation
import QOU.Nuclear.C1RamifiedLeadingBlocks
import QOU.Transcendental.MathlibExt.QGevreyOrder

set_option autoImplicit false

/-!
# Algebraic C1 Connection, Casoratian, Singular-Locus, and Bound-Form q-Gevrey Identities

Beans `qou-c1ln` (algebraic layer of rows 4 & 6), `qou-wgnx`, `qou-qbe9x`, and `qou-slvl` (item 1).

Several structural identities in the C1 connection and singular-locus scripts
(`computations/qbeta/c3_w2_c1_connection_matrix.py`,
`computations/qbeta/c3_w2_c1_connection_invariant.py`,
`computations/qbeta/c3_w2_c1_invariant_structure.py`,
`computations/qbeta/c3_w2_c1_theta_canonical.py`) were previously verified only numerically
(`1e-110` to `1e-167`), even though their cores are exact algebra over generic commutative rings
or fields (§7c). This module discharges those algebraic and bound-form results with `0 sorry` and
`0` custom axioms while keeping the genuinely analytic meromorphy/JTP questions (`qou-c1ln`
analytic half of rows 4 & 6) explicitly scoped out:

1. **§1 Casoratian Outward Propagation Law (`qou-c1ln`, `qou-wgnx`):**
   For any two solutions `y₁, y₂` of the ramified C1 recurrence
   `(p⁴ z² - 1) y(p² z) = (p² - 1) y(p z) + (p² - 1) y(z)`, their Casoratian
   `W(z) = y₁(z) y₂(p z) - y₂(z) y₁(p z)` obeys `(p⁴ z² - 1) W(p z) = -(p² - 1) W(z)` over any
   `[CommRing R]` (`casoratian_step_cleared`) and its `N`-step product form
   `casoratian_iterated_cleared`, proving analytically why `W(p^N z)` decays under outward
   propagation without rank collapse (`c3_w2_c1_connection_matrix.py` §2).

2. **§2 Automatic `p`-Ellipticity & `[−1]` Rebasing Cancellation (`qou-c1ln` row 4 algebraic half):**
   For any two invertible fundamental matrices `Y₀, Y_∞` of the same companion system
   `Y(p z) = A(z) Y(z)`, `P(z) = Y₀(z)⁻¹ Y_∞(z)` satisfies `P(p z) = P(z)` identically
   (`connectionMatrix_elliptic_units`, `connectionMatrix2_elliptic`), and common row/column
   rebasing factors cancel out of `χ = P₀₀ P₁₁ / (P₀₁ P₁₀)` (`chi_rebasing_invariant`).

3. **§3 Conjugate-Row Structure, Reflection Law `χ(z̄) = 1 / conj(χ(z))`, & Real-Axis Unit Modulus
   (`qou-c1ln` row 6, `qou-wgnx`):**
   Over `[Field K]` with an involutive ring endomorphism `σ : K →+* K`, column-swap conjugation
   `Y₀(σ z) = Y₀(z)^σ · J` against `σ`-real `Y_∞(σ z) = Y_∞(z)^σ` forces `P(σ z) = J · P(z)^σ`
   (`connectionMatrix2_conj_row_swap`), `P = [[c₊, c₋], [conj c₊, conj c₋]]` on the `σ`-fixed
   locus, `χ(σ z) · σ(χ(z)) = 1` (`chi_reflection_law`), and `‖χ(x)‖ = 1` on `ℝ` (`norm_chi_real`).

4. **§4 Canonical Sector Parameter `T_θ` vs `T_edge` & Divisor Modulus `|α| = |t₂/T_θ| = q^{3/4}`
   (`qou-c1ln` row 6, `qou-wgnx`):**
   Relates `p³ T_θ² = p² - 1` (`C1Ramified.edge_eq_iff`) and `p⁴ T_edge² = p² - 1` via
   `(T_θ / T_edge)⁴ = q`, proves `(α₁ α₂)² = q³` over any `[Field K]` from `C1ZeroSide.vieta`,
   and derives `‖t₂ / T_θ‖ = q ^ (3 / 4 : ℝ)` over `ℂ`.

5. **§5 Third Singular Site `x = q⁻²` Gauge-Invariant Torus Degree `−1` (`qou-qbe9x`):**
   Proves that the `Kˣ` divisor degree `natDegree P - natTrailingDegree P` is invariant under
   `q`-dilation `X ↦ q X`, so every rational gauge coboundary `g(q x) / g(x)` has torus degree `0`,
   whereas C1's companion determinant `detA q x = -(q - 1)/(q² x - 1)` has torus degree `-1 ≠ 0`
   and cannot be removed by any rational gauge transformation.

6. **§6 RSZ §1.3.2 Bound-Form `IsQGevreyOrderLE` & Full Lacunary `L_k` Order (`qou-slvl` item 1):**
   Defines `IsQGevreyOrderLE q s a`, proves `IsQGevreyOrder q s a → ∀ ε > 0, IsQGevreyOrderLE q (s + ε) a`,
   refutes the unshifted `ε = 0` implication via `a_n = 2^{n √n}`, and proves that the full
   lacunary sequence of `L_k = z^k σ - 1` (zeros included, no subsequence restriction) has sharp
   bound-form order `1 / k` (hence q-Gevrey level `k`).

-- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §1.3.2, §2.2, §3.3, §5.5 (Ramis–Sauloy–Zhang)
-- Ref: [leitner2026] computations/qbeta/c3_w2_c1_connection_matrix.py
-- Ref: [leitner2026] computations/qbeta/c3_w2_c1_invariant_structure.py
-- Ref: [leitner2026] computations/qbeta/c3_w2_c1_theta_canonical.py
-/

namespace QOU.QBeta.C1ConnectionAlgebra

open scoped BigOperators Matrix Polynomial
open Polynomial Matrix Filter Topology

/-! ## §1. Companion System & Casoratian Outward Propagation Law (`qou-c1ln`, `qou-wgnx`) -/

section Casoratian

/-- Fundamental `2 × 2` Casoratian matrix `[[y₁(z), y₂(z)], [y₁(p z), y₂(p z)]]` of two functions
under the ramified shift `z ↦ p z`. -/
def fundMat2 {R : Type*} [CommRing R] (y₁ y₂ : R → R) (p z : R) : Matrix (Fin 2) (Fin 2) R :=
  !![y₁ z, y₂ z; y₁ (p * z), y₂ (p * z)]

/-- Scalar Casoratian determinant `W(z) = y₁(z) y₂(p z) - y₂(z) y₁(p z)`. -/
def casoratian {R : Type*} [CommRing R] (y₁ y₂ : R → R) (p z : R) : R :=
  y₁ z * y₂ (p * z) - y₂ z * y₁ (p * z)

/-- `det (fundMat2 y₁ y₂ p z) = casoratian y₁ y₂ p z`. -/
theorem det_fundMat2 {R : Type*} [CommRing R] (y₁ y₂ : R → R) (p z : R) :
    (fundMat2 y₁ y₂ p z).det = casoratian y₁ y₂ p z := by
  simp [fundMat2, casoratian, Matrix.det_fin_two_of]

/-- Ramified C1 recurrence predicate at `(p, z)`:
`(p⁴ z² - 1) y(p² z) = (p² - 1) y(p z) + (p² - 1) y(z)`. -/
def SatisfiesRamifiedC1At {R : Type*} [CommRing R] (p : R) (y : R → R) (z : R) : Prop :=
  (p ^ 4 * z ^ 2 - 1) * y (p * (p * z)) = (p ^ 2 - 1) * y (p * z) + (p ^ 2 - 1) * y z

/-- **Division-free Casoratian step (`c3_w2_c1_connection_matrix.py` §2):**
Over any `[CommRing R]`, if `y₁` and `y₂` satisfy the ramified C1 recurrence at `z`, then
`(p⁴ z² - 1) W(p z) = -(p² - 1) W(z)` (with `q = p²`, `-(q - 1) W(z)`). -/
theorem casoratian_step_cleared {R : Type*} [CommRing R] {p z : R} {y₁ y₂ : R → R}
    (hy₁ : SatisfiesRamifiedC1At p y₁ z) (hy₂ : SatisfiesRamifiedC1At p y₂ z) :
    (p ^ 4 * z ^ 2 - 1) * casoratian y₁ y₂ p (p * z) = -(p ^ 2 - 1) * casoratian y₁ y₂ p z := by
  unfold casoratian
  unfold SatisfiesRamifiedC1At at hy₁ hy₂
  linear_combination y₁ (p * z) * hy₂ - y₂ (p * z) * hy₁

/-- **Iterated `N`-step outward Casoratian propagation over `[CommRing R]`:**
If `y₁, y₂` satisfy the ramified C1 recurrence along the orbit `p^k z` (`k < N`), then
`(∏_{k < N} (p⁴ (p^k z)² - 1)) · W(p^N z) = (-(p² - 1))^N · W(z)`. -/
theorem casoratian_iterated_cleared {R : Type*} [CommRing R] (p z : R) (y₁ y₂ : R → R) (N : ℕ)
    (horb : ∀ k < N, SatisfiesRamifiedC1At p y₁ (p ^ k * z) ∧
      SatisfiesRamifiedC1At p y₂ (p ^ k * z)) :
    (∏ k ∈ Finset.range N, (p ^ 4 * (p ^ k * z) ^ 2 - 1)) *
        casoratian y₁ y₂ p (p ^ N * z) =
      (-(p ^ 2 - 1)) ^ N * casoratian y₁ y₂ p z := by
  induction N with
  | zero =>
    simp
  | succ n ih =>
    have hprev : ∀ k < n, SatisfiesRamifiedC1At p y₁ (p ^ k * z) ∧
        SatisfiesRamifiedC1At p y₂ (p ^ k * z) :=
      fun k hk => horb k (Nat.lt_succ_of_lt hk)
    obtain ⟨h1n, h2n⟩ := horb n (Nat.lt_succ_self n)
    have hstep := casoratian_step_cleared h1n h2n
    have hp_pow : p * (p ^ n * z) = p ^ (n + 1) * z := by
      rw [pow_succ', mul_assoc]
    rw [hp_pow] at hstep
    rw [Finset.prod_range_succ]
    calc
      ((∏ k ∈ Finset.range n, (p ^ 4 * (p ^ k * z) ^ 2 - 1)) *
          (p ^ 4 * (p ^ n * z) ^ 2 - 1)) * casoratian y₁ y₂ p (p ^ (n + 1) * z)
          = (∏ k ∈ Finset.range n, (p ^ 4 * (p ^ k * z) ^ 2 - 1)) *
              ((p ^ 4 * (p ^ n * z) ^ 2 - 1) * casoratian y₁ y₂ p (p ^ (n + 1) * z)) := by ring
      _ = (∏ k ∈ Finset.range n, (p ^ 4 * (p ^ k * z) ^ 2 - 1)) *
            (-(p ^ 2 - 1) * casoratian y₁ y₂ p (p ^ n * z)) := by rw [hstep]
      _ = -(p ^ 2 - 1) *
            ((∏ k ∈ Finset.range n, (p ^ 4 * (p ^ k * z) ^ 2 - 1)) *
              casoratian y₁ y₂ p (p ^ n * z)) := by ring
      _ = -(p ^ 2 - 1) * ((-(p ^ 2 - 1)) ^ n * casoratian y₁ y₂ p z) := by rw [ih hprev]
      _ = (-(p ^ 2 - 1)) ^ (n + 1) * casoratian y₁ y₂ p z := by rw [pow_succ']; ring

/-- **Rational Casoratian propagation over `[Field K]`:**
Off the singular orbit `p⁴ z² ≠ 1`, `W(p z) = -(p² - 1) W(z) / (p⁴ z² - 1)`. -/
theorem casoratian_step_div {K : Type*} [Field K] {p z : K} {y₁ y₂ : K → K}
    (hy₁ : SatisfiesRamifiedC1At p y₁ z) (hy₂ : SatisfiesRamifiedC1At p y₂ z)
    (hden : p ^ 4 * z ^ 2 - 1 ≠ 0) :
    casoratian y₁ y₂ p (p * z) = -(p ^ 2 - 1) * casoratian y₁ y₂ p z / (p ^ 4 * z ^ 2 - 1) := by
  rw [eq_div_iff hden, mul_comm]
  exact casoratian_step_cleared hy₁ hy₂

/-- Companion matrix `A_ram(p, z) = [[0, 1], [(p²-1)/(p⁴z²-1), (p²-1)/(p⁴z²-1)]]` of the
ramified C1 operator over `[Field K]`, with determinant `-(p² - 1)/(p⁴ z² - 1)`. -/
noncomputable def ramifiedCompanion {K : Type*} [Field K] (p z : K) : Matrix (Fin 2) (Fin 2) K :=
  let a := (p ^ 2 - 1) / (p ^ 4 * z ^ 2 - 1)
  !![0, 1; a, a]

theorem det_ramifiedCompanion {K : Type*} [Field K] (p z : K) :
    (ramifiedCompanion p z).det = -(p ^ 2 - 1) / (p ^ 4 * z ^ 2 - 1) := by
  simp only [ramifiedCompanion, Matrix.det_fin_two_of]
  ring

end Casoratian

/-! ## §2. Automatic `p`-Ellipticity of `P = Y₀⁻¹ Y_∞` & Rebasing Cancellation (`qou-c1ln` row 4) -/

section ConnectionEllipticity

/-- **General matrix-unit `p`-ellipticity (`c3_w2_c1_connection_matrix.py` §4):**
Over any `[CommRing R]`, if two invertible fundamental matrix families `Y₀, Y_∞ : S → (Matrix n n R)ˣ`
satisfy the same `q`-difference system `Y₀(τ z) = A(z) * Y₀(z)` and `Y_∞(τ z) = A(z) * Y_∞(z)`
for a unit matrix `A(z)`, then `P(z) = Y₀(z)⁻¹ * Y_∞(z)` satisfies `P(τ z) = P(z)` identically. -/
theorem connectionMatrix_elliptic_units {R S n : Type*} [CommRing R] [Fintype n] [DecidableEq n]
    (τ : S → S) (A Y₀ Y_inf : S → (Matrix n n R)ˣ)
    (h0 : ∀ z, Y₀ (τ z) = A z * Y₀ z)
    (hinf : ∀ z, Y_inf (τ z) = A z * Y_inf z) (z : S) :
    (Y₀ (τ z))⁻¹ * Y_inf (τ z) = (Y₀ z)⁻¹ * Y_inf z := by
  rw [h0 z, hinf z, _root_.mul_inv_rev, mul_assoc, inv_mul_cancel_left]

/-- **Nonsingular-inverse `p`-ellipticity for `2 × 2` matrices over `[Field K]`:**
If `Y₀(p z) = A(z) * Y₀(z)` and `Y_∞(p z) = A(z) * Y_∞(z)` with `det A(z) ≠ 0`, then
`(Y₀ (p * z))⁻¹ * Y_∞ (p * z) = (Y₀ z)⁻¹ * Y_∞ z`. -/
theorem connectionMatrix2_elliptic {K : Type*} [Field K]
    (p z : K) (A Y₀ Y_inf : K → Matrix (Fin 2) (Fin 2) K)
    (h0 : Y₀ (p * z) = A z * Y₀ z)
    (hinf : Y_inf (p * z) = A z * Y_inf z)
    (hA : IsUnit (A z).det) :
    (Y₀ (p * z))⁻¹ * Y_inf (p * z) = (Y₀ z)⁻¹ * Y_inf z := by
  rw [h0, hinf, Matrix.mul_inv_rev]
  calc
    (Y₀ z)⁻¹ * (A z)⁻¹ * (A z * Y_inf z)
        = (Y₀ z)⁻¹ * ((A z)⁻¹ * A z) * Y_inf z := by simp only [Matrix.mul_assoc]
    _ = (Y₀ z)⁻¹ * 1 * Y_inf z := by rw [Matrix.nonsing_inv_mul _ hA]
    _ = (Y₀ z)⁻¹ * Y_inf z := by simp

/-- **Casoratian ratio `p`-ellipticity (`det P(p z) = det P(z)`):**
Because both fundamental Casoratians multiply by the same factor `-(p² - 1)/(p⁴ z² - 1)`, their
ratio `W_∞ / W₀ = det P` is `p`-periodic off the singular locus without inverting matrices. -/
theorem casoratian_ratio_elliptic {K : Type*} [Field K] {p z : K}
    {y₀₁ y₀₂ yᵢ₁ yᵢ₂ : K → K}
    (h01 : SatisfiesRamifiedC1At p y₀₁ z) (h02 : SatisfiesRamifiedC1At p y₀₂ z)
    (hi1 : SatisfiesRamifiedC1At p yᵢ₁ z) (hi2 : SatisfiesRamifiedC1At p yᵢ₂ z)
    (hden : p ^ 4 * z ^ 2 - 1 ≠ 0) (hp2 : p ^ 2 - 1 ≠ 0)
    (hW0 : casoratian y₀₁ y₀₂ p z ≠ 0) :
    casoratian yᵢ₁ yᵢ₂ p (p * z) / casoratian y₀₁ y₀₂ p (p * z) =
      casoratian yᵢ₁ yᵢ₂ p z / casoratian y₀₁ y₀₂ p z := by
  rw [casoratian_step_div hi1 hi2 hden, casoratian_step_div h01 h02 hden]
  have hm : -(p ^ 2 - 1) ≠ 0 := neg_ne_zero.mpr hp2
  field_simp

/-- Connection cross-ratio `χ(P) = P₀₀ P₁₁ / (P₀₁ P₁₀)` (`C1ConnectionPoles` convention). -/
noncomputable def connChi {K : Type*} [Field K] (P : Matrix (Fin 2) (Fin 2) K) : K :=
  (P 0 0 * P 1 1) / (P 0 1 * P 1 0)

/-- **`[−1]` Rebasing & Canonical Scaling Invariance (`c3_w2_c1_connection_invariant.py` §3):**
Scaling `P`'s rows by `(r₀, r₁)` (which captures changing the `0`-side character `e_t(z)` by any
common factor or rebasing `c`) and scaling `P`'s columns by `(s₀, s₁)` leaves `connChi` strictly
unchanged. -/
theorem chi_rebasing_invariant {K : Type*} [Field K]
    (P : Matrix (Fin 2) (Fin 2) K) (r₀ r₁ s₀ s₁ : K)
    (hr₀ : r₀ ≠ 0) (hr₁ : r₁ ≠ 0) (hs₀ : s₀ ≠ 0) (hs₁ : s₁ ≠ 0) :
    connChi !![r₀ * P 0 0 * s₀, r₀ * P 0 1 * s₁; r₁ * P 1 0 * s₀, r₁ * P 1 1 * s₁] =
      connChi P := by
  unfold connChi
  simp only [Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  field_simp

end ConnectionEllipticity

/-! ## §3. Conjugate-Row Structure, Reflection Law, & Real-Axis Unit Modulus (`qou-wgnx`) -/

section ReflectionAndUnitModulus

/-- Permutation matrix `J = [[0, 1], [1, 0]]` swapping the two conjugate `0`-side basis columns. -/
def swapMat2 (R : Type*) [CommRing R] : Matrix (Fin 2) (Fin 2) R :=
  !![0, 1; 1, 0]

theorem swapMat2_mul_self (R : Type*) [CommRing R] :
    swapMat2 R * swapMat2 R = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [swapMat2]

theorem det_swapMat2 (R : Type*) [CommRing R] :
    (swapMat2 R).det = -1 := by
  simp [swapMat2, Matrix.det_fin_two_of]

/-- Entrywise action of a ring endomorphism `σ` on a `2 × 2` matrix (`M.map σ`). -/
def mapMat {R S : Type*} [Semiring R] [Semiring S] (σ : R →+* S)
    (M : Matrix (Fin 2) (Fin 2) R) : Matrix (Fin 2) (Fin 2) S :=
  M.map σ

theorem mapMat_mul {R S : Type*} [CommRing R] [CommRing S] (σ : R →+* S)
    (A B : Matrix (Fin 2) (Fin 2) R) :
    mapMat σ (A * B) = mapMat σ A * mapMat σ B := by
  simp [mapMat]

theorem mapMat_one {R S : Type*} [CommRing R] [CommRing S] (σ : R →+* S) :
    mapMat σ (1 : Matrix (Fin 2) (Fin 2) R) = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [mapMat]

private lemma ringHom_ne_zero {K : Type*} [Field K] (σ : K →+* K) {x : K} (hx : x ≠ 0) :
    σ x ≠ 0 := by
  intro h0
  have h1 : σ (x * x⁻¹) = σ 1 := by rw [mul_inv_cancel₀ hx]
  rw [map_mul, h0, zero_mul, map_one] at h1
  exact zero_ne_one h1

/-- **Row-swap conjugation law for `P = Y₀⁻¹ Y_∞` (`c3_w2_c1_connection_matrix.py` §4):**
Over `[Field K]` with a ring endomorphism `σ : K →+* K`, if `Y₀(σ z) = mapMat σ (Y₀ z) * J`
(conjugating `z` swaps the two conjugate `0`-side solutions) and `Y_∞(σ z) = mapMat σ (Y_∞ z)`
(the `∞`-side canonical solutions have `σ`-fixed real coefficients), then for invertible `Y₀ z`,
`P(σ z) = J * mapMat σ (P z)`. -/
theorem connectionMatrix2_conj_row_swap {K : Type*} [Field K] (σ : K →+* K)
    {Y₀z Y₀σ Yᵢz Yᵢσ : Matrix (Fin 2) (Fin 2) K}
    (hY₀ : Y₀σ = mapMat σ Y₀z * swapMat2 K)
    (hYᵢ : Yᵢσ = mapMat σ Yᵢz)
    (hdet : Y₀z.det ≠ 0) :
    Y₀σ⁻¹ * Yᵢσ = swapMat2 K * mapMat σ (Y₀z⁻¹ * Yᵢz) := by
  have hu : IsUnit Y₀z.det := Ne.isUnit hdet
  have hmul1 : Y₀z * Y₀z⁻¹ = 1 := Matrix.mul_nonsing_inv Y₀z hu
  have hmap1 : mapMat σ Y₀z * mapMat σ (Y₀z⁻¹) = 1 := by
    rw [← mapMat_mul, hmul1, mapMat_one]
  have hY₀σ_mul : Y₀σ * (swapMat2 K * mapMat σ (Y₀z⁻¹)) = 1 := by
    calc
      Y₀σ * (swapMat2 K * mapMat σ (Y₀z⁻¹))
          = mapMat σ Y₀z * (swapMat2 K * swapMat2 K) * mapMat σ (Y₀z⁻¹) := by
            rw [hY₀]; simp only [Matrix.mul_assoc]
      _ = mapMat σ Y₀z * mapMat σ (Y₀z⁻¹) := by rw [swapMat2_mul_self, Matrix.mul_one]
      _ = 1 := hmap1
  have hdet_map : (mapMat σ Y₀z).det = σ Y₀z.det := by
    simp [mapMat, Matrix.det_fin_two]
  have hdetσ : Y₀σ.det ≠ 0 := by
    rw [hY₀, Matrix.det_mul, hdet_map, det_swapMat2, mul_neg, mul_one, neg_ne_zero]
    exact ringHom_ne_zero σ hdet
  have hinv_eq : Y₀σ⁻¹ = swapMat2 K * mapMat σ (Y₀z⁻¹) := by
    calc
      Y₀σ⁻¹ = Y₀σ⁻¹ * 1 := (Matrix.mul_one _).symm
      _ = Y₀σ⁻¹ * (Y₀σ * (swapMat2 K * mapMat σ (Y₀z⁻¹))) := by rw [hY₀σ_mul]
      _ = (Y₀σ⁻¹ * Y₀σ) * (swapMat2 K * mapMat σ (Y₀z⁻¹)) := by simp only [Matrix.mul_assoc]
      _ = 1 * (swapMat2 K * mapMat σ (Y₀z⁻¹)) := by
          rw [Matrix.nonsing_inv_mul _ (Ne.isUnit hdetσ)]
      _ = swapMat2 K * mapMat σ (Y₀z⁻¹) := Matrix.one_mul _
  rw [hinv_eq, hYᵢ, mapMat_mul, Matrix.mul_assoc]

/-- **Conjugate-row structure on the `σ`-fixed real axis (`P = [[c₊, c₋], [σ c₊, σ c₋]]`):**
Whenever `P = swapMat2 K * mapMat σ P` (i.e. `z` lies on the `σ`-fixed real locus), the bottom row
of `P` is the entrywise `σ`-image of its top row. -/
theorem connectionMatrix2_fixed_locus_rows {K : Type*} [Field K] (σ : K →+* K)
    {P : Matrix (Fin 2) (Fin 2) K} (hP : P = swapMat2 K * mapMat σ P) :
    P 1 0 = σ (P 0 0) ∧ P 1 1 = σ (P 0 1) := by
  have h10 := congrArg (fun M => M 1 0) hP
  have h11 := congrArg (fun M => M 1 1) hP
  simp only [swapMat2, mapMat, Matrix.mul_apply, Fin.sum_univ_two, Matrix.map_apply,
    Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one, one_mul, zero_mul, add_zero]
    at h10 h11
  exact ⟨h10, h11⟩

/-- **Exact Reflection Law `χ(σ z) · σ(χ(z)) = 1` (`c3_w2_c1_invariant_structure.py` §2):**
Previously verified numerically to `1e-167`. Whenever `Pσ = J * mapMat σ P` with nonzero entries,
`connChi Pσ = (σ (connChi P))⁻¹` and `connChi Pσ * σ (connChi P) = 1`. -/
theorem chi_reflection_law {K : Type*} [Field K] (σ : K →+* K)
    {P Pσ : Matrix (Fin 2) (Fin 2) K}
    (hswap : Pσ = swapMat2 K * mapMat σ P)
    (h00 : P 0 0 ≠ 0) (h01 : P 0 1 ≠ 0) (h10 : P 1 0 ≠ 0) (h11 : P 1 1 ≠ 0) :
    connChi Pσ = (σ (connChi P))⁻¹ ∧ connChi Pσ * σ (connChi P) = 1 := by
  have e00 : Pσ 0 0 = σ (P 1 0) := by
    rw [hswap]; simp [swapMat2, mapMat, Matrix.mul_apply, Fin.sum_univ_two]
  have e01 : Pσ 0 1 = σ (P 1 1) := by
    rw [hswap]; simp [swapMat2, mapMat, Matrix.mul_apply, Fin.sum_univ_two]
  have e10 : Pσ 1 0 = σ (P 0 0) := by
    rw [hswap]; simp [swapMat2, mapMat, Matrix.mul_apply, Fin.sum_univ_two]
  have e11 : Pσ 1 1 = σ (P 0 1) := by
    rw [hswap]; simp [swapMat2, mapMat, Matrix.mul_apply, Fin.sum_univ_two]
  have hs00 : σ (P 0 0) ≠ 0 := ringHom_ne_zero σ h00
  have hs01 : σ (P 0 1) ≠ 0 := ringHom_ne_zero σ h01
  have hs10 : σ (P 1 0) ≠ 0 := ringHom_ne_zero σ h10
  have hs11 : σ (P 1 1) ≠ 0 := ringHom_ne_zero σ h11
  have hinv : connChi Pσ = (σ (connChi P))⁻¹ := by
    unfold connChi
    rw [e00, e01, e10, e11, map_div₀, map_mul, map_mul, inv_div]
    ring
  refine ⟨hinv, ?_⟩
  rw [hinv, inv_mul_cancel₀]
  unfold connChi
  rw [map_div₀, map_mul, map_mul]
  exact div_ne_zero (mul_ne_zero hs00 hs11) (mul_ne_zero hs01 hs10)

/-- **Automatic Unit Modulus on `ℝ` (`|χ(x)| = 1`, `c3_w2_c1_invariant_structure.py` §2):**
For `K = ℂ` with `σ = starRingEnd ℂ`, any connection matrix `P` at a real point (`P = J * P̄`)
with nonzero entries has `‖connChi P‖ = 1` identically. -/
theorem norm_chi_real {P : Matrix (Fin 2) (Fin 2) ℂ}
    (hP : P = swapMat2 ℂ * mapMat (starRingEnd ℂ) P)
    (h00 : P 0 0 ≠ 0) (h01 : P 0 1 ≠ 0) (h10 : P 1 0 ≠ 0) (h11 : P 1 1 ≠ 0) :
    ‖connChi P‖ = 1 := by
  have hprod := (chi_reflection_law (starRingEnd ℂ) hP h00 h01 h10 h11).2
  have hn := congrArg Norm.norm hprod
  rw [norm_mul, Complex.norm_conj, norm_one] at hn
  have hnn : 0 ≤ ‖connChi P‖ := norm_nonneg _
  nlinarith

end ReflectionAndUnitModulus

/-! ## §4. Canonical Parameter `T_θ` vs `T_edge` & Divisor Modulus `|α| = q^{3/4}` (`qou-wgnx`) -/

section CanonicalParameterAndDivisorModulus

/-- **Algebraic `q^{1/4}` separation between `T_θ` and `T_edge` (`c3_w2_c1_theta_canonical.py` §1):**
Over any `[Field K]`, if `T_θ` solves the twisted canonical indicial equation `p³ T_θ² = p² - 1`
(`C1Ramified.edge_eq_iff`) and `T_edge` solves the untwisted Newton-edge equation
`p⁴ T_edge² = p² - 1` (`p ≠ 0`, `p² ≠ 1`), then `T_θ² / T_edge² = p` and `(T_θ / T_edge)⁴ = q`
for `q = p²`. -/
theorem canonical_vs_edge_sq_ratio {K : Type*} [Field K] {p q T_theta T_edge : K}
    (hp : p ≠ 0) (hp2 : p ^ 2 - 1 ≠ 0) (hq : q = p ^ 2)
    (htheta : p ^ 3 * T_theta ^ 2 = p ^ 2 - 1)
    (hedge : p ^ 4 * T_edge ^ 2 = p ^ 2 - 1) :
    T_theta ^ 2 / T_edge ^ 2 = p ∧ (T_theta / T_edge) ^ 4 = q := by
  have hTe2 : T_edge ^ 2 ≠ 0 := by
    intro h0
    rw [h0, mul_zero] at hedge
    exact hp2 hedge.symm
  have hrel : p ^ 3 * T_theta ^ 2 = p ^ 4 * T_edge ^ 2 := by rw [htheta, hedge]
  have hsq : T_theta ^ 2 = p * T_edge ^ 2 := by
    apply mul_left_cancel₀ (pow_ne_zero 3 hp)
    calc
      p ^ 3 * T_theta ^ 2 = p ^ 4 * T_edge ^ 2 := hrel
      _ = p ^ 3 * (p * T_edge ^ 2) := by ring
  have hdiv : T_theta ^ 2 / T_edge ^ 2 = p := by
    rw [hsq, mul_div_cancel_right₀ _ hTe2]
  refine ⟨hdiv, ?_⟩
  calc
    (T_theta / T_edge) ^ 4 = (T_theta ^ 2 / T_edge ^ 2) ^ 2 := by ring
    _ = p ^ 2 := by rw [hdiv]
    _ = q := hq.symm

/-- **Algebraic Connection Divisor Product (`(α₁ α₂)² = q³`, `qou-wgnx` 16th–17th entries):**
Over any `[Field K]`, if `(t₁, t₂)` are the `0`-side Fuchsian roots (`zeroSideIndicial q t =
(t - t₁)(t - t₂)`) and `T_θ` satisfies `p³ T_θ² = p² - 1` with `q = p²` (`p ≠ 0`, `p² ≠ 1`),
then the connection divisor ratios `α_j = t_j / T_θ` satisfy `α₁ α₂ = p³` and `(α₁ α₂)² = q³`. -/
theorem connDivisor_product_sq_eq_q_cubed {K : Type*} [Field K] {p q t₁ t₂ T_theta : K}
    (hq : q = p ^ 2) (hp2 : p ^ 2 - 1 ≠ 0)
    (hfac : ∀ t : K, C1ZeroSide.zeroSideIndicial q t = (t - t₁) * (t - t₂))
    (htheta : p ^ 3 * T_theta ^ 2 = p ^ 2 - 1) :
    (t₁ / T_theta) * (t₂ / T_theta) = p ^ 3 ∧
      ((t₁ / T_theta) * (t₂ / T_theta)) ^ 2 = q ^ 3 := by
  have hprod : t₁ * t₂ = q - 1 := ((C1ZeroSide.vieta q t₁ t₂).mp hfac).2
  have hT2 : T_theta ^ 2 ≠ 0 := by
    intro h0
    rw [h0, mul_zero] at htheta
    exact hp2 htheta.symm
  have hp3 : (t₁ / T_theta) * (t₂ / T_theta) = p ^ 3 := by
    rw [div_mul_div_comm, ← sq, hprod, hq, ← htheta, mul_div_cancel_right₀ _ hT2]
  refine ⟨hp3, ?_⟩
  rw [hp3, hq]
  ring

/-- **Exact Complex Divisor Modulus `‖t₂ / T_θ‖ = q ^ (3 / 4 : ℝ)` (`qou-wgnx` 16th–17th entries):**
At `1 < q` (`q < 5`), where the `0`-side exponent `t₂ : ℂ` satisfies `‖t₂‖² = q - 1`
(`C1ZeroSide.norm_sq_eq_q_sub_one`) and `T_θ > 0` satisfies `q^{3/2} T_θ² = q - 1`, the connection
divisor parameter `α = t₂ / T_θ` has exact modulus `q^{3/4}`. -/
theorem norm_connDivisorAlpha_eq_q_three_quarters {q T_theta : ℝ} {t₂ : ℂ}
    (hq : 1 < q) (hT_pos : 0 < T_theta)
    (ht₂ : ‖t₂‖ ^ 2 = q - 1)
    (hT_eq : q ^ ((3 : ℝ) / 2) * T_theta ^ 2 = q - 1) :
    ‖t₂ / (T_theta : ℂ)‖ = q ^ ((3 : ℝ) / 4) := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq1 : q - 1 ≠ 0 := ne_of_gt (sub_pos.mpr hq)
  have hT2 : T_theta ^ 2 ≠ 0 := pow_ne_zero 2 (ne_of_gt hT_pos)
  have hnorm_div : ‖t₂ / (T_theta : ℂ)‖ = ‖t₂‖ / T_theta := by
    rw [norm_div, Complex.norm_real, Real.norm_of_nonneg hT_pos.le]
  have hsq_lhs : (‖t₂‖ / T_theta) ^ 2 = q ^ ((3 : ℝ) / 2) := by
    rw [div_pow, ht₂, ← hT_eq, mul_div_cancel_right₀ _ hT2]
  have hsq_rhs : (q ^ ((3 : ℝ) / 4)) ^ 2 = q ^ ((3 : ℝ) / 2) := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hq0.le]
    norm_num
  have hlhs_nn : 0 ≤ ‖t₂‖ / T_theta := div_nonneg (norm_nonneg _) hT_pos.le
  have hrhs_nn : 0 ≤ q ^ ((3 : ℝ) / 4) := Real.rpow_nonneg hq0.le _
  rw [hnorm_div]
  nlinarith [sq_nonneg (‖t₂‖ / T_theta - q ^ ((3 : ℝ) / 4)), hsq_lhs, hsq_rhs]

end CanonicalParameterAndDivisorModulus

/-! ## §5. Third Singular Site `x = q⁻²` Gauge-Invariant Torus Degree `−1` (`qou-qbe9x`) -/

section ThirdSingularSite

/-- **Determinant under a `q`-difference gauge transformation (`qou-qbe9x`):**
Over any `[Field K]`, if `F` is invertible (`det F ≠ 0`), then transforming a companion matrix
`A ↦ Fq * A * F⁻¹` multiplies its determinant by `det Fq / det F`. -/
theorem det_companion_gauge {K n : Type*} [Field K] [Fintype n] [DecidableEq n]
    (A F Fq : Matrix n n K) (hF : F.det ≠ 0) :
    (Fq * A * F⁻¹).det = (Fq.det / F.det) * A.det := by
  have hu : IsUnit F.det := Ne.isUnit hF
  have hdet_inv : (F⁻¹).det * F.det = 1 := by
    rw [← Matrix.det_mul, Matrix.nonsing_inv_mul F hu, Matrix.det_one]
  have hinv : (F⁻¹).det = (F.det)⁻¹ := eq_inv_of_mul_eq_one_left hdet_inv
  rw [Matrix.det_mul, Matrix.det_mul, hinv]
  ring

/-- Coefficientwise action of `q`-dilation `P(X) ↦ P(q X)` on `R[X]`. -/
theorem coeff_comp_C_mul_X {R : Type*} [CommRing R] (q : R) (P : R[X]) (k : ℕ) :
    (P.comp (C q * X)).coeff k = P.coeff k * q ^ k := by
  induction P using Polynomial.induction_on' with
  | add p r hp hr =>
    rw [add_comp, coeff_add, hp, hr, coeff_add, add_mul]
  | monomial n a =>
    rw [monomial_comp, mul_pow, ← C_pow, ← mul_assoc, ← C_mul,
      C_mul_X_pow_eq_monomial, coeff_monomial, coeff_monomial]
    split_ifs with hnk
    · subst hnk; rfl
    · simp

/-- Over `[Field K]` (`q ≠ 0`), `q`-dilation preserves `natDegree`. -/
theorem natDegree_comp_C_mul_X {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (P : K[X]) :
    (P.comp (C q * X)).natDegree = P.natDegree := by
  apply le_antisymm
  · rw [natDegree_le_iff_coeff_eq_zero]
    intro k hk
    rw [coeff_comp_C_mul_X, coeff_eq_zero_of_natDegree_lt hk, zero_mul]
  · rw [natDegree_le_iff_coeff_eq_zero]
    intro k hk
    have hc := coeff_eq_zero_of_natDegree_lt hk
    rw [coeff_comp_C_mul_X] at hc
    exact (mul_eq_zero.mp hc).resolve_right (pow_ne_zero k hq)

/-- Over `[Field K]` (`q ≠ 0`), `q`-dilation preserves non-vanishing of polynomials. -/
theorem comp_C_mul_X_ne_zero {K : Type*} [Field K] {q : K} (hq : q ≠ 0) {P : K[X]}
    (hP : P ≠ 0) : P.comp (C q * X) ≠ 0 := by
  intro h0
  apply hP
  ext k
  have hk : (P.comp (C q * X)).coeff k = 0 := by rw [h0, coeff_zero]
  rw [coeff_comp_C_mul_X] at hk
  simpa using (mul_eq_zero.mp hk).resolve_right (pow_ne_zero k hq)

/-- Over `[Field K]` (`q ≠ 0`), `q`-dilation preserves `natTrailingDegree`. -/
theorem natTrailingDegree_comp_C_mul_X {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (P : K[X]) :
    (P.comp (C q * X)).natTrailingDegree = P.natTrailingDegree := by
  by_cases hP : P = 0
  · subst hP; simp
  · have hPq : P.comp (C q * X) ≠ 0 := comp_C_mul_X_ne_zero hq hP
    apply le_antisymm
    · refine le_natTrailingDegree hP fun i hi => ?_
      have hc := coeff_eq_zero_of_lt_natTrailingDegree hi
      rw [coeff_comp_C_mul_X] at hc
      exact (mul_eq_zero.mp hc).resolve_right (pow_ne_zero i hq)
    · refine le_natTrailingDegree hPq fun i hi => ?_
      rw [coeff_comp_C_mul_X, coeff_eq_zero_of_lt_natTrailingDegree hi, zero_mul]

/-- Torus divisor degree `deg(div P|_{Kˣ}) = natDegree P - natTrailingDegree P` of a polynomial
(total root multiplicity on `Kˣ = K \ {0}` over an algebraically closed extension). -/
def torusDeg {R : Type*} [CommRing R] (P : R[X]) : ℤ :=
  (P.natDegree : ℤ) - (P.natTrailingDegree : ℤ)

/-- **Gauge coboundary torus degree is identically `0` (`qou-qbe9x`):**
For any `q ≠ 0` and any rational function `g = G_num / G_den` (`G_num, G_den ≠ 0`), `q`-dilation
preserves `torusDeg` on both numerator and denominator, so the coboundary `g(q X) / g(X)`
contributes zero net torus divisor degree on `Kˣ`. -/
theorem torusDeg_comp_scale_eq {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (P : K[X]) :
    torusDeg (P.comp (C q * X)) = torusDeg P ∧
      torusDeg (P.comp (C q * X)) - torusDeg P = 0 := by
  have heq : torusDeg (P.comp (C q * X)) = torusDeg P := by
    unfold torusDeg
    rw [natDegree_comp_C_mul_X hq, natTrailingDegree_comp_C_mul_X hq]
  exact ⟨heq, sub_eq_zero.mpr heq⟩

/-- Numerator `-(q - 1)` and denominator `q² X - 1` of C1's unramified companion determinant
`QOU.QBeta.detA q x = -(q - 1) / (q² x - 1)`. -/
noncomputable def c1DetANumPoly {R : Type*} [CommRing R] (q : R) : R[X] :=
  C (-(q - 1))

noncomputable def c1DetADenPoly {R : Type*} [CommRing R] (q : R) : R[X] :=
  C (q ^ 2) * X - 1

/-- **Third singular site `x = q⁻²` has non-removable torus degree `-1` (`qou-qbe9x`):**
1. Evaluating `c1DetANumPoly q / c1DetADenPoly q` at `x` equals `QOU.QBeta.detA q x`;
2. `c1DetADenPoly q` vanishes at `x` iff `x = q⁻²` (representing the identity orbit `[1]` on `E_q`);
3. `torusDeg (c1DetANumPoly q) - torusDeg (c1DetADenPoly q) = -1 ≠ 0`, so no rational gauge
   coboundary `g(q X) / g(X)` (which has torus degree `0` by `torusDeg_comp_scale_eq`) can cancel
   the singularity out of `Kˣ`. -/
theorem c1_third_singular_site_torusDeg_neg_one {K : Type*} [Field K] {q : K}
    (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    c1DetANumPoly q ≠ 0 ∧
    c1DetADenPoly q ≠ 0 ∧
    (∀ x : K, (c1DetANumPoly q).eval x / (c1DetADenPoly q).eval x = QOU.QBeta.detA q x) ∧
    (∀ x : K, (c1DetADenPoly q).eval x = 0 ↔ x = (q ^ 2)⁻¹) ∧
    torusDeg (c1DetANumPoly q) - torusDeg (c1DetADenPoly q) = -1 := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  refine ⟨?_, ?_, fun x => ?_, fun x => ?_, ?_⟩
  · unfold c1DetANumPoly
    exact C_ne_zero.mpr (neg_ne_zero.mpr hq1)
  · intro h0
    have hev := congr_arg (eval 0) h0
    simp [c1DetADenPoly] at hev
  · simp [c1DetANumPoly, c1DetADenPoly, QOU.QBeta.detA]
  · simp only [c1DetADenPoly, eval_sub, eval_mul, eval_C, eval_X, eval_one]
    constructor
    · intro hx
      have hmul : q ^ 2 * x = 1 := sub_eq_zero.mp hx
      exact eq_inv_of_mul_eq_one_right hmul
    · rintro rfl
      rw [mul_inv_cancel₀ hq2, sub_self]
  · have hn_deg : (c1DetANumPoly q).natDegree = 0 := natDegree_C _
    have hn_ntd : (c1DetANumPoly q).natTrailingDegree = 0 := by
      refine natTrailingDegree_eq_zero_of_constantCoeff_ne_zero ?_
      simpa [c1DetANumPoly, sub_eq_zero] using (sub_ne_zero.mp hq1).symm
    have hd_deg : (c1DetADenPoly q).natDegree = 1 := by
      unfold c1DetADenPoly
      compute_degree!
    have hd_ntd : (c1DetADenPoly q).natTrailingDegree = 0 := by
      refine natTrailingDegree_eq_zero_of_constantCoeff_ne_zero ?_
      simp [c1DetADenPoly]
    unfold torusDeg
    rw [hn_deg, hn_ntd, hd_deg, hd_ntd]
    norm_num

end ThirdSingularSite

/-! ## §6. RSZ §1.3.2 Bound-Form `IsQGevreyOrderLE` & Full Lacunary `L_k` Order (`qou-slvl` item 1) -/

section BoundFormQGevrey

open QOU.Mathlib.QGevreyOrder

/-- **RSZ Astérisque 355 §1.3.2 big-O bound-form q-Gevrey order (`qou-slvl` item 1):**
`a ∈ ℂ[[z]]_{q; s}` iff `∃ C > 0, ∃ A > 0, ∀ n, ‖a n‖ ≤ C * A^n * q^(s * n² / 2)`.
Unlike the limit form `IsQGevreyOrder`, this handles lacunary sequences (whose vanishing terms have
`log ‖0‖ = 0`) without restricting to a nonzero subsequence. -/
def IsQGevreyOrderLE {K : Type*} [NormedField K] (q s : ℝ) (a : ℕ → K) : Prop :=
  ∃ C > (0 : ℝ), ∃ A > (0 : ℝ), ∀ n : ℕ, ‖a n‖ ≤ C * A ^ n * q ^ (s * (n : ℝ) ^ 2 / 2)

/-- **`IsQGevreyOrder q s a` implies `IsQGevreyOrderLE q (s + ε) a` for every `ε > 0`:**
From `order_eventually_le`, `2 log_q ‖a n‖ / n² ≤ s + ε` holds for all `n ≥ N`, and the finitely
many terms `n < N` are absorbed into `C` with `A = 1`. -/
theorem isQGevreyOrderLE_of_order_add_eps {K : Type*} [NormedField K] {q s : ℝ} {a : ℕ → K}
    (hq : 1 < q) (ha : IsQGevreyOrder q s a) {ε : ℝ} (hε : 0 < ε) :
    IsQGevreyOrderLE q (s + ε) a := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hlogq : 0 < Real.log q := Real.log_pos hq
  have hev := order_eventually_le ha hε
  obtain ⟨N, hN⟩ := eventually_atTop.mp hev
  set C : ℝ := 1 + ∑ j ∈ Finset.range (max N 1),
      ‖a j‖ / q ^ ((s + ε) * (j : ℝ) ^ 2 / 2) with hCdef
  have hC1 : 1 ≤ C := by
    have hsum_nn : 0 ≤ ∑ j ∈ Finset.range (max N 1),
        ‖a j‖ / q ^ ((s + ε) * (j : ℝ) ^ 2 / 2) :=
      Finset.sum_nonneg fun j _ => div_nonneg (norm_nonneg _) (Real.rpow_pos_of_pos hq0 _).le
    linarith
  have hC_pos : 0 < C := lt_of_lt_of_le zero_lt_one hC1
  refine ⟨C, hC_pos, 1, one_pos, fun n => ?_⟩
  rw [one_pow, mul_one]
  set Qn : ℝ := q ^ ((s + ε) * (n : ℝ) ^ 2 / 2) with hQndef
  have hQn_pos : 0 < Qn := Real.rpow_pos_of_pos hq0 _
  by_cases hn_lt : n < max N 1
  · have hterm_le : ‖a n‖ / Qn ≤ C := by
      have hsingle : ‖a n‖ / q ^ ((s + ε) * (n : ℝ) ^ 2 / 2) ≤ ∑ j ∈ Finset.range (max N 1),
          ‖a j‖ / q ^ ((s + ε) * (j : ℝ) ^ 2 / 2) :=
        Finset.single_le_sum
          (f := fun j => ‖a j‖ / q ^ ((s + ε) * (j : ℝ) ^ 2 / 2))
          (fun j _ => div_nonneg (norm_nonneg _) (Real.rpow_pos_of_pos hq0 _).le)
          (Finset.mem_range.mpr hn_lt)
      rw [hQndef, hCdef]
      linarith
    exact (div_le_iff₀ hQn_pos).mp hterm_le
  · push_neg at hn_lt
    have hnN : N ≤ n := le_trans (le_max_left N 1) hn_lt
    have hn1 : 1 ≤ n := le_trans (le_max_right N 1) hn_lt
    clear_value C
    clear hCdef
    by_cases ha0 : a n = 0
    · rw [ha0, norm_zero]
      exact mul_nonneg hC_pos.le hQn_pos.le
    · have han_pos : 0 < ‖a n‖ := norm_pos_iff.mpr ha0
      have hn2_pos : (0 : ℝ) < (n : ℝ) ^ 2 := by
        have : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn1
        positivity
      have hbd := hN n hnN
      have hbd' : 2 * (Real.log ‖a n‖ / Real.log q) / (n : ℝ) ^ 2 ≤ s + ε := hbd
      have hlog_le : Real.log ‖a n‖ ≤ ((s + ε) * (n : ℝ) ^ 2 / 2) * Real.log q := by
        rw [div_le_iff₀ hn2_pos] at hbd'
        have h2 : (2 * Real.log ‖a n‖) / Real.log q ≤ (s + ε) * (n : ℝ) ^ 2 := by
          rwa [← mul_div_assoc] at hbd'
        rw [div_le_iff₀ hlogq] at h2
        linarith
      have hexp_le : ‖a n‖ ≤ Qn := by
        rw [← Real.exp_log han_pos, hQndef, Real.rpow_def_of_pos hq0, mul_comm (Real.log q)]
        exact Real.exp_le_exp.mpr hlog_le
      clear_value Qn
      clear hQndef
      calc
        ‖a n‖ ≤ Qn := hexp_le
        _ = 1 * Qn := (one_mul Qn).symm
        _ ≤ C * Qn := mul_le_mul_of_nonneg_right hC1 hQn_pos.le

/-- **Refutation of the unshifted (`ε = 0`) implication:**
`IsQGevreyOrder q s a` does **not** imply `IsQGevreyOrderLE q s a` without `+ ε`: the sub-quadratic
super-linear sequence `a_n = 2^{n √n}` has limit order `0` (`2 n √n / n² = 2 / √n → 0`), yet
exceeds `C · A^n` for every `C, A > 0`. -/
theorem not_forall_isQGevreyOrder_imp_le :
    ¬ ∀ (q s : ℝ) (a : ℕ → ℝ),
        1 < q → IsQGevreyOrder q s a → IsQGevreyOrderLE q s a := by
  intro hall
  let a : ℕ → ℝ := fun n => (2 : ℝ) ^ ((n : ℝ) * Real.sqrt (n : ℝ))
  have ha_ord : IsQGevreyOrder 2 0 a := by
    unfold IsQGevreyOrder
    have hsqrt_top : Tendsto (fun n : ℕ => Real.sqrt (n : ℝ)) atTop atTop := by
      rw [tendsto_atTop]
      intro B
      obtain ⟨M, hM⟩ := exists_nat_gt ((max B 0) ^ 2)
      refine eventually_atTop.mpr ⟨M, fun n hn => ?_⟩
      have hB : B ≤ max B 0 := le_max_left B 0
      have hM_le : (max B 0) ^ 2 ≤ (n : ℝ) := by
        have h1 : (M : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
        linarith
      have hsq : max B 0 = Real.sqrt ((max B 0) ^ 2) :=
        (Real.sqrt_sq (le_max_right B 0)).symm
      calc
        B ≤ max B 0 := hB
        _ = Real.sqrt ((max B 0) ^ 2) := hsq
        _ ≤ Real.sqrt (n : ℝ) := Real.sqrt_le_sqrt hM_le
    have hlim : Tendsto (fun n : ℕ => 2 * (Real.sqrt (n : ℝ))⁻¹) atTop (𝓝 0) := by
      simpa using (tendsto_inv_atTop_zero.comp hsqrt_top).const_mul 2
    refine hlim.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hn_pos : (0 : ℝ) < (n : ℝ) := by
      have : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
      linarith
    have hsn_pos : 0 < Real.sqrt (n : ℝ) := Real.sqrt_pos.mpr hn_pos
    have hapos : 0 < a n := Real.rpow_pos_of_pos two_pos _
    have hlog2 : Real.log 2 ≠ 0 := ne_of_gt (Real.log_pos one_lt_two)
    show 2 * (Real.sqrt (n : ℝ))⁻¹ = 2 * (Real.log ‖a n‖ / Real.log 2) / (n : ℝ) ^ 2
    rw [Real.norm_of_nonneg hapos.le]
    dsimp [a]
    rw [Real.log_rpow two_pos, mul_div_cancel_right₀ _ hlog2]
    have hsq : Real.sqrt (n : ℝ) * Real.sqrt (n : ℝ) = (n : ℝ) := Real.mul_self_sqrt hn_pos.le
    field_simp [hn_pos.ne', hsn_pos.ne']
    nlinarith [hsq]
  obtain ⟨C, hC, A, hA, hbd⟩ := hall 2 0 a one_lt_two ha_ord
  have hlog2 : 0 < Real.log 2 := Real.log_pos one_lt_two
  obtain ⟨m, hm⟩ := exists_nat_gt (max 2 (|Real.log C / Real.log 2| + |Real.log A / Real.log 2| + 2))
  have hm2 : (2 : ℝ) < (m : ℝ) := lt_of_le_of_lt (le_max_left _ _) hm
  have hm_pos : (0 : ℝ) < (m : ℝ) := by linarith
  have hm_big : |Real.log C / Real.log 2| + |Real.log A / Real.log 2| + 2 < (m : ℝ) :=
    lt_of_le_of_lt (le_max_right _ _) hm
  have hspec := hbd (m * m)
  simp only [zero_mul, zero_div, Real.rpow_zero, mul_one] at hspec
  have hapos : 0 < a (m * m) := Real.rpow_pos_of_pos two_pos _
  rw [Real.norm_of_nonneg hapos.le] at hspec
  have hlog_le := Real.log_le_log hapos hspec
  dsimp [a] at hlog_le
  rw [Real.log_rpow two_pos, Real.log_mul hC.ne' (pow_pos hA _).ne', Real.log_pow] at hlog_le
  have hcast : ((m * m : ℕ) : ℝ) = (m : ℝ) ^ 2 := by push_cast; ring
  have hsqrt_m2 : Real.sqrt ((m * m : ℕ) : ℝ) = (m : ℝ) := by
    rw [hcast, Real.sqrt_sq hm_pos.le]
  rw [hsqrt_m2, hcast] at hlog_le
  have hdiv : (m : ℝ) ^ 3 ≤ Real.log C / Real.log 2 + (m : ℝ) ^ 2 * (Real.log A / Real.log 2) := by
    have h1 : (m : ℝ) ^ 3 * Real.log 2 ≤ Real.log C + (m : ℝ) ^ 2 * Real.log A := by
      nlinarith [hlog_le]
    have h2 : (Real.log C / Real.log 2 + (m : ℝ) ^ 2 * (Real.log A / Real.log 2)) * Real.log 2 =
        Real.log C + (m : ℝ) ^ 2 * Real.log A := by
      field_simp [hlog2.ne']
    exact le_of_mul_le_mul_right (by linarith [h1, h2]) hlog2
  have hc_abs : Real.log C / Real.log 2 ≤ |Real.log C / Real.log 2| := le_abs_self _
  have ha_abs : Real.log A / Real.log 2 ≤ |Real.log A / Real.log 2| := le_abs_self _
  have hm2_nn : 0 ≤ (m : ℝ) ^ 2 := sq_nonneg _
  have hstep1 : Real.log C / Real.log 2 + (m : ℝ) ^ 2 * (Real.log A / Real.log 2) ≤
      |Real.log C / Real.log 2| + (m : ℝ) ^ 2 * |Real.log A / Real.log 2| := by
    nlinarith [mul_le_mul_of_nonneg_left ha_abs hm2_nn, hc_abs]
  have hc_lt : |Real.log C / Real.log 2| < (m : ℝ) ^ 2 := by
    have h1 : |Real.log C / Real.log 2| < (m : ℝ) := by
      have := abs_nonneg (Real.log A / Real.log 2)
      linarith
    nlinarith [hm2]
  have ha_lt : |Real.log A / Real.log 2| + 2 ≤ (m : ℝ) := by
    have := abs_nonneg (Real.log C / Real.log 2)
    linarith
  nlinarith [hdiv, hstep1, hc_lt, mul_le_mul_of_nonneg_left ha_lt hm2_nn]

/-- **Full lacunary coefficient sequence of `L_k = z^k σ - 1` (`qou-slvl` item 1):**
`c_m = slopeKCoeff q k (m / k)` when `k ∣ m` and `0` otherwise, defined on all `m : ℕ` without
passing to the `m = j k` subsequence. -/
noncomputable def lacunarySlopeKCoeff (q : ℝ) (k m : ℕ) : ℝ :=
  if k ∣ m then slopeKCoeff q k (m / k) else 0

/-- **Sharp RSZ §1.3.2 bound-form order `1 / k` (level `k`) on the full lacunary sequence:**
1. `IsQGevreyOrderLE q (1 / k) (lacunarySlopeKCoeff q k)` holds unconditionally with `C = 1, A = 1`;
2. No `s < 1 / k` bounds `lacunarySlopeKCoeff q k` (`¬ IsQGevreyOrderLE q s (lacunarySlopeKCoeff q k)`).
Thus the full solution sequence of `L_k = z^k σ - 1` has exact RSZ order `1 / k` and level `k`
without any subsequence dodge. -/
theorem lacunarySlopeKCoeff_orderLE_sharp (q : ℝ) (hq : 1 < q) (k : ℕ) (hk : 1 ≤ k) :
    IsQGevreyOrderLE q (1 / (k : ℝ)) (lacunarySlopeKCoeff q k) ∧
    (∀ s : ℝ, s < 1 / (k : ℝ) → ¬ IsQGevreyOrderLE q s (lacunarySlopeKCoeff q k)) := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hlogq : 0 < Real.log q := Real.log_pos hq
  have hk_pos : (0 : ℝ) < (k : ℝ) := by exact_mod_cast hk
  have hk_ne : k ≠ 0 := by omega
  refine ⟨⟨1, one_pos, 1, one_pos, fun m => ?_⟩, fun s hs hle => ?_⟩
  · simp only [one_pow, one_mul, lacunarySlopeKCoeff]
    split_ifs with hdvd
    · obtain ⟨j, rfl⟩ := hdvd
      rw [Nat.mul_div_cancel_left j (by omega : 0 < k)]
      have hd_pos : 0 < slopeKCoeff q k j := slopeKCoeff_pos q hq0 k j
      rw [Real.norm_of_nonneg hd_pos.le]
      have hlog_eq := logb_slopeKCoeff q hq k j
      have hlog_d : Real.log (slopeKCoeff q k j) =
          ((k : ℝ) * ((j : ℝ) * j - j) / 2) * Real.log q := by
        have h1 : Real.log (slopeKCoeff q k j) / Real.log q =
            (k : ℝ) * ((j : ℝ) * j - j) / 2 := hlog_eq
        exact (div_eq_iff hlogq.ne').mp h1
      rw [← Real.exp_log hd_pos, hlog_d, Real.rpow_def_of_pos hq0]
      apply Real.exp_le_exp.mpr
      have hcast : ((k * j : ℕ) : ℝ) = (k : ℝ) * (j : ℝ) := by push_cast; ring
      rw [hcast]
      have hexp_le : (k : ℝ) * ((j : ℝ) * j - j) / 2 ≤
          1 / (k : ℝ) * ((k : ℝ) * (j : ℝ)) ^ 2 / 2 := by
        have hsimpl : 1 / (k : ℝ) * ((k : ℝ) * (j : ℝ)) ^ 2 / 2 =
            (k : ℝ) * ((j : ℝ) * j) / 2 := by
          field_simp [hk_pos.ne']
        rw [hsimpl]
        have hj_nn : (0 : ℝ) ≤ (j : ℝ) := Nat.cast_nonneg j
        nlinarith [mul_nonneg hk_pos.le hj_nn]
      rw [mul_comm (Real.log q)]
      exact mul_le_mul_of_nonneg_right hexp_le hlogq.le
    · rw [norm_zero]
      exact (Real.rpow_pos_of_pos hq0 _).le
  · obtain ⟨C, hC, A, hA, hbd⟩ := hle
    -- Along `m = k * j`, `2 log_q(lacunarySlopeKCoeff q k (k*j)) / (k*j)² → 1 / k > s`,
    -- whereas `hbd` forces the `atTop` limit to be `≤ s`.
    set δ : ℝ := (1 / (k : ℝ) - s) / 2 with hδdef
    have hδ_pos : 0 < δ := by linarith
    have hord := slopeKCoeff_order q hq k hk
    have hev1 : ∀ᶠ j : ℕ in atTop,
        1 / (k : ℝ) - δ ≤ 2 * (Real.log (slopeKCoeff q k j) / Real.log q) / (((k : ℝ) * j) ^ 2) := by
      have hmem : ∀ᶠ y : ℝ in 𝓝 (1 / (k : ℝ)), 1 / (k : ℝ) - δ ≤ y := by
        filter_upwards [Ioi_mem_nhds (show 1 / (k : ℝ) - δ < 1 / (k : ℝ) by linarith)] with y hy
          using le_of_lt hy
      exact hord.eventually hmem
    -- Upper bound along `j` from `hbd (k * j)`:
    set aC : ℝ := Real.log C / Real.log q
    set aA : ℝ := Real.log A / Real.log q
    have ht1 : Tendsto (fun j : ℕ => 2 * aC / (((k : ℝ) * j) ^ 2)) atTop (𝓝 0) := by
      have hsq : Tendsto (fun j : ℕ => ((k : ℝ) * j) ^ 2) atTop atTop :=
        (tendsto_pow_atTop (by norm_num : (2 : ℕ) ≠ 0)).comp
          (Tendsto.const_mul_atTop hk_pos tendsto_natCast_atTop_atTop)
      simpa [div_eq_mul_inv] using (tendsto_inv_atTop_zero.comp hsq).const_mul (2 * aC)
    have ht2 : Tendsto (fun j : ℕ => 2 * aA / ((k : ℝ) * j)) atTop (𝓝 0) := by
      have hlin : Tendsto (fun j : ℕ => (k : ℝ) * j) atTop atTop :=
        Tendsto.const_mul_atTop hk_pos tendsto_natCast_atTop_atTop
      simpa [div_eq_mul_inv] using (tendsto_inv_atTop_zero.comp hlin).const_mul (2 * aA)
    have ht_sum : Tendsto
        (fun j : ℕ => 2 * aC / (((k : ℝ) * j) ^ 2) + 2 * aA / ((k : ℝ) * j)) atTop (𝓝 0) := by
      simpa using ht1.add ht2
    have hev2 : ∀ᶠ j : ℕ in atTop,
        2 * aC / (((k : ℝ) * j) ^ 2) + 2 * aA / ((k : ℝ) * j) < δ :=
      ht_sum.eventually (gt_mem_nhds hδ_pos)
    obtain ⟨j, hj1, hj2, hj_ge1⟩ := (hev1.and (hev2.and (eventually_ge_atTop 1))).exists
    have hj_pos : (0 : ℝ) < (j : ℝ) := by exact_mod_cast (by omega : 0 < j)
    have hkj_pos : (0 : ℝ) < (k : ℝ) * j := mul_pos hk_pos hj_pos
    have hkj2_pos : (0 : ℝ) < ((k : ℝ) * j) ^ 2 := pow_pos hkj_pos 2
    have hspec := hbd (k * j)
    have hlac : lacunarySlopeKCoeff q k (k * j) = slopeKCoeff q k j := by
      simp [lacunarySlopeKCoeff, Nat.mul_div_cancel_left j (by omega : 0 < k)]
    rw [hlac] at hspec
    have hd_pos : 0 < slopeKCoeff q k j := slopeKCoeff_pos q hq0 k j
    rw [Real.norm_of_nonneg hd_pos.le] at hspec
    have hlog_le := Real.log_le_log hd_pos hspec
    have hArhs_pos : 0 < C * A ^ (k * j) := mul_pos hC (pow_pos hA _)
    have hQrhs_pos : 0 < q ^ (s * ((k * j : ℕ) : ℝ) ^ 2 / 2) := Real.rpow_pos_of_pos hq0 _
    rw [Real.log_mul hArhs_pos.ne' hQrhs_pos.ne',
        Real.log_mul hC.ne' (pow_pos hA _).ne', Real.log_pow, Real.log_rpow hq0] at hlog_le
    have hcast : ((k * j : ℕ) : ℝ) = (k : ℝ) * j := by push_cast; ring
    rw [hcast] at hlog_le
    have hdiv_q : Real.log (slopeKCoeff q k j) / Real.log q ≤
        aC + ((k : ℝ) * j) * aA + s * ((k : ℝ) * j) ^ 2 / 2 := by
      rw [div_le_iff₀ hlogq]
      have hexp_rhs : (aC + ((k : ℝ) * j) * aA + s * ((k : ℝ) * j) ^ 2 / 2) * Real.log q =
          Real.log C + ((k : ℝ) * j) * Real.log A +
            s * ((k : ℝ) * j) ^ 2 / 2 * Real.log q := by
        dsimp [aC, aA]
        field_simp [hlogq.ne']
      linarith [hlog_le, hexp_rhs]
    have hdiv_kj2 : 2 * (Real.log (slopeKCoeff q k j) / Real.log q) / (((k : ℝ) * j) ^ 2) ≤
        2 * aC / (((k : ℝ) * j) ^ 2) + 2 * aA / ((k : ℝ) * j) + s := by
      rw [div_le_iff₀ hkj2_pos]
      have hrhs_eq :
          (2 * aC / (((k : ℝ) * j) ^ 2) + 2 * aA / ((k : ℝ) * j) + s) * (((k : ℝ) * j) ^ 2) =
            2 * (aC + ((k : ℝ) * j) * aA + s * ((k : ℝ) * j) ^ 2 / 2) := by
        field_simp [hkj_pos.ne']
      nlinarith [hdiv_q, hrhs_eq]
    linarith [hj1, hj2, hdiv_kj2]

end BoundFormQGevrey

end QOU.QBeta.C1ConnectionAlgebra
