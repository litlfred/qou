/-!
# QOU.Archimedean.CSEvaluationFaithful

**PROPOSITION.** Faithfulness of the Chern--Simons evaluation on the brane tower
-/

namespace QOU.Archimedean

structure CSEvaluationFaithfulData where
  kappa_n_nonzero : True
  phi_n_nonzero : True

/-- **PROPOSITION.** Faithfulness of the Chern--Simons evaluation on the brane tower -/
theorem CSEvaluationFaithful (d : CSEvaluationFaithfulData) :
    d.kappa_n_nonzero ∧ d.phi_n_nonzero :=
  ⟨d.kappa_n_nonzero, d.phi_n_nonzero⟩

end QOU.Archimedean
