import QOU.Archimedean.DilogPartBBranchPointSum

/-!
# Part B of `conj:dilogarithm-archimedean-limit` — the W-P1 branch-point limit

The `wp1_riemann_bound` of `DilogPartBBranchPointSum` sandwiches the
positive-factor rescaled log-sum `(1−q)·Σ_{k<n} log(1−xqᵏ)` against the dilog
difference `Li₂(xqⁿ) − Li₂(x)` with an explicit boundary-decomposition error:

`0 ≤ (Li₂(xqⁿ) − Li₂(x)) − (1−q)Σ log(1−xqᵏ)`
`  ≤ (q−1)·(−log(1−xqⁿ)) − (q−1)·qⁿ·(−log(1−x))`.

As `q → 1⁺` along a branch-point scaling `x qⁿ → 1⁻`, the Abel limit
`tendsto_LiTwo_nhdsWithin_lt_one` gives `Li₂(xqⁿ) → π²/6`, so the whole W-P1 sum
converges to `π²/6 − Li₂(x)` **iff** the single scalar boundary term
`(q−1)·log(1−xqⁿ) → 0`.

**This file does not fabricate that scalar limit.**  Per bean `qou-jplv`, the
general limit is genuinely open: with the branch-point index
`n = ⌊log_q(1/x)⌋` one controls only the *upper* bound `1 − xqⁿ ≤ (q−1)/q`,
never the lower bound; `1 − xqⁿ` is governed by `frac(log_q(1/x))`, which
oscillates, so the limit holds only under a Faddeev-scaling / Diophantine
no-resonance hypothesis on `x` — analytic number theory, not a brick.

Accordingly this file provides the two *honest* pieces:

* `wp1_tendsto_of_boundary` — the full assembly `(1−q)Σ log(1−xqᵏ) → π²/6 − Li₂(x)`
  stated **conditionally** on the named boundary-vanishing hypothesis
  `(q−1)·log(1−xqⁿ) → 0` (the §3b-cond pattern: the open analytic input is an
  explicit hypothesis, never assumed away).  The error squeeze and the
  always-vanishing bulk term `(q−1)qⁿ log(1−x) → 0` are discharged unconditionally.
* `boundary_tendsto_zero_of_bounded` — the trivial *bulk* sub-case: whenever the
  scaling stays bounded away from the branch point (`x qⁿ ≤ ρ < 1`), the boundary
  hypothesis holds **for free**, so `wp1_tendsto_of_boundary` applies unconditionally
  in the tame regime.  (Away from the branch point the limit is `π²/6 − Li₂(x)`
  only under the *additional* `x qⁿ → 1⁻`; the bulk lemma discharges the
  *boundary hypothesis*, which is what makes it a witness that the hypothesis is
  non-vacuous.)

Everything is over `ℝ` (archimedean — `LiTwo`, `Real.log`, and the boundary
limits live past the substrate→archimedean wall).

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit; bean qou-jplv
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.Archimedean

open Filter Topology QOU.QPochhammer

/-- **The always-vanishing bulk term.**  For `0 < x` and a scaling with
    `x·qⁿ < 1` (so `qⁿ < 1/x` is bounded) and `q → 1⁺`, the second error term
    `(q−1)·qⁿ·(−log(1−x))` tends to `0` — it carries no branch-point singularity,
    only the vanishing width `q−1` times a bounded factor. -/
theorem wp1_bulkTerm_tendsto_zero {x : ℝ} (hx0 : 0 < x)
    {q : ℕ → ℝ} {n : ℕ → ℕ} (hq1 : ∀ j, 1 < q j)
    (hqlim : Tendsto q atTop (𝓝 1)) (hbelow : ∀ j, x * (q j) ^ (n j) < 1) :
    Tendsto (fun j => (q j - 1) * (q j) ^ (n j) * (-Real.log (1 - x * 1))) atTop (𝓝 0) := by
  have hq1sub : Tendsto (fun j => q j - 1) atTop (𝓝 0) := by
    simpa using hqlim.sub_const 1
  have hg : Tendsto (fun j => (q j - 1) * ((1 / x) * |Real.log (1 - x * 1)|)) atTop (𝓝 0) := by
    simpa using hq1sub.mul_const ((1 / x) * |Real.log (1 - x * 1)|)
  refine squeeze_zero_norm (fun j => ?_) hg
  have hqj0 : 0 ≤ q j - 1 := by linarith [hq1 j]
  have hqpos : 0 < q j := by linarith [hq1 j]
  have hqn0 : 0 < (q j) ^ (n j) := pow_pos hqpos _
  have hqnle : (q j) ^ (n j) ≤ 1 / x := by
    rw [le_div_iff₀ hx0]; nlinarith [hbelow j]
  rw [Real.norm_eq_abs, abs_mul, abs_mul, abs_of_nonneg hqj0, abs_of_pos hqn0, abs_neg]
  have hlog0 : 0 ≤ |Real.log (1 - x * 1)| := abs_nonneg _
  calc (q j - 1) * (q j) ^ (n j) * |Real.log (1 - x * 1)|
      = (q j - 1) * |Real.log (1 - x * 1)| * (q j) ^ (n j) := by ring
    _ ≤ (q j - 1) * |Real.log (1 - x * 1)| * (1 / x) := by
        gcongr
    _ = (q j - 1) * ((1 / x) * |Real.log (1 - x * 1)|) := by ring

/-- **W-P1 branch-point limit — conditional on the boundary term vanishing.**
    Along any scaling `(q_j, n_j)` with `q_j → 1⁺`, `x q_j^{n_j} < 1`, and
    `x q_j^{n_j} → 1⁻` (branch point), the positive-factor rescaled log-sum
    converges to `π²/6 − Li₂(x)` **provided** the single scalar boundary term
    `(q_j − 1)·log(1 − x q_j^{n_j}) → 0`.  The proof squeezes the
    `wp1_riemann_bound` error to `0`; the boundary hypothesis is the only
    non-derived input (the open Faddeev/Diophantine limit), threaded explicitly. -/
theorem wp1_tendsto_of_boundary {x : ℝ} (hx0 : 0 < x)
    {q : ℕ → ℝ} {n : ℕ → ℕ} (hq1 : ∀ j, 1 < q j)
    (hqlim : Tendsto q atTop (𝓝 1)) (hbelow : ∀ j, x * (q j) ^ (n j) < 1)
    (habel : Tendsto (fun j => x * (q j) ^ (n j)) atTop (𝓝[<] (1 : ℝ)))
    (hbdry : Tendsto (fun j => (q j - 1) * Real.log (1 - x * (q j) ^ (n j))) atTop (𝓝 0)) :
    Tendsto (fun j => (1 - q j) * ∑ k ∈ Finset.range (n j), Real.log (1 - x * (q j) ^ k))
      atTop (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
  -- the dilog difference tends to π²/6 − Li₂(x) via Abel
  have hD : Tendsto (fun j => LiTwo (x * (q j) ^ (n j)) - LiTwo x) atTop
      (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
    have hcomp : Tendsto (fun j => LiTwo (x * (q j) ^ (n j))) atTop (𝓝 (Real.pi ^ 2 / 6)) :=
      tendsto_LiTwo_nhdsWithin_lt_one.comp habel
    simpa using hcomp.sub_const (LiTwo x)
  -- the boundary error term tends to 0
  have ht1 : Tendsto (fun j => (q j - 1) * (-Real.log (1 - x * (q j) ^ (n j)))) atTop (𝓝 0) := by
    have := hbdry.neg
    simpa [mul_neg] using this
  -- the bulk error term tends to 0
  have ht2 := wp1_bulkTerm_tendsto_zero hx0 hq1 hqlim hbelow
  -- the whole majorant E tends to 0
  have hE : Tendsto (fun j => (q j - 1) * (-Real.log (1 - x * (q j) ^ (n j)))
      - (q j - 1) * (q j) ^ (n j) * (-Real.log (1 - x * 1))) atTop (𝓝 0) := by
    simpa using ht1.sub ht2
  -- squeeze the wp1 error to 0
  have herr : Tendsto (fun j => (LiTwo (x * (q j) ^ (n j)) - LiTwo x)
      - (1 - q j) * ∑ k ∈ Finset.range (n j), Real.log (1 - x * (q j) ^ k)) atTop (𝓝 0) := by
    refine squeeze_zero (fun j => ?_) (fun j => ?_) hE
    · exact (wp1_riemann_bound hx0 (hq1 j) (n j) (hbelow j)).1
    · exact (wp1_riemann_bound hx0 (hq1 j) (n j) (hbelow j)).2
  -- S = D − err, so S → (π²/6 − Li₂ x) − 0
  have key : Tendsto (fun j => (LiTwo (x * (q j) ^ (n j)) - LiTwo x)
      - ((LiTwo (x * (q j) ^ (n j)) - LiTwo x)
        - (1 - q j) * ∑ k ∈ Finset.range (n j), Real.log (1 - x * (q j) ^ k)))
      atTop (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
    simpa using hD.sub herr
  exact key.congr (fun j => by ring)

/-- **Bulk sub-case — the boundary hypothesis holds for free away from the branch
    point.**  If the scaling stays bounded below the branch point (`x qⁿ ≤ ρ < 1`),
    then `1 − x qⁿ ≥ 1 − ρ > 0`, so `log(1 − x qⁿ)` is bounded and the boundary
    term `(q − 1)·log(1 − x qⁿ) → 0` unconditionally as `q → 1⁺`.  This discharges
    the `hbdry` hypothesis of `wp1_tendsto_of_boundary` in the tame regime,
    witnessing that the hypothesis is non-vacuous. -/
theorem boundary_tendsto_zero_of_bounded {x ρ : ℝ} (hx0 : 0 < x)
    {q : ℕ → ℝ} {n : ℕ → ℕ} (hq1 : ∀ j, 1 < q j)
    (hqlim : Tendsto q atTop (𝓝 1)) (hρ : ρ < 1)
    (hbound : ∀ j, x * (q j) ^ (n j) ≤ ρ) :
    Tendsto (fun j => (q j - 1) * Real.log (1 - x * (q j) ^ (n j))) atTop (𝓝 0) := by
  have hq1sub : Tendsto (fun j => q j - 1) atTop (𝓝 0) := by
    simpa using hqlim.sub_const 1
  have hg : Tendsto (fun j => (q j - 1) * (-Real.log (1 - ρ))) atTop (𝓝 0) := by
    simpa using hq1sub.mul_const (-Real.log (1 - ρ))
  refine squeeze_zero_norm (fun j => ?_) hg
  have hqj0 : 0 ≤ q j - 1 := by linarith [hq1 j]
  have hqpos : 0 < q j := by linarith [hq1 j]
  have hqn0 : 0 < (q j) ^ (n j) := pow_pos hqpos _
  have hxqn0 : 0 < x * (q j) ^ (n j) := mul_pos hx0 hqn0
  have hxqnρ : x * (q j) ^ (n j) ≤ ρ := hbound j
  have h1ρ : (0 : ℝ) < 1 - ρ := by linarith
  have h1qn : (0 : ℝ) < 1 - x * (q j) ^ (n j) := by linarith
  have h1qnle : (1 : ℝ) - x * (q j) ^ (n j) ≤ 1 := by linarith
  have h1ρle : (1 : ℝ) - ρ ≤ 1 - x * (q j) ^ (n j) := by linarith
  -- log is nonpositive on (0,1]; bounded below by log(1−ρ)
  have hlognonpos : Real.log (1 - x * (q j) ^ (n j)) ≤ 0 :=
    Real.log_nonpos (by linarith) h1qnle
  have hloglb : Real.log (1 - ρ) ≤ Real.log (1 - x * (q j) ^ (n j)) :=
    Real.log_le_log h1ρ h1ρle
  have hlogbnd : |Real.log (1 - x * (q j) ^ (n j))| ≤ -Real.log (1 - ρ) := by
    rw [abs_of_nonpos hlognonpos]; linarith
  have hneglog0 : (0 : ℝ) ≤ -Real.log (1 - ρ) := by
    have := Real.log_nonpos (by linarith) (by linarith : (1 : ℝ) - ρ ≤ 1)
    linarith
  rw [Real.norm_eq_abs, abs_mul, abs_of_nonneg hqj0]
  gcongr

/-- **No-resonance boundary vanishing.**  The genuine branch-point regime.  If the
    scaling keeps the branch-point gap *comparable to the cell width* — a lower
    bound `c·(q−1) ≤ 1 − x qⁿ` for some fixed `c > 0` (the Faddeev / Diophantine
    no-resonance condition: the branch point does not fall super-exponentially
    close to a lattice node `qᵏ`) — then the boundary term `(q−1)·log(1−xqⁿ) → 0`
    unconditionally as `q → 1⁺`.  This is where the general limit *fails* without a
    hypothesis (bean qou-jplv): only the upper bound `1 − xqⁿ ≤ (q−1)/q` is
    automatic; this lemma supplies the missing lower bound and closes the term via
    the `t·log t → 0` squeeze `(q−1)·log(c(q−1)) ≤ (q−1)·log(1−xqⁿ) ≤ 0`. -/
theorem boundary_tendsto_zero_of_noResonance {x c : ℝ} (hx0 : 0 < x) (hc : 0 < c)
    {q : ℕ → ℝ} {n : ℕ → ℕ} (hq1 : ∀ j, 1 < q j)
    (hqlim : Tendsto q atTop (𝓝 1)) (hbelow : ∀ j, x * (q j) ^ (n j) < 1)
    (hlb : ∀ j, c * (q j - 1) ≤ 1 - x * (q j) ^ (n j)) :
    Tendsto (fun j => (q j - 1) * Real.log (1 - x * (q j) ^ (n j))) atTop (𝓝 0) := by
  -- `s log s → 0` as `s → 0⁺`
  have hbase : Tendsto (fun u : ℝ => Real.log u * u) (𝓝[>] (0 : ℝ)) (𝓝 0) := by
    have h0 := tendsto_log_mul_rpow_nhdsGT_zero (r := 1) one_pos
    refine h0.congr' (Filter.Eventually.of_forall (fun u => ?_))
    rw [Real.rpow_one]
  have hq1sub : Tendsto (fun j => q j - 1) atTop (𝓝 0) := by
    simpa using hqlim.sub_const 1
  -- `s_j = c·(q_j − 1) → 0⁺`
  have hsGT : Tendsto (fun j => c * (q j - 1)) atTop (𝓝[>] (0 : ℝ)) := by
    refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
    · simpa using hq1sub.const_mul c
    · exact Filter.Eventually.of_forall
        (fun j => by simp only [Set.mem_Ioi]; exact mul_pos hc (by linarith [hq1 j]))
  have hslog : Tendsto (fun j => Real.log (c * (q j - 1)) * (c * (q j - 1))) atTop (𝓝 0) :=
    hbase.comp hsGT
  -- the lower squeeze function `g_lo j = (q_j − 1)·log(c(q_j − 1)) → 0`
  have hglo : Tendsto (fun j => (q j - 1) * Real.log (c * (q j - 1))) atTop (𝓝 0) := by
    have h := hslog.const_mul (1 / c)
    simp only [mul_zero] at h
    refine h.congr (fun j => ?_)
    rw [one_div, mul_comm (Real.log (c * (q j - 1))) (c * (q j - 1)), ← mul_assoc,
      inv_mul_cancel_left₀ hc.ne']
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le hglo tendsto_const_nhds
    (fun j => ?_) (fun j => ?_)
  · -- g_lo j ≤ term j : monotone log on `c(q−1) ≤ 1 − xqⁿ`, scaled by `q−1 ≥ 0`
    have hqj0 : 0 ≤ q j - 1 := by linarith [hq1 j]
    have hs0 : 0 < c * (q j - 1) := mul_pos hc (by linarith [hq1 j])
    exact mul_le_mul_of_nonneg_left (Real.log_le_log hs0 (hlb j)) hqj0
  · -- term j ≤ 0 : `q − 1 ≥ 0` and `log(1 − xqⁿ) ≤ 0`
    have hqpos : 0 < q j := by linarith [hq1 j]
    have hxqn0 : 0 < x * (q j) ^ (n j) := mul_pos hx0 (pow_pos hqpos _)
    have hlognonpos : Real.log (1 - x * (q j) ^ (n j)) ≤ 0 :=
      Real.log_nonpos (by linarith [hbelow j]) (by linarith)
    exact mul_nonpos_iff.mpr (Or.inl ⟨by linarith [hq1 j], hlognonpos⟩)

/-- **W-P1 branch-point limit under no resonance.**  Combining the two branch-point
    controls — the automatic upper bound `1 − xqⁿ ≤ (q−1)/q` (the branch-point cell
    `n = ⌊log_q(1/x)⌋`) and the no-resonance lower bound `c·(q−1) ≤ 1 − xqⁿ` — the
    positive-factor rescaled log-sum converges to `π²/6 − Li₂(x)`.  The upper bound
    forces `x qⁿ → 1⁻` (branch point, so `Li₂(xqⁿ) → π²/6` by Abel); the lower bound
    kills the boundary error (`boundary_tendsto_zero_of_noResonance`).  No opaque
    hypothesis remains — only the geometric no-resonance bound, which *is* the open
    Diophantine input, now stated as a checkable inequality rather than an assumed
    limit. -/
theorem wp1_tendsto_of_noResonance {x c : ℝ} (hx0 : 0 < x) (hc : 0 < c)
    {q : ℕ → ℝ} {n : ℕ → ℕ} (hq1 : ∀ j, 1 < q j)
    (hqlim : Tendsto q atTop (𝓝 1)) (hbelow : ∀ j, x * (q j) ^ (n j) < 1)
    (hub : ∀ j, 1 - x * (q j) ^ (n j) ≤ (q j - 1) / q j)
    (hlb : ∀ j, c * (q j - 1) ≤ 1 - x * (q j) ^ (n j)) :
    Tendsto (fun j => (1 - q j) * ∑ k ∈ Finset.range (n j), Real.log (1 - x * (q j) ^ k))
      atTop (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
  -- `(q−1)/q → 0`
  have hqq : Tendsto (fun j => (q j - 1) / q j) atTop (𝓝 0) := by
    have hn : Tendsto (fun j => q j - 1) atTop (𝓝 0) := by simpa using hqlim.sub_const 1
    simpa using hn.div hqlim (by norm_num : (1 : ℝ) ≠ 0)
  -- `1 − xqⁿ → 0` (squeezed by the branch-point upper bound), so `xqⁿ → 1`
  have h1sub : Tendsto (fun j => 1 - x * (q j) ^ (n j)) atTop (𝓝 0) :=
    squeeze_zero (fun j => by linarith [hbelow j]) (fun j => hub j) hqq
  have hxqn : Tendsto (fun j => x * (q j) ^ (n j)) atTop (𝓝 1) := by
    have h := (tendsto_const_nhds (x := (1 : ℝ))).sub h1sub
    simp only [sub_zero] at h
    exact h.congr (fun j => by ring)
  have habel : Tendsto (fun j => x * (q j) ^ (n j)) atTop (𝓝[<] (1 : ℝ)) := by
    refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ hxqn ?_
    exact Filter.Eventually.of_forall (fun j => by simp only [Set.mem_Iio]; exact hbelow j)
  exact wp1_tendsto_of_boundary hx0 hq1 hqlim hbelow habel
    (boundary_tendsto_zero_of_noResonance hx0 hc hq1 hqlim hbelow hlb)

/-- **Non-vacuity at the branch point — an explicit realizing scaling.**  There is a
    concrete branch-point scaling `q_j = ((1 - 1/m_j)/x)^{1/m_j}`, `n_j = m_j`
    (`m_j = j + N₀`, `N₀ > 1/(1-x)`), along which the W-P1 sum converges to
    `π²/6 − Li₂(x)`.  By construction `x q_j^{n_j} = 1 - 1/m_j → 1⁻` (branch point),
    and the no-resonance bound holds with `c = x/\log(1/x)` because
    `q_j - 1 \le (1/x)^{1/m_j} - 1 \le (\log(1/x)/x)\,(1/m_j)` (from `e^t-1 \le t e^t`).
    This witnesses that `wp1_tendsto_of_noResonance` fires at the branch point, not
    only in the bulk — the dilog limit is *attained* along an explicit sequence, with
    the open Diophantine content being only the *general-x uniform* statement. -/
theorem exists_noResonance_branchPoint_scaling {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    ∃ (q : ℕ → ℝ) (n : ℕ → ℕ),
      (∀ j, 1 < q j) ∧ Tendsto q atTop (𝓝 1) ∧ (∀ j, x * (q j) ^ (n j) < 1) ∧
      Tendsto (fun j => (1 - q j) * ∑ k ∈ Finset.range (n j), Real.log (1 - x * (q j) ^ k))
        atTop (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hxinv1 : (1 : ℝ) < 1 / x := by rw [lt_div_iff₀ hx0, one_mul]; exact hx1
  set L : ℝ := Real.log (1 / x) with hL_def
  have hL0 : 0 < L := Real.log_pos hxinv1
  obtain ⟨N₀, hN₀⟩ := exists_nat_gt (1 / (1 - x))
  have hN0R : (1 : ℝ) ≤ (N₀ : ℝ) := by
    have h0 : (0 : ℝ) < 1 / (1 - x) := by positivity
    have : (0 : ℝ) < (N₀ : ℝ) := lt_trans h0 hN₀
    exact_mod_cast Nat.one_le_iff_ne_zero.mpr (by exact_mod_cast this.ne')
  set m : ℕ → ℕ := fun j => j + N₀ with hm_def
  have hmR : ∀ j, (1 / (1 - x)) < (m j : ℝ) := by
    intro j
    have : (N₀ : ℝ) ≤ (m j : ℝ) := by
      simp only [hm_def, Nat.cast_add]; linarith [Nat.cast_nonneg (α := ℝ) j]
    linarith
  have hm_ge1 : ∀ j, (1 : ℝ) ≤ (m j : ℝ) := by
    intro j; simp only [hm_def, Nat.cast_add]; linarith [Nat.cast_nonneg (α := ℝ) j]
  have hm_pos : ∀ j, (0 : ℝ) < (m j : ℝ) := fun j => lt_of_lt_of_le one_pos (hm_ge1 j)
  have h1m_lt : ∀ j, 1 / (m j : ℝ) < 1 - x := by
    intro j
    rw [div_lt_iff₀ (hm_pos j)]
    have := hmR j; rw [div_lt_iff₀ h1x] at this; nlinarith [this]
  set base : ℕ → ℝ := fun j => (1 - 1 / (m j : ℝ)) / x with hbase_def
  set e : ℕ → ℝ := fun j => 1 / (m j : ℝ) with he_def
  set q : ℕ → ℝ := fun j => (base j) ^ (e j) with hq_def
  have he_pos : ∀ j, 0 < e j := fun j => by simp only [he_def]; exact one_div_pos.mpr (hm_pos j)
  have he_le1 : ∀ j, e j ≤ 1 := by
    intro j; simp only [he_def]; rw [div_le_one (hm_pos j)]; exact hm_ge1 j
  have hbase_pos : ∀ j, 0 < base j := by
    intro j; simp only [hbase_def]; exact div_pos (by linarith [h1m_lt j]) hx0
  have hbase_gt1 : ∀ j, 1 < base j := by
    intro j; simp only [hbase_def]; rw [lt_div_iff₀ hx0, one_mul]; linarith [h1m_lt j]
  have hbase_le : ∀ j, base j ≤ 1 / x := by
    intro j; simp only [hbase_def]
    have hnn : (0 : ℝ) ≤ 1 / (m j : ℝ) := by positivity
    gcongr
    linarith [hnn]
  -- q_j > 1
  have hq1 : ∀ j, 1 < q j := by
    intro j; simp only [hq_def]
    exact (Real.one_lt_rpow_iff_of_pos (hbase_pos j)).mpr (Or.inl ⟨hbase_gt1 j, he_pos j⟩)
  -- x·q_j^{n_j} = 1 - 1/m_j
  have hqn_eq : ∀ j, x * (q j) ^ (m j) = 1 - 1 / (m j : ℝ) := by
    intro j
    have hpow : (q j) ^ (m j) = base j := by
      simp only [hq_def]
      rw [← Real.rpow_natCast ((base j) ^ (e j)) (m j), ← Real.rpow_mul (hbase_pos j).le]
      rw [show e j * (m j : ℝ) = 1 from by
        simp only [he_def]; exact one_div_mul_cancel (hm_pos j).ne', Real.rpow_one]
    rw [hpow]; simp only [hbase_def]; field_simp
  have hbelow : ∀ j, x * (q j) ^ (m j) < 1 := by
    intro j; rw [hqn_eq j]; have : 0 < 1 / (m j : ℝ) := one_div_pos.mpr (hm_pos j)
    linarith
  -- 1/m_j → 0, m_j → ∞
  have hm_atTop : Tendsto (fun j => (m j : ℝ)) atTop atTop := by
    have h : Tendsto (fun j : ℕ => (j : ℝ) + (N₀ : ℝ)) atTop atTop :=
      tendsto_atTop_add_const_right _ _ tendsto_natCast_atTop_atTop
    refine h.congr (fun j => ?_)
    simp only [hm_def, Nat.cast_add]
  have he_lim : Tendsto e atTop (𝓝 0) := by
    simp only [he_def, one_div]; exact hm_atTop.inv_tendsto_atTop
  -- q_j → 1
  have hbase_lim : Tendsto base atTop (𝓝 (1 / x)) := by
    have h1 : Tendsto (fun j => 1 - 1 / (m j : ℝ)) atTop (𝓝 1) := by
      have : Tendsto (fun j => 1 / (m j : ℝ)) atTop (𝓝 0) := by
        simp only [one_div]; exact hm_atTop.inv_tendsto_atTop
      simpa using tendsto_const_nhds.sub this
    simpa [hbase_def] using h1.div_const x
  have hqlim : Tendsto q atTop (𝓝 1) := by
    have hcont := Real.continuousAt_rpow (1 / x, 0) (Or.inl (by positivity : (1 / x : ℝ) ≠ 0))
    have hp : Tendsto (fun j => (base j, e j)) atTop (𝓝 (1 / x, 0)) :=
      hbase_lim.prodMk_nhds he_lim
    have := hcont.tendsto.comp hp
    simpa [hq_def, Function.comp, Real.rpow_zero] using this
  -- no-resonance lower bound with c = x/L
  have hlb : ∀ j, (x / L) * (q j - 1) ≤ 1 - x * (q j) ^ (m j) := by
    intro j
    -- q_j - 1 ≤ (L/x)·(1/m_j)
    have hstep1 : q j ≤ (1 / x) ^ (e j) := by
      simp only [hq_def]; exact Real.rpow_le_rpow (hbase_pos j).le (hbase_le j) (he_pos j).le
    have hxinv_pos : (0 : ℝ) < 1 / x := by positivity
    have hrpow_exp : (1 / x) ^ (e j) = Real.exp (L * e j) := by
      rw [Real.rpow_def_of_pos hxinv_pos, hL_def]
    have ht0 : 0 ≤ L * e j := mul_nonneg hL0.le (he_pos j).le
    have hE := Real.exp_pos (L * e j)
    have hexp_bound : Real.exp (L * e j) - 1 ≤ (L * e j) * Real.exp (L * e j) := by
      have h := Real.add_one_le_exp (-(L * e j))
      rw [Real.exp_neg] at h
      have h2 := mul_le_mul_of_nonneg_right h hE.le
      rw [inv_mul_cancel₀ hE.ne'] at h2
      nlinarith [h2]
    have hrpow_self : (1 / x) ^ (e j) ≤ 1 / x := by
      calc (1 / x) ^ (e j) ≤ (1 / x) ^ (1 : ℝ) :=
            Real.rpow_le_rpow_of_exponent_le hxinv1.le (he_le1 j)
        _ = 1 / x := Real.rpow_one _
    have hqm1 : q j - 1 ≤ (L * e j) * (1 / x) := by
      have hchain : Real.exp (L * e j) - 1 ≤ (L * e j) * (1 / x) := by
        calc Real.exp (L * e j) - 1 ≤ (L * e j) * Real.exp (L * e j) := hexp_bound
          _ = (L * e j) * (1 / x) ^ (e j) := by rw [hrpow_exp]
          _ ≤ (L * e j) * (1 / x) := mul_le_mul_of_nonneg_left hrpow_self ht0
      have : q j ≤ Real.exp (L * e j) := by rw [← hrpow_exp]; exact hstep1
      linarith
    -- multiply by c = x/L ≥ 0 and simplify (L·e·(1/x))·(x/L) = e = 1/m
    have hcpos : 0 < x / L := div_pos hx0 hL0
    rw [hqn_eq j, show (1 : ℝ) - (1 - 1 / (m j : ℝ)) = 1 / (m j : ℝ) from by ring]
    have hgoal : (x / L) * (q j - 1) ≤ (x / L) * ((L * e j) * (1 / x)) :=
      mul_le_mul_of_nonneg_left hqm1 hcpos.le
    have hsimp : (x / L) * ((L * e j) * (1 / x)) = 1 / (m j : ℝ) := by
      simp only [he_def]; field_simp
    linarith [hgoal, hsimp.le, hsimp.ge]
  -- assemble: habel + no-resonance boundary vanishing ⇒ W-P1 limit
  have hxqn : Tendsto (fun j => x * (q j) ^ (m j)) atTop (𝓝 1) := by
    have h1 : Tendsto (fun j => 1 - 1 / (m j : ℝ)) atTop (𝓝 1) := by
      have : Tendsto (fun j => 1 / (m j : ℝ)) atTop (𝓝 0) := by
        simp only [one_div]; exact hm_atTop.inv_tendsto_atTop
      simpa using tendsto_const_nhds.sub this
    exact (h1.congr (fun j => (hqn_eq j).symm))
  have habel : Tendsto (fun j => x * (q j) ^ (m j)) atTop (𝓝[<] (1 : ℝ)) := by
    refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ hxqn ?_
    exact Filter.Eventually.of_forall (fun j => by simp only [Set.mem_Iio]; exact hbelow j)
  have hbdry := boundary_tendsto_zero_of_noResonance hx0 (div_pos hx0 hL0) hq1 hqlim hbelow hlb
  exact ⟨q, m, hq1, hqlim, hbelow,
    wp1_tendsto_of_boundary hx0 hq1 hqlim hbelow habel hbdry⟩

/-- **Sharp general form — vanishing at any controllable rate.**  The boundary term
    `(q−1)·log(1−xqⁿ) → 0` whenever the branch-point gap is bounded below by a
    positive `g_j` whose own width-scaled log vanishes, `(q−1)·log(g_j) → 0`.  This is
    the exact envelope of the no-resonance analysis: the term dies precisely when the
    gap does not shrink faster than a rate the width `q−1` can absorb.
    `boundary_tendsto_zero_of_bounded` (`g ≡ 1−ρ`), `_of_noResonance` (`g = c(q−1)`),
    and `_of_powerBound` (`g = c(q−1)^K`) are the constant / linear / polynomial
    special cases. -/
theorem boundary_tendsto_zero_of_rate {x : ℝ} (hx0 : 0 < x)
    {q : ℕ → ℝ} {n : ℕ → ℕ} {g : ℕ → ℝ} (hq1 : ∀ j, 1 < q j)
    (hbelow : ∀ j, x * (q j) ^ (n j) < 1)
    (hg_pos : ∀ j, 0 < g j) (hg_le : ∀ j, g j ≤ 1 - x * (q j) ^ (n j))
    (hrate : Tendsto (fun j => (q j - 1) * Real.log (g j)) atTop (𝓝 0)) :
    Tendsto (fun j => (q j - 1) * Real.log (1 - x * (q j) ^ (n j))) atTop (𝓝 0) := by
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le hrate tendsto_const_nhds
    (fun j => ?_) (fun j => ?_)
  · have hqj0 : 0 ≤ q j - 1 := by linarith [hq1 j]
    exact mul_le_mul_of_nonneg_left (Real.log_le_log (hg_pos j) (hg_le j)) hqj0
  · have hqpos : 0 < q j := by linarith [hq1 j]
    have hxqn0 : 0 < x * (q j) ^ (n j) := mul_pos hx0 (pow_pos hqpos _)
    have hlognonpos : Real.log (1 - x * (q j) ^ (n j)) ≤ 0 :=
      Real.log_nonpos (by linarith [hbelow j]) (by linarith)
    exact mul_nonpos_iff.mpr (Or.inl ⟨by linarith [hq1 j], hlognonpos⟩)

/-- **Polynomial no-resonance — the badly-approximable regime.**  If the branch-point
    gap is bounded below by a fixed power of the cell width, `c·(q−1)^K ≤ 1−xqⁿ`, the
    boundary term still vanishes.  This is what a **Diophantine (badly-approximable)
    `x`** supplies: for `q_j = e^{1/j}` the maximal-cell gap is
    `≈ {j·log(1/x)}·(q_j−1)`, and bounded continued-fraction partial quotients give the
    three-distance lower bound `{j·log(1/x)} ≥ c/j ≈ c(q_j−1)`, i.e. a *quadratic*
    bound `K = 2`.  The `K = 1` case is `boundary_tendsto_zero_of_noResonance`.  Proof
    via `t·log t → 0`, feeding `boundary_tendsto_zero_of_rate`.  (The Diophantine fact
    "badly-approximable ⇒ quadratic gap" is the genuine number-theoretic input and is
    the remaining open piece; here it is the explicit hypothesis `hlb`.) -/
theorem boundary_tendsto_zero_of_powerBound {x c : ℝ} (hx0 : 0 < x) (hc : 0 < c) (K : ℕ)
    {q : ℕ → ℝ} {n : ℕ → ℕ} (hq1 : ∀ j, 1 < q j)
    (hqlim : Tendsto q atTop (𝓝 1)) (hbelow : ∀ j, x * (q j) ^ (n j) < 1)
    (hlb : ∀ j, c * (q j - 1) ^ K ≤ 1 - x * (q j) ^ (n j)) :
    Tendsto (fun j => (q j - 1) * Real.log (1 - x * (q j) ^ (n j))) atTop (𝓝 0) := by
  have hbase : Tendsto (fun u : ℝ => Real.log u * u) (𝓝[>] (0 : ℝ)) (𝓝 0) := by
    have h0 := tendsto_log_mul_rpow_nhdsGT_zero (r := 1) one_pos
    refine h0.congr' (Filter.Eventually.of_forall (fun u => ?_)); rw [Real.rpow_one]
  have hq1sub : Tendsto (fun j => q j - 1) atTop (𝓝 0) := by simpa using hqlim.sub_const 1
  have hsGT : Tendsto (fun j => q j - 1) atTop (𝓝[>] (0 : ℝ)) := by
    refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ hq1sub ?_
    exact Filter.Eventually.of_forall (fun j => by simp only [Set.mem_Ioi]; linarith [hq1 j])
  have hslog : Tendsto (fun j => Real.log (q j - 1) * (q j - 1)) atTop (𝓝 0) := hbase.comp hsGT
  refine boundary_tendsto_zero_of_rate hx0 hq1 hbelow (g := fun j => c * (q j - 1) ^ K)
    (fun j => mul_pos hc (pow_pos (by linarith [hq1 j]) K)) hlb ?_
  have hlim : Tendsto
      (fun j => (q j - 1) * Real.log c + (K : ℝ) * (Real.log (q j - 1) * (q j - 1)))
      atTop (𝓝 0) := by
    have h1 := hq1sub.mul_const (Real.log c)
    have h2 := hslog.const_mul (K : ℝ)
    simpa using h1.add h2
  refine hlim.congr (fun j => ?_)
  have hqp : 0 < q j - 1 := by linarith [hq1 j]
  rw [Real.log_mul hc.ne' (pow_ne_zero K hqp.ne'), Real.log_pow]
  ring

/-- **W-P1 branch-point limit for a Diophantine `x` (polynomial no-resonance).**  As
    `wp1_tendsto_of_noResonance` but with the gap bounded below by any fixed power
    `c·(q−1)^K ≤ 1−xqⁿ` — the regime a badly-approximable `x` provides (`K = 2`).  The
    upper bound forces `xqⁿ → 1⁻` (Abel); the polynomial lower bound kills the boundary
    error.  W-P1 `→ π²/6 − Li₂(x)`. -/
theorem wp1_tendsto_of_powerBound {x c : ℝ} (hx0 : 0 < x) (hc : 0 < c) (K : ℕ)
    {q : ℕ → ℝ} {n : ℕ → ℕ} (hq1 : ∀ j, 1 < q j)
    (hqlim : Tendsto q atTop (𝓝 1)) (hbelow : ∀ j, x * (q j) ^ (n j) < 1)
    (hub : ∀ j, 1 - x * (q j) ^ (n j) ≤ (q j - 1) / q j)
    (hlb : ∀ j, c * (q j - 1) ^ K ≤ 1 - x * (q j) ^ (n j)) :
    Tendsto (fun j => (1 - q j) * ∑ k ∈ Finset.range (n j), Real.log (1 - x * (q j) ^ k))
      atTop (𝓝 (Real.pi ^ 2 / 6 - LiTwo x)) := by
  have hqq : Tendsto (fun j => (q j - 1) / q j) atTop (𝓝 0) := by
    have hn : Tendsto (fun j => q j - 1) atTop (𝓝 0) := by simpa using hqlim.sub_const 1
    simpa using hn.div hqlim (by norm_num : (1 : ℝ) ≠ 0)
  have h1sub : Tendsto (fun j => 1 - x * (q j) ^ (n j)) atTop (𝓝 0) :=
    squeeze_zero (fun j => by linarith [hbelow j]) (fun j => hub j) hqq
  have hxqn : Tendsto (fun j => x * (q j) ^ (n j)) atTop (𝓝 1) := by
    have h := (tendsto_const_nhds (x := (1 : ℝ))).sub h1sub
    simp only [sub_zero] at h
    exact h.congr (fun j => by ring)
  have habel : Tendsto (fun j => x * (q j) ^ (n j)) atTop (𝓝[<] (1 : ℝ)) := by
    refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ hxqn ?_
    exact Filter.Eventually.of_forall (fun j => by simp only [Set.mem_Iio]; exact hbelow j)
  exact wp1_tendsto_of_boundary hx0 hq1 hqlim hbelow habel
    (boundary_tendsto_zero_of_powerBound hx0 hc K hq1 hqlim hbelow hlb)

end QOU.Archimedean
