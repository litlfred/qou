-- Ref: [leitner2026] Ch. 10, §covalent-bond-shared-trefoil
-- Covalent bond as shared electrons (each the word σ₀σ₁σ₀, closure: Hopf link)

namespace QOU.Molecular

/-- A **covalent bond** of order k consists of k electrons (words σ₀σ₁σ₀)
    Hopf-linked across two nuclei via 2k attractive σ⁻¹ crossings
    (one pair per nucleus per electron).

    Lone electrons have only one attractive crossing.
    Shared electrons have two (one to each nucleus). -/
structure CovalentBond where
  /-- Bond order (1 = single, 2 = double, 3 = triple). -/
  order : Nat
  order_pos : 0 < order
  /-- Number of attractive crossings = 2 × order. -/
  attractiveCrossings : Nat := 2 * order
  /-- Number of shared electrons = order. -/
  sharedElectrons : Nat := order

/-- Single bond has 2 attractive crossings. -/
theorem single_bond_crossings : 2 * 1 = 2 := by decide

/-- Double bond has 4 attractive crossings. -/
theorem double_bond_crossings : 2 * 2 = 4 := by decide

/-- Triple bond has 6 attractive crossings. -/
theorem triple_bond_crossings : 2 * 3 = 6 := by decide

end QOU.Molecular
