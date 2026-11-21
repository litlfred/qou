import QOU.Archimedean.DilogPartBBranchPointSum
import QOU.Archimedean.DilogPartBBoundarySeed

/-!
# Capstone — the conditional W-P1 `Tendsto` (dilog Part B, V3)

This file fuses the three W-P1 ingredients into a single joint-`(q,n)`
convergence statement:

* `riemann_error_bound_up` (brick 3c) — the two-sided going-up Riemann-sum error
  bound `0 ≤ ∫_1^{qⁿ} h − S_n ≤ qⁿ(q−1)(h(qⁿ)−h(1))`;
* `integral_one_to_c_eq_LiTwo_sub` (brick 3e) + `tendsto_LiTwo_nhdsWithin_lt_one`
  (brick 2's Abel limit) — the target integral `∫_1^{qⁿ} h = Li₂(xqⁿ) − Li₂(x)`
  with limit `π²/6 − Li₂(x)` as `xqⁿ → 1⁻`;
* `boundary_term_vanishes` (the analytic seed) — the boundary term
  `(q−1)·(−log(1−xqⁿ)) → 0` under the Diophantine no-resonance bound.

The conclusion is the honest **conditional** result: along any filter on which
`q → 1`, the going-up geometric partition reaches the branch point
(`x·qⁿ → 1⁻`) and the no-resonance bound `1 − x·qⁿ ≥ c·(q − 1)` holds, the
positive-factor W-P1 sum `(q − 1)·Σ_{k<n} log(1 − x·qᵏ)` converges to
`Li₂(x) − π²/6`.  No fit; the unconditional (all-`x`, Faddeev-scaling) case —
where `1 − x·qⁿ ≥ c(q − 1)` can fail along the resonant `n = ⌊log_q(1/x)⌋`
sequence — remains the research residual (bean `qou-jplv`).

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.Archimedean

open QOU.QPochhammer intervalIntegral Filter Topology

/-- **Capstone — conditional W-P1 convergence (joint `(q,n)` filter).**

    Let `l` be any filter on an index type `ι` carrying substrate data
    `q : ι → ℝ`, `n : ι → ℕ` and a fixed target `0 < x`.  Suppose along `l`:

    * `q → 1` (the substrate limit, `hq`) with `1 < q` eventually (`hq1`);
    * `x·qⁿ → 1⁻` (the going-up partition reaches the branch point, `hxqn`);
    * `1 − x·qⁿ ≥ c·(q − 1)` eventually, `c > 0` (the Diophantine no-resonance
      bound keeping the endpoint gap above the cell width, `hc` + `hbound`).

    Then the positive-factor **W-P1 sum** `(q − 1)·Σ_{k<n} log(1 − x·qᵏ)`
    converges to `Li₂(x) − π²/6`.

    Proof.  Write `S i` for the going-up Riemann sum
    `Σ_{k<n} h(qᵏ)(qᵏ⁺¹−qᵏ)` and `I i` for `∫_1^{qⁿ} h`.  Brick 3e turns
    `I = Li₂(xqⁿ) − Li₂(x)`, whose limit is `π²/6 − Li₂(x)` (brick 2's Abel
    limit composed with `hxqn`).  Brick 3c bounds `E := I − S` by
    `0 ≤ E ≤ qⁿ(q−1)(h(qⁿ)−h(1))`; the upper bound splits as
    `(q−1)(−log(1−xqⁿ)) − qⁿ(q−1)(−log(1−x))`, the first factor `→ 0` by
    `boundary_term_vanishes` (no-resonance) and the second `→ 0` since
    `qⁿ → 1/x` is bounded and `q − 1 → 0`.  A squeeze gives `E → 0`, hence
    `S = I − E → π²/6 − Li₂(x)`, and the W-P1 sum `= −S` (brick 3d) tends to
    `Li₂(x) − π²/6`. -/
theorem tendsto_wp1_sum_of_no_resonance
    {ι : Type*} {l : Filter ι} {x : ℝ} {q : ι → ℝ} {n : ι → ℕ} {c : ℝ}
    (hx0 : 0 < x) (hc : 0 < c)
    (hq1 : ∀ᶠ i in l, 1 < q i)
    (hbound : ∀ᶠ i in l, c * (q i - 1) ≤ 1 - x * q i ^ n i)
    (hxqn : Tendsto (fun i => x * q i ^ n i) l (𝓝[<] (1 : ℝ)))
    (hq : Tendsto q l (𝓝 (1 : ℝ))) :
    Tendsto (fun i => (q i - 1) * ∑ k ∈ Finset.range (n i), Real.log (1 - x * q i ^ k)) l
      (𝓝 (LiTwo x - Real.pi ^ 2 / 6)) := by
  -- the endpoint gap `δ = 1 − x·qⁿ` and the raw branch-point value `x·qⁿ`
  set b : ι → ℝ := fun i => x * q i ^ n i with hb_def
  -- `x·qⁿ < 1` eventually (from `hxqn` landing in `𝓝[<] 1`)
  have hb1 : ∀ᶠ i in l, b i < 1 := hxqn self_mem_nhdsWithin
  -- `q → 1` from below-and-around: convergence to `𝓝 1`
  have hq0 : ∀ᶠ i in l, 0 < q i := hq1.mono fun i hi => lt_trans one_pos hi
  -- the Riemann sum `S i` and target integral `I i`
  set S : ι → ℝ := fun i =>
    ∑ k ∈ Finset.range (n i), (-Real.log (1 - x * q i ^ k) / q i ^ k) * (q i ^ (k + 1) - q i ^ k)
    with hS_def
  set I : ι → ℝ := fun i => ∫ u in (1 : ℝ)..q i ^ n i, -Real.log (1 - x * u) / u with hI_def
  -- `I i = Li₂(x·qⁿ) − Li₂(x)` (brick 3e), using `1 ≤ qⁿ` and `x·qⁿ < 1`
  have hI_eq : ∀ᶠ i in l, I i = LiTwo (b i) - LiTwo x := by
    filter_upwards [hq1, hb1] with i hqi hbi
    have h1c : (1 : ℝ) ≤ q i ^ n i := one_le_pow₀ hqi.le
    simpa [hI_def, hb_def] using integral_one_to_c_eq_LiTwo_sub hx0 h1c hbi
  -- `I → π²/6 − Li₂(x)` via the Abel limit `Li₂(·) → π²/6` composed with `x·qⁿ → 1⁻`
  have hI_tendsto : Tendsto I l (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
    have hLi : Tendsto (fun i => LiTwo (b i)) l (𝓝 (Real.pi ^ 2 / 6)) :=
      tendsto_LiTwo_nhdsWithin_lt_one.comp hxqn
    refine (hLi.sub_const (LiTwo x)).congr' ?_
    exact hI_eq.mono fun i hi => hi.symm
  -- the error `E i = I i − S i`, non-negative and bounded above by `Ubound i`
  set Ub : ι → ℝ := fun i =>
    q i ^ n i * (q i - 1) *
      ((-Real.log (1 - x * q i ^ n i) / q i ^ n i) - (-Real.log (1 - x * 1) / 1)) with hUb_def
  have hErr : ∀ᶠ i in l, 0 ≤ I i - S i ∧ I i - S i ≤ Ub i := by
    filter_upwards [hq1, hb1] with i hqi hbi
    have := riemann_error_bound_up hx0 hqi (n i) hbi
    simpa [hI_def, hS_def, hUb_def] using this
  -- the boundary term `TermA i = (q i − 1)·(−log(1 − x·qⁿ)) → 0` (no-resonance seed)
  have hTermA : Tendsto (fun i => (q i - 1) * (-Real.log (1 - b i))) l (𝓝 0) := by
    have hw0 : ∀ᶠ i in l, 0 < q i - 1 := hq1.mono fun i hi => by linarith
    have hδ1 : ∀ᶠ i in l, (1 - b i) < 1 := by
      filter_upwards [hq0] with i hqi
      have : 0 < b i := by positivity
      linarith
    have hδlim : Tendsto (fun i => 1 - b i) l (𝓝[>] (0 : ℝ)) := by
      rw [tendsto_nhdsWithin_iff]
      constructor
      · have := (tendsto_const_nhds (x := (1 : ℝ)) (f := l)).sub
          (hxqn.mono_right nhdsWithin_le_nhds)
        simpa using this
      · filter_upwards [hb1] with i hbi
        simp only [Set.mem_Ioi]; linarith
    exact boundary_term_vanishes hc hw0 hδ1 hbound hδlim
  -- the second piece `TermB i = qⁿ(q−1)·(−log(1−x)) → 0` (`qⁿ → 1/x` bounded, `q−1 → 0`)
  have hqn_tendsto : Tendsto (fun i => q i ^ n i) l (𝓝 x⁻¹) := by
    have hbnh : Tendsto b l (𝓝 (1 : ℝ)) := hxqn.mono_right nhdsWithin_le_nhds
    have := hbnh.const_mul x⁻¹
    have heq : ∀ᶠ i in l, x⁻¹ * b i = q i ^ n i := by
      filter_upwards with i; rw [hb_def]; field_simp
    refine (this.congr' heq).mono_right (le_of_eq ?_)
    rw [mul_one]
  have hTermB : Tendsto (fun i => q i ^ n i * (q i - 1) * (-Real.log (1 - x * 1) / 1)) l (𝓝 0) := by
    have hqm1 : Tendsto (fun i => q i - 1) l (𝓝 0) := by
      simpa using hq.sub_const 1
    have : Tendsto (fun i => q i ^ n i * (q i - 1)) l (𝓝 0) := by
      simpa using hqn_tendsto.mul hqm1
    simpa using this.mul_const (-Real.log (1 - x * 1) / 1)
  -- `Ub = TermA − TermB` eventually, so `Ub → 0`
  have hUb_tendsto : Tendsto Ub l (𝓝 0) := by
    have hcong : ∀ᶠ i in l, Ub i =
        (q i - 1) * (-Real.log (1 - b i))
          - q i ^ n i * (q i - 1) * (-Real.log (1 - x * 1) / 1) := by
      filter_upwards [hq0] with i hqi
      have hpow : q i ^ n i ≠ 0 := ne_of_gt (pow_pos hqi _)
      rw [hUb_def, hb_def]; field_simp
    have : Tendsto
        (fun i => (q i - 1) * (-Real.log (1 - b i))
          - q i ^ n i * (q i - 1) * (-Real.log (1 - x * 1) / 1)) l (𝓝 (0 - 0)) :=
      hTermA.sub hTermB
    rw [sub_zero] at this
    exact this.congr' (hcong.mono fun i hi => hi.symm)
  -- squeeze: `E = I − S → 0`
  have hE_tendsto : Tendsto (fun i => I i - S i) l (𝓝 0) := by
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hUb_tendsto ?_ ?_
    · exact hErr.mono fun i hi => hi.1
    · exact hErr.mono fun i hi => hi.2
  -- `S = I − E → (π²/6 − Li₂ x) − 0`
  have hS_tendsto : Tendsto S l (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
    have : Tendsto (fun i => I i - (I i - S i)) l (𝓝 ((Real.pi ^ 2 / 6 - LiTwo x) - 0)) :=
      hI_tendsto.sub hE_tendsto
    simpa using this
  -- the W-P1 sum equals `−S` (brick 3d), so it tends to `−(π²/6 − Li₂ x) = Li₂ x − π²/6`
  have hWP1_eq : ∀ᶠ i in l,
      (q i - 1) * ∑ k ∈ Finset.range (n i), Real.log (1 - x * q i ^ k) = - S i := by
    filter_upwards [hq0] with i hqi
    have := partialSum_up_eq (x := x) (q := q i) hqi (n i)
    rw [hS_def]
    simp only at this ⊢
    rw [this]; ring
  have hneg : Tendsto (fun i => - S i) l (𝓝 (LiTwo x - Real.pi ^ 2 / 6)) := by
    have := hS_tendsto.neg
    simpa [neg_sub] using this
  exact hneg.congr' (hWP1_eq.mono fun i hi => hi.symm)

end QOU.Archimedean
