import QOU.Archimedean.DilogPartBBranchPointSum
import QOU.Archimedean.DilogReflection

/-!
# Part B of `conj:dilogarithm-archimedean-limit` — the INNER bulk-closure limit (W-P1)

The `wp1_riemann_bound` of `DilogPartBBranchPointSum` (PR #4262, sorry-free) sandwiches
the positive-factor rescaled log-sum `(1−q)·Σ_{k<n} log(1−xqᵏ)` against the dilog
difference `Li₂(xqⁿ) − Li₂(x)` with an explicit boundary-decomposition error, for any
`1 < q` and `x qⁿ < 1`:

`0 ≤ (Li₂(xqⁿ) − Li₂(x)) − (1−q)Σ log(1−xqᵏ)`
`  ≤ (q−1)·(−log(1−xqⁿ)) − (q−1)·qⁿ·(−log(1−x))`.

The **iterated-limit** reading of W-P1 (coordination ledger
`docs/coordination/dilog-part-b-cusp-attack.md`, PR #4299, numerical probe
`computations/probes/dilog_partb_iterated_limit_probe.py`, exit 0) closes the residual
**without any Diophantine / no-resonance hypothesis** by taking the two limits in order:

* **INNER (this file, bulk):** fix `x ∈ (0,1)` and a target `ρ ∈ (x,1)` *interior*, and
  choose `n(q) = ⌊log(ρ/x)/log q⌋` — the largest `n` with `x qⁿ ≤ ρ`.  Because `ρ` stays
  bounded away from the branch point `u = 1/x`, the endpoint converges *cleanly*:
  `ρ/q < x q^{n(q)} ≤ ρ`, so `x q^{n(q)} → ρ⁻` as `q → 1⁺` (the floor error `frac·log q`
  is absorbed by the `1/q → 1` factor — **no oscillation**, which is exactly what the
  interior `ρ` buys over the branch-point `n = ⌊log_q(1/x)⌋`).  Then `Li₂(x q^{n(q)}) →
  Li₂(ρ)` by continuity of `Li₂` on `(0,1)`, and the `wp1_riemann_bound` majorant `→ 0`
  because `−log(1 − x q^{n(q)}) ≤ −log(1 − ρ)` is **bounded** (the Diophantine subtlety
  is sidestepped).  Hence

      `−(1−q)·Σ_{k<n(q)} log(1−xqᵏ)  ⟶  Li₂(x) − Li₂(ρ)`   as `q → 1⁺`.

* **OUTER (sibling / follow-up):** `Li₂(x) − Li₂(ρ) → Li₂(x) − π²/6` as `ρ → 1⁻`, by the
  Abel / left-continuity brick `tendsto_LiTwo_nhdsWithin_lt_one` (sorry-free,
  `DilogReflection.lean`).  The composite iterated limit is the W-P1 target `Li₂(x) −
  π²/6` with **no** Diophantine input — the honest closeable route.

This file provides the INNER brick, sorry-free:

* `nOfQ` — the bulk floor index `n(q) = ⌊log(ρ/x)/log q⌋₊`.
* `nOfQ_mul_pow_le` / `nOfQ_mul_pow_gt` — the two-sided endpoint bracket
  `ρ/q < x q^{n(q)} ≤ ρ` for `1 < q`.
* `tendsto_nOfQ_mul_pow` — the clean endpoint limit `x q^{n(q)} → ρ` in `𝓝[>] 1`.
* `wp1_bulk_tendsto` — the INNER bulk closure `−(1−q)·Σ → Li₂(x) − Li₂(ρ)`.

Everything is over `ℝ` (archimedean — `LiTwo`, `Real.log`, `Real.exp`, and the ordering
`1 < q` live past the substrate→archimedean wall).

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; bean qou-jplv; PR #4299
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.Archimedean

open Filter Topology QOU.QPochhammer

/-- The **bulk floor index** `n(q) = ⌊log(ρ/x)/log q⌋₊` — the largest `n` with
    `x qⁿ ≤ ρ` when `1 < q` and `x < ρ`.  Unlike the branch-point index
    `⌊log_q(1/x)⌋`, the target `ρ` is *interior* (`ρ < 1`), which is what makes the
    endpoint limit oscillation-free. -/
noncomputable def nOfQ (x q ρ : ℝ) : ℕ := ⌊Real.log (ρ / x) / Real.log q⌋₊

/-- **Upper endpoint bound.**  For `0 < x`, `x < ρ`, `1 < q`:  `x · q^{n(q)} ≤ ρ`.
    Floor gives `n(q) ≤ log(ρ/x)/log q`, so `n(q)·log q ≤ log(ρ/x)`, hence
    `q^{n(q)} = exp(n(q)·log q) ≤ exp(log(ρ/x)) = ρ/x`. -/
theorem nOfQ_mul_pow_le {x ρ q : ℝ} (hx0 : 0 < x) (hxρ : x < ρ) (hq1 : 1 < q) :
    x * q ^ (nOfQ x q ρ) ≤ ρ := by
  have hq0 : 0 < q := by linarith
  have ht : 0 < Real.log q := Real.log_pos hq1
  have hρ0 : 0 < ρ := lt_trans hx0 hxρ
  have hρx1 : 1 < ρ / x := (one_lt_div hx0).mpr hxρ
  have hL : 0 < Real.log (ρ / x) := Real.log_pos hρx1
  have hr0 : 0 ≤ Real.log (ρ / x) / Real.log q := le_of_lt (div_pos hL ht)
  have hnle : ((nOfQ x q ρ : ℕ) : ℝ) ≤ Real.log (ρ / x) / Real.log q :=
    Nat.floor_le hr0
  have hnt : ((nOfQ x q ρ : ℕ) : ℝ) * Real.log q ≤ Real.log (ρ / x) :=
    (le_div_iff₀ ht).mp hnle
  have hpow : q ^ (nOfQ x q ρ) = Real.exp (((nOfQ x q ρ : ℕ) : ℝ) * Real.log q) := by
    have h := Real.exp_nat_mul (Real.log q) (nOfQ x q ρ)
    rw [Real.exp_log hq0] at h
    exact h.symm
  have hexpL : Real.exp (Real.log (ρ / x)) = ρ / x := Real.exp_log (by positivity)
  have hq_n_le : q ^ (nOfQ x q ρ) ≤ ρ / x := by
    rw [hpow]
    calc Real.exp (((nOfQ x q ρ : ℕ) : ℝ) * Real.log q)
        ≤ Real.exp (Real.log (ρ / x)) := Real.exp_le_exp.mpr hnt
      _ = ρ / x := hexpL
  calc x * q ^ (nOfQ x q ρ) ≤ x * (ρ / x) := mul_le_mul_of_nonneg_left hq_n_le hx0.le
    _ = ρ := by field_simp

/-- **Lower endpoint bound.**  For `0 < x`, `x < ρ`, `1 < q`:  `ρ/q < x · q^{n(q)}`.
    Floor gives `log(ρ/x)/log q < n(q) + 1`, so `log(ρ/x) − log q < n(q)·log q`, hence
    `q^{n(q)} = exp(n(q)·log q) > exp(log(ρ/x) − log q) = (ρ/x)·(1/q) = ρ/(x q)`, so
    `x q^{n(q)} > ρ/q`. -/
theorem nOfQ_mul_pow_gt {x ρ q : ℝ} (hx0 : 0 < x) (hxρ : x < ρ) (hq1 : 1 < q) :
    ρ / q < x * q ^ (nOfQ x q ρ) := by
  have hq0 : 0 < q := by linarith
  have ht : 0 < Real.log q := Real.log_pos hq1
  have hρ0 : 0 < ρ := lt_trans hx0 hxρ
  have hρx1 : 1 < ρ / x := (one_lt_div hx0).mpr hxρ
  have hlt : Real.log (ρ / x) / Real.log q < ((nOfQ x q ρ : ℕ) : ℝ) + 1 :=
    Nat.lt_floor_add_one _
  have hnt : Real.log (ρ / x) - Real.log q < ((nOfQ x q ρ : ℕ) : ℝ) * Real.log q := by
    have h := (div_lt_iff₀ ht).mp hlt
    rw [add_mul, one_mul] at h
    linarith
  have hpow : q ^ (nOfQ x q ρ) = Real.exp (((nOfQ x q ρ : ℕ) : ℝ) * Real.log q) := by
    have h := Real.exp_nat_mul (Real.log q) (nOfQ x q ρ)
    rw [Real.exp_log hq0] at h
    exact h.symm
  have hexpL : Real.exp (Real.log (ρ / x)) = ρ / x := Real.exp_log (by positivity)
  have hstep : ρ / (x * q) < q ^ (nOfQ x q ρ) := by
    rw [hpow]
    have hmono : Real.exp (Real.log (ρ / x) - Real.log q)
        < Real.exp (((nOfQ x q ρ : ℕ) : ℝ) * Real.log q) := Real.exp_lt_exp.mpr hnt
    have heq : Real.exp (Real.log (ρ / x) - Real.log q) = ρ / (x * q) := by
      rw [Real.exp_sub, hexpL, Real.exp_log hq0]
      field_simp
    rw [heq] at hmono
    exact hmono
  have hval : x * (ρ / (x * q)) = ρ / q := by field_simp
  calc ρ / q = x * (ρ / (x * q)) := hval.symm
    _ < x * q ^ (nOfQ x q ρ) := mul_lt_mul_of_pos_left hstep hx0

/-- **Clean endpoint limit (INNER, bulk).**  For `0 < x`, `x < ρ`, `ρ < 1`, the endpoint
    `x · q^{n(q)}` converges to `ρ` as `q → 1⁺`.  Squeezed between `ρ/q → ρ` (lower,
    `nOfQ_mul_pow_gt`) and the constant `ρ` (upper, `nOfQ_mul_pow_le`).  The absence of
    oscillation — the whole point of the bulk route — is visible in the `ρ/q` lower
    envelope tending to `ρ` cleanly. -/
theorem tendsto_nOfQ_mul_pow {x ρ : ℝ} (hx0 : 0 < x) (hxρ : x < ρ) (_hρ1 : ρ < 1) :
    Tendsto (fun q => x * q ^ (nOfQ x q ρ)) (𝓝[>] (1 : ℝ)) (𝓝 ρ) := by
  have hlow : Tendsto (fun q : ℝ => ρ / q) (𝓝[>] (1 : ℝ)) (𝓝 ρ) := by
    have h : Tendsto (fun q : ℝ => ρ / q) (𝓝 (1 : ℝ)) (𝓝 (ρ / 1)) :=
      (tendsto_const_nhds).div tendsto_id (by norm_num)
    rw [div_one] at h
    exact h.mono_left nhdsWithin_le_nhds
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlow tendsto_const_nhds ?_ ?_
  · filter_upwards [self_mem_nhdsWithin] with q hq
    exact (nOfQ_mul_pow_gt hx0 hxρ hq).le
  · filter_upwards [self_mem_nhdsWithin] with q hq
    exact nOfQ_mul_pow_le hx0 hxρ hq

/-- **INNER bulk closure of Dilog Part B W-P1.**  For fixed `x ∈ (0,1)` and a fixed
    *interior* target `ρ ∈ (x,1)`, with the bulk floor index `n(q) = ⌊log(ρ/x)/log q⌋`,
    the positive-factor rescaled log-sum converges to the interior dilog difference

    `−(1−q)·Σ_{k<n(q)} log(1−xqᵏ)  ⟶  Li₂(x) − Li₂(ρ)`   as `q → 1⁺`.

    Proof: `wp1_riemann_bound` gives `0 ≤ (Li₂(xq^{n}) − Li₂ x) − (1−q)Σ ≤ E(q)`.  The
    dilog difference `→ Li₂(ρ) − Li₂ x` (endpoint `x q^{n(q)} → ρ` by
    `tendsto_nOfQ_mul_pow`, then continuity of `Li₂` at the interior `ρ`).  The majorant
    `E(q) = (q−1)(−log(1−xq^{n})) − (q−1)q^{n}(−log(1−x)) → 0` because both boundary
    factors stay **bounded** away from the branch point (`x q^{n} ≤ ρ < 1` and
    `q^{n} ≤ ρ/x`), so the width `q−1 → 0` kills them — **no Diophantine input**.  Hence
    `(1−q)Σ = (Li₂(xq^{n}) − Li₂ x) − [error ∈ [0,E]] → Li₂(ρ) − Li₂ x`, and negating
    gives `Li₂(x) − Li₂(ρ)`.  This is the INNER limit of the iterated-limit route; the
    OUTER `ρ → 1⁻` limit (`Li₂ x − Li₂ ρ → Li₂ x − π²/6`) is the Abel brick
    `tendsto_LiTwo_nhdsWithin_lt_one`. -/
theorem wp1_bulk_tendsto {x ρ : ℝ} (hx0 : 0 < x) (hxρ : x < ρ) (hρ1 : ρ < 1) :
    Tendsto (fun q => -((1 - q) * ∑ k ∈ Finset.range (nOfQ x q ρ),
        Real.log (1 - x * q ^ k))) (𝓝[>] (1 : ℝ)) (𝓝 (LiTwo x - LiTwo ρ)) := by
  have hρ0 : 0 < ρ := lt_trans hx0 hxρ
  have hx1 : x < 1 := lt_trans hxρ hρ1
  have hself : ∀ᶠ q in 𝓝[>] (1 : ℝ), (1 : ℝ) < q := by
    filter_upwards [self_mem_nhdsWithin] with q hq; exact hq
  have hupper : ∀ᶠ q in 𝓝[>] (1 : ℝ), x * q ^ (nOfQ x q ρ) ≤ ρ := by
    filter_upwards [hself] with q hq; exact nOfQ_mul_pow_le hx0 hxρ hq
  have hbelow : ∀ᶠ q in 𝓝[>] (1 : ℝ), x * q ^ (nOfQ x q ρ) < 1 := by
    filter_upwards [hupper] with q hq; linarith
  -- endpoint limit x q^{n(q)} → ρ
  have hxqn := tendsto_nOfQ_mul_pow hx0 hxρ hρ1
  -- q − 1 → 0
  have hq1_sub : Tendsto (fun q : ℝ => q - 1) (𝓝[>] (1 : ℝ)) (𝓝 0) := by
    have h : Tendsto (fun q : ℝ => q - 1) (𝓝 (1 : ℝ)) (𝓝 (1 - 1)) := tendsto_id.sub_const 1
    simp only [sub_self] at h
    exact h.mono_left nhdsWithin_le_nhds
  -- D(q) = Li₂(x q^{n(q)}) − Li₂ x → Li₂ ρ − Li₂ x  (continuity of Li₂ at interior ρ)
  have hcontρ : ContinuousAt LiTwo ρ := (hasDerivAt_LiTwo hρ0 hρ1).continuousAt
  have hLcomp : Tendsto (fun q => LiTwo (x * q ^ (nOfQ x q ρ))) (𝓝[>] (1 : ℝ))
      (𝓝 (LiTwo ρ)) := hcontρ.tendsto.comp hxqn
  have hD : Tendsto (fun q => LiTwo (x * q ^ (nOfQ x q ρ)) - LiTwo x) (𝓝[>] (1 : ℝ))
      (𝓝 (LiTwo ρ - LiTwo x)) := hLcomp.sub_const (LiTwo x)
  -- T1 = (q−1)·(−log(1−xq^{n})) → 0  (bounded: −log(1−xq^n) ≤ −log(1−ρ))
  have hT1 : Tendsto (fun q => (q - 1) * (-Real.log (1 - x * q ^ (nOfQ x q ρ))))
      (𝓝[>] (1 : ℝ)) (𝓝 0) := by
    have hub : Tendsto (fun q : ℝ => (q - 1) * (-Real.log (1 - ρ))) (𝓝[>] (1 : ℝ)) (𝓝 0) := by
      have := hq1_sub.mul_const (-Real.log (1 - ρ)); simpa using this
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hub ?_ ?_
    · filter_upwards [hself, hupper] with q hq hqu
      have hqnn : 0 ≤ q - 1 := by linarith
      have hxqn_pos : 0 < x * q ^ (nOfQ x q ρ) := mul_pos hx0 (pow_pos (by linarith) _)
      have hlognonpos : Real.log (1 - x * q ^ (nOfQ x q ρ)) ≤ 0 :=
        Real.log_nonpos (by linarith) (by linarith)
      exact mul_nonneg hqnn (by linarith)
    · filter_upwards [hself, hupper] with q hq hqu
      have hqnn : 0 ≤ q - 1 := by linarith
      have h1ρ : (0 : ℝ) < 1 - ρ := by linarith
      have h1ρle : 1 - ρ ≤ 1 - x * q ^ (nOfQ x q ρ) := by linarith
      have hlogle : Real.log (1 - ρ) ≤ Real.log (1 - x * q ^ (nOfQ x q ρ)) :=
        Real.log_le_log h1ρ h1ρle
      exact mul_le_mul_of_nonneg_left (by linarith) hqnn
  -- T2 = (q−1)·q^{n}·(−log(1−x·1)) → 0  (bounded: q^{n} ≤ ρ/x)
  have hT2 : Tendsto (fun q => (q - 1) * q ^ (nOfQ x q ρ) * (-Real.log (1 - x * 1)))
      (𝓝[>] (1 : ℝ)) (𝓝 0) := by
    have hub : Tendsto (fun q : ℝ => (q - 1) * ((ρ / x) * (-Real.log (1 - x * 1))))
        (𝓝[>] (1 : ℝ)) (𝓝 0) := by
      have := hq1_sub.mul_const ((ρ / x) * (-Real.log (1 - x * 1))); simpa using this
    have hlognn : 0 ≤ -Real.log (1 - x * 1) := by
      have : Real.log (1 - x * 1) ≤ 0 := Real.log_nonpos (by nlinarith) (by nlinarith)
      linarith
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hub ?_ ?_
    · filter_upwards [hself] with q hq
      have hqnn : 0 ≤ q - 1 := by linarith
      have hqn_nn : 0 ≤ q ^ (nOfQ x q ρ) := le_of_lt (pow_pos (by linarith) _)
      exact mul_nonneg (mul_nonneg hqnn hqn_nn) hlognn
    · filter_upwards [hself, hupper] with q hq hqu
      have hqnn : 0 ≤ q - 1 := by linarith
      have hqn_le : q ^ (nOfQ x q ρ) ≤ ρ / x := by
        rw [le_div_iff₀ hx0]; nlinarith [hqu]
      calc (q - 1) * q ^ (nOfQ x q ρ) * (-Real.log (1 - x * 1))
          ≤ (q - 1) * (ρ / x) * (-Real.log (1 - x * 1)) :=
            mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hqn_le hqnn) hlognn
        _ = (q - 1) * ((ρ / x) * (-Real.log (1 - x * 1))) := by ring
  -- E = T1 − T2 → 0
  have hE : Tendsto (fun q => (q - 1) * (-Real.log (1 - x * q ^ (nOfQ x q ρ)))
      - (q - 1) * q ^ (nOfQ x q ρ) * (-Real.log (1 - x * 1))) (𝓝[>] (1 : ℝ)) (𝓝 0) := by
    have h := hT1.sub hT2
    rwa [sub_zero] at h
  -- err(q) = D(q) − (1−q)Σ → 0  (squeezed by wp1_riemann_bound between 0 and E)
  have herr : Tendsto (fun q => (LiTwo (x * q ^ (nOfQ x q ρ)) - LiTwo x)
      - (1 - q) * ∑ k ∈ Finset.range (nOfQ x q ρ), Real.log (1 - x * q ^ k))
      (𝓝[>] (1 : ℝ)) (𝓝 0) := by
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hE ?_ ?_
    · filter_upwards [hself, hbelow] with q hq hb
      exact (wp1_riemann_bound hx0 hq (nOfQ x q ρ) hb).1
    · filter_upwards [hself, hbelow] with q hq hb
      exact (wp1_riemann_bound hx0 hq (nOfQ x q ρ) hb).2
  -- Sraw = D − err → (Li₂ ρ − Li₂ x) − 0
  have hSraw : Tendsto (fun q => (1 - q) * ∑ k ∈ Finset.range (nOfQ x q ρ),
      Real.log (1 - x * q ^ k)) (𝓝[>] (1 : ℝ)) (𝓝 (LiTwo ρ - LiTwo x)) := by
    have hcomb := hD.sub herr
    rw [sub_zero] at hcomb
    exact hcomb.congr (fun q => by ring)
  -- target = −Sraw → −(Li₂ ρ − Li₂ x) = Li₂ x − Li₂ ρ
  have hfin := hSraw.neg
  rw [show -(LiTwo ρ - LiTwo x) = LiTwo x - LiTwo ρ from by ring] at hfin
  exact hfin

/-- **OUTER limit (`ρ → 1⁻`) of the iterated-limit route.**  The INNER bulk value
    `Li₂(x) − Li₂(ρ)` (the limit of `wp1_bulk_tendsto` for each fixed interior `ρ`)
    tends to the W-P1 target `Li₂(x) − π²/6` as `ρ → 1⁻`, by the sorry-free Abel /
    left-continuity brick `tendsto_LiTwo_nhdsWithin_lt_one` (`Li₂ → π²/6`).  Composing
    with `wp1_bulk_tendsto` realises the **iterated limit**

    `lim_{ρ→1⁻} lim_{q→1⁺} −(1−q)·Σ_{k<n(q)} log(1−xqᵏ)  =  Li₂(x) − π²/6`,

    the W-P1 target, with **no Diophantine input**.  (Combined with W-P2, the
    Dedekind-eta asymptotic of `DilogPartBEulerTail`, this gives the Part-B total
    `reg_n → Li₂(x) − π²/3` under the iterated ordering.  The iterated limit is a
    *weaker* statement than the joint `q→1⁺ × n→∞` limit, whose unconditional pointwise
    form is proved-false; see the coordination ledger.) -/
theorem wp1_outer_tendsto (x : ℝ) :
    Tendsto (fun ρ => LiTwo x - LiTwo ρ) (𝓝[<] (1 : ℝ))
      (𝓝 (LiTwo x - Real.pi ^ 2 / 6)) :=
  tendsto_const_nhds.sub tendsto_LiTwo_nhdsWithin_lt_one

end QOU.Archimedean
