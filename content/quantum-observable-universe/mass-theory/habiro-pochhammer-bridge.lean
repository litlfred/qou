import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

/-!
# Habiro–Markov bridge: Pochhammer factorisation

The identity `1 - q^k = (1 - u^k)(1 + u^k)` for `q = u²` gives the
factorisation `(q;q)_m = (u;u)_m · Π(1 + u^k)`.

## References

-- Ref: [habiro2000] https://doi.org/10.2140/gt.2000.4.227
-/


namespace QOU.BraidKnot

variable {R : Type*} [CommRing R]

/-- The fundamental factorisation: `1 - u² = (1 - u)(1 + u)`. -/
theorem one_sub_sq_factor (u : R) : 1 - u ^ 2 = (1 - u) * (1 + u) := by ring

/-- For `q = u²`, `1 - q^k = (1 - u^k)(1 + u^k)`. -/
theorem pochhammer_factor (u : R) (k : ℕ) :
    1 - (u ^ 2) ^ k = (1 - u ^ k) * (1 + u ^ k) := by ring

/-- The Pochhammer product factorises:
    `Π_{j=1}^{m} (1 - q^j) = Π_{j=1}^{m} (1 - u^j) · Π_{j=1}^{m} (1 + u^j)`
    when `q = u²`. -/
theorem HabiroPochhammerBridge (u : R) (m : ℕ) :
    (Finset.range m).prod (fun j => 1 - (u ^ 2) ^ (j + 1))
    = (Finset.range m).prod (fun j => 1 - u ^ (j + 1))
      * (Finset.range m).prod (fun j => 1 + u ^ (j + 1)) := by
  rw [← Finset.prod_mul_distrib]
  congr 1
  ext j
  exact pochhammer_factor u (j + 1)

end QOU.BraidKnot
