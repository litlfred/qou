/-
  Robbins' `1/(12n)` refinement of Stirling — bean `qou-mlgp` (A), gap 2.

  THE GAP, IN MATHLIB'S OWN WORDS.  `Mathlib/Analysis/SpecialFunctions/Stirling.lean`
  proves `Stirling.le_log_factorial_stirling`,

      n·log n − n + ½log n + ½log(2π)  ≤  log n!

  and its docstring says: *"Sharper bounds due to Robbins are available, but are
  not yet formalised. These would add lower order terms (beginning with
  `(12 * n)⁻¹`) to the left hand side."*  This file supplies the matching UPPER
  bound with exactly that term:

      log n!  ≤  n·log n − n + ½log n + ½log(2π) + 1/(12n).

  WHY THIS CORPUS WANTS IT.  `QOU/Knot/KashaevEndpointSplit.lean` reduces the
  `j = 0` endpoint of `qou-mlgp` (A) to Stirling by the exact split
  `∑_{j≤k} log(2 sin(jπ/N)) = k·log(2π/N) + log(k!) + ∑_{j≤k} logSinc(jπ/N)`.
  Reassembling, the `+1/(12k)` of Stirling cancels identically against the
  `−(h/12)·(1/θ)` coming from `logSinc′ = cot x − 1/x`, and what survives is
  exactly the measured `−(π/12N)·cot θ`.  The two halves are individually
  `O(1/N)` and only cancel together, so the refinement genuinely needs this
  term — Mathlib's `√π ≤ stirlingSeq n` bounds the same quantity only by `0`,
  which leaves an `O(1/N)` hole precisely where the answer lives.

  WHY IT COMES OUT EXACTLY.  Mathlib already proves the series
  (`log_stirlingSeq_diff_hasSum`)

      log σ(n) − log σ(n+1) = ∑_{k≥0} (1/(2k+3))·x^{k+1},   x = 1/(2n+1)²

  where `σ = stirlingSeq`.  Its existing consequence
  `log_stirlingSeq_diff_le_geo_sum` bounds every coefficient by `1`.  But the
  series starts at `k = 0` with coefficient `1/3`, so every coefficient is `≤ 1/3`,
  and

      ⅓·x/(1−x) = ⅓·1/((2n+1)²−1) = 1/(12n(n+1)) = 1/(12n) − 1/(12(n+1))

  with NO slack whatsoever — the telescoping bound Robbins needs is an equality,
  not an estimate.  Summing from `n` to `∞` against
  `tendsto_stirlingSeq_sqrt_pi` gives `log σ(n) − log √π ≤ 1/(12n)`.

  NOT A DUPLICATE of `QOU/Mathlib/StirlingUpperBound.lean` (bean `el8w`), which
  proves the CRUDE `n! ≤ e·√n·(n/e)ⁿ` by monotonicity from `stirlingSeq 1`.
  That is enough for the Watson-uniqueness optimisation it was built for and is
  left in place; this file is the sharp version, with the right constant
  `√(2π)` and the `e^{1/(12n)}` factor.

  BOTH SIDES ARE HERE.  The matching lower refinement
  `1/(12n+1) ≤ log σ(n) − log √π` is proved below too, and needs no series
  estimate at all: the terms are nonnegative, so the sum dominates its FIRST
  term `⅓·x`, and that alone already beats the telescoping gap — the margin is
  exactly `24m+1`, tight at `m = 0` where the two sides differ by `1`.
  Mathlib's `sqrt_pi_le_stirlingSeq` gives only the weaker `0 ≤ ·`.

  Together the two bounds pin `log n!` to within
  `1/(12n) − 1/(12n+1) = 1/(12n(12n+1)) = O(1/n²)`, which is what `qou-mlgp` (A)
  needs: the `−(π/12N)cot θ` refinement requires the `1/(12k)` term to `o(1/N)`
  accuracy, and either bound alone would leave an `O(1/N)` hole.

  -- Ref: [leitner2026] QOU/Knot/KashaevEndpointSplit.lean   (what consumes this)
  -- Ref: [leitner2026] QOU/Mathlib/StirlingUpperBound.lean  (the crude cousin)
  -- Ref: [leitner2026] computations/probes/kashaev_endpoint_split_probe.py
-/
import Mathlib.Analysis.SpecialFunctions.Stirling

namespace QOU.MathlibExt

open Real Filter Stirling
open scoped Topology Nat

/-- **The telescoping bound.**  `log σ(n+1) − log σ(n+2) ≤ 1/(12(n+1)) − 1/(12(n+2))`.

Sharpening `Stirling.log_stirlingSeq_diff_le_geo_sum`, which bounds the series
coefficients `1/(2k+3)` by `1`.  Bounding them by `1/3` — their actual first
value — turns the geometric sum into the telescoping difference exactly. -/
theorem log_stirlingSeq_diff_le_robbins (n : ℕ) :
    Real.log (stirlingSeq (n + 1)) - Real.log (stirlingSeq (n + 2))
      ≤ 1 / (12 * ((n : ℝ) + 1)) - 1 / (12 * ((n : ℝ) + 2)) := by
  have h_nonneg : (0 : ℝ) ≤ ((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2 := sq_nonneg _
  have hlt : ((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2 < 1 := by
    rw [one_div, inv_pow]
    exact inv_lt_one_of_one_lt₀
      (one_lt_pow₀ (lt_add_of_pos_left _ <| by positivity) two_ne_zero)
  -- the geometric series, scaled by the true leading coefficient `1/3`
  have g : HasSum
      (fun k : ℕ => (1 / 3 : ℝ) * (((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2) ^ ↑(k + 1))
      ((1 / 3 : ℝ) * (((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2
        / (1 - ((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2))) := by
    have h0 : HasSum (fun k : ℕ => (((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2) ^ ↑(k + 1))
        (((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2
          / (1 - ((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2)) := by
      have := (hasSum_geometric_of_lt_one h_nonneg hlt).mul_left
        (((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2)
      simp_rw [← _root_.pow_succ'] at this
      exact this
    exact h0.mul_left (1 / 3)
  -- every coefficient `1/(2k+3)` is at most `1/3`
  have hab (k : ℕ) :
      (1 : ℝ) / (2 * ↑(k + 1) + 1) * ((1 / (2 * ↑(n + 1) + 1)) ^ 2) ^ ↑(k + 1)
        ≤ (1 / 3 : ℝ) * ((((1 : ℝ) / (2 * ↑(n + 1) + 1)) ^ 2) ^ ↑(k + 1)) := by
    refine mul_le_mul_of_nonneg_right ?_ (pow_nonneg h_nonneg _)
    have hden : (0 : ℝ) < 2 * (↑(k + 1) : ℝ) + 1 := by positivity
    rw [div_le_iff₀ hden]
    push_cast
    linarith [Nat.cast_nonneg (α := ℝ) k]
  refine (hasSum_le hab (log_stirlingSeq_diff_hasSum n) g).trans (le_of_eq ?_)
  have hs : (2 : ℝ) * ↑(n + 1) + 1 = 2 * (n : ℝ) + 3 := by push_cast; ring
  rw [hs]
  have h23 : (0 : ℝ) < 2 * (n : ℝ) + 3 := by positivity
  have hd : (1 : ℝ) - (1 / (2 * (n : ℝ) + 3)) ^ 2
      = (4 * ((n : ℝ) + 1) * ((n : ℝ) + 2)) / (2 * (n : ℝ) + 3) ^ 2 := by
    field_simp
    ring
  rw [hd]
  have ha1 : (0 : ℝ) < (n : ℝ) + 1 := by positivity
  have ha2 : (0 : ℝ) < (n : ℝ) + 2 := by positivity
  field_simp
  ring

/-- The telescoped bound over any range: `log σ(n+1) − log σ(m+1) ≤
1/(12(n+1)) − 1/(12(m+1))` for `n ≤ m`. -/
theorem log_stirlingSeq_sub_le_robbins {n m : ℕ} (hnm : n ≤ m) :
    Real.log (stirlingSeq (n + 1)) - Real.log (stirlingSeq (m + 1))
      ≤ 1 / (12 * ((n : ℝ) + 1)) - 1 / (12 * ((m : ℝ) + 1)) := by
  induction m, hnm using Nat.le_induction with
  | base => simp
  | succ p hp ih =>
      have hstep := log_stirlingSeq_diff_le_robbins p
      push_cast at ih hstep ⊢
      ring_nf at ih hstep ⊢
      linarith

/-- **`log σ(n) − log √π ≤ 1/(12n)`** for `n ≠ 0`, where `σ = stirlingSeq`.

The telescoping bound summed to infinity against `tendsto_stirlingSeq_sqrt_pi`. -/
theorem log_stirlingSeq_sub_log_sqrt_pi_le {n : ℕ} (hn : n ≠ 0) :
    Real.log (stirlingSeq n) - Real.log (Real.sqrt π) ≤ 1 / (12 * (n : ℝ)) := by
  obtain ⟨p, rfl⟩ : ∃ p, n = p + 1 := ⟨n - 1, by omega⟩
  have hsqrt : (0 : ℝ) < Real.sqrt π := Real.sqrt_pos.mpr Real.pi_pos
  have hlim : Tendsto (fun m : ℕ => Real.log (stirlingSeq (m + 1))) atTop
      (𝓝 (Real.log (Real.sqrt π))) :=
    (Real.continuousAt_log (ne_of_gt hsqrt)).tendsto.comp
      (tendsto_stirlingSeq_sqrt_pi.comp (tendsto_add_atTop_nat 1))
  have hbd : ∀ᶠ m : ℕ in atTop,
      Real.log (stirlingSeq (p + 1)) - 1 / (12 * ((p : ℝ) + 1))
        ≤ Real.log (stirlingSeq (m + 1)) := by
    filter_upwards [eventually_ge_atTop p] with m hm
    have hpos : (0 : ℝ) < 1 / (12 * ((m : ℝ) + 1)) := by positivity
    linarith [log_stirlingSeq_sub_le_robbins hm]
  have := ge_of_tendsto hlim hbd
  push_cast
  linarith

/-- **Robbins' upper bound.**  For `n ≠ 0`,

    log n!  ≤  n·log n − n + ½·log n + ½·log(2π) + 1/(12n).

The exact counterpart of Mathlib's `Stirling.le_log_factorial_stirling`, with
the `1/(12n)` term its docstring records as missing.  Together the two pin
`log n!` to within `1/(12n)`. -/
theorem log_factorial_le_stirling_robbins {n : ℕ} (hn : n ≠ 0) :
    Real.log n ! ≤ (n : ℝ) * Real.log n - n + Real.log n / 2
      + Real.log (2 * π) / 2 + 1 / (12 * (n : ℝ)) := by
  have hnR : (0 : ℝ) < n := by exact_mod_cast Nat.pos_of_ne_zero hn
  have hkey := log_stirlingSeq_sub_log_sqrt_pi_le hn
  rw [log_stirlingSeq_formula n] at hkey
  have hsqrt : Real.log (Real.sqrt π) = Real.log π / 2 := by
    rw [Real.log_sqrt Real.pi_pos.le]
  have hlog2n : Real.log (2 * (n : ℝ)) = Real.log 2 + Real.log n :=
    Real.log_mul (by norm_num) (ne_of_gt hnR)
  have hlog2pi : Real.log (2 * π) = Real.log 2 + Real.log π :=
    Real.log_mul (by norm_num) (ne_of_gt Real.pi_pos)
  have hdiv : Real.log ((n : ℝ) / Real.exp 1) = Real.log n - 1 := by
    rw [Real.log_div (ne_of_gt hnR) (Real.exp_ne_zero 1), Real.log_exp]
  rw [hsqrt, hlog2n, hdiv] at hkey
  rw [hlog2pi]
  linarith

/-! ### The matching lower bound

Robbins' other half.  Remarkably it needs no series estimate at all: the terms
are all nonnegative, so the sum dominates its FIRST term `⅓·x`, and that alone
already beats the telescoping gap.  The margin is exactly `24m+1`:

    ⅓·x ≥ 1/(12(m+1)+1) − 1/(12(m+2)+1)
      ⟺  36(2m+3)² ≤ (12m+13)(12m+25)
      ⟺  0 ≤ 24m + 1

true for every `m ≥ 0`, and tight at `m = 0` where the two sides differ by `1`.
-/

/-- **The telescoping step, from below.**  The first term of the series already
dominates `1/(12(m+1)+1) − 1/(12(m+2)+1)`. -/
theorem log_stirlingSeq_diff_ge_robbins (m : ℕ) :
    1 / (12 * ((m : ℝ) + 1) + 1) - 1 / (12 * ((m : ℝ) + 2) + 1)
      ≤ Real.log (stirlingSeq (m + 1)) - Real.log (stirlingSeq (m + 2)) := by
  have hm : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
  -- the sum dominates its first term, all terms being nonnegative
  have hfirst := le_hasSum (log_stirlingSeq_diff_hasSum m) 0 (fun j _ => by positivity)
  -- the algebraic content, stated over a real variable so no cast shape matters
  have key : ∀ x : ℝ, 0 ≤ x →
      1 / (12 * (x + 1) + 1) - 1 / (12 * (x + 2) + 1) ≤ 1 / (3 * (2 * x + 3) ^ 2) := by
    intro x hx
    have h1 : (0 : ℝ) < 12 * (x + 1) + 1 := by linarith
    have h2 : (0 : ℝ) < 12 * (x + 2) + 1 := by linarith
    rw [div_sub_div _ _ (ne_of_gt h1) (ne_of_gt h2),
      div_le_div_iff₀ (by positivity) (by positivity)]
    nlinarith [hx]
  refine le_trans (key (m : ℝ) hm) (le_trans (le_of_eq ?_) hfirst)
  push_cast
  field_simp
  ring

/-- The telescoped lower bound over any range. -/
theorem log_stirlingSeq_sub_ge_robbins {n m : ℕ} (hnm : n ≤ m) :
    1 / (12 * ((n : ℝ) + 1) + 1) - 1 / (12 * ((m : ℝ) + 1) + 1)
      ≤ Real.log (stirlingSeq (n + 1)) - Real.log (stirlingSeq (m + 1)) := by
  induction m, hnm using Nat.le_induction with
  | base => simp
  | succ p hp ih =>
      have hstep := log_stirlingSeq_diff_ge_robbins p
      push_cast at ih hstep ⊢
      ring_nf at ih hstep ⊢
      linarith

/-- **`1/(12n+1) ≤ log σ(n) − log √π`** for `n ≠ 0` — Robbins' lower refinement,
the counterpart of `log_stirlingSeq_sub_log_sqrt_pi_le`. -/
theorem le_log_stirlingSeq_sub_log_sqrt_pi {n : ℕ} (hn : n ≠ 0) :
    1 / (12 * (n : ℝ) + 1) ≤ Real.log (stirlingSeq n) - Real.log (Real.sqrt π) := by
  obtain ⟨p, rfl⟩ : ∃ p, n = p + 1 := ⟨n - 1, by omega⟩
  have hsqrt : (0 : ℝ) < Real.sqrt π := Real.sqrt_pos.mpr Real.pi_pos
  have hlim : Tendsto (fun m : ℕ => Real.log (stirlingSeq (m + 1))) atTop
      (𝓝 (Real.log (Real.sqrt π))) :=
    (Real.continuousAt_log (ne_of_gt hsqrt)).tendsto.comp
      (tendsto_stirlingSeq_sqrt_pi.comp (tendsto_add_atTop_nat 1))
  -- the telescoping bound is not a constant bound on `log σ`, so shift by the
  -- vanishing tail: `m ↦ log σ(m+1) − 1/(12(m+1)+1)` is antitone with the same limit.
  have htend0 : Tendsto (fun m : ℕ => 1 / (12 * ((m : ℝ) + 1) + 1)) atTop (𝓝 0) := by
    have hmono : Tendsto (fun m : ℕ => 12 * ((m : ℝ) + 1) + 1) atTop atTop := by
      refine tendsto_atTop_mono (fun m => ?_) tendsto_natCast_atTop_atTop
      have : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
      linarith
    simpa only [one_div] using hmono.inv_tendsto_atTop
  have hlim2 : Tendsto
      (fun m : ℕ => Real.log (stirlingSeq (m + 1)) - 1 / (12 * ((m : ℝ) + 1) + 1))
      atTop (𝓝 (Real.log (Real.sqrt π) - 0)) := hlim.sub htend0
  have hbd : ∀ᶠ m : ℕ in atTop,
      Real.log (stirlingSeq (m + 1)) - 1 / (12 * ((m : ℝ) + 1) + 1)
        ≤ Real.log (stirlingSeq (p + 1)) - 1 / (12 * ((p : ℝ) + 1) + 1) := by
    filter_upwards [eventually_ge_atTop p] with m hm
    linarith [log_stirlingSeq_sub_ge_robbins hm]
  have := le_of_tendsto hlim2 hbd
  push_cast
  linarith

/-- **Robbins' bounds, both sides.**  For `n ≠ 0`,

    n·log n − n + ½log n + ½log(2π) + 1/(12n+1)
      ≤ log n! ≤
    n·log n − n + ½log n + ½log(2π) + 1/(12n).

The lower bound strictly sharpens Mathlib's `Stirling.le_log_factorial_stirling`
(which has no `1/(12n+1)` term), and the upper bound has no Mathlib counterpart
at all.  Their gap is `1/(12n) − 1/(12n+1) = 1/(12n(12n+1)) = O(1/n²)`, which is
what `qou-mlgp` (A) needs: the `−(π/12N)cot θ` refinement requires the `1/(12k)`
term to `o(1/N)` accuracy, and either bound alone leaves an `O(1/N)` hole. -/
theorem le_log_factorial_stirling_robbins {n : ℕ} (hn : n ≠ 0) :
    (n : ℝ) * Real.log n - n + Real.log n / 2 + Real.log (2 * π) / 2
        + 1 / (12 * (n : ℝ) + 1)
      ≤ Real.log n ! := by
  have hnR : (0 : ℝ) < n := by exact_mod_cast Nat.pos_of_ne_zero hn
  have hkey := le_log_stirlingSeq_sub_log_sqrt_pi hn
  rw [log_stirlingSeq_formula n] at hkey
  have hsqrt : Real.log (Real.sqrt π) = Real.log π / 2 := Real.log_sqrt Real.pi_pos.le
  have hlog2n : Real.log (2 * (n : ℝ)) = Real.log 2 + Real.log n :=
    Real.log_mul (by norm_num) (ne_of_gt hnR)
  have hlog2pi : Real.log (2 * π) = Real.log 2 + Real.log π :=
    Real.log_mul (by norm_num) (ne_of_gt Real.pi_pos)
  have hdiv : Real.log ((n : ℝ) / Real.exp 1) = Real.log n - 1 := by
    rw [Real.log_div (ne_of_gt hnR) (Real.exp_ne_zero 1), Real.log_exp]
  rw [hsqrt, hlog2n, hdiv] at hkey
  rw [hlog2pi]
  linarith

end QOU.MathlibExt
