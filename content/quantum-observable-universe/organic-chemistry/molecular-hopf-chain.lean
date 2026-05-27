import Mathlib.Data.Nat.Basic
import Mathlib.Data.Matrix.Basic


/-!
# QOU.Organic.MolecularHopfChain — Open molecular Hopf chain

A linear sequence of N atoms bonded pairwise by Hopf links.
The linking matrix is tridiagonal: L_{ij} = k if |i-j| = 1.
Crossing energy is (N-1) · E_bond(k).

## References

- [manuscript] Ch. 10, §2 Molecular Hopf chains and rings
-/

namespace QOU.Organic

/-- A molecular Hopf chain: N atoms bonded pairwise in a line. -/
-- Ref: [manuscript] Ch. 10, Definition: Molecular Hopf chain (open)
structure MolecularHopfChain where
  /-- Number of atoms in the chain. -/
  length : ℕ
  /-- At least 2 atoms. -/
  length_ge : 2 ≤ length
  /-- Bond order along the backbone. -/
  bondOrder : CovalentBond

/-- Number of bonds in an open chain. -/
def MolecularHopfChain.numBonds (c : MolecularHopfChain) : ℕ :=
  c.length - 1

/-- The linking matrix of a chain is tridiagonal:
    L_{ij} = k when |i-j| = 1, and 0 otherwise. -/
-- Ref: [manuscript] Ch. 10, Definition: Molecular Hopf chain (open)
def MolecularHopfChain.linkingMatrix (c : MolecularHopfChain)
    (i j : Fin c.length) : ℕ :=
  if (i.val + 1 = j.val) ∨ (j.val + 1 = i.val) then c.bondOrder.order
  else 0

/-- Alexander weight of a chain: (N-1) · Δ_{T(2,2)}(q) = N-1. -/
def MolecularHopfChain.alexanderWeight (c : MolecularHopfChain) : ℕ :=
  c.length - 1

end QOU.Organic
