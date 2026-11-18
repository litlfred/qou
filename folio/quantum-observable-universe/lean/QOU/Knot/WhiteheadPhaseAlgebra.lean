/-
# vdV Lemma 4, brick L4-4 — phase algebra (bean qou-wzmi, epic qou-u1b5)

Self-contained first brick of the Lemma-4 epic
(`docs/audits/2026-08-11-vdv-lemma4-formalization-workplan.md`): the exact
quadratic decomposition of the Whitehead-link Fresnel phase and the limits
of the non-oscillatory phase factors, transcribed from van der Veen §3,
proof of Lemma 4, Step 3 (`library/arxiv-math-0611181v2/0611181v2.pdf`):

    χ_{N,n}·e^{Nπi/8} = exp(n′²πi/(2N)) · exp(nπi/(2N)),   n′ = n − N/2,
    lim φ_N = e^{(c−d)πi}  (= −1 for the Whitehead link, c−d = 1),
    lim exp(nπi/(2N)) = e^{iπ/4} along the central row n = ⌊N/2⌋.

Everything here is exact `Complex.exp` arithmetic over real arguments plus
floor-squeeze grid limits — no Gaussian analysis.  The genuinely analytic
bricks (L4-1 Euler–Maclaurin, L4-2 window estimates, L4-5 sum→integral,
L4-6 erfc nonvanishing) remain open; see the epic workplan.  The phase
convention matches `whiteheadLinkKashaev` (`WhiteheadLinkScaffold.lean`),
which carries `χ^{−1}`, so the decomposition below is stated for the
inverse phase: the scaffold's `whiteheadLinkPhase N n` splits as
`exp(−n′²πi/(2N)) · exp(+Nπi/8) · exp(−nπi/(2N))` — the pure Fresnel
quadratic times two explicit unimodular factors.
-/

import QOU.Knot.WhiteheadLinkScaffold

namespace QOU.Knot.FigureEightVolume

open Real

/-- The real-argument identity behind vdV's Step-3 phase split:
    `−n(n+1−N)/(2N) = −(n−N/2)²/(2N) + N/8 − n/(2N)` (times `π`) —
    note the POSITIVE `N/8`: inverting vdV's `χ·e^{Nπi/8} = exp(n′²πi/(2N))
    ·exp(nπi/(2N))` puts `e^{+Nπi/8}` on the `χ^{−1}` side. -/
theorem whiteheadLinkPhase_arg_decomp {N n : ℕ} (hN : 0 < N) :
    -((n:ℝ) * ((n:ℝ) + 1 - (N:ℝ)) * π / (2 * N))
      = -(((n:ℝ) - (N:ℝ) / 2) ^ 2 * π / (2 * N)) + (N:ℝ) * π / 8
        + -((n:ℝ) * π / (2 * N)) := by
  have hN' : (N:ℝ) ≠ 0 := by
    have : (0:ℝ) < N := by exact_mod_cast hN
    exact ne_of_gt this
  field_simp
  ring

/-- **L4-4 — the Fresnel-phase decomposition (sorry-free, exact).**  The
    scaffold's phase `χ_{N,n}^{−1}` factors as the pure Gaussian quadratic
    `exp(−n′²πi/(2N))` times the constant `e^{+Nπi/8}` times the linear
    `exp(−nπi/(2N))` — vdV Step 3, inverted to the scaffold convention. -/
theorem whiteheadLinkPhase_decomp {N n : ℕ} (hN : 0 < N) :
    whiteheadLinkPhase N n
      = Complex.exp
          (((-(((n:ℝ) - (N:ℝ) / 2) ^ 2 * π / (2 * N)) : ℝ) : ℂ) * Complex.I)
        * Complex.exp (((((N:ℝ) * π / 8 : ℝ)) : ℂ) * Complex.I)
        * Complex.exp (((-((n:ℝ) * π / (2 * N)) : ℝ) : ℂ) * Complex.I) := by
  unfold whiteheadLinkPhase
  rw [← Complex.exp_add, ← Complex.exp_add, ← add_mul, ← add_mul]
  congr 1
  have h := whiteheadLinkPhase_arg_decomp (N := N) (n := n) hN
  have hc : ((-((n:ℝ) * ((n:ℝ) + 1 - (N:ℝ)) * π / (2 * N)) : ℝ) : ℂ)
      = ((-(((n:ℝ) - (N:ℝ) / 2) ^ 2 * π / (2 * N)) : ℝ) : ℂ)
        + ((((N:ℝ) * π / 8 : ℝ)) : ℂ)
        + ((-((n:ℝ) * π / (2 * N)) : ℝ) : ℂ) := by
    rw [← Complex.ofReal_add, ← Complex.ofReal_add]
    exact_mod_cast h
  rw [hc]

/-- The Whitehead-link global phase `φ_N = e^{(N−1)πi/N}` tends to
    `e^{(c−d)πi} = −1` (vdV Step 3, `c − d = 1`). -/
theorem tendsto_whiteheadLink_globalPhase :
    Filter.Tendsto
      (fun N : ℕ => Complex.exp
        (((((N:ℝ) - 1) * π / N : ℝ) : ℂ) * Complex.I))
      Filter.atTop (nhds (-1)) := by
  have hpi := Real.pi_pos
  -- the real argument (N−1)π/N → π
  have harg : Filter.Tendsto (fun N : ℕ => ((N:ℝ) - 1) * π / N)
      Filter.atTop (nhds π) := by
    have h0 := tendsto_const_div_atTop_nhds_zero_nat π
    have h1 := Filter.Tendsto.const_sub π h0
    rw [sub_zero] at h1
    refine h1.congr' ?_
    filter_upwards [Filter.eventually_ge_atTop 1] with N hN1
    have hN' : (N:ℝ) ≠ 0 := by
      have : (0:ℝ) < N := by exact_mod_cast hN1
      exact ne_of_gt this
    field_simp
  -- compose with the continuous map θ ↦ exp(θ·I)
  have hcont : Continuous (fun θ : ℝ => Complex.exp ((θ : ℂ) * Complex.I)) :=
    Complex.continuous_exp.comp (Complex.continuous_ofReal.mul continuous_const)
  have h := (hcont.tendsto π).comp harg
  rw [show Complex.exp ((π : ℂ) * Complex.I) = -1 from Complex.exp_pi_mul_I] at h
  exact h

/-- Along the central row `n = ⌊N/2⌋`, the linear phase argument
    `nπ/(2N)` tends to `π/4` (vdV: `lim n/(2N) = 1/4`). -/
theorem tendsto_center_linear_arg :
    Filter.Tendsto (fun N : ℕ => (↑(N / 2) : ℝ) * π / (2 * N))
      Filter.atTop (nhds (π / 4)) := by
  have hpi := Real.pi_pos
  have h0 := tendsto_const_div_atTop_nhds_zero_nat (π / 4)
  have hlow := Filter.Tendsto.const_sub (π / 4) h0
  rw [sub_zero] at hlow
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlow tendsto_const_nhds
    ?_ ?_
  · filter_upwards [Filter.eventually_ge_atTop 1] with N hN1
    have hNpos : (0:ℝ) < N := by exact_mod_cast hN1
    have hq : (0:ℝ) < π / (4 * N) := by positivity
    have hfield4 : (N:ℝ) * (π / (4 * N)) = π / 4 := by field_simp
    have h6 : N ≤ 2 * (N / 2) + 1 := by omega
    have h6' : (N:ℝ) - 1 ≤ 2 * (↑(N / 2) : ℝ) := by
      have h : (N:ℝ) ≤ 2 * (↑(N / 2) : ℝ) + 1 := by exact_mod_cast h6
      linarith
    have hdd : π / 4 / (N:ℝ) = π / (4 * N) := by
      rw [div_div]
    have hrw : (↑(N / 2) : ℝ) * π / (2 * N)
        = (2 * (↑(N / 2) : ℝ)) * (π / (4 * N)) := by
      ring
    rw [hdd, hrw]
    nlinarith [mul_le_mul_of_nonneg_right h6' hq.le, hfield4]
  · filter_upwards [Filter.eventually_ge_atTop 1] with N hN1
    have hNpos : (0:ℝ) < N := by exact_mod_cast hN1
    have hq : (0:ℝ) < π / (4 * N) := by positivity
    have hfield4 : (N:ℝ) * (π / (4 * N)) = π / 4 := by field_simp
    have h6 : 2 * (N / 2) ≤ N := by omega
    have h6' : (2:ℝ) * (↑(N / 2) : ℝ) ≤ (N:ℝ) := by exact_mod_cast h6
    have hrw : (↑(N / 2) : ℝ) * π / (2 * N)
        = (2 * (↑(N / 2) : ℝ)) * (π / (4 * N)) := by
      ring
    rw [hrw]
    nlinarith [mul_le_mul_of_nonneg_right h6' hq.le, hfield4]

/-- The central linear phase itself: `exp(⌊N/2⌋πi/(2N)) → e^{iπ/4}` —
    the constant vdV's `ψ = e^{(4a+3c−3d)πi/4}` absorbs at `Q_∞`
    assembly (Step 3). -/
theorem tendsto_center_linear_phase :
    Filter.Tendsto
      (fun N : ℕ => Complex.exp
        ((((↑(N / 2) : ℝ) * π / (2 * N) : ℝ) : ℂ) * Complex.I))
      Filter.atTop
      (nhds (Complex.exp (((π / 4 : ℝ) : ℂ) * Complex.I))) := by
  have hcont : Continuous (fun θ : ℝ => Complex.exp ((θ : ℂ) * Complex.I)) :=
    Complex.continuous_exp.comp (Complex.continuous_ofReal.mul continuous_const)
  exact (hcont.tendsto (π / 4)).comp tendsto_center_linear_arg

/-- **Vanishing of the quadratic-plus-linear Fresnel phase shift at `n = 0` (`qou-e1dc`).**
Evaluating `whiteheadLinkPhase_arg_decomp` at `n = 0` shows that the Fresnel
quadratic `-((0 - N/2)² π / (2N))` and constant `+ N π / 8` cancel identically. -/
theorem whiteheadLinkPhase_arg_decomp_zero {N : ℕ} (hN : 0 < N) :
    -(((0 : ℝ) - (N : ℝ) / 2) ^ 2 * π / (2 * N)) + (N : ℝ) * π / 8 = 0 := by
  have hN' : (N : ℝ) ≠ 0 := by
    have : (0 : ℝ) < N := by exact_mod_cast hN
    exact ne_of_gt this
  field_simp
  ring

end QOU.Knot.FigureEightVolume
