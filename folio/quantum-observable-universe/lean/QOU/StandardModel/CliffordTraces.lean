import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Kronecker

/-!
# Clifford algebra `Cl(1,3)`: Dirac trace identities

Bean `qou-qssg` (QFT-5, math-only core; epic `qou-3fjn`). Pure algebra: no loop, no
cross-section and no empirical value appears.

## Part I — trace identities from the Clifford relation alone

Let `A` be an `R`-algebra with a cyclic `R`-linear functional `τ` (`τ (x * y) = τ (y * x)`), and
let `g : ι → A` satisfy the Clifford relation `g μ * g ν + g ν * g μ = 2 η μ ν` for a symmetric
bilinear form `η` on the index set. With `2` invertible in `R`:

* `trace_two`  : `τ (g μ * g ν) = η μ ν * τ 1`;
* `trace_four` : `τ (g a g b g c g d) = (η_ab η_cd − η_ac η_bd + η_ad η_bc) τ 1`;
* `trace_eq_zero_of_anticomm` : `τ x = 0` whenever some `Γ` with `Γ² = 1` anticommutes with `x`.

Nothing here depends on the signature, the dimension or a matrix representation.

## Part II — the Weyl representation of `Cl(1,3)`

Over any commutative ring `K` with an element `i`, `i² = −1`, the explicit `4 × 4` matrices
`γ⁰ … γ³` satisfy `{γ^μ, γ^ν} = 2 η^{μν}` with `η = diag(1, −1, −1, −1)` (`weyl_clifford`), and
`γ⁵ = i γ⁰γ¹γ²γ³` satisfies `(γ⁵)² = 1` and `{γ⁵, γ^μ} = 0`. So Part I applies to the matrix
trace, giving `tr(γ^μ γ^ν) = 4 η^{μν}`, the four-gamma formula, and the vanishing of every trace of
one or three gamma matrices and of `γ⁵`, `γ⁵γ^μγ^ν`. The chiral projectors
`P_± = (1 ± γ⁵)/2` are complementary orthogonal idempotents.

Base ring (§7c): Part I is over a generic commutative ring with `2` invertible; Part II is over a
generic commutative ring containing a square root of `−1` (needing `2` invertible only for the
projectors and for the Part I corollaries). No `ℝ` and no `ℂ` are fixed.

Standard reference (not yet in the bibliography): Peskin, Schroeder, *An Introduction to Quantum Field Theory*, §5.1 (trace
   theorems) — the identities, not their physics use.
-/

namespace QOU.QFTMath.Clifford

open Matrix

section Abstract

variable {R A ι : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- A cyclic `R`-linear functional (`τ (x y) = τ (y x)`), the abstract trace. -/
structure CyclicTrace (R A : Type*) [CommRing R] [Ring A] [Algebra R A] where
  /-- The underlying linear functional. -/
  toFun : A →ₗ[R] R
  /-- Cyclicity. -/
  cyclic : ∀ x y : A, toFun (x * y) = toFun (y * x)

/-- A Clifford family: `g μ g ν + g ν g μ = 2 η μ ν` for a symmetric form `η`. -/
structure CliffordFamily (R A ι : Type*) [CommRing R] [Ring A] [Algebra R A] where
  /-- The generators. -/
  g : ι → A
  /-- The bilinear form. -/
  η : ι → ι → R
  /-- Symmetry of the form. -/
  η_symm : ∀ μ ν, η μ ν = η ν μ
  /-- The Clifford relation. -/
  rel : ∀ μ ν, g μ * g ν + g ν * g μ = algebraMap R A (2 * η μ ν)

variable (τ : CyclicTrace R A) (C : CliffordFamily R A ι)

private lemma cancel_two [Invertible (2 : R)] {x y : R} (h : 2 * x = 2 * y) : x = y := by
  have := congrArg (fun z => ⅟(2 : R) * z) h
  simpa [← mul_assoc] using this

/-- **Two-gamma trace**: `τ (g μ g ν) = η μ ν · τ 1`. -/
theorem trace_two [Invertible (2 : R)] (μ ν : ι) :
    τ.toFun (C.g μ * C.g ν) = C.η μ ν * τ.toFun 1 := by
  have h := congrArg τ.toFun (C.rel μ ν)
  rw [map_add, τ.cyclic (C.g ν) (C.g μ), Algebra.algebraMap_eq_smul_one, map_smul,
    smul_eq_mul] at h
  apply cancel_two
  rw [← mul_assoc, ← h]; ring

/-- Anticommutation in rewrite form: `g a g b = 2 η_ab − g b g a`. -/
lemma swap (a b : ι) : C.g a * C.g b = algebraMap R A (2 * C.η a b) - C.g b * C.g a := by
  rw [← C.rel a b]; abel

/-- The identity behind the four-gamma trace:
`abcd + bcda = 2η_ab cd − 2η_ac bd + 2η_ad bc`. -/
lemma four_identity (a b c d : ι) :
    C.g a * C.g b * C.g c * C.g d + C.g b * C.g c * C.g d * C.g a
      = algebraMap R A (2 * C.η a b) * (C.g c * C.g d)
        - algebraMap R A (2 * C.η a c) * (C.g b * C.g d)
        + algebraMap R A (2 * C.η a d) * (C.g b * C.g c) := by
  have e1 : C.g a * C.g b * C.g c * C.g d
      = algebraMap R A (2 * C.η a b) * (C.g c * C.g d) - C.g b * C.g a * C.g c * C.g d := by
    rw [swap C a b]; noncomm_ring
  have e2 : C.g b * C.g a * C.g c * C.g d
      = algebraMap R A (2 * C.η a c) * (C.g b * C.g d) - C.g b * C.g c * C.g a * C.g d := by
    have : C.g b * C.g a * C.g c * C.g d = C.g b * (C.g a * C.g c) * C.g d := by noncomm_ring
    rw [this, swap C a c, mul_sub, sub_mul, ← Algebra.commutes]; noncomm_ring
  have e3 : C.g b * C.g c * C.g a * C.g d
      = algebraMap R A (2 * C.η a d) * (C.g b * C.g c) - C.g b * C.g c * C.g d * C.g a := by
    have : C.g b * C.g c * C.g a * C.g d = C.g b * C.g c * (C.g a * C.g d) := by noncomm_ring
    rw [this, swap C a d, mul_sub, ← Algebra.commutes]; noncomm_ring
  rw [e1, e2, e3]; abel

/-- **Four-gamma trace**:
`τ (g a g b g c g d) = (η_ab η_cd − η_ac η_bd + η_ad η_bc) · τ 1`. -/
theorem trace_four [Invertible (2 : R)] (a b c d : ι) :
    τ.toFun (C.g a * C.g b * C.g c * C.g d)
      = (C.η a b * C.η c d - C.η a c * C.η b d + C.η a d * C.η b c) * τ.toFun 1 := by
  have h := congrArg τ.toFun (four_identity C a b c d)
  have hcyc : τ.toFun (C.g b * C.g c * C.g d * C.g a) = τ.toFun (C.g a * C.g b * C.g c * C.g d) := by
    rw [τ.cyclic]; congr 1; noncomm_ring
  simp only [map_add, map_sub, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul,
    map_smul, smul_eq_mul, hcyc] at h
  rw [trace_two τ C c d, trace_two τ C b d, trace_two τ C b c] at h
  apply cancel_two
  rw [← mul_assoc 2 (_ - _ + _), ← two_mul] at *
  linear_combination h

/-- **Odd-trace vanishing, abstract form**: if `Γ² = 1` and `Γ x = −x Γ`, then `τ x = 0`. -/
theorem trace_eq_zero_of_anticomm [Invertible (2 : R)] (Γ x : A) (hΓ : Γ * Γ = 1)
    (hx : Γ * x = -(x * Γ)) : τ.toFun x = 0 := by
  have h1 : τ.toFun x = τ.toFun (Γ * x * Γ) := by
    rw [τ.cyclic, ← mul_assoc, hΓ, one_mul]
  rw [hx, neg_mul, mul_assoc, hΓ, mul_one, map_neg] at h1
  apply cancel_two
  linear_combination h1

/-- If `Γ` anticommutes with `x` and with `y` then it commutes with `x y`. -/
lemma comm_mul_of_anticomm (Γ x y : A) (hx : Γ * x = -(x * Γ)) (hy : Γ * y = -(y * Γ)) :
    Γ * (x * y) = x * y * Γ := by
  rw [← mul_assoc, hx, neg_mul, mul_assoc, hy]; noncomm_ring

/-- If `Γ` commutes with `x` and anticommutes with `y` then it anticommutes with `x y`. -/
lemma anticomm_mul_of_comm (Γ x y : A) (hx : Γ * x = x * Γ) (hy : Γ * y = -(y * Γ)) :
    Γ * (x * y) = -(x * y * Γ) := by
  rw [← mul_assoc, hx, mul_assoc, hy]; noncomm_ring

end Abstract

/-! ## Part II — the Weyl representation, built as Kronecker products of `2 × 2` matrices

`γ⁰ = σ₁ ⊗ 1`, `γᵏ = ε ⊗ σₖ` with `ε = iσ₂ = [[0,1],[−1,0]]`, and `γ⁵ = −σ₃ ⊗ 1`. Every
Clifford relation then reduces, via `(A ⊗ B)(C ⊗ D) = AC ⊗ BD`, to a `2 × 2` identity. -/

section Weyl

open scoped Kronecker

variable {K : Type*} [CommRing K]

/-- The index type `ℂ² ⊗ ℂ²` of Dirac spinors. -/
abbrev D4 := Fin 2 × Fin 2

/-- The Minkowski form `η = diag(1, −1, −1, −1)`. -/
def η : Fin 4 → Fin 4 → K := fun μ ν => if μ = ν then (if μ = 0 then 1 else -1) else 0

/-- `σ₁`. -/
def s1 : Matrix (Fin 2) (Fin 2) K := !![0, 1; 1, 0]
/-- `σ₃`. -/
def s3 : Matrix (Fin 2) (Fin 2) K := !![1, 0; 0, -1]
/-- `ε = iσ₂`. -/
def ep : Matrix (Fin 2) (Fin 2) K := !![0, 1; -1, 0]
/-- The Pauli matrices `σ₁, σ₂, σ₃`, with `i` playing `√−1`. -/
def pauli (i : K) : Fin 3 → Matrix (Fin 2) (Fin 2) K := ![s1, !![0, -i; i, 0], s3]

/-- The Weyl (chiral) gamma matrices. -/
def γ (i : K) : Fin 4 → Matrix D4 D4 K :=
  ![s1 ⊗ₖ 1, ep ⊗ₖ pauli i 0, ep ⊗ₖ pauli i 1, ep ⊗ₖ pauli i 2]

/-- `γ⁵ = −σ₃ ⊗ 1 = diag(−1, −1, 1, 1)` in the chiral basis. -/
def γ5 : Matrix D4 D4 K := (-s3) ⊗ₖ 1

lemma s1_sq : (s1 : Matrix (Fin 2) (Fin 2) K) * s1 = 1 := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [s1]
lemma s3_sq : (s3 : Matrix (Fin 2) (Fin 2) K) * s3 = 1 := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [s3]
lemma ep_sq : (ep : Matrix (Fin 2) (Fin 2) K) * ep = -1 := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [ep]
lemma s1_ep : (s1 : Matrix (Fin 2) (Fin 2) K) * ep + ep * s1 = 0 := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [s1, ep]
lemma s3_s1 : (s3 : Matrix (Fin 2) (Fin 2) K) * s1 = -(s1 * s3) := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [s1, s3]
lemma s3_ep : (s3 : Matrix (Fin 2) (Fin 2) K) * ep = -(ep * s3) := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [s3, ep]

/-- The Pauli anticommutator `σₖσₗ + σₗσₖ = 2δₖₗ`. -/
lemma pauli_anticomm (i : K) (hi : i * i = -1) (k l : Fin 3) :
    pauli i k * pauli i l + pauli i l * pauli i k = (if k = l then (2 : K) else 0) • 1 := by
  ext a b
  fin_cases k <;> fin_cases l <;> fin_cases a <;> fin_cases b <;>
    simp [pauli, s1, s3] <;>
    first | ring1 | linear_combination (2 : K) * hi | linear_combination (-2 : K) * hi

/-- `{A ⊗ B, C ⊗ D} = {A,C} ⊗ BD` when `B` and `D` commute. -/
lemma kron_anticomm_of_commR {A C B D : Matrix (Fin 2) (Fin 2) K} (h : B * D = D * B) :
    (A ⊗ₖ B) * (C ⊗ₖ D) + (C ⊗ₖ D) * (A ⊗ₖ B) = (A * C + C * A) ⊗ₖ (B * D) := by
  rw [← mul_kronecker_mul, ← mul_kronecker_mul, ← h, ← add_kronecker]

/-- `{A ⊗ B, A ⊗ D} = A² ⊗ {B, D}`. -/
lemma kron_anticomm_same {A B D : Matrix (Fin 2) (Fin 2) K} :
    (A ⊗ₖ B) * (A ⊗ₖ D) + (A ⊗ₖ D) * (A ⊗ₖ B) = (A * A) ⊗ₖ (B * D + D * B) := by
  rw [← mul_kronecker_mul, ← mul_kronecker_mul, ← kronecker_add]

lemma one_D4 : (1 : Matrix D4 D4 K) = (1 : Matrix (Fin 2) (Fin 2) K) ⊗ₖ 1 :=
  one_kronecker_one.symm

lemma neg_kron (A B : Matrix (Fin 2) (Fin 2) K) : (-A) ⊗ₖ B = -(A ⊗ₖ B) := by
  ext a b; simp [kroneckerMap_apply]

variable (i : K)

/-- **The Clifford relation** `{γ^μ, γ^ν} = 2 η^{μν}` in the Weyl representation. -/
theorem weyl_clifford (hi : i * i = -1) (μ ν : Fin 4) :
    γ i μ * γ i ν + γ i ν * γ i μ = algebraMap K _ (2 * η μ ν) := by
  rw [Algebra.algebraMap_eq_smul_one, one_D4]
  have hc : ∀ k : Fin 3, (1 : Matrix (Fin 2) (Fin 2) K) * pauli i k = pauli i k * 1 := by simp
  fin_cases μ <;> fin_cases ν <;>
    simp only [γ, η, Fin.reduceFinMk, Matrix.cons_val, Fin.reduceEq, ite_true,
      ite_false, Fin.isValue] <;>
    first
    | (rw [kron_anticomm_same, s1_sq] <;> simp [kronecker_add, two_smul]) <;> done
    | (rw [kron_anticomm_of_commR (hc _), s1_ep] <;> simp) <;> done
    | (rw [add_comm, kron_anticomm_of_commR (hc _), s1_ep] <;> simp) <;> done
    | (rw [kron_anticomm_same, ep_sq, pauli_anticomm i hi] <;>
        simp [neg_kron, kronecker_smul] <;> norm_num) <;> done

/-- `(γ⁵)² = 1`. -/
theorem gamma5_sq : (γ5 : Matrix D4 D4 K) * γ5 = 1 := by
  rw [γ5, ← mul_kronecker_mul, neg_mul_neg, s3_sq, one_mul, one_kronecker_one]

/-- `γ⁵` anticommutes with every `γ^μ`. -/
theorem gamma5_anticomm (μ : Fin 4) : γ5 * γ i μ = -(γ i μ * γ5) := by
  fin_cases μ <;>
    simp only [γ, γ5, Fin.reduceFinMk, Matrix.cons_val, Fin.isValue] <;>
    rw [← mul_kronecker_mul, ← mul_kronecker_mul] <;>
    simp [neg_mul, mul_neg, s3_s1, s3_ep, neg_kron]

/-- `tr γ⁵ = 0`. -/
theorem trace_gamma5 : Matrix.trace (γ5 : Matrix D4 D4 K) = 0 := by
  rw [γ5, trace_kronecker]; simp [s3, Matrix.trace_fin_two]

/-- The Weyl gamma matrices as a Clifford family for the Minkowski form. -/
def weylFamily (hi : i * i = -1) : CliffordFamily K (Matrix D4 D4 K) (Fin 4) where
  g := γ i
  η := η
  η_symm := fun μ ν => by unfold η; split_ifs <;> simp_all
  rel := weyl_clifford i hi

/-- The matrix trace as a cyclic functional. -/
def matTrace : CyclicTrace K (Matrix D4 D4 K) where
  toFun := Matrix.traceLinearMap D4 K K
  cyclic := fun x y => Matrix.trace_mul_comm x y

lemma matTrace_one : (matTrace (K := K)).toFun 1 = 4 := by
  norm_num [matTrace, Matrix.trace_one]

/-- `tr(γ^μ γ^ν) = 4 η^{μν}`. -/
theorem trace_gamma_two [Invertible (2 : K)] (hi : i * i = -1) (μ ν : Fin 4) :
    Matrix.trace (γ i μ * γ i ν) = 4 * η μ ν := by
  have := trace_two matTrace (weylFamily i hi) μ ν
  rw [matTrace_one] at this
  simpa [matTrace, weylFamily, mul_comm] using this

/-- **Four-gamma trace** `tr(γ^a γ^b γ^c γ^d) = 4(η^{ab}η^{cd} − η^{ac}η^{bd} + η^{ad}η^{bc})`. -/
theorem trace_gamma_four [Invertible (2 : K)] (hi : i * i = -1) (a b c d : Fin 4) :
    Matrix.trace (γ i a * γ i b * γ i c * γ i d)
      = 4 * (η a b * η c d - η a c * η b d + η a d * η b c) := by
  have := trace_four matTrace (weylFamily i hi) a b c d
  rw [matTrace_one] at this
  simpa [matTrace, weylFamily, mul_comm] using this

/-- `tr γ^μ = 0`. -/
theorem trace_gamma_one [Invertible (2 : K)] (μ : Fin 4) : Matrix.trace (γ i μ) = 0 :=
  trace_eq_zero_of_anticomm matTrace γ5 (γ i μ) gamma5_sq (gamma5_anticomm i μ)

/-- `tr(γ^a γ^b γ^c) = 0`: every trace of three gamma matrices vanishes. -/
theorem trace_gamma_three [Invertible (2 : K)] (a b c : Fin 4) :
    Matrix.trace (γ i a * γ i b * γ i c) = 0 := by
  refine trace_eq_zero_of_anticomm matTrace γ5 _ gamma5_sq ?_
  exact anticomm_mul_of_comm _ _ _
    (comm_mul_of_anticomm _ _ _ (gamma5_anticomm i a) (gamma5_anticomm i b)) (gamma5_anticomm i c)

/-- `tr(γ⁵ γ^μ γ^ν) = 0`. For `μ = ν` this is `±tr γ⁵`; otherwise take a third index `ρ`: `γ^ρ`
squares to a unit and anticommutes with `γ⁵ γ^μ γ^ν`. Proved here directly from the Kronecker
form: `γ⁵ γ^μ γ^ν = (−σ₃ A C) ⊗ (B D)` and `tr(σ₃ A C) = 0` for `A, C ∈ {σ₁, ε}`. -/
theorem trace_gamma5_two (μ ν : Fin 4) : Matrix.trace (γ5 * γ i μ * γ i ν) = 0 := by
  fin_cases μ <;> fin_cases ν <;>
    simp only [γ, γ5, Fin.reduceFinMk, Matrix.cons_val, Fin.isValue] <;>
    rw [← mul_kronecker_mul, ← mul_kronecker_mul, trace_kronecker] <;>
    simp [pauli, s1, s3, ep, Matrix.trace_fin_two]

/-- The chiral projectors `P_± = (1 ± γ⁵)/2` are complementary orthogonal idempotents. -/
theorem chiral_projectors [Invertible (2 : K)] :
    let Pp : Matrix D4 D4 K := ⅟(2 : K) • (1 + γ5)
    let Pm : Matrix D4 D4 K := ⅟(2 : K) • (1 - γ5)
    Pp * Pp = Pp ∧ Pm * Pm = Pm ∧ Pp * Pm = 0 ∧ Pp + Pm = 1 := by
  intro Pp Pm
  have h5 := gamma5_sq (K := K)
  have h2 : (⅟(2 : K)) * ⅟2 * 2 = ⅟2 := by rw [mul_assoc, invOf_mul_self, mul_one]
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp only [Pp, smul_mul_smul_comm, add_mul, mul_add, one_mul, mul_one, h5]
    rw [show (1 + γ5 + (γ5 + 1) : Matrix D4 D4 K) = (2 : K) • (1 + γ5) by
      rw [two_smul]; abel, smul_smul, h2]
  · simp only [Pm, smul_mul_smul_comm, sub_mul, mul_sub, one_mul, mul_one, h5]
    rw [show (1 - γ5 - (γ5 - 1) : Matrix D4 D4 K) = (2 : K) • (1 - γ5) by
      rw [two_smul]; abel, smul_smul, h2]
  · simp only [Pp, Pm, smul_mul_smul_comm, add_mul, mul_sub, one_mul, mul_one, h5]
    rw [show ((1 : Matrix D4 D4 K) + γ5 - (γ5 + 1)) = 0 by abel, smul_zero]
  · rw [← smul_add, show (1 + γ5 + (1 - γ5) : Matrix D4 D4 K) = (2 : K) • 1 by
      rw [two_smul]; abel, smul_smul, invOf_mul_self, one_smul]

end Weyl

end QOU.QFTMath.Clifford
