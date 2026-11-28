import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Off-Shell 3-Edge Ribbon Pant, $\mathfrak{su}(3)_c$ Fierz–Jacobi Algebra, and Bern–Kosower Non-Abelian 3-Gluon Vertex

Unconditional Lean 4 formalization of the algebraic 3-edge ribbon pant colour factor and
Bern–Kosower cubic Yang–Mills vertex without Faddeev–Popov ghost fields (Bean `qou-t3zb`):

1. **§1 — Ribbon Pant Cyclic Colour Factor, $\mathfrak{su}(3)_c$ Gell-Mann Basis, Fierz Completeness,
   and Contracted Jacobi Identity:**
   - Defines the associative commutator `[A, B] = A B - B A` and cyclic 3-boundary ribbon trace
     functional `traceStructureMap A B C = tr([A, B] C)` over any commutative ring `R`, proving
     cyclic invariance, full $S_3$ oddness under transpositions, and the associative Jacobi identity.
   - Instantiates the 8 fundamental $\mathfrak{su}(3)_c$ generators $T^a = \frac{1}{2}\lambda_a$
     (`su3Gen : Fin 8 → Matrix (Fin 3) (Fin 3) ℂ`) and structure constants
     $f^{abc} = -2i\,\mathrm{tr}([T^a, T^b] T^c)$ (`su3StructConst`), proving tracelessness,
     Killing trace normalization $\mathrm{tr}(T^a T^b) = \frac{1}{2}\delta^{ab}$, explicit non-zero
     non-Abelian constants ($f^{123} = 1$, $f^{147} = 1/2$, $f^{458} = \sqrt{3}/2$), the
     $\mathfrak{su}(3)_c$ Fierz completeness identity
     $\sum_{e=0}^7 \mathrm{tr}(X T^e)\,\mathrm{tr}(Y T^e) = \frac{1}{2}\mathrm{tr}(X Y) - \frac{1}{6}\mathrm{tr}(X)\mathrm{tr}(Y)$,
     and the full 8-generator contracted Jacobi identity
     $\sum_{e=0}^7 (f^{abe} f^{cde} + f^{bce} f^{ade} + f^{cae} f^{bde}) = 0$.

2. **§2 — Yang–Mills / Bern–Kosower Kinematic 3-Gluon Tensor, Full $S_3$ Bose Symmetry, and
   Ghost-Free Off-Shell Slavnov–Taylor Ward Identity:**
   - Formalizes both the coordinate-free bilinear-form vertex `ymThreeGluonContracted` on any
     `R`-module `V` and the index-explicit tensor `ymThreeGluonTensor` on `Fin d → R` (specializing
     to $3+1\mathrm{D}$ Minkowski space `minkowskiMetricMat`).
   - Proves kinematic antisymmetry under all transpositions $(1 \leftrightarrow 2)$,
     $(2 \leftrightarrow 3)$, $(1 \leftrightarrow 3)$ and **complete $S_3$ Bose symmetry** of the
     colour-dressed vertex $f^{a_1 a_2 a_3} V^{\mu_1\mu_2\mu_3}(k_1, k_2, k_3)$.
   - Proves the **exact off-shell Slavnov–Taylor / Ward divergence identity** under momentum
     conservation $k_1 + k_2 + k_3 = 0$:
     $$V(\varepsilon_1, \varepsilon_2, k_3;\, k_1, k_2, k_3)
       = \bigl(k_2^2 (\varepsilon_1 \cdot \varepsilon_2) - (k_2 \cdot \varepsilon_1)(k_2 \cdot \varepsilon_2)\bigr)
       - \bigl(k_1^2 (\varepsilon_1 \cdot \varepsilon_2) - (k_1 \cdot \varepsilon_1)(k_1 \cdot \varepsilon_2)\bigr),$$
     manifestly equal to the difference of two transverse inverse gluon propagators (with zero
     longitudinal ghost remainder) and vanishing identically on transverse on-shell states.

3. **§3 — Bern–Kosower Pinch + Spin-Field-Strength Decomposition and 3-Edge Proper-Time
   Pant Kernel:**
   - Proves the exact Bern–Kosower / Strassler algebraic decomposition
     `ymThreeGluonContracted = bkConvectionPinch + bkSpinFieldStrength`, splitting the cubic Yang–Mills
     vertex into the convection pinch term $\frac{1}{2}\sum_{\mathrm{cyc}}(\varepsilon_a \cdot \varepsilon_b)((k_a - k_b)\cdot \varepsilon_c)$
     plus the individually gauge-invariant spin-1 field-strength coupling
     $\frac{1}{2}\sum_{\mathrm{cyc}} \varepsilon_a \cdot F_c \cdot \varepsilon_b$
     ($F_c^{\mu\nu} = \varepsilon_c^\mu k_c^\nu - k_c^\mu \varepsilon_c^\nu$).
   - Defines the proper-time Schwinger kernel `worldlineKernel T s = exp(-T * s)` and the 3-edge
     proper-time ribbon pant kernel $K_{\mathrm{pant}}(T_1, T_2, T_3; s_1, s_2, s_3)$, proving
     monoidal factorization, cyclic $S_3$ invariance, FTC proper-time pinch boundary evaluation,
     and strict damping on $(0, 1)$.

## References
- [bern1992] Z. Bern, D. A. Kosower, *Nucl. Phys. B* 379 (1992) 451.
- [strassler1992] M. J. Strassler, *Nucl. Phys. B* 385 (1992) 145.
- [schubert2001] C. Schubert, *Phys. Rept.* 355 (2001) 73.
-/

namespace QOU.StandardModel.RibbonPantBernKosowerGluonVertex

open scoped BigOperators
open Matrix Filter Topology MeasureTheory intervalIntegral

-- ============================================================================
-- §1. Cyclic Ribbon Pant Colour Trace & su(3)_c Fierz–Jacobi Algebra
-- ============================================================================

section ColourAlgebra

/-- Associative ring commutator $[A, B] = A B - B A$. -/
def commutator {α : Type*} [Ring α] (A B : α) : α :=
  A * B - B * A

theorem commutator_swap {α : Type*} [Ring α] (A B : α) :
    commutator B A = -commutator A B := by
  simp only [commutator, neg_sub]

/-- Associative Jacobi identity $[[A, B], C] + [[B, C], A] + [[C, A], B] = 0$ in any ring. -/
theorem commutator_jacobi {α : Type*} [Ring α] (A B C : α) :
    commutator (commutator A B) C +
    commutator (commutator B C) A +
    commutator (commutator C A) B = 0 := by
  simp only [commutator, sub_mul, mul_sub, mul_assoc]
  abel

/-- Cyclic 3-boundary ribbon pant colour trace functional $\mathrm{tr}([A, B] C)$ on $n \times n$
    matrices over any commutative ring `R`. -/
def traceStructureMap {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (A B C : Matrix n n R) : R :=
  Matrix.trace (commutator A B * C)

/-- Every matrix commutator has vanishing trace. -/
theorem trace_commutator_eq_zero {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (A B : Matrix n n R) :
    Matrix.trace (commutator A B) = 0 := by
  unfold commutator
  rw [Matrix.trace_sub, Matrix.trace_mul_comm A B, sub_self]

/-- Cyclic invariance of the 3-boundary ribbon pant trace functional:
    $\mathrm{tr}([A, B] C) = \mathrm{tr}([B, C] A) = \mathrm{tr}([C, A] B)$. -/
theorem traceStructureMap_cyclic {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (A B C : Matrix n n R) :
    traceStructureMap A B C = traceStructureMap B C A ∧
    traceStructureMap B C A = traceStructureMap C A B := by
  have hcyc : ∀ X Y Z : Matrix n n R, traceStructureMap X Y Z = traceStructureMap Y Z X := by
    intro X Y Z
    unfold traceStructureMap commutator
    rw [sub_mul, sub_mul, Matrix.trace_sub, Matrix.trace_sub]
    have h1 : Matrix.trace (X * Y * Z) = Matrix.trace (Y * Z * X) := by
      rw [mul_assoc, Matrix.trace_mul_comm X (Y * Z)]
    have h2 : Matrix.trace (Y * X * Z) = Matrix.trace (Z * Y * X) := by
      rw [Matrix.trace_mul_comm (Y * X) Z, mul_assoc]
    rw [h1, h2]
  exact ⟨hcyc A B C, hcyc B C A⟩

/-- Complete antisymmetry of `traceStructureMap` under all three transpositions of $S_3$. -/
theorem traceStructureMap_antisymm {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (A B C : Matrix n n R) :
    traceStructureMap B A C = -traceStructureMap A B C ∧
    traceStructureMap A C B = -traceStructureMap A B C ∧
    traceStructureMap C B A = -traceStructureMap A B C := by
  have h12 : ∀ X Y Z : Matrix n n R, traceStructureMap Y X Z = -traceStructureMap X Y Z := by
    intro X Y Z
    unfold traceStructureMap
    rw [commutator_swap, neg_mul, Matrix.trace_neg]
  have h23 : traceStructureMap A C B = -traceStructureMap A B C := by
    calc traceStructureMap A C B
        = traceStructureMap C B A := (traceStructureMap_cyclic A C B).1
      _ = -traceStructureMap B C A := h12 B C A
      _ = -traceStructureMap A B C := by rw [← (traceStructureMap_cyclic A B C).1]
  have h13 : traceStructureMap C B A = -traceStructureMap A B C := by
    calc traceStructureMap C B A
        = -traceStructureMap B C A := h12 B C A
      _ = -traceStructureMap A B C := by rw [← (traceStructureMap_cyclic A B C).1]
  exact ⟨h12 A B C, h23, h13⟩

/-- The 8 Gell-Mann matrices $\lambda_0, \dots, \lambda_7$ ($\lambda_1, \dots, \lambda_8$ in
    physics indexing) spanning traceless Hermitian $3 \times 3$ matrices. -/
noncomputable def gellMannLambda : Fin 8 → Matrix (Fin 3) (Fin 3) ℂ
  | 0 => !![0, 1, 0; 1, 0, 0; 0, 0, 0]
  | 1 => !![0, -Complex.I, 0; Complex.I, 0, 0; 0, 0, 0]
  | 2 => !![1, 0, 0; 0, -1, 0; 0, 0, 0]
  | 3 => !![0, 0, 1; 0, 0, 0; 1, 0, 0]
  | 4 => !![0, 0, -Complex.I; 0, 0, 0; Complex.I, 0, 0]
  | 5 => !![0, 0, 0; 0, 0, 1; 0, 1, 0]
  | 6 => !![0, 0, 0; 0, 0, -Complex.I; 0, Complex.I, 0]
  | 7 => ((1 : ℂ) / ((Real.sqrt 3 : ℝ) : ℂ)) • !![1, 0, 0; 0, 1, 0; 0, 0, -2]

/-- Fundamental $\mathfrak{su}(3)_c$ generators $T^a = \frac{1}{2}\lambda_a$. -/
noncomputable def su3Gen (a : Fin 8) : Matrix (Fin 3) (Fin 3) ℂ :=
  ((1 / 2 : ℂ)) • gellMannLambda a

/-- Real-normalized $\mathfrak{su}(3)_c$ structure constants
    $f^{abc} = -2 i\,\mathrm{tr}([T^a, T^b] T^c)$ satisfying $[T^a, T^b] = i f^{abc} T^c$. -/
noncomputable def su3StructConst (a b c : Fin 8) : ℂ :=
  (-2 * Complex.I) * traceStructureMap (su3Gen a) (su3Gen b) (su3Gen c)

private theorem trace_mul_su3Gen_formulas (X : Matrix (Fin 3) (Fin 3) ℂ) :
    Matrix.trace (X * su3Gen 0) = (1 / 2 : ℂ) * (X 0 1 + X 1 0) ∧
    Matrix.trace (X * su3Gen 1) = (Complex.I / 2) * (X 0 1 - X 1 0) ∧
    Matrix.trace (X * su3Gen 2) = (1 / 2 : ℂ) * (X 0 0 - X 1 1) ∧
    Matrix.trace (X * su3Gen 3) = (1 / 2 : ℂ) * (X 0 2 + X 2 0) ∧
    Matrix.trace (X * su3Gen 4) = (Complex.I / 2) * (X 0 2 - X 2 0) ∧
    Matrix.trace (X * su3Gen 5) = (1 / 2 : ℂ) * (X 1 2 + X 2 1) ∧
    Matrix.trace (X * su3Gen 6) = (Complex.I / 2) * (X 1 2 - X 2 1) ∧
    Matrix.trace (X * su3Gen 7) =
      ((1 : ℂ) / (2 * ((Real.sqrt 3 : ℝ) : ℂ))) * (X 0 0 + X 1 1 - 2 * X 2 2) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
  · simp [su3Gen, gellMannLambda, Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
    ring

/-- Every $\mathfrak{su}(3)_c$ generator $T^a$ is traceless and satisfies Killing trace
    orthonormality $\mathrm{tr}(T^a T^b) = \frac{1}{2}\delta^{ab}$. -/
theorem su3Gen_trace_zero_and_killing_orthonormal :
    (∀ a : Fin 8, Matrix.trace (su3Gen a) = 0) ∧
    (∀ a b : Fin 8, Matrix.trace (su3Gen a * su3Gen b) = if a = b then (1 / 2 : ℂ) else 0) := by
  have hs3_pos : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hs3_ne : ((Real.sqrt 3 : ℝ) : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr (ne_of_gt hs3_pos)
  have hs3_sq : (((Real.sqrt 3 : ℝ) : ℂ)) ^ 2 = 3 := by
    norm_cast
    exact Real.sq_sqrt (by norm_num)
  refine ⟨?_, ?_⟩
  · intro a
    fin_cases a <;>
      (simp [su3Gen, gellMannLambda, Matrix.trace_fin_three]; try ring)
  · intro a b
    rcases trace_mul_su3Gen_formulas (su3Gen a) with ⟨h0, h1, h2, h3, h4, h5, h6, h7⟩
    fin_cases b
    · change Matrix.trace (su3Gen a * su3Gen 0) = if a = 0 then 1 / 2 else 0
      rw [h0]; fin_cases a <;> (simp [su3Gen, gellMannLambda]; try norm_num)
    · change Matrix.trace (su3Gen a * su3Gen 1) = if a = 1 then 1 / 2 else 0
      rw [h1]; fin_cases a <;>
        (simp [su3Gen, gellMannLambda]; try (ring_nf; rw [Complex.I_sq]; norm_num))
    · change Matrix.trace (su3Gen a * su3Gen 2) = if a = 2 then 1 / 2 else 0
      rw [h2]; fin_cases a <;> (simp [su3Gen, gellMannLambda]; try norm_num)
    · change Matrix.trace (su3Gen a * su3Gen 3) = if a = 3 then 1 / 2 else 0
      rw [h3]; fin_cases a <;> (simp [su3Gen, gellMannLambda]; try norm_num)
    · change Matrix.trace (su3Gen a * su3Gen 4) = if a = 4 then 1 / 2 else 0
      rw [h4]; fin_cases a <;>
        (simp [su3Gen, gellMannLambda]; try (ring_nf; rw [Complex.I_sq]; norm_num))
    · change Matrix.trace (su3Gen a * su3Gen 5) = if a = 5 then 1 / 2 else 0
      rw [h5]; fin_cases a <;> (simp [su3Gen, gellMannLambda]; try norm_num)
    · change Matrix.trace (su3Gen a * su3Gen 6) = if a = 6 then 1 / 2 else 0
      rw [h6]; fin_cases a <;>
        (simp [su3Gen, gellMannLambda]; try (ring_nf; rw [Complex.I_sq]; norm_num))
    · change Matrix.trace (su3Gen a * su3Gen 7) = if a = 7 then 1 / 2 else 0
      rw [h7]; fin_cases a <;>
        (simp [su3Gen, gellMannLambda]; try (field_simp [hs3_ne]; rw [hs3_sq]; ring))

/-- Explicit non-zero non-Abelian $\mathfrak{su}(3)_c$ structure constants:
    $f^{123} = 1$, $f^{147} = 1/2$, $f^{458} = \sqrt{3}/2$. -/
theorem su3StructConst_fundamental_examples :
    su3StructConst 0 1 2 = 1 ∧
    su3StructConst 0 3 6 = 1 / 2 ∧
    su3StructConst 3 4 7 = ((Real.sqrt 3 : ℝ) : ℂ) / 2 := by
  have hs3_pos : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hs3_ne : ((Real.sqrt 3 : ℝ) : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr (ne_of_gt hs3_pos)
  have hs3_sq : (((Real.sqrt 3 : ℝ) : ℂ)) ^ 2 = 3 := by
    norm_cast
    exact Real.sq_sqrt (by norm_num)
  refine ⟨?_, ?_, ?_⟩
  · simp [su3StructConst, traceStructureMap, commutator, su3Gen, gellMannLambda,
      Matrix.trace_fin_three]
    ring_nf; rw [Complex.I_sq]; norm_num
  · simp [su3StructConst, traceStructureMap, commutator, su3Gen, gellMannLambda,
      Matrix.trace_fin_three]
    ring_nf; rw [Complex.I_sq]; norm_num
  · simp [su3StructConst, traceStructureMap, commutator, su3Gen, gellMannLambda,
      Matrix.trace_fin_three]
    field_simp [hs3_ne]
    ring_nf; rw [Complex.I_sq, hs3_sq]; ring

/-- **$\mathfrak{su}(3)_c$ Fierz Completeness Identity:**
    For arbitrary $3 \times 3$ complex matrices $X, Y$,
    $$\sum_{e=0}^{7} \mathrm{tr}(X T^e)\,\mathrm{tr}(Y T^e)
      = \frac{1}{2}\,\mathrm{tr}(X Y) - \frac{1}{6}\,\mathrm{tr}(X)\,\mathrm{tr}(Y).$$ -/
theorem su3_fierz_trace_completeness (X Y : Matrix (Fin 3) (Fin 3) ℂ) :
    (∑ e : Fin 8, Matrix.trace (X * su3Gen e) * Matrix.trace (Y * su3Gen e)) =
      (1 / 2 : ℂ) * Matrix.trace (X * Y) - (1 / 6 : ℂ) * Matrix.trace X * Matrix.trace Y := by
  have hs3_pos : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hs3_ne : ((Real.sqrt 3 : ℝ) : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr (ne_of_gt hs3_pos)
  have hs3_sq : (((Real.sqrt 3 : ℝ) : ℂ)) ^ 2 = 3 := by
    norm_cast
    exact Real.sq_sqrt (by norm_num)
  rcases trace_mul_su3Gen_formulas X with ⟨hx0, hx1, hx2, hx3, hx4, hx5, hx6, hx7⟩
  rcases trace_mul_su3Gen_formulas Y with ⟨hy0, hy1, hy2, hy3, hy4, hy5, hy6, hy7⟩
  rw [Fin.sum_univ_eight, hx0, hx1, hx2, hx3, hx4, hx5, hx6, hx7,
    hy0, hy1, hy2, hy3, hy4, hy5, hy6, hy7]
  have h7 :
      ((1 : ℂ) / (2 * ((Real.sqrt 3 : ℝ) : ℂ))) * (X 0 0 + X 1 1 - 2 * X 2 2) *
        (((1 : ℂ) / (2 * ((Real.sqrt 3 : ℝ) : ℂ))) * (Y 0 0 + Y 1 1 - 2 * Y 2 2)) =
      (1 / 12 : ℂ) * (X 0 0 + X 1 1 - 2 * X 2 2) * (Y 0 0 + Y 1 1 - 2 * Y 2 2) := by
    field_simp [hs3_ne]
    rw [hs3_sq]
    ring
  rw [h7]
  simp only [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  have hi2 : ∀ u v : ℂ, (Complex.I / 2 * u) * (Complex.I / 2 * v) = -(1 / 4 : ℂ) * u * v := by
    intro u v
    calc
      (Complex.I / 2 * u) * (Complex.I / 2 * v)
          = (Complex.I ^ 2 / 4) * u * v := by ring
      _ = -(1 / 4 : ℂ) * u * v := by rw [Complex.I_sq]; ring
  rw [hi2, hi2, hi2]
  ring

/-- Cyclic invariance and complete antisymmetry of `su3StructConst`. -/
theorem su3StructConst_cyclic_and_antisymm (a b c : Fin 8) :
    su3StructConst a b c = su3StructConst b c a ∧
    su3StructConst b c a = su3StructConst c a b ∧
    su3StructConst b a c = -su3StructConst a b c ∧
    su3StructConst a c b = -su3StructConst a b c ∧
    su3StructConst c b a = -su3StructConst a b c := by
  unfold su3StructConst
  rcases traceStructureMap_cyclic (su3Gen a) (su3Gen b) (su3Gen c) with ⟨hc1, hc2⟩
  rcases traceStructureMap_antisymm (su3Gen a) (su3Gen b) (su3Gen c) with ⟨ha1, ha2, ha3⟩
  refine ⟨by rw [hc1], by rw [hc2], by rw [ha1, mul_neg], by rw [ha2, mul_neg],
    by rw [ha3, mul_neg]⟩

/-- **Contracted $\mathfrak{su}(3)_c$ Jacobi Identity (`qou-t3zb`, §1):**
    $$\sum_{e=0}^{7} \bigl(f^{abe} f^{cde} + f^{bce} f^{ade} + f^{cae} f^{bde}\bigr) = 0.$$ -/
theorem su3StructConst_jacobi (a b c d : Fin 8) :
    (∑ e : Fin 8,
      (su3StructConst a b e * su3StructConst c d e +
       su3StructConst b c e * su3StructConst a d e +
       su3StructConst c a e * su3StructConst b d e)) = 0 := by
  have hpair : ∀ x y z w : Fin 8,
      (∑ e : Fin 8, su3StructConst x y e * su3StructConst z w e) =
        (-2 : ℂ) * Matrix.trace (commutator (commutator (su3Gen x) (su3Gen y)) (su3Gen z) *
          su3Gen w) := by
    intro x y z w
    have hpull :
        (∑ e : Fin 8, su3StructConst x y e * su3StructConst z w e) =
          (-4 : ℂ) * (∑ e : Fin 8,
            Matrix.trace (commutator (su3Gen x) (su3Gen y) * su3Gen e) *
              Matrix.trace (commutator (su3Gen z) (su3Gen w) * su3Gen e)) := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl ?_
      intro e _
      unfold su3StructConst traceStructureMap
      calc
        (-2 * Complex.I * Matrix.trace (commutator (su3Gen x) (su3Gen y) * su3Gen e)) *
            (-2 * Complex.I * Matrix.trace (commutator (su3Gen z) (su3Gen w) * su3Gen e))
            = (4 * Complex.I ^ 2) *
                (Matrix.trace (commutator (su3Gen x) (su3Gen y) * su3Gen e) *
                  Matrix.trace (commutator (su3Gen z) (su3Gen w) * su3Gen e)) := by ring
        _ = (-4 : ℂ) *
              (Matrix.trace (commutator (su3Gen x) (su3Gen y) * su3Gen e) *
                Matrix.trace (commutator (su3Gen z) (su3Gen w) * su3Gen e)) := by
            rw [Complex.I_sq]; ring
    rw [hpull, su3_fierz_trace_completeness, trace_commutator_eq_zero,
      trace_commutator_eq_zero]
    have htr :
        Matrix.trace (commutator (su3Gen x) (su3Gen y) * commutator (su3Gen z) (su3Gen w)) =
          Matrix.trace (commutator (commutator (su3Gen x) (su3Gen y)) (su3Gen z) * su3Gen w) := by
      rw [Matrix.trace_mul_comm]
      exact (traceStructureMap_cyclic (commutator (su3Gen x) (su3Gen y)) (su3Gen z) (su3Gen w)).1.symm
    rw [htr]
    ring
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib,
    hpair a b c d, hpair b c a d, hpair c a b d]
  have hsum :
      (-2 : ℂ) * Matrix.trace (commutator (commutator (su3Gen a) (su3Gen b)) (su3Gen c) * su3Gen d) +
      (-2 : ℂ) * Matrix.trace (commutator (commutator (su3Gen b) (su3Gen c)) (su3Gen a) * su3Gen d) +
      (-2 : ℂ) * Matrix.trace (commutator (commutator (su3Gen c) (su3Gen a)) (su3Gen b) * su3Gen d) =
        (-2 : ℂ) * Matrix.trace
          ((commutator (commutator (su3Gen a) (su3Gen b)) (su3Gen c) +
            commutator (commutator (su3Gen b) (su3Gen c)) (su3Gen a) +
            commutator (commutator (su3Gen c) (su3Gen a)) (su3Gen b)) * su3Gen d) := by
    rw [add_mul, add_mul, Matrix.trace_add, Matrix.trace_add]
    ring
  rw [hsum, commutator_jacobi, zero_mul, Matrix.trace_zero, mul_zero]

end ColourAlgebra

-- ============================================================================
-- §2. Kinematic 3-Gluon Vertex, S_3 Bose Symmetry, & Off-Shell Ward Identity
-- ============================================================================

section KinematicAndWard

variable {R : Type*} [CommRing R]

/-- Coordinate-free Yang–Mills 3-gluon kinematic vertex contracted with polarizations
    $\varepsilon_1, \varepsilon_2, \varepsilon_3 \in V$ and incoming momenta $k_1, k_2, k_3 \in V$
    via a bilinear metric $B : V \to_R V \to_R R$. -/
def ymThreeGluonContracted {V : Type*} [AddCommGroup V] [Module R V]
    (B : V →ₗ[R] V →ₗ[R] R) (ε1 ε2 ε3 k1 k2 k3 : V) : R :=
  B ε1 ε2 * B (k1 - k2) ε3 +
  B ε2 ε3 * B (k2 - k3) ε1 +
  B ε3 ε1 * B (k3 - k1) ε2

/-- Component-index Yang–Mills 3-gluon kinematic tensor
    $V^{\mu_1\mu_2\mu_3}(k_1, k_2, k_3) = \eta^{\mu_1\mu_2}(k_1 - k_2)^{\mu_3} + \eta^{\mu_2\mu_3}(k_2 - k_3)^{\mu_1} + \eta^{\mu_3\mu_1}(k_3 - k_1)^{\mu_2}$
    on $d$-dimensional momentum space `Fin d → R`. -/
def ymThreeGluonTensor {d : ℕ} (η : Matrix (Fin d) (Fin d) R)
    (k1 k2 k3 : Fin d → R) (μ1 μ2 μ3 : Fin d) : R :=
  η μ1 μ2 * (k1 μ3 - k2 μ3) +
  η μ2 μ3 * (k2 μ1 - k3 μ1) +
  η μ3 μ1 * (k3 μ2 - k1 μ2)

/-- Standard $3+1\mathrm{D}$ Minkowski metric $\eta = \mathrm{diag}(1, -1, -1, -1)$. -/
def minkowskiMetricMat (R : Type*) [CommRing R] : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0;
     0, -1, 0, 0;
     0, 0, -1, 0;
     0, 0, 0, -1]

theorem minkowskiMetricMat_symm (μ ν : Fin 4) :
    minkowskiMetricMat R μ ν = minkowskiMetricMat R ν μ := by
  fin_cases μ <;> fin_cases ν <;> rfl

/-- Kinematic antisymmetry under all transpositions and invariance under 3-cycles when $\eta$ is symmetric. -/
theorem ymThreeGluonTensor_symmetries {d : ℕ} {η : Matrix (Fin d) (Fin d) R}
    (hη : ∀ μ ν : Fin d, η μ ν = η ν μ) (k1 k2 k3 : Fin d → R) (μ1 μ2 μ3 : Fin d) :
    ymThreeGluonTensor η k2 k1 k3 μ2 μ1 μ3 = -ymThreeGluonTensor η k1 k2 k3 μ1 μ2 μ3 ∧
    ymThreeGluonTensor η k1 k3 k2 μ1 μ3 μ2 = -ymThreeGluonTensor η k1 k2 k3 μ1 μ2 μ3 ∧
    ymThreeGluonTensor η k3 k2 k1 μ3 μ2 μ1 = -ymThreeGluonTensor η k1 k2 k3 μ1 μ2 μ3 ∧
    ymThreeGluonTensor η k2 k3 k1 μ2 μ3 μ1 = ymThreeGluonTensor η k1 k2 k3 μ1 μ2 μ3 := by
  unfold ymThreeGluonTensor
  rw [hη μ2 μ1, hη μ3 μ2, hη μ1 μ3]
  refine ⟨by ring, by ring, by ring, by ring⟩

/-- Colour-dressed non-Abelian 3-gluon vertex $f^{a_1 a_2 a_3} V^{\mu_1\mu_2\mu_3}(k_1, k_2, k_3)$. -/
def fullThreeGluonVertex {α : Type*} {d : ℕ}
    (f : α → α → α → R) (η : Matrix (Fin d) (Fin d) R)
    (a1 a2 a3 : α) (k1 k2 k3 : Fin d → R) (μ1 μ2 μ3 : Fin d) : R :=
  f a1 a2 a3 * ymThreeGluonTensor η k1 k2 k3 μ1 μ2 μ3

/-- **Complete $S_3$ Bose Symmetry of the Non-Abelian 3-Gluon Vertex (`qou-t3zb`, §2):**
    Because both the ribbon-pant colour factor $f^{a_1 a_2 a_3}$ and the kinematic vertex
    $V^{\mu_1\mu_2\mu_3}(k_1, k_2, k_3)$ flip sign under every odd permutation, their product is
    invariant under all transpositions $(1 \leftrightarrow 2)$, $(2 \leftrightarrow 3)$,
    $(1 \leftrightarrow 3)$ and cyclic permutations. -/
theorem fullThreeGluonVertex_bose_symmetry {α : Type*} {d : ℕ}
    {f : α → α → α → R} {η : Matrix (Fin d) (Fin d) R}
    (hf12 : ∀ a b c, f b a c = -f a b c)
    (hf23 : ∀ a b c, f a c b = -f a b c)
    (hf13 : ∀ a b c, f c b a = -f a b c)
    (hfcyc : ∀ a b c, f b c a = f a b c)
    (hη : ∀ μ ν : Fin d, η μ ν = η ν μ)
    (a1 a2 a3 : α) (k1 k2 k3 : Fin d → R) (μ1 μ2 μ3 : Fin d) :
    fullThreeGluonVertex f η a2 a1 a3 k2 k1 k3 μ2 μ1 μ3 =
      fullThreeGluonVertex f η a1 a2 a3 k1 k2 k3 μ1 μ2 μ3 ∧
    fullThreeGluonVertex f η a1 a3 a2 k1 k3 k2 μ1 μ3 μ2 =
      fullThreeGluonVertex f η a1 a2 a3 k1 k2 k3 μ1 μ2 μ3 ∧
    fullThreeGluonVertex f η a3 a2 a1 k3 k2 k1 μ3 μ2 μ1 =
      fullThreeGluonVertex f η a1 a2 a3 k1 k2 k3 μ1 μ2 μ3 ∧
    fullThreeGluonVertex f η a2 a3 a1 k2 k3 k1 μ2 μ3 μ1 =
      fullThreeGluonVertex f η a1 a2 a3 k1 k2 k3 μ1 μ2 μ3 := by
  rcases ymThreeGluonTensor_symmetries hη k1 k2 k3 μ1 μ2 μ3 with ⟨hv12, hv23, hv13, hvcyc⟩
  unfold fullThreeGluonVertex
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [hf12, hv12, neg_mul_neg]
  · rw [hf23, hv23, neg_mul_neg]
  · rw [hf13, hv13, neg_mul_neg]
  · rw [hfcyc, hvcyc]

/-- Transverse inverse gluon propagator bilinear form
    $\Pi_{\mathrm{inv}}(k; \varepsilon_1, \varepsilon_2) = k^2 (\varepsilon_1 \cdot \varepsilon_2) - (k \cdot \varepsilon_1)(k \cdot \varepsilon_2)$. -/
def invTransverseGluonProp {V : Type*} [AddCommGroup V] [Module R V]
    (B : V →ₗ[R] V →ₗ[R] R) (k ε1 ε2 : V) : R :=
  B k k * B ε1 ε2 - B k ε1 * B k ε2

/-- **Off-Shell Slavnov–Taylor / Ward Divergence Identity (`qou-t3zb`, §2):**
    For any symmetric bilinear metric $B$ and momenta $k_1 + k_2 + k_3 = 0$, contracting leg 3 of
    the 3-gluon vertex with its momentum $k_3$ yields the exact difference of transverse inverse
    gluon propagators on legs 2 and 1, with **zero longitudinal Faddeev–Popov ghost remainder**:
    $$V(\varepsilon_1, \varepsilon_2, k_3;\, k_1, k_2, k_3)
      = \Pi_{\mathrm{inv}}(k_2; \varepsilon_1, \varepsilon_2)
      - \Pi_{\mathrm{inv}}(k_1; \varepsilon_1, \varepsilon_2).$$ -/
theorem ymThreeGluon_ward_identity {V : Type*} [AddCommGroup V] [Module R V]
    (B : V →ₗ[R] V →ₗ[R] R) (hB : ∀ u v : V, B u v = B v u)
    {k1 k2 k3 : V} (hk : k1 + k2 + k3 = 0) (ε1 ε2 : V) :
    ymThreeGluonContracted B ε1 ε2 k3 k1 k2 k3 =
      invTransverseGluonProp B k2 ε1 ε2 - invTransverseGluonProp B k1 ε1 ε2 := by
  have hk3 : k3 = -(k1 + k2) := eq_neg_of_add_eq_zero_right hk
  unfold ymThreeGluonContracted invTransverseGluonProp
  rw [hk3]
  simp only [map_sub, map_add, map_neg, LinearMap.sub_apply, LinearMap.add_apply,
    LinearMap.neg_apply]
  rw [hB k2 k1, hB ε2 k1, hB ε2 k2, hB ε1 ε2]
  ring

/-- **On-Shell Ghost-Free Ward Vanishing Corollary:**
    When legs 1 and 2 are massless transverse gluons ($k_1^2 = k_2^2 = 0$ and
    $k_1 \cdot \varepsilon_1 = k_2 \cdot \varepsilon_2 = 0$) and $k_1 + k_2 + k_3 = 0$, a pure
    gauge polarization $\varepsilon_3 = k_3$ decouples identically (`= 0`) without ghosts. -/
theorem ymThreeGluon_onshell_ward_zero {V : Type*} [AddCommGroup V] [Module R V]
    (B : V →ₗ[R] V →ₗ[R] R) (hB : ∀ u v : V, B u v = B v u)
    {k1 k2 k3 ε1 ε2 : V} (hk : k1 + k2 + k3 = 0)
    (hm1 : B k1 k1 = 0) (hm2 : B k2 k2 = 0)
    (ht1 : B k1 ε1 = 0) (ht2 : B k2 ε2 = 0) :
    ymThreeGluonContracted B ε1 ε2 k3 k1 k2 k3 = 0 := by
  rw [ymThreeGluon_ward_identity B hB hk ε1 ε2]
  unfold invTransverseGluonProp
  rw [hm1, hm2, ht1, ht2]
  ring

end KinematicAndWard

-- ============================================================================
-- §3. Bern–Kosower Pinch + Spin Decomposition & 3-Edge Proper-Time Pant Kernel
-- ============================================================================

section BernKosowerWorldline

/-- Scalar-convection pinch vertex (`1/2` times the cyclic sea-gull + IBP derivative sum)
    generated when adjacent proper-time insertions coalesce. -/
noncomputable def bkConvectionPinch {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (ε1 ε2 ε3 k1 k2 k3 : V) : ℝ :=
  (1 / 2 : ℝ) * (B ε1 ε2 * B (k1 - k2) ε3 +
                 B ε2 ε3 * B (k2 - k3) ε1 +
                 B ε3 ε1 * B (k3 - k1) ε2)

/-- Abelianized single-leg Lorentz spin field-strength bilinear
    $\varepsilon_a \cdot F_c \cdot \varepsilon_b = (\varepsilon_a \cdot \varepsilon_c)(k_c \cdot \varepsilon_b) - (\varepsilon_a \cdot k_c)(\varepsilon_c \cdot \varepsilon_b)$
    associated with $F_c^{\mu\nu} = \varepsilon_c^\mu k_c^\nu - k_c^\mu \varepsilon_c^\nu$. -/
def bkLegFieldStrength {R V : Type*} [CommRing R] [AddCommGroup V] [Module R V]
    (B : V →ₗ[R] V →ₗ[R] R) (εa εb εc kc : V) : R :=
  B εa εc * B kc εb - B εa kc * B εc εb

/-- Each single-leg spin field-strength insertion vanishes identically under pure-gauge
    substitution $\varepsilon_c = k_c$. -/
theorem bkLegFieldStrength_pure_gauge_zero {R V : Type*} [CommRing R] [AddCommGroup V] [Module R V]
    (B : V →ₗ[R] V →ₗ[R] R) (εa εb kc : V) :
    bkLegFieldStrength B εa εb kc kc = 0 := by
  unfold bkLegFieldStrength
  ring

/-- Cyclic spin-1 magnetic-moment vertex $\frac{1}{2}\sum_{\mathrm{cyc}} \varepsilon_a \cdot F_c \cdot \varepsilon_b$. -/
noncomputable def bkSpinFieldStrength {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (ε1 ε2 ε3 k1 k2 k3 : V) : ℝ :=
  (1 / 2 : ℝ) * (bkLegFieldStrength B ε1 ε2 ε3 k3 +
                 bkLegFieldStrength B ε2 ε3 ε1 k1 +
                 bkLegFieldStrength B ε3 ε1 ε2 k2)

/-- **Bern–Kosower / Strassler Convection + Spin Decomposition (`qou-t3zb`, §3):**
    For any symmetric bilinear metric $B$, the sum of the convection pinch vertex and the
    individually gauge-invariant spin-1 field-strength vertex equals the exact Yang–Mills 3-gluon
    vertex `ymThreeGluonContracted` **off shell** (even prior to imposing $k_1 + k_2 + k_3 = 0$). -/
theorem bernKosower_convection_plus_spin_eq_ymThreeGluon {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (hB : ∀ u v : V, B u v = B v u)
    (ε1 ε2 ε3 k1 k2 k3 : V) :
    bkConvectionPinch B ε1 ε2 ε3 k1 k2 k3 + bkSpinFieldStrength B ε1 ε2 ε3 k1 k2 k3 =
      ymThreeGluonContracted B ε1 ε2 ε3 k1 k2 k3 := by
  unfold bkConvectionPinch bkSpinFieldStrength bkLegFieldStrength ymThreeGluonContracted
  simp only [map_sub, LinearMap.sub_apply]
  rw [hB ε2 ε1, hB ε3 ε2, hB ε1 ε3,
    hB k1 ε3, hB k2 ε3, hB k2 ε1, hB k3 ε1, hB k3 ε2, hB k1 ε2]
  ring

/-- Single-edge proper-time Schwinger heat kernel `K(T, s) = exp(-T * s)`. -/
noncomputable def worldlineKernel (T s : ℝ) : ℝ :=
  Real.exp (-T * s)

/-- 3-edge proper-time Schwinger ribbon pant kernel
    $K_{\mathrm{pant}}(T_1, T_2, T_3; s_1, s_2, s_3) = \exp(-T_1 s_1 - T_2 s_2 - T_3 s_3)$. -/
noncomputable def ribbonPantKernel (T1 T2 T3 s1 s2 s3 : ℝ) : ℝ :=
  worldlineKernel T1 s1 * worldlineKernel T2 s2 * worldlineKernel T3 s3

/-- Monoidal exponent additivity, cyclic $S_3$ symmetry, and strict damping $(0, 1)$ of the
    3-edge proper-time ribbon pant kernel. -/
theorem ribbonPantKernel_properties (T1 T2 T3 s1 s2 s3 : ℝ) :
    ribbonPantKernel T1 T2 T3 s1 s2 s3 = Real.exp (-(T1 * s1 + T2 * s2 + T3 * s3)) ∧
    ribbonPantKernel T2 T3 T1 s2 s3 s1 = ribbonPantKernel T1 T2 T3 s1 s2 s3 ∧
    (0 < T1 → 0 < T2 → 0 < T3 → 0 < s1 → 0 < s2 → 0 < s3 →
      0 < ribbonPantKernel T1 T2 T3 s1 s2 s3 ∧ ribbonPantKernel T1 T2 T3 s1 s2 s3 < 1) := by
  have hexp : ∀ a b c d e f : ℝ,
      ribbonPantKernel a b c d e f = Real.exp (-(a * d + b * e + c * f)) := by
    intro a b c d e f
    unfold ribbonPantKernel worldlineKernel
    rw [← Real.exp_add, ← Real.exp_add]
    congr 1
    ring
  refine ⟨hexp T1 T2 T3 s1 s2 s3, ?_, ?_⟩
  · rw [hexp, hexp]
    congr 1
    ring
  · intro hT1 hT2 hT3 hs1 hs2 hs3
    rw [hexp]
    refine ⟨Real.exp_pos _, Real.exp_lt_one_iff.mpr ?_⟩
    have h1 : 0 < T1 * s1 := mul_pos hT1 hs1
    have h2 : 0 < T2 * s2 := mul_pos hT2 hs2
    have h3 : 0 < T3 * s3 := mul_pos hT3 hs3
    linarith

/-- **Proper-Time Pinch Integration-by-Parts Identity (`qou-t3zb`, §3):**
    Integrating the proper-time derivative $(-s)\exp(-T s)$ on $[T_{\min}, T_{\max}]$ produces the
    exact boundary pinch difference $\exp(-T_{\max} s) - \exp(-T_{\min} s)$. -/
theorem worldline_pinch_ibp_interval_integral (s Tmin Tmax : ℝ) :
    (∫ T in Tmin..Tmax, (-s) * worldlineKernel T s) =
      worldlineKernel Tmax s - worldlineKernel Tmin s := by
  unfold worldlineKernel
  have hderiv : ∀ T ∈ Set.uIcc Tmin Tmax,
      HasDerivAt (fun t : ℝ => Real.exp (-t * s)) ((-s) * Real.exp (-T * s)) T := by
    intro T _
    have hlin : HasDerivAt (fun t : ℝ => -t * s) (-s) T := by
      simpa using (hasDerivAt_id T).neg.mul_const s
    simpa [mul_comm] using hlin.exp
  have hint : IntervalIntegrable (fun T : ℝ => (-s) * Real.exp (-T * s)) volume Tmin Tmax := by
    have hcont : Continuous (fun T : ℝ => (-s) * Real.exp (-T * s)) :=
      continuous_const.mul (Real.continuous_exp.comp (continuous_id.neg.mul continuous_const))
    exact hcont.intervalIntegrable Tmin Tmax
  exact integral_eq_sub_of_hasDerivAt hderiv hint

/-- Archimedean `(R := ℝ)` specialisation of `ymThreeGluon_ward_identity` (§7c `_real` pair). -/
theorem ymThreeGluon_ward_identity_real {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (hB : ∀ u v : V, B u v = B v u)
    {k1 k2 k3 : V} (hk : k1 + k2 + k3 = 0) (ε1 ε2 : V) :
    ymThreeGluonContracted B ε1 ε2 k3 k1 k2 k3 =
      invTransverseGluonProp B k2 ε1 ε2 - invTransverseGluonProp B k1 ε1 ε2 :=
  ymThreeGluon_ward_identity B hB hk ε1 ε2

end BernKosowerWorldline

end QOU.StandardModel.RibbonPantBernKosowerGluonVertex
