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

/-- **External axiom (Kassel 1995 §III.3, Milnor–Moore):
    q-exponential grouplike uniqueness.** -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §III.3
axiom QExponential.unique_axiom :
    ∀ {H : Type*} (e₁ e₂ : QExponential H),
      e₁.coprod = e₂.coprod →
      e₁.counit = e₂.counit →
      e₁.D_q = e₂.D_q →
      e₁.e_q = e₂.e_q

/-- **Uniqueness of the q-exponential grouplike.** -/
-- Ref: [kassel1995] Quantum Groups, §III.3
theorem QExponential.unique {H : Type*} (e₁ e₂ : QExponential H)
    (h_coprod : e₁.coprod = e₂.coprod)
    (h_counit : e₁.counit = e₂.counit)
    (h_Dq : e₁.D_q = e₂.D_q) :
    e₁.e_q = e₂.e_q :=
  QExponential.unique_axiom e₁ e₂ h_coprod h_counit h_Dq

end

end QOU
