import BraidKnotOctonion.WhiteheadLemma1RootOfUnity
import QOU.Transcendental.BraidKnotOctonion.WhiteheadLinkScaffold

/-!
# vdV Lemma 1 for the Whitehead link: evaluation at the Kashaev point

Transcendental companion of `BraidKnotOctonion/WhiteheadLemma1RootOfUnity.lean`, which
states van der Veen's generic-`t` formula `vdvWhiteheadLinkJones` algebraically. This
file evaluates it at `s = e^{πi/N}` and proves the value is exactly
`whiteheadLinkKashaev N` (`vdvWhiteheadLinkJones_at_kashaev_point`), sorry-free.
Split out under the strangler pattern (bean `qou-dk7p`): the exponential lives here,
the algebra stays outside `QOU/Transcendental/`.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-/

namespace QOU.Knot.FigureEightVolume

open Real Complex

/-! ### Evaluation at `s = e^{πi/N}` -/

/-- Powers of `s = e^{πi/N}`. -/
theorem kpoint_zpow (N : ℕ) (m : ℤ) :
    Complex.exp (((π / N : ℝ) : ℂ) * I) ^ m = Complex.exp (((m * (π / N) : ℝ) : ℂ) * I) := by
  rw [← Complex.exp_int_mul]; congr 1; push_cast; ring

/-- `e^{i·2πz} = 1` for integer `z`, in the real-argument form used here. -/
theorem exp_two_pi_int (z : ℤ) (r : ℝ) (hr : r = 2 * π * z) :
    Complex.exp ((r : ℂ) * I) = 1 := by
  rw [hr, ← Complex.exp_int_mul_two_pi_mul_I z]; congr 1; push_cast; ring

theorem kpoint_beltFused {N : ℕ} (hN : 1 ≤ N) (n : ℕ) :
    vdvBeltFused (Complex.exp (((π / N : ℝ) : ℂ) * I)) N n = ((2 * n + 1 : ℕ) : ℂ) := by
  have hN0 : (N : ℝ) ≠ 0 := by positivity
  unfold vdvBeltFused
  rw [Finset.sum_congr rfl (g := fun _ => (1 : ℂ))]
  · simp
  intro j _
  rw [kpoint_zpow]
  apply exp_two_pi_int ((n : ℤ) - j)
  push_cast; field_simp

/-- One clasp numerator factor is `(2 sin(mπ/N))²`. -/
theorem kpoint_clasp_num {N : ℕ} (hN : 1 ≤ N) (m : ℤ) :
    (1 - Complex.exp (((π / N : ℝ) : ℂ) * I) ^ (2 * ((N : ℤ) - m))) *
        (1 - Complex.exp (((π / N : ℝ) : ℂ) * I) ^ (2 * m))
      = (((2 * Real.sin (m * (π / N))) ^ 2 : ℝ) : ℂ) := by
  have hN0 : (N : ℝ) ≠ 0 := by positivity
  set x : ℝ := m * (π / N)
  rw [kpoint_zpow, kpoint_zpow]
  have h1 : Complex.exp ((((2 * ((N : ℤ) - m) : ℤ) * (π / N) : ℝ) : ℂ) * I)
      = Complex.exp (-(2 * (x : ℂ)) * I) := by
    have hsplit : ((((2 * ((N : ℤ) - m) : ℤ) * (π / N) : ℝ) : ℂ) * I)
        = -(2 * (x : ℂ)) * I + (((2 * π * (1 : ℤ)) : ℝ) : ℂ) * I := by
      simp only [x]; push_cast
      have hNc : (N : ℂ) ≠ 0 := by exact_mod_cast hN0
      field_simp
      ring
    rw [hsplit, Complex.exp_add, exp_two_pi_int 1 _ rfl, mul_one]
  have h2 : Complex.exp ((((2 * m : ℤ) * (π / N) : ℝ) : ℂ) * I)
      = Complex.exp (2 * (x : ℂ) * I) := by
    congr 1; simp only [x]; push_cast; ring
  rw [h1, h2]
  push_cast
  rw [Complex.sin]
  have h3 : Complex.exp (-(x : ℂ) * I) * Complex.exp ((x : ℂ) * I) = 1 := by
    rw [← Complex.exp_add]; simp
  have e1 : Complex.exp (-(2 * (x : ℂ)) * I) = Complex.exp (-(x : ℂ) * I) ^ 2 := by
    rw [← Complex.exp_nat_mul]; ring_nf
  have e2 : Complex.exp (2 * (x : ℂ) * I) = Complex.exp ((x : ℂ) * I) ^ 2 := by
    rw [← Complex.exp_nat_mul]; ring_nf
  rw [e1, e2]
  set a := Complex.exp (-(x : ℂ) * I)
  set b := Complex.exp ((x : ℂ) * I)
  linear_combination (a * b - 1) * h3 + (-(a - b) ^ 2) * Complex.I_sq

/-- One clasp denominator factor: `1/(1 − e^{2iφ}) = i·e^{−iφ}/(2 sin φ)`. -/
theorem kpoint_clasp_den {N : ℕ} (m : ℤ) (hsin : Real.sin (m * (π / N)) ≠ 0) :
    1 / (1 - Complex.exp (((π / N : ℝ) : ℂ) * I) ^ (2 * m))
      = (I * Complex.exp (-(((m * (π / N) : ℝ) : ℂ)) * I)) / (((2 * Real.sin (m * (π / N))) : ℝ) : ℂ) := by
  set x : ℝ := m * (π / N)
  rw [kpoint_zpow]
  have h2 : Complex.exp ((((2 * m : ℤ) * (π / N) : ℝ) : ℂ) * I)
      = Complex.exp ((x : ℂ) * I) ^ 2 := by
    rw [← Complex.exp_nat_mul]; congr 1; simp only [x]; push_cast; ring
  rw [h2]
  have h3 : Complex.exp (-(x : ℂ) * I) * Complex.exp ((x : ℂ) * I) = 1 := by
    rw [← Complex.exp_add]; simp
  have hsC : Complex.sin (x : ℂ) ≠ 0 := by
    rw [← Complex.ofReal_sin]; exact_mod_cast hsin
  set a := Complex.exp (-(x : ℂ) * I)
  set b := Complex.exp ((x : ℂ) * I)
  have hb : b ≠ 0 := Complex.exp_ne_zero _
  have hsin_def : Complex.sin (x : ℂ) = (a - b) * I / 2 := by
    rw [Complex.sin]
  have hden : (1 : ℂ) - b ^ 2 ≠ 0 := by
    intro h
    apply hsC
    rw [hsin_def]
    have ha : a = b⁻¹ := eq_inv_of_mul_eq_one_left h3
    rw [ha]
    field_simp
    linear_combination I * h
  have hc : ((((2 * Real.sin x) : ℝ)) : ℂ) = 2 * Complex.sin (x : ℂ) := by push_cast; rfl
  rw [hc, hsin_def]
  have ha : a = b⁻¹ := eq_inv_of_mul_eq_one_left h3
  have hab : b⁻¹ - b ≠ 0 := by
    intro h; apply hden; field_simp at h; linear_combination h
  rw [ha]
  field_simp


/-- `i = e^{iπ/2}`. -/
theorem I_eq_exp_half_pi : I = Complex.exp (((π / 2 : ℝ) : ℂ) * I) := by
  rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin, Real.cos_pi_div_two,
    Real.sin_pi_div_two]
  simp

theorem sum_range_succ_cast (n : ℕ) :
    ∑ j ∈ Finset.range n, (((j : ℤ) + 1 : ℤ) : ℝ) = (n : ℝ) * (n + 1) / 2 := by
  induction n with
  | zero => simp
  | succ n ih => rw [Finset.sum_range_succ, ih]; push_cast; ring

/-- The `k`-independent phase of the clasp product is vdV's `χ_{N,n}^{-1}`. -/
theorem kpoint_phase_prod {N : ℕ} (hN : 1 ≤ N) (n : ℕ) :
    ∏ j ∈ Finset.range n, (I * Complex.exp (-((((((j : ℤ) + 1 : ℤ) : ℝ) * (π / N) : ℝ) : ℂ)) * I))
      = whiteheadLinkPhase N n := by
  have hN0 : (N : ℝ) ≠ 0 := by positivity
  rw [Finset.prod_mul_distrib, Finset.prod_const, Finset.card_range, ← Complex.exp_sum]
  have hI : I ^ n = Complex.exp ((n : ℂ) * ((((π / 2 : ℝ)) : ℂ) * I)) := by
    rw [Complex.exp_nat_mul]
    conv_lhs => rw [I_eq_exp_half_pi]
  have hs : ∑ j ∈ Finset.range n, (-((((((j : ℤ) + 1 : ℤ) : ℝ) * (π / N) : ℝ) : ℂ)) * I)
      = -((((n : ℝ) * (n + 1) / 2 * (π / N) : ℝ) : ℂ)) * I := by
    rw [← sum_range_succ_cast, Finset.sum_mul, Complex.ofReal_sum]
    simp only [neg_mul, Finset.sum_neg_distrib, Finset.sum_mul]
  rw [hI, hs, ← Complex.exp_add, whiteheadLinkPhase]
  congr 1
  push_cast
  have hNc : (N : ℂ) ≠ 0 := by exact_mod_cast hN0
  field_simp
  ring

/-- The framing prefactor `s^{(N²−1)+N(N−1)}` is vdV's `φ_N = e^{(N−1)πi/N}`. -/
theorem kpoint_prefactor {N : ℕ} (hN : 1 ≤ N) :
    Complex.exp (((π / N : ℝ) : ℂ) * I) ^ (((N : ℤ) ^ 2 - 1) + (N : ℤ) * ((N : ℤ) - 1))
      = Complex.exp ((((((N : ℝ) - 1) * π / N) : ℝ) : ℂ) * I) := by
  have hN0 : (N : ℝ) ≠ 0 := by positivity
  rw [kpoint_zpow]
  have hsplit : (((((((N : ℤ) ^ 2 - 1) + (N : ℤ) * ((N : ℤ) - 1) : ℤ) : ℝ) * (π / N) : ℝ) : ℂ) * I)
      = (((((N : ℝ) - 1) * π / N) : ℝ) : ℂ) * I
        + (((2 * π * (((N : ℤ) - 1 : ℤ) : ℝ)) : ℝ) : ℂ) * I := by
    push_cast
    have hNc : (N : ℂ) ≠ 0 := by exact_mod_cast hN0
    field_simp
    ring
  rw [hsplit, Complex.exp_add, exp_two_pi_int ((N : ℤ) - 1) _ rfl, mul_one]

/-- One full clasp factor at the Kashaev point. -/
theorem kpoint_clasp_factor {N n k j : ℕ} (hN : 1 ≤ N) (hjn : j < n) (hn : n < N) :
    (1 - Complex.exp (((π / N : ℝ) : ℂ) * I) ^ (2 * ((N : ℤ) - ((j : ℤ) + 1) - k))) *
        (1 - Complex.exp (((π / N : ℝ) : ℂ) * I) ^ (2 * ((j : ℤ) + 1 + k)))
        / (1 - Complex.exp (((π / N : ℝ) : ℂ) * I) ^ (2 * ((j : ℤ) + 1)))
      = (((2 * Real.sin ((((k + 1 + j : ℕ) : ℝ)) * (π / N))) ^ 2 : ℝ) : ℂ)
        / (((2 * Real.sin ((((1 + j : ℕ) : ℝ)) * (π / N))) : ℝ) : ℂ)
        * (I * Complex.exp (-((((((j : ℤ) + 1 : ℤ) : ℝ) * (π / N) : ℝ) : ℂ)) * I)) := by
  have hsin : Real.sin ((((j : ℤ) + 1 : ℤ) : ℝ) * (π / N)) ≠ 0 := by
    have := sin_grid_pos (N := N) (j := j + 1) (by omega) (by omega)
    push_cast at this ⊢; exact this.ne'
  have e1 : 2 * ((N : ℤ) - ((j : ℤ) + 1) - k) = 2 * ((N : ℤ) - ((j : ℤ) + 1 + k)) := by ring
  rw [e1, div_eq_mul_one_div, kpoint_clasp_num hN, kpoint_clasp_den _ hsin]
  have c1 : (((j : ℤ) + 1 + k : ℤ) : ℝ) = (((k + 1 + j : ℕ) : ℝ)) := by push_cast; ring
  have c2 : ((((j : ℤ) + 1 : ℤ)) : ℝ) = (((1 + j : ℕ) : ℝ)) := by push_cast; ring
  rw [c1]
  rw [show (2 * Real.sin ((((j : ℤ) + 1 : ℤ) : ℝ) * (π / N)) : ℝ)
      = 2 * Real.sin ((((1 + j : ℕ) : ℝ)) * (π / N)) by rw [c2]]
  ring

/-- The clasp at the Kashaev point: `C(n, e^{2πi/N}) = φ_N · χ_{N,n}^{-1} · Σ_k S_{n,k}`. -/
theorem kpoint_clasp {N n : ℕ} (hN : 1 ≤ N) (hn : n < N) :
    vdvClasp (Complex.exp (((π / N : ℝ) : ℂ) * I)) N n
      = Complex.exp ((((((N : ℝ) - 1) * π / N) : ℝ) : ℂ) * I) * whiteheadLinkPhase N n
        * (((∑ k ∈ Finset.range (N - n), whiteheadTerm N n k : ℝ)) : ℂ) := by
  have hN0 : (N : ℝ) ≠ 0 := by positivity
  unfold vdvClasp
  rw [kpoint_prefactor hN, mul_assoc]
  congr 1
  rw [Complex.ofReal_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  have hone : Complex.exp (((π / N : ℝ) : ℂ) * I) ^ (-(2 * (N : ℤ) * ((n : ℤ) + k))) = 1 := by
    rw [kpoint_zpow]; apply exp_two_pi_int (-((n : ℤ) + k)); push_cast; field_simp
  rw [hone, one_mul, Finset.prod_congr rfl fun j hj =>
    kpoint_clasp_factor (k := k) hN (Finset.mem_range.mp hj) hn]
  rw [Finset.prod_mul_distrib, Finset.prod_div_distrib, kpoint_phase_prod hN]
  unfold whiteheadTerm whiteheadNum whiteheadDen
  have hnum : ∏ j ∈ Finset.Icc (k + 1) (k + n), (2 * Real.sin ((j : ℝ) * (π / N))) ^ 2
      = ∏ j ∈ Finset.range n, (2 * Real.sin ((((k + 1 + j : ℕ) : ℝ)) * (π / N))) ^ 2 := by
    have hI : Finset.Icc (k + 1) (k + n) = Finset.Ico (k + 1) (k + n + 1) := by
      ext x; simp only [Finset.mem_Icc, Finset.mem_Ico]; omega
    rw [hI, Finset.prod_Ico_eq_prod_range, show k + n + 1 - (k + 1) = n by omega]
  have hden : ∏ j ∈ Finset.Icc 1 n, (2 * Real.sin ((j : ℝ) * (π / N)))
      = ∏ j ∈ Finset.range n, (2 * Real.sin ((((1 + j : ℕ) : ℝ)) * (π / N))) := by
    have hI : Finset.Icc 1 n = Finset.Ico 1 (n + 1) := by
      ext x; simp only [Finset.mem_Icc, Finset.mem_Ico]; omega
    rw [hI, Finset.prod_Ico_eq_prod_range, show n + 1 - 1 = n by omega]
  rw [hnum, hden]
  push_cast
  ring

/-- **vdV Lemma 1, root-of-unity layer (derived).**  The generic-`t` tangle formula
    for the Whitehead link `W_{0,1,1,0}`, evaluated at `t = e^{2πi/N}`
    (`s = e^{πi/N}`), equals the closed form `whiteheadLinkKashaev N`. -/
theorem vdvWhiteheadLinkJones_at_kashaev_point {N : ℕ} (hN : 1 ≤ N) :
    vdvWhiteheadLinkJones (Complex.exp (((π / N : ℝ) : ℂ) * I)) N = whiteheadLinkKashaev N := by
  unfold vdvWhiteheadLinkJones whiteheadLinkKashaev
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun n hn => ?_
  rw [kpoint_beltFused hN, kpoint_clasp hN (Finset.mem_range.mp hn)]
  have e : ((((N : ℝ) - 1) * π / N : ℝ) : ℂ) = ((((N : ℝ) - 1) * π / N : ℝ) : ℂ) := rfl
  ring

end QOU.Knot.FigureEightVolume
