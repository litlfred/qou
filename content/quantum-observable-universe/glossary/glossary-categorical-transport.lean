/-!
# QOU.CategoricalTransport — Glossary: categorical transport equation

The transport equation D_∇ψ = 0 for sections of the jet bundle,
wrapping Mathlib's connection/covariant derivative concepts.

LaTeX label: `rem:glossary-categorical-transport`
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- The categorical transport equation D_∇ψ = 0.

    In the QOU framework this is the q-deformed covariant derivative
    condition on sections ψ ∈ τ(J¹(A)). The q-correction comes from
    the categorical q-exterior derivative d_q acting on the jet bundle. -/
-- Ref: [manuscript] Ch. 8 Glossary
structure CategoricalTransport where
  /-- The q-deformed connection component. -/
  q_connection : Prop
  /-- The transport condition D_∇ψ = 0. -/
  transport_eq : Prop

end QOU
