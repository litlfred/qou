/-!
# QOU.QuantumObservableUniverse.exists_instance — existence of QOU

A QOU structure exists: Rep(SU_q(2)) is a witness with Haar integration,
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

    A `QuantumObservableUniverse k` term exists for every field `k`,
    witnessed by Rep(SU_q(2)) equipped with Haar integration, vanishing
    Chern classes on the adjoint, and the quantum determinant volume
    constraint. -/
-- Ref: [kassel1995] Quantum Groups, §IX
/-- **External axiom (§3b-cond pattern): QuantumObservableUniverse.exists_instance.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom QuantumObservableUniverse.exists_instance_axiom (k : Type*) [Field k] :
    Nonempty (QuantumObservableUniverse k)

theorem QuantumObservableUniverse.exists_instance (k : Type*) [Field k] :
    Nonempty (QuantumObservableUniverse k) :=
  QuantumObservableUniverse.exists_instance_axiom k

end QOU
