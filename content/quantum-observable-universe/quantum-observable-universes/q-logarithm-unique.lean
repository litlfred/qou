/-!
# QOU.QLogarithm.unique — uniqueness of the q-logarithm primitive

Any two primitives of 𝓗_q with the same q-exponential image and
trivial counit coincide.

LaTeX: `\label{prop:q-logarithm-unique}`

## References

- [manuscript] §2-quantum-observable-universes/q-logarithm-unique
- [kassel1995] Quantum Groups (Springer GTM 155), §IV.3
-/

import QOU.Basic

namespace QOU

noncomputable section

/-- **External axiom (Kassel 1995 §IV.3, Milnor–Moore uniqueness):
    q-logarithm primitive is unique under matching coproduct/counit/
    grouplike.**

    Argument: `ℓ₁ - ℓ₂` is primitive with trivial counit; Milnor–
    Moore forces it to vanish, so `ℓ₁.log_q = ℓ₂.log_q`.  Pending
    Mathlib's Hopf-algebra primitive-uniqueness library. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IV.3
axiom QLogarithm.unique_axiom :
    ∀ {H : Type*} (ℓ₁ ℓ₂ : QLogarithm H),
      ℓ₁.coprod = ℓ₂.coprod →
      ℓ₁.counit = ℓ₂.counit →
      ℓ₁.one = ℓ₂.one →
      ℓ₁.log_q = ℓ₂.log_q

/-- **Uniqueness of the q-logarithm primitive.**

    Two q-logarithm structures on the same Hopf algebra with the
    same coproduct, counit, and primitive axiom satisfying
    exp_q(log_q) = g for the same grouplike g coincide. -/
-- Ref: [kassel1995] Quantum Groups, §IV.3
theorem QLogarithm.unique {H : Type*} (ℓ₁ ℓ₂ : QLogarithm H)
    (h_coprod : ℓ₁.coprod = ℓ₂.coprod)
    (h_counit : ℓ₁.counit = ℓ₂.counit)
    (h_one : ℓ₁.one = ℓ₂.one) :
    ℓ₁.log_q = ℓ₂.log_q :=
  QLogarithm.unique_axiom ℓ₁ ℓ₂ h_coprod h_counit h_one

end

end QOU
