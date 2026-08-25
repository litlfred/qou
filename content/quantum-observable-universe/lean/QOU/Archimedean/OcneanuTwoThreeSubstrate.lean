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

theorem qb_two_pos (hq : 1 < q) : 0 < qb q 2 := by
  have h0 : q ≠ 0 := by positivity
  rw [qb_two_eq q h0 (q_sq_ne_one hq)]
  have : (0:ℝ) < q := by linarith
  positivity

theorem qb_three_pos (hq : 1 < q) : 0 < qb q 3 := by
  have h0 : q ≠ 0 := by positivity
  rw [qb_three_eq q h0 (q_sq_ne_one hq)]
  positivity

theorem qb_four_pos (hq : 1 < q) : 0 < qb q 4 := by
  have h0 : q ≠ 0 := by positivity
  rw [qb_four_eq q h0 (q_sq_ne_one hq)]
  have : (0:ℝ) < q := by linarith
  positivity

theorem qb_five_pos (hq : 1 < q) : 0 < qb q 5 := by
  have h0 : q ≠ 0 := by positivity
  rw [qb_five_eq q h0 (q_sq_ne_one hq)]
  positivity

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
      (ne_of_gt (qb_two_pos hq)) (ne_of_gt (qb_four_pos hq))
      (ne_of_gt (qb_five_pos hq))).mp h
  exact absurd h3 (ne_of_gt (qb_three_pos hq))

end QOU.Archimedean.OcneanuTwoThreeSubstrate
