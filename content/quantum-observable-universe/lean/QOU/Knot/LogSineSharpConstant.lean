/-
# L4-1 sharp constant, step 3 (bean qou-shrp)

Applies the first Euler–Maclaurin correction (`EulerMaclaurinFirst.lean`) to
the smooth part `φ(x) = log(2 sin x / x)` of the log-sine cell defect.  The
E–M bracket needs `φ′` **antitone**, which is what this file establishes:

    φ′(x) = cot x − 1/x,      φ″(x) = 1/x² − 1/sin²x  <  0  on (0, π),

the inequality being just `sin x < x`.  Antitonicity then comes from the
standard derivative test on any `[a, b] ⊆ (0, π)`.

**Route note (honest scoping).**  The bean's step-3 plan routed through
`phiSinc x = log 2 + log (sinc x)` so that `φ` would be differentiable at the
closed endpoint `0`.  That turns out to be unnecessary *for this assembly*:
the `i = 0` cell never needs a derivative — it is already squeezed between
`h·(φ(h) − log 2)` and `0` by `LogSineSmoothPart.smooth_defect_squeeze`, and
that bracket collapses as `h → 0`.  So the E–M machinery is applied only to
the interior cells `[h, nh]`, where `φ` is honestly smooth and no removable
singularity is crossed.

The `sinc` differentiability infra of step 1 therefore stands on its own
merits as upstreamable Mathlib material rather than as a dependency of this
file — recorded so nobody infers a false chain of necessity.
-/

import QOU.Knot.EulerMaclaurinFirst
import QOU.Knot.LogSineSmoothPart

namespace QOU.Knot.FigureEightVolume

open Real

/-- `φ′` as an explicit function, matching `hasDerivAt_phi`. -/
noncomputable def phiDeriv (x : ℝ) : ℝ :=
  (2 * Real.cos x) / (2 * Real.sin x) - x⁻¹

theorem hasDerivAt_phi' {x : ℝ} (h0 : 0 < x) (hπ : x < π) :
    HasDerivAt phi (phiDeriv x) x := hasDerivAt_phi h0 hπ

/-- `φ″(x) = 1/x² − 1/sin²x` on `(0, π)`. -/
theorem hasDerivAt_phiDeriv {x : ℝ} (h0 : 0 < x) (hπ : x < π) :
    HasDerivAt phiDeriv (x⁻¹ ^ 2 - (Real.sin x)⁻¹ ^ 2) x := by
  have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi h0 hπ
  have h2s : (2 : ℝ) * Real.sin x ≠ 0 := by positivity
  have hnum : HasDerivAt (fun t : ℝ => 2 * Real.cos t) (2 * (-Real.sin x)) x := by
    simpa using (Real.hasDerivAt_cos x).const_mul (2 : ℝ)
  have hden : HasDerivAt (fun t : ℝ => 2 * Real.sin t) (2 * Real.cos x) x := by
    simpa using (Real.hasDerivAt_sin x).const_mul (2 : ℝ)
  have hdiv := hnum.div hden h2s
  have hinv : HasDerivAt (fun t : ℝ => t⁻¹) (-(x ^ 2)⁻¹) x :=
    hasDerivAt_inv h0.ne'
  have hcomb := hdiv.sub hinv
  convert hcomb using 1
  have hpy : Real.sin x ^ 2 + Real.cos x ^ 2 = 1 := Real.sin_sq_add_cos_sq x
  field_simp
  nlinarith [hpy]

/-- **`φ′` is antitone** on any closed subinterval of `(0, π)` — the
    hypothesis the Euler–Maclaurin bracket needs.  `φ″ = 1/x² − 1/sin²x < 0`
    because `sin x < x`. -/
theorem continuousOn_phiDeriv {a b : ℝ} (ha : 0 < a) (hb : b < π) :
    ContinuousOn phiDeriv (Set.Icc a b) := by
  refine ContinuousOn.sub ?_ ?_
  · refine ContinuousOn.div ?_ ?_ ?_
    · exact (continuous_const.mul Real.continuous_cos).continuousOn
    · exact (continuous_const.mul Real.continuous_sin).continuousOn
    · intro x hx
      have hs : 0 < Real.sin x :=
        Real.sin_pos_of_pos_of_lt_pi (lt_of_lt_of_le ha hx.1)
          (lt_of_le_of_lt hx.2 hb)
      positivity
  · exact continuousOn_inv₀.mono (by
      intro x hx
      exact ne_of_gt (lt_of_lt_of_le ha hx.1))

theorem phiDeriv_antitoneOn {a b : ℝ} (ha : 0 < a) (hb : b < π) :
    AntitoneOn phiDeriv (Set.Icc a b) := by
  rcases le_or_gt a b with hab | hba
  · refine antitoneOn_of_deriv_nonpos (convex_Icc _ _) ?_ ?_ ?_
    · exact continuousOn_phiDeriv ha hb
    · rw [interior_Icc]
      intro x hx
      exact (hasDerivAt_phiDeriv (lt_of_lt_of_le ha hx.1.le)
        (lt_trans hx.2 hb)).differentiableAt.differentiableWithinAt
    · rw [interior_Icc]
      intro x hx
      have h0x : 0 < x := lt_of_lt_of_le ha hx.1.le
      have hxπ : x < π := lt_trans hx.2 hb
      rw [(hasDerivAt_phiDeriv h0x hxπ).deriv]
      have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi h0x hxπ
      have hlt : Real.sin x < x := Real.sin_lt h0x
      have hsq : Real.sin x ^ 2 < x ^ 2 := by nlinarith
      have h1 : x⁻¹ ^ 2 = (x ^ 2)⁻¹ := by rw [inv_pow]
      have h2 : (Real.sin x)⁻¹ ^ 2 = (Real.sin x ^ 2)⁻¹ := by rw [inv_pow]
      have hspos : (0:ℝ) < Real.sin x ^ 2 := by positivity
      rw [h1, h2, sub_nonpos]
      gcongr
  · rw [Set.Icc_eq_empty (by linarith)]
    intro u hu
    exact absurd hu (Set.notMem_empty u)

/-- **Step 3 — the Euler–Maclaurin bracket for `φ` on the interior cells.**
    On the grid `x_i = i·h` with `nh < π`, the interior-cell defect sum
    (`i = 1 … n−1`, i.e. the cells covering `[h, nh]`) is bracketed by `h²/2`
    times the two endpoint Riemann sums of `φ′`:

        (h²/2)·Σ φ′(x_{i+1})  ≤  Σ ∫_{cell_i} (φ(x_{i+1}) − φ(u)) du
                              ≤  (h²/2)·Σ φ′(x_i).

    Both envelopes are `(h/2)` times a Riemann sum of `φ′` over `[h, nh]`, so
    both carry the first Euler–Maclaurin term `(h/2)(φ(nh) − φ(h))` — the `½`
    the antitone squeeze could not pin.  The excluded `i = 0` cell needs no
    derivative: `smooth_defect_squeeze` already brackets it between
    `h·(φ(h) − log 2)` and `0`. -/
theorem phi_interior_bracket {h : ℝ} (hh : 0 < h) {n : ℕ}
    (hnπ : (n : ℝ) * h < π) :
    h ^ 2 / 2 * (∑ i ∈ Finset.Ico 1 n, phiDeriv (((i : ℝ) + 1) * h))
        ≤ ∑ i ∈ Finset.Ico 1 n,
            ∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (phi (((i : ℝ) + 1) * h) - phi u)
      ∧ (∑ i ∈ Finset.Ico 1 n,
            ∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (phi (((i : ℝ) + 1) * h) - phi u))
        ≤ h ^ 2 / 2 * (∑ i ∈ Finset.Ico 1 n, phiDeriv ((i : ℝ) * h)) := by
  have hcell : ∀ i ∈ Finset.Ico 1 n,
      h ^ 2 / 2 * phiDeriv (((i : ℝ) + 1) * h)
          ≤ (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (phi (((i : ℝ) + 1) * h) - phi u))
        ∧ (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (phi (((i : ℝ) + 1) * h) - phi u))
          ≤ h ^ 2 / 2 * phiDeriv ((i : ℝ) * h) := by
    intro i hi
    obtain ⟨hi1, hi2⟩ := Finset.mem_Ico.mp hi
    have hipos : (0 : ℝ) < (i : ℝ) * h := by
      have : (1 : ℝ) ≤ (i : ℝ) := by exact_mod_cast hi1
      nlinarith
    have hup : (i : ℝ) * h + h < π := by
      have hin : ((i : ℝ) + 1) ≤ (n : ℝ) := by exact_mod_cast hi2
      nlinarith
    have heq : (i : ℝ) * h + h = ((i : ℝ) + 1) * h := by ring
    have hres := cell_defect_bracket (f := phi) (f' := phiDeriv)
      (a := (i : ℝ) * h) hh
      (fun x hx => hasDerivAt_phi' (lt_of_lt_of_le hipos hx.1)
        (lt_of_le_of_lt hx.2 hup))
      (phiDeriv_antitoneOn hipos hup)
    rw [heq] at hres
    exact hres
  constructor
  · rw [Finset.mul_sum]
    exact Finset.sum_le_sum fun i hi => (hcell i hi).1
  · rw [Finset.mul_sum]
    exact Finset.sum_le_sum fun i hi => (hcell i hi).2

/-! ### Convergence: from the two envelopes to the Euler–Maclaurin term

`phi_interior_bracket` brackets the interior-cell defect sum `S` between
`(h²/2)·R` and `(h²/2)·L`, where

    L = Σ_{i=1}^{n−1} φ′(x_i),      R = Σ_{i=1}^{n−1} φ′(x_{i+1})

are the left- and right-endpoint Riemann sums of `φ′` over `[h, nh]`.  Two
telescopes turn that into the sharp statement:

* the same antitone MVT bracket applied to `φ` itself gives
  `h·R ≤ φ(nh) − φ(h) ≤ h·L` — so `φ(nh) − φ(h)` is trapped between the very
  same two sums (`phi_riemann_sum_bracket`);
* `L − R = φ′(h) − φ′(nh)` telescopes exactly (`sum_phiDeriv_telescope`).

Combining, `S` and `(h/2)·(φ(nh) − φ(h))` differ by at most
`(h²/2)·(φ′(h) − φ′(nh))`.  Since `φ′(x) = cot x − 1/x → 0` as `x → 0⁺` and
`φ′(nh) → φ′(rπ)` is finite, that error is `O(h²)`, while the identified term
is `(h/2)·(φ(nh) − φ(h))` — van der Veen's missing `½`.  No limit is taken
here: the statement is a finite, effective inequality valid for every
`0 < h` and every `n ≥ 1` with `nh < π`.
-/

/-- Telescoping a difference over `Finset.Ico 1 n`. -/
theorem sum_Ico_one_telescope (G : ℕ → ℝ) {n : ℕ} (hn : 1 ≤ n) :
    ∑ i ∈ Finset.Ico 1 n, (G (i + 1) - G i) = G n - G 1 := by
  rw [Finset.sum_Ico_eq_sum_range]
  have hkey := Finset.sum_range_sub (fun j => G (1 + j)) (n - 1)
  have hshift : (∑ j ∈ Finset.range (n - 1), (G (1 + j + 1) - G (1 + j)))
      = ∑ j ∈ Finset.range (n - 1), (G (1 + (j + 1)) - G (1 + j)) :=
    Finset.sum_congr rfl fun j _ => by rw [Nat.add_assoc]
  rw [hshift, hkey]
  have hn1 : 1 + (n - 1) = n := by omega
  rw [hn1]

/-- **MVT bracket for `φ` on one cell** `[a, a+h] ⊆ (0, π)`: the increment is
    trapped between `h·φ′` at the two endpoints, `φ′` being antitone. -/
theorem phi_sub_cell_bracket {a h : ℝ} (hh : 0 < h) (ha : 0 < a)
    (hup : a + h < π) :
    h * phiDeriv (a + h) ≤ phi (a + h) - phi a
      ∧ phi (a + h) - phi a ≤ h * phiDeriv a := by
  have hres := sub_bracket_of_antitoneOn_deriv (f := phi) (f' := phiDeriv)
    (a := a) (b := a + h) (u := a)
    (fun x hx => hasDerivAt_phi' (lt_of_lt_of_le ha hx.1)
      (lt_of_le_of_lt hx.2 hup))
    (phiDeriv_antitoneOn ha hup) le_rfl (by linarith)
  simpa using hres

/-- **`φ(nh) − φ(h)` is trapped between the same two Riemann sums** that
    bracket the cell-defect sum.  This is what converts the Euler–Maclaurin
    envelopes into the identified term `(h/2)(φ(nh) − φ(h))`. -/
theorem phi_riemann_sum_bracket {h : ℝ} (hh : 0 < h) {n : ℕ} (hn : 1 ≤ n)
    (hnπ : (n : ℝ) * h < π) :
    h * (∑ i ∈ Finset.Ico 1 n, phiDeriv (((i : ℝ) + 1) * h))
        ≤ phi ((n : ℝ) * h) - phi h
      ∧ phi ((n : ℝ) * h) - phi h
        ≤ h * (∑ i ∈ Finset.Ico 1 n, phiDeriv ((i : ℝ) * h)) := by
  have hcell : ∀ i ∈ Finset.Ico 1 n,
      h * phiDeriv (((i : ℝ) + 1) * h)
          ≤ phi (((i : ℝ) + 1) * h) - phi ((i : ℝ) * h)
        ∧ phi (((i : ℝ) + 1) * h) - phi ((i : ℝ) * h)
          ≤ h * phiDeriv ((i : ℝ) * h) := by
    intro i hi
    obtain ⟨hi1, hi2⟩ := Finset.mem_Ico.mp hi
    have hipos : (0 : ℝ) < (i : ℝ) * h := by
      have : (1 : ℝ) ≤ (i : ℝ) := by exact_mod_cast hi1
      nlinarith
    have hup : (i : ℝ) * h + h < π := by
      have hin : ((i : ℝ) + 1) ≤ (n : ℝ) := by exact_mod_cast hi2
      nlinarith
    have heq : (i : ℝ) * h + h = ((i : ℝ) + 1) * h := by ring
    have hres := phi_sub_cell_bracket (a := (i : ℝ) * h) hh hipos hup
    rw [heq] at hres
    exact hres
  have htel : (∑ i ∈ Finset.Ico 1 n,
      (phi (((i : ℝ) + 1) * h) - phi ((i : ℝ) * h)))
        = phi ((n : ℝ) * h) - phi h := by
    have hg := sum_Ico_one_telescope (fun k : ℕ => phi ((k : ℝ) * h)) hn
    push_cast at hg
    simpa using hg
  constructor
  · rw [← htel, Finset.mul_sum]
    exact Finset.sum_le_sum fun i hi => (hcell i hi).1
  · rw [← htel, Finset.mul_sum]
    exact Finset.sum_le_sum fun i hi => (hcell i hi).2

/-- **The two Riemann sums differ by exactly the endpoint gap** — the
    telescope that makes the Euler–Maclaurin error `O(h²)` rather than `O(h)`. -/
theorem sum_phiDeriv_telescope {h : ℝ} {n : ℕ} (hn : 1 ≤ n) :
    (∑ i ∈ Finset.Ico 1 n, phiDeriv ((i : ℝ) * h))
        - ∑ i ∈ Finset.Ico 1 n, phiDeriv (((i : ℝ) + 1) * h)
      = phiDeriv h - phiDeriv ((n : ℝ) * h) := by
  have hg := sum_Ico_one_telescope (fun k : ℕ => phiDeriv ((k : ℝ) * h)) hn
  push_cast at hg
  rw [Finset.sum_sub_distrib] at hg
  simp only [one_mul] at hg
  linarith

/-- **L4-1 sharp constant (step 3, final form).**  The interior-cell smooth
    defect equals the first Euler–Maclaurin term to within `O(h²)`:

        | Σ_{i=1}^{n−1} ∫_{cell_i} (φ(x_{i+1}) − φ(u)) du
              −  (h/2)·(φ(nh) − φ(h)) |   ≤   (h²/2)·(φ′(h) − φ′(nh)).

    This is the `½` that `LogSineSmoothPart.smooth_defect_squeeze` provably
    cannot pin (measured: `computations/logsine_smooth_defect_constant.py`,
    where the scaled defect converges to the *midpoint* of the squeeze
    interval, whose width does not shrink).  Effective and hypothesis-light:
    valid for every `0 < h` and every `n ≥ 1` with `nh < π`; no limit is
    taken, and no modulus of continuity is carried. -/
theorem phi_smooth_defect_sharp {h : ℝ} (hh : 0 < h) {n : ℕ} (hn : 1 ≤ n)
    (hnπ : (n : ℝ) * h < π) :
    |(∑ i ∈ Finset.Ico 1 n,
        ∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
          (phi (((i : ℝ) + 1) * h) - phi u))
        - h / 2 * (phi ((n : ℝ) * h) - phi h)|
      ≤ h ^ 2 / 2 * (phiDeriv h - phiDeriv ((n : ℝ) * h)) := by
  obtain ⟨hS1, hS2⟩ := phi_interior_bracket hh hnπ
  obtain ⟨hI1, hI2⟩ := phi_riemann_sum_bracket hh hn hnπ
  have htel := sum_phiDeriv_telescope (h := h) hn
  have hhalf : (0 : ℝ) ≤ h / 2 := by linarith
  have e1 := mul_le_mul_of_nonneg_left hI1 hhalf
  have e2 := mul_le_mul_of_nonneg_left hI2 hhalf
  rw [← htel, abs_le]
  constructor <;> nlinarith [hS1, hS2, e1, e2]

end QOU.Knot.FigureEightVolume
