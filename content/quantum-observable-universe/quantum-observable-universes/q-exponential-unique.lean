/-!
# QOU.QExponential.unique — uniqueness of the q-exponential grouplike

Any two grouplikes of H_q satisfying the flow equation D_q e = e and
the counit condition ε(e) = 1 coincide.  Proof reduces to: the flow
equation on primitives has only the trivial solution.

LaTeX: `\label{prop:q-exponential-unique}`

## References

- [manuscript] §2-quantum-observable-universes/q-exponential-unique
- [kassel1995] Quantum Groups (Springer GTM 155), §III.3 (grouplikes)
-/

import QOU.Basic

namespace QOU

noncomputable section

/-- **Uniqueness of the q-exponential grouplike.**

    Two q-exponential structures on the same Hopf algebra with the
    same coproduct, counit, and q-Jackson derivative have equal
    grouplike elements.

    The argument: if `e₁, e₂` both satisfy `D_q eᵢ = eᵢ` and the
    grouplike axiom, then `e₁ - e₂` is a primitive element fixed by
    `D_q` with counit zero; the only such element is `0`. -/
-- Ref: [kassel1995] Quantum Groups, §III.3
theorem QExponential.unique {H : Type*} (e₁ e₂ : QExponential H)
    (h_coprod : e₁.coprod = e₂.coprod)
    (h_counit : e₁.counit = e₂.counit)
    (h_Dq : e₁.D_q = e₂.D_q) :
    e₁.e_q = e₂.e_q := by
  -- Reduction to: the flow equation D_q p = p on primitives has only
  -- the zero solution.  Requires primitive-decomposition of H_q via
  -- Milnor–Moore, which is not in Mathlib.
  -- Ref: [kassel1995] Quantum Groups, §III.3
  sorry

end

end QOU
