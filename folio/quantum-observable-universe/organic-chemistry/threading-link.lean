import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.Ring.Parity
import Mathlib.Algebra.Order.Group.Nat


/-!
# QOU.Organic.ThreadingLink — Threading link T(2,N)

The threading link T(2,N) is a torus link that passes through all N
atoms in a molecular ring simultaneously.  Its Alexander polynomial
Δ_{T(2,2m)}(t) = (t^m - t^{-m})/(t - t^{-1}) carries half the
Alexander weight of N pairwise Hopf links.

## References

- [leitner2026] Ch. 10, §2 Molecular Hopf chains and rings
- [kauffman1991] https://doi.org/10.1142/1116
-/

namespace QOU.Organic

/-- The threading link T(2,N) for a ring of N atoms.
    For even N, this is a 2-component torus link.
    For odd N, it is a torus knot. -/
-- Ref: [leitner2026] Ch. 10, Definition: Threading link T(2,N)
structure ThreadingLink where
  /-- Number of atoms threaded. -/
  atoms : ℕ
  /-- At least 3 atoms for a ring. -/
  atoms_ge : 3 ≤ atoms

/-- Number of components of T(2,N) = gcd(2,N). -/
def ThreadingLink.numComponents (t : ThreadingLink) : ℕ :=
  Nat.gcd 2 t.atoms

/-- T(2,N) is a 2-component link when N is even. -/
theorem ThreadingLink.two_components_of_even (t : ThreadingLink)
    (h : Even t.atoms) : t.numComponents = 2 := by
  simp only [numComponents]
  have he : t.atoms % 2 = 0 := Nat.even_iff.mp h
  rw [Nat.gcd_rec, he]; decide

/-- T(2,N) is a knot (1 component) when N is odd. -/
theorem ThreadingLink.one_component_of_odd (t : ThreadingLink)
    (h : ¬Even t.atoms) : t.numComponents = 1 := by
  simp only [numComponents]
  have ho : t.atoms % 2 = 1 := Nat.odd_iff.mp (Nat.not_even_iff_odd.mp h)
  rw [Nat.gcd_rec, ho]; decide

/-- Number of crossings in the standard braid representation
    (σ₁σ₂⋯σ_{N-1})²: always 2(N-1). -/
def ThreadingLink.numCrossings (t : ThreadingLink) : ℕ :=
  2 * (t.atoms - 1)

/-- Alexander weight of T(2,2m) at q=1 is m = N/2.
    This is half the pairwise weight N.
    (Only valid for even N.) -/
-- Ref: [leitner2026] Ch. 10, Definition: Threading link T(2,N)
-- Ref: [kauffman1991] Kauffman, "Knots and Physics," World Scientific 1991
def ThreadingLink.alexanderWeightAtOne (t : ThreadingLink) : ℕ :=
  t.atoms / 2

/-- The threading efficiency: alexander weight / pairwise weight = 1/2
    for even N. -/
-- Ref: [leitner2026] Ch. 10, Proposition: Predicted vs. observed barrier
theorem ThreadingLink.half_efficiency (t : ThreadingLink)
    (h : Even t.atoms) :
    2 * t.alexanderWeightAtOne = t.atoms := by
  simp [alexanderWeightAtOne]
  obtain ⟨k, hk⟩ := h
  rw [hk]
  omega

end QOU.Organic
