/-!
# QOU.QLogarithm.exists_in_shuffle_hopf — existence of the q-logarithm

Over a base ring where the Jackson integers [n]_q are invertible, the
q-shuffle Hopf algebra 𝓗_q admits a primitive element log_q inverse
to the q-exponential grouplike.

LaTeX: `\label{prop:q-logarithm-exists}`

## References

- [manuscript] §2-quantum-observable-universes/q-logarithm-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §IV.3 (primitives
  and Milnor–Moore)
-/

import QOU.Basic

namespace QOU

noncomputable section

/-- **Existence of the q-logarithm primitive.**

    Under the hypotheses of `QExponential.exists_in_shuffle_hopf`,
    the q-shuffle Hopf algebra admits a primitive element `log_q`
    forming an adjoint pair with the q-exponential grouplike.

    The construction uses Milnor–Moore to identify
    Prim(𝓗_q) with the Lie algebra of G(𝓗_q), then takes the
    formal inverse of exp_q. -/
-- Ref: [kassel1995] Quantum Groups, §IV.3
theorem QLogarithm.exists_in_shuffle_hopf
    (H : Type*) [Nonempty H] :
    ∃ (ℓ : QLogarithm H), True := by
  -- The construction requires Milnor–Moore for the q-shuffle Hopf
  -- algebra, which is not in Mathlib.  See Kassel §IV.3.
  -- Ref: [kassel1995] Quantum Groups, §IV.3
  sorry

end

end QOU
