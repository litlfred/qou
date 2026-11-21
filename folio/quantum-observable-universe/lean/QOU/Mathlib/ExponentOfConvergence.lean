import QOU.Mathlib.JensenZeroCounting
import QOU.Mathlib.HadamardFactorization
import Mathlib.Analysis.SpecificLimits.Basic

/-!
# Exponent of convergence ≤ order (Hadamard PI-4)

Bean `qou-c3if`. For an entire `f` with `f 0 ≠ 0` satisfying the growth hypothesis
`IsEntireOfOrderLE f ρ` (`‖f z‖ ≤ A·exp(C‖z‖^ρ)`, `0 ≤ ρ`), and every `σ > ρ`, the zeros
of `f`, counted with multiplicity, satisfy

    ∑_u ord_u(f) · ‖u‖^{−σ} < ∞,

i.e. the exponent of convergence of the zero sequence is at most `ρ`.

The zero sequence is encoded by Mathlib's divisor `MeromorphicOn.divisor f univ`, so the
statement is a `Summable` over `ℂ`; no enumeration of the zeros is chosen.

Proof:

* `count_le_rpow` — from `zero_count_le` (Jensen, `QOU.Mathlib.JensenZeroCounting`) and the
  growth bound on the circle `‖z‖ = 2r`: `n(r) ≤ K · r^ρ` for `r ≥ 1`.
* `sum_divisor_le_count` — a finite partial sum of orders over points of `‖u‖ ≤ r` is at
  most `n(r)`.
* `summable_divisor_mul_rpow_neg` — dyadic shells. Each zero with `‖u‖ > 1` is assigned
  `k` with `‖u‖ ≤ 2^k ≤ 2‖u‖`; the shell `k` contributes at most
  `n(2^k)·(2^k/2)^{−σ} ≤ K·2^σ·(2^{ρ−σ})^k`, a geometric series. The zeros with
  `‖u‖ ≤ 1` are finitely many.

SCOPE. This is one of the three inputs to the Hadamard factorization (PI-5), not PI-5.
It is stated against `IsEntireOfOrderLE`, which is finite type at order `ρ` and is
strictly stronger than "order ≤ ρ" (bean `qou-c3if`, ROAST).
`summable_divisor_mul_rpow_neg_of_forall_gt` takes the eps-form hypothesis
"`IsEntireOfOrderLE f ρ'` for every `ρ' > ρ`" instead. That classical "order ≤ ρ" implies
this eps-form hypothesis is standard but is not proved here.

§7c: archimedean (norms, `Real.rpow`, `Real.log`, `Real.exp`).

-- Ref: [leitner2026] standard complex analysis: Ahlfors, *Complex Analysis*, 3rd ed.,
   §5.3.2 (the zero-counting estimate in Hadamard's theorem); Conway, *Functions of One
   Complex Variable I*, XI.§2.
-/

open Real Metric Set Function

namespace QOU.Mathlib.ExponentOfConvergence

open QOU.Mathlib.JensenZeroCounting
open QOU.Mathlib.HadamardFactorization (IsEntireOfOrderLE)

/-- The zero divisor of `f` on all of `ℂ`. -/
noncomputable abbrev zeroDivisor (f : ℂ → ℂ) := MeromorphicOn.divisor f univ

/-- The counting function `n(r)`: the number of zeros of `f` in `‖z‖ ≤ r` with
multiplicity. -/
noncomputable def count (f : ℂ → ℂ) (r : ℝ) : ℝ :=
  ∑ᶠ u, (MeromorphicOn.divisor f (closedBall 0 r) u : ℝ)

theorem zeroDivisor_nonneg {f : ℂ → ℂ} (hf : Differentiable ℂ f) (u : ℂ) :
    (0 : ℝ) ≤ zeroDivisor f u := by
  exact_mod_cast MeromorphicOn.AnalyticOnNhd.divisor_nonneg
    (fun z _ => hf.analyticAt z : AnalyticOnNhd ℂ f univ) u

theorem divisor_ball_eq {f : ℂ → ℂ} (hf : Differentiable ℂ f) {r : ℝ} {u : ℂ}
    (hu : u ∈ closedBall (0 : ℂ) r) :
    MeromorphicOn.divisor f (closedBall 0 r) u = zeroDivisor f u := by
  have han : AnalyticOnNhd ℂ f univ := fun z _ => hf.analyticAt z
  rw [← MeromorphicOn.divisor_restrict han.meromorphicOn (subset_univ _),
    Function.locallyFinsuppWithin.restrict_apply, if_pos hu]

/-- A finite partial sum of orders over points in `‖u‖ ≤ r` is at most `n(r)`. -/
theorem sum_divisor_le_count {f : ℂ → ℂ} (hf : Differentiable ℂ f) {r : ℝ}
    (t : Finset ℂ) (ht : ∀ u ∈ t, u ∈ closedBall (0 : ℂ) r) :
    ∑ u ∈ t, (zeroDivisor f u : ℝ) ≤ count f r := by
  classical
  set Dr := MeromorphicOn.divisor f (closedBall (0 : ℂ) r)
  have hanr : AnalyticOnNhd ℂ f (closedBall 0 r) := fun z _ => hf.analyticAt z
  have hnn : ∀ u, (0 : ℝ) ≤ Dr u := fun u => by
    exact_mod_cast MeromorphicOn.AnalyticOnNhd.divisor_nonneg hanr u
  have hfin : Dr.support.Finite := Dr.finiteSupport (isCompact_closedBall 0 _)
  have hsupp : (fun u => (Dr u : ℝ)).support ⊆ ↑(t ∪ hfin.toFinset) := by
    intro u hu
    simp only [Finset.coe_union, Set.Finite.coe_toFinset, mem_union, mem_support]
    right; intro h; simp_all
  rw [count, finsum_eq_sum_of_support_subset _ hsupp]
  calc ∑ u ∈ t, (zeroDivisor f u : ℝ) = ∑ u ∈ t, (Dr u : ℝ) :=
        Finset.sum_congr rfl fun u hu => by rw [divisor_ball_eq hf (ht u hu)]
    _ ≤ ∑ u ∈ t ∪ hfin.toFinset, (Dr u : ℝ) :=
        Finset.sum_le_sum_of_subset_of_nonneg Finset.subset_union_left
          fun u _ _ => hnn u

/-- **The counting bound.** Under `IsEntireOfOrderLE f ρ` with `0 ≤ ρ` and `f 0 ≠ 0`,
there is `K` with `n(r) ≤ K · r^ρ` for every `r ≥ 1`. -/
theorem count_le_rpow {f : ℂ → ℂ} {ρ : ℝ} (hf : IsEntireOfOrderLE f ρ) (hf0 : f 0 ≠ 0)
    (hρ : 0 ≤ ρ) : ∃ K : ℝ, 0 ≤ K ∧ ∀ r : ℝ, 1 ≤ r → count f r ≤ K * r ^ ρ := by
  obtain ⟨hd, A, C, hC, hgrowth⟩ := hf
  set B := max A 1
  have hB1 : 1 ≤ B := le_max_right _ _
  have hlog2 : 0 < log 2 := log_pos one_lt_two
  set c0 := |log B - log ‖f 0‖|
  refine ⟨(c0 + C * 2 ^ ρ) / log 2, by positivity, fun r hr => ?_⟩
  have hr0 : 0 < r := lt_of_lt_of_le one_pos hr
  set M := B * exp (C * (2 * r) ^ ρ)
  have hM : 1 ≤ M := by
    have : 1 ≤ exp (C * (2 * r) ^ ρ) := one_le_exp (by positivity)
    nlinarith
  have hbound : ∀ z ∈ sphere (0 : ℂ) (2 * r), ‖f z‖ ≤ M := by
    intro z hz
    have hz' : ‖z‖ = 2 * r := by simpa using hz
    calc ‖f z‖ ≤ A * exp (C * ‖z‖ ^ ρ) := hgrowth z
      _ ≤ B * exp (C * ‖z‖ ^ ρ) := mul_le_mul_of_nonneg_right (le_max_left _ _) (exp_pos _).le
      _ = M := by rw [hz']
  have hcount := zero_count_le hd hf0 hr0 hM hbound
  have hlogM : log M = log B + C * (2 * r) ^ ρ := by
    rw [log_mul (by positivity) (exp_pos _).ne', log_exp]
  have hrρ : 1 ≤ r ^ ρ := one_le_rpow hr hρ
  have h2r : (2 * r) ^ ρ = 2 ^ ρ * r ^ ρ := mul_rpow (by norm_num) hr0.le
  have hc0 : log B - log ‖f 0‖ ≤ c0 * r ^ ρ := by
    calc log B - log ‖f 0‖ ≤ c0 := le_abs_self _
      _ = c0 * 1 := (mul_one _).symm
      _ ≤ c0 * r ^ ρ := mul_le_mul_of_nonneg_left hrρ (abs_nonneg _)
  rw [count, div_mul_eq_mul_div, le_div_iff₀ hlog2]
  have h2ρ : 0 < (2 : ℝ) ^ ρ := by positivity
  calc (∑ᶠ u, (MeromorphicOn.divisor f (closedBall 0 r) u : ℝ)) * log 2
      ≤ log M - log ‖f 0‖ := hcount
    _ = (log B - log ‖f 0‖) + C * 2 ^ ρ * r ^ ρ := by rw [hlogM, h2r]; ring
    _ ≤ c0 * r ^ ρ + C * 2 ^ ρ * r ^ ρ := by linarith
    _ = (c0 + C * 2 ^ ρ) * r ^ ρ := by ring

/-- **Exponent of convergence ≤ order (Hadamard PI-4).** If `f` satisfies
`IsEntireOfOrderLE f ρ` with `0 ≤ ρ` and `f 0 ≠ 0`, then for every `σ > ρ`,
`∑_u ord_u(f) · ‖u‖^{−σ}` converges. -/
theorem summable_divisor_mul_rpow_neg {f : ℂ → ℂ} {ρ σ : ℝ} (hf : IsEntireOfOrderLE f ρ)
    (hf0 : f 0 ≠ 0) (hρ : 0 ≤ ρ) (hσ : ρ < σ) :
    Summable fun u : ℂ => (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ) := by
  classical
  have hd : Differentiable ℂ f := hf.1
  obtain ⟨K, hK, hcount⟩ := count_le_rpow hf hf0 hρ
  have hσ0 : 0 < σ := lt_of_le_of_lt hρ hσ
  have hnn : ∀ u : ℂ, (0 : ℝ) ≤ zeroDivisor f u * ‖u‖ ^ (-σ) := fun u =>
    mul_nonneg (zeroDivisor_nonneg hd u) (rpow_nonneg (norm_nonneg _) _)
  -- the finitely many zeros in the unit ball
  set D1 := MeromorphicOn.divisor f (closedBall (0 : ℂ) 1)
  have hfin1 : D1.support.Finite := D1.finiteSupport (isCompact_closedBall 0 _)
  set S1 := ∑ u ∈ hfin1.toFinset, (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)
  -- the geometric ratio
  set g := (2 : ℝ) ^ (ρ - σ)
  have hg0 : 0 ≤ g := by positivity
  have hg1 : g < 1 := rpow_lt_one_of_one_lt_of_neg one_lt_two (by linarith)
  have hgeo : Summable fun k : ℕ => g ^ k := summable_geometric_of_lt_one hg0 hg1
  set S2 := K * 2 ^ σ * ∑' k : ℕ, g ^ k
  refine summable_of_sum_le hnn (c := S1 + S2) fun s => ?_
  rw [← Finset.sum_filter_add_sum_filter_not s (fun u => ‖u‖ ≤ 1)]
  refine add_le_add ?_ ?_
  · -- inside the unit ball
    calc ∑ u ∈ s with ‖u‖ ≤ 1, (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)
        = ∑ u ∈ (s.filter fun u => ‖u‖ ≤ 1) ∩ hfin1.toFinset,
            (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ) := by
          refine (Finset.sum_subset Finset.inter_subset_left fun u hu hnot => ?_).symm
          have hu1 : u ∈ closedBall (0 : ℂ) 1 := by
            simpa [mem_closedBall, dist_zero_right] using (Finset.mem_filter.mp hu).2
          have : D1 u = 0 := by
            by_contra h
            exact hnot (Finset.mem_inter.mpr ⟨hu, by simpa using h⟩)
          rw [← divisor_ball_eq hd hu1]
          simp [D1, this]
      _ ≤ S1 := Finset.sum_le_sum_of_subset_of_nonneg Finset.inter_subset_right
          fun u _ _ => hnn u
  · -- outside the unit ball: dyadic shells
    set s2 := s.filter fun u => ¬ ‖u‖ ≤ 1
    have hshell : ∀ u ∈ s2, ∃ k : ℕ, ‖u‖ ≤ 2 ^ k ∧ (2 : ℝ) ^ k ≤ 2 * ‖u‖ := by
      intro u hu
      have hu1 : 1 < ‖u‖ := lt_of_not_ge (Finset.mem_filter.mp hu).2
      obtain ⟨n, hn1, hn2⟩ := exists_nat_pow_near hu1.le one_lt_two
      refine ⟨n + 1, hn2.le, ?_⟩
      rw [pow_succ]; linarith
    choose! kf hkf using hshell
    set T := s2.image kf
    rw [← Finset.sum_fiberwise_of_maps_to (g := kf) (t := T)
      (fun u hu => Finset.mem_image_of_mem kf hu)]
    calc ∑ k ∈ T, ∑ u ∈ s2 with kf u = k, (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)
        ≤ ∑ k ∈ T, K * 2 ^ σ * g ^ k := by
          refine Finset.sum_le_sum fun k _ => ?_
          have hk2 : (1 : ℝ) ≤ 2 ^ k := one_le_pow₀ one_le_two
          have h2k : (0 : ℝ) < 2 ^ k := by positivity
          -- each term: ‖u‖^{-σ} ≤ (2^k/2)^{-σ}
          have hterm : ∀ u ∈ s2.filter (fun u => kf u = k),
              (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)
                ≤ (zeroDivisor f u : ℝ) * ((2 : ℝ) ^ k / 2) ^ (-σ) := by
            intro u hu
            obtain ⟨hu', rfl⟩ := Finset.mem_filter.mp hu
            refine mul_le_mul_of_nonneg_left ?_ (zeroDivisor_nonneg hd u)
            exact rpow_le_rpow_of_nonpos (by positivity) (by linarith [(hkf u hu').2])
              (by linarith)
          have hball : ∀ u ∈ s2.filter (fun u => kf u = k), u ∈ closedBall (0 : ℂ) (2 ^ k) := by
            intro u hu
            obtain ⟨hu', rfl⟩ := Finset.mem_filter.mp hu
            simpa [mem_closedBall, dist_zero_right] using (hkf u hu').1
          calc ∑ u ∈ s2 with kf u = k, (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)
              ≤ ∑ u ∈ s2 with kf u = k, (zeroDivisor f u : ℝ) * ((2 : ℝ) ^ k / 2) ^ (-σ) :=
                Finset.sum_le_sum hterm
            _ = (∑ u ∈ s2 with kf u = k, (zeroDivisor f u : ℝ)) * ((2 : ℝ) ^ k / 2) ^ (-σ) := by
                rw [Finset.sum_mul]
            _ ≤ (K * ((2 : ℝ) ^ k) ^ ρ) * ((2 : ℝ) ^ k / 2) ^ (-σ) :=
                mul_le_mul_of_nonneg_right
                  ((sum_divisor_le_count hd _ hball).trans (hcount _ hk2)) (by positivity)
            _ = K * 2 ^ σ * g ^ k := by
                have e1 : ((2 : ℝ) ^ k / 2) ^ (-σ) = ((2 : ℝ) ^ k) ^ (-σ) * 2 ^ σ := by
                  rw [div_rpow h2k.le (by norm_num), rpow_neg (by norm_num : (0:ℝ) ≤ 2),
                    div_inv_eq_mul]
                have e2 : ((2 : ℝ) ^ k) ^ ρ * ((2 : ℝ) ^ k) ^ (-σ) = g ^ k := by
                  rw [← rpow_add h2k, ← rpow_natCast, ← rpow_mul (by norm_num),
                    ← rpow_natCast, ← rpow_mul (by norm_num)]
                  congr 1; ring
                rw [e1, ← e2]; ring
      _ = K * 2 ^ σ * ∑ k ∈ T, g ^ k := by rw [Finset.mul_sum]
      _ ≤ S2 := mul_le_mul_of_nonneg_left
          (hgeo.sum_le_tsum T fun k _ => pow_nonneg hg0 k) (by positivity)

/-- **Eps-form.** If `f` satisfies `IsEntireOfOrderLE f ρ'` for every `ρ' > ρ` (finite type
at every order above `ρ`, which is the classical "order ≤ ρ" up to the bound near the
origin), then `∑_u ord_u(f)·‖u‖^{−σ}` converges for every `σ > ρ`. -/
theorem summable_divisor_mul_rpow_neg_of_forall_gt {f : ℂ → ℂ} {ρ σ : ℝ}
    (hf : ∀ ρ', ρ < ρ' → IsEntireOfOrderLE f ρ') (hf0 : f 0 ≠ 0) (hρ : 0 ≤ ρ) (hσ : ρ < σ) :
    Summable fun u : ℂ => (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ) :=
  summable_divisor_mul_rpow_neg (hf ((ρ + σ) / 2) (by linarith)) hf0 (by linarith)
    (by linarith)

/-- **Genus bound.** With `p = ⌊ρ⌋₊ ≤ ρ`, the series `∑_u ord_u(f)·‖u‖^{−(p+1)}` converges.
So the least `p` for which this series converges (the genus of the zero sequence) is at
most `⌊ρ⌋₊ ≤ ρ`. -/
theorem summable_divisor_floor_genus {f : ℂ → ℂ} {ρ : ℝ} (hf : IsEntireOfOrderLE f ρ)
    (hf0 : f 0 ≠ 0) (hρ : 0 ≤ ρ) :
    ((⌊ρ⌋₊ : ℕ) : ℝ) ≤ ρ ∧
      Summable fun u : ℂ => (zeroDivisor f u : ℝ) * ‖u‖ ^ (-((⌊ρ⌋₊ : ℝ) + 1)) :=
  ⟨Nat.floor_le hρ, summable_divisor_mul_rpow_neg hf hf0 hρ (Nat.lt_floor_add_one ρ)⟩

end QOU.Mathlib.ExponentOfConvergence
