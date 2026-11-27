import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi
import Mathlib.Analysis.Normed.Group.Tannery
import Mathlib.Analysis.SpecialFunctions.Exp

/-!
# QOU.FluidDynamics.q_ns_block_heat_loss — the linear q-heat flow on the Cartan block
# loses no energy in the limit `q → 1⁺`

Bean `qou-d2tt` (item 5 of `qou-innq`, the exponent `α`); thread "Use q-Bessel functions
to close derivation gaps" (2026-11-27), route 2.

`CompactQuantumMetrics/OqSU2BudgetLittleQJacobi` shows that on the torus-invariant block
`K[ζ]`, the operator `L = X₊X₋` is diagonal in the little q-Jacobi basis, with eigenvalues

    λ_n(q) = [n]_{q⁻²} [n+1]_{q²} = q [n]_q [n+1]_q,

and that the budget is `h(X₊a·X₋a) = −q⁻² h(a·La)`. So the linear q-heat flow
`u̇ = −ν_q L u` acts mode by mode. A mode with initial energy `e_n` keeps energy
`e_n exp(−2 ν_q λ_n(q) t)` at time `t`. This is the q-Bessel / little q-Jacobi form of
energy diffusion on the block. Its `E_q(2)` contraction is the Hahn–Exton q-Hankel
transform, which is not formalised here.

The energy lost on `[0, T]` is therefore

    blockLoss e T q = Σ_n e_n (1 − exp(−2 ν_q λ_n(q) T)),   ν_q = (1 − q⁻¹)/2.

## Results

* `blockLoss_tendsto_zero`: for nonnegative summable mode energies `e` that do not depend on
  `q` (substrate-layer data, owner ruling 2026-11-27) and `T ≥ 0`,
  `blockLoss e T q → 0` as `q → 1⁺`.
* `no_uniform_loss`: so no `δ > 0` bounds the loss below on a whole window `(1, q₀]`.

## Consequence for `α`

`q_ns_alpha_dissipation_bound.alpha_ge_one_of_anomaly` gives `α ≥ 1` from a uniform
energy loss `δ > 0`. On the Cartan block the linear part cannot supply that loss, so any
dissipation anomaly must come from triad transfer, the nonlinear term. That is a
scope-(a) negative: it constrains the linear part only.

The rate is not `O(q − 1)` uniformly in the data. For `n(q − 1) ≪ 1`,
`ν_q λ_n ≈ (q − 1) n² / 2`, so modes above `n ≈ ((q − 1) T)^{−1/2}` are strongly damped.
For `n(q − 1) ≫ 1`, `[n]_q` grows like `q^n/(q − q⁻¹)` and the damping is stronger still.
The loss tends to 0 because the threshold tends to infinity. The rate depends on the tail
of `e`. (This paragraph is a heuristic, not a theorem.)

## Not established

* The other weight blocks, the nonlinear term, and Part A.
* That `exp(−2 ν_q λ_n t)` is the solution of the flow on `O_q(SU(2))`. Here it is the
  modal definition.

The proofs use real analysis (`Real.exp`, limits, dominated convergence for series), so
this file lives in `QOU/Transcendental/`. No empirical value enters any proof.
-/

namespace QOU.FluidDynamics.QNsBlockHeatLoss

open Filter Topology QOU.AlgebraicSubstrate.OqSU2

/-- The q-NS viscosity `ν_q = (1 − q⁻¹)/2`, the same formula as `DEC.nuQ`. -/
noncomputable def nuQ (q : ℝ) : ℝ := (1 - q⁻¹) / 2

/-- The block eigenvalue `λ_n(q) = [n]_{q⁻²} [n+1]_{q²}` of `X₊X₋` on `ζ^n`
(`lap_zeta_pow`). -/
noncomputable def blockEig (q : ℝ) (n : ℕ) : ℝ := jk (q⁻¹ * q⁻¹) n * jk (q * q) (n + 1)

/-- Energy lost on `[0, T]` by the linear q-heat flow on the block, with mode energies `e`. -/
noncomputable def blockLoss (e : ℕ → ℝ) (T q : ℝ) : ℝ :=
  ∑' n, e n * (1 - Real.exp (-(2 * nuQ q * blockEig q n * T)))

theorem jk_nonneg {x : ℝ} (hx : 0 ≤ x) (n : ℕ) : 0 ≤ jk x n :=
  Finset.sum_nonneg fun i _ => pow_nonneg hx i

theorem blockEig_nonneg {q : ℝ} (hq : 0 < q) (n : ℕ) : 0 ≤ blockEig q n :=
  mul_nonneg (jk_nonneg (by positivity) n) (jk_nonneg (by positivity) _)

theorem nuQ_nonneg {q : ℝ} (hq : 1 ≤ q) : 0 ≤ nuQ q := by
  unfold nuQ
  have : q⁻¹ ≤ 1 := inv_le_one_of_one_le₀ hq
  linarith

theorem nuQ_one : nuQ 1 = 0 := by simp [nuQ]

theorem continuousAt_blockEig (n : ℕ) : ContinuousAt (fun q => blockEig q n) 1 := by
  unfold blockEig jk
  fun_prop (disch := norm_num)

/-- Each mode's lost fraction tends to 0 as `q → 1`. -/
theorem mode_tendsto (e : ℕ → ℝ) (T : ℝ) (n : ℕ) :
    Tendsto (fun q => e n * (1 - Real.exp (-(2 * nuQ q * blockEig q n * T)))) (𝓝 1)
      (𝓝 0) := by
  have hν : ContinuousAt nuQ 1 := by unfold nuQ; fun_prop (disch := norm_num)
  have h : ContinuousAt (fun q => e n * (1 - Real.exp (-(2 * nuQ q * blockEig q n * T)))) 1 := by
    have := continuousAt_blockEig n
    fun_prop
  have h1 : e n * (1 - Real.exp (-(2 * nuQ 1 * blockEig 1 n * T))) = 0 := by simp [nuQ_one]
  simpa [h1] using h.tendsto

/-- **No energy loss in the limit.** -/
theorem blockLoss_tendsto_zero {e : ℕ → ℝ} (he : ∀ n, 0 ≤ e n) (hs : Summable e) {T : ℝ}
    (hT : 0 ≤ T) : Tendsto (blockLoss e T) (𝓝[>] 1) (𝓝 0) := by
  have key := tendsto_tsum_of_dominated_convergence (𝓕 := 𝓝[>] (1 : ℝ))
    (f := fun q n => e n * (1 - Real.exp (-(2 * nuQ q * blockEig q n * T))))
    (g := fun _ => (0 : ℝ)) (bound := e) hs
    (fun n => (mode_tendsto e T n).mono_left nhdsWithin_le_nhds) ?_
  · simpa [blockLoss, tsum_zero] using key
  · filter_upwards [self_mem_nhdsWithin] with q hq n
    have hq1 : (1 : ℝ) < q := hq
    have hx : 0 ≤ 2 * nuQ q * blockEig q n * T :=
      mul_nonneg (mul_nonneg (by linarith [nuQ_nonneg hq1.le]) (blockEig_nonneg (by linarith) n)) hT
    have hexp_le : Real.exp (-(2 * nuQ q * blockEig q n * T)) ≤ 1 :=
      Real.exp_le_one_iff.mpr (by linarith)
    have hexp_pos := Real.exp_pos (-(2 * nuQ q * blockEig q n * T))
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (he n) (by linarith))]
    nlinarith [he n]

/-- **No uniform energy loss.** On no window `(1, q₀]` is the loss bounded below by a
`δ > 0`. So the hypothesis of `alpha_ge_one_of_anomaly` fails for the linear block flow. -/
theorem no_uniform_loss {e : ℕ → ℝ} (he : ∀ n, 0 ≤ e n) (hs : Summable e) {T : ℝ}
    (hT : 0 ≤ T) {q₀ δ : ℝ} (hq₀ : 1 < q₀) (hδ : 0 < δ) :
    ¬ ∀ q ∈ Set.Ioc 1 q₀, δ ≤ blockLoss e T q := by
  intro h
  have hev : ∀ᶠ q in 𝓝[>] (1 : ℝ), blockLoss e T q < δ :=
    (blockLoss_tendsto_zero he hs hT).eventually (gt_mem_nhds hδ)
  have hwin : ∀ᶠ q in 𝓝[>] (1 : ℝ), q ∈ Set.Ioc 1 q₀ := Ioc_mem_nhdsGT hq₀
  obtain ⟨q, hlt, hmem⟩ := (hev.and hwin).exists
  exact absurd (h q hmem) (not_le.mpr hlt)

end QOU.FluidDynamics.QNsBlockHeatLoss
