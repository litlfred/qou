/-!
# QOU.QLocalSystem

q-Local system: a functor from the fundamental groupoid Π₁(X) to
Rep(G_q) with q-monodromy condition.

Co-located sibling for content block `def:q-local-system`.
Full formalization: `QOU/QGeometricLanglands.lean`
-/

import QOU.QGeometricLanglands

-- Re-export: QOU.QGeometricLanglands.QLocalSystem

namespace QOU

/-- **def:q-local-system** — placeholder stub; full definition TBD. -/
structure QLocalSystem where
  witness : ℝ
  witness_pos : 0 < witness
end QOU
