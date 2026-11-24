import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Basis
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Field.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Frobenius–Schur Block Norm Action and Expectation Framing Cancellation

Over an arbitrary commutative ring `R` and field `K` (§7c generic base-ring discipline,
no `ℝ`), this module proves two foundational results connecting Geck–Pfeiffer's Schur-element
Frobenius structure on matrix blocks to normalized quantum-state expectation values:

1. **Geck–Pfeiffer §7.2 Wedderburn Block Norm Law:** On `Matrix n n R` (`d_λ = card n`),
   the Higman matrix-unit sandwich satisfies `∑_{i,j} E_{ij} M E_{ji} = (tr M) • 1`
   (`higman_matrix_sandwich_eq_trace_smul_one`). Under the scaled Frobenius trace
   `τ_u(M) = u * tr(M)` (`u = c_λ⁻¹ ∈ Rˣ`), `(E_{ij}, u⁻¹ E_{ji})` is an exact dual basis
   (`scaledMatrix_dual_left`, `scaledMatrix_dual_right`), and the Schur-weighted Higman
   norm map acts on the block identity `1` (representing the central idempotent `e_λ`) by
   scalar multiplication by `c_λ * card(n)` (`schurWeightedNorm_one_eq_schur_mul_dim`),
   vanishing when `c_λ = 0` or `char(R) ∣ card(n)`.
2. **Expectation Framing Cancellation (`expectation_framing_invariant`):** Rescaling a
   linear trace `τ ↦ τ_u = u • τ` by a nonzero framing unit `u` (such as `u = q₀^{±3}`)
   scales unconditioned traces `τ_u(e * x) = u * τ(e * x)` (`framedTrace_ne_of_ne_one`),
   while leaving every conditioned Rayleigh–Schrödinger / Hellmann–Feynman expectation
   `τ_u(e * x) / τ_u(e) = τ(e * x) / τ(e)` **strictly invariant** (`expectation_qPower_framing_invariant`).

References: Meinolf Geck & Götz Pfeiffer (2000) §7.2; Donald G. Higman (1955), Canad. J. Math. 7, 490–508.
-- Ref: [manuscript]
-/

namespace QOU.AlgebraicSubstrate

open BigOperators

/-! ## 1. Wedderburn Matrix Block Dual Basis and Schur-Weighted Higman Norm -/

section MatrixSchurBlock

variable {R : Type*} [CommRing R]
variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Standard `(i, j)` elementary matrix unit `E_{i,j}` on `Matrix n n R`. -/
def matUnit (i j : n) : Matrix n n R :=
  Matrix.single i j 1

/-- Entrywise formula for the sandwich `E_{i,j} * M * E_{j,i}`. -/
theorem matUnit_mul_mat_mul_matUnit_apply (M : Matrix n n R) (i j p q : n) :
    (matUnit (R := R) i j * M * matUnit (R := R) j i) p q =
      if p = i ∧ q = i then M j j else 0 := by
  simp only [matUnit, Matrix.mul_apply, Matrix.single, Matrix.of_apply, boole_mul, mul_boole]
  by_cases hpi : p = i
  · subst hpi
    by_cases hqi : q = p
    · subst hqi
      simp
    · have hne : ¬ (p = q) := fun h => hqi h.symm
      simp [hqi, hne]
  · have hip : ¬ (i = p) := fun h => hpi h.symm
    simp [hpi, hip]

/-- **Higman Matrix Sandwich Identity:** `∑_{i,j} E_{i,j} * M * E_{j,i} = (tr M) • 1`. -/
theorem higman_matrix_sandwich_eq_trace_smul_one (M : Matrix n n R) :
    (∑ i : n, ∑ j : n, matUnit (R := R) i j * M * matUnit (R := R) j i) =
      (Matrix.trace M) • (1 : Matrix n n R) := by
  ext p q
  simp only [Matrix.sum_apply, matUnit_mul_mat_mul_matUnit_apply, Matrix.smul_apply,
    Matrix.one_apply, Matrix.trace, Matrix.diag_apply, smul_eq_mul]
  by_cases hpq : p = q
  · subst hpq
    simp
  · have hno : ∀ i : n, ¬ (p = i ∧ q = i) := by
      intro i ⟨hpi, hqi⟩
      exact hpq (hpi.trans hqi.symm)
    simp [hpq, hno]

/-- Trace of `M * E_{j,i}` extracts entry `M i j`. -/
theorem trace_mul_matUnit (M : Matrix n n R) (i j : n) :
    Matrix.trace (M * matUnit (R := R) j i) = M i j := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, matUnit, Matrix.single,
    Matrix.of_apply, mul_boole]
  rw [Finset.sum_eq_single i]
  · simp
  · intro k _ hki
    have hik : ¬ (i = k) := fun h => hki h.symm
    simp [hik]
  · intro hi
    exact absurd (Finset.mem_univ i) hi

/-- Trace of `E_{i,j} * M` extracts entry `M j i`. -/
theorem trace_matUnit_mul (M : Matrix n n R) (i j : n) :
    Matrix.trace (matUnit (R := R) i j * M) = M j i := by
  rw [Matrix.trace_mul_comm, trace_mul_matUnit]

/-- Scaled Frobenius trace `τ_u(M) = u * tr(M)` on `Matrix n n R` for a reciprocal Schur
weight `u ∈ Rˣ` (`u = c_λ⁻¹`). -/
def scaledMatrixTrace (u : Rˣ) : Matrix n n R →ₗ[R] R :=
  (u : R) • Matrix.traceLinearMap n R R

omit [DecidableEq n] in
theorem scaledMatrixTrace_apply (u : Rˣ) (M : Matrix n n R) :
    scaledMatrixTrace (n := n) u M = (u : R) * Matrix.trace M := rfl

omit [DecidableEq n] in
/-- Symmetry of the scaled block trace: `τ_u(M * N) = τ_u(N * M)`. -/
theorem scaledMatrixTrace_mul_comm (u : Rˣ) (M N : Matrix n n R) :
    scaledMatrixTrace u (M * N) = scaledMatrixTrace u (N * M) := by
  rw [scaledMatrixTrace_apply, scaledMatrixTrace_apply, Matrix.trace_mul_comm]

/-- Left dual-basis family `E_{(i,j)} = E_{i,j}` on `Matrix n n R`. -/
def dualE (pq : n × n) : Matrix n n R :=
  matUnit pq.1 pq.2

/-- Right dual-basis family `F_{(i,j)} = u⁻¹ • E_{j,i}` on `Matrix n n R`. -/
def dualF (u : Rˣ) (pq : n × n) : Matrix n n R :=
  (((u⁻¹ : Rˣ) : R)) • matUnit pq.2 pq.1

/-- **Left Dual-Basis Reconstruction on `Matrix n n R`:**
`∑_{p,q} τ_u(M * F_{(p,q)}) • E_{(p,q)} = M`. -/
theorem scaledMatrix_dual_left (u : Rˣ) (M : Matrix n n R) :
    (∑ pq : n × n, scaledMatrixTrace u (M * dualF u pq) • dualE (R := R) pq) = M := by
  ext r s
  rw [Fintype.sum_prod_type]
  simp only [dualE, dualF, Algebra.mul_smul_comm, map_smul, scaledMatrixTrace_apply,
    trace_mul_matUnit, smul_eq_mul, Matrix.sum_apply, Matrix.smul_apply]
  simp only [matUnit, Matrix.single, Matrix.of_apply, mul_boole]
  have hu : (u : R) * (((u⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv u
  rw [Finset.sum_eq_single r]
  · rw [Finset.sum_eq_single s]
    · simp only [and_self, ↓reduceIte]
      linear_combination M r s * hu
    · intro j _ hjs
      simp [hjs]
    · intro hs
      exact absurd (Finset.mem_univ s) hs
  · intro i _ hir
    simp [hir]
  · intro hr
    exact absurd (Finset.mem_univ r) hr

/-- **Right Dual-Basis Reconstruction on `Matrix n n R`:**
`∑_{p,q} τ_u(E_{(p,q)} * M) • F_{(p,q)} = M`. -/
theorem scaledMatrix_dual_right (u : Rˣ) (M : Matrix n n R) :
    (∑ pq : n × n, scaledMatrixTrace u (dualE pq * M) • dualF u pq) = M := by
  ext r s
  rw [Fintype.sum_prod_type]
  simp only [dualE, dualF, scaledMatrixTrace_apply, trace_matUnit_mul, smul_smul,
    Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul]
  simp only [matUnit, Matrix.single, Matrix.of_apply, mul_boole]
  have hu : (u : R) * (((u⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv u
  rw [Finset.sum_eq_single s]
  · rw [Finset.sum_eq_single r]
    · simp only [and_self, ↓reduceIte]
      linear_combination M r s * hu
    · intro j _ hjr
      simp [hjr]
    · intro hr
      exact absurd (Finset.mem_univ r) hr
  · intro i _ his
    simp [his]
  · intro hs
    exact absurd (Finset.mem_univ s) hs

/-- Integral Schur-weighted Higman norm map `N_c(M) = ∑_{i,j} E_{i,j} * M * (c • E_{j,i})`,
valid for arbitrary `c : R` (including non-invertible Schur elements at roots of unity). -/
def schurWeightedNorm (c : R) (M : Matrix n n R) : Matrix n n R :=
  ∑ i : n, ∑ j : n, matUnit i j * M * (c • matUnit j i)

/-- **Geck–Pfeiffer Block Norm Formula:** `N_c(M) = (c * tr M) • 1`. -/
theorem schurWeightedNorm_eq_trace_smul_one (c : R) (M : Matrix n n R) :
    schurWeightedNorm c M = (c * Matrix.trace M) • (1 : Matrix n n R) := by
  unfold schurWeightedNorm
  calc
    (∑ i : n, ∑ j : n, matUnit i j * M * (c • matUnit j i))
        = c • (∑ i : n, ∑ j : n, matUnit i j * M * matUnit j i) := by
          rw [Finset.smul_sum]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Finset.smul_sum]
          refine Finset.sum_congr rfl fun j _ => ?_
          rw [Algebra.mul_smul_comm]
    _ = c • ((Matrix.trace M) • (1 : Matrix n n R)) := by
          rw [higman_matrix_sandwich_eq_trace_smul_one]
    _ = (c * Matrix.trace M) • (1 : Matrix n n R) := by rw [smul_smul]

/-- **Central Idempotent Schur-Dimension Scaling:** On the block identity `1` (representing
the central Wedderburn idempotent `e_λ` of `M_{d_λ}(R)`), the Schur-weighted Higman norm acts
by the scalar `c_λ * card(n) = c_λ * d_λ`. -/
theorem schurWeightedNorm_one_eq_schur_mul_dim (c : R) :
    schurWeightedNorm c (1 : Matrix n n R) =
      (c * (Fintype.card n : R)) • (1 : Matrix n n R) := by
  rw [schurWeightedNorm_eq_trace_smul_one, Matrix.trace_one]

/-- Dual-basis Higman norm of `1` for `u = c_λ⁻¹ ∈ Rˣ`:
`∑_{p,q} E_{(p,q)} * 1 * F_{(p,q)} = (u⁻¹ * card n) • 1`. -/
theorem dualBasis_higmanNorm_one_eq (u : Rˣ) :
    (∑ pq : n × n, dualE (R := R) pq * (1 : Matrix n n R) * dualF u pq) =
      ((((u⁻¹ : Rˣ) : R) * (Fintype.card n : R))) • (1 : Matrix n n R) := by
  rw [Fintype.sum_prod_type]
  exact schurWeightedNorm_one_eq_schur_mul_dim (((u⁻¹ : Rˣ) : R))

/-- Root-of-unity / singular Schur vanishing: when `c_λ = 0`, `N_0(M) = 0`. -/
theorem schurWeightedNorm_zero_left (M : Matrix n n R) :
    schurWeightedNorm (0 : R) M = 0 := by
  rw [schurWeightedNorm_eq_trace_smul_one, zero_mul, zero_smul]

/-- Modular characteristic vanishing: when `(card n : R) = 0` (`char R ∣ d_λ`), the block
norm of the central idempotent `1` vanishes even for nonzero `c_λ`. -/
theorem schurWeightedNorm_one_eq_zero_of_card_eq_zero (c : R)
    (hchar : (Fintype.card n : R) = 0) :
    schurWeightedNorm c (1 : Matrix n n R) = 0 := by
  rw [schurWeightedNorm_one_eq_schur_mul_dim, hchar, mul_zero, zero_smul]

end MatrixSchurBlock

/-! ## 2. Framing Scaling vs Conditioned State Expectation Cancellation -/

section FramingCancellation

/-- Framed trace `τ_u = u • τ` obtained by rescaling a linear functional `τ : A →ₗ[R] R`
by a framing factor `u : R` (modelling writhe framing `q₀^{±3}`). -/
def framedTrace {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (τ : A →ₗ[R] R) (u : R) : A →ₗ[R] R :=
  u • τ

@[simp]
theorem framedTrace_apply {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (τ : A →ₗ[R] R) (u : R) (x : A) :
    framedTrace τ u x = u * τ x := rfl

/-- Unconditioned trace on an idempotent sector scales linearly with `u`:
`τ_u(e * x) = u * τ(e * x)`. -/
theorem framedTrace_idempotent_mul {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (τ : A →ₗ[R] R) (u : R) (e x : A) :
    framedTrace τ u (e * x) = u * τ (e * x) := rfl

/-- Over any integral domain `R`, an unconditioned trace `τ(e * x) ≠ 0` is **not**
framing-invariant whenever `u ≠ 1`: `τ_u(e * x) ≠ τ(e * x)`. -/
theorem framedTrace_ne_of_ne_one {R A : Type*} [CommRing R] [IsDomain R]
    [Ring A] [Algebra R A] (τ : A →ₗ[R] R) {u : R} {e x : A}
    (hu : u ≠ 1) (hx : τ (e * x) ≠ 0) :
    framedTrace τ u (e * x) ≠ τ (e * x) := by
  intro heq
  rw [framedTrace_apply] at heq
  have hsub : (u - 1) * τ (e * x) = 0 := by linear_combination heq
  rcases mul_eq_zero.mp hsub with hu0 | hx0
  · exact hu (sub_eq_zero.mp hu0)
  · exact hx hx0

/-- Division-free cross-multiplied framing invariance over **any** commutative ring `R`:
`τ_u(e * x) * τ(e) = τ(e * x) * τ_u(e)`. -/
theorem framedTrace_cross_invariant {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (τ : A →ₗ[R] R) (u : R) (e x : A) :
    framedTrace τ u (e * x) * τ e = τ (e * x) * framedTrace τ u e := by
  simp only [framedTrace_apply]
  ring

/-- Normalized quantum-state expectation `⟨x⟩_e = τ(e * x) / τ(e)` conditioned on an
idempotent `e ∈ A` over a field `K`. -/
def stateExpectation {K A : Type*} [Field K] [Ring A] [Algebra K A]
    (τ : A →ₗ[K] K) (e x : A) : K :=
  τ (e * x) / τ e

/-- **Expectation Framing Cancellation Theorem:** For any nonzero framing factor `u ≠ 0`
over a field `K`, the conditioned state expectation `⟨x⟩_e = τ(e * x) / τ(e)` is strictly
invariant under `τ ↦ τ_u = u • τ`:
`τ_u(e * x) / τ_u(e) = τ(e * x) / τ(e)`. -/
theorem expectation_framing_invariant {K A : Type*} [Field K] [Ring A] [Algebra K A]
    (τ : A →ₗ[K] K) {u : K} (hu : u ≠ 0) (e x : A) :
    stateExpectation (framedTrace τ u) e x = stateExpectation τ e x := by
  simp only [stateExpectation, framedTrace_apply]
  exact mul_div_mul_left (τ (e * x)) (τ e) hu

/-- Joint normalization and framing invariance on a genuine idempotent `e * e = e` with
nonzero quantum dimension `τ(e) ≠ 0`: the framed state remains normalized (`⟨e⟩_e = 1`)
and preserves all observable expectations (`⟨x⟩_{e, u} = ⟨x⟩_e`). -/
theorem stateExpectation_idempotent_normalized_and_invariant
    {K A : Type*} [Field K] [Ring A] [Algebra K A]
    (τ : A →ₗ[K] K) {u : K} {e : A} (hu : u ≠ 0) (he_idem : e * e = e) (he_nz : τ e ≠ 0)
    (x : A) :
    stateExpectation (framedTrace τ u) e e = 1 ∧
      stateExpectation (framedTrace τ u) e x = stateExpectation τ e x := by
  refine ⟨?_, expectation_framing_invariant τ hu e x⟩
  rw [expectation_framing_invariant τ hu e e, stateExpectation, he_idem]
  exact div_self he_nz

/-- **Integer `q₀^m` Writhe Framing Cancellation (`m = ±3` Case A Corollary):**
For every unit `q₀ : Kˣ` and every integer framing power `m : ℤ` (in particular `m = 3`
and `m = -3`), rescaling `τ` by `q₀^m` cancels identically out of `⟨x⟩_e`. -/
theorem expectation_qPower_framing_invariant {K A : Type*} [Field K] [Ring A] [Algebra K A]
    (τ : A →ₗ[K] K) (q₀ : Kˣ) (m : ℤ) (e x : A) :
    stateExpectation (framedTrace τ ((q₀ ^ m : Kˣ) : K)) e x = stateExpectation τ e x :=
  expectation_framing_invariant τ (Units.ne_zero (q₀ ^ m)) e x

end FramingCancellation

end QOU.AlgebraicSubstrate
