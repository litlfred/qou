import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# Intrinsic $3+1\mathrm{D}$ Spinor–Minkowski Emergence & Worldline–Schwinger Functor $\mathcal{F}_{\mathrm{SW}}$

This module establishes the unconditional algebraic and analytic foundations of the
Worldline–Schwinger observation functor $\mathcal{F}_{\mathrm{SW}}$ without external spacetime
postulates, auxiliary ghost fields, or uninstantiated context classes:

1. **Section 1 — Intrinsic $3+1\mathrm{D}$ Spinor–Minkowski Momentum Space from $\dim_{\mathbb{C}} V_2 = 2$**:
   - From the 2-dimensional complex spinor fibre $V_2 = \mathbb{C}^2$ equipped with the determinant
     form on $\Lambda^2 V_2 \cong \mathbb{C}$ and conjugate-transpose self-duality, constructs the
     spinor-momentum parametrization `spinorMat` / `spinorMatVec` into $2 \times 2$ complex matrices:
     $$P(p_0, p_1, p_2, p_3) =
       \begin{pmatrix} p_0 + p_3 & p_1 - i p_2 \\ p_1 + i p_2 & p_0 - p_3 \end{pmatrix}.$$
   - Proves conjugate-transpose self-duality (`spinorMat_conjTranspose_eq_self`), injectivity
     (`spinorMat_injective`), and an exact $\mathbb{R}$-linear equivalence
     `spinorHermitianLinearEquiv` between $\mathbb{R}^4$ (`Fin 4 → ℝ`) and the real subspace of
     $2 \times 2$ Hermitian matrices `{ H : Matrix (Fin 2) (Fin 2) ℂ // H.conjTranspose = H }`,
     establishing spacetime dimension $4 = 2^2$ directly from $\dim_{\mathbb{C}} V_2 = 2$.
   - Proves `spinorMat_det_eq_minkowski`:
     $$\det P(p_0, p_1, p_2, p_3) = p_0^2 - p_1^2 - p_2^2 - p_3^2,$$
     forcing Lorentzian signature $(+, -, -, -)$ from the $2 \times 2$ spinor determinant.
   - Proves $\mathrm{SL}(2, \mathbb{C})$ Lorentz covariance (`sl2c_action_hermitian_and_lorentz_invariant`,
     `sl2c_preserves_minkowski_quadratic`), forward causal-cone positivity on spinor outer products
     $P = X X^\dagger$ (`spinorOuterProduct_forward_causal_cone`), and $n$-leg vertex momentum
     additivity for primitive derivations (`primitive_derivation_fin_prod_eigenvalue`,
     `spinorMatVec_finset_sum`).

2. **Section 2 — Metric-Worldline Semigroup, Monoidal Factorization, & Improper FTC Integral**:
   - Formalizes the worldline evolution kernel `worldlineKernel T E = exp(-T * E)` and diagonal
     multi-channel worldline operator `worldlineDiagKernel`, proving identity at $T = 0$,
     1D cobordism semigroup composition $U(T_1 + T_2, E) = U(T_1, E) U(T_2, E)$, monoidal tensor
     factorization $U(T, E_1 + E_2) = U(T, E_1) U(T, E_2)$, and strict UV damping $0 < U(T, E) < 1$
     for $T, E > 0$.
   - Applies the Fundamental Theorem of Calculus (`worldline_interval_integral_eq`) on
     $[T_{\min}, T_{\max}]$ and proves improper $T_{\max} \to +\infty$ convergence
     (`worldline_integral_tendsto_schwingerPropagator`) to the UV-truncated Schwinger propagator
     $$G_{\mathrm{SW}}(z, m^2, T_{\min}) = \frac{\exp\bigl(-(z + m^2) T_{\min}\bigr)}{z + m^2}.$$

3. **Section 3 — Ghost-Freedom, Unit On-Shell Residue, IR Feynman Limit, & Cutkosky Unitarity**:
   - **Ghost-freedom (`schwinger_complex_numerator_ne_zero`, `pauliVillars_ghost_pole_residue_neg_one`)**:
     Proves that $\exp(-(z + m^2) T_{\min})$ is nowhere vanishing on $\mathbb{C}$ and $G_{\mathrm{SW}}$
     is holomorphic on $\mathbb{C} \setminus \{-m^2\}$ with zero residue at any auxiliary scale
     $z = -M_{\mathrm{PV}}^2 \ne -m^2$, whereas Pauli–Villars carries a wrong-sign ghost residue $-1$.
   - **Exact unit on-shell residue (`schwinger_onshell_residue_eq_one`, `unshifted_cutoff_residue_gt_one`)**:
     Proves $(z + m^2) G_{\mathrm{SW}}(z, m^2, T_{\min}) \to 1$ as $z \to -m^2$ for every $T_{\min} \in \mathbb{C}$,
     contrasted with the unshifted regulator $\exp(-z T_{\min})/(z + m^2)$ whose residue is
     $\exp(m^2 T_{\min}) > 1$ for $m^2, T_{\min} > 0$.
   - **Uniform $O(T_{\min}) = O(\mathfrak{E}_*^{-2})$ IR Feynman convergence (`schwinger_ir_feynman_error_bound`,
     `schwinger_uv_scale_feynman_convergence`)**:
     Proves $0 < \frac{1}{z + m^2} - G_{\mathrm{SW}}(z, m^2, T_{\min}) \le T_{\min} = \mathfrak{E}_*^{-2}$
     for $z + m^2 > 0, T_{\min} > 0$.
   - **Pius–Sen Cutkosky optical-theorem unitarity (`cutkosky_optical_phase_space_unitarity`)**:
     Proves exact sub-threshold vanishing ($s \le 4 m^2$), strict super-threshold positivity
     ($s > 4 m^2$), strict boundedness below $\frac{1}{16\pi}$ for $m > 0$, and asymptotic
     convergence to the conformal limit $\frac{1}{16\pi}$ as $s \to +\infty$.
-/

namespace QOU.StandardModel.WorldlineSchwingerFunctorAndSpinorMinkowski

open scoped BigOperators
open Matrix Filter Topology MeasureTheory intervalIntegral

-- ============================================================================
-- § 1. Intrinsic 3+1D Spinor–Minkowski Momentum Space from dim_ℂ V_2 = 2
-- ============================================================================

section SpinorMinkowskiEmergence

/-- Real 4-momentum spinor matrix on `V_2 ⊗ V̄_2 ≅ M_2(ℂ)`:
`P(p₀, p₁, p₂, p₃) = [[p₀ + p₃, p₁ - i p₂], [p₁ + i p₂, p₀ - p₃]]`. -/
def spinorMat (p0 p1 p2 p3 : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(p0 : ℂ) + (p3 : ℂ), (p1 : ℂ) - Complex.I * (p2 : ℂ);
     (p1 : ℂ) + Complex.I * (p2 : ℂ), (p0 : ℂ) - (p3 : ℂ)]

/-- Vector-indexed form of `spinorMat` on `p : Fin 4 → ℝ`. -/
def spinorMatVec (p : Fin 4 → ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  spinorMat (p 0) (p 1) (p 2) (p 3)

/-- Inverse real coordinate projection from any `2 × 2` complex matrix `H` onto `Fin 4 → ℝ`. -/
noncomputable def hermitianCoords (H : Matrix (Fin 2) (Fin 2) ℂ) : Fin 4 → ℝ
  | 0 => ((H 0 0).re + (H 1 1).re) / 2
  | 1 => ((H 0 1).re + (H 1 0).re) / 2
  | 2 => ((H 1 0).im - (H 0 1).im) / 2
  | 3 => ((H 0 0).re - (H 1 1).re) / 2

/-- Minkowski quadratic form `(p₀)² - (p₁)² - (p₂)² - (p₃)²` on `Fin 4 → ℝ`. -/
def minkowskiNormSq (p : Fin 4 → ℝ) : ℝ :=
  (p 0) ^ 2 - (p 1) ^ 2 - (p 2) ^ 2 - (p 3) ^ 2

/-- Every spinor-momentum matrix `spinorMat p0 p1 p2 p3` is strictly Hermitian (`Pᴴ = P`). -/
theorem spinorMat_conjTranspose_eq_self (p0 p1 p2 p3 : ℝ) :
    (spinorMat p0 p1 p2 p3).conjTranspose = spinorMat p0 p1 p2 p3 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [spinorMat, Matrix.conjTranspose_apply]; try ring)

/-- Trace of `spinorMat` recovers twice the timelike energy component `2 p₀`. -/
theorem spinorMat_trace_eq_two_p0 (p0 p1 p2 p3 : ℝ) :
    Matrix.trace (spinorMat p0 p1 p2 p3) = 2 * (p0 : ℂ) := by
  simp only [spinorMat, Matrix.trace, Matrix.diag, Fin.sum_univ_two, Matrix.of_apply,
    Matrix.cons_val_zero, Matrix.cons_val_one]
  ring

/-- Left-inverse recovery of all four real momentum coordinates from `spinorMatVec p`. -/
theorem hermitianCoords_spinorMatVec (p : Fin 4 → ℝ) :
    hermitianCoords (spinorMatVec p) = p := by
  funext μ
  fin_cases μ <;> simp [hermitianCoords, spinorMatVec, spinorMat]

/-- Injectivity of `spinorMat` on `(p₀, p₁, p₂, p₃) ∈ ℝ⁴`. -/
theorem spinorMat_injective {p0 p1 p2 p3 q0 q1 q2 q3 : ℝ}
    (h : spinorMat p0 p1 p2 p3 = spinorMat q0 q1 q2 q3) :
    p0 = q0 ∧ p1 = q1 ∧ p2 = q2 ∧ p3 = q3 := by
  let p : Fin 4 → ℝ := ![p0, p1, p2, p3]
  let q : Fin 4 → ℝ := ![q0, q1, q2, q3]
  have hpq : spinorMatVec p = spinorMatVec q := h
  have hcoords := congrArg hermitianCoords hpq
  rw [hermitianCoords_spinorMatVec, hermitianCoords_spinorMatVec] at hcoords
  exact ⟨congrFun hcoords 0, congrFun hcoords 1, congrFun hcoords 2, congrFun hcoords 3⟩

/-- Every `2 × 2` Hermitian matrix `Hᴴ = H` is uniquely of the form `spinorMatVec (hermitianCoords H)`,
proving that the real vector space of self-adjoint operators on `V_2 = ℂ²` is 4-dimensional. -/
theorem spinorMatVec_hermitianCoords_of_hermitian {H : Matrix (Fin 2) (Fin 2) ℂ}
    (hH : H.conjTranspose = H) :
    spinorMatVec (hermitianCoords H) = H := by
  have h00 : star (H 0 0) = H 0 0 := by
    have := congrArg (fun M => M 0 0) hH
    simpa [Matrix.conjTranspose_apply] using this
  have h11 : star (H 1 1) = H 1 1 := by
    have := congrArg (fun M => M 1 1) hH
    simpa [Matrix.conjTranspose_apply] using this
  have h01 : star (H 1 0) = H 0 1 := by
    have := congrArg (fun M => M 0 1) hH
    simpa [Matrix.conjTranspose_apply] using this
  have h00_im : (H 0 0).im = 0 := by
    have := congrArg Complex.im h00
    simp only [ RCLike.star_def, Complex.conj_im] at this
    linarith
  have h11_im : (H 1 1).im = 0 := by
    have := congrArg Complex.im h11
    simp only [RCLike.star_def, Complex.conj_im] at this
    linarith
  have h01_re : (H 1 0).re = (H 0 1).re := by
    have := congrArg Complex.re h01
    simpa [RCLike.star_def, Complex.conj_re] using this
  have h01_im : -(H 1 0).im = (H 0 1).im := by
    have := congrArg Complex.im h01
    simpa [RCLike.star_def, Complex.conj_im] using this
  ext i j
  fin_cases i <;> fin_cases j
  · apply Complex.ext <;> (simp [spinorMatVec, spinorMat, hermitianCoords, h00_im]; try linarith)
  · apply Complex.ext <;> (simp [spinorMatVec, spinorMat, hermitianCoords, h01_re]; try linarith)
  · apply Complex.ext <;> (simp [spinorMatVec, spinorMat, hermitianCoords, h01_re]; try linarith)
  · apply Complex.ext <;> (simp [spinorMatVec, spinorMat, hermitianCoords, h11_im]; try linarith)

/-- Real additivity of `spinorMatVec`. -/
theorem spinorMatVec_add (p q : Fin 4 → ℝ) :
    spinorMatVec (p + q) = spinorMatVec p + spinorMatVec q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [spinorMatVec, spinorMat]; ring)

/-- Real scalar homogeneity of `spinorMatVec`. -/
theorem spinorMatVec_smul (c : ℝ) (p : Fin 4 → ℝ) :
    spinorMatVec (c • p) = c • spinorMatVec p := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [spinorMatVec, spinorMat, Complex.real_smul]; try ring)

/-- Real submodule of `2 × 2` Hermitian complex matrices `{ H // Hᴴ = H }`. -/
def hermitianSubmodule2 : Submodule ℝ (Matrix (Fin 2) (Fin 2) ℂ) where
  carrier := { H | H.conjTranspose = H }
  zero_mem' := Matrix.conjTranspose_zero
  add_mem' {A B} hA hB := by rw [Set.mem_setOf_eq, Matrix.conjTranspose_add, hA, hB]
  smul_mem' c {A} hA := by
    rw [Set.mem_setOf_eq]
    ext i j
    have hij := congrArg (fun M => M i j) hA
    simp only [Matrix.conjTranspose_apply, Matrix.smul_apply, Complex.real_smul,
      RCLike.star_def, map_mul, Complex.conj_ofReal] at hij ⊢
    rw [hij]

/-- **Intrinsic $4 = 2^2$ Spacetime Linear Equivalence**:
`spinorMatVec` induces an exact `ℝ`-linear isomorphism between `Fin 4 → ℝ` and the Hermitian
subspace `hermitianSubmodule2` of `Matrix (Fin 2) (Fin 2) ℂ`. -/
noncomputable def spinorHermitianLinearEquiv : (Fin 4 → ℝ) ≃ₗ[ℝ] hermitianSubmodule2 where
  toFun p := ⟨spinorMatVec p, spinorMat_conjTranspose_eq_self (p 0) (p 1) (p 2) (p 3)⟩
  map_add' p q := Subtype.ext (spinorMatVec_add p q)
  map_smul' c p := Subtype.ext (spinorMatVec_smul c p)
  invFun H := hermitianCoords H.1
  left_inv p := hermitianCoords_spinorMatVec p
  right_inv H := Subtype.ext (spinorMatVec_hermitianCoords_of_hermitian H.2)

/-- **Forced Lorentzian Signature `(+, -, -, -)` from $\dim_{\mathbb{C}} V_2 = 2$**:
The `2 × 2` determinant of `spinorMat p0 p1 p2 p3` equals the `3+1D` Minkowski quadratic form
`p₀² - p₁² - p₂² - p₃²`. -/
theorem spinorMat_det_eq_minkowski (p0 p1 p2 p3 : ℝ) :
    Matrix.det (spinorMat p0 p1 p2 p3) =
      ((p0 ^ 2 - p1 ^ 2 - p2 ^ 2 - p3 ^ 2 : ℝ) : ℂ) := by
  rw [Matrix.det_fin_two]
  simp only [spinorMat, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  calc ((p0 : ℂ) + (p3 : ℂ)) * ((p0 : ℂ) - (p3 : ℂ)) -
        ((p1 : ℂ) - Complex.I * (p2 : ℂ)) * ((p1 : ℂ) + Complex.I * (p2 : ℂ))
      = (p0 : ℂ) ^ 2 - (p3 : ℂ) ^ 2 - ((p1 : ℂ) ^ 2 - Complex.I ^ 2 * (p2 : ℂ) ^ 2) := by ring
    _ = (p0 : ℂ) ^ 2 - (p1 : ℂ) ^ 2 - (p2 : ℂ) ^ 2 - (p3 : ℂ) ^ 2 := by
        rw [Complex.I_sq]
        ring
    _ = ((p0 ^ 2 - p1 ^ 2 - p2 ^ 2 - p3 ^ 2 : ℝ) : ℂ) := by push_cast; ring

/-- **$\mathrm{SL}(2, \mathbb{C})$ Congruence Preserves Hermiticity and Determinant**:
For any `L, P ∈ M_2(ℂ)` with `L.det = 1`, `(L * P * Lᴴ)ᴴ = L * Pᴴ * Lᴴ` and
`det(L * P * Lᴴ) = det P`. -/
theorem sl2c_action_hermitian_and_lorentz_invariant (L P : Matrix (Fin 2) (Fin 2) ℂ)
    (hL : L.det = 1) :
    (L * P * L.conjTranspose).conjTranspose = L * P.conjTranspose * L.conjTranspose ∧
      Matrix.det (L * P * L.conjTranspose) = Matrix.det P := by
  refine ⟨?_, ?_⟩
  · rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
      Matrix.mul_assoc]
  · rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_conjTranspose, hL, star_one, one_mul, mul_one]

/-- **Induced $\mathrm{SL}(2, \mathbb{C}) \to \mathrm{O}(1, 3)$ Lorentz Isometry on $\mathbb{R}^4$**:
For any `L ∈ M_2(ℂ)` with `L.det = 1` and `p : Fin 4 → ℝ`, the transformed 4-momentum
`p' = hermitianCoords (L * spinorMatVec p * Lᴴ)` satisfies `spinorMatVec p' = L * spinorMatVec p * Lᴴ`
and preserves `minkowskiNormSq` identically. -/
theorem sl2c_preserves_minkowski_quadratic (L : Matrix (Fin 2) (Fin 2) ℂ) (hL : L.det = 1)
    (p : Fin 4 → ℝ) :
    let p' := hermitianCoords (L * spinorMatVec p * L.conjTranspose)
    spinorMatVec p' = L * spinorMatVec p * L.conjTranspose ∧
      minkowskiNormSq p' = minkowskiNormSq p := by
  intro p'
  have hP_herm : (spinorMatVec p).conjTranspose = spinorMatVec p :=
    spinorMat_conjTranspose_eq_self (p 0) (p 1) (p 2) (p 3)
  obtain ⟨hconj, hdet⟩ := sl2c_action_hermitian_and_lorentz_invariant L (spinorMatVec p) hL
  rw [hP_herm] at hconj
  have hrec : spinorMatVec p' = L * spinorMatVec p * L.conjTranspose :=
    spinorMatVec_hermitianCoords_of_hermitian hconj
  refine ⟨hrec, ?_⟩
  have hdet_eq : Matrix.det (spinorMatVec p') = Matrix.det (spinorMatVec p) := by
    rw [hrec, hdet]
  unfold spinorMatVec at hdet_eq
  rw [spinorMat_det_eq_minkowski, spinorMat_det_eq_minkowski] at hdet_eq
  exact Complex.ofReal_injective hdet_eq

/-- **Forward Causal Cone Positivity on Spinor Outer Products $P = X X^\dagger$**:
For every `X ∈ M_2(ℂ)`, `X * Xᴴ` is Hermitian, its trace has non-negative real part
`∑_{i,j} ‖X_{ij}‖² ≥ 0`, and its determinant equals `(Complex.normSq (det X) : ℂ)` with real part
`Complex.normSq (det X) ≥ 0`. -/
theorem spinorOuterProduct_forward_causal_cone (X : Matrix (Fin 2) (Fin 2) ℂ) :
    (X * X.conjTranspose).conjTranspose = X * X.conjTranspose ∧
      0 ≤ (Matrix.trace (X * X.conjTranspose)).re ∧
      Matrix.det (X * X.conjTranspose) = (Complex.normSq (Matrix.det X) : ℂ) ∧
      0 ≤ (Matrix.det (X * X.conjTranspose)).re := by
  have hherm : (X * X.conjTranspose).conjTranspose = X * X.conjTranspose := by
    rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  have htr : (Matrix.trace (X * X.conjTranspose)).re =
      ∑ i : Fin 2, ∑ j : Fin 2, Complex.normSq (X i j) := by
    simp only [Matrix.trace, Matrix.diag, Matrix.mul_apply, Matrix.conjTranspose_apply,
      RCLike.star_def, Complex.mul_conj, Fin.sum_univ_two, Complex.add_re, Complex.ofReal_re]
  have htr_nn : 0 ≤ (Matrix.trace (X * X.conjTranspose)).re := by
    rw [htr]
    exact Finset.sum_nonneg (fun i _ => Finset.sum_nonneg (fun j _ => Complex.normSq_nonneg _))
  have hdet : Matrix.det (X * X.conjTranspose) = (Complex.normSq (Matrix.det X) : ℂ) := by
    rw [Matrix.det_mul, Matrix.det_conjTranspose, RCLike.star_def, Complex.mul_conj]
  refine ⟨hherm, htr_nn, hdet, ?_⟩
  rw [hdet, Complex.ofReal_re]
  exact Complex.normSq_nonneg (Matrix.det X)

/-- Additive conservation of `spinorMatVec` across any finite leg set `s : Finset ι`. -/
theorem spinorMatVec_finset_sum {ι : Type*} (s : Finset ι) (p : ι → Fin 4 → ℝ) :
    spinorMatVec (fun μ => ∑ a ∈ s, p a μ) = ∑ a ∈ s, spinorMatVec (p a) := by
  have hfun : (fun μ => ∑ a ∈ s, p a μ) = ∑ a ∈ s, p a := by
    funext μ
    simp [Finset.sum_apply]
  rw [hfun]
  clear hfun
  induction s using Finset.cons_induction with
  | empty =>
    ext i j
    fin_cases i <;> fin_cases j <;> simp [spinorMatVec, spinorMat]
  | cons a t _hat ih =>
    rw [Finset.sum_cons, Finset.sum_cons, spinorMatVec_add, ih]

/-- **Primitive Derivation $n$-Leg Eigenvalue Additivity (Hopf Comultiplication Conservation Law)**:
If `D : A → A` is an additive derivation (`D 1 = 0` and `D(x * y) = D x * y + x * D y`) on a
commutative ring `A`, and `e : Fin n → A` are eigenmodes satisfying `D (e a) = k a * e a`, then
`D` acts on the `n`-fold vertex product `∏ a, e a` with additive eigenvalue `∑ a, k a`. -/
theorem primitive_derivation_fin_prod_eigenvalue {A : Type*} [CommRing A]
    (D : A → A) (hD1 : D 1 = 0) (hLeib : ∀ x y : A, D (x * y) = D x * y + x * D y) :
    ∀ (n : ℕ) (e k : Fin n → A), (∀ a : Fin n, D (e a) = k a * e a) →
      D (∏ a : Fin n, e a) = (∑ a : Fin n, k a) * ∏ a : Fin n, e a := by
  intro n
  induction n with
  | zero =>
    intro e k _
    simp [hD1]
  | succ m ih =>
    intro e k heig
    rw [Fin.prod_univ_succ, Fin.sum_univ_succ, hLeib, heig 0,
      ih (fun j => e j.succ) (fun j => k j.succ) (fun j => heig j.succ)]
    ring

end SpinorMinkowskiEmergence

-- ============================================================================
-- § 2. Metric-Worldline Semigroup, Monoidal Laws, & Improper FTC Integral
-- ============================================================================

section MetricWorldlineSemigroup

/-- Real metric-worldline heat-kernel evolution `U(T, E) = exp(-T · E)`. -/
noncomputable def worldlineKernel (T E : ℝ) : ℝ :=
  Real.exp (-T * E)

/-- Multi-channel diagonal metric-worldline operator `diag_i exp(-T · E_i)`. -/
noncomputable def worldlineDiagKernel {ι : Type*} [DecidableEq ι] (T : ℝ) (E : ι → ℝ) :
    Matrix ι ι ℝ :=
  Matrix.diagonal (fun i => worldlineKernel T (E i))

/-- UV-truncated real Schwinger worldline propagator
`G_SW(z, m², T_min) = exp(-(z + m²) T_min) / (z + m²)`. -/
noncomputable def schwingerPropagatorReal (z mSq Tmin : ℝ) : ℝ :=
  Real.exp (-(z + mSq) * Tmin) / (z + mSq)

/-- Identity, 1D cobordism semigroup composition, monoidal tensor factorization, and strict UV
damping (`0 < U(T, E) < 1` for `T, E > 0`) of `worldlineKernel`. -/
theorem worldlineKernel_functor_laws :
    (∀ E : ℝ, worldlineKernel 0 E = 1) ∧
    (∀ T₁ T₂ E : ℝ, worldlineKernel (T₁ + T₂) E = worldlineKernel T₁ E * worldlineKernel T₂ E) ∧
    (∀ T E₁ E₂ : ℝ, worldlineKernel T (E₁ + E₂) = worldlineKernel T E₁ * worldlineKernel T E₂) ∧
    (∀ T E : ℝ, 0 < T → 0 < E → 0 < worldlineKernel T E ∧ worldlineKernel T E < 1) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro E
    simp [worldlineKernel]
  · intro T₁ T₂ E
    unfold worldlineKernel
    rw [show -(T₁ + T₂) * E = (-T₁ * E) + (-T₂ * E) by ring, Real.exp_add]
  · intro T E₁ E₂
    unfold worldlineKernel
    rw [show -T * (E₁ + E₂) = (-T * E₁) + (-T * E₂) by ring, Real.exp_add]
  · intro T E hT hE
    unfold worldlineKernel
    refine ⟨Real.exp_pos _, ?_⟩
    rw [Real.exp_lt_one_iff]
    nlinarith

/-- Matrix-level identity and semigroup functoriality of `worldlineDiagKernel`. -/
theorem worldlineDiagKernel_semigroup {ι : Type*} [Fintype ι] [DecidableEq ι]
    (T₁ T₂ : ℝ) (E : ι → ℝ) :
    worldlineDiagKernel 0 E = 1 ∧
      worldlineDiagKernel (T₁ + T₂) E =
        worldlineDiagKernel T₁ E * worldlineDiagKernel T₂ E := by
  refine ⟨?_, ?_⟩
  · unfold worldlineDiagKernel
    simp [(worldlineKernel_functor_laws).1]
  · unfold worldlineDiagKernel
    rw [Matrix.diagonal_mul_diagonal]
    congr 1
    funext i
    exact (worldlineKernel_functor_laws).2.1 T₁ T₂ (E i)

/-- **Exact Finite-Window Worldline Integral via Fundamental Theorem of Calculus**:
For any `A ≠ 0` and endpoints `Tmin, Tmax ∈ ℝ`,
`∫ T in Tmin..Tmax, exp(-T * A) = (exp(-Tmin * A) - exp(-Tmax * A)) / A`. -/
theorem worldline_interval_integral_eq {A : ℝ} (hA : A ≠ 0) (Tmin Tmax : ℝ) :
    (∫ T in Tmin..Tmax, Real.exp (-T * A)) =
      (Real.exp (-Tmin * A) - Real.exp (-Tmax * A)) / A := by
  let F : ℝ → ℝ := fun T => -(1 / A) * Real.exp (-T * A)
  have hderiv : ∀ T ∈ Set.uIcc Tmin Tmax, HasDerivAt F (Real.exp (-T * A)) T := by
    intro T _
    have hlin : HasDerivAt (fun x : ℝ => -x * A) (-A) T := by
      simpa using ((hasDerivAt_id T).neg).mul_const A
    have hexp : HasDerivAt (fun x : ℝ => Real.exp (-x * A)) (Real.exp (-T * A) * (-A)) T :=
      hlin.exp
    have hF : HasDerivAt F (-(1 / A) * (Real.exp (-T * A) * (-A))) T :=
      hexp.const_mul (-(1 / A))
    convert hF using 1
    field_simp [hA]
  have hint : IntervalIntegrable (fun T : ℝ => Real.exp (-T * A)) volume Tmin Tmax :=
    (Real.continuous_exp.comp (continuous_id.neg.mul continuous_const)).intervalIntegrable Tmin Tmax
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint]
  dsimp [F]
  ring

/-- **Improper Worldline Integral Convergence (`T_max → +∞`) to the Schwinger Propagator**:
For `0 < z + mSq` and any `Tmin ∈ ℝ`, as `Tmax → +∞` (`atTop`), the worldline proper-time integral
`∫ T in Tmin..Tmax, exp(-T * (z + mSq))` converges to `schwingerPropagatorReal z mSq Tmin`. -/
theorem worldline_integral_tendsto_schwingerPropagator {z mSq : ℝ} (hA : 0 < z + mSq)
    (Tmin : ℝ) :
    Tendsto (fun Tmax : ℝ => ∫ T in Tmin..Tmax, Real.exp (-T * (z + mSq)))
      atTop (𝓝 (schwingerPropagatorReal z mSq Tmin)) := by
  have hAne : z + mSq ≠ 0 := ne_of_gt hA
  have hfn_eq : (fun Tmax : ℝ => ∫ T in Tmin..Tmax, Real.exp (-T * (z + mSq))) =
      fun Tmax : ℝ => (Real.exp (-(z + mSq) * Tmin) - Real.exp (-(z + mSq) * Tmax)) / (z + mSq) := by
    funext Tmax
    rw [worldline_interval_integral_eq hAne Tmin Tmax,
      show -Tmin * (z + mSq) = -(z + mSq) * Tmin by ring,
      show -Tmax * (z + mSq) = -(z + mSq) * Tmax by ring]
  rw [hfn_eq]
  have hexp_zero : Tendsto (fun Tmax : ℝ => Real.exp (-(z + mSq) * Tmax)) atTop (𝓝 0) :=
    Real.tendsto_exp_atBot.comp
      (Filter.Tendsto.const_mul_atTop_of_neg (neg_lt_zero.mpr hA) tendsto_id)
  have hnum : Tendsto (fun Tmax : ℝ => Real.exp (-(z + mSq) * Tmin) - Real.exp (-(z + mSq) * Tmax))
      atTop (𝓝 (Real.exp (-(z + mSq) * Tmin) - 0)) :=
    tendsto_const_nhds.sub hexp_zero
  have hdiv := hnum.div_const (z + mSq)
  simpa [sub_zero, schwingerPropagatorReal] using hdiv

end MetricWorldlineSemigroup

-- ============================================================================
-- § 3. Ghost-Freedom, Unit On-Shell Residue, IR Limit, & Cutkosky Unitarity
-- ============================================================================

section GhostFreedomResidueAndUnitarity

/-- Complexified UV-truncated Schwinger propagator
`G_SW(z, m², T_min) = exp(-(z + m²) T_min) / (z + m²)` on `ℂ`. -/
noncomputable def schwingerPropagatorComplex (z mSq Tmin : ℂ) : ℂ :=
  Complex.exp (-(z + mSq) * Tmin) / (z + mSq)

/-- Pauli–Villars subtracted propagator `(z + m²)⁻¹ - (z + M_PV²)⁻¹` for comparison. -/
noncomputable def pauliVillarsPropagator (z mSq MpvSq : ℂ) : ℂ :=
  1 / (z + mSq) - 1 / (z + MpvSq)

/-- Unshifted exponential regulator `exp(-z T_min) / (z + m²)` lacking the mass-shell shift. -/
noncomputable def unshiftedCutoffPropagator (z mSq Tmin : ℝ) : ℝ :=
  Real.exp (-z * Tmin) / (z + mSq)

/-- **1. Complete Absence of Ghost Poles or Zeros in `ℂ`**:
The complex worldline numerator `exp(-(z + m²) T_min)` never vanishes anywhere in `ℂ`, and
`schwingerPropagatorComplex` is differentiable (holomorphic) and non-zero at every off-shell
point `z + m² ≠ 0`. -/
theorem schwinger_complex_numerator_ne_zero (z mSq Tmin : ℂ) :
    Complex.exp (-(z + mSq) * Tmin) ≠ 0 ∧
      (z + mSq ≠ 0 →
        schwingerPropagatorComplex z mSq Tmin ≠ 0 ∧
        DifferentiableAt ℂ (fun w => schwingerPropagatorComplex w mSq Tmin) z) := by
  refine ⟨Complex.exp_ne_zero _, ?_⟩
  intro hz
  refine ⟨div_ne_zero (Complex.exp_ne_zero _) hz, ?_⟩
  unfold schwingerPropagatorComplex
  have hnum : DifferentiableAt ℂ (fun w : ℂ => Complex.exp (-(w + mSq) * Tmin)) z :=
    (((differentiableAt_id.add (differentiableAt_const mSq)).neg).mul
      (differentiableAt_const Tmin)).cexp
  have hden : DifferentiableAt ℂ (fun w : ℂ => w + mSq) z :=
    differentiableAt_id.add (differentiableAt_const mSq)
  exact hnum.div hden hz

/-- **Contrast with Pauli–Villars Wrong-Sign Ghost Pole (`Res = -1` vs `Res = 0`)**:
For `MpvSq ≠ mSq`, Pauli–Villars rationalizes to `(MpvSq - mSq) / ((z + mSq)(z + MpvSq))` and has
residue **`-1`** at the ghost pole `z = -MpvSq`, whereas `(z + MpvSq) * G_SW(z, mSq, Tmin)`
converges to **`0`** at `z = -MpvSq` (complete absence of ghost poles). -/
theorem pauliVillars_ghost_pole_residue_neg_one {mSq MpvSq Tmin : ℂ} (hdiff : MpvSq ≠ mSq) :
    (∀ z : ℂ, z + mSq ≠ 0 → z + MpvSq ≠ 0 →
      pauliVillarsPropagator z mSq MpvSq = (MpvSq - mSq) / ((z + mSq) * (z + MpvSq))) ∧
    Tendsto (fun z : ℂ => (z + MpvSq) * pauliVillarsPropagator z mSq MpvSq)
      (𝓝[≠] (-MpvSq)) (𝓝 (-1 : ℂ)) ∧
    Tendsto (fun z : ℂ => (z + MpvSq) * schwingerPropagatorComplex z mSq Tmin)
      (𝓝 (-MpvSq)) (𝓝 (0 : ℂ)) := by
  refine ⟨?_, ?_, ?_⟩
  · intro z hm hM
    unfold pauliVillarsPropagator
    field_simp [hm, hM]
    ring
  · have hcont : Tendsto (fun z : ℂ => (z + MpvSq) / (z + mSq) - 1)
        (𝓝 (-MpvSq)) (𝓝 (-1 : ℂ)) := by
      have hden_ne : (-MpvSq) + mSq ≠ 0 := by
        intro hzero
        apply hdiff
        linear_combination -hzero
      have hq : Tendsto (fun z : ℂ => (z + MpvSq) / (z + mSq)) (𝓝 (-MpvSq)) (𝓝 0) := by
        have hnum_t : Tendsto (fun z : ℂ => z + MpvSq) (𝓝 (-MpvSq)) (𝓝 (-MpvSq + MpvSq)) :=
          (continuous_id.add continuous_const).tendsto (-MpvSq)
        have hden_t : Tendsto (fun z : ℂ => z + mSq) (𝓝 (-MpvSq)) (𝓝 (-MpvSq + mSq)) :=
          (continuous_id.add continuous_const).tendsto (-MpvSq)
        simpa using hnum_t.div hden_t hden_ne
      simpa using hq.sub tendsto_const_nhds
    refine (hcont.mono_left nhdsWithin_le_nhds).congr' ?_
    filter_upwards [self_mem_nhdsWithin] with z hz
    have hzne : z ≠ -MpvSq := Set.mem_compl_singleton_iff.mp hz
    have hzM : z + MpvSq ≠ 0 := by
      intro h0
      apply hzne
      linear_combination h0
    unfold pauliVillarsPropagator
    rw [mul_sub, mul_one_div, mul_one_div_cancel hzM]
  · have hden_ne : (-MpvSq) + mSq ≠ 0 := by
      intro h0
      apply hdiff
      linear_combination -h0
    have hcont_sw : ContinuousAt (fun z : ℂ => schwingerPropagatorComplex z mSq Tmin) (-MpvSq) :=
      ((schwinger_complex_numerator_ne_zero (-MpvSq) mSq Tmin).2 hden_ne).2.continuousAt
    have hlin_c : ContinuousAt (fun z : ℂ => z + MpvSq) (-MpvSq) :=
      (continuous_id.add continuous_const).continuousAt
    have hprod := (hlin_c.mul hcont_sw).tendsto
    simpa using hprod

/-- **2. Exact Unit On-Shell S-Matrix Residue Independent of `T_min`**:
For all `mSq, Tmin ∈ ℂ`:
(i) `(z + mSq) * schwingerPropagatorComplex z mSq Tmin = Complex.exp (-(z + mSq) * Tmin)` for `z + mSq ≠ 0`,
(ii) `lim_{z → -mSq, z ≠ -mSq} (z + mSq) * schwingerPropagatorComplex z mSq Tmin = 1` identically
for **every** `Tmin ∈ ℂ`. -/
theorem schwinger_onshell_residue_eq_one (mSq Tmin : ℂ) :
    (∀ z : ℂ, z + mSq ≠ 0 →
      (z + mSq) * schwingerPropagatorComplex z mSq Tmin = Complex.exp (-(z + mSq) * Tmin)) ∧
    Tendsto (fun z : ℂ => (z + mSq) * schwingerPropagatorComplex z mSq Tmin)
      (𝓝[≠] (-mSq)) (𝓝 (1 : ℂ)) := by
  have hident : ∀ z : ℂ, z + mSq ≠ 0 →
      (z + mSq) * schwingerPropagatorComplex z mSq Tmin = Complex.exp (-(z + mSq) * Tmin) := by
    intro z hz
    unfold schwingerPropagatorComplex
    exact mul_div_cancel₀ _ hz
  refine ⟨hident, ?_⟩
  have hexp_lim : Tendsto (fun z : ℂ => Complex.exp (-(z + mSq) * Tmin)) (𝓝 (-mSq)) (𝓝 1) := by
    have hcont : Continuous (fun z : ℂ => Complex.exp (-(z + mSq) * Tmin)) :=
      (((continuous_id.add continuous_const).neg).mul continuous_const).cexp
    simpa using hcont.tendsto (-mSq)
  refine (hexp_lim.mono_left nhdsWithin_le_nhds).congr' ?_
  filter_upwards [self_mem_nhdsWithin] with z hz
  have hzne : z ≠ -mSq := Set.mem_compl_singleton_iff.mp hz
  have hzm : z + mSq ≠ 0 := by
    intro h0
    apply hzne
    linear_combination h0
  exact (hident z hzm).symm

/-- **Contrast with Unshifted Cutoff (`Res = exp(m² T_min) > 1` Distortion)**:
Without the full worldline operator shift `z + m²` in the exponent, the naive regulator
`exp(-z T_min) / (z + m²)` has distorted on-shell residue `exp(m² T_min) > 1` whenever `m² > 0`
and `T_min > 0`. -/
theorem unshifted_cutoff_residue_gt_one {mSq Tmin : ℝ} (hm : 0 < mSq) (hT : 0 < Tmin) :
    (∀ z : ℝ, z + mSq ≠ 0 →
      (z + mSq) * unshiftedCutoffPropagator z mSq Tmin = Real.exp (-z * Tmin)) ∧
    1 < Real.exp (-(-mSq) * Tmin) := by
  refine ⟨?_, ?_⟩
  · intro z hz
    unfold unshiftedCutoffPropagator
    exact mul_div_cancel₀ _ hz
  · rw [Real.one_lt_exp_iff]
    nlinarith

/-- **3. Uniform $O(T_{\min})$ Infrared Convergence to the Continuum Feynman Propagator**:
For `0 < z + mSq` and `0 < Tmin`, the difference between the continuum propagator `(z + mSq)⁻¹`
and `schwingerPropagatorReal z mSq Tmin` is strictly positive and bounded above by `Tmin`
uniformly across all Euclidean momenta `z + mSq > 0`. -/
theorem schwinger_ir_feynman_error_bound {z mSq Tmin : ℝ} (hA : 0 < z + mSq) (hT : 0 < Tmin) :
    1 / (z + mSq) - schwingerPropagatorReal z mSq Tmin =
      (1 - Real.exp (-(z + mSq) * Tmin)) / (z + mSq) ∧
    0 < 1 / (z + mSq) - schwingerPropagatorReal z mSq Tmin ∧
    1 / (z + mSq) - schwingerPropagatorReal z mSq Tmin ≤ Tmin := by
  have hdiff : 1 / (z + mSq) - schwingerPropagatorReal z mSq Tmin =
      (1 - Real.exp (-(z + mSq) * Tmin)) / (z + mSq) := by
    unfold schwingerPropagatorReal
    rw [sub_div]
  refine ⟨hdiff, ?_, ?_⟩
  · rw [hdiff]
    apply div_pos _ hA
    have hexp_lt : Real.exp (-(z + mSq) * Tmin) < 1 := by
      rw [Real.exp_lt_one_iff]
      nlinarith
    linarith
  · rw [hdiff, div_le_iff₀ hA]
    have hexp_lb := Real.add_one_le_exp (-(z + mSq) * Tmin)
    linarith

/-- **Substrate UV Scale Form (`T_min = 1 / E_*²`) and `E_* → +∞` Convergence**:
Setting `T_min = 1 / E_*²` for `0 < E_*` bounds `0 < (z + m²)⁻¹ - G_SW(z, m², 1 / E_*²) ≤ 1 / E_*²`,
and `G_SW(z, m², 1 / E_*²) → (z + m²)⁻¹` as `E_* → +∞`. -/
theorem schwinger_uv_scale_feynman_convergence {z mSq : ℝ} (hA : 0 < z + mSq) :
    (∀ EStar : ℝ, 0 < EStar →
      0 < 1 / (z + mSq) - schwingerPropagatorReal z mSq (1 / EStar ^ 2) ∧
      1 / (z + mSq) - schwingerPropagatorReal z mSq (1 / EStar ^ 2) ≤ 1 / EStar ^ 2) ∧
    Tendsto (fun EStar : ℝ => schwingerPropagatorReal z mSq (1 / EStar ^ 2))
      atTop (𝓝 (1 / (z + mSq))) := by
  refine ⟨?_, ?_⟩
  · intro EStar hE
    have hT : 0 < 1 / EStar ^ 2 := by positivity
    obtain ⟨_, hpos, hle⟩ := schwinger_ir_feynman_error_bound hA hT
    exact ⟨hpos, hle⟩
  · have hinv_sq : Tendsto (fun EStar : ℝ => 1 / EStar ^ 2) atTop (𝓝 0) := by
      have hp : Tendsto (fun EStar : ℝ => EStar ^ 2) atTop atTop :=
        tendsto_pow_atTop (by norm_num : (2 : ℕ) ≠ 0)
      simpa [one_div] using tendsto_inv_atTop_zero.comp hp
    have hcont : Continuous (fun T : ℝ => schwingerPropagatorReal z mSq T) := by
      unfold schwingerPropagatorReal
      exact (Real.continuous_exp.comp (continuous_const.mul continuous_id)).div_const (z + mSq)
    have hlim := (hcont.tendsto 0).comp hinv_sq
    simpa [schwingerPropagatorReal] using hlim

/-- Two-body Pius–Sen / Cutkosky absorptive phase-space spectral density
`ρ₂(s, m) = 0` for `s ≤ 4 m²` and `(1 / (16 π)) * √(1 - 4 m² / s)` for `s > 4 m²`. -/
noncomputable def cutkoskyPhaseSpace2 (s m : ℝ) : ℝ :=
  if s ≤ 4 * m ^ 2 then 0 else (1 / (16 * Real.pi)) * Real.sqrt (1 - 4 * m ^ 2 / s)

/-- One-loop absorptive imaginary part `Im M_{1-loop}(s) = λ² · ρ₂(s, m)`. -/
noncomputable def oneLoopAbsorptiveIm (lam s m : ℝ) : ℝ :=
  lam ^ 2 * cutkoskyPhaseSpace2 s m

/-- **4. Pius–Sen Cutkosky Discontinuity Unitarity, Sub-Threshold Hermiticity, & Conformal Limit**:
1. Sub-threshold hermiticity: for all `s ≤ 4 m²`, `ρ₂(s, m) = 0` and `Im M_{1-loop}(s) = 0`.
2. Super-threshold optical-theorem positivity & ceiling: for `m ≥ 0` and `s > 4 m²`,
   `0 < ρ₂(s, m) ≤ 1 / (16 π)` (with strict `< 1 / (16 π)` for `m > 0`), and `Im M_{1-loop}(s) > 0`
   for every non-zero coupling `λ ≠ 0`.
3. UV conformal limit: `lim_{s → +∞} ρ₂(s, m) = 1 / (16 π)`. -/
theorem cutkosky_optical_phase_space_unitarity (m : ℝ) :
    (∀ lam s : ℝ, s ≤ 4 * m ^ 2 →
      cutkoskyPhaseSpace2 s m = 0 ∧ oneLoopAbsorptiveIm lam s m = 0) ∧
    (0 ≤ m → ∀ s : ℝ, 4 * m ^ 2 < s →
      0 < cutkoskyPhaseSpace2 s m ∧
      cutkoskyPhaseSpace2 s m ≤ 1 / (16 * Real.pi) ∧
      (0 < m → cutkoskyPhaseSpace2 s m < 1 / (16 * Real.pi)) ∧
      (∀ lam : ℝ, lam ≠ 0 → 0 < oneLoopAbsorptiveIm lam s m)) ∧
    Tendsto (fun s : ℝ => cutkoskyPhaseSpace2 s m) atTop (𝓝 (1 / (16 * Real.pi))) := by
  have h16pi_pos : 0 < 1 / (16 * Real.pi) := by
    have hpi := Real.pi_pos
    positivity
  refine ⟨?_, ?_, ?_⟩
  · intro lam s hs
    have h0 : cutkoskyPhaseSpace2 s m = 0 := if_pos hs
    exact ⟨h0, by simp [oneLoopAbsorptiveIm, h0]⟩
  · intro _hm s hs
    have hnot : ¬ (s ≤ 4 * m ^ 2) := not_le.mpr hs
    have hs_pos : 0 < s := by
      have hm2 : 0 ≤ 4 * m ^ 2 := by positivity
      linarith
    have hrad_pos : 0 < 1 - 4 * m ^ 2 / s := by
      rw [sub_pos, div_lt_one hs_pos]
      exact hs
    have hrad_le_one : 1 - 4 * m ^ 2 / s ≤ 1 := by
      have hdiv_nn : 0 ≤ 4 * m ^ 2 / s := div_nonneg (by positivity) (le_of_lt hs_pos)
      linarith
    have hsqrt_pos : 0 < Real.sqrt (1 - 4 * m ^ 2 / s) := Real.sqrt_pos.mpr hrad_pos
    have hsqrt_le : Real.sqrt (1 - 4 * m ^ 2 / s) ≤ 1 := by
      calc Real.sqrt (1 - 4 * m ^ 2 / s)
          ≤ Real.sqrt 1 := Real.sqrt_le_sqrt hrad_le_one
        _ = 1 := Real.sqrt_one
    have hrho_eq : cutkoskyPhaseSpace2 s m =
        (1 / (16 * Real.pi)) * Real.sqrt (1 - 4 * m ^ 2 / s) := if_neg hnot
    have hrho_pos : 0 < cutkoskyPhaseSpace2 s m := by
      rw [hrho_eq]
      exact mul_pos h16pi_pos hsqrt_pos
    refine ⟨hrho_pos, ?_, ?_, ?_⟩
    · rw [hrho_eq]
      calc (1 / (16 * Real.pi)) * Real.sqrt (1 - 4 * m ^ 2 / s)
          ≤ (1 / (16 * Real.pi)) * 1 := mul_le_mul_of_nonneg_left hsqrt_le (le_of_lt h16pi_pos)
        _ = 1 / (16 * Real.pi) := mul_one _
    · intro hm_pos
      rw [hrho_eq]
      have hdiv_pos : 0 < 4 * m ^ 2 / s := div_pos (by positivity) hs_pos
      have hrad_lt : 1 - 4 * m ^ 2 / s < 1 := by linarith
      have hsqrt_lt : Real.sqrt (1 - 4 * m ^ 2 / s) < 1 := by
        calc Real.sqrt (1 - 4 * m ^ 2 / s)
            < Real.sqrt 1 := Real.sqrt_lt_sqrt (le_of_lt hrad_pos) hrad_lt
          _ = 1 := Real.sqrt_one
      calc (1 / (16 * Real.pi)) * Real.sqrt (1 - 4 * m ^ 2 / s)
          < (1 / (16 * Real.pi)) * 1 := mul_lt_mul_of_pos_left hsqrt_lt h16pi_pos
        _ = 1 / (16 * Real.pi) := mul_one _
    · intro lam hlam
      unfold oneLoopAbsorptiveIm
      exact mul_pos (sq_pos_of_ne_zero hlam) hrho_pos
  · have hq_zero : Tendsto (fun s : ℝ => 4 * m ^ 2 / s) atTop (𝓝 0) := by
      have hmul : Tendsto (fun s : ℝ => (4 * m ^ 2) * s⁻¹) atTop (𝓝 ((4 * m ^ 2) * 0)) :=
        (tendsto_const_nhds (x := 4 * m ^ 2)).mul tendsto_inv_atTop_zero
      simpa [div_eq_mul_inv] using hmul
    have hrad_one : Tendsto (fun s : ℝ => 1 - 4 * m ^ 2 / s) atTop (𝓝 1) := by
      simpa using tendsto_const_nhds.sub hq_zero
    have hsqrt_one : Tendsto (fun s : ℝ => Real.sqrt (1 - 4 * m ^ 2 / s)) atTop (𝓝 1) := by
      have h := (Real.continuous_sqrt.tendsto 1).comp hrad_one
      simpa [Real.sqrt_one] using h
    have hprod : Tendsto (fun s : ℝ => (1 / (16 * Real.pi)) * Real.sqrt (1 - 4 * m ^ 2 / s))
        atTop (𝓝 (1 / (16 * Real.pi))) := by
      simpa using tendsto_const_nhds.mul hsqrt_one
    refine hprod.congr' ?_
    filter_upwards [Filter.eventually_ge_atTop (4 * m ^ 2 + 1)] with s hs
    have hgt : 4 * m ^ 2 < s := by linarith
    exact (if_neg (not_le.mpr hgt)).symm

end GhostFreedomResidueAndUnitarity

end QOU.StandardModel.WorldlineSchwingerFunctorAndSpinorMinkowski
