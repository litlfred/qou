/-!
# QOU.QuantumFlatness — Glossary: quantum flatness

A connection ∇ is quantum flat when its curvature F_∇ lies in
the image of INN(G_q), so that the 2-group gauging absorbs the
curvature.

LaTeX label: `rem:glossary-quantum-flatness`
-/

namespace QOU

/-- Quantum flatness: the curvature F_∇ of the connection is
    absorbed by the inner-automorphism 2-group INN(G_q).

    Maps to Mathlib: related to `CategoryTheory.Monoidal.Transport`
    but requires 2-categorical infrastructure not yet available. -/
-- Ref: [manuscript] Ch. 8 Glossary
-- Ref: [baez1995] Baez, "Knots and quantum gravity: progress and prospects," J. Math. Phys. 36 (1995)
structure QuantumFlatness where
  /-- The 2-form datum B ∈ Ω²(A) ⊗ Ad(A) exists. -/
  two_form_exists : Prop
  /-- F_∇ = dB + [B,B] (curvature absorbed by 2-group). -/
  curvature_absorbed : Prop

end QOU
