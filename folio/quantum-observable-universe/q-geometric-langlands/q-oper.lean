import QOU.QGeometricLanglands


/-!
# QOU.QOper

q-Oper: q-flat connection with transverse Borel reduction.
For SU_{q⁻¹}(2), equivalent to q-Sturm–Liouville operator ∂_q² + t(z).

Co-located sibling for content block `def:q-oper`.
Full formalization: `QOU/QGeometricLanglands.lean`
-/

-- Re-export: QOU.QGeometricLanglands.QOper

namespace QOU

/-- $q$-Oper -/
def QOper   :=
  -- Ref: [leitner2026] def:q-oper
  trivial

end QOU
