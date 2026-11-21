import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.Order.Ring.Defs


/-!
# QOU.Organic.CovalentBond — Covalent bond as shared Hopf links

A covalent bond of order k between two atoms is k shared trefoils
Hopf-linked to both atoms' residual sub-links.  The crossing energy
is k · E_cross(T(2,2)) plus inter-link interaction terms.

## References

- [leitner2026] Ch. 10, §1 Covalent bonding as shared sub-Hopf links
-/

namespace QOU.Organic

/-- A covalent bond of order `k` between two atoms.
    Each shared Hopf link contributes `E_cross(T(2,2))` to the
    crossing energy, plus pairwise inter-link interactions. -/
-- Ref: [leitner2026] Ch. 10, Definition: Covalent bond (shared Hopf links)
structure CovalentBond where
  /-- Bond order: number of shared Hopf links (1 = single, 2 = double, 3 = triple). -/
  order : ℕ
  /-- Bond order is at least 1. -/
  order_pos : 0 < order
  /-- Bond order is at most 3 (limited by linking sites). -/
  order_le : order ≤ 3

/-- Linking sites consumed per atom by a bond of order k. -/
def CovalentBond.sitesConsumed (b : CovalentBond) : ℕ := b.order

/-- A single bond. -/
def singleBond : CovalentBond where
  order := 1
  order_pos := by omega
  order_le := by omega

/-- A double bond. -/
def doubleBond : CovalentBond where
  order := 2
  order_pos := by omega
  order_le := by omega

/-- A triple bond. -/
def tripleBond : CovalentBond where
  order := 3
  order_pos := by omega
  order_le := by omega

end QOU.Organic
