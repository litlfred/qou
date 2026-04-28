/-!
# QOU.Organic.HydrogenCapacity — H capacity of CₙHₘ from chain topology

The hydrogen capacity of a molecular Hopf chain or ring as a
function of the carbon count N, the degree of unsaturation d, and
whether the chain is open or closed.

## References

- [manuscript] Ch. 10, Proposition `prop:hydrogen-capacity`
- [iupac2013] IUPAC Recommendations on Organic Nomenclature, 2013
-/

namespace QOU.Organic

/-- Hydrogen capacity for an open chain CₙHₘ with degree of
    unsaturation d. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:hydrogen-capacity
def hydrogenCapacityOpen (N d : ℕ) : ℤ :=
  2 * (N : ℤ) + 2 - 2 * (d : ℤ)

/-- Hydrogen capacity for a closed ring CₙHₘ with degree of
    unsaturation d. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:hydrogen-capacity
def hydrogenCapacityClosed (N d : ℕ) : ℤ :=
  2 * (N : ℤ) - 2 * (d : ℤ)

/-- Closed-ring formula equals open-chain formula minus 2. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:hydrogen-capacity
theorem closed_eq_open_minus_two (N d : ℕ) :
    hydrogenCapacityClosed N d = hydrogenCapacityOpen N d - 2 := by
  unfold hydrogenCapacityClosed hydrogenCapacityOpen
  ring

/-- Methane: N = 1, d = 0, open ⇒ m = 4. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:hydrogen-capacity
theorem methane : hydrogenCapacityOpen 1 0 = 4 := by
  unfold hydrogenCapacityOpen
  rfl

/-- Benzene: N = 6, d = 3, closed ⇒ m = 6. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:hydrogen-capacity
theorem benzene : hydrogenCapacityClosed 6 3 = 6 := by
  unfold hydrogenCapacityClosed
  rfl

/-- Cyclohexane: N = 6, d = 0, closed ⇒ m = 12. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:hydrogen-capacity
theorem cyclohexane : hydrogenCapacityClosed 6 0 = 12 := by
  unfold hydrogenCapacityClosed
  rfl

end QOU.Organic
