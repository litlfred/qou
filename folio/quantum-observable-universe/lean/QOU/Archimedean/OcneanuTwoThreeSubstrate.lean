import QOU.Eightfold.OcneanuTwoThreeNotProportional

/-!
# QOU.Archimedean.OcneanuTwoThreeSubstrate — the two ratios really do differ over `ℝ`

Bean `qou-bhfg`. The **archimedean** half of
`QOU.Eightfold.OcneanuTwoThreeNotProportional`, split per AGENTS.md §7c: the
generic file states the gate over an arbitrary field and mentions no ordering,
and `ℝ` enters only here, to discharge the gate's right-hand side.

## What it discharges

The generic file proves the `N=2` and `N=3` Ocneanu weight ratios are equal
**iff** `[3]_q = 0`, and that `[3]_q = q² + 1 + q⁻²`. Over an ordered field that
is a sum of positive terms, so it never vanishes and the ratios always differ.

This is what upgrades the exclusion's stated reason from *"differs at every `q`
tested"* to a proof: the discrepancy is exactly `[3]_q`, and `[3]_q > 0`.

## Scope

Unchanged from the generic file: this concerns the quoted ratio formula
`y_{(2,1)}/y_{(3)} = q [2]_q [N−1]_q / [N+2]_q`, which is consumed from
`docs/audits/2026-08-07-two-row-projection-is-the-pairwise-cap.md` and not
re-derived. It says the `N=2` and `N=3` weightings differ; it says nothing
about whether `N = 3` is otherwise available.
-/

namespace QOU.Archimedean.OcneanuTwoThreeSubstrate

open QOU.Eightfold.OcneanuTwoThreeNotProportional

variable {q : ℝ}

theorem q_sq_ne_one (hq : 1 < q) : q ^ 2 ≠ 1 := by nlinarith

/-- **Every `q`-integer is positive at `q > 1`.** One lemma in place of a
per-index battery: `[m]_q = (qᵐ − q⁻ᵐ)/(q − q⁻¹)` has a positive numerator
(`qᵐ > 1 > q⁻ᵐ`) over a positive denominator (`q > 1 > q⁻¹`). -/
theorem qb_pos (hq : 1 < q) {m : ℕ} (hm : m ≠ 0) : 0 < qb q m := by
  have hq0 : (0:ℝ) < q := by linarith
  have hpm : 1 < q ^ m := one_lt_pow₀ hq hm
  have hppos : (0:ℝ) < q ^ m := by positivity
  rw [qb]
  apply div_pos
  · have : (q ^ m)⁻¹ < 1 := by
      rw [inv_lt_one_iff₀]; right; exact hpm
    linarith
  · have : q⁻¹ < 1 := by
      rw [inv_lt_one_iff₀]; right; exact hq
    linarith

/-- **Positivity of the canonical balanced `q`-integer at `q > 1`.**

Stated on `QOU.QInteger.qIntBal` rather than on the local `qb`, at the request
of the agent working bean `qou-qint` (PR #5746): the canonical module is generic
over a field and so carries no ordering — correctly, per §7c — which leaves
positivity genuinely absent from it. This is the right side of the wall for it,
and `qIntBal` is the right object to say it about. -/
theorem qIntBal_pos (hq : 1 < q) {m : ℕ} (hm : m ≠ 0) :
    0 < QOU.QInteger.qIntBal q m := by
  rw [← qb_eq_canonical]; exact qb_pos hq hm

/-- **The exclusion, proved.** At any real `q > 1` — the substrate sits at
`q₀ ≈ 1.10998` — the `N = 2` and `N = 3` Ocneanu weight ratios are different.

So moving to `N = 3` does not merely add the singlet channel; it re-weights the
channels already in use. That is the content the exclusion row asserts, and it
no longer rests on a sample. -/
theorem ocneanu_ratio_N2_ne_N3 (hq : 1 < q) :
    q * qb q 2 * qb q 1 / qb q 4 ≠ q * qb q 2 * qb q 2 / qb q 5 := by
  have h0 : q ≠ 0 := by positivity
  intro h
  have h3 : qb q 3 = 0 :=
    (ratio_eq_iff_qb_three_eq_zero q h0 (q_sq_ne_one hq)
      (ne_of_gt (qb_pos hq (by norm_num))) (ne_of_gt (qb_pos hq (by norm_num)))
      (ne_of_gt (qb_pos hq (by norm_num)))).mp h
  exact absurd h3 (ne_of_gt (qb_pos hq (by norm_num)))

/-- **The exclusion at full strength.** For *every* `N`, the Ocneanu weight
ratios at `N` and at `N + 1` differ — and by `qb_shift_identity` the discrepancy
is the same `[3]_q` at every `N`.

So the recorded reason for the route-3 exclusion — *"the `N=2` and `N=3` traces
are not proportional"* — is the `N = 2` case of a fact that holds all the way
up: no re-tuning to an adjacent `N` reproduces the weighting. -/
theorem ocneanu_ratio_adjacent_ne (hq : 1 < q) (n : ℕ) :
    q * qb q 2 * qb q n / qb q (n + 3) ≠ q * qb q 2 * qb q (n + 1) / qb q (n + 4) := by
  have h0 : q ≠ 0 := by positivity
  have hd3 : qb q (n + 3) ≠ 0 := ne_of_gt (qb_pos hq (by omega))
  have hd4 : qb q (n + 4) ≠ 0 := ne_of_gt (qb_pos hq (by omega))
  have h2 : q * qb q 2 ≠ 0 := mul_ne_zero h0 (ne_of_gt (qb_pos hq (by norm_num)))
  have hid := qb_shift_identity q h0 (q_sq_ne_one hq) n
  have h3 : qb q 3 ≠ 0 := ne_of_gt (qb_pos hq (by norm_num))
  intro h
  rw [div_eq_div_iff hd3 hd4] at h
  apply h3
  have hc : qb q (n + 1) * qb q (n + 3) - qb q n * qb q (n + 4) = 0 := by
    apply mul_left_cancel₀ h2
    linear_combination -h
  linear_combination hc - hid

end QOU.Archimedean.OcneanuTwoThreeSubstrate
