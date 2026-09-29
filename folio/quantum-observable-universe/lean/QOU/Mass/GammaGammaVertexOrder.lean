import QOU.Mass.GammaGammaSelectorH3

/-!
# The γγ vertex is the `q`-deformed 3-cycle: powers, symmetry, and the Chebyshev table

Bean `qou-ales`, step 4 — the `k ≥ 2` non-symmetry left open in §4.3 of the
step-3 record (`docs/audits/2026-09-11-gamma-gamma-word-selection-step3.md`).
Step 3 proved that the `(2,1)`-block image `V` of one pair-production vertex
`σ₀σ₁⁻¹` is not symmetric, and *measured* (to `k ≤ 5`, at the proton `q₀`)
that no power `V^k` is either. This file replaces the measurement by algebra.

## What is proved (all sorry-free)

Let `h = q − q⁻¹` and let `V = ρ_(2,1)(σ₀σ₁⁻¹)` be the Hoefsmit image of the
vertex (`stdImage_vertex_entries`). Everything below is over a generic field
unless an order is used.

* `vtx_det`, `vtx_trace` — from the Hoefsmit relations alone,
  `det V = 1` and `tr V = −1 − h²`.
* `sq_eq_of_det_one` — Cayley–Hamilton for a `2×2` matrix of determinant one,
  `M² = (tr M)·M − 1`; hence `pow_eq_lin`: `M^k = α_k M + β_k 1` with
  `α_{k+1} = t α_k + β_k`, `β_{k+1} = −α_k` (`lin`).
* `vtx_pow_isHermitian_iff` — on `ℝ` with `b ≠ 0`,
  **`V^k` is symmetric ⇔ `α_k = 0` ⇔ `V^k = ±1`** (`vtx_pow_isHermitian_iff_scalar`).
  So the *literal* `Matrix.PosSemidef` reading admits a non-trivial γγ word in
  `H₃` iff some vertex power is a scalar — iff `θ/π` is rational, where
  `2 cos θ = tr V`.
* `vtx_three` — `V³ = (2h² + h⁴)·V + (1 + h²)·1`, i.e.
  `V³ − 1 = h²·((2 + h²)·V + 1)`; hence `vtx_three_eq_one_iff`: `V³ = 1 ⇔ h = 0`.
  At `q = 1` the vertex is the 3-cycle `s₀s₁ ∈ S₃`, so the `k = 3` survivor of
  step 3 (`β_Bor`) is its **`q`-deformation** — which is *why* it lies within
  `0.11` of the identity at `q₀` and why the selected pp bond moves the
  diproton by only `4.5` keV.
* `trace_vtx_pow_*` — the probe's `χ_(2,1)` column is the Chebyshev recurrence
  `χ_{k+1} = (tr V)·χ_k − χ_{k−1}` in closed form: with `x = h²`,
  `χ₁ = −1 − x`, `χ₂ = x² + 2x − 1`, `χ₃ = 2 − 3x² − x³`,
  `χ₄ = x⁴ + 4x³ + 2x² − 4x − 1`, `χ₅ = −x⁵ − 5x⁴ − 5x³ + 5x² + 5x − 1`.
* `chi_signs_of_small` — for every `0 < x ≤ 1/10` the signs are
  `(−, −, +, −, −)` for `k = 1..5`, and `lin_ne_zero_of_small` — `α_k ≠ 0`
  for `k = 1..5`. The proton pin has `h² ≈ 0.0437` (`h_sq_le_of_q_le`), so the
  step-3 table is a theorem on an interval, not a point measurement: under the
  Frobenius reading the minimal non-zero survivor is `k = 3` for every such `q`,
  and under the literal reading no `k ≤ 5` survives for any such `q`.

## What is NOT proved

Whether some `V^k = ±1` for *some* `k` at the proton pin — i.e. whether
`θ/π ∈ ℚ` — is not decided here; it is the arithmetic of `cos θ = −(1+h²)/2`
at a transcendental-looking `q₀`, and `lin_ne_zero_of_small` covers `k ≤ 5`
only. Nothing here reads AME, CODATA, or a census.

## Base ring (§7c)

`lin`, Cayley–Hamilton, `pow_eq_lin`, the trace/determinant identities and the
closed-form traces are over a generic `[Field R]` (or `[CommRing R]`). Only the
symmetry criterion (`Matrix.IsHermitian` on `ℝ`), the sign lemmas and the `q`
bound use an order.
-/

namespace QOU.Mass.GammaGammaVertexOrder

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaSelectorH3

/-! ## Generic `2×2` algebra: Cayley–Hamilton at determinant one -/

section TwoByTwo

variable {R : Type*} [CommRing R]

/-- The linearisation coefficients: `M^k = (lin t k).1 • M + (lin t k).2 • 1`
for any `M` with `M * M = t • M - 1` (`pow_eq_lin`). -/
def lin (t : R) : ℕ → R × R
  | 0 => (0, 1)
  | k + 1 => (t * (lin t k).1 + (lin t k).2, -(lin t k).1)

@[simp] theorem lin_zero (t : R) : lin t 0 = (0, 1) := rfl

@[simp] theorem lin_succ (t : R) (k : ℕ) :
    lin t (k + 1) = (t * (lin t k).1 + (lin t k).2, -(lin t k).1) := rfl

theorem lin_one (t : R) : lin t 1 = (1, 0) := by
  ext <;> simp

theorem lin_two (t : R) : lin t 2 = (t, -1) := by
  ext <;> simp

theorem lin_three (t : R) : lin t 3 = (t ^ 2 - 1, -t) := by
  ext <;> simp
  ring

theorem lin_four (t : R) : lin t 4 = (t ^ 3 - 2 * t, -(t ^ 2 - 1)) := by
  ext <;> simp <;> ring

theorem lin_five (t : R) : lin t 5 = (t ^ 4 - 3 * t ^ 2 + 1, -(t ^ 3 - 2 * t)) := by
  ext <;> simp <;> ring

/-- **Cayley–Hamilton for a `2×2` matrix of determinant one**, entrywise. -/
theorem sq_eq_of_det_one (M : Matrix (Fin 2) (Fin 2) R) (hdet : M.det = 1) :
    M * M = M.trace • M - 1 := by
  rw [Matrix.det_fin_two] at hdet
  rw [Matrix.trace_fin_two]
  ext i j
  fin_cases i <;> fin_cases j
  · simp [Matrix.mul_apply, Fin.sum_univ_two]
    linear_combination -1 * hdet
  · simp [Matrix.mul_apply, Fin.sum_univ_two]
    ring
  · simp [Matrix.mul_apply, Fin.sum_univ_two]
    ring
  · simp [Matrix.mul_apply, Fin.sum_univ_two]
    linear_combination -1 * hdet

/-- `M^k` is the `lin`-combination of `M` and `1` whenever `M² = t·M − 1`. -/
theorem pow_eq_lin (M : Matrix (Fin 2) (Fin 2) R) (t : R) (hM : M * M = t • M - 1) (k : ℕ) :
    M ^ k = (lin t k).1 • M + (lin t k).2 • (1 : Matrix (Fin 2) (Fin 2) R) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, ih, lin_succ]
    rw [add_mul, smul_mul_assoc, smul_mul_assoc, one_mul, hM]
    rw [smul_sub, smul_smul, add_smul, neg_smul, mul_comm t]
    abel

/-- The trace of `M^k` in terms of the `lin` coefficients. -/
theorem trace_pow_eq (M : Matrix (Fin 2) (Fin 2) R) (t : R) (hM : M * M = t • M - 1)
    (k : ℕ) : (M ^ k).trace = (lin t k).1 * M.trace + 2 * (lin t k).2 := by
  rw [pow_eq_lin M t hM k]
  simp [Matrix.trace_add, Matrix.trace_smul, Matrix.trace_one]
  ring

/-- The off-diagonal defect of `M^k` is `α_k` times that of `M`. -/
theorem pow_off_diagonal (M : Matrix (Fin 2) (Fin 2) R) (t : R) (hM : M * M = t • M - 1)
    (k : ℕ) : (M ^ k) 0 1 - (M ^ k) 1 0 = (lin t k).1 * (M 0 1 - M 1 0) := by
  rw [pow_eq_lin M t hM k]
  simp [Matrix.add_apply, Matrix.smul_apply]
  ring

end TwoByTwo

/-! ## The vertex image: determinant one, trace `−1 − h²` -/

section Vertex

variable {R : Type*} [Field R]

/-- The `(2,1)`-block image of the γγ vertex `σ₀σ₁⁻¹` under the Hoefsmit data. -/
def vtx (q a b a' h : R) : Matrix (Fin 2) (Fin 2) R :=
  stdImage (hoefsmitGen q a b a') h (vertex 0)

theorem vtx_entries (q a b a' h : R) :
    vtx q a b a' h = !![q * (a - h), q * b; -q⁻¹ * b, -q⁻¹ * (a' - h)] :=
  stdImage_vertex_entries q a b a' h

/-- The vertex power's image is the power of the vertex image. -/
theorem stdImage_vertexPow (S : ℕ → Matrix (Fin 2) (Fin 2) R) (h : R) (k : ℕ) :
    stdImage S h (vertexPow k) = (stdImage S h (vertex 0)) ^ k := by
  induction k with
  | zero => simp [vertexPow, stdImage_nil]
  | succ k ih =>
    rw [vertexPow, pow_succ']
    rw [← ih]
    simp [stdImage, List.map_append, List.prod_append]

/-- The Hoefsmit relations `a(1 − q⁴) = h`, `h = q − q⁻¹` force
`a·q·(1 + q²) = −1` whenever `q² ≠ 1`. -/
theorem hoefsmit_a_mul {q a h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (hq1 : q ^ 2 ≠ 1) : a * q * (1 + q ^ 2) = -1 := by
  have h0 : (a * q * (1 + q ^ 2) + 1) * (1 - q ^ 2) = 0 := by
    linear_combination q * ha + q * hh - hqinv
  have h1 : (1 : R) - q ^ 2 ≠ 0 := sub_ne_zero.mpr hq1.symm
  have := (mul_eq_zero.mp h0).resolve_right h1
  linear_combination this

/-- `tr V = −1 − h²`. -/
theorem vtx_trace {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hq1 : q ^ 2 ≠ 1) :
    (vtx q a b a' h).trace = -1 - h ^ 2 := by
  have hA := hoefsmit_a_mul hqinv hh ha hq1
  rw [vtx_entries, Matrix.trace_fin_two_of]
  subst ha'
  linear_combination hA + h * hh + q ^ 3 * a * hqinv

/-- `det V = 1`. -/
theorem vtx_det {q a b a' h : R} (hqinv : q * q⁻¹ = 1)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1) :
    (vtx q a b a' h).det = 1 := by
  have hsum : a + a' = h := by
    rw [ha']
    linear_combination ha
  rw [vtx_entries, Matrix.det_fin_two_of]
  linear_combination (-(a - h) * (a' - h) + b ^ 2) * hqinv + h * hsum + hb

/-- Cayley–Hamilton for the vertex: `V² = (−1 − h²)·V − 1`. -/
theorem vtx_sq {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) :
    vtx q a b a' h * vtx q a b a' h = (-1 - h ^ 2) • vtx q a b a' h - 1 := by
  rw [← vtx_trace hqinv hh ha ha' hq1]
  exact sq_eq_of_det_one _ (vtx_det hqinv ha ha' hb)

/-- `V^k = α_k V + β_k 1`. -/
theorem vtx_pow_eq_lin {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) (k : ℕ) :
    vtx q a b a' h ^ k =
      (lin (-1 - h ^ 2) k).1 • vtx q a b a' h +
        (lin (-1 - h ^ 2) k).2 • (1 : Matrix (Fin 2) (Fin 2) R) :=
  pow_eq_lin _ _ (vtx_sq hqinv hh ha ha' hb hq1) k

/-- **The vertex cube is the `q`-deformed identity**:
`V³ = (2h² + h⁴)·V + (1 + h²)·1`. -/
theorem vtx_three {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) :
    vtx q a b a' h ^ 3 =
      (2 * h ^ 2 + h ^ 4) • vtx q a b a' h + (1 + h ^ 2) • (1 : Matrix (Fin 2) (Fin 2) R) := by
  rw [vtx_pow_eq_lin hqinv hh ha ha' hb hq1 3, lin_three]
  have e1 : ((-1 - h ^ 2) ^ 2 - 1 : R) = 2 * h ^ 2 + h ^ 4 := by ring
  have e2 : (-(-1 - h ^ 2) : R) = 1 + h ^ 2 := by ring
  rw [e1, e2]

/-- `V³ − 1 = h²·((2 + h²)·V + 1)`: the defect from the identity is exactly `h²`
times a matrix whose `(0,1)` entry is `(2 + h²)·q·b`. -/
theorem vtx_three_sub_one {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) :
    vtx q a b a' h ^ 3 - 1 =
      h ^ 2 • ((2 + h ^ 2) • vtx q a b a' h + (1 : Matrix (Fin 2) (Fin 2) R)) := by
  rw [vtx_three hqinv hh ha ha' hb hq1, smul_add, smul_smul]
  have e1 : (h ^ 2 * (2 + h ^ 2) : R) = 2 * h ^ 2 + h ^ 4 := by ring
  have e2 : ((1 : R) + h ^ 2) • (1 : Matrix (Fin 2) (Fin 2) R) - 1 = h ^ 2 • 1 := by
    rw [add_smul, one_smul]
    abel
  rw [e1, add_sub_assoc, e2]

/-- Closed-form traces of the first five vertex powers (`x = h²`): the probe's
`χ_(2,1)` column is this Chebyshev recurrence. -/
theorem trace_vtx_pow_one {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) : (vtx q a b a' h ^ 1).trace = -1 - h ^ 2 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_one]
  ring

theorem trace_vtx_pow_two {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) : (vtx q a b a' h ^ 2).trace = h ^ 4 + 2 * h ^ 2 - 1 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_two]
  ring

theorem trace_vtx_pow_three {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) : (vtx q a b a' h ^ 3).trace = 2 - 3 * h ^ 4 - h ^ 6 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_three]
  ring

theorem trace_vtx_pow_four {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) :
    (vtx q a b a' h ^ 4).trace = h ^ 8 + 4 * h ^ 6 + 2 * h ^ 4 - 4 * h ^ 2 - 1 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_four]
  ring

theorem trace_vtx_pow_five {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) :
    (vtx q a b a' h ^ 5).trace =
      -h ^ 10 - 5 * h ^ 8 - 5 * h ^ 6 + 5 * h ^ 4 + 5 * h ^ 2 - 1 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_five]
  ring

end Vertex

/-! ## Archimedean part: symmetry of `V^k` on `ℝ`, and the interval statements -/

section Real

/-- A real `2×2` matrix is Hermitian (= symmetric) iff its two off-diagonal
entries agree. -/
theorem isHermitian_iff_off (A : Matrix (Fin 2) (Fin 2) ℝ) :
    A.IsHermitian ↔ A 0 1 = A 1 0 := by
  constructor
  · intro H
    have := H.apply 0 1
    simpa using this.symm
  · intro h
    apply Matrix.IsHermitian.ext
    intro i j
    fin_cases i <;> fin_cases j <;> simp [h]

/-- **`V^k` is symmetric iff `α_k = 0`** (with `t = −1 − h²`), for `0 < q` and
`b ≠ 0`: the off-diagonal defect of `V` is `b(q + q⁻¹) ≠ 0`, and that of `V^k`
is `α_k` times it. -/
theorem vtx_pow_isHermitian_iff {q a b a' h : ℝ} (hq : 0 < q) (hb : b ≠ 0)
    (hh : h = q - q⁻¹) (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a)
    (hbb : b ^ 2 = a * a' + 1) (hq1 : q ^ 2 ≠ 1) (k : ℕ) :
    (vtx q a b a' h ^ k).IsHermitian ↔ (lin (-1 - h ^ 2) k).1 = 0 := by
  have hqinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq.ne'
  have hoff : (vtx q a b a' h) 0 1 - (vtx q a b a' h) 1 0 = b * (q + q⁻¹) := by
    rw [vtx_entries]
    simp
    ring
  have hne : b * (q + q⁻¹) ≠ 0 := mul_ne_zero hb (by positivity)
  rw [isHermitian_iff_off, ← sub_eq_zero,
    pow_off_diagonal _ _ (vtx_sq hqinv hh ha ha' hbb hq1), hoff]
  constructor
  · intro h0
    exact (mul_eq_zero.mp h0).resolve_right hne
  · intro h0
    rw [h0, zero_mul]

/-- **`V^k` is symmetric iff it is `±1`.** -/
theorem vtx_pow_isHermitian_iff_scalar {q a b a' h : ℝ} (hq : 0 < q) (hb : b ≠ 0)
    (hh : h = q - q⁻¹) (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a)
    (hbb : b ^ 2 = a * a' + 1) (hq1 : q ^ 2 ≠ 1) (k : ℕ) :
    (vtx q a b a' h ^ k).IsHermitian ↔
      vtx q a b a' h ^ k = 1 ∨ vtx q a b a' h ^ k = -1 := by
  have hqinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq.ne'
  rw [vtx_pow_isHermitian_iff hq hb hh ha ha' hbb hq1 k]
  constructor
  · intro h0
    have hpow := vtx_pow_eq_lin hqinv hh ha ha' hbb hq1 k
    rw [h0, zero_smul, zero_add] at hpow
    have hdet : (vtx q a b a' h ^ k).det = 1 := by
      rw [Matrix.det_pow, vtx_det hqinv ha ha' hbb, one_pow]
    rw [hpow, Matrix.det_smul, Matrix.det_one, mul_one, Fintype.card_fin] at hdet
    have hβ : (lin (-1 - h ^ 2) k).2 = 1 ∨ (lin (-1 - h ^ 2) k).2 = -1 := by
      rw [← mul_self_eq_one_iff, ← sq]
      exact hdet
    rcases hβ with hβ | hβ
    · left; rw [hpow, hβ, one_smul]
    · right; rw [hpow, hβ, neg_one_smul]
  · intro h0
    have hsym : (vtx q a b a' h ^ k).IsHermitian := by
      rcases h0 with h0 | h0 <;> rw [h0]
      · exact Matrix.isHermitian_one
      · exact Matrix.isHermitian_one.neg
    exact (vtx_pow_isHermitian_iff hq hb hh ha ha' hbb hq1 k).mp hsym

/-- **`V³ = 1 ⇔ h = 0`**: the cube of the vertex is the identity exactly at the
undeformed point. -/
theorem vtx_three_eq_one_iff {q a b a' h : ℝ} (hq : 0 < q) (hb : b ≠ 0)
    (hh : h = q - q⁻¹) (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a)
    (hbb : b ^ 2 = a * a' + 1) (hq1 : q ^ 2 ≠ 1) :
    vtx q a b a' h ^ 3 = 1 ↔ h = 0 := by
  have hqinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq.ne'
  constructor
  · intro h3
    have := congrArg (fun M : Matrix (Fin 2) (Fin 2) ℝ => M 0 1) h3
    simp only at this
    rw [vtx_three hqinv hh ha ha' hbb hq1, vtx_entries] at this
    simp [Matrix.add_apply, Matrix.smul_apply] at this
    -- this : 2 * h ^ 2 + h ^ 4 = 0 ∨ q = 0 ∨ b = 0
    have hpos : 0 < 2 + h ^ 2 := by positivity
    rcases this with h0 | h0 | h0
    · have h2 : h ^ 2 * (2 + h ^ 2) = 0 := by linear_combination h0
      rcases mul_eq_zero.mp h2 with h2 | h2
      · exact pow_eq_zero_iff (by norm_num) |>.mp h2
      · exact absurd h2 hpos.ne'
    · exact absurd h0 hq.ne'
    · exact absurd h0 hb
  · intro h0
    rw [vtx_three hqinv hh ha ha' hbb hq1, h0]
    simp

/-- `α_k ≠ 0` for `k = 1..5` whenever `0 < h² ≤ 1/10` (`x = h²`): no vertex
power up to the fifth is symmetric on that whole interval. -/
theorem lin_ne_zero_of_small {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1 / 10) :
    (lin (-1 - x) 1).1 ≠ 0 ∧ (lin (-1 - x) 2).1 ≠ 0 ∧ (lin (-1 - x) 3).1 ≠ 0 ∧
      (lin (-1 - x) 4).1 ≠ 0 ∧ (lin (-1 - x) 5).1 ≠ 0 := by
  rw [lin_one, lin_two, lin_three, lin_four, lin_five]
  simp only
  have h2 : x * x ≤ x / 10 := by nlinarith
  refine ⟨one_ne_zero, ?_, ?_, ?_, ?_⟩
  · intro h; linarith
  · -- (1+x)² − 1 = x(2+x) > 0
    intro h; nlinarith
  · -- t(t² − 2) with t < 0 and t² < 2
    intro h
    have ht : (-1 - x) ^ 3 - 2 * (-1 - x) = (-1 - x) * ((1 + x) ^ 2 - 2) := by ring
    rw [ht] at h
    rcases mul_eq_zero.mp h with h | h
    · linarith
    · nlinarith
  · -- y² − 3y + 1 with y = (1+x)² ∈ [1, 1.21]
    intro h
    have hy : (-1 - x) ^ 4 - 3 * (-1 - x) ^ 2 + 1 = ((1 + x) ^ 2) ^ 2 - 3 * (1 + x) ^ 2 + 1 := by
      ring
    rw [hy] at h
    have hy1 : 1 ≤ (1 + x) ^ 2 := by nlinarith
    have hy2 : (1 + x) ^ 2 ≤ 121 / 100 := by nlinarith
    nlinarith

/-- The sign pattern `(−, −, +, −, −)` of `χ_(2,1)(V^k)`, `k = 1..5`, for every
`0 < h² ≤ 1/10` — the step-3 table as a theorem on an interval. -/
theorem chi_signs_of_small {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1 / 10) :
    -1 - x < 0 ∧ x ^ 2 + 2 * x - 1 < 0 ∧ 0 < 2 - 3 * x ^ 2 - x ^ 3 ∧
      x ^ 4 + 4 * x ^ 3 + 2 * x ^ 2 - 4 * x - 1 < 0 ∧
      -x ^ 5 - 5 * x ^ 4 - 5 * x ^ 3 + 5 * x ^ 2 + 5 * x - 1 < 0 := by
  have h2 : x ^ 2 ≤ x / 10 := by nlinarith
  have h3 : x ^ 3 ≤ x / 100 := by nlinarith [pow_nonneg hx.le 2]
  have h4 : x ^ 4 ≤ x / 1000 := by nlinarith [pow_nonneg hx.le 3]
  have h5 : x ^ 5 ≤ x / 10000 := by nlinarith [pow_nonneg hx.le 4]
  have p2 : 0 ≤ x ^ 2 := by positivity
  have p3 : 0 ≤ x ^ 3 := by positivity
  have p4 : 0 ≤ x ^ 4 := by positivity
  have p5 : 0 ≤ x ^ 5 := by positivity
  refine ⟨by linarith, by nlinarith, by nlinarith, by nlinarith, by nlinarith⟩

/-- `h² ≤ 1/10` for every `1 ≤ q ≤ 23/20` (the proton pin `q₀ ≈ 1.10998` is
inside; there `h² ≈ 0.0437`). -/
theorem h_sq_le_of_q_le {q : ℝ} (hq1 : 1 ≤ q) (hq2 : q ≤ 23 / 20) :
    (q - q⁻¹) ^ 2 ≤ 1 / 10 := by
  have hq0 : 0 < q := by linarith
  have hi1 : q⁻¹ ≤ 1 := inv_le_one_of_one_le₀ hq1
  have hi2 : 20 / 23 ≤ q⁻¹ := by
    rw [le_inv_comm₀ (by norm_num) hq0]
    calc q ≤ 23 / 20 := hq2
      _ = (20 / 23 : ℝ)⁻¹ := by norm_num
  have hh0 : 0 ≤ q - q⁻¹ := by linarith
  have hh1 : q - q⁻¹ ≤ 129 / 460 := by linarith
  nlinarith

/-- **Consequence for the literal reading**: for `1 < q ≤ 23/20` (`q₀`
included) and the actual Hoefsmit data, no vertex power `V^k` with `1 ≤ k ≤ 5`
is symmetric — so none is `Matrix.PosSemidef`, and the literal `SDPSelected`
admits no γγ word of `2 ≤ 2k ≤ 10` crossings. The corresponding claim for all
`k` is exactly `vtx_pow_isHermitian_iff_scalar`. -/
theorem hoefsmit_vtx_pow_not_isHermitian {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (k : ℕ) (hk1 : 1 ≤ k) (hk5 : k ≤ 5) :
    ¬ (vtx q (hoefsmitA q) (hoefsmitB q) (hoefsmitA' q) (hOf q) ^ k).IsHermitian := by
  have hq : 0 < q := by linarith
  have hqne : q ≠ 1 := hq1.ne'
  have hq0 : q ≠ 0 := hq.ne'
  have h4 := one_sub_pow_four_ne_zero hq hqne
  have hh : hOf q = q - q⁻¹ := rfl
  have ha : hoefsmitA q * (1 - q ^ 4) = hOf q := by
    unfold hoefsmitA; field_simp
  have ha' : hoefsmitA' q = -q ^ 4 * hoefsmitA q := by
    have h4m : q ^ 4 - 1 ≠ 0 := by intro h; apply h4; linarith
    unfold hoefsmitA' hoefsmitA
    rw [show (1 : ℝ) - (q ^ 4)⁻¹ = (q ^ 4 - 1) / q ^ 4 by field_simp]
    rw [div_div_eq_mul_div]
    field_simp
    ring
  have hbb := hoefsmitB_sq hq hqne
  have hb : hoefsmitB q ≠ 0 := (hoefsmitB_pos hq hqne).ne'
  have hq21 : q ^ 2 ≠ 1 := by
    intro h
    have : q = 1 := by nlinarith
    exact hqne this
  rw [vtx_pow_isHermitian_iff hq hb hh ha ha' hbb hq21 k]
  have hx : 0 < (hOf q) ^ 2 := by
    have : 0 < hOf q := by
      unfold hOf
      have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
      linarith
    positivity
  have hx1 : (hOf q) ^ 2 ≤ 1 / 10 := h_sq_le_of_q_le hq1.le hq2
  obtain ⟨n1, n2, n3, n4, n5⟩ := lin_ne_zero_of_small hx hx1
  interval_cases k
  · exact n1
  · exact n2
  · exact n3
  · exact n4
  · exact n5

end Real

end QOU.Mass.GammaGammaVertexOrder
