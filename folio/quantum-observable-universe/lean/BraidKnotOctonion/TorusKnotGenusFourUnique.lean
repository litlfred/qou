import Mathlib.Data.Nat.Notation
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.IntervalCases


/-!
# QOU.Archimedean.torus_knot_genus_four_unique

The torus knots `T_{m,n}` with `gcd(m,n) = 1`, `2 ≤ m ≤ n`, and
genus `(m-1)(n-1)/2 = 4` are exactly `T_{2,9}` and `T_{3,5}`.

LaTeX label: `prop:torus-knot-genus-four-unique`

## References

- [leitner2026] §5/torus-knot-genus-four-unique
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
    `m ≤ n`, `gcd(m,n) = 1` ordering) are `T_{2,9}` and `T_{3,5}`.

    Proof: `genus = (m-1)(n-1)/2 = 4` (floor division) forces
    `(m-1)(n-1) ∈ {8, 9}`.  Since `m-1 ≥ 1` and `n-1 ≥ 1`, both
    factors are `≤ 9`, bounding `m, n ≤ 10`; a finite case split
    (`interval_cases`) with the coprimality hypothesis leaves exactly
    `(2,9)` and `(3,5)` — the cofactor cases `(2,10)` and `(4,4)` are
    eliminated by `gcd ≠ 1`. -/
-- Ref: [leitner2026] §5/torus-knot-genus-four-unique
-- Ref: [rolfsen] Rolfsen, *Knots and Links*
theorem torus_knot_genus_four_unique (K : TorusKnot)
    (h : K.genus = 4) :
    (K.m = 2 ∧ K.n = 9) ∨ (K.m = 3 ∧ K.n = 5) := by
  have hm := K.m_ge_two
  have hmn := K.m_le_n
  have hco := K.coprime
  simp only [TorusKnot.genus] at h
  -- h : (K.m - 1) * (K.n - 1) / 2 = 4, hence the product is 8 or 9.
  have hub : (K.m - 1) * (K.n - 1) ≤ 9 := by omega
  -- Each factor is bounded by the product (the other factor is ≥ 1).
  have hmle : K.m - 1 ≤ (K.m - 1) * (K.n - 1) :=
    Nat.le_mul_of_pos_right _ (by omega)
  have hnle : K.n - 1 ≤ (K.m - 1) * (K.n - 1) :=
    Nat.le_mul_of_pos_left _ (by omega)
  have hmub : K.m ≤ 10 := by omega
  have hnub : K.n ≤ 10 := by omega
  interval_cases K.m <;> interval_cases K.n <;> revert hco h <;> decide

/-- The crossing numbers of the unique genus-4 pair are `9` and `10`. -/
-- Ref: [leitner2026] §5/torus-knot-genus-four-unique
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
