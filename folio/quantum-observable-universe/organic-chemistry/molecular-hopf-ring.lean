import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.Ring.Parity
import Mathlib.Algebra.Order.Group.Nat


/-!
# QOU.Organic.MolecularHopfRing — Threaded molecular ring

A molecular Hopf ring is N atoms bound by a single threading link
T(2,N), not by pairwise Hopf links.  The crossing energy is
proportional to the Alexander polynomial Δ_{T(2,N)}(q), which
carries half the weight of the pairwise construction.

## References

- [manuscript] Ch. 10, §2 Molecular Hopf chains and rings
-/

namespace QOU.Organic

/-- Honest mirror of the threading link T(2,N) from the sibling
    content-extract file `threading-link.lean` (not a cached library
    module, so inlined here for single-file `lean`-direct checking).
    Fields match the canonical declaration's structure. -/
-- canonical decl: QOU.Organic.ThreadingLink
-- Ref: [manuscript] Ch. 10, Definition: Threading link T(2,N)
structure ThreadingLink where
  /-- Number of atoms threaded. -/
  atoms : ℕ
  /-- At least 3 atoms for a ring. -/
  atoms_ge : 3 ≤ atoms

/-- Alexander weight of T(2,2m) at q=1 is m = N/2 (mirror of the
    canonical `QOU.Organic.ThreadingLink.alexanderWeightAtOne`). -/
-- canonical decl: QOU.Organic.ThreadingLink.alexanderWeightAtOne
-- Ref: [manuscript] Ch. 10, Definition: Threading link T(2,N)
def ThreadingLink.alexanderWeightAtOne (t : ThreadingLink) : ℕ :=
  t.atoms / 2

/-- A molecular Hopf ring: N atoms bound by a threading link T(2,N). -/
-- Ref: [manuscript] Ch. 10, Definition: Molecular Hopf ring (closed)
structure MolecularHopfRing where
  /-- The threading link binding the ring. -/
  threading : ThreadingLink

/-- Number of atoms in the ring. -/
def MolecularHopfRing.length (r : MolecularHopfRing) : ℕ :=
  r.threading.atoms

/-- Alexander weight of the ring (at q=1) is N/2. -/
def MolecularHopfRing.alexanderWeight (r : MolecularHopfRing) : ℕ :=
  r.threading.alexanderWeightAtOne

/-- The ring's Alexander weight is strictly less than the chain's
    for N ≥ 4. This means the ring is energetically more efficient. -/
-- Ref: [manuscript] Ch. 10, Remark: Why the C₆ chain resists hexagonalisation
theorem MolecularHopfRing.weight_lt_chain (r : MolecularHopfRing)
    (heven : Even r.threading.atoms)
    (hge : 4 ≤ r.threading.atoms) :
    r.alexanderWeight < r.threading.atoms - 1 := by
  simp [alexanderWeight, ThreadingLink.alexanderWeightAtOne]
  obtain ⟨k, hk⟩ := heven
  rw [hk]
  omega

end QOU.Organic
