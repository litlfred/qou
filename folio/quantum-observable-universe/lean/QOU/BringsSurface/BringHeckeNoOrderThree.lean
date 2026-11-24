/-
Route 2 of the O'Hara selection question (beans `qou-99qc`, `qou-pzsi`, `qou-brfy`):
target (L3) of `computations/probes/bring_route2/preregistration.md` §3, proved.

The pre-registration routes braids to Bring's surface through `Γ₀(2)` and a commensurability
with the Hecke group `H₄ = ⟨S, U⟩` (`S : z ↦ -1/z`, `U : z ↦ z + √2`) rather than through a
homomorphism `B₃ → H₄`, on the grounds that

  *`H₄` has no element of order 3, so every homomorphism from `B₃ = ⟨x, y | x² = y³⟩` to
  `H₄` has abelian image.*

That claim was recorded as "to be proved, not assumed", with a warning that Mathlib's free
products are thin. This file proves it without free products, by working with the matrices.

* Every element of `H₄` (as a matrix in `SL(2, ℝ)`) has one of two **Hecke shapes**,
  `[[a, b√2], [c√2, d]]` or `[[a√2, b], [c, d√2]]` with `a, b, c, d ∈ ℤ`
  (`heckeShape_S`, `heckeShape_U`, `heckeShape_U_inv`, `HeckeShape.mul`,
  `heckeShape_of_mem_closure`).
* No Hecke-shaped matrix of determinant 1 has trace `±1` (`trace_sq_ne_one`): in the first
  shape `ad − 2bc = 1` forces `a, d` odd, so `a + d` is even; in the second the trace is
  `(a + d)√2`, whose square `2(a + d)²` is even.
* Hence (`eq_one_or_neg_one_of_pow_three`) a Hecke-shaped `M` with `M³ = ±1` is `±1`: `H₄`
  has no element of order 3 in `PSL(2, ℝ)`.
* If `A² = ±B³` with `B` Hecke-shaped of determinant 1, then `AB = BA`
  (`commute_of_sq_eq_pm_cube`). Either `A²` is a scalar, and then `B³` is a scalar, so `B` is
  a scalar (`scalar_of_cube_scalar`); or `A²` is not a scalar, and `A`, `B` both commute with it, and the commutant of a
  non-scalar `2 × 2` matrix is commutative (`commute_of_commute_nonscalar`).

Only the image of `y` needs to lie in `H₄`: the argument sees `x` only through `x²`.

So the images `f(x)`, `f(y)` of the two generators of `B₃` commute, and the image of any
homomorphism `B₃ → H₄` is abelian. The lift to `SL(2)` carries the signs: a relation `x² = y³`
in `PSL(2)` is `A² = ±B³` in `SL(2)`.

Base ring: `ℝ`, because the shapes carry `√2` and the parity argument needs integer entries
(§7c: archimedean square root). The commutant lemma is over any field.
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination
import QOU.BringsSurface.BringHeckeCommensurability
import QOU.BringsSurface.BringTriangleTraces

namespace QOU.BringHecke

open Matrix

/-! ### Commutant of a non-scalar `2 × 2` matrix -/

section Commutant

variable {K : Type*} [Field K]

theorem eq_smul_one_of_entries (G : Matrix (Fin 2) (Fin 2) K) (h01 : G 0 1 = 0) (h10 : G 1 0 = 0)
    (hd : G 0 0 = G 1 1) : G = G 0 0 • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [h01, h10, hd]

/-- Two matrices that commute with the same non-scalar `2 × 2` matrix commute with each other. -/
theorem commute_of_commute_nonscalar (G X Y : Matrix (Fin 2) (Fin 2) K)
    (hG : ∀ c : K, G ≠ c • 1) (hX : X * G = G * X) (hY : Y * G = G * Y) : X * Y = Y * X := by
  have e := fun (M N : Matrix (Fin 2) (Fin 2) K) (h : M * N = N * M) (i j : Fin 2) =>
    congrFun (congrFun h i) j
  have x1 := e _ _ hX 0 0; have x2 := e _ _ hX 0 1; have x3 := e _ _ hX 1 0
  have y1 := e _ _ hY 0 0; have y2 := e _ _ hY 0 1; have y3 := e _ _ hY 1 0
  simp only [Matrix.mul_apply, Fin.sum_univ_two] at x1 x2 x3 y1 y2 y3
  set p := G 0 0; set q := G 0 1; set r := G 1 0; set s := G 1 1
  -- x1: X01 r = q X10 ;  x2: q (X00 - X11) = X01 (p - s) ;  x3: r (X00 - X11) = X10 (p - s)
  have E1x : X 0 1 * r - q * X 1 0 = 0 := by linear_combination x1
  have E1y : Y 0 1 * r - q * Y 1 0 = 0 := by linear_combination y1
  have E2x : q * (X 0 0 - X 1 1) - X 0 1 * (p - s) = 0 := by linear_combination x2
  have E2y : q * (Y 0 0 - Y 1 1) - Y 0 1 * (p - s) = 0 := by linear_combination y2
  have E3x : X 1 0 * (p - s) - r * (X 0 0 - X 1 1) = 0 := by linear_combination x3
  have E3y : Y 1 0 * (p - s) - r * (Y 0 0 - Y 1 1) = 0 := by linear_combination y3
  have key : X 0 1 * Y 1 0 = Y 0 1 * X 1 0 ∧
      Y 0 1 * (X 0 0 - X 1 1) = X 0 1 * (Y 0 0 - Y 1 1) ∧
      X 1 0 * (Y 0 0 - Y 1 1) = Y 1 0 * (X 0 0 - X 1 1) := by
    by_cases hq : q = 0
    · by_cases hr : r = 0
      · have hw : p - s ≠ 0 := by
          intro hw
          exact hG p (eq_smul_one_of_entries G hq hr (sub_eq_zero.mp hw))
        have a1 : X 0 1 = 0 := by
          have : X 0 1 * (p - s) = 0 := by linear_combination -E2x + (X 0 0 - X 1 1) * hq
          simpa [hw] using this
        have a2 : Y 0 1 = 0 := by
          have : Y 0 1 * (p - s) = 0 := by linear_combination -E2y + (Y 0 0 - Y 1 1) * hq
          simpa [hw] using this
        have a3 : X 1 0 = 0 := by
          have : X 1 0 * (p - s) = 0 := by linear_combination E3x + (X 0 0 - X 1 1) * hr
          simpa [hw] using this
        have a4 : Y 1 0 = 0 := by
          have : Y 1 0 * (p - s) = 0 := by linear_combination E3y + (Y 0 0 - Y 1 1) * hr
          simpa [hw] using this
        simp [a1, a2, a3, a4]
      · have a1 : X 0 1 = 0 := by
          have : X 0 1 * r = 0 := by linear_combination E1x + X 1 0 * hq
          simpa [hr] using this
        have a2 : Y 0 1 = 0 := by
          have : Y 0 1 * r = 0 := by linear_combination E1y + Y 1 0 * hq
          simpa [hr] using this
        refine ⟨by simp [a1, a2], by simp [a1, a2], mul_left_cancel₀ hr ?_⟩
        linear_combination -(X 1 0) * E3y + Y 1 0 * E3x
    · have h1 : X 0 1 * Y 1 0 = Y 0 1 * X 1 0 :=
        mul_left_cancel₀ hq (by linear_combination -(X 0 1) * E1y + Y 0 1 * E1x)
      have h2 : Y 0 1 * (X 0 0 - X 1 1) = X 0 1 * (Y 0 0 - Y 1 1) :=
        mul_left_cancel₀ hq (by linear_combination Y 0 1 * E2x - X 0 1 * E2y)
      refine ⟨h1, h2, mul_left_cancel₀ hq ?_⟩
      linear_combination -(Y 0 0 - Y 1 1) * E1x + (X 0 0 - X 1 1) * E1y - r * h2
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
  · linear_combination key.1
  · linear_combination key.2.1
  · linear_combination key.2.2
  · linear_combination -key.1

end Commutant

/-! ### Matrices with `M³` scalar and trace not `±1` are scalar -/

section Cube

variable {K : Type*} [Field K]

/-- `M³ = (t² − 1) M − t` for `det M = 1`, `t = tr M`. -/
theorem cube_eq (M : Matrix (Fin 2) (Fin 2) K) (hdet : M.det = 1) :
    M ^ 3 = (M.trace ^ 2 - 1) • M - M.trace • (1 : Matrix (Fin 2) (Fin 2) K) := by
  have h2 := QOU.BringTriangle.sq_eq_trace_smul_sub M
  rw [hdet, one_smul] at h2
  rw [pow_three, h2, mul_sub, mul_smul_comm, h2, mul_one, smul_sub, smul_smul, ← pow_two,
    sub_smul, one_smul]
  abel

/-- If `det M = 1`, `(tr M)² ≠ 1` and `M³` is a scalar, then `M` is a scalar. -/
theorem scalar_of_cube_scalar (M : Matrix (Fin 2) (Fin 2) K) (hdet : M.det = 1)
    (ht : M.trace ^ 2 ≠ 1) (c : K) (h : M ^ 3 = c • (1 : Matrix (Fin 2) (Fin 2) K)) :
    ∃ μ : K, M = μ • (1 : Matrix (Fin 2) (Fin 2) K) := by
  have hne : M.trace ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr ht
  refine ⟨(M.trace ^ 2 - 1)⁻¹ * (c + M.trace), ?_⟩
  have key : (M.trace ^ 2 - 1) • M = (c + M.trace) • (1 : Matrix (Fin 2) (Fin 2) K) := by
    have e := cube_eq M hdet
    rw [h] at e
    rw [add_smul, e]
    abel
  rw [MulAction.mul_smul, ← key, smul_smul, inv_mul_cancel₀ hne, one_smul]

theorem det_smul_one (μ : K) : (μ • (1 : Matrix (Fin 2) (Fin 2) K)).det = μ ^ 2 := by
  rw [Matrix.det_smul, Matrix.det_one, mul_one, Fintype.card_fin]

/-- A determinant-one scalar `2 × 2` matrix is `±1`. -/
theorem eq_one_or_neg_one_of_scalar (M : Matrix (Fin 2) (Fin 2) K) (hdet : M.det = 1)
    (μ : K) (hμ : M = μ • (1 : Matrix (Fin 2) (Fin 2) K)) : M = 1 ∨ M = -1 := by
  subst hμ
  rw [det_smul_one, pow_two] at hdet
  rcases mul_self_eq_one_iff.mp hdet with h | h
  · left; rw [h, one_smul]
  · right; rw [h, neg_one_smul]

end Cube

/-! ### Hecke shapes -/

section Shapes

open Real

lemma sqrt2_sq : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)

/-- `[[a, b√2], [c√2, d]]` with integer `a, b, c, d`. -/
def EvenShape (M : Matrix (Fin 2) (Fin 2) ℝ) : Prop :=
  ∃ a b c d : ℤ, M = !![(a : ℝ), b * Real.sqrt 2; c * Real.sqrt 2, d]

/-- `[[a√2, b], [c, d√2]]` with integer `a, b, c, d`. -/
def OddShape (M : Matrix (Fin 2) (Fin 2) ℝ) : Prop :=
  ∃ a b c d : ℤ, M = !![a * Real.sqrt 2, (b : ℝ); c, d * Real.sqrt 2]

/-- The two shapes of an element of `H₄`. -/
def HeckeShape (M : Matrix (Fin 2) (Fin 2) ℝ) : Prop := EvenShape M ∨ OddShape M

theorem EvenShape.mul {M N : Matrix (Fin 2) (Fin 2) ℝ} (hM : EvenShape M) (hN : EvenShape N) :
    EvenShape (M * N) := by
  obtain ⟨a, b, c, d, rfl⟩ := hM
  obtain ⟨a', b', c', d', rfl⟩ := hN
  refine ⟨a * a' + 2 * b * c', a * b' + b * d', c * a' + d * c', 2 * c * b' + d * d', ?_⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two] <;>
    ring_nf <;> simp only [sqrt2_sq] <;> ring

theorem EvenShape.mul_odd {M N : Matrix (Fin 2) (Fin 2) ℝ} (hM : EvenShape M)
    (hN : OddShape N) : OddShape (M * N) := by
  obtain ⟨a, b, c, d, rfl⟩ := hM
  obtain ⟨a', b', c', d', rfl⟩ := hN
  refine ⟨a * a' + b * c', a * b' + 2 * b * d', 2 * c * a' + d * c', c * b' + d * d', ?_⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two] <;>
    ring_nf <;> simp only [sqrt2_sq] <;> ring

theorem OddShape.mul_even {M N : Matrix (Fin 2) (Fin 2) ℝ} (hM : OddShape M)
    (hN : EvenShape N) : OddShape (M * N) := by
  obtain ⟨a, b, c, d, rfl⟩ := hM
  obtain ⟨a', b', c', d', rfl⟩ := hN
  refine ⟨a * a' + b * c', 2 * a * b' + b * d', c * a' + 2 * d * c', c * b' + d * d', ?_⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two] <;>
    ring_nf <;> simp only [sqrt2_sq] <;> ring

theorem OddShape.mul {M N : Matrix (Fin 2) (Fin 2) ℝ} (hM : OddShape M) (hN : OddShape N) :
    EvenShape (M * N) := by
  obtain ⟨a, b, c, d, rfl⟩ := hM
  obtain ⟨a', b', c', d', rfl⟩ := hN
  refine ⟨2 * a * a' + b * c', a * b' + b * d', c * a' + d * c', c * b' + 2 * d * d', ?_⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two] <;>
    ring_nf <;> simp only [sqrt2_sq] <;> ring

theorem HeckeShape.mul {M N : Matrix (Fin 2) (Fin 2) ℝ} (hM : HeckeShape M)
    (hN : HeckeShape N) : HeckeShape (M * N) := by
  rcases hM with hM | hM <;> rcases hN with hN | hN
  · exact Or.inl (hM.mul hN)
  · exact Or.inr (hM.mul_odd hN)
  · exact Or.inr (hM.mul_even hN)
  · exact Or.inl (hM.mul hN)

theorem heckeShape_one : HeckeShape 1 :=
  Or.inl ⟨1, 0, 0, 1, by ext i j; fin_cases i <;> fin_cases j <;> simp⟩

theorem heckeShape_S : HeckeShape sHecke :=
  Or.inr ⟨0, -1, 1, 0, by ext i j; fin_cases i <;> fin_cases j <;> simp [sHecke]⟩

theorem heckeShape_U : HeckeShape uHecke :=
  Or.inl ⟨1, 1, 0, 1, by ext i j; fin_cases i <;> fin_cases j <;> simp [uHecke]⟩

/-- `U⁻¹ : z ↦ z - √2`. -/
noncomputable def uHeckeInv : Matrix (Fin 2) (Fin 2) ℝ := !![1, -Real.sqrt 2; 0, 1]

theorem uHecke_mul_uHeckeInv : uHecke * uHeckeInv = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [uHecke, uHeckeInv, Matrix.mul_apply]

theorem heckeShape_U_inv : HeckeShape uHeckeInv :=
  Or.inl ⟨1, -1, 0, 1, by ext i j; fin_cases i <;> fin_cases j <;> simp [uHeckeInv]⟩

/-- Every element of the monoid generated by `S`, `U`, `U⁻¹` (that is, every element of `H₄`
as a matrix; `S⁻¹ = S³`) has a Hecke shape and determinant `1`. -/
theorem heckeShape_of_mem_closure {M : Matrix (Fin 2) (Fin 2) ℝ}
    (hM : M ∈ Submonoid.closure ({sHecke, uHecke, uHeckeInv} : Set (Matrix (Fin 2) (Fin 2) ℝ))) :
    HeckeShape M ∧ M.det = 1 := by
  induction hM using Submonoid.closure_induction with
  | mem x hx =>
    rcases hx with rfl | rfl | rfl
    · exact ⟨heckeShape_S, by simp [sHecke, Matrix.det_fin_two]⟩
    · exact ⟨heckeShape_U, by simp [uHecke, Matrix.det_fin_two]⟩
    · exact ⟨heckeShape_U_inv, by simp [uHeckeInv, Matrix.det_fin_two]⟩
  | one => exact ⟨heckeShape_one, Matrix.det_one⟩
  | mul x y _ _ hx hy => exact ⟨hx.1.mul hy.1, by rw [Matrix.det_mul, hx.2, hy.2, one_mul]⟩

lemma zmod2_even_trace (x y z w : ZMod 2) (h1 : x * w - 2 * y * z = 1) :
    (x + w) ^ 2 ≠ 1 := by
  revert x y z w; decide

lemma zmod2_two_mul (k : ZMod 2) : 2 * k ≠ 1 := by
  revert k; decide

/-- No Hecke-shaped matrix of determinant `1` has trace `±1`. -/
theorem trace_sq_ne_one {M : Matrix (Fin 2) (Fin 2) ℝ} (hM : HeckeShape M) (hdet : M.det = 1) :
    M.trace ^ 2 ≠ 1 := by
  rcases hM with ⟨a, b, c, d, rfl⟩ | ⟨a, b, c, d, rfl⟩
  · rw [Matrix.det_fin_two_of] at hdet
    rw [Matrix.trace_fin_two_of]
    intro ht
    have hz : ((a * d - 2 * b * c : ℤ) : ℝ) = 1 := by
      push_cast; linear_combination hdet + ((b : ℝ) * c) * sqrt2_sq
    have hz' : a * d - 2 * b * c = 1 := by exact_mod_cast hz
    have ht' : (a + d) ^ 2 = 1 := by exact_mod_cast ht
    have h1 := congrArg (Int.cast : ℤ → ZMod 2) hz'
    have h2 := congrArg (Int.cast : ℤ → ZMod 2) ht'
    push_cast at h1 h2
    exact zmod2_even_trace _ _ _ _ h1 h2
  · rw [Matrix.trace_fin_two_of]
    intro ht
    have hz : ((2 * (a + d) ^ 2 : ℤ) : ℝ) = 1 := by
      push_cast; linear_combination ht - ((a : ℝ) + d) ^ 2 * sqrt2_sq
    have hz' : 2 * (a + d) ^ 2 = 1 := by exact_mod_cast hz
    have h1 := congrArg (Int.cast : ℤ → ZMod 2) hz'
    push_cast at h1
    exact zmod2_two_mul _ h1

/-- `H₄` has no element of order `3` in `PSL(2, ℝ)`: a Hecke-shaped `M` of determinant `1`
with `M³ = ±1` is `±1`. -/
theorem eq_one_or_neg_one_of_pow_three {M : Matrix (Fin 2) (Fin 2) ℝ} (hM : HeckeShape M)
    (hdet : M.det = 1) (h : M ^ 3 = 1 ∨ M ^ 3 = -1) : M = 1 ∨ M = -1 := by
  obtain ⟨μ, hμ⟩ : ∃ μ : ℝ, M = μ • (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
    rcases h with h | h
    · exact scalar_of_cube_scalar M hdet (trace_sq_ne_one hM hdet) 1 (by rw [h, one_smul])
    · exact scalar_of_cube_scalar M hdet (trace_sq_ne_one hM hdet) (-1)
        (by rw [h, neg_one_smul])
  exact eq_one_or_neg_one_of_scalar M hdet μ hμ

/-- **(L3)** If `B` is Hecke-shaped of determinant `1` and `A² = ±B³` (the relation `x² = y³`
of `B₃`, lifted from `PSL(2)` to `SL(2)`), then `A` and `B` commute. Only `B` needs the shape:
the argument uses `A` only through `A²`. -/
theorem commute_of_sq_eq_pm_cube {A B : Matrix (Fin 2) (Fin 2) ℝ}
    (hB : HeckeShape B) (dB : B.det = 1) (h : A ^ 2 = B ^ 3 ∨ A ^ 2 = -B ^ 3) :
    A * B = B * A := by
  obtain ⟨ε, hε, hεε⟩ : ∃ ε : ℝ, A ^ 2 = ε • B ^ 3 ∧ ε * ε = 1 := by
    rcases h with h | h
    · exact ⟨1, by rw [h, one_smul], by norm_num⟩
    · exact ⟨-1, by rw [h, neg_one_smul], by norm_num⟩
  by_cases hs : ∃ μ : ℝ, A ^ 2 = μ • (1 : Matrix (Fin 2) (Fin 2) ℝ)
  · obtain ⟨μ, hμ⟩ := hs
    have hB3 : B ^ 3 = (ε * μ) • (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
      rw [MulAction.mul_smul, ← hμ, hε, smul_smul, hεε, one_smul]
    obtain ⟨ν, rfl⟩ := scalar_of_cube_scalar B dB (trace_sq_ne_one hB dB) _ hB3
    rw [Matrix.mul_smul, Matrix.smul_mul, mul_one, one_mul]
  · push_neg at hs
    refine commute_of_commute_nonscalar (A ^ 2) A B hs ?_ ?_
    · rw [← pow_succ', ← pow_succ]
    · rw [hε, Matrix.mul_smul, Matrix.smul_mul, ← pow_succ', ← pow_succ]

end Shapes

end QOU.BringHecke
