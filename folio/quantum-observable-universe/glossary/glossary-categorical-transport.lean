import Mathlib.Data.Real.Basic


/-!
# QOU.CategoricalTransport — Glossary: categorical transport equation

The transport equation D_∇ψ = 0 for sections of the jet bundle,
wrapping Mathlib's connection/covariant derivative concepts.

LaTeX label: `rem:glossary-categorical-transport`
-/

namespace QOU

/-- The categorical transport equation D_∇ψ = 0.

    In the QOU framework this is the q-deformed covariant derivative
    condition on sections ψ ∈ τ(J¹(A)). The q-correction comes from
    the categorical q-exterior derivative d_q acting on the jet bundle. -/
-- Ref: [leitner2026] Ch. 8 Glossary
structure CategoricalTransport (E : Type*) [AddCommGroup E] where
  /-- The q-deformed covariant derivative `D_∇`, acting on sections.

      Was `q_connection : Prop`, which is a typing error rather than a thin
      statement: a connection is DATA, and a field typed with the universe
      `Prop` holds a proposition. There was no proposition to hold. -/
  D : E → E
  /-- The section `ψ ∈ τ(J¹(A))`. -/
  psi : E
  /-- **The transport equation** `D_∇ψ = 0`.

      Was `transport_eq : Prop`, so the instance chose what the equation
      said and `True` discharged it. It is now the equation the docstring
      names. -/
  transport_eq : D psi = 0

end QOU
