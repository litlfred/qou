import QOU.QGeometricLanglands


/-!
# QOU.QLocalSystem

q-Local system: a functor from the fundamental groupoid Π₁(X) to
Rep(G_q) with q-monodromy condition.

Co-located sibling for content block `def:q-local-system`.
Full formalization: `QOU/QGeometricLanglands.lean`
-/

-- Re-export: QOU.QGeometricLanglands.QLocalSystem

namespace QOU

/-- $q$-Local system -/
def QLocalSystem   :=
  -- Ref: [leitner2026] def:q-local-system
  trivial

end QOU
