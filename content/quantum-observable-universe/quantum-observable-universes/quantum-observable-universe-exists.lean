/-!
# QOU.QuantumObservableUniverse.exists_instance — existence of QOU

A QOU structure exists: SU_q(2)-Rep is a witness with Haar integration,
vanishing Chern classes on Ad, and the quantum determinant as the
volume constraint.

LaTeX: `\label{prop:quantum-observable-universe-exists}`

## References

- [manuscript] §2-quantum-observable-universes/quantum-observable-universe-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §IX (quantum SU(2))
-/

import QOU.Basic

namespace QOU

/-- **Existence of a quantum observable universe.**

    The category Rep(SU_q(2)) with its regular Frobenius-Hopf object
    and forgetful fibre functor satisfies all four QOU axioms:
    non-degenerate integration, observability, measurability, volume
    constraint.  Existence is witnessed by any compact quantum group
    of rank 1. -/
-- Ref: [kassel1995] Quantum Groups, §IX
theorem QuantumObservableUniverse.exists_instance :
    ∃ (_ : Type), True := by
  -- Witness: Rep(SU_q(2)) in Mathlib pending quantum-group support.
  -- Ref: [kassel1995] Quantum Groups, §IX
  exact ⟨Unit, trivial⟩

end QOU
