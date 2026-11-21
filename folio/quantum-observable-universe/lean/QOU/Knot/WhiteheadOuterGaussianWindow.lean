import QOU.Knot.WhiteheadLemma4Reduction
import QOU.MathlibExt.GaussianThetaBound

/-!
# Whitehead outer Gaussian model from the 2D (vdV Lemma 2a/2b) model (bean qou-kc8h)

Proves, sorry-free, `WhiteheadOuterGaussianModel` FROM the strictly smaller carrier
`WhiteheadInnerGaussianModel` (vdV Lemma 2a/2b, signed form, in `(2n+1)`-weighted
`L¹`): `Σ_n (2n+1) Σ_k |S_{n,k} − B_N E(n,k)| ≤ B_N N²/8` eventually, with
`E = exp(−(π/N)(x² + 2xy + 2y²))` (`whitehead2DGauss_eq`).  Everything else —
completing the square in `k` (centre `(N−n)/2`, the midpoint of the `k`-range),
the theta-function evaluation of the `k`-sum, the lattice points outside the
range, and the `(2n+1) → N` swap — is proved here, with `A_N = B_N N √(N/2)`.

The 2D carrier is NOT discharged: no instance is provided.  Numerically
(`mpmath`, `B_N = ΣS/ΣE`, best of `±3 %`) its ratio
`Σ(2n+1)Σ_k|S − BE|/(BN²)` is `0.346, 0.246, 0.171, 0.120, 0.085` at
`N = 20, 40, 80, 160, 320` (`∝ N^{-1/2}`), so the tolerance `1/8` holds from
`N ≈ 160` on.  The open content is vdV Lemma 2a (window, quadratic expansion of
`log S_{n,k}` about `(N/2, N/4)`) + Lemma 2b (tails), bean qou-vy77.
-- Ref: [manuscript] library/arxiv-math-0611181v2/0611181v2.pdf, Lemma 2a/2b
-/

namespace QOU.MathlibExt

open Real

theorem summable_gaussian_shift (a c : ℝ) (ha : 0 < a) :
    Summable (fun n : ℤ => Real.exp (-a * ((n : ℝ) - c) ^ 2)) :=
  (hasSum_gaussian_theta_real a c ha).summable

/-- With `q = e^{−π²/a} ≤ 1/3`, the full lattice sum is within `3q√(π/a)` of `√(π/a)`. -/
theorem abs_tsum_gaussian_sub_sqrt_le_three {a c : ℝ} (ha : 0 < a)
    (hq : Real.exp (-(π ^ 2 / a)) ≤ 1 / 3) :
    |(∑' n : ℤ, Real.exp (-a * ((n : ℝ) - c) ^ 2)) - Real.sqrt (π / a)|
      ≤ Real.sqrt (π / a) * (3 * Real.exp (-(π ^ 2 / a))) := by
  refine le_trans (abs_tsum_gaussian_sub_sqrt_le a c ha) ?_
  refine mul_le_mul_of_nonneg_left ?_ (Real.sqrt_nonneg _)
  set q := Real.exp (-(π ^ 2 / a))
  have hq0 : 0 ≤ q := (Real.exp_pos _).le
  rw [div_le_iff₀ (by linarith)]
  nlinarith

theorem tsum_gaussian_le_two {a c : ℝ} (ha : 0 < a)
    (hq : Real.exp (-(π ^ 2 / a)) ≤ 1 / 3) :
    (∑' n : ℤ, Real.exp (-a * ((n : ℝ) - c) ^ 2)) ≤ 2 * Real.sqrt (π / a) := by
  have h := abs_tsum_gaussian_sub_sqrt_le_three (c := c) ha hq
  have hs := Real.sqrt_nonneg (π / a)
  have hq0 : 0 ≤ Real.exp (-(π ^ 2 / a)) := (Real.exp_pos _).le
  have := (abs_le.mp h).2
  nlinarith

theorem finset_sum_gaussian_le_two {a c : ℝ} (ha : 0 < a)
    (hq : Real.exp (-(π ^ 2 / a)) ≤ 1 / 3) (s : Finset ℤ) :
    ∑ n ∈ s, Real.exp (-a * ((n : ℝ) - c) ^ 2) ≤ 2 * Real.sqrt (π / a) :=
  le_trans ((summable_gaussian_shift a c ha).sum_le_tsum s
    (fun _ _ => (Real.exp_pos _).le)) (tsum_gaussian_le_two ha hq)

theorem range_sum_gaussian_le_two {a c : ℝ} (ha : 0 < a)
    (hq : Real.exp (-(π ^ 2 / a)) ≤ 1 / 3) (M : ℕ) :
    ∑ n ∈ Finset.range M, Real.exp (-a * ((n : ℝ) - c) ^ 2) ≤ 2 * Real.sqrt (π / a) := by
  have h := finset_sum_gaussian_le_two (c := c) ha hq
    ((Finset.range M).map ⟨((↑) : ℕ → ℤ), Nat.cast_injective⟩)
  rw [Finset.sum_map] at h
  simpa using h

/-- Lattice points outside `[0, L)` are at distance `≥ L/2` from the centre `L/2`,
so the full sum exceeds the window sum by at most `e^{−a(L/2)²/2}` times the
half-rate lattice sum. -/
theorem tsum_gaussian_sub_range_le {a : ℝ} (ha : 0 < a)
    (hq : Real.exp (-(π ^ 2 / (a / 2))) ≤ 1 / 3) (L : ℕ) :
    (∑' n : ℤ, Real.exp (-a * ((n : ℝ) - (L : ℝ) / 2) ^ 2))
        - ∑ n ∈ Finset.range L, Real.exp (-a * ((n : ℝ) - (L : ℝ) / 2) ^ 2)
      ≤ Real.exp (-(a * ((L : ℝ) / 2) ^ 2 / 2)) * (2 * Real.sqrt (π / (a / 2))) := by
  set c : ℝ := (L : ℝ) / 2 with hc
  set f : ℤ → ℝ := fun n => Real.exp (-a * ((n : ℝ) - c) ^ 2) with hf
  set g : ℤ → ℝ := fun n => Real.exp (-(a / 2) * ((n : ℝ) - c) ^ 2) with hg
  have ha2 : 0 < a / 2 := by linarith
  have hfs : Summable f := summable_gaussian_shift a c ha
  have hgs : Summable g := summable_gaussian_shift (a / 2) c ha2
  set F : Finset ℤ := (Finset.range L).map ⟨((↑) : ℕ → ℤ), Nat.cast_injective⟩ with hF
  have hsumF : ∑ n ∈ Finset.range L, Real.exp (-a * ((n : ℝ) - c) ^ 2) = ∑ n ∈ F, f n := by
    rw [hF, Finset.sum_map]; simp [hf]
  rw [hsumF, ← hfs.sum_add_tsum_compl (s := F), add_sub_cancel_left]
  have hout : ∀ x : ↑((F : Set ℤ)ᶜ), f x ≤ Real.exp (-(a * c ^ 2 / 2)) * g x := by
    rintro ⟨n, hn⟩
    have hn' : n ∉ F := hn
    have hfar : c ^ 2 ≤ ((n : ℝ) - c) ^ 2 := by
      have hc0 : 0 ≤ c := by rw [hc]; positivity
      rcases lt_or_ge n 0 with h0 | h0
      · have : (n : ℝ) ≤ -1 := by exact_mod_cast (show n ≤ -1 by omega)
        nlinarith
      · have hL : (L : ℤ) ≤ n := by
          by_contra hlt
          push_neg at hlt
          apply hn'
          rw [hF, Finset.mem_map]
          refine ⟨n.toNat, ?_, ?_⟩
          · rw [Finset.mem_range]; omega
          · simp [Int.toNat_of_nonneg h0]
        have : (L : ℝ) ≤ (n : ℝ) := by exact_mod_cast hL
        nlinarith
    simp only [hf, hg]
    rw [← Real.exp_add]
    exact Real.exp_le_exp.mpr (by nlinarith)
  calc ∑' x : ↑((F : Set ℤ)ᶜ), f x
      ≤ ∑' x : ↑((F : Set ℤ)ᶜ), Real.exp (-(a * c ^ 2 / 2)) * g x :=
        Summable.tsum_le_tsum hout (hfs.subtype _) ((hgs.subtype _).mul_left _)
    _ = Real.exp (-(a * c ^ 2 / 2)) * ∑' x : ↑((F : Set ℤ)ᶜ), g x := tsum_mul_left
    _ ≤ Real.exp (-(a * c ^ 2 / 2)) * (2 * Real.sqrt (π / (a / 2))) := by
        refine mul_le_mul_of_nonneg_left ?_ (Real.exp_pos _).le
        refine le_trans (Summable.tsum_subtype_le g _ (fun _ => (Real.exp_pos _).le) hgs) ?_
        exact tsum_gaussian_le_two ha2 hq

end QOU.MathlibExt

namespace QOU.MathlibExt

open Real

/-- `|x| e^{−b x²} ≤ K e^{−(b/2) x²}` whenever `K² b ≥ 2`. -/
theorem abs_mul_exp_neg_sq_le {b K x : ℝ} (hb : 0 < b) (hK : 0 < K) (hKb : 2 ≤ K ^ 2 * b) :
    |x| * Real.exp (-b * x ^ 2) ≤ K * Real.exp (-(b / 2) * x ^ 2) := by
  set u := |x| / K with hu
  have hu0 : 0 ≤ u := by positivity
  have hux : |x| = K * u := by rw [hu]; field_simp
  have hu2 : u ^ 2 ≤ b / 2 * x ^ 2 := by
    have hx2 : |x| ^ 2 = x ^ 2 := sq_abs x
    have : K ^ 2 * u ^ 2 = x ^ 2 := by rw [← hx2, hux]; ring
    nlinarith [sq_nonneg u]
  have hle : u ≤ Real.exp (b / 2 * x ^ 2) := by
    have h1 : u ≤ u ^ 2 + 1 := by nlinarith [sq_nonneg (u - 1)]
    have h2 := Real.add_one_le_exp (u ^ 2)
    have h3 : Real.exp (u ^ 2) ≤ Real.exp (b / 2 * x ^ 2) := Real.exp_le_exp.mpr hu2
    linarith
  have hsplit : Real.exp (-b * x ^ 2) = (Real.exp (b / 2 * x ^ 2))⁻¹ * Real.exp (-(b / 2) * x ^ 2) := by
    rw [← Real.exp_neg, ← Real.exp_add]; congr 1; ring
  rw [hux, hsplit]
  have hepos := Real.exp_pos (b / 2 * x ^ 2)
  have : u * (Real.exp (b / 2 * x ^ 2))⁻¹ ≤ 1 := by
    rw [mul_inv_le_iff₀ hepos]; linarith
  calc K * u * ((Real.exp (b / 2 * x ^ 2))⁻¹ * Real.exp (-(b / 2) * x ^ 2))
      = K * (u * (Real.exp (b / 2 * x ^ 2))⁻¹) * Real.exp (-(b / 2) * x ^ 2) := by ring
    _ ≤ K * 1 * Real.exp (-(b / 2) * x ^ 2) := by
        gcongr
    _ = K * Real.exp (-(b / 2) * x ^ 2) := by ring

end QOU.MathlibExt

namespace QOU.Knot.FigureEightVolume

open Real QOU.MathlibExt

/-- The inner (`k`-direction) Gaussian factor, centred at the midpoint `(N−n)/2`
of the `k`-range `[0, N−n)`. -/
noncomputable def whiteheadInnerGauss (N n k : ℕ) : ℝ :=
  Real.exp (-(2 * π / N) * ((k : ℝ) - ((N - n : ℕ) : ℝ) / 2) ^ 2)

/-- The two-dimensional Gaussian model of `S_{n,k}` (vdV Lemma 2a, SIGNED form). -/
noncomputable def whitehead2DGauss (N n k : ℕ) : ℝ :=
  whiteheadGaussianProfile N n * whiteheadInnerGauss N n k

/-- The model is exactly van der Veen's signed quadratic form
`exp(−(π/N)(x² + 2xy + 2y²))`, `x = n − N/2`, `y = k − N/4` (signed offsets). -/
theorem whitehead2DGauss_eq {N n : ℕ} (hN : 0 < N) (hn : n ≤ N) (k : ℕ) :
    whitehead2DGauss N n k
      = Real.exp (-(π / N) * (((n : ℝ) - N / 2) ^ 2
          + 2 * ((n : ℝ) - N / 2) * ((k : ℝ) - N / 4) + 2 * ((k : ℝ) - N / 4) ^ 2)) := by
  have hN' : (N : ℝ) ≠ 0 := by exact_mod_cast hN.ne'
  unfold whitehead2DGauss whiteheadGaussianProfile whiteheadInnerGauss
  rw [← Real.exp_add, Nat.cast_sub hn]
  congr 1
  field_simp
  ring

/-- The Gaussian profile in the `exp(−b (n−c)²)` normal form. -/
theorem whiteheadGaussianProfile_eq (N n : ℕ) :
    whiteheadGaussianProfile N n
      = Real.exp (-(π / (2 * N)) * ((n : ℝ) - (N : ℝ) / 2) ^ 2) := by
  unfold whiteheadGaussianProfile
  congr 1
  ring

/-- **Primary carrier (§3b-tax): vdV Lemma 2a/2b (signed form), summed in `L¹`.**
    The positive two-dimensional terms `S_{n,k}` are, in the `(2n+1)`-weighted
    `L¹` norm over the grid, within `B_N N²/8` of the signed Gaussian
    `B_N exp(−(π/N)(x² + 2xy + 2y²))` (total model mass `≈ B_N N²`).  Numerically
    (`mpmath`, `B_N := ΣS/ΣE`) the ratio `Σ(2n+1)Σ_k|S − B E| / (B N²)` is
    `0.346, 0.246, 0.171, 0.120` at `N = 20, 40, 80, 160` (decaying like
    `N^{-1/2}`); the truth is `o(1)`, so the fixed tolerance `1/8` holds
    eventually.  No instance is provided. -/
class WhiteheadInnerGaussianModel : Prop where
  model : ∃ B : ℕ → ℝ, ∀ᶠ N in Filter.atTop, 0 < B N ∧
    ∑ n ∈ Finset.range N, ((2 * n + 1 : ℕ) : ℝ) *
        ∑ k ∈ Finset.range (N - n), |whiteheadTerm N n k - B N * whitehead2DGauss N n k|
      ≤ B N * (N : ℝ) ^ 2 / 8

theorem exp_neg_le_third {x : ℝ} (hx : 3 / 2 ≤ x) : Real.exp (-x) ≤ 1 / 3 := by
  have h1 := Real.add_one_le_exp (x / 2)
  have h2 : Real.exp x = Real.exp (x / 2) ^ 2 := by
    rw [sq, ← Real.exp_add]; congr 1; ring
  have h3 : 3 ≤ Real.exp x := by rw [h2]; nlinarith
  rw [Real.exp_neg, inv_eq_one_div, div_le_div_iff₀ (Real.exp_pos x) (by norm_num)]
  linarith

/-- Upper bound on the inner `k`-sum: `T_n ≤ 2√(N/2)`. -/
theorem whiteheadInnerSum_le {N : ℕ} (hN : 1 ≤ N) (n : ℕ) :
    ∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k ≤ 2 * Real.sqrt ((N : ℝ) / 2) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hN1 : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have ha : 0 < 2 * π / N := by positivity
  have hpa : π / (2 * π / N) = (N : ℝ) / 2 := by field_simp
  have hq : Real.exp (-(π ^ 2 / (2 * π / N))) ≤ 1 / 3 := by
    apply exp_neg_le_third
    rw [show π ^ 2 / (2 * π / N) = π * N / 2 by field_simp]
    nlinarith [Real.pi_gt_three]
  have h := range_sum_gaussian_le_two (c := ((N - n : ℕ) : ℝ) / 2) ha hq (N - n)
  rw [hpa] at h
  simpa [whiteheadInnerGauss] using h

/-- Two-sided bound on the inner `k`-sum: `|T_n − √(N/2)| ≤ 3√(N/2)e^{−πN/2}
+ 2√N e^{−π(N−n)²/(4N)}` (theta-function error + lattice points outside `[0,N−n)`). -/
theorem abs_whiteheadInnerSum_sub_le {N : ℕ} (hN : 1 ≤ N) (n : ℕ) :
    |∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k - Real.sqrt ((N : ℝ) / 2)|
      ≤ Real.sqrt ((N : ℝ) / 2) * (3 * Real.exp (-(π * N / 2)))
        + Real.exp (-(π * ((N - n : ℕ) : ℝ) ^ 2 / (4 * N))) * (2 * Real.sqrt N) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have ha : 0 < 2 * π / N := by positivity
  have hpa : π / (2 * π / N) = (N : ℝ) / 2 := by field_simp
  have hpa2 : π / (2 * π / N / 2) = (N : ℝ) := by field_simp
  have hq : Real.exp (-(π ^ 2 / (2 * π / N))) ≤ 1 / 3 := by
    apply exp_neg_le_third
    rw [show π ^ 2 / (2 * π / N) = π * N / 2 by field_simp]
    have : (1 : ℝ) ≤ N := by exact_mod_cast hN
    nlinarith [Real.pi_gt_three]
  have hq2 : Real.exp (-(π ^ 2 / (2 * π / N / 2))) ≤ 1 / 3 := by
    apply exp_neg_le_third
    rw [show π ^ 2 / (2 * π / N / 2) = π * N by field_simp]
    have : (1 : ℝ) ≤ N := by exact_mod_cast hN
    nlinarith [Real.pi_gt_three]
  set L := N - n with hL
  set c : ℝ := (L : ℝ) / 2
  set T := ∑ k ∈ Finset.range L, whiteheadInnerGauss N n k with hT
  set Θ := ∑' m : ℤ, Real.exp (-(2 * π / N) * ((m : ℝ) - c) ^ 2) with hΘ
  have hT' : T = ∑ k ∈ Finset.range L, Real.exp (-(2 * π / N) * ((k : ℝ) - c) ^ 2) := by
    simp [hT, whiteheadInnerGauss, c, hL]
  have h1 := abs_tsum_gaussian_sub_sqrt_le_three (c := c) ha hq
  rw [hpa, show π ^ 2 / (2 * π / N) = π * N / 2 by field_simp] at h1
  have h2 := tsum_gaussian_sub_range_le ha hq2 L
  rw [hpa2] at h2
  have hexp : -(2 * π / N * ((L : ℝ) / 2) ^ 2 / 2) = -(π * (L : ℝ) ^ 2 / (4 * N)) := by
    field_simp; ring
  rw [hexp] at h2
  have h3 : T ≤ Θ := by
    rw [hT']
    have := (summable_gaussian_shift (2 * π / N) c ha).sum_le_tsum
      ((Finset.range L).map ⟨((↑) : ℕ → ℤ), Nat.cast_injective⟩)
      (fun _ _ => (Real.exp_pos _).le)
    rw [Finset.sum_map] at this
    rw [hΘ]
    simpa using this
  rw [← hT'] at h2
  rw [abs_le] at h1 ⊢
  constructor <;> nlinarith [Real.exp_pos (-(π * (L : ℝ) ^ 2 / (4 * N))),
    Real.sqrt_nonneg (N : ℝ)]

theorem sum_whiteheadGaussianProfile_le {N : ℕ} (hN : 1 ≤ N) :
    ∑ n ∈ Finset.range N, whiteheadGaussianProfile N n ≤ 2 * Real.sqrt (2 * N) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hN1 : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have hb : 0 < π / (2 * N) := by positivity
  have hq : Real.exp (-(π ^ 2 / (π / (2 * N)))) ≤ 1 / 3 := by
    apply exp_neg_le_third
    rw [show π ^ 2 / (π / (2 * N)) = 2 * π * N by field_simp]
    nlinarith [Real.pi_gt_three]
  have h := range_sum_gaussian_le_two (c := (N : ℝ) / 2) hb hq N
  rw [show π / (π / (2 * N)) = 2 * (N : ℝ) by field_simp] at h
  simpa [whiteheadGaussianProfile_eq] using h

theorem sum_abs_mul_whiteheadGaussianProfile_le {N : ℕ} (hN : 1 ≤ N) :
    ∑ n ∈ Finset.range N, |(n : ℝ) - N / 2| * whiteheadGaussianProfile N n ≤ 8 * N := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hN1 : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have hb : 0 < π / (2 * N) := by positivity
  have hb2 : 0 < π / (2 * N) / 2 := by positivity
  have hq : Real.exp (-(π ^ 2 / (π / (2 * N) / 2))) ≤ 1 / 3 := by
    apply exp_neg_le_third
    rw [show π ^ 2 / (π / (2 * N) / 2) = 4 * π * N by field_simp; ring]
    nlinarith [Real.pi_gt_three]
  have hK : (0 : ℝ) < 2 * Real.sqrt N := by positivity
  have hKb : 2 ≤ (2 * Real.sqrt N) ^ 2 * (π / (2 * N)) := by
    rw [mul_pow, Real.sq_sqrt hNpos.le]
    rw [show (2 : ℝ) ^ 2 * N * (π / (2 * N)) = 2 * π by field_simp]
    nlinarith [Real.pi_gt_three]
  have hterm : ∀ n ∈ Finset.range N, |(n : ℝ) - N / 2| * whiteheadGaussianProfile N n
      ≤ 2 * Real.sqrt N * Real.exp (-(π / (2 * N) / 2) * ((n : ℝ) - N / 2) ^ 2) := by
    intro n _
    rw [whiteheadGaussianProfile_eq]
    exact abs_mul_exp_neg_sq_le hb hK hKb
  refine le_trans (Finset.sum_le_sum hterm) ?_
  rw [← Finset.mul_sum]
  have h := range_sum_gaussian_le_two (c := (N : ℝ) / 2) hb2 hq N
  rw [show π / (π / (2 * N) / 2) = 4 * (N : ℝ) by field_simp; ring] at h
  have h4 : Real.sqrt (4 * (N : ℝ)) = 2 * Real.sqrt N := by
    rw [Real.sqrt_mul (by norm_num), show (4 : ℝ) = 2 ^ 2 by norm_num,
      Real.sqrt_sq (by norm_num)]
  rw [h4] at h
  have hs := Real.sq_sqrt hNpos.le
  have hs0 := Real.sqrt_nonneg (N : ℝ)
  calc 2 * Real.sqrt N * ∑ n ∈ Finset.range N,
        Real.exp (-(π / (2 * N) / 2) * ((n : ℝ) - N / 2) ^ 2)
      ≤ 2 * Real.sqrt N * (2 * (2 * Real.sqrt N)) := by gcongr
    _ = 8 * N := by nlinarith

theorem whiteheadGaussianProfile_mul_tail_le {N n : ℕ} (hN : 1 ≤ N) (hn : n ≤ N) :
    whiteheadGaussianProfile N n * Real.exp (-(π * ((N - n : ℕ) : ℝ) ^ 2 / (4 * N)))
      ≤ Real.exp (-(π * N / 24)) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  unfold whiteheadGaussianProfile
  rw [← Real.exp_add, Nat.cast_sub hn]
  apply Real.exp_le_exp.mpr
  have key : π * ((n : ℝ) - N / 2) ^ 2 / (2 * N) + π * ((N : ℝ) - n) ^ 2 / (4 * N)
      - π * N / 24 = π * (3 / 4) * ((n : ℝ) - 2 * N / 3) ^ 2 / N := by
    field_simp; ring
  have : 0 ≤ π * (3 / 4) * ((n : ℝ) - 2 * N / 3) ^ 2 / N := by
    have := Real.pi_pos; positivity
  linarith

/-- The Gaussian bookkeeping error: the `k`-sum of the 2D model and the
`(2n+1) → N` swap, measured against the 1D profile. -/
noncomputable def whiteheadGaussErr (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.range N, whiteheadGaussianProfile N n *
    |((2 * n + 1 : ℕ) : ℝ) * (∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k)
      - N * Real.sqrt ((N : ℝ) / 2)|

theorem whiteheadGaussErr_le {N : ℕ} (hN : 1 ≤ N) :
    whiteheadGaussErr N ≤ 32 * N * Real.sqrt N + 4 * N
      + 6 * (N : ℝ) ^ 2 * Real.exp (-(π * N / 2))
      + 2 * (N : ℝ) ^ 2 * Real.sqrt N * Real.exp (-(π * N / 24)) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  set s := Real.sqrt ((N : ℝ) / 2) with hs
  set r := Real.sqrt (N : ℝ) with hr
  have hs0 : 0 ≤ s := Real.sqrt_nonneg _
  have hr0 : 0 ≤ r := Real.sqrt_nonneg _
  have hsr : s ≤ r := Real.sqrt_le_sqrt (by linarith)
  have hs2N : s * Real.sqrt (2 * N) = N := by
    rw [hs, ← Real.sqrt_mul (by positivity)]
    rw [show (N : ℝ) / 2 * (2 * N) = (N : ℝ) ^ 2 by ring, Real.sqrt_sq hNpos.le]
  set q := Real.exp (-(π * N / 2))
  set e := Real.exp (-(π * N / 24))
  have hq0 : 0 ≤ q := (Real.exp_pos _).le
  -- per-n bound
  have hper : ∀ n ∈ Finset.range N,
      whiteheadGaussianProfile N n *
        |((2 * n + 1 : ℕ) : ℝ) * (∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k)
          - N * s|
      ≤ 4 * s * (|(n : ℝ) - N / 2| * whiteheadGaussianProfile N n)
        + (2 * s + 3 * N * s * q) * whiteheadGaussianProfile N n
        + 2 * N * r * e := by
    intro n hn
    have hnN : n < N := Finset.mem_range.mp hn
    set T := ∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k with hT
    set g := whiteheadGaussianProfile N n with hg
    have hg0 : 0 ≤ g := (Real.exp_pos _).le
    have hT0 : 0 ≤ T := Finset.sum_nonneg (fun _ _ => (Real.exp_pos _).le)
    have hTle : T ≤ 2 * s := whiteheadInnerSum_le hN n
    have hTabs := abs_whiteheadInnerSum_sub_le hN n
    rw [← hT, ← hs] at hTabs
    set t := Real.exp (-(π * ((N - n : ℕ) : ℝ) ^ 2 / (4 * N)))
    have ht0 : 0 ≤ t := (Real.exp_pos _).le
    have hgt : g * t ≤ e := whiteheadGaussianProfile_mul_tail_le hN hnN.le
    have hcast : ((2 * n + 1 : ℕ) : ℝ) = 2 * ((n : ℝ) - N / 2) + 1 + N := by push_cast; ring
    have hsplit : ((2 * n + 1 : ℕ) : ℝ) * T - N * s
        = (2 * ((n : ℝ) - N / 2) + 1) * T + N * (T - s) := by rw [hcast]; ring
    have habs1 : |((2 * n + 1 : ℕ) : ℝ) * T - N * s|
        ≤ (2 * |(n : ℝ) - N / 2| + 1) * (2 * s) + N * (s * (3 * q) + t * (2 * r)) := by
      rw [hsplit]
      refine le_trans (abs_add_le _ _) ?_
      rw [abs_mul, abs_mul, abs_of_nonneg hT0, abs_of_nonneg hNpos.le]
      have h2 : |2 * ((n : ℝ) - N / 2) + 1| ≤ 2 * |(n : ℝ) - N / 2| + 1 := by
        refine le_trans (abs_add_le _ _) ?_
        rw [abs_mul]; norm_num
      have hx0 := abs_nonneg ((n : ℝ) - N / 2)
      have hA1 : |2 * ((n : ℝ) - N / 2) + 1| * T ≤ (2 * |(n : ℝ) - N / 2| + 1) * (2 * s) :=
        le_trans (mul_le_mul_of_nonneg_right h2 hT0)
          (mul_le_mul_of_nonneg_left hTle (by positivity))
      have hA2 : (N : ℝ) * |T - s| ≤ N * (s * (3 * q) + t * (2 * r)) :=
        mul_le_mul_of_nonneg_left hTabs hNpos.le
      linarith
    calc g * |((2 * n + 1 : ℕ) : ℝ) * T - N * s|
        ≤ g * ((2 * |(n : ℝ) - N / 2| + 1) * (2 * s) + N * (s * (3 * q) + t * (2 * r))) :=
          mul_le_mul_of_nonneg_left habs1 hg0
      _ = 4 * s * (|(n : ℝ) - N / 2| * g) + (2 * s + 3 * N * s * q) * g
            + 2 * N * r * (g * t) := by ring
      _ ≤ 4 * s * (|(n : ℝ) - N / 2| * g) + (2 * s + 3 * N * s * q) * g
            + 2 * N * r * e := by gcongr
  unfold whiteheadGaussErr
  rw [← hs]
  refine le_trans (Finset.sum_le_sum hper) ?_
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum,
    Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  have hA := sum_abs_mul_whiteheadGaussianProfile_le hN
  have hB := sum_whiteheadGaussianProfile_le hN
  have hBs : (2 * s + 3 * N * s * q) * ∑ n ∈ Finset.range N, whiteheadGaussianProfile N n
      ≤ (2 * s + 3 * N * s * q) * (2 * Real.sqrt (2 * N)) :=
    mul_le_mul_of_nonneg_left hB (by positivity)
  have he0 : 0 ≤ e := (Real.exp_pos _).le
  have hAs : 4 * s * ∑ n ∈ Finset.range N, |(n : ℝ) - N / 2| * whiteheadGaussianProfile N n
      ≤ 4 * s * (8 * N) := mul_le_mul_of_nonneg_left hA (by positivity)
  have hexp : (2 * s + 3 * N * s * q) * (2 * Real.sqrt (2 * N))
      = 4 * N + 6 * (N : ℝ) ^ 2 * q := by
    have : (2 * s + 3 * N * s * q) * (2 * Real.sqrt (2 * N))
        = 4 * (s * Real.sqrt (2 * N)) + 6 * N * q * (s * Real.sqrt (2 * N)) := by ring
    rw [this, hs2N]; ring
  have hfinal : 4 * s * (8 * N) ≤ 32 * N * r := by
    have : 4 * s * (8 * N) = 32 * N * s := by ring
    rw [this]; exact mul_le_mul_of_nonneg_left hsr (by positivity)
  have hlast : (N : ℝ) * (2 * N * r * e) = 2 * (N : ℝ) ^ 2 * r * e := by ring
  linarith

theorem whiteheadGaussErr_le_eventually :
    ∀ᶠ N : ℕ in Filter.atTop, whiteheadGaussErr N ≤ (N : ℝ) ^ 2 / 20 := by
  filter_upwards [Filter.eventually_ge_atTop 4000000] with N hN
  have hN1 : 1 ≤ N := by omega
  have hNr : (4000000 : ℝ) ≤ N := by exact_mod_cast hN
  have hNpos : (0 : ℝ) < N := by linarith
  refine le_trans (whiteheadGaussErr_le hN1) ?_
  set r := Real.sqrt (N : ℝ) with hr
  have hr2 : r ^ 2 = N := Real.sq_sqrt hNpos.le
  have hr0 : 0 ≤ r := Real.sqrt_nonneg _
  have hr2000 : 2000 ≤ r := by
    rw [hr, show (2000 : ℝ) = Real.sqrt (2000 ^ 2) by rw [Real.sqrt_sq (by norm_num)]]
    exact Real.sqrt_le_sqrt (by linarith)
  -- `N e^{−πN/2} ≤ 1`
  have hq : (N : ℝ) * Real.exp (-(π * N / 2)) ≤ 1 := by
    have h1 := Real.add_one_le_exp (π * N / 2)
    have h2 : (N : ℝ) ≤ Real.exp (π * N / 2) := by nlinarith [Real.pi_gt_three]
    rw [Real.exp_neg]
    rw [mul_inv_le_iff₀ (Real.exp_pos _)]
    linarith
  -- `N² e^{−πN/24} ≤ 128`
  have he : (N : ℝ) ^ 2 * Real.exp (-(π * N / 24)) ≤ 128 := by
    have h1 := Real.pow_div_factorial_le_exp (x := π * N / 24) (by positivity) 2
    have hy : (N : ℝ) / 8 ≤ π * N / 24 := by nlinarith [Real.pi_gt_three]
    have hy0 : (0 : ℝ) ≤ N / 8 := by positivity
    have h2 : ((N : ℝ) / 8) ^ 2 / 2 ≤ Real.exp (π * N / 24) := by
      refine le_trans ?_ h1
      simp only [Nat.factorial]
      norm_num
      nlinarith
    rw [Real.exp_neg, mul_inv_le_iff₀ (Real.exp_pos _)]
    nlinarith
  have hq0 : 0 ≤ Real.exp (-(π * N / 2)) := (Real.exp_pos _).le
  have he0 : 0 ≤ Real.exp (-(π * N / 24)) := (Real.exp_pos _).le
  have hA : 6 * (N : ℝ) ^ 2 * Real.exp (-(π * N / 2)) ≤ 6 * N := by
    have : 6 * (N : ℝ) ^ 2 * Real.exp (-(π * N / 2))
        = 6 * N * ((N : ℝ) * Real.exp (-(π * N / 2))) := by ring
    rw [this]; nlinarith
  have hB : 2 * (N : ℝ) ^ 2 * r * Real.exp (-(π * N / 24)) ≤ 256 * r := by
    have : 2 * (N : ℝ) ^ 2 * r * Real.exp (-(π * N / 24))
        = 2 * r * ((N : ℝ) ^ 2 * Real.exp (-(π * N / 24))) := by ring
    rw [this]; nlinarith
  rw [← hr2]
  rw [← hr2] at hA hB
  nlinarith [pow_le_pow_left₀ (by norm_num : (0:ℝ) ≤ 2000) hr2000 3]

/-- **The reduction.**  vdV Lemma 2a/2b in `(2n+1)`-weighted `L¹` form
(`WhiteheadInnerGaussianModel`) implies the outer Gaussian model, with
`A_N = B_N · N · √(N/2)`.  The `k`-sum of the 2D Gaussian (completing the square,
centre `(N−n)/2` = midpoint of the `k`-range), the lattice points outside the
range, and the `(2n+1) → N` swap are all proved here. -/
instance whiteheadOuterGaussianModel_of_inner [WhiteheadInnerGaussianModel] :
    WhiteheadOuterGaussianModel := by
  obtain ⟨B, hB⟩ := WhiteheadInnerGaussianModel.model
  refine ⟨⟨fun N => B N * N * Real.sqrt ((N : ℝ) / 2), ?_⟩⟩
  filter_upwards [hB, whiteheadGaussErr_le_eventually, Filter.eventually_ge_atTop 1]
    with N ⟨hBpos, hres⟩ herr hN1
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN1
  set s := Real.sqrt ((N : ℝ) / 2) with hs
  have hspos : 0 < s := Real.sqrt_pos.mpr (by positivity)
  refine ⟨by positivity, ?_⟩
  -- per-n decomposition
  have hper : ∀ n ∈ Finset.range N,
      |whiteheadOuterWeight N n - B N * N * s * whiteheadGaussianProfile N n|
        ≤ ((2 * n + 1 : ℕ) : ℝ) *
            ∑ k ∈ Finset.range (N - n), |whiteheadTerm N n k - B N * whitehead2DGauss N n k|
          + B N * (whiteheadGaussianProfile N n *
            |((2 * n + 1 : ℕ) : ℝ) * (∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k)
              - N * s|) := by
    intro n _
    set g := whiteheadGaussianProfile N n with hg
    have hg0 : 0 ≤ g := (Real.exp_pos _).le
    set T := ∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k with hT
    have hdecomp : whiteheadOuterWeight N n - B N * N * s * g
        = ((2 * n + 1 : ℕ) : ℝ) *
            ∑ k ∈ Finset.range (N - n), (whiteheadTerm N n k - B N * whitehead2DGauss N n k)
          + B N * g * (((2 * n + 1 : ℕ) : ℝ) * T - N * s) := by
      unfold whiteheadOuterWeight
      rw [Finset.sum_sub_distrib, hT, Finset.mul_sum, Finset.mul_sum]
      simp only [whitehead2DGauss, ← hg]
      rw [mul_sub, Finset.mul_sum, Finset.mul_sum]
      have : ∑ i ∈ Finset.range (N - n), ((2 * n + 1 : ℕ) : ℝ) * (B N * (g * whiteheadInnerGauss N n i))
          = B N * g * ∑ i ∈ Finset.range (N - n), ((2 * n + 1 : ℕ) : ℝ) * whiteheadInnerGauss N n i := by
        rw [Finset.mul_sum]; refine Finset.sum_congr rfl (fun i _ => by ring)
      rw [this, ← Finset.mul_sum]
      ring
    rw [hdecomp]
    refine le_trans (abs_add_le _ _) ?_
    have h2 : |B N * g * (((2 * n + 1 : ℕ) : ℝ) * T - N * s)|
        = B N * (g * |((2 * n + 1 : ℕ) : ℝ) * T - N * s|) := by
      rw [abs_mul, abs_mul, abs_of_pos hBpos, abs_of_nonneg hg0]; ring
    rw [h2, abs_mul, abs_of_nonneg (by positivity)]
    gcongr
    exact Finset.abs_sum_le_sum_abs _ _
  refine le_trans (Finset.sum_le_sum hper) ?_
  rw [Finset.sum_add_distrib, ← Finset.mul_sum]
  have herr' : ∑ n ∈ Finset.range N, whiteheadGaussianProfile N n *
      |((2 * n + 1 : ℕ) : ℝ) * (∑ k ∈ Finset.range (N - n), whiteheadInnerGauss N n k)
        - N * s| ≤ (N : ℝ) ^ 2 / 20 := herr
  have hBerr := mul_le_mul_of_nonneg_left herr' hBpos.le
  -- `s √N = N/√2 ≥ (7/10) N`
  have hsN : (7 / 10 : ℝ) * N ≤ s * Real.sqrt N := by
    have hsq : (s * Real.sqrt N) ^ 2 = (N : ℝ) ^ 2 / 2 := by
      rw [mul_pow, hs, Real.sq_sqrt (by positivity), Real.sq_sqrt hNpos.le]; ring
    have h0 : 0 ≤ s * Real.sqrt N := by positivity
    nlinarith
  have htarget : B N * (N : ℝ) ^ 2 / 8 + B N * ((N : ℝ) ^ 2 / 20)
      ≤ B N * N * s * Real.sqrt N / 4 := by
    have : B N * N * s * Real.sqrt N / 4 = B N * N * (s * Real.sqrt N) / 4 := by ring
    rw [this]
    have hBN : 0 ≤ B N * N := by positivity
    nlinarith [mul_le_mul_of_nonneg_left hsN hBN]
  linarith

end QOU.Knot.FigureEightVolume
