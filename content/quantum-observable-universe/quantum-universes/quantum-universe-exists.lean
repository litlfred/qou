/-!
# QOU.QuantumUniverse.exists_instance — existence of a quantum universe

Trivial witness: R-Mod with A = R.  Richer witness: Rep(SU_q(2)).

LaTeX: `\label{prop:quantum-universe-exists}`

## References

- [manuscript] §1-quantum-universes/quantum-universe-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §XI
-/

import QOU.Basic

namespace QOU

/-- **Existence of a quantum universe over a base field `k`.**

    Records the claim that a `QuantumUniverse k` term exists for every
    field `k`.  The stub uses `sorry` because construction of a concrete
    witness (R-Mod or Rep(SU_q(2))) requires category/monoidal-category
    instances not yet provided in `QOU.Basic`. -/
-- Ref: [kassel1995] Quantum Groups, §XI
theorem QuantumUniverse.exists_instance (k : Type*) [Field k] :
    Nonempty (QuantumUniverse k) := by
  -- Witness: trivial category R-Mod with A = R; or Rep(SU_q(2)).
  -- Ref: [kassel1995] §XI
  sorry

end QOU
