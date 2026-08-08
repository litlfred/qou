/-
Copyright (c) 2026 litlfred. All rights reserved.

# μ–p residual on the muon carrier: order window + the `MmuR9V9Closure` exclusions

Bean `qou-6gf9`. Companion audit:
`docs/audits/2026-08-08-mu-p-residual-carrier-order-and-bar-parity-prune.md`.
Probe: `docs/audits/scripts/mu_p_carrier_order_window_probe.py`.

This is the **archimedean** half of the μ–p carrier prune; the generic
bar-parity algebra lives in `QOU/BraidKnot/MuPCarrierBarParity.lean`. The split
follows AGENTS.md §7c: the results below are statements about *magnitudes at
the substrate pin* and about `ℝ`-valued production definitions, so `ℝ` is the
correct base ring here, while the parity bookkeeping needs no ordering at all.

## The datum (probe, proton pin, 60 dps)

`ℏ_q = 0.09908171604425850783917712`; predicted `m_μ/m_e = 206.76832637067386`
vs CODATA `206.7682830`, i.e. `+209.755 ppb = 9.534 σ`. The multiplicative
correction the carrier would need is `t = 2.09754920524e-7`, known to
`σ_exp/t = 10.49 %`.

## What this file proves

1. `order_window` — if the correction is a monomial `t = |c|·ℏ_q^k` with a
   *small-height* coefficient `|c| ∈ [1/5, 5]`, then `k ∈ {6, 7}`. Orders
   `k ≤ 5` overshoot by ≥ 7.5×; orders `k ≥ 8` undershoot by ≥ 3.6×.

   Corollary drawn in the audit: this prunes the Ohtsuki / volume-conjecture
   reading of "`Vol(4₁)` is the leading term", whose 1-loop term sits at `k = 1`
   and overshoots by `4.7e5×`.

2. `delta_R9_not_bar_even`, `delta_V9_not_bar_even` — the two rungs of the
   NEAR-MATCH m_μ closure in `MmuR9V9Closure.lean` are **bar-mixed**, hence fail
   the bar-even precondition that disqualified the projector-weight shift. These
   are proved against the *production definitions themselves* (imported), not a
   re-transcription.

## What this file does NOT claim

No correction is derived; nothing is wired. In particular the tighter class
`|c| ∈ [1/2, 2]` ("`±ℏ_q^k` up to a factor of two") is **not** claimed empty:
it is empty at the central value (`c₆ = 0.22169`, `c₇ = 2.23747`) but `c₇` falls
to `2.003` at the −1σ edge, so the exclusion is knife-edge and is deliberately
left unformalized.

The bar-mixedness in (2) is unconditional; the *exclusion* it licenses is
conditional on the bar-even precondition, which is argued in the corpus, not
proved (AGENTS.md §"Conditional-proved ≠ premise-established").

Scope of both negatives: **(b)** relative to a stated class — the magnitude
bound for (1), bar-parity under `q ↦ q⁻¹` for (2). Neither excludes any
ingredient outside its class.
-/
import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import QOU.BraidKnot.MmuR9V9Closure
import QOU.BraidKnot.MuPCarrierBarParity

namespace QOU.BraidKnot.MuPCarrierOrderWindow

open QOU.BraidKnot.MuPCarrier

/-! ## 1. The generic substrate agrees with the production one on `ℝ` -/

/-- The generic `ℏ` of `MuPCarrierBarParity` agrees with the production `hbarQ`
on `ℝ`, so the parity results there apply verbatim to the definitions below. -/
theorem hbarGen_eq_hbarQ (q : ℝ) (hq : q ≠ 0) : hbarGen q = hbarQ q := by
  unfold hbarGen hbarQ hbarQ'
  field_simp

/-! ## 2. The corpus's own m_μ rungs are bar-mixed

`delta_R9 = ℏ_q⁶·q/5` has exponent pattern `(k, m) = (6, 1)`; bar-evenness
needs `m = k/2 = 3`. `delta_V9 = ℏ_q⁸·[3]_q/25` has a bar-even `[3]_q` factor,
so its `ℏ_q⁸` prefactor is left undressed by the required `q⁴`. Both therefore
fail the selection rule of `MuPCarrierBarParity`, and the witnesses below make
that concrete. -/

/-- **`delta_R9` is not bar-even.** Witness `q = 2`:
`δ_R9(1/2) = 1/10` but `δ_R9(2) = 1/160`.

At the substrate pin the violation is not marginal — the probe measures
`δ_R9(1/q₀)/δ_R9(q₀) = 1.5180`. -/
theorem delta_R9_not_bar_even : delta_R9 ((2 : ℝ)⁻¹) ≠ delta_R9 (2 : ℝ) := by
  unfold delta_R9 hbarQ hbarQ'
  norm_num

/-- **`delta_V9` is not bar-even.** Witness `q = 2`:
`δ_V9(1/2) = 21/100` but `δ_V9(2) = 21/25600`.

Probe measures `δ_V9(1/q₀)/δ_V9(q₀) = 2.3042`. -/
theorem delta_V9_not_bar_even : delta_V9 ((2 : ℝ)⁻¹) ≠ delta_V9 (2 : ℝ) := by
  unfold delta_V9 quantumInt hbarQ hbarQ'
  norm_num

/-! ## 3. Order window -/

/-- **Order window.** Suppose the μ–p correction has the monomial form
`t = |c| · h^k`, where

* `h = ℏ_q ∈ [0.098, 0.100]` (the substrate at any pin in the legitimate μ–p
  window; the probe measures `ℏ_{q₀} = 0.09908171604`),
* `|c| ∈ [1/5, 5]` is a *small-height* coefficient, and
* `t ∈ [1.8e-7, 2.4e-7]` is the measured residual `209.755 ppb`, a window that
  comfortably contains `±1σ_exp = ±22 ppb`.

Then `k ∈ {6, 7}`.

Orders `k ≤ 5` give at least `0.098⁵/5 ≈ 1.81e-6`, over 7.5× the top of the
window; orders `k ≥ 8` give at most `5·0.1⁸ = 5e-8`, under 0.28× the bottom.
Both are contradictions. -/
theorem order_window (h c t : ℝ) (k : ℕ)
    (hh0 : (98 : ℝ) / 1000 ≤ h) (hh1 : h ≤ (1 : ℝ) / 10)
    (hc0 : (1 : ℝ) / 5 ≤ |c|) (hc1 : |c| ≤ 5)
    (ht : |c| * h ^ k = t)
    (htlo : (18 : ℝ) / 10 ^ 8 ≤ t) (hthi : t ≤ (24 : ℝ) / 10 ^ 8) :
    k = 6 ∨ k = 7 := by
  have hhpos : (0 : ℝ) < h := by linarith
  have hh1' : h ≤ 1 := by linarith
  have hpk : (0 : ℝ) ≤ h ^ k := by positivity
  by_contra hk
  push_neg at hk
  obtain ⟨hk6, hk7⟩ := hk
  rcases (show k ≤ 5 ∨ 8 ≤ k by omega) with hle | hge
  · -- `k ≤ 5`: the monomial is too large.
    have hmono : h ^ 5 ≤ h ^ k := pow_le_pow_of_le_one hhpos.le hh1' hle
    have hlow : ((98 : ℝ) / 1000) ^ 5 ≤ h ^ 5 := by gcongr
    have hcm : (1 : ℝ) / 5 * h ^ k ≤ |c| * h ^ k :=
      mul_le_mul_of_nonneg_right hc0 hpk
    have hbig : (1 : ℝ) / 5 * ((98 : ℝ) / 1000) ^ 5 ≤ t := by rw [← ht]; linarith
    have hnum : (24 : ℝ) / 10 ^ 8 < (1 : ℝ) / 5 * ((98 : ℝ) / 1000) ^ 5 := by norm_num
    linarith
  · -- `k ≥ 8`: the monomial is too small.
    have hmono : h ^ k ≤ h ^ 8 := pow_le_pow_of_le_one hhpos.le hh1' hge
    have hhigh : h ^ 8 ≤ ((1 : ℝ) / 10) ^ 8 := by gcongr
    have hcm : |c| * h ^ k ≤ 5 * h ^ k := mul_le_mul_of_nonneg_right hc1 hpk
    have hsmall : t ≤ 5 * ((1 : ℝ) / 10) ^ 8 := by rw [← ht]; linarith
    have hnum : (5 : ℝ) * ((1 : ℝ) / 10) ^ 8 < (18 : ℝ) / 10 ^ 8 := by norm_num
    linarith

-- Verification (2026-08-08, `scripts/lean-verify.sh`, exit 0, 0 sorries):
-- `#print axioms` on `hbarGen_eq_hbarQ`, `delta_R9_not_bar_even`,
-- `delta_V9_not_bar_even`, `order_window` each returns exactly
-- `[propext, Classical.choice, Quot.sound]` — no `sorryAx`.

end QOU.BraidKnot.MuPCarrierOrderWindow
