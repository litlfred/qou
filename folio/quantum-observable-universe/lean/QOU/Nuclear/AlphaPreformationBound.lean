import Mathlib.Algebra.Order.Field.Basic

/-!
# A preformation probability cannot shorten an α half-life

In the Gamow picture the half-life with preformation `S` is `T / S`, where `T`
is the barrier (WKB) half-life. A preformation probability satisfies
`0 < S ≤ 1`. So it can only lengthen the half-life.

* `le_div_preformation`: `T ≤ T / S`.
* `preformation_cannot_close_of_lt`: if the barrier half-life already exceeds
  the reference half-life `Tref`, no admissible `S` reaches `Tref`. The
  discrepancy must then come from the barrier side (`Q`, radius, deformation)
  rather than from preformation.

Pure order algebra over an ordered field; no measured values appear. The
numerical partition of the emitters lives in
`computations/probes/alpha_preformation_bound/`.
-/

namespace QOU.Nuclear.AlphaPreformationBound

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

theorem le_div_preformation {T S : R} (hT : 0 ≤ T) (hS0 : 0 < S) (hS1 : S ≤ 1) :
    T ≤ T / S :=
  le_div_self hT hS0 hS1

theorem preformation_cannot_close_of_lt {T S Tref : R} (hT : 0 ≤ T) (hS0 : 0 < S)
    (hS1 : S ≤ 1) (hlt : Tref < T) : Tref < T / S :=
  lt_of_lt_of_le hlt (le_div_preformation hT hS0 hS1)

theorem preformation_ne_of_lt {T S Tref : R} (hT : 0 ≤ T) (hS0 : 0 < S)
    (hS1 : S ≤ 1) (hlt : Tref < T) : T / S ≠ Tref :=
  ne_of_gt (preformation_cannot_close_of_lt hT hS0 hS1 hlt)

/-- When the barrier half-life is too short, the preformation that closes the
gap is `S = T / Tref`, and it is admissible. -/
theorem required_preformation_admissible {T Tref : R} (hT : 0 < T) (hle : T ≤ Tref) :
    0 < T / Tref ∧ T / Tref ≤ 1 ∧ T / (T / Tref) = Tref := by
  have hTref : 0 < Tref := lt_of_lt_of_le hT hle
  exact ⟨div_pos hT hTref, (div_le_one hTref).mpr hle, div_div_cancel₀ hT.ne'⟩

end QOU.Nuclear.AlphaPreformationBound
