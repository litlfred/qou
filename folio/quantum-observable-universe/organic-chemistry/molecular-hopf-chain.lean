import Mathlib.Data.Matrix.Basic


/-!
# QOU.Organic.MolecularHopfChain — Open molecular Hopf chain

A linear sequence of N atoms bonded pairwise by Hopf links.
The linking matrix is tridiagonal: L_{ij} = k if |i-j| = 1.
Crossing energy is (N-1) · E_bond(k).

## References

- [leitner2026] Ch. 10, §2 Molecular Hopf chains and rings
-/

namespace QOU.Organic

/-- Honest mirror of the covalent bond from the sibling content-extract
    file `covalent-bond-types.lean` (not a cached library module, so
    inlined here for single-file `lean`-direct checking).  Fields match
    the canonical declaration's structure. -/
-- canonical decl: QOU.Organic.CovalentBond
-- Ref: [leitner2026] Ch. 10, Definition: Covalent bond (shared Hopf links)
structure CovalentBond where
  /-- Bond order: number of shared Hopf links (1 = single, 2 = double, 3 = triple). -/
  order : ℕ
  /-- Bond order is at least 1. -/
  order_pos : 0 < order
  /-- Bond order is at most 3 (limited by linking sites). -/
  order_le : order ≤ 3

/-- A molecular Hopf chain: N atoms bonded pairwise in a line. -/
-- Ref: [leitner2026] Ch. 10, Definition: Molecular Hopf chain (open)
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
-- Ref: [leitner2026] Ch. 10, Definition: Molecular Hopf chain (open)
def MolecularHopfChain.linkingMatrix (c : MolecularHopfChain)
    (i j : Fin c.length) : ℕ :=
  if (i.val + 1 = j.val) ∨ (j.val + 1 = i.val) then c.bondOrder.order
  else 0

/-- reduced Alexander weight (linking number) of a chain: (N-1) · Δ̃_{T(2,2)}(q) = N-1. -/
def MolecularHopfChain.alexanderWeight (c : MolecularHopfChain) : ℕ :=
  c.length - 1

end QOU.Organic
