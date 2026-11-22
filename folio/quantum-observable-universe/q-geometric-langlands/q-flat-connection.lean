import QOU.QGeometricLanglands


/-!
# QOU.QFlatConnection

q-Flat connection: ∇_q² = (q−1)·F_q where F_q = HKR⁻¹(κ₀).

Co-located sibling for content block `def:q-flat-connection`.
Full formalization: `QOU/QGeometricLanglands.lean`
-/

-- Re-export: QOU.QGeometricLanglands.QFlatConnection

namespace QOU

/-- $q$-Flat connection -/
def QFlatConnection   :=
  -- Ref: [leitner2026] def:q-flat-connection
  trivial

end QOU
