/-!
# QOU.Descartes.torus_knot_genus_four_unique

The torus knots `T_{m,n}` with `gcd(m,n) = 1`, `2 ≤ m ≤ n`, and
genus `(m-1)(n-1)/2 = 4` are exactly `T_{2,9}` and `T_{3,5}`.

LaTeX label: `prop:torus-knot-genus-four-unique`

## References

- [manuscript] §5/torus-knot-genus-four-unique
- [rolfsen] Rolfsen, *Knots and Links*
-/

import Mathlib.Data.Nat.Defs
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.IntervalCases

namespace QOU.Descartes

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

/-- Crossing number of a torus knot: `c = m(n-1)` for `m ≤ n`. -/
def crossingNumber : ℕ := K.m * (K.n - 1)

end TorusKnot

/-- **Proposition (genus-4 torus knot uniqueness)**.

    The only torus knots of genus `4` (under the canonical
    `m ≤ n`, `gcd(m,n) = 1` ordering) are `T_{2,9}` and `T_{3,5}`. -/
-- Ref: [manuscript] §5/torus-knot-genus-four-unique
-- Ref: [rolfsen] Rolfsen, *Knots and Links*
theorem torus_knot_genus_four_unique (K : TorusKnot)
    (h : K.genus = 4) :
    (K.m = 2 ∧ K.n = 9) ∨ (K.m = 3 ∧ K.n = 5) := by
  obtain ⟨m, n, hm_ge, hmn, hcop⟩ := K
  simp only [TorusKnot.genus] at h
  -- h : (m - 1) * (n - 1) / 2 = 4, i.e. (m-1)(n-1) ∈ {8, 9}
  have hprod_lo : 8 ≤ (m - 1) * (n - 1) := by omega
  have hprod_hi : (m - 1) * (n - 1) ≤ 9 := by omega
  -- (m-1)² ≤ (m-1)(n-1) ≤ 9 ⇒ m ≤ 4
  have hm_le : m ≤ 4 := by
    have hsq : (m - 1) * (m - 1) ≤ (m - 1) * (n - 1) :=
      Nat.mul_le_mul_left _ (by omega : m - 1 ≤ n - 1)
    have : (m - 1) * (m - 1) ≤ 9 := le_trans hsq hprod_hi
    -- (m-1)² ≤ 9 ⇒ m - 1 ≤ 3 ⇒ m ≤ 4
    rcases Nat.lt_or_ge m 5 with hlt | hge
    · omega
    · exfalso
      have : 4 ≤ m - 1 := by omega
      have : 16 ≤ (m - 1) * (m - 1) := Nat.mul_le_mul this this
      omega
  -- Bound n ≤ 10 from (n-1) ≤ (m-1)(n-1) ≤ 9 (using m - 1 ≥ 1)
  have hn_le : n ≤ 10 := by
    have h1 : 1 * (n - 1) ≤ (m - 1) * (n - 1) :=
      Nat.mul_le_mul_right _ (by omega : 1 ≤ m - 1)
    have : n - 1 ≤ 9 := by omega
    omega
  -- Case analysis on m ∈ {2, 3, 4}
  interval_cases m
  · -- m = 2: (n-1)/2 = 4, so n ∈ {9, 10}; gcd(2,n) = 1 forces n = 9
    interval_cases n <;> simp_all <;> omega
  · -- m = 3: 2(n-1)/2 = (n-1) = 4, so n = 5
    interval_cases n <;> simp_all <;> omega
  · -- m = 4: 3(n-1)/2 = 4 ⇒ 3(n-1) ∈ {8, 9}; only n = 4 (gcd violated)
    interval_cases n <;> simp_all <;> omega

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

end QOU.Descartes
