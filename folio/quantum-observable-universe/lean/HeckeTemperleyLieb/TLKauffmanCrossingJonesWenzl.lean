import HeckeTemperleyLieb.TemperleyLiebMarkovNondegenerate
import Mathlib.Tactic.Module

/-!
# Kauffman crossings in the Temperley–Lieb tower and the Jones–Wenzl twist scalar

At loop value `δ = −(A² + A⁻²)` the Kauffman crossing `σᵢ = A·1 + A⁻¹·eᵢ` in the corpus
Temperley–Lieb algebra `TLFin K δ n` (on `n + 1` strands) is a braid representation:

* `crossing_mul_crossingInv`, `crossingInv_mul_crossing`: `σᵢ` is invertible,
  `σᵢ⁻¹ = A⁻¹·1 + A·eᵢ`;
* `crossing_braid`: `σᵢσⱼσᵢ = σⱼσᵢσⱼ` for adjacent `i, j`;
* `crossing_commute`: `σᵢσⱼ = σⱼσᵢ` for far-apart `i, j`.

The corpus Jones–Wenzl projector `p_n = jw δ n` absorbs every crossing as the scalar `A`
(`jw_mul_crossing`, `crossing_mul_jw`), because `p_n eᵢ = eᵢ p_n = 0`. Hence any braid word `w`
acts on `p_n` by `A^{|w|}` (`jw_mul_word`), and the full twist `Δ² = (σ₀⋯σ_{n−1})^{n+1}` on
`n + 1` strands acts by `A^{n(n+1)}` (`jw_mul_fullTwist`).

This is the braid part of the ribbon twist on the simple `f_{n+1}`. The framing (curl) factor
`(−A³)` per strand, and the identification of the result with the level-`k` matrix
`T = diag(ω^{(j+1)²})` of `TLRootOfUnitySMatrixNondegenerate`, are not derived here.
-/

namespace QOU.HeckeTemperleyLieb.TLKauffmanCrossing

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov

variable {K : Type*} [Field K] {δ A : K} (hA : A ≠ 0) (hδ : δ = -(A ^ 2 + A⁻¹ ^ 2))
  {n : ℕ}

variable (δ A) in
/-- The Kauffman crossing `σᵢ = A·1 + A⁻¹·eᵢ`. -/
noncomputable def crossing (i : Fin n) : TLFin K δ n := A • 1 + A⁻¹ • e K δ adjFin i

variable (δ A) in
/-- The candidate inverse crossing `A⁻¹·1 + A·eᵢ`. -/
noncomputable def crossingInv (i : Fin n) : TLFin K δ n := A⁻¹ • 1 + A • e K δ adjFin i

include hA hδ in
theorem crossing_mul_crossingInv (i : Fin n) :
    crossing δ A i * crossingInv δ A i = 1 := by
  unfold crossing crossingInv
  simp only [mul_add, add_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    e_sq']
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

include hA hδ in
theorem crossingInv_mul_crossing (i : Fin n) :
    crossingInv δ A i * crossing δ A i = 1 := by
  unfold crossing crossingInv
  simp only [mul_add, add_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    e_sq']
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

theorem crossing_commute {i j : Fin n} (h : ¬ (i.val + 1 = j.val ∨ j.val + 1 = i.val)) :
    crossing δ A i * crossing δ A j = crossing δ A j * crossing δ A i := by
  have hc : e K δ adjFin i * e K δ adjFin j = e K δ adjFin j * e K δ adjFin i :=
    e_farCommute (show ¬ adjFin i j from h)
  unfold crossing
  simp only [mul_add, add_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, hc]
  module

include hA hδ in
theorem crossing_braid {i j : Fin n} (h : i.val + 1 = j.val ∨ j.val + 1 = i.val) :
    crossing δ A i * crossing δ A j * crossing δ A i =
      crossing δ A j * crossing δ A i * crossing δ A j := by
  have hiji := e_adjacent_fin (δ := δ) h
  have hjij := e_adjacent_fin (δ := δ) (i := j) (j := i) (h.symm)
  have hi := e_sq' δ i
  have hj := e_sq' δ j
  have hiji' : e K δ adjFin i * (e K δ adjFin j * e K δ adjFin i) = e K δ adjFin i := by
    rw [← mul_assoc, hiji]
  have hjij' : e K δ adjFin j * (e K δ adjFin i * e K δ adjFin j) = e K δ adjFin j := by
    rw [← mul_assoc, hjij]
  unfold crossing
  simp only [mul_add, add_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    mul_assoc, hiji', hjij', hi, hj]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- The Jones–Wenzl projector absorbs a crossing on the right as the scalar `A`. -/
theorem jw_mul_crossing (hS : JWSpec δ n) (i : Fin n) :
    jw δ n * crossing δ A i = A • jw δ n := by
  unfold crossing
  rw [mul_add, mul_smul_comm, mul_one, mul_smul_comm, hS.1 i, smul_zero, add_zero]

/-- The Jones–Wenzl projector absorbs a crossing on the left as the scalar `A`. -/
theorem crossing_mul_jw (hS : JWSpec δ n) (i : Fin n) :
    crossing δ A i * jw δ n = A • jw δ n := by
  unfold crossing
  rw [add_mul, smul_mul_assoc, one_mul, smul_mul_assoc, hS.2.1 i, smul_zero, add_zero]

/-- Any braid word `w` (positive crossings) acts on `p_n` by `A^{|w|}`. -/
theorem jw_mul_word (hS : JWSpec δ n) (w : List (Fin n)) :
    jw δ n * (w.map (crossing δ A)).prod = A ^ w.length • jw δ n := by
  induction w with
  | nil => simp
  | cons a w ih =>
    rw [List.map_cons, List.prod_cons, ← mul_assoc, jw_mul_crossing hS, smul_mul_assoc, ih,
      smul_smul, List.length_cons, pow_succ, mul_comm]

/-- The full twist `Δ² = (σ₀σ₁⋯σ_{n−1})^{n+1}` on `n + 1` strands. -/
noncomputable def fullTwist (δ A : K) (n : ℕ) : TLFin K δ n :=
  (((List.finRange n).map (crossing δ A)).prod) ^ (n + 1)

/-- **Twist scalar.** The full twist acts on the Jones–Wenzl projector on `n + 1` strands by
`A^{n(n+1)}`. -/
theorem jw_mul_fullTwist (hS : JWSpec δ n) :
    jw δ n * fullTwist δ A n = A ^ (n * (n + 1)) • jw δ n := by
  have hstep := jw_mul_word (A := A) hS (List.finRange n)
  rw [List.length_finRange] at hstep
  have key : ∀ m : ℕ, jw δ n * ((List.finRange n).map (crossing δ A)).prod ^ m =
      (A ^ n) ^ m • jw δ n := by
    intro m
    induction m with
    | zero => simp
    | succ m ih => rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, hstep, smul_smul, pow_succ]
  rw [fullTwist, key, ← pow_mul]

/-- With the corpus genericity hypothesis, the twist scalar holds for the actual `jw δ n`. -/
theorem jw_mul_fullTwist_of_qint (hg : ∀ k ≤ n, qint δ (k + 1) ≠ 0) :
    jw δ n * fullTwist δ A n = A ^ (n * (n + 1)) • jw δ n :=
  jw_mul_fullTwist (jw_spec δ n hg)

end QOU.HeckeTemperleyLieb.TLKauffmanCrossing
