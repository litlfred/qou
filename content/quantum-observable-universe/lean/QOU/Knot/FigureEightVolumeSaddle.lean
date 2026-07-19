/-
  Figure-eight volume conjecture — saddle-point analysis, brick 1 (the sin²
  / Lobachevsky entry point).

  The `sorry` in `FigureEightVolumeLiterature` is the concrete saddle-point
  asymptotic `(2π/N)·log⟨4₁⟩_N → Vol(4₁)` of the explicit Kashaev sum. This
  file begins the honest formalization of that analysis (NOT the general Borel
  uniqueness engine, which is a different ingredient — see the status note in
  `FigureEightVolumeLiterature`). The first step of every published proof
  (Andersen–Hansen; Ohtsuki) is to rewrite the Kashaev product in the
  `2 − 2cos = 4sin²` form, turning each `log`-term into a Riemann sum for the
  Lobachevsky integral `∫ log(2 sin πx) dx` whose extremum is `Vol(4₁)`.

  Proved here, sorry-free:
    * `two_sub_two_cos_two_mul` — the factor identity `2 − 2cos(2x) = 4 sin²x`;
    * `kashaevProd_eq_sin` — hence `⟨4₁⟩`'s k-th product is `4ᵏ (∏ⱼ sin(πj/N))²`.

  HONEST SCOPE. This is the algebraic entry point only. The load-bearing
  remainder is genuinely research-grade and NOT closed here: (i) the Riemann
  sum `(1/N)∑ⱼ log(2 sin(πj/N)) → −Λ(·)/π` (Lobachevsky; Mathlib has
  `∫ log sin` in `LogTrigonometric`, not the Lobachevsky function); (ii) the
  saddle/extremum over `k` giving `Vol(4₁) = 6Λ(π/3)`; (iii) the
  `log(∑) ≈ max log-term` step (the sum is dominated by its largest term to
  leading exponential order). Each is a separate brick; the full theorem is the
  Andersen–Hansen/Ohtsuki analysis. Scoped in bean bca6 / el8w-saddle.

  Archimedean (ℝ).

  -- Ref: [andersen-hansen2006] https://doi.org/10.1142/S0218216506004555
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import QOU.Knot.FigureEightVolume
import QOU.Knot.Clausen
import Mathlib.Analysis.Calculus.LocalExtr.Basic
import Mathlib.Topology.Order.LocalExtr
import Mathlib.Topology.Order.Compact

namespace QOU.Knot.FigureEightVolume

open Real Finset

/-- The factor identity `2 − 2cos(2x) = 4 sin²x` (from `cos 2x = 1 − 2sin²x`). -/
theorem two_sub_two_cos_two_mul (x : ℝ) :
    2 - 2 * Real.cos (2 * x) = 4 * Real.sin x ^ 2 := by
  have h1 := Real.cos_two_mul x
  have h2 := Real.sin_sq_add_cos_sq x
  nlinarith [h1, h2]

/-- **The Kashaev product in sin form.** The `k`-th factor of the figure-eight
    Kashaev invariant is `4ᵏ (∏ⱼ₌₁ᵏ sin(πj/N))²` — the `2 − 2cos = 4sin²`
    rewrite that turns `log ⟨4₁⟩` into a Lobachevsky Riemann sum. -/
theorem kashaevProd_eq_sin (N k : ℕ) :
    kashaevProd N k
      = 4 ^ k * (∏ j ∈ Finset.Icc 1 k, Real.sin (π * j / N)) ^ 2 := by
  unfold kashaevProd
  have hfac : ∀ j ∈ Finset.Icc 1 k,
      2 - 2 * Real.cos (2 * π * j / N) = 4 * Real.sin (π * j / N) ^ 2 := by
    intro j _
    have hx : 2 * π * (j : ℝ) / N = 2 * (π * j / N) := by ring
    rw [hx, two_sub_two_cos_two_mul]
  rw [Finset.prod_congr rfl hfac, Finset.prod_mul_distrib, Finset.prod_const,
    Finset.prod_pow, Nat.card_Icc, Nat.add_sub_cancel]

/-- **The saddle critical point (dual-purpose).** On `(0, π)`,
    `2 sin(θ/2) = 1 ↔ θ = π/3`. This is the location of the Kashaev
    saddle — the factors `4 sin²(πj/N)` of `kashaevProd_eq_sin` cross `1` here —
    and it is *simultaneously* the critical point of the QOU dilog-saddle
    potential `V(θ) = Im Li₂(e^{iθ})`, whose derivative is `−log(2 sin(θ/2))`
    (content block `rem:dilog-saddle-regime`): `V'(θ) = 0 ⟺ 2 sin(θ/2) = 1 ⟺
    θ = π/3`, giving `Vol(4₁) = 2 Cl₂(π/3)`. The block states this narratively;
    this is its Lean proof, needing no Clausen function — only `sin(π/6) = 1/2`
    and injectivity of `sin` on `[−π/2, π/2]`. -/
theorem saddle_critical_point {θ : ℝ} (h0 : 0 < θ) (hπ : θ < π) :
    2 * Real.sin (θ / 2) = 1 ↔ θ = π / 3 := by
  have hpi := Real.pi_pos
  constructor
  · intro h
    have hs : Real.sin (θ / 2) = Real.sin (π / 6) := by
      rw [Real.sin_pi_div_six]; linarith
    have hmem1 : θ / 2 ∈ Set.Icc (-(π / 2)) (π / 2) :=
      ⟨by linarith, by linarith⟩
    have hmem2 : π / 6 ∈ Set.Icc (-(π / 2)) (π / 2) :=
      ⟨by linarith, by linarith⟩
    have := Real.injOn_sin hmem1 hmem2 hs
    linarith
  · intro h
    rw [h, show π / 3 / 2 = π / 6 by ring, Real.sin_pi_div_six]
    norm_num

/-- **Saddle brick E3a (sorry-free).** On the full interval `(0, 2π)` the
    critical-point equation has exactly TWO roots:
    `2 sin(θ/2) = 1 ↔ θ = π/3 ∨ θ = 5π/3`. Extends `saddle_critical_point`
    (which covers `(0, π)`) by reflecting through `sin(π − x) = sin x` on the
    upper half. `θ = 5π/3` is where `Cl₂` attains its minimum `−Cl₂(π/3)` —
    the Kashaev saddle the volume emerges from (bean qou-yzs2). -/
theorem saddle_critical_point_two_pi {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    2 * Real.sin (θ / 2) = 1 ↔ θ = π / 3 ∨ θ = 5 * π / 3 := by
  have hpi := Real.pi_pos
  constructor
  · intro h
    rcases le_or_gt (θ / 2) (π / 2) with hle | hgt
    · rcases lt_or_eq_of_le (by linarith : θ ≤ π) with hlt | heq
      · exact Or.inl ((saddle_critical_point h0 hlt).mp h)
      · exfalso
        rw [heq] at h
        norm_num [Real.sin_pi_div_two] at h
    · right
      have hs : Real.sin (π - θ / 2) = Real.sin (π / 6) := by
        rw [Real.sin_pi_sub, Real.sin_pi_div_six]; linarith
      have hmem1 : π - θ / 2 ∈ Set.Icc (-(π / 2)) (π / 2) :=
        ⟨by linarith, by linarith⟩
      have hmem2 : π / 6 ∈ Set.Icc (-(π / 2)) (π / 2) :=
        ⟨by linarith, by linarith⟩
      have := Real.injOn_sin hmem1 hmem2 hs
      linarith
  · rintro (h | h) <;> rw [h]
    · rw [show π / 3 / 2 = π / 6 by ring, Real.sin_pi_div_six]; norm_num
    · rw [show 5 * π / 3 / 2 = π - π / 6 by ring, Real.sin_pi_sub,
        Real.sin_pi_div_six]
      norm_num

/-- The largest Kashaev term is at least `1` (witnessed by the `k = 0` empty
    product) — the positivity the log-squeeze needs. -/
theorem one_le_sup_kashaevProd (N : ℕ) (hN : 1 ≤ N) :
    1 ≤ (Finset.range N).sup'
      (Finset.nonempty_range_iff.mpr (by omega)) (kashaevProd N) := by
  have h0 : (0 : ℕ) ∈ Finset.range N := Finset.mem_range.mpr (by omega)
  calc (1 : ℝ) = kashaevProd N 0 := (kashaevProd_zero N).symm
    _ ≤ _ := Finset.le_sup' (kashaevProd N) h0

/-- **Saddle brick E1, lower half (sorry-free).** The max log-term bounds
    `log kashaev` below: a single nonneg term is at most the sum. -/
theorem log_sup_le_log_kashaev (N : ℕ) (hN : 1 ≤ N) :
    Real.log ((Finset.range N).sup'
        (Finset.nonempty_range_iff.mpr (by omega)) (kashaevProd N))
      ≤ Real.log (kashaev N) := by
  have hne : (Finset.range N).Nonempty := Finset.nonempty_range_iff.mpr (by omega)
  have hsup1 := one_le_sup_kashaevProd N hN
  obtain ⟨k, hk, hEq⟩ := Finset.exists_mem_eq_sup' hne (kashaevProd N)
  have hle : (Finset.range N).sup' hne (kashaevProd N) ≤ kashaev N := by
    rw [hEq]
    unfold kashaev
    exact Finset.single_le_sum (fun i _ => kashaevProd_nonneg N i) hk
  exact Real.log_le_log (by linarith) hle

/-- **Saddle brick E1, upper half (sorry-free).** `log kashaev` exceeds the max
    log-term by at most `log N`: the sum of `N` terms is at most `N · max`.
    Together with the lower half, `(2π/N)·log kashaev` and `(2π/N)·max log-term`
    differ by at most `(2π/N)·log N → 0` — the `log(Σ) ≈ max log-term` step of
    the saddle asymptotic at exponential scale (bean qou-3g69). -/
theorem log_kashaev_le_log_add (N : ℕ) (hN : 1 ≤ N) :
    Real.log (kashaev N)
      ≤ Real.log N + Real.log ((Finset.range N).sup'
          (Finset.nonempty_range_iff.mpr (by omega)) (kashaevProd N)) := by
  have hne : (Finset.range N).Nonempty := Finset.nonempty_range_iff.mpr (by omega)
  have hsup1 := one_le_sup_kashaevProd N hN
  have hNpos : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
  have hsum : kashaev N ≤ (N : ℝ) * (Finset.range N).sup' hne (kashaevProd N) := by
    unfold kashaev
    calc ∑ k ∈ Finset.range N, kashaevProd N k
        ≤ ∑ _k ∈ Finset.range N, (Finset.range N).sup' hne (kashaevProd N) :=
          Finset.sum_le_sum (fun i hi => Finset.le_sup' (kashaevProd N) hi)
      _ = (N : ℝ) * (Finset.range N).sup' hne (kashaevProd N) := by
          rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  calc Real.log (kashaev N)
      ≤ Real.log ((N : ℝ) * (Finset.range N).sup' hne (kashaevProd N)) :=
        Real.log_le_log (kashaev_pos N hN) hsum
    _ = Real.log N + Real.log ((Finset.range N).sup' hne (kashaevProd N)) :=
        Real.log_mul (ne_of_gt hNpos) (by linarith)

/-- **Saddle brick E3c — the global minimum of `Cl₂` (sorry-free).** On
    `[0, 2π]`, `Cl₂(θ) ≥ −Cl₂(π/3)`. Compactness gives a minimiser; it is
    interior (the endpoints give `0`, but `Cl₂(5π/3) = −Cl₂(π/3) < 0` by E2+E3b);
    interior minimisers are critical (`IsLocalMin.deriv_eq_zero` +
    `hasDerivAt_cl_2`), so by E3a the minimiser is `π/3` or `5π/3`; positivity
    (E3b) rules out `π/3`. Hence the minimum is `Cl₂(5π/3) = −Cl₂(π/3)`.
    (bean qou-yzs2) -/
theorem neg_Cl_2_pi_div_three_le {θ : ℝ} (hθ : θ ∈ Set.Icc (0 : ℝ) (2 * π)) :
    -QOU.Archimedean.Cl_2 (π / 3) ≤ QOU.Archimedean.Cl_2 θ := by
  have hpi := Real.pi_pos
  obtain ⟨θ₀, hθ₀mem, hmin⟩ :=
    (isCompact_Icc (a := (0 : ℝ)) (b := 2 * π)).exists_isMinOn
      (Set.nonempty_Icc.mpr (by linarith)) QOU.Knot.continuous_Cl_2.continuousOn
  have h53 : QOU.Archimedean.Cl_2 (5 * π / 3) = -QOU.Archimedean.Cl_2 (π / 3) := by
    have h := QOU.Knot.Cl_2_two_pi_sub (π / 3)
    rw [show 2 * π - π / 3 = 5 * π / 3 by ring] at h
    exact h
  have hminle : QOU.Archimedean.Cl_2 θ₀ ≤ -QOU.Archimedean.Cl_2 (π / 3) := by
    have h5mem : (5 * π / 3 : ℝ) ∈ Set.Icc (0 : ℝ) (2 * π) := ⟨by linarith, by linarith⟩
    have := hmin h5mem
    simp only [Set.mem_setOf_eq] at this
    rwa [h53] at this
  have hneg : QOU.Archimedean.Cl_2 θ₀ < 0 := by
    linarith [QOU.Knot.Cl_2_pi_div_three_pos]
  have h00 : θ₀ ≠ 0 := by
    intro h; rw [h, QOU.Archimedean.Cl_2_zero] at hneg; linarith
  have h2p : θ₀ ≠ 2 * π := by
    intro h; rw [h, QOU.Archimedean.Cl_2_two_pi] at hneg; linarith
  have hint : θ₀ ∈ Set.Ioo (0 : ℝ) (2 * π) :=
    ⟨lt_of_le_of_ne hθ₀mem.1 (Ne.symm h00), lt_of_le_of_ne hθ₀mem.2 h2p⟩
  have hloc : IsLocalMin QOU.Archimedean.Cl_2 θ₀ :=
    hmin.isLocalMin (Icc_mem_nhds hint.1 hint.2)
  have hd := QOU.Knot.hasDerivAt_cl_2 hint.1 hint.2
  have hderiv0 : -Real.log (2 * Real.sin (θ₀ / 2)) = 0 := by
    rw [← hd.deriv]
    exact hloc.deriv_eq_zero
  have hspos : 0 < 2 * Real.sin (θ₀ / 2) := by
    have := Real.sin_pos_of_pos_of_lt_pi
      (by linarith [hint.1] : 0 < θ₀ / 2) (by linarith [hint.2] : θ₀ / 2 < π)
    linarith
  have hcrit : 2 * Real.sin (θ₀ / 2) = 1 := by
    have hlog0 : Real.log (2 * Real.sin (θ₀ / 2)) = 0 := by linarith
    have h := congrArg Real.exp hlog0
    rwa [Real.exp_log hspos, Real.exp_zero] at h
  rcases (saddle_critical_point_two_pi hint.1 hint.2).mp hcrit with h13 | h53'
  · exfalso
    rw [h13] at hneg
    linarith [QOU.Knot.Cl_2_pi_div_three_pos]
  · have hval : QOU.Archimedean.Cl_2 θ₀ = -QOU.Archimedean.Cl_2 (π / 3) := by
      rw [h53']; exact h53
    calc -QOU.Archimedean.Cl_2 (π / 3) = QOU.Archimedean.Cl_2 θ₀ := hval.symm
      _ ≤ QOU.Archimedean.Cl_2 θ := hmin hθ

/-- **E3 corollary — the saddle max bound.** For `x ∈ [0,1]`,
    `−2Cl₂(2πx) ≤ 2Cl₂(π/3)`: the continuum saddle functional is bounded by the
    figure-eight volume `Vol(4₁) = 2Cl₂(π/3)`. -/
theorem neg_two_Cl_2_le {x : ℝ} (hx : x ∈ Set.Icc (0 : ℝ) 1) :
    -2 * QOU.Archimedean.Cl_2 (2 * π * x) ≤ 2 * QOU.Archimedean.Cl_2 (π / 3) := by
  have hpi := Real.pi_pos
  have h := neg_Cl_2_pi_div_three_le (θ := 2 * π * x)
    ⟨by nlinarith [hx.1], by nlinarith [hx.2]⟩
  linarith

/-- **E3 corollary — the saddle max is attained at `x = 5/6`.**
    `−2Cl₂(2π·(5/6)) = 2Cl₂(π/3)` — the Kashaev saddle location. -/
theorem neg_two_Cl_2_at_five_sixths :
    -2 * QOU.Archimedean.Cl_2 (2 * π * (5 / 6)) = 2 * QOU.Archimedean.Cl_2 (π / 3) := by
  have h := QOU.Knot.Cl_2_two_pi_sub (π / 3)
  rw [show 2 * π * (5 / 6 : ℝ) = 2 * π - π / 3 by ring, h]
  ring

end QOU.Knot.FigureEightVolume
