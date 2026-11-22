/-
# Whitehead link (b = 1) scaffold: complex carrier, majorant bound, and the
# vdV-Lemma-4 conditional class (bean qou-ybpk)

The `b ≥ 2` Whitehead-chain volume-conjecture instance is proved sorry-free
in `WhiteheadChainVolume.lean` because its Kashaev-point modulus is a
phase-free positive sum.  The `b = 1` Whitehead link proper
(`W_{0,1,1,0}` = L5a1, Vol = 4G) is different: vdV Lemma 1 gives

    J_N = φ_N Σ_{n=0}^{N-1} (2n+1) χ_{N,n}^{-1} (Σ_{k=0}^{N-1-n} S_{n,k}),
    χ_{N,n} = exp(n(n+1-N)πi/(2N)),  φ_N = exp((N-1)πi/N),

whose outer `n`-sum carries Fresnel phases.  Van der Veen's Lemma 4 (the
Gaussian/erfc stationary-phase analysis, arXiv:math/0611181 §3 Steps 3-6)
shows the phases cost only polynomially — `J_N ∼ C·N^{(c+d+3)/2}·S̃^{c+d}`
with `C ≠ 0` — but that analysis is NOT elementary and is not reproduced
here.  This file records the honest split:

* **Sorry-free**: the complex carrier `whiteheadLinkKashaev` (faithful
  Lemma-1 transcription, anchor-verified numerically in
  `computations/whitehead_vdv_lemma1.py`), the positive majorant
  `whiteheadLinkMajorant`, its positivity, and the triangle inequality
  `‖J_N‖ ≤ majorant` — the upper half of a future squeeze.
* **Conditional class** `VdVWhiteheadLemma4` (a PRIMARY conjecture carrier,
  §3b-tax): the single content field `phase_cost` states Lemma 4's analytic
  essence — the majorant exceeds the modulus by at most a fixed power of
  `N`.  No instance is provided: the class is the open analytic input.
* **Derived conditional theorem**
  `tendsto_log_norm_whiteheadLinkKashaev_of_majorant`: GIVEN the class and
  the majorant volume rate (the open 2D brick W6, bean qou-oiv6 — the
  2-variable functional `f(x,y) = Λ(x) + 2Λ(y) − 2Λ(x+y)` maximised at
  `(π/2, π/4)`), the Whitehead-link volume limit follows by an elementary
  log-squeeze.  The conclusion is derived, not axiomatised.

Route context: `docs/audits/2026-08-02-whitehead-chain-positive-sum-route.md`.
-/

/-
**CROSS-REFERENCE (2026-08-19) — a second Whitehead-link VC program exists.**

`QOU/Knot/WhiteheadVolumeConjecture.lean` + `QOU/Knot/WhiteheadSaddleClausen.lean`
(beans `qou-t2sc` / `qou-dw20` / `qou-1gkf`) attack the same theorem from the
OPPOSITE end, by van der Veen's Lemma-1 POSITIVE-sum route:

* they have the MAGNITUDE — `whitehead_vc_innerSum_half` (sorry-free): the
  inner sum `Σ_k S_{n,k}` at the slice `n = ⌊N/2⌋` has scaled log `→ 4G`;
* this program has the PHASES — the majorant bound, its `4G` limit, and the
  residue isolated as `VdVWhiteheadLemma4` (no instance anywhere: open).

The gap between the two ends is non-cancellation of the phased outer sum
`Σ_n (2n+1)·χ_{N,n}^{-1}·(Σ_k S_{n,k})` — which is exactly Lemma 4. The two are
COMPLEMENTARY, not redundant. Coordinate before extending either.

Note their `whitehead_volume_conjecture` is not the VC for `J_N(W)`: it assumes
`hk : kashaev N = whiteheadInnerSum N ((N-1)/2)`, so it concerns the inner sum
at one slice. Their docstring says so; the name alone does not.
Audit: `docs/audits/2026-08-19-volume-conjecture-work-overlap-sweep.md`.
-/

import QOU.Knot.WhiteheadChainVolume
import QOU.MathlibExt.ExponentialGrowthRate

namespace QOU.Knot.FigureEightVolume

open Real

/-- The Fresnel phase `χ_{N,n}^{-1} = exp(−n(n+1−N)πi/(2N))` of vdV
    Lemma 1 at exponent `4a−c+d = −1` (the Whitehead link `W_{0,1,1,0}`). -/
noncomputable def whiteheadLinkPhase (N n : ℕ) : ℂ :=
  Complex.exp (((-((n:ℝ) * ((n:ℝ) + 1 - (N:ℝ)) * π / (2 * N)) : ℝ) : ℂ)
    * Complex.I)

/-- The `b = 1` Whitehead-link Lemma-1 sum at the Kashaev point (faithful
    transcription; `φ_N = exp((N−1)πi/N)` for `c+d = 1`, inner sums are the
    positive `S_{n,k}` of the chain file with the `M`-slot at `n`). -/
noncomputable def whiteheadLinkKashaev (N : ℕ) : ℂ :=
  Complex.exp (((((N:ℝ) - 1) * π / N : ℝ) : ℂ) * Complex.I)
    * ∑ n ∈ Finset.range N, ((2 * n + 1 : ℕ) : ℂ) * whiteheadLinkPhase N n
        * (((∑ k ∈ Finset.range (N - n), whiteheadTerm N n k : ℝ)) : ℂ)

/-- The positive majorant: the same double sum with the phases dropped. -/
noncomputable def whiteheadLinkMajorant (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.range N,
    ((2 * n + 1 : ℕ) : ℝ) * (∑ k ∈ Finset.range (N - n), whiteheadTerm N n k)

/-- Each inner sum is strictly positive (`n ≤ N−1` leaves at least the
    `k = 0` term, and every term is an in-grid positive `S_{n,k}`). -/
theorem whiteheadLink_inner_pos {N n : ℕ} (hn : n < N) :
    0 < ∑ k ∈ Finset.range (N - n), whiteheadTerm N n k := by
  apply Finset.sum_pos
  · intro k hk
    have hk' := Finset.mem_range.mp hk
    exact whiteheadTerm_pos (by omega)
  · exact ⟨0, Finset.mem_range.mpr (by omega)⟩

/-- The majorant is strictly positive for `N ≥ 1`. -/
theorem whiteheadLinkMajorant_pos {N : ℕ} (hN : 1 ≤ N) :
    0 < whiteheadLinkMajorant N := by
  unfold whiteheadLinkMajorant
  apply Finset.sum_pos
  · intro n hn
    have hn' := Finset.mem_range.mp hn
    have hinner := whiteheadLink_inner_pos (N := N) (n := n) hn'
    have h2n : (0:ℝ) < ((2 * n + 1 : ℕ) : ℝ) := by
      exact_mod_cast (by omega : 0 < 2 * n + 1)
    exact mul_pos h2n hinner
  · exact ⟨0, Finset.mem_range.mpr (by omega)⟩

/-- **The triangle bound (sorry-free)** — the upper half of the future
    `b = 1` squeeze: `‖J_N‖ ≤ majorant N`.  The global `φ_N` and each
    `χ_{N,n}^{-1}` are unimodular, the inner sums are positive. -/
theorem norm_whiteheadLinkKashaev_le (N : ℕ) :
    ‖whiteheadLinkKashaev N‖ ≤ whiteheadLinkMajorant N := by
  unfold whiteheadLinkKashaev whiteheadLinkMajorant
  rw [norm_mul, Complex.norm_exp_ofReal_mul_I, one_mul]
  refine le_trans (norm_sum_le _ _) ?_
  apply Finset.sum_le_sum
  intro n hn
  have hn' := Finset.mem_range.mp hn
  have hinner := (whiteheadLink_inner_pos (N := N) (n := n) hn').le
  rw [norm_mul, norm_mul]
  unfold whiteheadLinkPhase
  rw [Complex.norm_exp_ofReal_mul_I, mul_one]
  rw [Complex.norm_natCast, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg hinner]

/-- **vdV Lemma 4, axiomatised as a primary conjecture class** (§3b-tax; no
    instance is provided — this is the open analytic input).  Content: the
    Fresnel phases of the `b = 1` outer sum cost at most a fixed power of
    `N` — the stationary-phase constant is nonzero, so modulus and majorant
    share their exponential growth.  This is the analytic essence of
    van der Veen's Lemma 4 (Gaussian → erfc, arXiv:math/0611181 §3); a
    future sorry-free discharge would formalize that argument.
    -- Ref: [leitner2026] library/arxiv-math-0611181v2/0611181v2.pdf, Lemma 4 -/
class VdVWhiteheadLemma4 : Prop where
  /-- The majorant exceeds the modulus by at most `N^p` for some fixed `p`,
      eventually in `N` — phases cost polynomially, never exponentially. -/
  phase_cost : ∃ p : ℕ, ∀ᶠ N in Filter.atTop,
    whiteheadLinkMajorant N ≤ (N:ℝ) ^ p * ‖whiteheadLinkKashaev N‖

/-- **Conditional volume limit for the Whitehead link (derived, not
    axiomatised).**  Given the Lemma-4 class AND the majorant volume rate
    (the open 2D brick W6, bean qou-oiv6), the Whitehead-link Kashaev
    modulus obeys the volume conjecture:
    `(2π/N)·log ‖J_N‖ → 4·Cl₂(π/2) = 4G = Vol(L5a1)`.

    **The squeeze is no longer hand-rolled.**  It is
    `QOU.MathlibExt.tendsto_log_div_of_sandwich` — *a sub-exponential sandwich
    does not move an exponential growth rate* — instantiated at

        m N = majorant N / N^p ,   S N = ‖J_N‖ ,   c N = N^p ,

    for which `m ≤ S` is exactly `VdVWhiteheadLemma4.phase_cost` and
    `S ≤ c·m` is exactly the sorry-free triangle bound
    `norm_whiteheadLinkKashaev_le`.  That is the whole content of the
    conditional: the class supplies one inequality, the triangle bound the
    other, and the shared lemma does the analysis.

    Note the direction.  The shared lemma is stated knowing the *small* side's
    rate and concluding about the *large* one; here it is the large side
    (`majorant`) whose rate is known.  Dividing the known side by `N^p` is what
    puts it in the lemma's `m` slot — and it costs nothing precisely because
    `log(N^p)/N → 0`, which is the same sub-exponentiality the lemma's `c`
    slot wants.  Getting this backwards (trying `m = ‖J_N‖`) asks for the rate
    that is open. -/
theorem tendsto_log_norm_whiteheadLinkKashaev_of_majorant [VdVWhiteheadLemma4]
    (hMaj : Filter.Tendsto
      (fun N : ℕ => (2 * π / N) * Real.log (whiteheadLinkMajorant N))
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2))) :
    Filter.Tendsto
      (fun N : ℕ => (2 * π / N) * Real.log ‖whiteheadLinkKashaev N‖)
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) := by
  have hpi := Real.pi_pos
  have h2pi : (0:ℝ) < 2 * π := by linarith
  obtain ⟨p, hp⟩ := VdVWhiteheadLemma4.phase_cost
  -- `log N / N → 0`, the one analytic fact, borrowed rather than re-proved
  have hlogN := QOU.MathlibExt.tendsto_log_natCast_div_atTop
  -- restate the hypothesis in the `log(·)/N` normalisation the lemma uses
  have hMaj' : Filter.Tendsto
      (fun N : ℕ => Real.log (whiteheadLinkMajorant N) / (N:ℝ))
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2 / (2 * π))) := by
    refine (hMaj.div_const (2 * π)).congr (fun N => ?_)
    rcases eq_or_ne ((N:ℝ)) 0 with h | h
    · simp [h]
    · field_simp
  -- the sandwich, in `log(·)/N` form
  have key : Filter.Tendsto
      (fun N : ℕ => Real.log ‖whiteheadLinkKashaev N‖ / (N:ℝ))
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2 / (2 * π))) := by
    refine QOU.MathlibExt.tendsto_log_div_of_sandwich
      (m := fun N : ℕ => whiteheadLinkMajorant N / (N:ℝ) ^ p)
      (c := fun N : ℕ => (N:ℝ) ^ p) ?_ ?_ ?_ ?_ ?_ ?_
    · filter_upwards [Filter.eventually_ge_atTop 1] with N hN
      have hNpos : (0:ℝ) < N := by exact_mod_cast hN
      exact div_pos (whiteheadLinkMajorant_pos hN) (by positivity)
    · filter_upwards [Filter.eventually_ge_atTop 1] with N hN
      have hNpos : (0:ℝ) < N := by exact_mod_cast hN
      positivity
    · -- `majorant / N^p ≤ ‖J‖` is `phase_cost`, divided through
      filter_upwards [hp, Filter.eventually_ge_atTop 1] with N hpN hN
      have hNpos : (0:ℝ) < N := by exact_mod_cast hN
      have hNp : (0:ℝ) < (N:ℝ) ^ p := by positivity
      rw [div_le_iff₀ hNp]
      linarith [hpN]
    · -- `‖J‖ ≤ N^p · (majorant / N^p) = majorant` is the triangle bound
      filter_upwards [Filter.eventually_ge_atTop 1] with N hN
      have hNpos : (0:ℝ) < N := by exact_mod_cast hN
      have hNp : (0:ℝ) < (N:ℝ) ^ p := by positivity
      rw [mul_div_cancel₀ _ (ne_of_gt hNp)]
      exact norm_whiteheadLinkKashaev_le N
    · -- `log (N^p) / N = p · (log N / N) → 0`
      have h := hlogN.const_mul (p:ℝ)
      rw [mul_zero] at h
      refine h.congr (fun N => ?_)
      rw [Real.log_pow]
      ring
    · -- `log (majorant / N^p) / N = log majorant / N − p · (log N / N)`
      have h := hMaj'.sub (hlogN.const_mul (p:ℝ))
      rw [mul_zero, sub_zero] at h
      refine h.congr' ?_
      filter_upwards [Filter.eventually_ge_atTop 1] with N hN
      have hNpos : (0:ℝ) < N := by exact_mod_cast hN
      have hNp : (0:ℝ) < (N:ℝ) ^ p := by positivity
      rw [Real.log_div (ne_of_gt (whiteheadLinkMajorant_pos hN)) (ne_of_gt hNp),
        Real.log_pow]
      ring
  -- undo the `2π` normalisation
  have hfin := key.const_mul (2 * π)
  rw [show (2 * π) * (QOU.Archimedean.Vol_Borromean / 2 / (2 * π))
      = QOU.Archimedean.Vol_Borromean / 2 by field_simp] at hfin
  exact hfin.congr (fun N => by ring)

end QOU.Knot.FigureEightVolume
