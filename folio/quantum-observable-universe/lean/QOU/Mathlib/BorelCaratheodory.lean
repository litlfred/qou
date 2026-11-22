/-
  Borel-Carathéodory inequality — a Mathlib v4.24.0 gap.

  WHAT IT SAYS. For `f` holomorphic on `ball 0 R` with `f 0 = 0` and a ONE-SIDED
  bound on the real part, `Re f ≤ M`, one gets a TWO-SIDED bound on the modulus:

      ‖f z‖ ≤ 2 M r / (R - r)     for ‖z‖ ≤ r < R.

  That trade — real part in, modulus out — is what makes it load-bearing for
  Hadamard factorization (PI-5 of `QOU.Mathlib.HadamardFactorization`, bean
  qou-v4if). There, `f` is a branch of `log` of an entire function of finite
  order; the growth hypothesis bounds `Re log = log‖·‖` from above and says
  nothing about the modulus of the log itself, which is what the polynomial
  degree bound on `g` needs.

  WHY IT IS HERE AND NOT USED FROM MATHLIB. Mathlib v4.24.0 has the Schwarz
  lemma (`Complex.dist_le_div_mul_dist_of_mapsTo_ball`), the maximum modulus
  principle, Jensen's formula (`MeromorphicOn.circleAverage_log_norm`) and the
  Nevanlinna value-distribution cone (`ValueDistribution.logCounting`,
  `.proximity`, `.characteristic`). It does NOT have Borel-Carathéodory —
  checked by enumerating the environment, not by grepping filenames.

  THE PROOF, AND ONE DEVIATION FROM THE TEXTBOOK. The standard route sets
  `g = f/(2M - f)`, notes `‖g‖ ≤ 1`, applies Schwarz to get `‖g z‖ ≤ ‖z‖/R`, and
  then INVERTS the Möbius map, `f = 2Mg/(1+g)`, bounding `‖1+g‖ ≥ 1 - ‖g‖`.
  The inversion is avoidable. From `g·(2M - f) = f` alone,

      ‖f‖ = ‖g‖·‖2M - f‖ ≤ ‖g‖·(2M + ‖f‖)

  by the triangle inequality, and rearranging with `‖g‖ < 1` gives
  `‖f‖ ≤ 2M‖g‖/(1 - ‖g‖)` directly. No Möbius algebra, no division by `1 + g`.

  A SECOND DEVIATION, forced. Mathlib's Schwarz lemma wants `MapsTo f (ball c R)
  (ball (f c) R₂)` — an OPEN ball, so a STRICT bound. `Re f ≤ M` gives `‖g‖ ≤ 1`,
  not `< 1`. Rather than strengthening the hypothesis, the proof applies Schwarz
  with radius `1 + ε` for every `ε > 0` and takes the limit. That keeps the
  hypothesis at `≤`, which is what callers can actually supply.

  SCOPE — read before citing. The hypothesis here is `Re f ≤ M` on the whole
  BALL, not merely on the circle `‖z‖ = R`. The classical statement assumes the
  circle bound and upgrades it by the maximum principle for harmonic functions.
  That upgrade is NOT proved here (Mathlib has the maximum modulus principle for
  holomorphic functions, not obviously the harmonic-function version needed for
  `Re f`), and the ball hypothesis is what the Hadamard application supplies
  anyway. Stated honestly rather than assumed away.

  -- Ref: [leitner2026] Borel-Carathéodory; Titchmarsh, *The Theory of Functions*,
     2nd ed., §5.5; Conway, *Functions of One Complex Variable I*, XI.§1.
-/
import Mathlib.Analysis.Complex.Schwarz
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

namespace QOU.Mathlib.BorelCaratheodory

open Metric

/-- If `Re w ≤ M` and `0 < M` then `‖w‖ ≤ ‖2M - w‖`.

This is the engine: it converts a ONE-SIDED bound on the real part into a
TWO-SIDED bound on the modulus of the Möbius transform. Geometrically, the
half-plane `Re w ≤ M` is exactly the set of points at least as close to `0` as
to `2M`. -/
theorem norm_le_norm_two_mul_sub {M : ℝ} (hM : 0 < M) {w : ℂ} (hw : w.re ≤ M) :
    ‖w‖ ≤ ‖(2 * M : ℂ) - w‖ := by
  have h1 : ‖w‖ ^ 2 = w.re ^ 2 + w.im ^ 2 := by
    rw [Complex.sq_norm, Complex.normSq_apply]; ring
  have h2 : ‖(2 * M : ℂ) - w‖ ^ 2 = (2 * M - w.re) ^ 2 + w.im ^ 2 := by
    rw [Complex.sq_norm, Complex.normSq_apply]; simp; ring
  have key : w.re ^ 2 ≤ (2 * M - w.re) ^ 2 := by nlinarith [sq_nonneg (w.re - M)]
  have hsq : ‖w‖ ^ 2 ≤ ‖(2 * M : ℂ) - w‖ ^ 2 := by rw [h1, h2]; linarith
  exact (pow_le_pow_iff_left₀ (norm_nonneg _) (norm_nonneg _) two_ne_zero).mp hsq

/-- `2M - w ≠ 0` whenever `Re w ≤ M` and `0 < M`: its real part is at least `M`. -/
theorem two_mul_sub_ne_zero {M : ℝ} (hM : 0 < M) {w : ℂ} (hw : w.re ≤ M) :
    (2 * M : ℂ) - w ≠ 0 := by
  intro h
  have : ((2 * M : ℂ) - w).re = 0 := by rw [h]; simp
  simp only [Complex.sub_re, Complex.mul_re] at this
  simp at this
  linarith

/-- **Borel-Carathéodory inequality.** A one-sided bound on the real part of a
holomorphic `f` with `f 0 = 0` yields a two-sided bound on its modulus strictly
inside the disc.

No `0 ≤ r` hypothesis is needed: for `r < 0` the hypothesis `‖z‖ ≤ r` is
unsatisfiable, and the proof never case-splits on the sign. -/
theorem norm_le_of_re_le {R M r : ℝ} {f : ℂ → ℂ}
    (hR : 0 < R) (hM : 0 < M) (hrR : r < R)
    (hd : DifferentiableOn ℂ f (ball 0 R)) (h0 : f 0 = 0)
    (hre : ∀ w ∈ ball (0 : ℂ) R, (f w).re ≤ M)
    {z : ℂ} (hz : ‖z‖ ≤ r) :
    ‖f z‖ ≤ 2 * M * r / (R - r) := by
  have hzR : z ∈ ball (0 : ℂ) R := by
    simp only [mem_ball, dist_zero_right]; linarith
  have h0R : (0 : ℂ) ∈ ball (0 : ℂ) R := by simp [hR]
  set g : ℂ → ℂ := fun w => f w / ((2 * M : ℂ) - f w) with hgdef
  have hne : ∀ w ∈ ball (0 : ℂ) R, (2 * M : ℂ) - f w ≠ 0 :=
    fun w hw => two_mul_sub_ne_zero hM (hre w hw)
  have hg0 : g 0 = 0 := by simp [hgdef, h0]
  have hgle : ∀ w ∈ ball (0 : ℂ) R, ‖g w‖ ≤ 1 := by
    intro w hw
    rw [hgdef]
    simp only [norm_div]
    exact div_le_one_of_le₀ (norm_le_norm_two_mul_sub hM (hre w hw)) (norm_nonneg _)
  have hgdiff : DifferentiableOn ℂ g (ball 0 R) := by
    apply DifferentiableOn.div hd
    · exact (differentiableOn_const _).sub hd
    · exact hne
  -- Schwarz at radius `1 + ε`, then `ε → 0`.
  have hschwarz : ‖g z‖ ≤ ‖z‖ / R := by
    have step : ∀ ε : ℝ, 0 < ε → ‖g z‖ ≤ (1 + ε) / R * ‖z‖ := by
      intro ε hε
      have hmaps : Set.MapsTo g (ball 0 R) (ball (g 0) (1 + ε)) := by
        intro w hw
        simp only [mem_ball, hg0, dist_zero_right]
        exact lt_of_le_of_lt (hgle w hw) (by linarith)
      have := Complex.dist_le_div_mul_dist_of_mapsTo_ball hgdiff hmaps hzR
      simpa [hg0, dist_zero_right] using this
    refine le_of_forall_pos_le_add ?_
    intro δ hδ
    have hpos : 0 < ‖z‖ / R + 1 := by positivity
    have hε : 0 < δ / (‖z‖ / R + 1) := by positivity
    have h := step _ hε
    have hexp : (1 + δ / (‖z‖ / R + 1)) / R * ‖z‖
        = ‖z‖ / R + (δ / (‖z‖ / R + 1)) * (‖z‖ / R) := by
      field_simp
    rw [hexp] at h
    refine h.trans (add_le_add_left ?_ _)
    rw [div_mul_eq_mul_div, div_le_iff₀ hpos]
    nlinarith [norm_nonneg z, hR.le, div_nonneg (norm_nonneg z) hR.le]
  -- `‖g z‖ ≤ r / R < 1`, then invert WITHOUT the Möbius map.
  have hgr : ‖g z‖ ≤ r / R := hschwarz.trans (by gcongr)
  have hlt1 : ‖g z‖ < 1 := lt_of_le_of_lt hgr ((div_lt_one hR).mpr hrR)
  have hkey : g z * ((2 * M : ℂ) - f z) = f z := by
    rw [hgdef]; field_simp [hne z hzR]
  have hnorm : ‖f z‖ = ‖g z‖ * ‖(2 * M : ℂ) - f z‖ := by
    rw [← norm_mul, hkey]
  have htri : ‖(2 * M : ℂ) - f z‖ ≤ 2 * M + ‖f z‖ := by
    refine (norm_sub_le _ _).trans (le_of_eq ?_)
    simp [abs_of_pos hM]
  have hbound : ‖f z‖ * (1 - ‖g z‖) ≤ 2 * M * ‖g z‖ := by
    have := mul_le_mul_of_nonneg_left htri (norm_nonneg (g z))
    nlinarith [norm_nonneg (f z), norm_nonneg (g z)]
  have hRr : 0 < R - r := by linarith
  have hGR : ‖g z‖ * R ≤ r := (le_div_iff₀ hR).mp hgr
  rw [le_div_iff₀ hRr]
  calc ‖f z‖ * (R - r) ≤ ‖f z‖ * (R - ‖g z‖ * R) := by
        nlinarith [norm_nonneg (f z)]
    _ = R * (‖f z‖ * (1 - ‖g z‖)) := by ring
    _ ≤ R * (2 * M * ‖g z‖) := mul_le_mul_of_nonneg_left hbound hR.le
    _ = 2 * M * (‖g z‖ * R) := by ring
    _ ≤ 2 * M * r := mul_le_mul_of_nonneg_left hGR (by linarith)

/-- Non-vacuity witness: the hypotheses are simultaneously satisfiable with a
nontrivial conclusion. Take `f = id`, `R = 1`, `M = 1`, `r = 1/2`; the bound
gives `‖z‖ ≤ 2`, which is weaker than `‖z‖ ≤ 1/2` — as it must be, since
Borel-Carathéodory is not sharp for this `f`. -/
example {z : ℂ} (hz : ‖z‖ ≤ 1 / 2) : ‖z‖ ≤ 2 * 1 * (1 / 2) / (1 - 1 / 2) := by
  have := norm_le_of_re_le (R := 1) (M := 1) (r := 1 / 2) (f := id)
    one_pos one_pos (by norm_num) differentiableOn_id rfl
    (fun w hw => by
      simp only [id]
      have : ‖w‖ < 1 := by simpa [dist_zero_right] using hw
      exact le_trans (Complex.re_le_norm w) this.le) hz
  simpa using this

end QOU.Mathlib.BorelCaratheodory
