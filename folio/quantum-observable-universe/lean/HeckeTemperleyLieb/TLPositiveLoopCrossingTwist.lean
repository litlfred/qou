import HeckeTemperleyLieb.TemperleyLiebMarkovNondegenerate
import HeckeTemperleyLieb.TLRootOfUnitySMatrixNondegenerate
import Mathlib.Tactic.Module

/-!
# The twist in the positive-loop convention matches `T = diag(ω^{(j+1)²})`

`TLKauffmanCrossingJonesWenzl` uses the Kauffman convention, loop value `δ = −(A² + A⁻²)`, where the
ribbon twist on the simple with `j` strands is `(−1)ʲ A^{j(j+2)}`. The root-of-unity `S`-matrix file
(and the vacuum-row bridge `TLVacuumRowFromJonesWenzl`) use the **positive** loop value
`δ = ζ + ζ⁻¹`. In that convention the crossing is `σᵢ = A·1 − A⁻¹·eᵢ` with `δ = A² + A⁻²`
(the image of the Kauffman crossing under `eᵢ ↦ −eᵢ`), and the sign `(−1)ʲ` disappears.

* `crossing_mul_crossingInv`, `crossingInv_mul_crossing`, `crossing_braid`, `crossing_commute`:
  `σᵢ` is an invertible braid generator in the corpus `TLFin K δ n`.
* `jw_mul_crossing`, `jw_mul_fullTwist`: the Jones–Wenzl projector `p_n` (on `n + 1` strands)
  absorbs each crossing as `A`, so the full twist acts on it by `A^{n(n+1)}`.
* `markov_curl`: for any Markov trace with `δε = 1`, closing the last strand through one crossing
  multiplies the unnormalised trace by `A³` (`δ·τ_{n+1}(ι(x)σ_n) = A³·τ_n(x)`): the framing factor
  is `+A³`, with no sign.
* `twist_eq_tMatrix`: with `A = ω`, the scalar `(A³)^{n+1}·A^{n(n+1)}` (framing factor per strand
  times full twist) equals `ω⁻¹·T_{n+1,n+1}`, so the twists agree with `tMatrix` up to the single
  global scalar `ω⁻¹`; ratios `θ_j/θ_0 = ω^{j(j+2)}` match exactly.

Not proved here: that the ribbon twist on `p_n` *is* that product (the curl on each interior strand
needs a partial trace on a non-last strand; the decomposition is standard, Kauffman–Lins).
-/

namespace QOU.HeckeTemperleyLieb.TLPositiveLoop

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov

variable {K : Type*} [Field K] {δ A : K} (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) {n : ℕ}

variable (δ A) in
/-- The positive-loop crossing `σᵢ = A·1 − A⁻¹·eᵢ`. -/
noncomputable def crossing (i : Fin n) : TLFin K δ n := A • 1 - A⁻¹ • e K δ adjFin i

variable (δ A) in
/-- Its inverse `A⁻¹·1 − A·eᵢ`. -/
noncomputable def crossingInv (i : Fin n) : TLFin K δ n := A⁻¹ • 1 - A • e K δ adjFin i

include hA hδ in
theorem crossing_mul_crossingInv (i : Fin n) :
    crossing δ A i * crossingInv δ A i = 1 := by
  unfold crossing crossingInv
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    e_sq']
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

include hA hδ in
theorem crossingInv_mul_crossing (i : Fin n) :
    crossingInv δ A i * crossing δ A i = 1 := by
  unfold crossing crossingInv
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    e_sq']
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

theorem crossing_commute {i j : Fin n} (h : ¬ (i.val + 1 = j.val ∨ j.val + 1 = i.val)) :
    crossing δ A i * crossing δ A j = crossing δ A j * crossing δ A i := by
  have hc : e K δ adjFin i * e K δ adjFin j = e K δ adjFin j * e K δ adjFin i :=
    e_farCommute (show ¬ adjFin i j from h)
  unfold crossing
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, hc]
  module

include hA hδ in
theorem crossing_braid {i j : Fin n} (h : i.val + 1 = j.val ∨ j.val + 1 = i.val) :
    crossing δ A i * crossing δ A j * crossing δ A i =
      crossing δ A j * crossing δ A i * crossing δ A j := by
  have hi := e_sq' δ i
  have hj := e_sq' δ j
  have hiji' : e K δ adjFin i * (e K δ adjFin j * e K δ adjFin i) = e K δ adjFin i := by
    rw [← mul_assoc, e_adjacent_fin h]
  have hjij' : e K δ adjFin j * (e K δ adjFin i * e K δ adjFin j) = e K δ adjFin j := by
    rw [← mul_assoc, e_adjacent_fin h.symm]
  unfold crossing
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    mul_assoc, hiji', hjij', hi, hj]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- The Jones–Wenzl projector absorbs a crossing as `A`. -/
theorem jw_mul_crossing (hS : JWSpec δ n) (i : Fin n) :
    jw δ n * crossing δ A i = A • jw δ n := by
  unfold crossing
  rw [mul_sub, mul_smul_comm, mul_one, mul_smul_comm, hS.1 i, smul_zero, sub_zero]

/-- A positive braid word `w` acts on `p_n` by `A^{|w|}`. -/
theorem jw_mul_word (hS : JWSpec δ n) (w : List (Fin n)) :
    jw δ n * (w.map (crossing δ A)).prod = A ^ w.length • jw δ n := by
  induction w with
  | nil => simp
  | cons a w ih =>
    rw [List.map_cons, List.prod_cons, ← mul_assoc, jw_mul_crossing hS, smul_mul_assoc, ih,
      smul_smul, List.length_cons, pow_succ, mul_comm]

/-- The full twist `Δ² = (σ₀⋯σ_{n−1})^{n+1}` on `n + 1` strands. -/
noncomputable def fullTwist (δ A : K) (n : ℕ) : TLFin K δ n :=
  (((List.finRange n).map (crossing δ A)).prod) ^ (n + 1)

/-- The full twist acts on `p_n` by `A^{n(n+1)}`. -/
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

include hA hδ in
/-- **Framing factor.** For any Markov trace with `δε = 1`, closing the last strand through one
crossing multiplies the unnormalised trace by `A³`. -/
theorem markov_curl {ε : K} (T : MarkovTower δ ε) (hε : δ * ε = 1) (x : TLFin K δ n) :
    δ * T.τ (n + 1) (incl δ n x * crossing δ A (Fin.last n)) = A ^ 3 * T.τ n x := by
  unfold crossing
  rw [mul_sub, mul_smul_comm, mul_one, mul_smul_comm, map_sub, map_smul, map_smul, T.tr_incl,
    T.tr_markov, smul_eq_mul, smul_eq_mul]
  generalize T.τ n x = t
  have hAA : A * A⁻¹ = 1 := mul_inv_cancel₀ hA
  linear_combination (-A⁻¹ * t) * hε + (A * t) * hδ + (A⁻¹ * t) * hAA

/-- **Matching `T`.** With `A = ω`, framing factor `(A³)^{n+1}` times the full-twist scalar
`A^{n(n+1)}` is `ω⁻¹·T_{n+1,n+1}`: the twists equal `tMatrix` up to the global scalar `ω⁻¹`. -/
theorem twist_eq_tMatrix (ω : Kˣ) (n : ℕ) :
    ((ω : K) ^ 3) ^ (n + 1) * (ω : K) ^ (n * (n + 1)) * (ω : K) =
      TLRootOfUnity.thetaW ω (n + 1 + 1) := by
  unfold TLRootOfUnity.thetaW
  rw [show ((n + 1 + 1 : ℕ) : ℤ) ^ 2 = (((n + 2) ^ 2 : ℕ) : ℤ) by push_cast; ring, zpow_natCast,
    Units.val_pow_eq_pow_val, ← pow_mul, ← pow_add, ← pow_succ]
  congr 1
  ring

end QOU.HeckeTemperleyLieb.TLPositiveLoop
