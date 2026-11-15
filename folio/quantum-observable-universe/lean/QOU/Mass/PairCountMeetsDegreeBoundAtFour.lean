/-
# The regular-graph degree bound meets the pair count only at A = 4

`QOU.Mass.TypedBondSiteInvariance` bounds the A = 4 binding ratio by the
*regular simple-graph* degree bound `2 * (A - 1)`, while the coordination weight
`w z = B / C(A,2)` divides by the *pair count* `C(A,2) = A * (A - 1) / 2`.

At `A = 4` both equal `6`, so `ε(3)/ε(1) = (B 4 / 6) / B 2` and "the factor by
which `B 4 / B 2` exceeds the pairwise wall" are the *same number* — the two
readings are numerically indistinguishable there.

This file proves that the coincidence happens at `A = 4` and **nowhere else**
with `2 ≤ A`. The consequence is a caution rather than a result: `A = 4` is the
arc's only convention-free coordinate, and it is simultaneously the unique place
two distinct questions collapse onto one number, so agreement there is *less*
discriminating than it looks.

No `sorry`. Statements are over `ℕ`; the doubled form avoids division.
-/
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.IntervalCases

namespace QOU.Mass.PairCountMeetsDegreeBoundAtFour

/-- Regular simple-graph degree bound on the binding ratio at mass number `A`. -/
def degreeBound (A : ℕ) : ℕ := 2 * (A - 1)

/-- Doubled pair count `2 * C(A,2) = A * (A - 1)`, division-free. -/
def twicePairCount (A : ℕ) : ℕ := A * (A - 1)

/-- Doubled degree bound, so the two are compared in the same units. -/
def twiceDegreeBound (A : ℕ) : ℕ := 2 * degreeBound A

/-- At `A = 4` the two coincide: both pair count and degree bound are `6`. -/
theorem coincide_at_four : twicePairCount 4 = twiceDegreeBound 4 := by
  unfold twicePairCount twiceDegreeBound degreeBound
  norm_num

/-- The pair count at `A = 4` is `6`. -/
theorem pairCount_four : twicePairCount 4 = 12 := by
  unfold twicePairCount; norm_num

/-- The degree bound at `A = 4` is `6`. -/
theorem degreeBound_four : degreeBound 4 = 6 := by
  unfold degreeBound; norm_num

/-- **The coincidence is unique.** For `2 ≤ A`, the doubled pair count equals
the doubled degree bound exactly when `A = 4`. -/
theorem eq_iff_four {A : ℕ} (hA : 2 ≤ A) :
    twicePairCount A = twiceDegreeBound A ↔ A = 4 := by
  unfold twicePairCount twiceDegreeBound degreeBound
  obtain ⟨k, rfl⟩ : ∃ k, A = k + 2 := ⟨A - 2, by omega⟩
  have hsub : k + 2 - 1 = k + 1 := by omega
  rw [hsub]
  constructor
  · intro h
    -- (k+2)*(k+1) = 4*(k+1), and (k+1) > 0, so k+2 = 4
    have hk : (k + 2) * (k + 1) = 4 * (k + 1) := by rw [h]; ring
    have : k + 2 = 4 := Nat.eq_of_mul_eq_mul_right (by omega) hk
    omega
  · rintro h
    have : k = 2 := by omega
    subst this; norm_num

/-- Below `A = 4` the pair count is strictly smaller than the degree bound. -/
theorem pairCount_lt_of_lt_four {A : ℕ} (h2 : 2 ≤ A) (h4 : A < 4) :
    twicePairCount A < twiceDegreeBound A := by
  interval_cases A <;> · unfold twicePairCount twiceDegreeBound degreeBound; norm_num

/-- Above `A = 4` the pair count strictly exceeds the degree bound, so the
coordination weight and the wall-excess reading diverge and keep diverging. -/
theorem degreeBound_lt_of_four_lt {A : ℕ} (h : 4 < A) :
    twiceDegreeBound A < twicePairCount A := by
  unfold twicePairCount twiceDegreeBound degreeBound
  obtain ⟨k, rfl⟩ : ∃ k, A = k + 5 := ⟨A - 5, by omega⟩
  have hsub : k + 5 - 1 = k + 4 := by omega
  rw [hsub]
  nlinarith [Nat.zero_le k]

end QOU.Mass.PairCountMeetsDegreeBoundAtFour
