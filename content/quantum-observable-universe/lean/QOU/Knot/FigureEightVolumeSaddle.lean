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

end QOU.Knot.FigureEightVolume
