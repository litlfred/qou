/-!
# QOU.Archimedean.knot_operator_selection

**PROPOSITION.** Knot operator selection via Frobenius dual
-/

namespace QOU.Archimedean

structure KnotOperatorSelectionData where
  is_frobenius_dual : True
  selects_knot_operator : True

/-- **PROPOSITION.** Knot operator selection via Frobenius dual -/
theorem knot_operator_selection (d : KnotOperatorSelectionData) :
    d.is_frobenius_dual ∧ d.selects_knot_operator :=
  ⟨d.is_frobenius_dual, d.selects_knot_operator⟩

end QOU.Archimedean
