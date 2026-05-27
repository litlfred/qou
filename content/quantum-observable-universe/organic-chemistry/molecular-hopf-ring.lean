import Mathlib.Data.Nat.Basic


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
