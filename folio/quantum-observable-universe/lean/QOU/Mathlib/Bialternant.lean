import Mathlib.LinearAlgebra.Vandermonde
import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Algebra.BigOperators.Fin

/-!
# QOU.Mathlib.Bialternant — the alternant branching rule

For exponents `α₀ < α₁ < ⋯ < α_N` and variables `x₀, …, x_N` in a commutative ring, the
alternant `a_α(x) = det (x_i ^ α_j)` splits off the variable `x₀`:

    a_α(x) = x₀^{α₀} · ∏_{i ≥ 1} (x_i − x₀) ·
             Σ_{k_j < α_{j+1} − α_j} x₀^{Σ_j (α_{j+1} − 1 − α_j − k_j)} · a_{(α_j + k_j)_j}(x₁, …, x_N).

The new exponents `γ_j = α_j + k_j` range over `α_j ≤ γ_j < α_{j+1}`, so they interlace the old
ones. This is the determinant half of the bialternant formula `a_{λ+δ} = a_δ · s_λ`.

Proof: subtract `x₀^{α_j − α_{j−1}}` times column `j − 1` from column `j`. Row `0` becomes
`(x₀^{α₀}, 0, …, 0)`; each remaining entry is `x_i^{α_j}(x_i^d − x₀^d)`, which carries the factor
`x_i − x₀` times a geometric sum, and the determinant is multilinear in those sums.

## Base ring (§7c)

Generic `[CommRing R]`. Nothing archimedean.
-/

namespace QOU.Mathlib.Bialternant

open Matrix Finset

variable {R : Type*} [CommRing R]

/-- The alternant `det (x_i ^ α_j)`. -/
def alt {N : ℕ} (x : Fin N → R) (α : Fin N → ℕ) : R :=
  (Matrix.of fun i j => x i ^ α j).det

/-- The column-operation matrix: `1` on the diagonal and `−x₀^{α_j − α_{j−1}}` just above it. -/
def colOp {N : ℕ} (y : R) (α : Fin (N + 1) → ℕ) : Matrix (Fin (N + 1)) (Fin (N + 1)) R :=
  fun a b => if a = b then 1 else if a.val + 1 = b.val then -(y ^ (α b - α a)) else 0

theorem det_colOp {N : ℕ} (y : R) (α : Fin (N + 1) → ℕ) : (colOp y α).det = 1 := by
  rw [det_of_upperTriangular]
  · simp [colOp]
  · intro a b hab
    have : b < a := hab
    simp only [colOp]
    rw [if_neg (by intro h; subst h; exact lt_irrefl _ this),
      if_neg (by intro h; have := Fin.lt_def.mp this; omega)]

/-- The matrix after the column operations. -/
def opMat {N : ℕ} (x : Fin (N + 1) → R) (α : Fin (N + 1) → ℕ) :
    Matrix (Fin (N + 1)) (Fin (N + 1)) R :=
  fun i j => Fin.cases (x i ^ α 0)
    (fun j' : Fin N => x i ^ α j'.succ - x 0 ^ (α j'.succ - α j'.castSucc) * x i ^ α j'.castSucc) j

theorem mul_colOp {N : ℕ} (x : Fin (N + 1) → R) (α : Fin (N + 1) → ℕ) :
    (Matrix.of fun i j => x i ^ α j) * colOp (x 0) α = opMat x α := by
  ext i j
  rw [mul_apply]
  refine Fin.cases ?_ (fun j' => ?_) j
  · rw [Fintype.sum_eq_single 0]
    · simp [colOp, opMat]
    · intro a ha
      simp only [colOp]
      rw [if_neg ha, if_neg (by simp), mul_zero]
  · rw [Fintype.sum_eq_add j'.succ j'.castSucc (by
        intro h; have := congrArg Fin.val h; simp at this)]
    · simp only [colOp, opMat, of_apply, Fin.cases_succ]
      rw [if_true, if_neg (by intro h; have := congrArg Fin.val h; simp at this),
        if_pos (by simp)]
      ring
    · intro a ⟨ha1, ha2⟩
      simp only [colOp]
      rw [if_neg ha1, if_neg (by
        intro h; apply ha2; ext; simp only [Fin.val_succ, Fin.coe_castSucc] at h ⊢; omega),
        mul_zero]

/-- Row `0` of the operated matrix is `(x₀^{α₀}, 0, …, 0)`, so the determinant is that entry
times the minor on rows and columns `1, …, N`. -/
theorem det_opMat {N : ℕ} (x : Fin (N + 1) → R) (α : Fin (N + 1) → ℕ) (hα : Monotone α) :
    (opMat x α).det = x 0 ^ α 0 * ((opMat x α).submatrix Fin.succ Fin.succ).det := by
  rw [det_succ_row_zero, Fin.sum_univ_succ, Finset.sum_eq_zero]
  · simp [opMat]
  · intro j _
    have hle : α j.castSucc ≤ α j.succ := hα (Fin.castSucc_le_succ j)
    have h0 : opMat x α 0 j.succ = 0 := by
      simp only [opMat, Fin.cases_succ]
      rw [← pow_add, Nat.sub_add_cancel hle, sub_self]
    rw [h0, mul_zero, zero_mul]

/-- `u^{a+d} − y^d u^a = (u − y) · Σ_{k<d} u^{a+k} y^{d−1−k}`. -/
theorem pow_add_sub_pow_mul (u y : R) (a d : ℕ) :
    u ^ (a + d) - y ^ d * u ^ a
      = (u - y) * ∑ k : Fin d, u ^ (a + k) * y ^ (d - 1 - k) := by
  have h := geom_sum₂_mul u y d
  rw [Fin.sum_univ_eq_sum_range (fun k => u ^ (a + k) * y ^ (d - 1 - k)) d]
  have : ∑ k ∈ Finset.range d, u ^ (a + k) * y ^ (d - 1 - k)
      = u ^ a * ∑ k ∈ Finset.range d, u ^ k * y ^ (d - 1 - k) := by
    rw [Finset.mul_sum]; refine Finset.sum_congr rfl fun k _ => ?_; ring
  rw [this, pow_add]
  linear_combination (-(u ^ a)) * h

/-- Determinant of a matrix whose row `j` is a sum indexed by `Fin (d j)`: multilinearity. -/
theorem det_sum_rows {N : ℕ} (d : Fin N → ℕ) (g : (j : Fin N) → Fin (d j) → Fin N → R) :
    (Matrix.of fun j i => ∑ k, g j k i).det
      = ∑ r : (j : Fin N) → Fin (d j), (Matrix.of fun j i => g j (r j) i).det := by
  have h : (Matrix.of fun j i => ∑ k, g j k i) = fun j => ∑ k, g j k := by
    ext j i; simp [Finset.sum_apply]
  rw [h]
  exact (detRowAlternating (n := Fin N) (R := R)).toMultilinearMap.map_sum g

/-- **The alternant branching rule.** -/
theorem alt_succ {N : ℕ} (x : Fin (N + 1) → R) (α : Fin (N + 1) → ℕ) (hα : Monotone α) :
    alt x α = x 0 ^ α 0 * (∏ i : Fin N, (x i.succ - x 0)) *
      ∑ k : (j : Fin N) → Fin (α j.succ - α j.castSucc),
        x 0 ^ (∑ j, (α j.succ - 1 - (α j.castSucc + k j))) *
          alt (Fin.tail x) (fun j => α j.castSucc + k j) := by
  set d : Fin N → ℕ := fun j => α j.succ - α j.castSucc with hd
  have hle : ∀ j : Fin N, α j.castSucc ≤ α j.succ := fun j => hα (Fin.castSucc_le_succ j)
  unfold alt
  rw [← mul_one (Matrix.of fun i j => x i ^ α j).det, ← det_colOp (x 0) α, ← det_mul,
    mul_colOp, det_opMat x α hα, mul_assoc]
  congr 1
  -- factor `x_i − x₀` out of every row of the minor
  have hsub : (opMat x α).submatrix Fin.succ Fin.succ
      = Matrix.of fun i j => (x i.succ - x 0) *
          ∑ k : Fin (d j), x i.succ ^ (α j.castSucc + k) * x 0 ^ (d j - 1 - k) := by
    ext i j
    simp only [submatrix_apply, opMat, Fin.cases_succ, of_apply]
    rw [← pow_add_sub_pow_mul, hd]
    simp only
    rw [Nat.add_sub_cancel' (hle j)]
  rw [hsub, det_mul_column, ← det_transpose]
  congr 1
  have htr : (Matrix.of fun (i j : Fin N) => ∑ k : Fin (d j),
        x i.succ ^ (α j.castSucc + k) * x 0 ^ (d j - 1 - k))ᵀ
      = Matrix.of fun (j i : Fin N) => ∑ k : Fin (d j),
          x 0 ^ (d j - 1 - k) * x i.succ ^ (α j.castSucc + k) := by
    ext j i; simp only [transpose_apply, of_apply]
    exact Finset.sum_congr rfl fun k _ => mul_comm _ _
  erw [htr]
  rw [det_sum_rows d (fun j k i => x 0 ^ (d j - 1 - k) * x i.succ ^ (α j.castSucc + k))]
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [det_mul_column, ← det_transpose, Finset.prod_pow_eq_pow_sum]
  congr 1
  · congr 1
    refine Finset.sum_congr rfl fun j _ => ?_
    simp only [hd]; omega

/-! ## The Schur polynomial by branching, and the bialternant formula -/

/-- The Schur polynomial `s_ν(x₀, …, x_{N−1})` of a weakly *increasing* sequence `ν`
(a partition written smallest part first), defined by branching on `x₀`: the interlacing
`μ_j = ν_j + k_j ∈ [ν_j, ν_{j+1}]` carries weight `x₀^{|ν| − |μ|}`. -/
def schur : (N : ℕ) → (Fin N → ℕ) → (Fin N → R) → R
  | 0, _, _ => 1
  | N + 1, ν, x =>
      ∑ k : (j : Fin N) → Fin (ν j.succ + 1 - ν j.castSucc),
        x 0 ^ (ν 0 + ∑ j, (ν j.succ - (ν j.castSucc + k j))) *
          schur N (fun j => ν j.castSucc + k j) (Fin.tail x)

/-- The staircase `δ_j = j`. -/
def stair (N : ℕ) : Fin N → ℕ := fun j => j

theorem alt_zero (x : Fin 0 → R) (α : Fin 0 → ℕ) : alt x α = 1 := by
  simp [alt]

/-- Branching for the Vandermonde alternant: every gap is `1`, so the sum has one term. -/
theorem alt_stair_succ {N : ℕ} (x : Fin (N + 1) → R) :
    alt x (stair (N + 1)) = (∏ i : Fin N, (x i.succ - x 0)) * alt (Fin.tail x) (stair N) := by
  rw [alt_succ x _ (fun a b h => by simpa [stair] using h)]
  have hd : ∀ j : Fin N, stair (N + 1) j.succ - stair (N + 1) j.castSucc = 1 := by
    intro j; simp [stair]
  have hsub : Subsingleton ((j : Fin N) → Fin (stair (N + 1) j.succ - stair (N + 1) j.castSucc)) :=
    ⟨fun r r' => funext fun j => Fin.ext (by
      have h1 := (r j).2; have h2 := (r' j).2; have := hd j; omega)⟩
  let r0 : (j : Fin N) → Fin (stair (N + 1) j.succ - stair (N + 1) j.castSucc) :=
    fun j => ⟨0, by rw [hd]; omega⟩
  rw [Fintype.sum_eq_single r0 (fun r hr => absurd (Subsingleton.elim r r0) hr)]
  have he : ∀ j : Fin N, stair (N + 1) j.succ - 1 - (stair (N + 1) j.castSucc + (r0 j : ℕ)) = 0 := by
    intro j; simp [stair, r0]
  simp only [he, Finset.sum_const_zero, pow_zero, one_mul]
  simp [stair, r0]
  rfl

theorem schur_index_monotone {N : ℕ} (ν : Fin (N + 1) → ℕ) (hν : Monotone ν)
    (k : (j : Fin N) → Fin (ν j.succ + 1 - ν j.castSucc)) :
    Monotone (fun j : Fin N => ν j.castSucc + k j) := by
  intro a b hab
  rcases hab.lt_or_eq with h | h
  · have h1 : (k a : ℕ) < ν a.succ + 1 - ν a.castSucc := (k a).2
    have h2 : ν a.succ ≤ ν b.castSucc :=
      hν (by rw [Fin.le_def]; simp only [Fin.val_succ, Fin.coe_castSucc]; exact h)
    have h3 : ν a.castSucc ≤ ν a.succ := hν (Fin.castSucc_le_succ a)
    simp only
    omega
  · rw [h]

/-- **The bialternant formula** `a_{ν+δ}(x) = a_δ(x) · s_ν(x)`, for every weakly increasing `ν`
and every family of elements of a commutative ring. -/
theorem alt_add_stair (N : ℕ) (ν : Fin N → ℕ) (hν : Monotone ν) (x : Fin N → R) :
    alt x (fun j => ν j + stair N j) = alt x (stair N) * schur N ν x := by
  induction N with
  | zero => simp [alt_zero, schur]
  | succ N ih =>
    have hα : Monotone (fun j : Fin (N + 1) => ν j + stair (N + 1) j) :=
      fun a b h => Nat.add_le_add (hν h) (by simpa [stair] using h)
    rw [alt_succ x _ hα, alt_stair_succ, schur, Finset.mul_sum, Finset.mul_sum]
    have hd : ∀ j : Fin N, ν j.succ + stair (N + 1) j.succ - (ν j.castSucc + stair (N + 1) j.castSucc)
        = ν j.succ + 1 - ν j.castSucc := by
      intro j; simp only [stair, Fin.val_succ, Fin.coe_castSucc]; omega
    let e : ((j : Fin N) → Fin (ν j.succ + stair (N + 1) j.succ - (ν j.castSucc + stair (N + 1) j.castSucc)))
        ≃ ((j : Fin N) → Fin (ν j.succ + 1 - ν j.castSucc)) :=
      Equiv.piCongrRight fun j => finCongr (hd j)
    refine Fintype.sum_equiv e _ _ fun k => ?_
    have hk : ∀ j, ((e k) j : ℕ) = k j := fun j => rfl
    have hmono := schur_index_monotone ν hν (e k)
    have hih := ih _ hmono (Fin.tail x)
    simp only at hih
    have hexp : ν 0 + stair (N + 1) 0 + ∑ j : Fin N, (ν j.succ + stair (N + 1) j.succ - 1 -
          (ν j.castSucc + stair (N + 1) j.castSucc + k j))
        = ν 0 + ∑ j : Fin N, (ν j.succ - (ν j.castSucc + (e k) j)) := by
      simp only [stair, Fin.val_zero, add_zero]
      congr 1
      refine Finset.sum_congr rfl fun j _ => ?_
      have := hk j
      simp only [Fin.val_succ, Fin.coe_castSucc]; omega
    have halt : alt (Fin.tail x) (fun j => ν j.castSucc + stair (N + 1) j.castSucc + k j)
        = alt (Fin.tail x) (fun j => ν j.castSucc + (e k) j + stair N j) := by
      congr 1; funext j; have := hk j; simp only [stair, Fin.coe_castSucc]; omega
    rw [halt, hih, ← hexp, pow_add]
    ring

end QOU.Mathlib.Bialternant
