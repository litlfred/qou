/-
# ⚠ NOT YET BUILT — DO NOT TREAT AS VERIFIED

This file has **never successfully compiled** in the environment it was written
in. The build reached 1126/1156 of `DilogReflection`'s Mathlib dependency cone
and was killed — no error, no completion line, zero `lean` workers afterwards.

It contains **no `sorry`**, and the mathematics is a one-line `linear_combination`
off an existing sorry-free theorem, so it is *expected* to compile. But expected
is not verified, and every other Lean file in this lane was built and had its
axioms audited before landing. **Build it before relying on it, and delete this
header when you do.**

Tracked in `qou-rhyp`.
-/

import QOU.Archimedean.DilogReflection

/-!
# Rogers reflection, from the corpus's real `LiTwo`

Bean `qou-rhyp`, item 1 — discharging four of the nine hypotheses that
`FiveTwoLevelSevenLadder.lean` takes abstractly.

`FiveTwoLevelSevenLadder.numerators_of_five_term` assumes `L (1 − x) = L1 − L x`
at four points. With Rogers `L` built from the corpus's real dilogarithm this is
not a new analytic fact: it follows from `LiTwo_reflection'`, which is already
**sorry-free** in `QOU/Archimedean/DilogReflection.lean`.

The reason it is free is a cancellation worth stating. Euler reflection carries a
correction term,

    LiTwo x + LiTwo (1 − x) = π²/6 − log x · log (1 − x),

and Rogers' two **half** `log·log` terms add to a **whole** one:

    L x + L (1 − x)
      = LiTwo x + LiTwo (1 − x) + ½·log x·log(1−x) + ½·log(1−x)·log x
      = LiTwo x + LiTwo (1 − x) + log x·log(1−x)
      = π²/6.

The correction cancels exactly. That is the whole content, and it is why the
Rogers normalisation is the one in which the level-7 ladder has rational values.

Note `LiTwo` lives in namespace `QOU.QPochhammer`, not `QOU.Archimedean`.

**Scope.** This discharges *reflection only*. The inversion and Landen extensions
and the five-term relation — the other five hypotheses — remain open; see
`qou-rhyp`. The 5₂ sum rule remains **verified to 80 dps, unproved**.
-/

namespace QOU.QBeta.FiveTwoRogersReflection

open QOU.QPochhammer

/-- The Rogers dilogarithm, built from the corpus's real `LiTwo`. -/
noncomputable def rogersL (x : ℝ) : ℝ :=
  LiTwo x + Real.log x * Real.log (1 - x) / 2

/-- **Rogers reflection**, from `LiTwo_reflection'`.

The Euler correction term `−log x · log(1−x)` is cancelled exactly by the two
half-`log·log` terms in the Rogers normalisation. -/
theorem rogersL_reflection {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    rogersL x + rogersL (1 - x) = Real.pi ^ 2 / 6 := by
  have h := LiTwo_reflection' x hx0 hx1
  have h1 : (1 : ℝ) - (1 - x) = x := by ring
  unfold rogersL
  rw [h1]
  linear_combination h

/-- The form the ladder file consumes: `L (1 − x) = L1 − L x` with `L1 = π²/6`. -/
theorem rogersL_one_sub {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    rogersL (1 - x) = Real.pi ^ 2 / 6 - rogersL x := by
  have h := rogersL_reflection hx0 hx1
  linarith

end QOU.QBeta.FiveTwoRogersReflection
