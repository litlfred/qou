import MathlibExt.SL2ChebyshevTrace
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# Borromean `V³` Mixed-Symmetry Trace, Pivotal Flavour Weight Split, and Pure-Braid Diagnostic

Over an arbitrary field `R`, commutative ring, ordered field `K`, and `ℚ` (§7c generic base-ring
discipline, zero `ℝ`), this module unifies the `H₃(q)` Temperley–Lieb / Hecke `(2, 1)` sector,
the `3 + 3` nucleon weight-space intertwiner, the pivotal Reshetikhin–Turaev quantum trace
(`ε_flav`), Cautis–Kamnitzer–Morrison skew-Howe `q ↦ -q⁻¹` invariance, and the pure-braid
commutator `[A₁₂, A₁₃]`, together with both halves of the elliptic/hyperbolic boundedness
diagnostic.

Historical credits:
- Tadashi Nakayama (1939), *On Frobeniusean algebras I*
- David E. Radford (1976), *The order of the antipode of a finite dimensional Hopf algebra is finite*
- Michio Jimbo (1986), *A q-analogue of U(gl(N+1)), Hecke algebra, and the Yang–Baxter equation*
- Stanisław Lech Woronowicz (1987), *Compact matrix pseudogroups*
- Nicolai Yu. Reshetikhin & Vladimir G. Turaev (1990), *Ribbon graphs and their invariants derived from quantum groups*
- Saburo Cautis, Joel Kamnitzer & Scott Morrison (2014), *Webs and quantum skew Howe duality*

-- Ref: [nakayama1939]
-- Ref: [jimbo1986]
-- Ref: [woronowicz1987]
-- Ref: [reshetikhin-turaev1990]
-/

namespace QOU.QBeta.BorromeanFlavourPivotalUnification

open Matrix
open QOU.MathlibInfra.SL2ChebyshevTrace

/-! ## 1. Temperley–Lieb / Hecke `(2, 1)` `2 × 2` Representation and Braid Relations -/

section Hecke21

variable {R : Type*} [Field R]

/-- Temperley–Lieb generator `e₀ = !![q + q⁻¹, 1; 0, 0]` on the 2D `(2, 1)` sector. -/
def tl_e0 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  !![q + q⁻¹, 1; 0, 0]

/-- Temperley–Lieb generator `e₁ = !![0, 0; 1, q + q⁻¹]` on the 2D `(2, 1)` sector. -/
def tl_e1 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  !![0, 0; 1, q + q⁻¹]

/-- Hecke generator `σ₀ = q • 1 - e₀` on `Matrix (Fin 2) (Fin 2) R`. -/
def rho21_sigma0 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  q • (1 : Matrix (Fin 2) (Fin 2) R) - tl_e0 q

/-- Hecke generator `σ₁ = q • 1 - e₁` on `Matrix (Fin 2) (Fin 2) R`. -/
def rho21_sigma1 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  q • (1 : Matrix (Fin 2) (Fin 2) R) - tl_e1 q

/-- Inverse Hecke generator `σ₀⁻¹ = q⁻¹ • 1 - e₀` on `Matrix (Fin 2) (Fin 2) R`. -/
def rho21_sigma0_inv (q : R) : Matrix (Fin 2) (Fin 2) R :=
  q⁻¹ • (1 : Matrix (Fin 2) (Fin 2) R) - tl_e0 q

/-- Inverse Hecke generator `σ₁⁻¹ = q⁻¹ • 1 - e₁` on `Matrix (Fin 2) (Fin 2) R`. -/
def rho21_sigma1_inv (q : R) : Matrix (Fin 2) (Fin 2) R :=
  q⁻¹ • (1 : Matrix (Fin 2) (Fin 2) R) - tl_e1 q

/-- Explicit `2 × 2` matrix form of `ρ_{(2,1)}(σ₀) = !![-q⁻¹, -1; 0, q]`. -/
theorem rho21_sigma0_eq (q : R) :
    rho21_sigma0 q = !![-q⁻¹, -1; 0, q] := by
  ext i j
  fin_cases i <;> fin_cases j <;> (simp [rho21_sigma0, tl_e0]; try ring)

/-- Explicit `2 × 2` matrix form of `ρ_{(2,1)}(σ₁) = !![q, 0; -1, -q⁻¹]`. -/
theorem rho21_sigma1_eq (q : R) :
    rho21_sigma1 q = !![q, 0; -1, -q⁻¹] := by
  ext i j
  fin_cases i <;> fin_cases j <;> (simp [rho21_sigma1, tl_e1]; try ring)

/-- Explicit `2 × 2` matrix form of `ρ_{(2,1)}(σ₀⁻¹) = !![-q, -1; 0, q⁻¹]`. -/
theorem rho21_sigma0_inv_eq (q : R) :
    rho21_sigma0_inv q = !![-q, -1; 0, q⁻¹] := by
  ext i j
  fin_cases i <;> fin_cases j <;> (simp [rho21_sigma0_inv, tl_e0]; try ring)

/-- Explicit `2 × 2` matrix form of `ρ_{(2,1)}(σ₁⁻¹) = !![q⁻¹, 0; -1, -q]`. -/
theorem rho21_sigma1_inv_eq (q : R) :
    rho21_sigma1_inv q = !![q⁻¹, 0; -1, -q] := by
  ext i j
  fin_cases i <;> fin_cases j <;> (simp [rho21_sigma1_inv, tl_e1]; try ring)

/-- **Braid Relation on `S^{(2,1)}`:** `σ₀ * σ₁ * σ₀ = σ₁ * σ₀ * σ₁` for `q ≠ 0`. -/
theorem rho21_braid_rel {q : R} (hq : q ≠ 0) :
    rho21_sigma0 q * rho21_sigma1 q * rho21_sigma0 q =
      rho21_sigma1 q * rho21_sigma0 q * rho21_sigma1 q := by
  rw [rho21_sigma0_eq, rho21_sigma1_eq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp only [Matrix.mul_fin_two, Matrix.of_apply];
      field_simp; try ring)

/-- **Hecke Quadratic Relation for `σ₀`:** `(σ₀ - q • 1) * (σ₀ + q⁻¹ • 1) = 0`. -/
theorem rho21_hecke_quad_sigma0 (q : R) :
    (rho21_sigma0 q - q • (1 : Matrix (Fin 2) (Fin 2) R)) *
      (rho21_sigma0 q + q⁻¹ • (1 : Matrix (Fin 2) (Fin 2) R)) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [rho21_sigma0, tl_e0, Matrix.mul_apply, Fin.sum_univ_two]; try ring)

/-- **Hecke Quadratic Relation for `σ₁`:** `(σ₁ - q • 1) * (σ₁ + q⁻¹ • 1) = 0`. -/
theorem rho21_hecke_quad_sigma1 (q : R) :
    (rho21_sigma1 q - q • (1 : Matrix (Fin 2) (Fin 2) R)) *
      (rho21_sigma1 q + q⁻¹ • (1 : Matrix (Fin 2) (Fin 2) R)) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [rho21_sigma1, tl_e1, Matrix.mul_apply, Fin.sum_univ_two]; try ring)

/-- Invertibility `σ₀ * σ₀⁻¹ = 1` and `σ₀⁻¹ * σ₀ = 1` for `q ≠ 0`. -/
theorem rho21_sigma0_mul_inv {q : R} (hq : q ≠ 0) :
    rho21_sigma0 q * rho21_sigma0_inv q = 1 ∧
      rho21_sigma0_inv q * rho21_sigma0 q = 1 := by
  rw [rho21_sigma0_eq, rho21_sigma0_inv_eq]
  refine ⟨?_, ?_⟩ <;>
    (ext i j;
      fin_cases i <;> fin_cases j <;>
        (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp))

/-- Invertibility `σ₁ * σ₁⁻¹ = 1` and `σ₁⁻¹ * σ₁ = 1` for `q ≠ 0`. -/
theorem rho21_sigma1_mul_inv {q : R} (hq : q ≠ 0) :
    rho21_sigma1 q * rho21_sigma1_inv q = 1 ∧
      rho21_sigma1_inv q * rho21_sigma1 q = 1 := by
  rw [rho21_sigma1_eq, rho21_sigma1_inv_eq]
  refine ⟨?_, ?_⟩ <;>
    (ext i j;
      fin_cases i <;> fin_cases j <;>
        (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp))

/-! ## 2. Borromean Step `V = σ₀ σ₁⁻¹`, `SL₂` Cayley–Hamilton Evaluation, and `P(q)` -/

/-- Single Borromean period `V = σ₀ * σ₁⁻¹` on the 2D `(2, 1)` representation. -/
def rho21_V (q : R) : Matrix (Fin 2) (Fin 2) R :=
  rho21_sigma0 q * rho21_sigma1_inv q

/-- **`V ∈ SL₂`:** `det(ρ_{(2,1)}(V)) = 1` for every `q ≠ 0`. -/
theorem det_V_21 {q : R} (hq : q ≠ 0) :
    (rho21_V q).det = 1 := by
  unfold rho21_V
  rw [rho21_sigma0_eq, rho21_sigma1_inv_eq]
  simp [Matrix.det_fin_two]
  field_simp
  ring

/-- **Trace of `V` on `S^{(2,1)}`:** `tr(ρ_{(2,1)}(V)) = -(1 + (q - q⁻¹)²)`. -/
theorem tr_V_21 {q : R} (hq : q ≠ 0) :
    (rho21_V q).trace = -(1 + (q - q⁻¹) ^ 2) := by
  unfold rho21_V
  rw [rho21_sigma0_eq, rho21_sigma1_inv_eq]
  simp [Matrix.trace_fin_two]
  field_simp
  ring

/-- **3-Line Cayley–Hamilton Evaluation of `tr(V³)` on `S^{(2,1)}`:**
`tr(ρ_{(2,1)}(V)³) = 2 - 3 * (q - q⁻¹)⁴ - (q - q⁻¹)⁶`. -/
theorem tr_V3_21 {q : R} (hq : q ≠ 0) :
    (rho21_V q ^ 3).trace = 2 - 3 * (q - q⁻¹) ^ 4 - (q - q⁻¹) ^ 6 := by
  rw [trace_cube_of_det_eq_one (det_V_21 hq), tr_V_21 hq]
  ring

/-- Full 3D nucleon weight-space trace `tr_W(V³) = 1 + tr_{(2,1)}(V³)` combining the 1D
zero-writhe `S^{(3)}` eigenvalue `q^0 = 1` with `S^{(2,1)}`. -/
def trW_V3 (q : R) : R :=
  1 + (rho21_V q ^ 3).trace

/-- Degree-12 palindromic Borromean polynomial
`P_poly(q) = q¹² - 3 q¹⁰ + 3 q⁸ - 5 q⁶ + 3 q⁴ - 3 q² + 1`. -/
def P_poly (q : R) : R :=
  q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1

/-- **Unification of `tr_W(V³)` with `-q⁻⁶ P_poly(q)`:**
`tr_W(V³) = 3 - 3 * (q - q⁻¹)⁴ - (q - q⁻¹)⁶ = -q⁻¹ ^ 6 * P_poly(q)`. -/
theorem tr_W_V3_eq_P_poly {q : R} (hq : q ≠ 0) :
    trW_V3 q = 3 - 3 * (q - q⁻¹) ^ 4 - (q - q⁻¹) ^ 6 ∧
      3 - 3 * (q - q⁻¹) ^ 4 - (q - q⁻¹) ^ 6 = -q⁻¹ ^ 6 * P_poly q := by
  refine ⟨?_, ?_⟩
  · unfold trW_V3
    rw [tr_V3_21 hq]
    ring
  · unfold P_poly
    field_simp
    ring

/-! ## 3. Weight-Space Intertwiner Equality and Pivotal Reshetikhin–Turaev `ε_flav(V³)` -/

/-- **Intertwiner Trace Equality (`W_uud ≃ₗ W_udd`):**
Over any commutative ring `S`, if an `S`-linear isomorphism `e : (ι₁ → S) ≃ₗ[S] (ι₂ → S)`
(in particular `Fin 3 → S` for the 3D `uud` and `udd` weight spaces) intertwines `T_uud` and
`T_udd` (`e ∘ T_uud = T_udd ∘ e`), then `T_uud` and `T_udd` have identical trace. -/
theorem tr_uud_eq_tr_udd_of_intertwiner {S : Type*} [CommRing S]
    {ι₁ ι₂ : Type*} [Fintype ι₁] [DecidableEq ι₁] [Fintype ι₂] [DecidableEq ι₂]
    (e : (ι₁ → S) ≃ₗ[S] (ι₂ → S))
    (T_uud : Module.End S (ι₁ → S)) (T_udd : Module.End S (ι₂ → S))
    (h_inter : e.toLinearMap.comp T_uud = T_udd.comp e.toLinearMap) :
    (LinearMap.toMatrix' T_uud).trace = (LinearMap.toMatrix' T_udd).trace := by
  let E : Matrix ι₂ ι₁ S := LinearMap.toMatrix' e.toLinearMap
  let E_inv : Matrix ι₁ ι₂ S := LinearMap.toMatrix' e.symm.toLinearMap
  let M_uud : Matrix ι₁ ι₁ S := LinearMap.toMatrix' T_uud
  let M_udd : Matrix ι₂ ι₂ S := LinearMap.toMatrix' T_udd
  have hEE : E * E_inv = 1 := by
    dsimp [E, E_inv]
    rw [← LinearMap.toMatrix'_comp, e.comp_symm, LinearMap.toMatrix'_id]
  have hEinvE : E_inv * E = 1 := by
    dsimp [E, E_inv]
    rw [← LinearMap.toMatrix'_comp, e.symm_comp, LinearMap.toMatrix'_id]
  have hEM : E * M_uud = M_udd * E := by
    dsimp [E, M_uud, M_udd]
    rw [← LinearMap.toMatrix'_comp, ← LinearMap.toMatrix'_comp, h_inter]
  calc
    M_uud.trace = (1 * M_uud).trace := by rw [Matrix.one_mul]
    _ = ((E_inv * E) * M_uud).trace := by rw [hEinvE]
    _ = (E_inv * (E * M_uud)).trace := by rw [Matrix.mul_assoc]
    _ = ((E * M_uud) * E_inv).trace := Matrix.trace_mul_comm E_inv (E * M_uud)
    _ = ((M_udd * E) * E_inv).trace := by rw [hEM]
    _ = (M_udd * (E * E_inv)).trace := by rw [Matrix.mul_assoc]
    _ = (M_udd * 1).trace := by rw [hEE]
    _ = M_udd.trace := by rw [Matrix.mul_one]

/-- **Pivotal Reshetikhin–Turaev Quantum Trace Difference (`ε_flav(V³)`):**
Weighting `W_udd` by `q⁻¹` and `W_uud` by `q` and dividing by `[2]_q³ = (q + q⁻¹)³` produces
`-(q - q⁻¹) * (-q⁻¹^6 * P_poly q) * q^3 / (q^2 + 1)^3`
`= -(q^2 - 1) * (-q⁻¹^6 * P_poly q) * q^2 / (q^2 + 1)^3`
`= (q^2 - 1) * P_poly q / (q^4 * (q^2 + 1)^3)` (matching `|ε_flav(V³)|` up to sign). -/
theorem pivotal_RT_trace_eq_neg_flavourWeightSplit {q : R} (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    (q⁻¹ * trW_V3 q - q * trW_V3 q) / (q + q⁻¹) ^ 3 =
        -(q - q⁻¹) * (-q⁻¹ ^ 6 * P_poly q) * q ^ 3 / (q ^ 2 + 1) ^ 3 ∧
      (q⁻¹ * trW_V3 q - q * trW_V3 q) / (q + q⁻¹) ^ 3 =
        -(q ^ 2 - 1) * (-q⁻¹ ^ 6 * P_poly q) * q ^ 2 / (q ^ 2 + 1) ^ 3 ∧
      (q⁻¹ * trW_V3 q - q * trW_V3 q) / (q + q⁻¹) ^ 3 =
        (q ^ 2 - 1) * P_poly q / (q ^ 4 * (q ^ 2 + 1) ^ 3) := by
  obtain ⟨htr1, htr2⟩ := tr_W_V3_eq_P_poly hq
  have htr : trW_V3 q = -q⁻¹ ^ 6 * P_poly q := htr1.trans htr2
  have hqdim : q + q⁻¹ ≠ 0 := by
    intro h0
    apply hq2
    have hmul : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← hmul, h0, mul_zero]
  rw [htr]
  refine ⟨by field_simp; try ring, by field_simp; try ring, by field_simp; try ring⟩

/-! ## 4. Cautis–Kamnitzer–Morrison Skew-Howe `q ↦ -q⁻¹` Invariance and `[A₁₂, A₁₃]` -/

/-- **Skew-Howe `q ↦ -q⁻¹` Invariance of `h = q - q⁻¹` and `tr_W(V³)`:**
Substituting `q ↦ -q⁻¹` leaves `h = q - q⁻¹` strictly invariant, hence leaves `tr_W(V³)`
invariant. -/
theorem skewHowe_invariance_V3 {q : R} (hq : q ≠ 0) :
    ((-q⁻¹) - (-q⁻¹)⁻¹) = q - q⁻¹ ∧ trW_V3 (-q⁻¹) = trW_V3 q := by
  have hqn : -q⁻¹ ≠ 0 := neg_ne_zero.mpr (inv_ne_zero hq)
  have hh : ((-q⁻¹) - (-q⁻¹)⁻¹) = q - q⁻¹ := by
    rw [inv_neg, inv_inv, sub_neg_eq_add]
    ring
  refine ⟨hh, ?_⟩
  rw [(tr_W_V3_eq_P_poly hqn).1, (tr_W_V3_eq_P_poly hq).1, hh]

/-- Pure-braid generator `A₁₂ = σ₀²` on `S^{(2,1)}`. -/
def A12 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  rho21_sigma0 q ^ 2

/-- Inverse pure-braid generator `A₁₂⁻¹ = (σ₀⁻¹)²` on `S^{(2,1)}`. -/
def A12_inv (q : R) : Matrix (Fin 2) (Fin 2) R :=
  rho21_sigma0_inv q ^ 2

/-- Pure-braid generator `A₁₃ = σ₁ σ₀² σ₁⁻¹` on `S^{(2,1)}`. -/
def A13 (q : R) : Matrix (Fin 2) (Fin 2) R :=
  rho21_sigma1 q * A12 q * rho21_sigma1_inv q

/-- Inverse pure-braid generator `A₁₃⁻¹ = σ₁ (σ₀⁻¹)² σ₁⁻¹` on `S^{(2,1)}`. -/
def A13_inv (q : R) : Matrix (Fin 2) (Fin 2) R :=
  rho21_sigma1 q * A12_inv q * rho21_sigma1_inv q

/-- Explicit `2 × 2` entries of `A₁₂` and `A₁₂⁻¹` for `q ≠ 0`. -/
theorem A12_and_inv_explicit {q : R} (hq : q ≠ 0) :
    A12 q = !![q⁻¹ ^ 2, -(q - q⁻¹); 0, q ^ 2] ∧
      A12_inv q = !![q ^ 2, q - q⁻¹; 0, q⁻¹ ^ 2] := by
  refine ⟨?_, ?_⟩
  · unfold A12
    rw [sq, rho21_sigma0_eq]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)
  · unfold A12_inv
    rw [sq, rho21_sigma0_inv_eq]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)

/-- Exact invertibility `A₁₂ * A₁₂⁻¹ = 1` and `A₁₃ * A₁₃⁻¹ = 1` for `q ≠ 0`. -/
theorem A12_and_A13_mul_inv {q : R} (hq : q ≠ 0) :
    A12 q * A12_inv q = 1 ∧ A13 q * A13_inv q = 1 := by
  obtain ⟨hA12, hA12i⟩ := A12_and_inv_explicit hq
  have h12 : A12 q * A12_inv q = 1 := by
    rw [hA12, hA12i]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)
  refine ⟨h12, ?_⟩
  unfold A13 A13_inv
  rw [hA12, hA12i, rho21_sigma1_eq, rho21_sigma1_inv_eq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp; try field_simp; try ring)

/-- **Pure-Braid Commutator `[A₁₂, A₁₃]` Reproduces `tr_W(V³)`:**
`1 + tr(A₁₂ A₁₃ A₁₂⁻¹ A₁₃⁻¹) = 3 - 3 * (q - q⁻¹)⁴ - (q - q⁻¹)⁶ = tr_W(V³)`. -/
theorem commutator_A12_A13_trace_eq_V3 {q : R} (hq : q ≠ 0) :
    1 + (A12 q * A13 q * A12_inv q * A13_inv q).trace =
      3 - 3 * (q - q⁻¹) ^ 4 - (q - q⁻¹) ^ 6 ∧
    1 + (A12 q * A13 q * A12_inv q * A13_inv q).trace = trW_V3 q := by
  obtain ⟨hA12, hA12i⟩ := A12_and_inv_explicit hq
  have htr : 1 + (A12 q * A13 q * A12_inv q * A13_inv q).trace =
      3 - 3 * (q - q⁻¹) ^ 4 - (q - q⁻¹) ^ 6 := by
    unfold A13 A13_inv
    rw [hA12, hA12i, rho21_sigma1_eq, rho21_sigma1_inv_eq]
    simp [Matrix.trace_fin_two]
    field_simp
    ring
  exact ⟨htr, htr.trans (tr_W_V3_eq_P_poly hq).1.symm⟩

end Hecke21

/-! ## 5. Honest Elliptic vs Hyperbolic Boundedness Diagnostic -/

section BoundednessDiagnostic

/-- **Elliptic Regime Bound (`0 ≤ h² < 1 → |-(1 + h²)| < 2`):**
When `h = q - q⁻¹` satisfies `0 ≤ h² < 1` (covering the physical substrate `h₀² ≈ 0.0437 < 1`),
`|tr(ρ_{(2,1)}(V))| = |-(1 + h²)| < 2`, placing `ρ_{(2,1)}(V) ∈ SL₂` strictly inside the
elliptic interval `(-2, 2)`. -/
theorem elliptic_V_trace_bound {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {h : K} (hnonneg : 0 ≤ h ^ 2) (hlt : h ^ 2 < 1) :
    |-(1 + h ^ 2)| < 2 := by
  rw [abs_neg, abs_of_pos (by linarith)]
  linarith

/-- **Hyperbolic Commutator Refutes Uniform `[P₃, P₃]` Bound:**
1. At `q = 111 / 100 : ℚ` (within `2.2 × 10⁻⁵` of `q₀ ≈ 1.10998`), the 5-fold pure-braid
   commutator `1 + tr([A₁₂⁵, A₁₃⁵])` evaluates to `< -3`.
2. At `q = 11 / 10 : ℚ` (`h = 21 / 110`), `1 + tr([A₁₂⁵, A₁₃⁵]) < -1` and
   `1 + tr([A₁₂⁶, A₁₃⁶]) < -3`, refuting any uniform `≈ 3` trace ceiling across `[P₃, P₃]`. -/
theorem hyperbolic_commutator_refutes_uniform_bound :
    (1 + ((A12 (111 / 100 : ℚ) ^ 5) * (A13 (111 / 100 : ℚ) ^ 5) *
        (A12_inv (111 / 100 : ℚ) ^ 5) * (A13_inv (111 / 100 : ℚ) ^ 5)).trace < -3) ∧
    (1 + ((A12 (11 / 10 : ℚ) ^ 5) * (A13 (11 / 10 : ℚ) ^ 5) *
        (A12_inv (11 / 10 : ℚ) ^ 5) * (A13_inv (11 / 10 : ℚ) ^ 5)).trace < -1) ∧
    (1 + ((A12 (11 / 10 : ℚ) ^ 6) * (A13 (11 / 10 : ℚ) ^ 6) *
        (A12_inv (11 / 10 : ℚ) ^ 6) * (A13_inv (11 / 10 : ℚ) ^ 6)).trace < -3) := by
  have h5_eq : ∀ M : Matrix (Fin 2) (Fin 2) ℚ, M ^ 5 = (M * M) * (M * M) * M := by
    intro M
    simp [pow_succ, Matrix.mul_assoc]
  have h6_eq : ∀ M : Matrix (Fin 2) (Fin 2) ℚ, M ^ 6 = ((M * M) * M) * ((M * M) * M) := by
    intro M
    simp [pow_succ, Matrix.mul_assoc]
  obtain ⟨hA_111, hAi_111⟩ := A12_and_inv_explicit (q := (111 / 100 : ℚ)) (by norm_num)
  obtain ⟨hA_11, hAi_11⟩ := A12_and_inv_explicit (q := (11 / 10 : ℚ)) (by norm_num)
  refine ⟨?_, ?_, ?_⟩
  · unfold A13 A13_inv
    rw [hA_111, hAi_111, rho21_sigma1_eq, rho21_sigma1_inv_eq, h5_eq, h5_eq, h5_eq, h5_eq]
    simp [Matrix.trace_fin_two]
    norm_num
  · unfold A13 A13_inv
    rw [hA_11, hAi_11, rho21_sigma1_eq, rho21_sigma1_inv_eq, h5_eq, h5_eq, h5_eq, h5_eq]
    simp [Matrix.trace_fin_two]
    norm_num
  · unfold A13 A13_inv
    rw [hA_11, hAi_11, rho21_sigma1_eq, rho21_sigma1_inv_eq, h6_eq, h6_eq, h6_eq, h6_eq]
    simp [Matrix.trace_fin_two]
    norm_num

end BoundednessDiagnostic

end QOU.QBeta.BorromeanFlavourPivotalUnification
