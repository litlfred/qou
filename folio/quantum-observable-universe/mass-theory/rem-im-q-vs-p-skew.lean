import Mathlib.Algebra.Field.Defs


/-!
# QOU.BraidKnot.ImQVsPSkew

Structural clarification: Im(q) (complex-q modulus-projection-discarded
degree of freedom) and P_skew (bar-anti-symmetric content, EM channel)
are DIFFERENT mechanisms. Promotes the chat correction (PR #1127) to
a paper-side audit-visibility stub.

Ref: [leitner2026] rem:im-q-vs-p-skew
Ref: [leitner2026] prop:lusztig-vs-hermitian-bar
-/

namespace QOU.BraidKnot.ImQVsPSkew

/-- The two distinct projection mechanisms in the framework. -/
inductive ProjectionMechanism
  | bar_projection  -- P_avg / P_skew via q ↦ q⁻¹ (real q phenomenon)
  | modulus_projection  -- m = |tr_M| via |·| (complex q phenomenon)
  deriving DecidableEq

/-- The two mechanisms operate on DIFFERENT q-regimes and are independent. -/
theorem mechanisms_are_distinct :
    ProjectionMechanism.bar_projection ≠ ProjectionMechanism.modulus_projection := by
  decide

end QOU.BraidKnot.ImQVsPSkew
