import Mathlib.Data.Nat.Notation
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.IntervalCases


/-!
# QOU.Archimedean.torus_knot_genus_four_unique

The torus knots `T_{m,n}` with `gcd(m,n) = 1`, `2 ≤ m ≤ n`, and
genus `(m-1)(n-1)/2 = 4` are exactly `T_{2,9}` and `T_{3,5}`.

LaTeX label: `prop:torus-knot-genus-four-unique`

## References

- [manuscript] §5/torus-knot-genus-four-unique
- [rolfsen] Rolfsen, *Knots and Links*
-/

namespace QOU.Archimedean

/-- A torus knot `T_{m,n}` with `2 ≤ m ≤ n`, `gcd(m,n) = 1`. -/
structure TorusKnot where
  m : ℕ
  n : ℕ
  m_ge_two : 2 ≤ m
  m_le_n : m ≤ n
  coprime : Nat.gcd m n = 1

namespace TorusKnot

variable (K : TorusKnot)

/-- Genus of a torus knot: `g = (m-1)(n-1)/2`. -/
def genus : ℕ := (K.m - 1) * (K.n - 1) / 2

/-- Crossing number of a torus knot: `c = (m-1)n` for `m ≤ n`.
    This is the standard torus-knot formula `min ((m-1)n) (m(n-1))`;
    under the built-in hypothesis `m ≤ n` we have `(m-1)n ≤ m(n-1)`,
    so the minimum is `(m-1)n`. -/
def crossingNumber : ℕ := (K.m - 1) * K.n

end TorusKnot

/-- **Proposition (genus-4 torus knot uniqueness)**.

    The only torus knots of genus `4` (under the canonical
    `m ≤ n`, `gcd(m,n) = 1` ordering) are `T_{2,9}` and `T_{3,5}`. -/
-- Ref: [manuscript] §5/torus-knot-genus-four-unique
-- Ref: [rolfsen] Rolfsen, *Knots and Links*
-- Ref: [manuscript] the previous explicit proof no longer typechecked under the
-- current Lean/Mathlib stack, so this file temporarily keeps the cited
-- classification result as a `sorry`-backed placeholder until the arithmetic
-- proof is restored.
-- TODO: restore a proof once the arithmetic script is updated for the current
-- Lean/Mathlib toolchain.
theorem torus_knot_genus_four_unique (K : TorusKnot)
    (h : K.genus = 4) :
    (K.m = 2 ∧ K.n = 9) ∨ (K.m = 3 ∧ K.n = 5) := by
  sorry

/-- The crossing numbers of the unique genus-4 pair are `9` and `10`. -/
-- Ref: [manuscript] §5/torus-knot-genus-four-unique
theorem genus_four_crossing_numbers (K : TorusKnot)
    (h : K.genus = 4) :
    K.crossingNumber = 9 ∨ K.crossingNumber = 10 := by
  rcases torus_knot_genus_four_unique K h with ⟨hm, hn⟩ | ⟨hm, hn⟩
  · left
    unfold TorusKnot.crossingNumber
    rw [hm, hn]
  · right
    unfold TorusKnot.crossingNumber
    rw [hm, hn]

end QOU.Archimedean
