/-
  **The Mahler measure of a linear factor** — the cornerstone of the Jensen form.

  Bean `qou-4lbh`.  ⚠ Mathlib-style, Mathlib imports only, no QOU dependency: liftable
  verbatim.

  ═══ ⚠ THIS REVERSES A RECOMMENDATION ═══

  `qou-4lbh` recorded that the last open step of Roth's lemma — bounding the heights of the
  factors `φₖ, ψₖ` of a separated `P = ∑ₖ φₖ(x)ψₖ(y)` — needs Gelfond's inequality, and that
  the choice was between **filling Mathlib's missing Mahler bridges upstream** and a
  **bare-hands Gelfond inequality on `ℤ[X]`**.  The recommendation given was bare-hands, to
  avoid `ℂ[X]` and circle averages.

  **That was the wrong call, and measuring says so.**  Two things:

  * Gelfond's standard proof *goes through* the Mahler measure.  "Bare-hands" is not a
    shortcut around it; it is a re-derivation of it.
  * Mathlib already has the hard analytic content —
    `circleAverage_log_norm_sub_const_eq_posLog`, i.e. Jensen's formula for a single root.
    What was missing is only its connection to `mahlerMeasure`, which is the one theorem
    below.

  So the upstream route is much cheaper than it looked.  What remains for the Jensen form
  `M(P) = ‖lead P‖ · ∏ max(1, ‖root‖)` is the factorization of a complex polynomial into
  linear factors together with `mahlerMeasure_mul`, both of which Mathlib has.

  ═══ WHAT THIS DOES NOT YET GIVE ═══

  ⚠ The Jensen form is one of *two* bridges, and neither is finished here.

  * **The Jensen form** `M(P) = ‖lead P‖ · ∏ max(1, ‖root‖)`.  The single-root case is
    `mahlerMeasure_X_sub_C` below; the product is still to be assembled.
  * **The coefficient bridge.**  `mahlerMeasure_le_max_one_sum_norm_coeff` below gives
    `M(p) ≤ max(1, ‖p‖₁)`.  ⚠ **That is weaker than Landau's inequality and must not be
    cited as it.**  Landau is `M(P) ≤ ‖P‖₂ ≤ √(deg+1) · H(P)`, proved through Parseval; the
    bound below goes through the crude sup bound on the circle, and `‖p‖₁ ≤ (deg+1) · H(p)`
    loses a factor `√(deg+1)` against it.

    It is nevertheless enough downstream.  Gelfond then reads `∏ H(pᵢ) ≤ 2^{deg}(deg+1)H(p)`
    rather than `2^{deg}√(deg+1)H(p)`, and that extra polynomial factor is invisible beside
    the exponential constants Roth's lemma already carries.
-/
import Mathlib.Analysis.Polynomial.MahlerMeasure
import Mathlib.Analysis.SpecialFunctions.Integrals.PosLogEqCircleAverage

open Real Finset

namespace Polynomial

/-- **The Mahler measure of a linear factor:** `M(X − a) = max(1, ‖a‖)`.

This is Jensen's formula for a single root.  Mathlib supplies the analytic content
(`circleAverage_log_norm_sub_const_eq_posLog`) but does not connect it to `mahlerMeasure`. -/
theorem mahlerMeasure_X_sub_C (a : ℂ) :
    (X - C a : ℂ[X]).mahlerMeasure = max 1 ‖a‖ := by
  have hne : (X - C a : ℂ[X]) ≠ 0 := X_sub_C_ne_zero a
  have hpos : (0 : ℝ) < max 1 ‖a‖ := lt_of_lt_of_le one_pos (le_max_left _ _)
  have hlog : (X - C a : ℂ[X]).logMahlerMeasure = Real.log (max 1 ‖a‖) := by
    rw [logMahlerMeasure_def]
    have heval : (fun x : ℂ => Real.log ‖eval x (X - C a : ℂ[X])‖)
        = fun x : ℂ => Real.log ‖x - a‖ := by
      funext x
      simp
    rw [heval, circleAverage_log_norm_sub_const_eq_posLog,
      posLog_eq_log_max_one (norm_nonneg a)]
  rw [mahlerMeasure, if_pos hne, hlog, Real.exp_log hpos]

/-! ### A coefficient bound

The direction that turns a Mahler bound into a bound on coefficients.  See the ⚠ in the
module header: this is *not* Landau's inequality, only a cruder cousin of it. -/

/-- On the unit circle a polynomial is bounded by the sum of the norms of its
coefficients. -/
theorem norm_eval_le_sum_norm_coeff {p : ℂ[X]} {z : ℂ} (hz : ‖z‖ = 1) :
    ‖p.eval z‖ ≤ ∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖ := by
  rw [eval_eq_sum_range]
  refine le_trans (norm_sum_le _ _) (le_of_eq (Finset.sum_congr rfl fun i _ => ?_))
  rw [norm_mul, norm_pow, hz, one_pow, mul_one]

/-- **A Landau-*type* bound:** `M(p) ≤ max(1, ‖p‖₁)`.

⚠ Weaker than Landau's inequality — see the module header.  This is the sup bound on the
circle, `M(p) = exp ∫ log‖p‖ ≤ sup‖p‖ ≤ ‖p‖₁`, not the Parseval one.

⚠ **The `max 1` is not slack, it is forced.**  The pointwise step is `log ‖p(z)‖ ≤ log S`
with `S = ‖p‖₁`, and that **fails** at a zero of `p` on the unit circle when `S < 1`:
Mathlib's `Real.log 0 = 0`, which exceeds `log S < 0`.  Bounding by `max 1 S` makes the
pointwise inequality hold at every point of the circle and so avoids an a.e. argument.

For a non-zero **integer** polynomial the distinction vanishes, since the leading
coefficient alone contributes at least one — that is `mahlerMeasure_le_sum_int`. -/
theorem mahlerMeasure_le_max_one_sum_norm_coeff (p : ℂ[X]) :
    p.mahlerMeasure ≤ max 1 (∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖) := by
  classical
  set S := ∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖ with hS
  have hmax : (0 : ℝ) < max 1 S := lt_of_lt_of_le one_pos (le_max_left _ _)
  by_cases hp : p = 0
  · simp [hp, mahlerMeasure_zero, le_of_lt hmax]
  have hci : CircleIntegrable (fun z : ℂ => log ‖p.eval z‖) 0 1 := by
    rw [circleIntegrable_def]
    exact p.intervalIntegrable_mahlerMeasure
  have hbound : ∀ z ∈ Metric.sphere (0 : ℂ) |(1 : ℝ)|,
      log ‖p.eval z‖ ≤ log (max 1 S) := by
    intro z hz
    have hz1 : ‖z‖ = 1 := by simpa using hz
    rcases eq_or_lt_of_le (norm_nonneg (p.eval z)) with h0 | h0
    · -- `p` vanishes at `z`; here `Real.log 0 = 0`, and `0 ≤ log (max 1 S)`.
      rw [← h0, Real.log_zero]
      exact Real.log_nonneg (le_max_left _ _)
    · exact Real.log_le_log h0
        (le_trans (norm_eval_le_sum_norm_coeff hz1) (le_max_right _ _))
  have hlog : p.logMahlerMeasure ≤ log (max 1 S) := by
    rw [logMahlerMeasure_def]
    exact circleAverage_mono_on_of_le_circle hci hbound
  rw [mahlerMeasure, if_pos hp]
  calc rexp p.logMahlerMeasure ≤ rexp (log (max 1 S)) := Real.exp_le_exp.mpr hlog
    _ = max 1 S := Real.exp_log hmax

/-- When the coefficient sum is itself at least one, the `max` drops away. -/
theorem mahlerMeasure_le_sum_norm_coeff {p : ℂ[X]}
    (h : 1 ≤ ∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖) :
    p.mahlerMeasure ≤ ∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖ :=
  le_trans (mahlerMeasure_le_max_one_sum_norm_coeff p) (max_le h le_rfl)

/-- A non-zero integer polynomial has coefficient sum at least one: its leading coefficient
is a non-zero integer, hence of absolute value at least one, and every other term of the sum
is non-negative. -/
theorem one_le_sum_norm_coeff_map_int {q : ℤ[X]} (hq : q ≠ 0) :
    1 ≤ ∑ i ∈ range ((q.map (Int.castRingHom ℂ)).natDegree + 1),
      ‖(q.map (Int.castRingHom ℂ)).coeff i‖ := by
  classical
  have hinj : Function.Injective (Int.castRingHom ℂ) := fun a b h => by simpa using h
  have hdeg : (q.map (Int.castRingHom ℂ)).natDegree = q.natDegree :=
    natDegree_map_eq_of_injective hinj q
  have hmem : q.natDegree ∈ range ((q.map (Int.castRingHom ℂ)).natDegree + 1) := by
    rw [hdeg]; exact self_mem_range_succ _
  have hlead : (1 : ℝ) ≤ ‖(q.map (Int.castRingHom ℂ)).coeff q.natDegree‖ := by
    rw [coeff_map]
    have : q.leadingCoeff ≠ 0 := leadingCoeff_ne_zero.mpr hq
    have h1 : (1 : ℤ) ≤ |q.leadingCoeff| := Int.one_le_abs (by omega)
    simpa [Int.cast_abs] using (by exact_mod_cast h1 : (1 : ℝ) ≤ |(q.leadingCoeff : ℝ)|)
  refine le_trans hlead (Finset.single_le_sum (f := fun i =>
    ‖(q.map (Int.castRingHom ℂ)).coeff i‖) (fun i _ => norm_nonneg _) hmem)

/-- **The coefficient bound over `ℤ`.**  For a non-zero integer polynomial, the Mahler
measure of its complex image is at most the sum of the absolute values of its coefficients.

This is the form the Roth's-lemma height bookkeeping consumes: over `ℤ` the `max 1` of
`mahlerMeasure_le_max_one_sum_norm_coeff` disappears.  ⚠ Still not Landau — see the
module header. -/
theorem mahlerMeasure_le_sum_int {q : ℤ[X]} (hq : q ≠ 0) :
    (q.map (Int.castRingHom ℂ)).mahlerMeasure
      ≤ ∑ i ∈ range ((q.map (Int.castRingHom ℂ)).natDegree + 1),
        ‖(q.map (Int.castRingHom ℂ)).coeff i‖ :=
  mahlerMeasure_le_sum_norm_coeff (one_le_sum_norm_coeff_map_int hq)

/-! ### Next

1. **The Jensen form** `M(P) = ‖lead P‖ · ∏ max(1, ‖root‖)`.  With `mahlerMeasure_X_sub_C`,
   `mahlerMeasure_mul`, and the factorization of a complex polynomial into linear factors,
   this is assembly rather than analysis.
2. **`H(p) ≤ 2^{deg p} · M(p)`** — the *reverse* bridge, which follows from the Jensen form
   by Vieta.  Nothing above supplies this direction, and Gelfond needs both.
3. **Gelfond**, from (1)–(2) together with `mahlerMeasure_le_sum_int`, and then the height
   control on the factors `φₖ, ψₖ` that the induction step of Roth's lemma needs.

Sharpening `mahlerMeasure_le_max_one_sum_norm_coeff` to Landau proper (`M(p) ≤ ‖p‖₂`, via
Parseval and Jensen's inequality for `exp`) is optional: the lost `√(deg+1)` is invisible
downstream, so this is worth doing only as an upstream contribution. -/

end Polynomial
