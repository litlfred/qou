import Mathlib.Logic.Basic


/-!
# QOU.QuantumObservableUniverse.IsQuantumFlat — quantum flatness F_∇ = B

Atomic definition of the quantum flatness condition: a 2-connection `(A, B)` on
the inner-automorphism 2-group `INN(G_q)` is *quantum flat* when the curvature
`F_∇` of the ordinary connection `∇` equals the 2-form datum `B`.

This is the condition named at the define-site `#quantum-flatness`; that it is a
*derived* consequence of the instanton condition + the simplicity constraint
(rather than an independent axiom) is the content of
`prop:emergence-to-quantum-flat`.

LaTeX label: `def:quantum-flatness`

## References
- [leitner2026] Ch. 2, §elaboration (2-group gauge theory)
-/

namespace QOU.QuantumObservableUniverse

/-- **Quantum flatness**: a 2-connection `(A, B)` is *quantum flat* when the
    curvature `F_∇` of the ordinary connection equals the 2-form datum `B`,
    i.e. `F_∇ = B`.  Stated as a predicate on the curvature and the 2-form
    datum, valued in an arbitrary type `V` of `Ad`-valued 2-forms. -/
def IsQuantumFlat {V : Type*} (curvature twoFormDatum : V) : Prop :=
  curvature = twoFormDatum

end QOU.QuantumObservableUniverse
