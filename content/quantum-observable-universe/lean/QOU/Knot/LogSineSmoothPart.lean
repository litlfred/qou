/-
# L4-1c(ii) — the smooth part is MONOTONE (bean qou-ph2s, epic qou-u1b5)

Last input of L4-1.  After the exact singular telescope (L4-1c(i)) the
whole remaining content of the second-order log-sine expansion is the
Riemann-sum defect of

    φ(x) := log(2 sin x / x) = log(2 sin x) − log x,   φ(0⁺) = log 2,

which the bean scoped as "a Lipschitz bound across the removable
singularity at 0", with `φ' = cot x − 1/x` (each term singular at 0, the
difference regular) as the expected obstacle.

**That obstacle is avoidable.**  The cell defects do not need a derivative
*bound* — they need a *sign*, and `φ` is strictly antitone on `(0, π)`.
Antitonicity comes from the single inequality `x·cos x < sin x`, proved
here from `ψ(x) = sin x − x·cos x` having `ψ(0) = 0` and
`ψ'(x) = x·sin x > 0`.  No behaviour of `φ` *at* `0` is ever needed: the
first cell is closed off instead by the elementary ceiling
`φ(u) ≤ log 2` (which is just `sin u ≤ u`).

So the pieces this file supplies are:

* `sin_sub_mul_cos_pos` — `x·cos x < sin x` on `(0, π)`;
* `strictAntiOn_phi` — `φ` strictly antitone on `(0, π)`, hence
  `φ(x_j) ≤ φ(u)` for every `u` in the cell `(x_{j−1}, x_j]`: each cell
  defect is `≤ 0`;
* `phi_le_log_two` — `φ(u) ≤ log 2` on `(0, π)`, the surrogate for the
  missing value at `0` that closes the first cell.

Together these squeeze the smooth half between `h·(φ(nh) − log 2)` and `0`
by telescoping — an `O(h)` two-sided bound with no derivative estimate
anywhere.
-/

/-
**REDUNDANT (2026-08-19) — L4-1's target was already proved on `main`, stronger,
before this file was written.**

`QOU.Knot.FigureEightVolume.kashaev_log_sum_asymptotic`
(`QOU/Knot/KashaevAsymptotic.lean`, on main since 2026-08-10, sorry-free) gives

    | ∑_{j=1}^{k} log(2 sin(jπ/N))
        − ( −(N/π)·Lob(kπ/N) + ½·log(2N·sin(kπ/N)) + (π/(12N))·cot(kπ/N) ) |
      ≤ 1/(144k²) + (7/12)(π/N)² + (π/N)²/(12·sin²(kπ/N))

— strictly stronger than the L4-1 target this file serves: it identifies the
`O(1/N)` term and its error is effective.  The decomposition L4-1 was organised
around is `KashaevEndpointSplit.sum_log_two_sin_split`, exact algebra with no
cell integrals and no telescope.

Kept, not deleted: the proofs here are correct and sorry-free.  **New
downstream work should cite `kashaev_log_sum_asymptotic`, not this file.**
Audit: `docs/audits/2026-08-19-l41-was-already-proved-on-main.md`.
-/

import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.Calculus.MeanValue
import QOU.Knot.Clausen

namespace QOU.Knot.FigureEightVolume

open Real

/-- The smooth part of the log-sine integrand, `φ(x) = log(2 sin x / x)`
    written as a difference (so no removable-singularity bookkeeping is
    needed; the value at `0` is never used). -/
noncomputable def phi (x : ℝ) : ℝ := Real.log (2 * Real.sin x) - Real.log x

/-- `x·cos x < sin x` on `(0, π)` — the single inequality behind `φ`'s
    monotonicity.  `ψ(x) = sin x − x·cos x` vanishes at `0` and has
    `ψ'(x) = x·sin x > 0` on the interval. -/
theorem sin_sub_mul_cos_pos {x : ℝ} (h0 : 0 < x) (hπ : x < π) :
    x * Real.cos x < Real.sin x := by
  have hpi := Real.pi_pos
  set ψ : ℝ → ℝ := fun t => Real.sin t - t * Real.cos t with hψ
  have hderiv : ∀ t : ℝ, HasDerivAt ψ (t * Real.sin t) t := by
    intro t
    have h1 : HasDerivAt Real.sin (Real.cos t) t := Real.hasDerivAt_sin t
    have h2 : HasDerivAt (fun s : ℝ => s * Real.cos s)
        (1 * Real.cos t + t * (-Real.sin t)) t :=
      (hasDerivAt_id t).mul (Real.hasDerivAt_cos t)
    have h3 := h1.sub h2
    convert h3 using 1
    ring
  have hmono : StrictMonoOn ψ (Set.Icc 0 π) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc _ _) ?_ ?_
    · exact (Continuous.sub Real.continuous_sin
        (continuous_id.mul Real.continuous_cos)).continuousOn
    · intro t ht
      rw [interior_Icc] at ht
      rw [(hderiv t).deriv]
      exact mul_pos ht.1 (Real.sin_pos_of_pos_of_lt_pi ht.1 ht.2)
  have h := hmono (Set.left_mem_Icc.mpr hpi.le)
    ⟨h0.le, hπ.le⟩ h0
  simp only [hψ, Real.sin_zero, zero_mul, sub_zero, sub_pos] at h
  linarith [h]

/-- `φ` has the expected derivative on `(0, π)`. -/
theorem hasDerivAt_phi {x : ℝ} (h0 : 0 < x) (hπ : x < π) :
    HasDerivAt phi
      ((2 * Real.cos x) / (2 * Real.sin x) - x⁻¹) x := by
  have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi h0 hπ
  have h2s : (2 : ℝ) * Real.sin x ≠ 0 := by positivity
  have hd1 : HasDerivAt (fun t : ℝ => 2 * Real.sin t) (2 * Real.cos x) x := by
    simpa using (Real.hasDerivAt_sin x).const_mul (2 : ℝ)
  have hlog2 : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log h0.ne'
  exact (hd1.log h2s).sub hlog2

/-- **`φ` is strictly antitone on `(0, π)`** — so every cell defect
    `φ(x_j) − φ(u)`, `u ≤ x_j`, is `≤ 0`.  This is the property that
    replaces the Lipschitz bound the bean expected to need. -/
theorem strictAntiOn_phi : StrictAntiOn phi (Set.Ioo 0 π) := by
  refine strictAntiOn_of_deriv_neg (convex_Ioo _ _) ?_ ?_
  · refine ContinuousOn.sub ?_ ?_
    · refine ContinuousOn.log ?_ ?_
      · exact (continuous_const.mul Real.continuous_sin).continuousOn
      · intro x hx
        have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx.1 hx.2
        positivity
    · exact Real.continuousOn_log.mono (by
        intro x hx
        exact ne_of_gt hx.1)
  · intro x hx
    rw [interior_Ioo] at hx
    rw [(hasDerivAt_phi hx.1 hx.2).deriv]
    have hs : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi hx.1 hx.2
    have hkey := sin_sub_mul_cos_pos hx.1 hx.2
    have hgoal : (2 * Real.cos x) / (2 * Real.sin x) < x⁻¹ := by
      rw [div_lt_iff₀ (by positivity : (0:ℝ) < 2 * Real.sin x),
        inv_mul_eq_div, lt_div_iff₀ hx.1]
      nlinarith [hkey]
    linarith [hgoal]

/-- The first-cell ceiling: `φ(u) ≤ log 2` on `(0, π)` — just `sin u ≤ u`.
    This stands in for the (unused) value `φ(0⁺) = log 2`. -/
theorem phi_le_log_two {u : ℝ} (h0 : 0 < u) (hπ : u < π) :
    phi u ≤ Real.log 2 := by
  have hs : 0 < Real.sin u := Real.sin_pos_of_pos_of_lt_pi h0 hπ
  have hlt : Real.sin u < u := Real.sin_lt h0
  unfold phi
  have h2 : Real.log (2 * Real.sin u) ≤ Real.log (2 * u) :=
    Real.log_le_log (by positivity) (by linarith)
  rw [Real.log_mul (by norm_num) h0.ne'] at h2
  linarith

/-! ## Assembly — the telescoping two-sided bound -/

/-- `φ` is interval-integrable everywhere: both halves are, unconditionally
    (`intervalIntegrable_log'` covers the singularity at `0`). -/
theorem intervalIntegrable_phi (a b : ℝ) :
    IntervalIntegrable phi MeasureTheory.volume a b := by
  unfold phi
  exact (intervalIntegrable_log_two_sin a b).sub
    intervalIntegral.intervalIntegrable_log'

/-- The cell ceiling: `log 2` for the first cell (whose left endpoint is the
    unusable `0`), the previous grid value thereafter. -/
noncomputable def phiExt (h : ℝ) (j : ℕ) : ℝ :=
  if j = 0 then Real.log 2 else phi ((j : ℝ) * h)

@[simp] theorem phiExt_zero (h : ℝ) : phiExt h 0 = Real.log 2 := by
  simp [phiExt]

theorem phiExt_succ (h : ℝ) (j : ℕ) :
    phiExt h (j + 1) = phi (((j : ℝ) + 1) * h) := by
  simp [phiExt]

/-- On each cell, `φ` stays under the cell ceiling — a.e., the single
    exception being `u = 0` in the first cell (where `φ`'s junk value is
    irrelevant). -/
theorem ae_phi_le_phiExt {h : ℝ} (hh : 0 < h) {i n : ℕ} (hi : i < n)
    (hnπ : (n : ℝ) * h < π) :
    ∀ᵐ u ∂(MeasureTheory.volume.restrict
        (Set.Icc ((i : ℝ) * h) (((i : ℝ) + 1) * h))),
      phi u ≤ phiExt h i := by
  have hpi := Real.pi_pos
  have hi1 : ((i : ℝ) + 1) * h ≤ (n : ℝ) * h := by
    have : ((i : ℝ) + 1) ≤ (n : ℝ) := by exact_mod_cast hi
    nlinarith
  have hnull : ∀ᵐ (u : ℝ), u ≠ 0 := by
    rw [MeasureTheory.ae_iff]
    simpa using (Real.volume_singleton (a := (0 : ℝ)))
  filter_upwards [MeasureTheory.ae_restrict_of_ae hnull,
    MeasureTheory.ae_restrict_mem measurableSet_Icc] with u hu0 humem
  obtain ⟨hu1, hu2⟩ := humem
  have hupos : 0 < u := by
    rcases Nat.eq_zero_or_pos i with hi0 | hi0
    · subst hi0
      simp only [Nat.cast_zero, zero_mul] at hu1
      exact lt_of_le_of_ne hu1 (Ne.symm hu0)
    · have : (0:ℝ) < (i : ℝ) * h := by
        have : (0:ℝ) < (i : ℝ) := by exact_mod_cast hi0
        positivity
      linarith
  have huπ : u < π := by linarith [hi1, hnπ]
  rcases Nat.eq_zero_or_pos i with hi0 | hi0
  · subst hi0
    rw [phiExt_zero]
    exact phi_le_log_two hupos huπ
  · have hine : i ≠ 0 := by omega
    have hxpos : (0:ℝ) < (i : ℝ) * h := by
      have : (0:ℝ) < (i : ℝ) := by exact_mod_cast hi0
      positivity
    have hxπ : (i : ℝ) * h < π := by nlinarith [hi1, hnπ]
    rw [phiExt, if_neg hine]
    rcases eq_or_lt_of_le hu1 with heq | hlt
    · rw [heq]
    · exact le_of_lt (strictAntiOn_phi ⟨hxpos, hxπ⟩ ⟨hupos, huπ⟩ hlt)

/-- **Per-cell two-sided bound.**  Each cell defect is `≤ 0` (antitonicity)
    and `≥ h·(φ(x_{i+1}) − ceiling_i)`. -/
theorem cell_defect_bounds {h : ℝ} (hh : 0 < h) {i n : ℕ} (hi : i < n)
    (hnπ : (n : ℝ) * h < π) :
    h * (phiExt h (i + 1) - phiExt h i)
      ≤ (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
          (phi (((i : ℝ) + 1) * h) - phi u))
    ∧ (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
          (phi (((i : ℝ) + 1) * h) - phi u)) ≤ 0 := by
  have hpi := Real.pi_pos
  have hab : (i : ℝ) * h ≤ ((i : ℝ) + 1) * h := by nlinarith
  have hae := ae_phi_le_phiExt hh hi hnπ
  have hc0 : IntervalIntegrable (fun _ : ℝ => phi (((i : ℝ) + 1) * h))
      MeasureTheory.volume ((i : ℝ) * h) (((i : ℝ) + 1) * h) :=
    intervalIntegrable_const
  have hint : IntervalIntegrable (fun u => phi (((i : ℝ) + 1) * h) - phi u)
      MeasureTheory.volume ((i : ℝ) * h) (((i : ℝ) + 1) * h) :=
    hc0.sub (intervalIntegrable_phi _ _)
  constructor
  · -- lower: replace φ(u) by the ceiling
    have hcap : IntervalIntegrable
        (fun _ : ℝ => phi (((i : ℝ) + 1) * h) - phiExt h i)
        MeasureTheory.volume ((i : ℝ) * h) (((i : ℝ) + 1) * h) :=
      intervalIntegrable_const
    have hmono := intervalIntegral.integral_mono_ae_restrict hab hcap hint
      (by
        filter_upwards [hae] with u hu
        linarith [hu])
    have hconst : (∫ _u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
          (phi (((i : ℝ) + 1) * h) - phiExt h i))
        = h * (phiExt h (i + 1) - phiExt h i) := by
      rw [intervalIntegral.integral_const, smul_eq_mul, phiExt_succ]
      ring
    rw [hconst] at hmono
    exact hmono
  · -- upper: antitonicity makes every cell defect nonpositive
    have hae2 : ∀ᵐ u ∂(MeasureTheory.volume.restrict
        (Set.Icc ((i : ℝ) * h) (((i : ℝ) + 1) * h))),
        phi (((i : ℝ) + 1) * h) - phi u ≤ 0 := by
      have hnull : ∀ᵐ (u : ℝ), u ≠ 0 := by
        rw [MeasureTheory.ae_iff]
        simpa using (Real.volume_singleton (a := (0 : ℝ)))
      have hi1 : ((i : ℝ) + 1) * h ≤ (n : ℝ) * h := by
        have : ((i : ℝ) + 1) ≤ (n : ℝ) := by exact_mod_cast hi
        nlinarith
      filter_upwards [MeasureTheory.ae_restrict_of_ae hnull,
        MeasureTheory.ae_restrict_mem measurableSet_Icc] with u hu0 humem
      obtain ⟨hu1, hu2⟩ := humem
      have hupos : 0 < u := by
        rcases Nat.eq_zero_or_pos i with hi0 | hi0
        · subst hi0
          simp only [Nat.cast_zero, zero_mul] at hu1
          exact lt_of_le_of_ne hu1 (Ne.symm hu0)
        · have : (0:ℝ) < (i : ℝ) * h := by
            have : (0:ℝ) < (i : ℝ) := by exact_mod_cast hi0
            positivity
          linarith
      have huπ : u < π := by linarith [hi1, hnπ]
      have hxpos : (0:ℝ) < ((i : ℝ) + 1) * h := by positivity
      have hxπ : ((i : ℝ) + 1) * h < π := by linarith [hi1, hnπ]
      rcases eq_or_lt_of_le hu2 with heq | hlt
      · rw [heq]
        simp
      · have := strictAntiOn_phi ⟨hupos, huπ⟩ ⟨hxpos, hxπ⟩ hlt
        linarith
    have := intervalIntegral.integral_mono_ae_restrict hab hint
      intervalIntegrable_const hae2
    simpa using this

/-- **L4-1c(ii) — the smooth half is squeezed (sorry-free).**  Telescoping
    the per-cell bounds:

        h·( φ_ext(n) − log 2 )  ≤  Σ_{i<n} ∫_{cell_i} (φ(x_{i+1}) − φ(u)) du  ≤  0,

    an `O(h)` two-sided bound obtained with **no derivative estimate** — only
    antitonicity of `φ` and the `sin u ≤ u` ceiling.  Together with the exact
    singular telescope (L4-1c(i)) and Stirling (L4-1b) this closes the
    ingredient list for the second-order log-sine expansion. -/
theorem smooth_defect_squeeze {h : ℝ} (hh : 0 < h) {n : ℕ}
    (hnπ : (n : ℝ) * h < π) :
    h * (phiExt h n - Real.log 2)
      ≤ ∑ i ∈ Finset.range n,
          (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
            (phi (((i : ℝ) + 1) * h) - phi u))
    ∧ ∑ i ∈ Finset.range n,
        (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
          (phi (((i : ℝ) + 1) * h) - phi u)) ≤ 0 := by
  constructor
  · have hlow : ∀ i ∈ Finset.range n,
        h * (phiExt h (i + 1) - phiExt h i)
          ≤ ∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (phi (((i : ℝ) + 1) * h) - phi u) := by
      intro i hi
      exact (cell_defect_bounds hh (Finset.mem_range.mp hi) hnπ).1
    have hsum := Finset.sum_le_sum hlow
    have htel : ∑ i ∈ Finset.range n, h * (phiExt h (i + 1) - phiExt h i)
        = h * (phiExt h n - Real.log 2) := by
      rw [← Finset.mul_sum, Finset.sum_range_sub (fun j => phiExt h j),
        phiExt_zero]
    linarith [hsum, htel.symm.le, htel.le]
  · refine Finset.sum_nonpos fun i hi => ?_
    exact (cell_defect_bounds hh (Finset.mem_range.mp hi) hnπ).2

end QOU.Knot.FigureEightVolume
