import Mathlib.Algebra.Group.Defs

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
-- Ref: [leitner2026] Ch. 8 Glossary
-- Ref: [baez1995] Baez, "Knots and quantum gravity: progress and prospects," J. Math. Phys. 36 (1995)
structure QuantumFlatness (Ω : Type*) [AddCommGroup Ω] where
  /-- The curvature `F_∇`. -/
  F : Ω
  /-- The 2-form datum `B ∈ Ω²(A) ⊗ Ad(A)`.

      Was `two_form_exists : Prop` — "the datum exists" as a proposition the
      instance chose. **Existence of data is expressed by having the field**,
      not by asserting it: a `QuantumFlatness` cannot be built without
      supplying a `B`, which is exactly what the old field was trying to say
      and could not. -/
  B : Ω
  /-- The exterior derivative on 2-forms. -/
  d : Ω → Ω
  /-- The bracket `[·,·]`. -/
  bracket : Ω → Ω → Ω
  /-- **Curvature absorbed by the 2-group**: `F_∇ = dB + [B,B]`.

      Was `curvature_absorbed : Prop`, so the instance chose the identity. -/
  curvature_absorbed : F = d B + bracket B B

end QOU
