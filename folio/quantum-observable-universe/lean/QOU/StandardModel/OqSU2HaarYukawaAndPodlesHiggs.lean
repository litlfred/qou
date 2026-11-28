/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import CompactQuantumMetrics.OqSU2ModularNakayama
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# `O_q(SU(2))` Woronowicz Haar–Yukawa Unification, Podleś `q`-Monopole Higgs Projector, and Kurtosis Laws

This module formalizes over generic commutative rings (`[CommRing R]`, **zero `sorry`**, **zero
custom axioms**, **zero `[Field]` / `field_simp`**, **zero transcendental tokens**, **zero
empirical literals**) five structural bridges connecting Woronowicz's coordinate algebra
`O_q(SU(2))`, the Podleś standard quantum sphere `S²_q = O_q(SU(2))^{U(1)}`, noncommutative-geometry
Higgs quartic couplings, and QOU's electroweak/Higgs sector:

1. **Section 1 — Woronowicz Haar Eigenvalues `≡` Jimbo Singlet Yukawa Compression & `[2]_q / 2`
   Variance Lock (`qou-99qc`):**
   - Constructs the Jimbo right-handed singlet projector `prJimbo q qTwo` and its strand-flipped
     partner `prJimboFlip q qTwo` on `V ⊗ V` over `[CommRing R]` (`(qTwo : R) = q + q⁻¹`).
   - Proves (`haar_eq_jimbo_yukawa_weights_and_variance`) that for any normalized `R`-linear
     functional `h : OqSU2 R q →ₗ[R] R` satisfying Woronowicz's rank-1 Haar relation
     `(1 + q²) h(βγ) = -q h(1)`:
     * `h(δα) = q² u⁻¹ = q · [2]_q⁻¹ = (prJimbo)_{1,1}` and
       `h(αδ) = u⁻¹ = q⁻¹ · [2]_q⁻¹ = (prJimbo)_{2,2}`;
     * Partial-trace flavour-blindness `(ptrRJimbo)_{0,0} = (ptrRJimbo)_{1,1}` holds **if and only if**
       `a = q² b` (Woronowicz's KMS modular swap relation `h(δα) = q² h(αδ)`);
     * `[2]_q² · h(δα) · h(αδ) = 1`, identifying the electroweak Plancherel dressing `([2]_q / 2)²`
       with the inverse normalized Woronowicz Haar variance `(4 h(δα) h(αδ))⁻¹`;
     * Over any strict ordered commutative ring with `1 < q`, KMS positivity `h(αδ) < h(δα)`
       strictly breaks the `matter ⊗ Higgs` vs `Higgs ⊗ matter` tie by the Haar polarization bias
       `(q² - 1) u⁻¹ = (q - q⁻¹) [2]_q⁻¹ > 0`.

2. **Section 2 — Podleś Standard Sphere `S²_q`, Nonlinear-`σ` Constraint, and Hajac–Majid
   `q`-Monopole Projector (`qou-ukqh`):**
   - Defines on `OqSU2 R q` the `U(1)`-charge-`(+1)` spinor column `hopfCol q = (α, γ)^T`, its
     `compactStar`-adjoint row `hopfRow q = (δ, -q⁻¹ β)`, and the `2 × 2` Hajac–Majid / Bott
     projector `podlesProj q = hopfCol q ⊗ hopfRow q ∈ M₂(OqSU2 R q)`.
   - Proves unconditionally over `[CommRing R]`:
     * **Nonlinear-`σ` vacuum pairing (`hopfRow_dot_hopfCol_eq_one`):** `δ α - q⁻¹ β γ = 1`;
     * **Exact idempotence & residual orthogonality (`podlesProj_idem_and_resid`):**
       `e_Podleś² = e_Podleś`, `(1 - e_Podleś)² = 1 - e_Podleś`, `e_Podleś (1 - e_Podleś) = 0`;
     * **Exact `compactStar`-Hermiticity (`podlesProj_compactStar_hermitian`):**
       `((e_Podleś)_{ij})^* = (e_Podleś)_{ji}`;
     * **Exact `U(1)` gauge invariance (`podlesProj_u1_invariant`):** fixed entrywise under
       `torusScaleAlgHom q v v⁻¹` for every `v : Rˣ` (descending to `O(S²_q)`);
     * **Quantum pivotal trace `= 1` vs classical trace & determinant symmetry-breaking defects
       (`podlesProj_quantum_trace_eq_one_and_defects`):**
       `(e_Podleś)_{00} + q² (e_Podleś)_{11} = 1`, whereas the ordinary matrix trace is
       `1 + (q - q⁻¹) β γ` (Haar defect `(q² - 1) u⁻¹`) and the classical determinant defect
       `1 - (αδ - βγ) = -(q - 1) β γ` has Haar expectation `(q - 1) [2]_q⁻¹`.

3. **Section 3 — Podleś Radial Kurtosis `[2]_q² / [3]_q`, Universal `v²`-Cancellation, and
   Jucys–Murphy Rank-vs-`q`-Factorial Separation (`qou-z3x8`, `qou-zd6l`):**
   - Proves the cleared Podleś radial kurtosis identity `[3]_q (1 + q²)² = [2]_q² (1 + q² + q⁴)`
     (`h((γ*γ)²) / h(γ*γ)² = [2]_q² / [3]_q = (4 + h²) / (3 + h²)`) and strict sub-`4/3` bound
     `4 [3]_q - 3 [2]_q² = (q - q⁻¹)² > 0` (`[2]_q² / [3]_q < 4/3` for `q - q⁻¹ ≠ 0`).
   - Proves the cleared `v²`-cancellation law shared by Chamseddine–Connes spectral-action and
     QOU Plancherel Higgs quartics, and proves that `H₃`/`H₄` Jucys–Murphy content sums give `[3]_q`
     on `(2,1)` and `[2]_q²` on `(2,2)`, while `[2]_q [3]_q > 6` for `1 < q` separates the quantum
     factorial `[3]_q! / 5` from the undeformed Wedderburn rank ratio `dim H₃ / dim Z(H₄) = 6 / 5`.

-- Ref: [woronowicz1987] Woronowicz, Compact matrix pseudogroups and Haar state on SU_q(2)
-- Ref: [podles1987] Podleś, Quantum spheres S^2_q as U(1)-invariant subalgebras
-- Ref: [hajac-majid1999] Hajac & Majid, Projective module description of the q-monopole
-- Ref: [connes-lott1990] Connes & Lott, Particle models and noncommutative geometry
-- Ref: [chamseddine-connes-1997] Chamseddine & Connes, The spectral action principle
-- Ref: [chamseddine-connes-2012-resilience] Chamseddine & Connes, Resilience of the Spectral Standard Model
-- Ref: [dubois-violette-kerner-madore1990a] Dubois-Violette, Kerner & Madore, Noncommutative differential geometry of matrix algebras
-- Ref: [dubois-violette-kerner-madore1990b] Dubois-Violette, Kerner & Madore, Noncommutative differential geometry and new models of gauge theory
-- Ref: [dabrowski-sitarz2003] Dąbrowski & Sitarz, Dirac operator on the standard Podleś quantum sphere
-- Ref: [klimyk-schmudgen1997] Klimyk & Schmüdgen, Quantum Groups and Their Representations
-- Ref: [sirlin1980] Sirlin, Radiative corrections in the SU(2)_L x U(1) theory
-/

set_option autoImplicit false

namespace QOU.StandardModel
namespace OqSU2HaarYukawaAndPodlesHiggs

open QOU.AlgebraicSubstrate

/-! ## Section 1: Woronowicz Haar Eigenvalues `≡` Jimbo Singlet Yukawa VEV Compression -/

section HaarYukawaUnification

/-- Jimbo crossing matrix `Ř` on `V_{1/2} ⊗ V_{1/2}` (basis `uu, ud, du, dd`) over `[CommRing R]`. -/
def rcJimbo {R : Type*} [CommRing R] (q : Rˣ) : Matrix (Fin 4) (Fin 4) R :=
  let qv : R := q
  let qi : R := ↑q⁻¹
  !![qv, 0, 0, 0; 0, 0, 1, 0; 0, 1, qv - qi, 0; 0, 0, 0, qv]

/-- Tensor-factor swap matrix `P` on `V_{1/2} ⊗ V_{1/2}`. -/
def swapMat4 {R : Type*} [CommRing R] : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0; 0, 0, 1, 0; 0, 1, 0, 0; 0, 0, 0, 1]

/-- Jimbo right-handed singlet projector `P_R = [2]_q⁻¹ (q · I₄ - Ř)` (`matter ⊗ Higgs` order)
over `[CommRing R]` when `qTwo = q + q⁻¹` is a unit `qTwo : Rˣ`. -/
def prJimbo {R : Type*} [CommRing R] (q qTwo : Rˣ) : Matrix (Fin 4) (Fin 4) R :=
  (↑qTwo⁻¹ : R) • ((q : R) • (1 : Matrix (Fin 4) (Fin 4) R) - rcJimbo q)

/-- Strand-flipped Jimbo singlet projector `P_R^flip = [2]_q⁻¹ (q · I₄ - P Ř P)` (`Higgs ⊗ matter`). -/
def prJimboFlip {R : Type*} [CommRing R] (q qTwo : Rˣ) : Matrix (Fin 4) (Fin 4) R :=
  (↑qTwo⁻¹ : R) • ((q : R) • (1 : Matrix (Fin 4) (Fin 4) R) - swapMat4 * rcJimbo q * swapMat4)

/-- Right partial trace `(id ⊗ tr)((1 ⊗ diag(a, b)) · M)` over `[CommRing R]`. -/
def ptrRMat {R : Type*} [CommRing R] (M : Matrix (Fin 4) (Fin 4) R) (a b : R) :
    Matrix (Fin 2) (Fin 2) R :=
  !![a * M 0 0 + b * M 1 1, a * M 0 2 + b * M 1 3;
     a * M 2 0 + b * M 3 1, a * M 2 2 + b * M 3 3]

private lemma prJimbo_explicit {R : Type*} [CommRing R] (q qTwo : Rˣ) :
    prJimbo q qTwo =
      !![0, 0, 0, 0;
         0, (↑qTwo⁻¹ : R) * (q : R), -(↑qTwo⁻¹ : R), 0;
         0, -(↑qTwo⁻¹ : R), (↑qTwo⁻¹ : R) * (↑q⁻¹ : R), 0;
         0, 0, 0, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [prJimbo, rcJimbo]

private lemma prJimboFlip_explicit {R : Type*} [CommRing R] (q qTwo : Rˣ) :
    prJimboFlip q qTwo =
      !![0, 0, 0, 0;
         0, (↑qTwo⁻¹ : R) * (↑q⁻¹ : R), -(↑qTwo⁻¹ : R), 0;
         0, -(↑qTwo⁻¹ : R), (↑qTwo⁻¹ : R) * (q : R), 0;
         0, 0, 0, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [prJimboFlip, swapMat4, rcJimbo]

/-- **Exact Idempotence of the Jimbo Right-Handed Singlet Projector over `[CommRing R]`:**
Whenever `(qTwo : R) = q + q⁻¹`, `prJimbo q qTwo * prJimbo q qTwo = prJimbo q qTwo`. -/
theorem prJimbo_idem {R : Type*} [CommRing R] (q qTwo : Rˣ)
    (hq2 : (qTwo : R) = (q : R) + ↑q⁻¹) :
    prJimbo q qTwo * prJimbo q qTwo = prJimbo q qTwo := by
  have hqi : (q : R) * (↑q⁻¹ : R) = 1 := q.val_inv
  have hq2i : (qTwo : R) * (↑qTwo⁻¹ : R) = 1 := qTwo.val_inv
  rw [prJimbo_explicit]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_four]
  · linear_combination
      -(↑qTwo⁻¹ : R) ^ 2 * hqi - (q : R) * (↑qTwo⁻¹ : R) ^ 2 * hq2 +
        (q : R) * (↑qTwo⁻¹ : R) * hq2i
  · linear_combination (↑qTwo⁻¹ : R) ^ 2 * hq2 - (↑qTwo⁻¹ : R) * hq2i
  · linear_combination (↑qTwo⁻¹ : R) ^ 2 * hq2 - (↑qTwo⁻¹ : R) * hq2i
  · linear_combination
      -(↑qTwo⁻¹ : R) ^ 2 * hqi - (↑q⁻¹ : R) * (↑qTwo⁻¹ : R) ^ 2 * hq2 +
        (↑q⁻¹ : R) * (↑qTwo⁻¹ : R) * hq2i

/-- **Woronowicz Haar–Yukawa VEV Weight Unification & Inverse-Variance Dressing Lock (`[CommRing R]`):**
Let `q, u, qTwo : Rˣ` satisfy `(u : R) = 1 + q²` and `(qTwo : R) = q + q⁻¹`, and let
`h : OqSU2 R q →ₗ[R] R` be any normalized functional (`h 1 = 1`) satisfying Woronowicz's rank-1
Haar relation `(1 + q²) * h(β * γ) = -(q * h 1)`. Then:
1. `h(δ * α) = q² * u⁻¹ = q * qTwo⁻¹ = (prJimbo q qTwo) 1 1 = (prJimboFlip q qTwo) 2 2`;
2. `h(α * δ) = u⁻¹ = q⁻¹ * qTwo⁻¹ = (prJimbo q qTwo) 2 2 = (prJimboFlip q qTwo) 1 1`;
3. `h(δ * α) + h(α * δ) = 1` and `h(δ * α) - h(α * δ) = (q² - 1) * u⁻¹ = (q - q⁻¹) * qTwo⁻¹`;
4. Flavour-blind partial trace `(ptrRMat (prJimbo q qTwo) a b) 0 0 = (...) 1 1` holds **iff**
   `a = q² * b` (matching Woronowicz's KMS modular swap `h(δ * α) = q² * h(α * δ)`);
5. `(qTwo : R)² * (h(δ * α) * h(α * δ)) = 1` (locking the EW Plancherel dressing `[2]_q²` to the
   inverse Woronowicz Haar variance `(h(δα) h(αδ))⁻¹`). -/
theorem haar_eq_jimbo_yukawa_weights_and_variance {R : Type*} [CommRing R]
    (q u qTwo : Rˣ)
    (hu : (u : R) = 1 + (q : R) ^ 2)
    (hq2 : (qTwo : R) = (q : R) + ↑q⁻¹)
    (h : OqSU2 R q →ₗ[R] R)
    (h1 : h 1 = 1)
    (hbg : (1 + (q : R) ^ 2) * h (OqSU2.β q * OqSU2.γ q) = -(q : R) * h 1) :
    let qv : R := q
    let qi : R := ↑q⁻¹
    let ui : R := ↑u⁻¹
    let q2i : R := ↑qTwo⁻¹
    (h (OqSU2.δ q * OqSU2.α q) = qv ^ 2 * ui ∧
      qv ^ 2 * ui = qv * q2i ∧
      prJimbo q qTwo 1 1 = qv * q2i ∧
      prJimboFlip q qTwo 2 2 = qv * q2i) ∧
    (h (OqSU2.α q * OqSU2.δ q) = ui ∧
      ui = qi * q2i ∧
      prJimbo q qTwo 2 2 = qi * q2i ∧
      prJimboFlip q qTwo 1 1 = qi * q2i) ∧
    (h (OqSU2.δ q * OqSU2.α q) + h (OqSU2.α q * OqSU2.δ q) = 1 ∧
      h (OqSU2.δ q * OqSU2.α q) - h (OqSU2.α q * OqSU2.δ q) = (qv ^ 2 - 1) * ui ∧
      (qv ^ 2 - 1) * ui = (qv - qi) * q2i) ∧
    (∀ a b : R,
      ptrRMat (prJimbo q qTwo) a b 0 0 = ptrRMat (prJimbo q qTwo) a b 1 1 ↔ a = qv ^ 2 * b) ∧
    (qTwo : R) ^ 2 * (h (OqSU2.δ q * OqSU2.α q) * h (OqSU2.α q * OqSU2.δ q)) = 1 := by
  intro qv qi ui q2i
  have hqi : qv * qi = 1 := q.val_inv
  have hui : (u : R) * ui = 1 := u.val_inv
  have hq2i : (qTwo : R) * q2i = 1 := qTwo.val_inv
  obtain ⟨hAD, hDA⟩ := OqSU2.haar_cleared_alpha_delta q h hbg
  rw [h1, mul_one, ← hu] at hDA
  rw [h1, ← hu] at hAD
  have h_ad : h (OqSU2.α q * OqSU2.δ q) = ui := by
    linear_combination ui * hAD - h (OqSU2.α q * OqSU2.δ q) * hui
  have h_da : h (OqSU2.δ q * OqSU2.α q) = qv ^ 2 * ui := by
    linear_combination ui * hDA - h (OqSU2.δ q * OqSU2.α q) * hui
  have hu_eq_q_q2 : (u : R) = qv * (qTwo : R) := by
    dsimp only [qv]
    linear_combination hu - (q : R) * hq2 - hqi
  have hui' : qv * (qTwo : R) * ui = 1 := by
    rw [← hu_eq_q_q2]; exact hui
  have hprod : (qv * (qTwo : R)) * (qi * q2i) = 1 := by
    linear_combination (qv * qi) * hq2i + hqi
  have hui_eq : ui = qi * q2i := by
    linear_combination (qi * q2i) * hui' - ui * hprod
  have hqp_eq : qv ^ 2 * ui = qv * q2i := by
    rw [hui_eq]
    linear_combination (qv * q2i) * hqi
  have hpr11 : prJimbo q qTwo 1 1 = qv * q2i := by
    rw [prJimbo_explicit]; dsimp only [qv, q2i]; simp [mul_comm]
  have hprf22 : prJimboFlip q qTwo 2 2 = qv * q2i := by
    rw [prJimboFlip_explicit]; dsimp only [qv, q2i]; simp [mul_comm]
  have hpr22 : prJimbo q qTwo 2 2 = qi * q2i := by
    rw [prJimbo_explicit]; dsimp only [qi, q2i]; simp [mul_comm]
  have hprf11 : prJimboFlip q qTwo 1 1 = qi * q2i := by
    rw [prJimboFlip_explicit]; dsimp only [qi, q2i]; simp [mul_comm]
  have hsum : h (OqSU2.δ q * OqSU2.α q) + h (OqSU2.α q * OqSU2.δ q) = 1 := by
    rw [h_da, h_ad]
    dsimp only [qv, ui]
    linear_combination hui - (↑u⁻¹ : R) * hu
  have hdiff1 : h (OqSU2.δ q * OqSU2.α q) - h (OqSU2.α q * OqSU2.δ q) = (qv ^ 2 - 1) * ui := by
    rw [h_da, h_ad]; ring
  have hdiff2 : (qv ^ 2 - 1) * ui = (qv - qi) * q2i := by
    linear_combination hqp_eq - hui_eq
  refine ⟨⟨h_da, hqp_eq, hpr11, hprf22⟩, ⟨h_ad, hui_eq, hpr22, hprf11⟩,
    ⟨hsum, hdiff1, hdiff2⟩, ?_, ?_⟩
  · intro a b
    have hp0 : prJimbo q qTwo 0 0 = 0 := by rw [prJimbo_explicit]; rfl
    have hp3 : prJimbo q qTwo 3 3 = 0 := by rw [prJimbo_explicit]; rfl
    have hp00 : ptrRMat (prJimbo q qTwo) a b 0 0 = b * (qv ^ 2 * ui) := by
      simp only [ptrRMat, Matrix.of_apply, Matrix.cons_val_zero, hp0, hpr11, mul_zero, zero_add,
        ← hqp_eq]
    have hp11 : ptrRMat (prJimbo q qTwo) a b 1 1 = a * ui := by
      simp only [ptrRMat, Matrix.of_apply, Matrix.cons_val_one, Matrix.cons_val_fin_one, hpr22,
        hp3, mul_zero, add_zero, ← hui_eq]
    rw [hp00, hp11]
    constructor
    · intro heq
      linear_combination -(u : R) * heq - (a - qv ^ 2 * b) * hui
    · intro ha
      rw [ha]; ring
  · rw [h_da, h_ad, hqp_eq, hui_eq]
    linear_combination ((qTwo : R) * q2i) ^ 2 * hqi + ((qTwo : R) * q2i + 1) * hq2i

/-- **Ordered-Ring KMS Symmetry Breaking on Yukawa Strand Order (`1 < q`):**
Over any strict ordered commutative ring `R`, if `1 < (q : R)` and `(u : R) = 1 + q²`, then
`0 < u⁻¹`, `2 * u⁻¹ < 1 < 2 * (q² * u⁻¹)`, and `(prJimbo)_{1,1} - (prJimboFlip)_{1,1} = (q² - 1) u⁻¹ > 0`,
canonically breaking the `matter ⊗ Higgs` vs `Higgs ⊗ matter` tie. -/
theorem haar_kms_breaks_yukawa_order
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (q u : Rˣ) (hu : (u : R) = 1 + (q : R) ^ 2) (hq : (1 : R) < (q : R)) :
    let qv : R := q
    let ui : R := ↑u⁻¹
    0 < ui ∧ 2 * ui < 1 ∧ 1 < 2 * (qv ^ 2 * ui) ∧ 0 < (qv ^ 2 - 1) * ui := by
  intro qv ui
  have hui : (u : R) * ui = 1 := u.val_inv
  have hqv_pos : 0 < qv := lt_trans zero_lt_one hq
  have hq2_gt1 : 1 < qv ^ 2 := by
    have h1 : 1 * qv < qv * qv := mul_lt_mul_of_pos_right hq hqv_pos
    linarith
  have hu_pos : 0 < (u : R) := by linarith
  have hui_pos : 0 < ui := by
    by_contra hle
    push_neg at hle
    have hnp : (u : R) * ui ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hu_pos.le hle
    linarith
  have h2ui_lt1 : 2 * ui < 1 := by
    have h2_lt_u : (2 : R) < (u : R) := by linarith
    have hm : 2 * ui < (u : R) * ui := mul_lt_mul_of_pos_right h2_lt_u hui_pos
    linarith
  have h1_lt_2p : 1 < 2 * (qv ^ 2 * ui) := by
    have hu_lt_2q2 : (u : R) < 2 * qv ^ 2 := by linarith
    have hm : (u : R) * ui < (2 * qv ^ 2) * ui := mul_lt_mul_of_pos_right hu_lt_2q2 hui_pos
    linarith
  exact ⟨hui_pos, h2ui_lt1, h1_lt_2p, mul_pos (by linarith) hui_pos⟩

end HaarYukawaUnification

/-! ## Section 2: Podleś Sphere `S²_q` & Hajac–Majid `q`-Monopole Higgs Projector -/

section PodlesMonopoleProjector

variable {R : Type*} [CommRing R]

private lemma compactStar_gen (q : Rˣ) :
    OqSU2.compactStar q (OqSU2.α (R := R) q) = OqSU2.δ q ∧
    OqSU2.compactStar q (OqSU2.β (R := R) q) = -(q : R) • OqSU2.γ q ∧
    OqSU2.compactStar q (OqSU2.γ (R := R) q) = -(((q⁻¹ : Rˣ) : R)) • OqSU2.β q ∧
    OqSU2.compactStar q (OqSU2.δ (R := R) q) = OqSU2.α q := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp [OqSU2.compactStar, OqSU2.compactStarOpAlgEquiv, OqSU2.compactStarToOpAlgHom]

/-- `U(1)`-charge-`(+1)` Hopf spinor column `v = (α, γ)^T` in `OqSU2 R q`. -/
noncomputable def hopfCol (q : Rˣ) : Fin 2 → OqSU2 R q :=
  ![OqSU2.α q, OqSU2.γ q]

/-- `U(1)`-charge-`(-1)` adjoint spinor row `v^* = (δ, -q⁻¹ β)` (`= (α^*, γ^*)`) in `OqSU2 R q`. -/
noncomputable def hopfRow (q : Rˣ) : Fin 2 → OqSU2 R q :=
  ![OqSU2.δ q, -(((q⁻¹ : Rˣ) : R)) • OqSU2.β q]

/-- Hajac–Majid / Podleś `2 × 2` rank-1 `q`-monopole projector `e_Podleś = v ⊗ v^* ∈ M₂(OqSU2 R q)`. -/
noncomputable def podlesProj (q : Rˣ) : Matrix (Fin 2) (Fin 2) (OqSU2 R q) :=
  Matrix.of fun i j => hopfCol q i * hopfRow q j

private lemma neg_smul_oqsu2 (q : Rˣ) (r : R) (x : OqSU2 R q) :
    (-r) • x = -(r • x) := by
  have h : ((-r) + r) • x = 0 := by rw [neg_add_cancel, zero_smul]
  rw [add_smul] at h
  exact eq_neg_of_add_eq_zero_left h

/-- **Noncommutative Nonlinear-`σ` Sphere Normalization (`v^* · v = δ α - q⁻¹ β γ = 1`):**
Over every `[CommRing R]`, `hopfRow q` and `hopfCol q` form a unit-normalized point/copoint pair. -/
theorem hopfRow_dot_hopfCol_eq_one (q : Rˣ) :
    hopfRow (R := R) q 0 * hopfCol q 0 + hopfRow q 1 * hopfCol q 1 = 1 := by
  simp only [hopfRow, hopfCol, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_fin_one]
  rw [Algebra.smul_mul_assoc, neg_smul_oqsu2, ← sub_eq_add_neg]
  exact OqSU2.rel_det_right q

/-- **Exact Idempotence & Vacuum-Residual Orthogonality of `podlesProj` over `[CommRing R]`:**
`e_Podleś * e_Podleś = e_Podleś`, `(1 - e_Podleś) * (1 - e_Podleś) = 1 - e_Podleś`, and
`e_Podleś * (1 - e_Podleś) = 0`. -/
theorem podlesProj_idem_and_resid (q : Rˣ) :
    podlesProj (R := R) q * podlesProj q = podlesProj q ∧
    (1 - podlesProj (R := R) q) * (1 - podlesProj q) = 1 - podlesProj q ∧
    podlesProj (R := R) q * (1 - podlesProj q) = 0 := by
  have hnorm := hopfRow_dot_hopfCol_eq_one (R := R) q
  have hidem : podlesProj (R := R) q * podlesProj q = podlesProj q := by
    ext i k
    rw [Matrix.mul_apply, Fin.sum_univ_two]
    simp only [podlesProj, Matrix.of_apply]
    calc
      hopfCol q i * hopfRow q 0 * (hopfCol q 0 * hopfRow q k) +
          hopfCol q i * hopfRow q 1 * (hopfCol q 1 * hopfRow q k)
        = hopfCol q i * (hopfRow q 0 * hopfCol q 0 + hopfRow q 1 * hopfCol q 1) * hopfRow q k := by
            simp only [mul_add, add_mul, mul_assoc]
      _ = hopfCol q i * 1 * hopfRow q k := by rw [hnorm]
      _ = hopfCol q i * hopfRow q k := by rw [mul_one]
  have horth : podlesProj (R := R) q * (1 - podlesProj q) = 0 := by
    rw [mul_sub, mul_one, hidem, sub_self]
  have hres : (1 - podlesProj (R := R) q) * (1 - podlesProj q) = 1 - podlesProj q := by
    rw [sub_mul, one_mul, mul_sub, mul_one, hidem]
    abel
  exact ⟨hidem, hres, horth⟩

/-- **Exact `compactStar`-Hermiticity of `podlesProj` (`(e_{ij})^* = e_{ji}`):**
Every matrix entry satisfies `compactStar q (podlesProj q i j) = podlesProj q j i`. -/
theorem podlesProj_compactStar_hermitian (q : Rˣ) (i j : Fin 2) :
    OqSU2.compactStar q (podlesProj (R := R) q i j) = podlesProj q j i := by
  have hcs := compactStar_gen (R := R) q
  have hcol_star : ∀ k : Fin 2, OqSU2.compactStar q (hopfCol (R := R) q k) = hopfRow q k := by
    intro k; fin_cases k
    · exact hcs.1
    · exact hcs.2.2.1
  have hrow_star : ∀ k : Fin 2, OqSU2.compactStar q (hopfRow (R := R) q k) = hopfCol q k := by
    intro k
    rw [← hcol_star k, OqSU2.compactStar_involutive]
  simp only [podlesProj, Matrix.of_apply, OqSU2.compactStar_mul, hcol_star, hrow_star]

/-- **Exact `U(1)` Gauge Invariance (`podlesProj` Descends to Podleś Sphere `O(S²_q)`):**
Under right `U(1)` character scaling `torusScaleAlgHom q v v⁻¹ : (α, β, γ, δ) ↦ (vα, v⁻¹β, vγ, v⁻¹δ)`,
`hopfCol` transforms with charge `+1`, `hopfRow` with charge `-1`, and every entry of `podlesProj`
is strictly fixed for all `v : Rˣ`. -/
theorem podlesProj_u1_invariant (q v : Rˣ) (i j : Fin 2) :
    OqSU2.torusScaleAlgHom q v v⁻¹ (hopfCol (R := R) q i) = (v : R) • hopfCol q i ∧
    OqSU2.torusScaleAlgHom q v v⁻¹ (hopfRow (R := R) q j) = (((v⁻¹ : Rˣ) : R)) • hopfRow q j ∧
    OqSU2.torusScaleAlgHom q v v⁻¹ (podlesProj (R := R) q i j) = podlesProj q i j := by
  have hcol : ∀ k : Fin 2,
      OqSU2.torusScaleAlgHom q v v⁻¹ (hopfCol (R := R) q k) = (v : R) • hopfCol q k := by
    intro k; fin_cases k <;> simp [hopfCol, OqSU2.torusScaleAlgHom]
  have hrow : ∀ k : Fin 2,
      OqSU2.torusScaleAlgHom q v v⁻¹ (hopfRow (R := R) q k) =
        (((v⁻¹ : Rˣ) : R)) • hopfRow q k := by
    intro k; fin_cases k
    · simp [hopfRow, OqSU2.torusScaleAlgHom]
    · simp [hopfRow, OqSU2.torusScaleAlgHom, smul_smul, mul_comm]
  refine ⟨hcol i, hrow j, ?_⟩
  simp only [podlesProj, Matrix.of_apply, map_mul, hcol i, hrow j,
    Algebra.smul_mul_assoc, Algebra.mul_smul_comm, smul_smul, Units.inv_mul, one_smul]

/-- **Quantum Pivotal Trace `= 1` vs Classical Trace & Determinant Symmetry-Breaking Defects:**
Over every `[CommRing R]`:
1. **Quantum pivotal trace (`= 1`):** `e_{00} + q² • e_{11} = α δ - q β γ = 1` (realizing
   `VacuumPairing.tr_proj_eq_one` noncommutatively);
2. **Ordinary matrix trace defect:** `e_{00} + e_{11} = 1 + (q - q⁻¹) • (β γ)`;
3. **Classical vs quantum determinant defect:** `1 - (α δ - β γ) = -((q - 1) • (β γ))`;
4. Under Woronowicz's Haar state (`h 1 = 1`, `(1 + q²) h(βγ) = -q h 1`), with `(u : R) = 1 + q²`
   and `(qTwo : R) = q + q⁻¹`:
   `1 - h(e_{00} + e_{11}) = (q² - 1) * u⁻¹` (KMS asymmetry) and
   `h(1 - (α δ - β γ)) = (q - 1) * qTwo⁻¹` (classical determinant defect). -/
theorem podlesProj_quantum_trace_eq_one_and_defects
    (q u qTwo : Rˣ)
    (hu : (u : R) = 1 + (q : R) ^ 2)
    (hq2 : (qTwo : R) = (q : R) + ↑q⁻¹)
    (h : OqSU2 R q →ₗ[R] R)
    (h1 : h 1 = 1)
    (hbg : (1 + (q : R) ^ 2) * h (OqSU2.β q * OqSU2.γ q) = -(q : R) * h 1) :
    podlesProj (R := R) q 0 0 + ((q : R) ^ 2) • podlesProj q 1 1 = 1 ∧
    podlesProj (R := R) q 0 0 + podlesProj q 1 1 =
      1 + ((q : R) - ↑q⁻¹) • (OqSU2.β q * OqSU2.γ q) ∧
    1 - (OqSU2.α (R := R) q * OqSU2.δ q - OqSU2.β q * OqSU2.γ q) =
      -(((q : R) - 1) • (OqSU2.β q * OqSU2.γ q)) ∧
    1 - h (podlesProj q 0 0 + podlesProj q 1 1) = ((q : R) ^ 2 - 1) * (↑u⁻¹ : R) ∧
    h (1 - (OqSU2.α q * OqSU2.δ q - OqSU2.β q * OqSU2.γ q)) =
      ((q : R) - 1) * (↑qTwo⁻¹ : R) := by
  have hqi : (q : R) * (↑q⁻¹ : R) = 1 := q.val_inv
  have hui : (u : R) * (↑u⁻¹ : R) = 1 := u.val_inv
  have hq2i : (qTwo : R) * (↑qTwo⁻¹ : R) = 1 := qTwo.val_inv
  have he00 : podlesProj (R := R) q 0 0 = OqSU2.α q * OqSU2.δ q := by
    simp [podlesProj, hopfCol, hopfRow]
  have he11 : podlesProj (R := R) q 1 1 = -((((q⁻¹ : Rˣ) : R)) • (OqSU2.β q * OqSU2.γ q)) := by
    change hopfCol q 1 * hopfRow q 1 = _
    simp only [hopfCol, hopfRow, Matrix.cons_val_one, Matrix.cons_val_fin_one]
    rw [Algebra.mul_smul_comm, ← OqSU2.rel_bg, neg_smul_oqsu2]
  have hq2_qi : ((q : R) ^ 2) * (↑q⁻¹ : R) = (q : R) := by
    linear_combination (q : R) * hqi
  have htr_q : podlesProj (R := R) q 0 0 + ((q : R) ^ 2) • podlesProj q 1 1 = 1 := by
    rw [he00, he11, smul_neg, smul_smul, hq2_qi, ← sub_eq_add_neg]
    exact OqSU2.rel_det_left q
  have had_eq : OqSU2.α (R := R) q * OqSU2.δ q = 1 + (q : R) • (OqSU2.β q * OqSU2.γ q) := by
    rw [← OqSU2.rel_det_left q]; abel
  have htr_cl : podlesProj (R := R) q 0 0 + podlesProj q 1 1 =
      1 + ((q : R) - ↑q⁻¹) • (OqSU2.β q * OqSU2.γ q) := by
    rw [he00, he11, had_eq]
    simp only [Algebra.smul_def, map_sub, sub_mul]
    abel
  have hdet_def : 1 - (OqSU2.α (R := R) q * OqSU2.δ q - OqSU2.β q * OqSU2.γ q) =
      -(((q : R) - 1) • (OqSU2.β q * OqSU2.γ q)) := by
    rw [had_eq]
    simp only [Algebra.smul_def, map_sub, map_one, sub_mul, one_mul]
    abel
  have hbg' : (u : R) * h (OqSU2.β q * OqSU2.γ q) = -(q : R) := by
    rw [h1, mul_one, ← hu] at hbg
    exact hbg
  have hbg_val : h (OqSU2.β q * OqSU2.γ q) = -(q : R) * (↑u⁻¹ : R) := by
    linear_combination (↑u⁻¹ : R) * hbg' - h (OqSU2.β q * OqSU2.γ q) * hui
  have hu_eq_q_q2 : (u : R) = (q : R) * (qTwo : R) := by
    linear_combination hu - (q : R) * hq2 - hqi
  have hui' : (q : R) * (qTwo : R) * (↑u⁻¹ : R) = 1 := by
    rw [← hu_eq_q_q2]; exact hui
  have hqp_eq : (q : R) * (↑u⁻¹ : R) = (↑qTwo⁻¹ : R) := by
    linear_combination (↑qTwo⁻¹ : R) * hui' - ((q : R) * (↑u⁻¹ : R)) * hq2i
  refine ⟨htr_q, htr_cl, hdet_def, ?_, ?_⟩
  · rw [htr_cl, map_add, h1, map_smul, smul_eq_mul, hbg_val]
    linear_combination -(↑u⁻¹ : R) * hqi
  · rw [hdet_def, map_neg, map_smul, smul_eq_mul, hbg_val]
    linear_combination ((q : R) - 1) * hqp_eq

end PodlesMonopoleProjector

/-! ## Section 3: Podleś Kurtosis `[2]_q² / [3]_q`, `v²`-Cancellation, & Jucys–Murphy Bounds -/

section PodlesKurtosisAndJucysMurphy

/-- **Cleared Podleś Radial Kurtosis Identity (`h((γ*γ)²) / h(γ*γ)² = [2]_q² / [3]_q < 4 / 3`):**
Over every `[CommRing R]` and unit `q : Rˣ`, with `q2 = q + q⁻¹`, `q3 = q² + 1 + q⁻²`, and
`h = q - q⁻¹`:
1. `(1 + q²)² = q² · q2²` and `1 + q² + q⁴ = q² · q3`;
2. `q3 · (1 + q²)² = q2² · (1 + q² + q⁴)` (cleared `h((γ*γ)²) / h(γ*γ)² = [2]_q² / [3]_q`);
3. `q2² = 4 + h²`, `q3 = 3 + h²`, and `4 * q3 - 3 * q2² = h²` (hence at `q = 1` the ratio equals
   Chamseddine–Connes' `4 / 3`, and for `h ≠ 0` in an ordered ring `[2]_q² / [3]_q < 4 / 3`). -/
theorem podles_radial_kurtosis_identities {R : Type*} [CommRing R] (q : Rˣ) :
    let qv : R := q
    let qi : R := ↑q⁻¹
    let q2 : R := qv + qi
    let q3 : R := qv ^ 2 + 1 + qi ^ 2
    let hv : R := qv - qi
    (1 + qv ^ 2) ^ 2 = qv ^ 2 * q2 ^ 2 ∧
    1 + qv ^ 2 + qv ^ 4 = qv ^ 2 * q3 ∧
    q3 * (1 + qv ^ 2) ^ 2 = q2 ^ 2 * (1 + qv ^ 2 + qv ^ 4) ∧
    q2 ^ 2 = 4 + hv ^ 2 ∧
    q3 = 3 + hv ^ 2 ∧
    4 * q3 - 3 * q2 ^ 2 = hv ^ 2 := by
  intro qv qi q2 q3 hv
  have hqi : qv * qi = 1 := q.val_inv
  have h1 : (1 + qv ^ 2) ^ 2 = qv ^ 2 * q2 ^ 2 := by
    dsimp only [q2]
    linear_combination (-2 * qv ^ 2 - qv * qi - 1) * hqi
  have h2 : 1 + qv ^ 2 + qv ^ 4 = qv ^ 2 * q3 := by
    dsimp only [q3]
    linear_combination (-qv * qi - 1) * hqi
  have h3 : q3 * (1 + qv ^ 2) ^ 2 = q2 ^ 2 * (1 + qv ^ 2 + qv ^ 4) := by
    rw [h1, h2]; ring
  have h4 : q2 ^ 2 = 4 + hv ^ 2 := by
    dsimp only [q2, hv]
    linear_combination 4 * hqi
  have h5 : q3 = 3 + hv ^ 2 := by
    dsimp only [q3, hv]
    linear_combination 2 * hqi
  refine ⟨h1, h2, h3, h4, h5, ?_⟩
  rw [h4, h5]; ring

/-- **Universal Cleared `v²`-Cancellation Identity (`λ_H = m_H² / (2 v²)`):**
Over any `[CommRing R]`, whenever `mW_sq * denom = piAlpha * vSq` and `mH_sq = mW_sq * ratioSq`,
`(2 * denom) * mH_sq = (2 * vSq) * (piAlpha * ratioSq)`, cancelling `vSq` symmetrically across both
Chamseddine–Connes spectral-action and QOU Plancherel quartic formulas. -/
theorem higgs_quartic_cleared_vev_cancellation {R : Type*} [CommRing R]
    (mW_sq mH_sq piAlpha vSq denom ratioSq : R)
    (hmW : mW_sq * denom = piAlpha * vSq)
    (hmH : mH_sq = mW_sq * ratioSq) :
    (2 * denom) * mH_sq = (2 * vSq) * (piAlpha * ratioSq) := by
  rw [hmH]
  linear_combination (2 * ratioSq) * hmW

/-- **Jucys–Murphy `H₃` / `H₄` Content Traces & Strict Separation `[2]_q [3]_q > 6` (`1 < q`):**
1. Over any `[CommRing R]` and `q : Rˣ`, multiplicative Jucys–Murphy eigenvalues `q^{2 c(x)}` sum
   to `[3]_q` on `H₃` standard `(2,1)` (`contents = (0, 1, -1)`) and to `[2]_q²` on `H₄` `(2,2)`
   (`contents = (0, 1, -1, 0)`), with unit products;
2. Over any strict ordered commutative ring with `1 < (q : R)`, `[2]_q > 2`, `[3]_q > 3`, and
   `5 * ([2]_q * [3]_q) > 5 * 6` (`[2]_q [3]_q / 5 > 6 / 5`), separating the quantum factorial
   from the undeformed topological rank ratio `dim H₃ / dim Z(H₄) = 6 / 5`. -/
theorem jm_h3_h4_traces_and_qfactorial_gt_six
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : Rˣ) (hq : (1 : R) < (q : R)) :
    let qv : R := q
    let qi : R := ↑q⁻¹
    let q2 : R := qv + qi
    let q3 : R := qv ^ 2 + 1 + qi ^ 2
    (1 + qv ^ 2 + qi ^ 2 = q3 ∧ 1 * qv ^ 2 * qi ^ 2 = 1) ∧
    (1 + qv ^ 2 + qi ^ 2 + 1 = q2 ^ 2) ∧
    (2 < q2 ∧ 3 < q3 ∧ 6 < q2 * q3 ∧ 5 * 6 < 5 * (q2 * q3)) := by
  intro qv qi q2 q3
  have hqi : qv * qi = 1 := q.val_inv
  have hqv_pos : 0 < qv := lt_trans zero_lt_one hq
  have hqi_pos : 0 < qi := by
    by_contra hle
    push_neg at hle
    have hnp : qv * qi ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hqv_pos.le hle
    linarith
  have hqi_lt1 : qi < 1 := by
    have hm : 1 * qi < qv * qi := mul_lt_mul_of_pos_right hq hqi_pos
    linarith
  have hh_pos : 0 < qv - qi := by linarith
  have hh2_pos : 0 < (qv - qi) ^ 2 := by
    rw [sq]
    exact mul_pos hh_pos hh_pos
  have hq2_sub2 : q2 - 2 = (qv - 1) * (1 - qi) := by
    dsimp only [q2]
    linear_combination hqi
  have hq2_gt2 : 2 < q2 := by
    have hp : 0 < (qv - 1) * (1 - qi) := mul_pos (by linarith) (by linarith)
    linarith
  have hq3_eq : q3 = 3 + (qv - qi) ^ 2 := (podles_radial_kurtosis_identities q).2.2.2.2.1
  have hq3_gt3 : 3 < q3 := by linarith
  have hprod_gt6 : 6 < q2 * q3 := by
    have h1 : 2 * 3 < q2 * 3 := mul_lt_mul_of_pos_right hq2_gt2 (by norm_num)
    have h2 : q2 * 3 < q2 * q3 := mul_lt_mul_of_pos_left hq3_gt3 (by linarith)
    linarith
  refine ⟨⟨by dsimp only [q3]; ring, by linear_combination (qv * qi + 1) * hqi⟩, ?_,
    ⟨hq2_gt2, hq3_gt3, hprod_gt6, by linarith⟩⟩
  dsimp only [q2]
  linear_combination -2 * hqi

end PodlesKurtosisAndJucysMurphy

end OqSU2HaarYukawaAndPodlesHiggs
end QOU.StandardModel
