/-
# The Whitehead-link VC needs only a ONE-SIDED rate (bean qou-u1b5)

`WhiteheadLinkScaffold` states the remaining gap as the conditional class
`VdVWhiteheadLemma4`:

    ∃ p, ∀ᶠ N, whiteheadLinkMajorant N ≤ N^p · ‖whiteheadLinkKashaev N‖

a two-sided polynomial comparison between the majorant and the modulus.  That
is van der Veen's Lemma 4 as stated, and it is more than the volume conjecture
needs.

**The upper half is already closed, sorry-free**, by two results on `main`:

* `norm_whiteheadLinkKashaev_le`      — `‖J_N‖ ≤ majorant N`  (triangle ineq.)
* `tendsto_log_whiteheadLinkMajorant_vol` — `(2π/N)·log(majorant N) → 4G`

so `limsup (2π/N)·log‖J_N‖ ≤ 4G` is a fact, not a hypothesis.  Everything still
open lives on the **other** side.  This file makes that precise: it introduces

    WhiteheadLinkLowerRate :   ∀ ε > 0, ∀ᶠ N,  4G − ε ≤ (2π/N)·log‖J_N‖

— a one-sided asymptotic lower bound, no majorant, no exponent `p` — proves the
volume conjecture from it (`whiteheadLink_volume_of_lowerRate`, sorry-free), and
proves `VdVWhiteheadLemma4 → WhiteheadLinkLowerRate` so that nothing is lost:
anyone who discharges Lemma 4 still gets the conclusion, and anyone attacking
the problem now has a strictly weaker target.

Why the narrowing is worth having: Lemma 4 asks for a comparison uniform in the
exponent `p` against the *whole* majorant, which is a statement about the phased
sum's cancellation structure at every scale.  The lower rate asks only that the
sum not lose exponential order — the single quantitative fact the squeeze
consumes.  It is also the half that the sibling programme
(`QOU/Knot/WhiteheadSaddleClausen.lean`, `qou-t2sc`, sorry-free) is closest to,
having already proved the *inner sum at the saddle slice* attains `4G`; what
remains there is non-cancellation of the outer phased `n`-sum.  See
`docs/coordination/whitehead-link-volume-conjecture-join.md`.

**No claim is made here that either class is proved.**  `VdVWhiteheadLemma4`
has no instance in the corpus, and neither does `WhiteheadLinkLowerRate`; this
file only relocates the open problem to the weakest form that suffices.

Archimedean (ℝ).
-- Ref: [vanderveen2008] arXiv:math/0611181, Lemma 4
-/

import QOU.Knot.WhiteheadMajorantRate
import QOU.Knot.CatalanValueBounds

namespace QOU.Knot.FigureEightVolume

open Real

/-- The volume target is positive — needed to turn the lower rate into
    positivity of `‖J_N‖`, since `Real.log` is junk-valued at `0`. -/
theorem vol_borromean_half_pos : 0 < QOU.Archimedean.Vol_Borromean / 2 := by
  have hV : QOU.Archimedean.Vol_Borromean
      = 8 * QOU.Archimedean.Cl_2 (π / 2) := rfl
  have hG : 0 < QOU.Archimedean.Cl_2 (π / 2) := Cl_2_pi_div_two_pos
  rw [hV]; linarith

/-- **The one-sided rate the volume conjecture actually needs.**

    Strictly weaker than `VdVWhiteheadLemma4` (see `lowerRate_of_lemma4`): it
    mentions neither the majorant nor a polynomial exponent, only that the
    scaled log-modulus is not asymptotically below the volume.

    OPEN: no instance exists in this corpus. -/
class WhiteheadLinkLowerRate : Prop where
  /-- For every `ε > 0`, eventually `4G − ε ≤ (2π/N)·log‖J_N‖`. -/
  lower : ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in Filter.atTop,
    QOU.Archimedean.Vol_Borromean / 2 - ε
      ≤ (2 * π / (N : ℝ)) * Real.log ‖whiteheadLinkKashaev N‖

/-- Under the lower rate, `‖J_N‖ > 1` eventually — so `Real.log`'s junk value
    at `0` never bites in the upper comparison below. -/
theorem eventually_one_lt_norm [WhiteheadLinkLowerRate] :
    ∀ᶠ N : ℕ in Filter.atTop, 1 < ‖whiteheadLinkKashaev N‖ := by
  have hpos := vol_borromean_half_pos
  have hlow := WhiteheadLinkLowerRate.lower
    (QOU.Archimedean.Vol_Borromean / 4) (by linarith)
  have hN : ∀ᶠ N : ℕ in Filter.atTop, 1 ≤ N := Filter.eventually_atTop.2 ⟨1, fun _ h => h⟩
  filter_upwards [hlow, hN] with N hN1 hNpos
  by_contra hcon
  push_neg at hcon
  -- `‖J‖ ≤ 1` forces `log ‖J‖ ≤ 0`, hence the scaled log is `≤ 0`
  have hlog : Real.log ‖whiteheadLinkKashaev N‖ ≤ 0 :=
    Real.log_nonpos (norm_nonneg _) hcon
  have hNR : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hNpos
  have hcoef : 0 < 2 * π / (N : ℝ) := by positivity
  have : (2 * π / (N : ℝ)) * Real.log ‖whiteheadLinkKashaev N‖ ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hcoef.le hlog
  -- but the rate says it is at least `Vol/2 − Vol/4 = Vol/4 > 0`
  have hquarter : QOU.Archimedean.Vol_Borromean / 2
      - QOU.Archimedean.Vol_Borromean / 4 = QOU.Archimedean.Vol_Borromean / 4 := by
    ring
  rw [hquarter] at hN1
  have : (0 : ℝ) < QOU.Archimedean.Vol_Borromean / 4 := by linarith
  linarith

/-- **The Whitehead-link volume conjecture from the one-sided rate**
    (sorry-free given the class).

    `(2π/N)·log‖J_N(W)‖ → Vol(𝓑₃)/2 = 4G = Vol(L5a1)`.

    The upper half is unconditional — the triangle bound
    `norm_whiteheadLinkKashaev_le` against the sorry-free majorant rate
    `tendsto_log_whiteheadLinkMajorant_vol`.  Only the lower half uses the
    class. -/
theorem whiteheadLink_volume_of_lowerRate [WhiteheadLinkLowerRate] :
    Filter.Tendsto
      (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log ‖whiteheadLinkKashaev N‖)
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) := by
  have hmaj := tendsto_log_whiteheadLinkMajorant_vol
  refine tendsto_order.2 ⟨?_, ?_⟩
  · -- below: from the class with `ε = (a − b)/2`
    intro b hb
    have hε : 0 < (QOU.Archimedean.Vol_Borromean / 2 - b) / 2 := by linarith
    filter_upwards [WhiteheadLinkLowerRate.lower _ hε] with N hN
    linarith
  · -- above: the triangle bound against the majorant, which converges to `a`
    intro b hb
    have hmajb : ∀ᶠ N : ℕ in Filter.atTop,
        (2 * π / (N : ℝ)) * Real.log (whiteheadLinkMajorant N) < b :=
      hmaj.eventually (eventually_lt_nhds hb)
    have hNpos : ∀ᶠ N : ℕ in Filter.atTop, 1 ≤ N :=
      Filter.eventually_atTop.2 ⟨1, fun _ h => h⟩
    filter_upwards [hmajb, eventually_one_lt_norm, hNpos] with N hNb hNnorm hNpos
    have hJpos : 0 < ‖whiteheadLinkKashaev N‖ := by linarith
    have hle : ‖whiteheadLinkKashaev N‖ ≤ whiteheadLinkMajorant N :=
      norm_whiteheadLinkKashaev_le N
    have hNR : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hNpos
    have hcoef : 0 < 2 * π / (N : ℝ) := by positivity
    have hlog : Real.log ‖whiteheadLinkKashaev N‖
        ≤ Real.log (whiteheadLinkMajorant N) := Real.log_le_log hJpos hle
    have : (2 * π / (N : ℝ)) * Real.log ‖whiteheadLinkKashaev N‖
        ≤ (2 * π / (N : ℝ)) * Real.log (whiteheadLinkMajorant N) :=
      mul_le_mul_of_nonneg_left hlog hcoef.le
    linarith

/-- **Nothing is lost by the narrowing**: van der Veen's Lemma 4 implies the
    one-sided rate.  So any discharge of `VdVWhiteheadLemma4` still yields the
    volume conjecture through `whiteheadLink_volume_of_lowerRate`, while an
    attack may now target the weaker `WhiteheadLinkLowerRate` instead.

    The `N^p` factor costs `p·(2π/N)·log N → 0`, which is why a *polynomial*
    phase cost is invisible at this scale — the content of Lemma 4 is that the
    cost is not exponential. -/
theorem lowerRate_of_lemma4 [VdVWhiteheadLemma4] : WhiteheadLinkLowerRate where
  lower := by
    intro ε hε
    obtain ⟨p, hp⟩ := VdVWhiteheadLemma4.phase_cost
    have hmaj := tendsto_log_whiteheadLinkMajorant_vol
    -- `(2π/N)·log(majorant) → a`, so eventually it exceeds `a − ε/2`
    have hmajlow : ∀ᶠ N : ℕ in Filter.atTop,
        QOU.Archimedean.Vol_Borromean / 2 - ε / 2
          < (2 * π / (N : ℝ)) * Real.log (whiteheadLinkMajorant N) :=
      hmaj.eventually (eventually_gt_nhds (by linarith))
    -- the `N^p` correction is `o(1)`
    have hcorr : Filter.Tendsto
        (fun N : ℕ => (2 * π / (N : ℝ)) * ((p : ℝ) * Real.log (N : ℝ)))
        Filter.atTop (nhds 0) := by
      have h := Real.tendsto_pow_log_div_mul_add_atTop 1 0 1 (by norm_num)
      have h' : Filter.Tendsto (fun x : ℝ => Real.log x / x) Filter.atTop (nhds 0) := by
        simpa using h
      have hnat : Filter.Tendsto (fun N : ℕ => Real.log (N : ℝ) / (N : ℝ))
          Filter.atTop (nhds 0) := h'.comp tendsto_natCast_atTop_atTop
      have hmul := hnat.const_mul (2 * π * (p : ℝ))
      rw [mul_zero] at hmul
      refine hmul.congr fun N => ?_
      ring
    have hsmall : ∀ᶠ N : ℕ in Filter.atTop,
        (2 * π / (N : ℝ)) * ((p : ℝ) * Real.log (N : ℝ)) < ε / 2 := by
      have := hcorr.eventually (eventually_lt_nhds (show (0:ℝ) < ε / 2 by linarith))
      simpa using this
    have hNpos : ∀ᶠ N : ℕ in Filter.atTop, 1 ≤ N :=
      Filter.eventually_atTop.2 ⟨1, fun _ h => h⟩
    filter_upwards [hp, hmajlow, hsmall, hNpos] with N hpN hmajN hsmallN hNpos
    have hNR : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hNpos
    have hcoef : 0 < 2 * π / (N : ℝ) := by positivity
    have hMpos : 0 < whiteheadLinkMajorant N := by
      have := whiteheadLink_inner_pos (N := N) (n := 0) (by omega)
      have hsum : 0 < ∑ n ∈ Finset.range N,
          ((2 * n + 1 : ℕ) : ℝ) * (∑ k ∈ Finset.range (N - n), whiteheadTerm N n k) := by
        apply Finset.sum_pos
        · intro n hn
          have hnN : n < N := Finset.mem_range.mp hn
          have := whiteheadLink_inner_pos (N := N) (n := n) hnN
          positivity
        · exact ⟨0, Finset.mem_range.mpr (by omega)⟩
      exact hsum
    have hJpos : 0 < ‖whiteheadLinkKashaev N‖ := by
      rcases (norm_nonneg (whiteheadLinkKashaev N)).lt_or_eq with h | h
      · exact h
      · exfalso
        rw [← h] at hpN
        simp only [mul_zero] at hpN
        linarith
    -- `log majorant ≤ p·log N + log ‖J‖`
    have hNpow : (0 : ℝ) < (N : ℝ) ^ p := by positivity
    have hlog : Real.log (whiteheadLinkMajorant N)
        ≤ (p : ℝ) * Real.log (N : ℝ) + Real.log ‖whiteheadLinkKashaev N‖ := by
      have := Real.log_le_log hMpos hpN
      rwa [Real.log_mul (ne_of_gt hNpow) (ne_of_gt hJpos), Real.log_pow] at this
    have hscaled : (2 * π / (N : ℝ)) * Real.log (whiteheadLinkMajorant N)
        ≤ (2 * π / (N : ℝ)) * ((p : ℝ) * Real.log (N : ℝ))
          + (2 * π / (N : ℝ)) * Real.log ‖whiteheadLinkKashaev N‖ := by
      have := mul_le_mul_of_nonneg_left hlog hcoef.le
      linarith [this]
    linarith

end QOU.Knot.FigureEightVolume
