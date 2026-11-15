/-
# The ordered refinement: `Q² = 1` and `Q > 0` give `Q = 1`

Split out of `AveragedLetterSpectrum.lean` per §7c, which asks that a file
mixing generic-ring content with archimedean content be separated. That file is
generic `[Field K] [CharZero K]` throughout and uses no order; this one is the
single statement that needs one.

Note the order is carried as **typeclass hypotheses on a separate type
variable** `L`, not by specialising to `ℝ`. §7c's concern is a gratuitous `ℝ`
on an algebraic statement; there is none here, and a caller over any strictly
ordered field gets the result.

**`check-sidecars.sh` flags this file `§7c MIXED`, and that is a false
positive — do NOT "fix" it by specialising to `ℝ`.** The heuristic sets
`hasGen` on any of `[Field`, `[CommRing`, `{R : Type`, and `hasArch` on any
order-needing tactic, then reports the conjunction. A statement generic over
*ordered* fields matches both by construction, so no split can clear it: this
file already IS the split, and the flag simply moved here from
`AveragedLetterSpectrum.lean`. §7c exists to stop a gratuitous `ℝ` landing on
an algebraic statement; there is no `ℝ` here, and adding one to silence the
checker would be the exact defect the rule is written against. The documented
downgrade path (`pairedReal`, a `foo` / `foo_real` pair) does not apply either,
since there is no generic twin to pair with — the order is the content.

`-- Ref: [leitner2026] docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md`
-/
import QOU.MassTheory.AveragedLetterSpectrum
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith

namespace QOU.MassTheory

/-- With positivity, `Q = 1` — and then the scale is exactly the spectrum value.
For the averaged letter that value is `[2]_q/2`. -/
theorem second_parameter_is_one {L : Type*} [Field L] [LinearOrder L]
    [IsStrictOrderedRing L] (Q c t : L) (hQ : 0 < Q) (ht : t ≠ 0)
    (hpos : c * Q = t) (hneg : -(c * Q⁻¹) = -t) : Q = 1 ∧ c = t := by
  have hsq : Q ^ 2 = 1 :=
    second_parameter_forced Q c t (ne_of_gt hQ) ht hpos hneg
  have hQ1 : Q = 1 := by nlinarith [sq_nonneg (Q - 1)]
  refine ⟨hQ1, ?_⟩
  rw [hQ1, mul_one] at hpos
  exact hpos

end QOU.MassTheory
