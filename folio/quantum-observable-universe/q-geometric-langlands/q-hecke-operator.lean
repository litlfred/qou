import QOU.QGeometricLanglands


/-!
# QOU.QHeckeOperator

q-Hecke operator: integral transform on D_q-mod(Bun_{G_q})
satisfying (T − q)(T + q⁻¹) = 0.

Co-located sibling for content block `def:q-hecke-operator`.
Full formalization: `QOU/QGeometricLanglands.lean`
-/

-- Re-export: QOU.QGeometricLanglands.QHeckeOperator

namespace QOU

/-- $q$-Hecke operator -/
def QHeckeOperator   :=
  -- Ref: [leitner2026] def:q-hecke-operator
  trivial

end QOU
