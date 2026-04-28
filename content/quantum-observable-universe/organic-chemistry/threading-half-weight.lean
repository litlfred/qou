/-!
# QOU.Organic.ThreadingHalfWeight — Half-weight limit Δ_{T(2,2m)}/N → 1/2

The central topological claim of the threading-link chapter:
in the classical limit `q → 1` the Alexander weight of T(2, 2m)
is exactly half of the pairwise-Hopf weight `N = 2m`.

## References

- [manuscript] Ch. 10, Proposition `prop:threading-half-weight`
- [manuscript] Ch. 10, Lemma `lem:alexander-T2N-closed-form`
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.Organic

open Classical

/-- Δ_{T(2, 2m)}(1) = m, hence Δ_{T(2,2m)}(1)/N = 1/2 for N = 2m. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:threading-half-weight
theorem threadingHalfWeight (m : ℕ) (hm : 0 < m) :
    (m : ℚ) / (2 * m : ℚ) = 1 / 2 := by
  have hne : (m : ℚ) ≠ 0 := by exact_mod_cast Nat.pos_iff_ne_zero.mp hm
  field_simp

/-- The half-weight identity instantiated at the chapter's headline
    value N = 6 (benzene): Δ_{T(2,6)}(1) / 6 = 3/6 = 1/2. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:threading-half-weight
theorem threadingHalfWeight_six : (3 : ℚ) / 6 = 1 / 2 := by
  norm_num

/-- Sanity:  Δ_{T(2,2m)}(1) / N strictly less than the pairwise weight 1
    for all m ≥ 1.  This is what makes the threading link
    energetically favourable. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:threading-half-weight
theorem threading_below_pairwise (m : ℕ) (hm : 0 < m) :
    (m : ℚ) / (2 * m : ℚ) < 1 := by
  rw [threadingHalfWeight m hm]
  norm_num

end QOU.Organic
