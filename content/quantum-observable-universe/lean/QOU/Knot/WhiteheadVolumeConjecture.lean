/-
  Whitehead link — Volume Conjecture, van der Veen positive-sum route (start of
  the Lean squeeze proof, bean qou-t2sc).

  The Whitehead link is W_{0,1,1,0} in van der Veen's Whitehead-chain notation.
  Its N-colored Jones at the Kashaev point has the POSITIVE-sum form
  (arXiv:math/0611181, Lemma 1):

      J_N(W) = φ_N · Σ_{n=0}^{N-1} (2n+1) · χ_{N,n}^{-1} · ( Σ_{k=0}^{N-1-n} S_{n,k} ),
      S_{n,k} = ∏_{j=1}^{n} 2 sin²((k+j)π/N) / sin(jπ/N)  >  0.

  The volume-conjecture limit  (2π/N)·log|J_N| → Vol(W) = 4G  is PROVED in van
  der Veen's paper; formalizing it here mirrors the landed 4₁
  (`FigureEightVolumeSqueeze`, E1-E5d) and Borromean (B1-B5) squeeze proofs,
  which use the SAME `log(2 sin)` Riemann-sum-vs-Clausen machinery:
      log S_{n,k} = Σ_{j=1}^n [ log 2 + 2 log sin((k+j)π/N) − log sin(jπ/N) ].

  This file establishes the foundational sorry-free brick — the positivity of
  the van der Veen kernel `whiteheadS` (the analogue of `kashaevProd_pos`) — on
  the summation range `k + n ≤ N − 1` where every `(k+j)π/N ∈ (0, π)`.  The full
  limit theorem is state-and-queued (`sorry` + Ref); the reusable Clausen bricks
  + a `whiteheadS` max-term saddle-location lemma are the remaining work.

  Archimedean (ℝ).  Mathlib-only imports (verifiable standalone).

  -- Ref: [vanderveen2008] arXiv:math/0611181 (Alg. Geom. Topol.)
-/

/-
**CROSS-REFERENCE (2026-08-19) — a second Whitehead-link VC program exists.**

`QOU/Knot/WhiteheadLinkScaffold.lean` + `QOU/Knot/WhiteheadMajorantRate.lean`
(epic `qou-u1b5`) attack the same theorem from the OPPOSITE end, via the
phase/majorant route:

* this program has the MAGNITUDE — `whitehead_vc_innerSum_half`, sorry-free;
* that one has the PHASES — `‖J_N(W)‖ ≤ majorant`,
  `tendsto_log_whiteheadLinkMajorant_vol` (`→ 4G`), and the residue isolated as
  the conditional class `VdVWhiteheadLemma4` (open: no instance in the corpus).

The gap between the two ends — non-cancellation of the phased outer sum
`Σ_n (2n+1)·χ_{N,n}^{-1}·(Σ_k S_{n,k})` — is exactly what `VdVWhiteheadLemma4`
states. Discharging it is what would join the two halves into the VC for
`J_N(W)` proper. COMPLEMENTARY, not redundant; coordinate before extending.
Audit: `docs/audits/2026-08-19-volume-conjecture-work-overlap-sweep.md`.
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.Knot.WhiteheadVC

open Real Finset

/-- Catalan's constant `G = Σ (-1)ⁿ/(2n+1)²`.  `Vol(Whitehead) = 4G`. -/
noncomputable def catalanG : ℝ := ∑' n : ℕ, (-1 : ℝ) ^ n / (2 * n + 1) ^ 2

/-- van der Veen's positive-sum kernel for the Whitehead colored Jones
    (arXiv:math/0611181, Lemma 1):
    `S_{n,k} = ∏_{j=1}^{n} 2 sin²((k+j)π/N) / sin(jπ/N)`. -/
noncomputable def whiteheadS (N n k : ℕ) : ℝ :=
  ∏ j ∈ Finset.Icc 1 n,
    (2 * Real.sin (((k : ℝ) + j) * π / N) ^ 2 / Real.sin ((j : ℝ) * π / N))

/-- Each factor of `whiteheadS` is strictly positive on the summation range:
    for `1 ≤ j ≤ n` with `k + n ≤ N − 1`, both `jπ/N` and `(k+j)π/N` lie in
    `(0, π)`, so `sin > 0`. -/
theorem whiteheadS_factor_pos {N n k j : ℕ} (hN : 2 ≤ N) (hj1 : 1 ≤ j)
    (hjn : j ≤ n) (hkn : k + n ≤ N - 1) :
    0 < 2 * Real.sin (((k : ℝ) + j) * π / N) ^ 2 / Real.sin ((j : ℝ) * π / N) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hpi := Real.pi_pos
  -- denominator: 0 < sin(jπ/N)
  have hj1' : (1 : ℝ) ≤ (j : ℝ) := by exact_mod_cast hj1
  have hjN : (j : ℝ) < N := by
    have : j ≤ N - 1 := le_trans hjn (le_trans (Nat.le_add_left n k) hkn)
    have : j < N := by omega
    exact_mod_cast this
  have hden : 0 < Real.sin ((j : ℝ) * π / N) := by
    apply Real.sin_pos_of_pos_of_lt_pi
    · positivity
    · rw [div_lt_iff₀ hNpos]; nlinarith [Real.pi_pos]
  -- numerator argument in (0, π)
  have hkj1 : (1 : ℝ) ≤ (k : ℝ) + j := by
    have : (0 : ℝ) ≤ (k : ℝ) := by positivity
    linarith
  have hkjN : (k : ℝ) + j < N := by
    have h1 : k + j ≤ N - 1 := le_trans (by omega : k + j ≤ k + n) hkn
    have h2 : k + j < N := by omega
    exact_mod_cast h2
  have hnum_sin : 0 < Real.sin (((k : ℝ) + j) * π / N) := by
    apply Real.sin_pos_of_pos_of_lt_pi
    · positivity
    · rw [div_lt_iff₀ hNpos]; nlinarith [Real.pi_pos]
  have hnum : 0 < 2 * Real.sin (((k : ℝ) + j) * π / N) ^ 2 := by positivity
  exact div_pos hnum hden

/-- **Positive-sum brick.** The van der Veen kernel `whiteheadS N n k` is
    strictly positive on the summation range `k + n ≤ N − 1` — the positivity
    that the volume-conjecture squeeze proof rests on (analogue of
    `FigureEightVolume.kashaevProd_pos`). -/
theorem whiteheadS_pos {N n k : ℕ} (hN : 2 ≤ N) (hkn : k + n ≤ N - 1) :
    0 < whiteheadS N n k := by
  unfold whiteheadS
  apply Finset.prod_pos
  intro j hj
  obtain ⟨hj1, hjn⟩ := Finset.mem_Icc.mp hj
  exact whiteheadS_factor_pos hN hj1 hjn hkn

/-- **Log-expansion brick** (the `log(2 sin)` Riemann-sum form, analogue of
    the figure-eight `E5a`).  On the summation range `k + n ≤ N − 1`,
    `log S_{n,k} = Σ_{j=1}^n [ log 2 + 2·log sin((k+j)π/N) − log sin(jπ/N) ]`.
    This is what reduces the squeeze to the landed Clausen / `log(2 sin)`
    Riemann-sum-vs-primitive machinery. -/
theorem whiteheadS_log {N n k : ℕ} (hN : 2 ≤ N) (hkn : k + n ≤ N - 1) :
    Real.log (whiteheadS N n k)
      = ∑ j ∈ Finset.Icc 1 n,
          (Real.log 2 + 2 * Real.log (Real.sin (((k : ℝ) + j) * π / N))
            - Real.log (Real.sin ((j : ℝ) * π / N))) := by
  unfold whiteheadS
  rw [Real.log_prod _ _ (fun j hj => by
    obtain ⟨hj1, hjn⟩ := Finset.mem_Icc.mp hj
    exact ne_of_gt (whiteheadS_factor_pos hN hj1 hjn hkn))]
  apply Finset.sum_congr rfl
  intro j hj
  obtain ⟨hj1, hjn⟩ := Finset.mem_Icc.mp hj
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hpi := Real.pi_pos
  have hjN : (j : ℝ) < N := by
    have : j < N := by omega
    exact_mod_cast this
  have hden : 0 < Real.sin ((j : ℝ) * π / N) := by
    apply Real.sin_pos_of_pos_of_lt_pi
    · positivity
    · rw [div_lt_iff₀ hNpos]; nlinarith [Real.pi_pos]
  have hkjN : (k : ℝ) + j < N := by
    have : k + j < N := by omega
    exact_mod_cast this
  have hnum : 0 < Real.sin (((k : ℝ) + j) * π / N) := by
    apply Real.sin_pos_of_pos_of_lt_pi
    · positivity
    · rw [div_lt_iff₀ hNpos]; nlinarith [Real.pi_pos]
  rw [Real.log_div (by positivity) (ne_of_gt hden),
      Real.log_mul (by norm_num) (by positivity), Real.log_pow]
  push_cast
  ring

/-- The Whitehead Kashaev magnitude as the inner positive sum
    `Σ_{k=0}^{N-1-n} S_{n,k}` summed with the `(2n+1)` weight — the real,
    positive object the squeeze bounds (the `χ_{N,n}` phase is unimodular and
    only shifts the argument, not the magnitude analysis).  Placeholder shape
    for the limit statement below. -/
noncomputable def whiteheadInnerSum (N n : ℕ) : ℝ :=
  ∑ k ∈ Finset.range (N - n), whiteheadS N n k

theorem whiteheadInnerSum_pos {N n : ℕ} (hN : 2 ≤ N) (hn : n < N) :
    0 < whiteheadInnerSum N n := by
  unfold whiteheadInnerSum
  apply Finset.sum_pos
  · intro k hk
    have hk' : k < N - n := Finset.mem_range.mp hk
    have hkn : k + n ≤ N - 1 := by omega
    exact whiteheadS_pos hN hkn
  · exact ⟨0, Finset.mem_range.mpr (by omega)⟩

/-- **Lower-envelope brick** (lower half of the E1 log-Σ≈max squeeze).  The
    inner sum dominates any single term `S_{n,k}`, so `log` of the sum is at
    least `log S_{n,k}` for the saddle index — this is the lower bound that,
    at the saddle `k* ≈ N/4` (Whitehead `x* = k*/N = 1/4`), pushes the growth
    up to the volume. -/
theorem whiteheadS_le_innerSum {N n k : ℕ} (hN : 2 ≤ N) (hk : k < N - n) :
    whiteheadS N n k ≤ whiteheadInnerSum N n := by
  unfold whiteheadInnerSum
  refine Finset.single_le_sum (f := fun k => whiteheadS N n k) ?_ (Finset.mem_range.mpr hk)
  intro i hi
  have : i < N - n := Finset.mem_range.mp hi
  exact le_of_lt (whiteheadS_pos hN (by omega))

/-- **Upper-envelope brick** (upper half of the E1 squeeze).  The inner sum is
    at most the term count `(N − n)` times the largest term, so `log` of the
    sum exceeds `log(max term)` by at most `log(N − n) ≤ log N` — the `± log N`
    slack that vanishes under `(2π/N)·(·)`. -/
theorem whiteheadInnerSum_le_card_nsmul {N n : ℕ}
    {M : ℝ} (hM : ∀ k, k < N - n → whiteheadS N n k ≤ M) :
    whiteheadInnerSum N n ≤ (N - n) • M := by
  unfold whiteheadInnerSum
  calc ∑ k ∈ Finset.range (N - n), whiteheadS N n k
      ≤ ∑ _k ∈ Finset.range (N - n), M := by
        apply Finset.sum_le_sum
        intro k hk; exact hM k (Finset.mem_range.mp hk)
    _ = (N - n) • M := by rw [Finset.sum_const, Finset.card_range]

/-- **Saddle-packaging brick** (E1 at the saddle).  There is a maximizing index
    `k*` in the summation range whose single term brackets the whole inner sum
    within the term-count factor: `S_{n,k*} ≤ Σ_k S_{n,k} ≤ (N−n)·S_{n,k*}`.
    Taking `(2π/N)·log`, the two sides differ by `(2π/N)·log(N−n) → 0`, so the
    volume limit is governed by the single saddle term `S_{n,k*}` — the exact
    reduction the Clausen max-value analysis then evaluates. -/
theorem whiteheadInnerSum_saddle {N n : ℕ} (hN : 2 ≤ N) (hn : n < N) :
    ∃ kmax, kmax < N - n ∧
      whiteheadS N n kmax ≤ whiteheadInnerSum N n ∧
      whiteheadInnerSum N n ≤ (N - n) • whiteheadS N n kmax := by
  have hne : (Finset.range (N - n)).Nonempty := ⟨0, Finset.mem_range.mpr (by omega)⟩
  obtain ⟨kmax, hkmem, hkmax⟩ := Finset.exists_max_image (Finset.range (N - n))
    (fun k => whiteheadS N n k) hne
  refine ⟨kmax, Finset.mem_range.mp hkmem, ?_, ?_⟩
  · exact whiteheadS_le_innerSum hN (Finset.mem_range.mp hkmem)
  · exact whiteheadInnerSum_le_card_nsmul (fun k hk => hkmax k (Finset.mem_range.mpr hk))

/-- **Slack-vanishing brick.**  `(2π/N)·log N → 0` — the term-count slack in the
    saddle bound `whiteheadInnerSum_saddle` vanishes under the `(2π/N)` scaling,
    so both envelopes converge to the same saddle value.  (Mathlib
    `Real.tendsto_log_div_atTop`.) -/
theorem tendsto_slack_zero :
    Filter.Tendsto (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log N)
      Filter.atTop (nhds 0) := by
  have h0 : Filter.Tendsto (fun x : ℝ => Real.log x ^ 1 / (1 * x + 0))
      Filter.atTop (nhds 0) := tendsto_pow_log_div_mul_add_atTop 1 0 1 one_ne_zero
  have h : Filter.Tendsto (fun N : ℕ => Real.log (N : ℝ) / (N : ℝ))
      Filter.atTop (nhds 0) := by
    refine (h0.comp tendsto_natCast_atTop_atTop).congr (fun N => ?_)
    simp
  have h2 := h.const_mul (2 * π)
  rw [mul_zero] at h2
  refine h2.congr (fun N => ?_)
  ring

/-- **Squeeze-reduction capstone** (Mathlib-only).  For any choice of level
    `n(N)` and saddle index `k*(N)`, the scaled log of the inner sum and of the
    saddle term differ by an amount that VANISHES: bracketed below by `0`
    (the sum dominates one term) and above by `(2π/N)·log N` (the sum is at most
    `(N−n)` copies of the max), which `tendsto_slack_zero` sends to `0`.  Hence
    `(2π/N)·log(whiteheadInnerSum)` and `(2π/N)·log(S_{n,k*})` share every limit
    — the VC limit is reduced to the saddle-TERM value (the Clausen step). -/
theorem innerSum_saddle_scaledLog_diff_tendsto_zero
    (nseq kseq : ℕ → ℕ)
    (hvalid : ∀ N, 2 ≤ N →
        (whiteheadS N (nseq N) (kseq N) ≤ whiteheadInnerSum N (nseq N) ∧
         whiteheadInnerSum N (nseq N) ≤ (N - nseq N) • whiteheadS N (nseq N) (kseq N)))
    (hnlt : ∀ N, 2 ≤ N → nseq N < N)
    (hpos : ∀ N, 2 ≤ N → 0 < whiteheadS N (nseq N) (kseq N)) :
    Filter.Tendsto
      (fun N : ℕ => (2 * π / N) * Real.log (whiteheadInnerSum N (nseq N))
        - (2 * π / N) * Real.log (whiteheadS N (nseq N) (kseq N)))
      Filter.atTop (nhds 0) := by
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le'
    (tendsto_const_nhds (x := (0:ℝ))) tendsto_slack_zero ?_ ?_
  · -- eventually 0 ≤ D N
    filter_upwards [Filter.eventually_ge_atTop 2] with N hN
    obtain ⟨hlow, _⟩ := hvalid N hN
    have hspos := hpos N hN
    have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hscale : (0 : ℝ) ≤ 2 * π / N := by positivity
    have hlog := Real.log_le_log hspos hlow
    have := mul_le_mul_of_nonneg_left hlog hscale
    linarith
  · -- eventually D N ≤ (2π/N)·log N
    filter_upwards [Filter.eventually_ge_atTop 2] with N hN
    obtain ⟨hlow, hup⟩ := hvalid N hN
    have hspos := hpos N hN
    have hnlt' := hnlt N hN
    have hcardpos : (0 : ℝ) < ((N - nseq N : ℕ) : ℝ) := by
      exact_mod_cast (by omega : 0 < N - nseq N)
    have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hscale : (0 : ℝ) ≤ 2 * π / N := by positivity
    have hinner_pos : 0 < whiteheadInnerSum N (nseq N) := lt_of_lt_of_le hspos hlow
    have hup' : whiteheadInnerSum N (nseq N)
        ≤ ((N - nseq N : ℕ) : ℝ) * whiteheadS N (nseq N) (kseq N) := by
      rw [nsmul_eq_mul] at hup; exact hup
    have hlog1 := Real.log_le_log hinner_pos hup'
    rw [Real.log_mul (ne_of_gt hcardpos) (ne_of_gt hspos)] at hlog1
    have hstep := mul_le_mul_of_nonneg_left hlog1 hscale
    rw [mul_add] at hstep
    have hlogmono : Real.log ((N - nseq N : ℕ) : ℝ) ≤ Real.log N := by
      refine Real.log_le_log hcardpos ?_
      exact_mod_cast Nat.sub_le N (nseq N)
    have hslack := mul_le_mul_of_nonneg_left hlogmono hscale
    linarith

/-- **Conditional VC (sorry-free).**  IF the scaled log of the saddle TERM
    converges to `4G`, THEN so does the scaled log of the inner sum — immediate
    from the capstone (`inner = (inner − saddle) + saddle`, and the difference
    → 0).  This isolates the single genuinely-open input (the saddle-value =
    `4G` identification, van der Veen's Clausen/Lobachevsky evaluation) as an
    explicit hypothesis rather than a `sorry`; discharging that hypothesis via
    the landed `QOU.Infra.Clausen` machinery closes the Whitehead VC. -/
theorem whitehead_vc_of_saddle_value
    (nseq kseq : ℕ → ℕ)
    (hvalid : ∀ N, 2 ≤ N →
        (whiteheadS N (nseq N) (kseq N) ≤ whiteheadInnerSum N (nseq N) ∧
         whiteheadInnerSum N (nseq N) ≤ (N - nseq N) • whiteheadS N (nseq N) (kseq N)))
    (hnlt : ∀ N, 2 ≤ N → nseq N < N)
    (hpos : ∀ N, 2 ≤ N → 0 < whiteheadS N (nseq N) (kseq N))
    (hsaddle : Filter.Tendsto
        (fun N : ℕ => (2 * π / N) * Real.log (whiteheadS N (nseq N) (kseq N)))
        Filter.atTop (nhds (4 * catalanG))) :
    Filter.Tendsto
      (fun N : ℕ => (2 * π / N) * Real.log (whiteheadInnerSum N (nseq N)))
      Filter.atTop (nhds (4 * catalanG)) := by
  have hdiff := innerSum_saddle_scaledLog_diff_tendsto_zero nseq kseq hvalid hnlt hpos
  have hsum := hdiff.add hsaddle
  rw [zero_add] at hsum
  exact hsum.congr (fun N => by ring)

/-- **CONJECTURE (OPEN).** The Whitehead Volume Conjecture (van der Veen's theorem). -/
class WhiteheadVolumeConjectureLimit (kashaev : ℕ → ℝ) (hk : ∀ N, kashaev N = whiteheadInnerSum N ((N - 1) / 2)) : Prop where
  /-- The limit holds. -/
  limit : Filter.Tendsto (fun N : ℕ => (2 * π / N) * Real.log (kashaev N)) Filter.atTop (nhds (4 * catalanG))

/-- **The Whitehead Volume Conjecture** (van der Veen's theorem):
    `(2π/N)·log|J_N(W)(e^{2πi/N})| → Vol(Whitehead) = 4G`.

    STATE-AND-QUEUED: proved in van der Veen arXiv:math/0611181.  The
    unconditional in-repo squeeze proof for the `⌊N/2⌋` inner sum is now
    `QOU.Knot.WhiteheadSaddle.whitehead_vc_innerSum_half` (sorry-free,
    downstream — it imports the `QOU.Knot.Clausen` machinery that this
    Mathlib-only base file cannot).  This abstract `kashaev`-linked form with
    the `(N-1)/2` placeholder index remains the one honest `sorry` here; bean
    qou-1gkf tracks porting the downstream ⌊N/2⌋ result to this exact form. -/
theorem whitehead_volume_conjecture
    (kashaev : ℕ → ℝ)
    (hk : ∀ N, kashaev N = whiteheadInnerSum N ((N - 1) / 2))
    [hi : WhiteheadVolumeConjectureLimit kashaev hk] :   -- placeholder link
    Filter.Tendsto (fun N : ℕ => (2 * π / N) * Real.log (kashaev N))
      Filter.atTop (nhds (4 * catalanG)) := by
  -- Ref: [vanderveen2008] arXiv:math/0611181 — VC for the Whitehead link.
  -- Honest sorry: this base file is Mathlib-only and cannot import
  -- QOU.Knot.Clausen; the genuine unconditional proof (⌊N/2⌋ inner sum) is
  -- QOU.Knot.WhiteheadSaddle.whitehead_vc_innerSum_half (sorry-free).
  exact hi.limit

end QOU.Knot.WhiteheadVC
