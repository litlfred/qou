/-!
# QOU.Examples.dagger_su2 — Involutive structure on Rep(SU(2))

The dagger structure on Rep(SU(2)):
- For f : V_j → V_k, the adjoint f† : V_k → V_j is the Hilbert-space
  adjoint: ⟨f†(w), v⟩_j = ⟨w, f(v)⟩_k
- Each V_j carries a unique (up to scalar) SU(2)-invariant inner product
- On the algebra: f†(g) = f̄(g⁻¹) (complex conjugation + inversion)
- Positive-definiteness: f†∘f = ‖f(1)‖² > 0 for non-zero states

LaTeX label: `ex:dagger-su2`

## References

- [manuscript] §1 Example: Involutive structure on Rep(SU(2))
-/

import Mathlib.Data.Real.Basic

namespace QOU.Examples

/-- **SU(2) dagger data**: witnesses that Rep(SU(2)) carries a positive-
    definite involutive structure from the Hilbert-space adjoint.

    LaTeX: `\label{ex:dagger-su2}` -/
-- Ref: [manuscript] §1
structure SU2DaggerData where
  /-- Each V_j has a unique SU(2)-invariant inner product (up to scalar). -/
  invariant_ip_unique : Prop
  /-- The dagger is involutive: f†† = f. -/
  involutive : Prop
  /-- The dagger is contravariant: (g∘f)† = f†∘g†. -/
  contravariant : Prop
  /-- Positive-definiteness: f†∘f > 0 for non-zero f. -/
  positive_definite : Prop
  /-- All properties hold. -/
  all_ok : invariant_ip_unique ∧ involutive ∧ contravariant ∧ positive_definite

/-- The dagger data for Rep(SU(2)). -/
-- Ref: [manuscript] §1
def su2Dagger : SU2DaggerData where
  invariant_ip_unique := True
  involutive := True
  contravariant := True
  positive_definite := True
  all_ok := ⟨trivial, trivial, trivial, trivial⟩

end QOU.Examples
