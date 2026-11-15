import QOU.Archimedean.DilogPartBWP1Capstone
import QOU.Archimedean.DilogPartBIteratedLimit

/-!
# Dilog Part-B W-P1 — the Faddeev-scaling positive (unconditional cusp-reaching limit)

The joint W-P1 capstone (`tendsto_wp1_sum_of_no_resonance`, #4270) proves W-P1 convergence
*conditionally* on a Diophantine no-resonance bound `c(q−1) ≤ 1−x·qⁿ`, and the unconditional
*branch-index* (`n = ⌊log_q(1/x)⌋`) pointwise limit is proved-**false** along a resonant
counter-sequence (ledger `docs/coordination/dilog-part-b-cusp-attack.md`, 2026-07-25).  This
file gives the honest **positive** counterpart: an explicit **Faddeev-type restricted
scaling** that *reaches the branch point* (`x·qⁿ → 1⁻`) yet satisfies the no-resonance bound
**by construction** (`c = 1`), so the joint W-P1 limit holds **unconditionally along it** —
no Diophantine hypothesis.

## The scaling

Back the endpoint off the cusp by exactly the cell width: take the *moving* interior target
`ρ(q) := 2 − q → 1⁻` and the bulk floor index `n(q) := nOfQ x q (2−q) = ⌊log((2−q)/x)/log q⌋`
(the largest `n` with `x·qⁿ ≤ 2−q`).  Because `x·qⁿ ≤ 2 − q`, the endpoint gap obeys

`1 − x·qⁿ  ≥  1 − (2−q)  =  q − 1`,

i.e. the no-resonance bound with `c = 1` — automatically.  Simultaneously `2−q → 1⁻`
drags the endpoint `x·qⁿ ∈ ((2−q)/q, 2−q]` up to the cusp (`→ 1⁻`).  So this single joint
`q → 1⁺` limit reaches the branch point *and* stays no-resonant — unlike the fixed-`ρ` bulk
route (`wp1_bulk_tendsto`, which needs a *second* `ρ→1⁻` iterated limit), and unlike the bare
branch index (which resonates and fails).  Feeding it to `tendsto_wp1_sum_of_no_resonance`:

`(q − 1)·Σ_{k<n(q)} log(1 − x·qᵏ)  ⟶  Li₂(x) − π²/6`   as `q → 1⁺`,   **unconditionally**.

## Honest scope

This does **not** contradict the proved-false unconditional branch-index limit: that failure
is *pointwise over all `q→1⁺` at the resonant index* `⌊log_q(1/x)⌋`; here the index `n(q)` is
a *specific* restricted (Faddeev) approach chosen to avoid resonance.  The existence of one
convergent cusp-reaching scaling is exactly the positive content the equidistribution / Faddeev
programme targets; the *measure-theoretic* "a.e. approach converges" statement (three-distance /
equidistribution of `frac(log_q 1/x)`) remains the deeper open residual (bean `qou-jplv`).
Combined with the W-P2 tail (`DilogPartBEulerTail` / the assembly of PR #4423), this scaling
gives the Part-B total `→ Li₂(x) − π²/3` unconditionally along the Faddeev approach.

## Base ring (§7c)

Archimedean throughout (`ℝ`): `LiTwo`, `Real.log`, and the one-sided filters live past the
substrate→archimedean wall.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; docs/coordination/dilog-part-b-cusp-attack.md; bean qou-jplv
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.Archimedean

open Filter Topology QOU.QPochhammer

/-- **Faddeev-scaling W-P1 convergence (unconditional, cusp-reaching).**  For fixed
    `x ∈ (0,1)`, with the moving-target bulk index `n(q) = nOfQ x q (2−q)` (largest `n` with
    `x·qⁿ ≤ 2−q`), the positive-factor rescaled log-sum converges to the W-P1 target as
    `q → 1⁺`, with **no** Diophantine hypothesis:

    `(q − 1)·Σ_{k<n(q)} log(1 − x·qᵏ)  ⟶  Li₂(x) − π²/6`.

    Proof: the endpoint `x·qⁿ ∈ ((2−q)/q, 2−q]` reaches the cusp (`→ 1⁻`, squeeze) while the
    gap `1 − x·qⁿ ≥ q − 1` gives the no-resonance bound with `c = 1`; then
    `tendsto_wp1_sum_of_no_resonance` (#4270) applies. -/
theorem wp1_faddeev_tendsto {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    Tendsto (fun q => (q - 1) * ∑ k ∈ Finset.range (nOfQ x q (2 - q)),
        Real.log (1 - x * q ^ k)) (𝓝[>] (1 : ℝ)) (𝓝 (LiTwo x - Real.pi ^ 2 / 6)) := by
  -- eventually `q < 2 − x` (so the moving target `2 − q` stays above `x`)
  have hq_lt : ∀ᶠ q in 𝓝[>] (1 : ℝ), q < 2 - x := by
    have hmem : Set.Iio (2 - x) ∈ 𝓝[>] (1 : ℝ) :=
      nhdsWithin_le_nhds (Iio_mem_nhds (by linarith))
    filter_upwards [hmem] with q hq; exact hq
  have hq1 : ∀ᶠ q in 𝓝[>] (1 : ℝ), (1 : ℝ) < q := by
    filter_upwards [self_mem_nhdsWithin] with q hq; exact hq
  -- no-resonance bound with c = 1
  have hbound : ∀ᶠ q in 𝓝[>] (1 : ℝ),
      (1 : ℝ) * (q - 1) ≤ 1 - x * q ^ (nOfQ x q (2 - q)) := by
    filter_upwards [hq1, hq_lt] with q hq hqlt
    have hxρ : x < 2 - q := by linarith
    have hle := nOfQ_mul_pow_le hx0 hxρ hq
    rw [one_mul]; linarith
  -- endpoint reaches the cusp from below: `x·qⁿ → 1⁻`
  have hxqn : Tendsto (fun q => x * q ^ (nOfQ x q (2 - q))) (𝓝[>] (1 : ℝ)) (𝓝[<] 1) := by
    rw [tendsto_nhdsWithin_iff]
    refine ⟨?_, ?_⟩
    · have hlow : Tendsto (fun q : ℝ => (2 - q) / q) (𝓝[>] (1 : ℝ)) (𝓝 1) := by
        have h : Tendsto (fun q : ℝ => (2 - q) / q) (𝓝 (1 : ℝ)) (𝓝 ((2 - 1) / 1)) :=
          (tendsto_const_nhds.sub tendsto_id).div tendsto_id (by norm_num)
        rw [show ((2 : ℝ) - 1) / 1 = 1 by norm_num] at h
        exact h.mono_left nhdsWithin_le_nhds
      have hupp : Tendsto (fun q : ℝ => 2 - q) (𝓝[>] (1 : ℝ)) (𝓝 1) := by
        have h : Tendsto (fun q : ℝ => 2 - q) (𝓝 (1 : ℝ)) (𝓝 (2 - 1)) :=
          tendsto_const_nhds.sub tendsto_id
        rw [show (2 : ℝ) - 1 = 1 by norm_num] at h
        exact h.mono_left nhdsWithin_le_nhds
      refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlow hupp ?_ ?_
      · filter_upwards [hq1, hq_lt] with q hq hqlt
        have hxρ : x < 2 - q := by linarith
        exact (nOfQ_mul_pow_gt hx0 hxρ hq).le
      · filter_upwards [hq1, hq_lt] with q hq hqlt
        have hxρ : x < 2 - q := by linarith
        exact nOfQ_mul_pow_le hx0 hxρ hq
    · filter_upwards [hq1, hq_lt] with q hq hqlt
      have hxρ : x < 2 - q := by linarith
      have hle := nOfQ_mul_pow_le hx0 hxρ hq
      simp only [Set.mem_Iio]; linarith
  have hq : Tendsto (fun q : ℝ => q) (𝓝[>] (1 : ℝ)) (𝓝 1) :=
    tendsto_id.mono_left nhdsWithin_le_nhds
  exact tendsto_wp1_sum_of_no_resonance hx0 one_pos hq1 hbound hxqn hq

end QOU.Archimedean
