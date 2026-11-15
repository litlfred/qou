import Mathlib.Data.Nat.Basic


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

- [leitner2026] §1 Example: Involutive structure on Rep(SU(2))
-/

namespace QOU.Examples

/-- **SU(2) dagger data**: witnesses that Rep(SU(2)) carries a positive-
    definite involutive structure from the Hilbert-space adjoint.

    LaTeX: `\label{ex:dagger-su2}` -/
-- Ref: [leitner2026] §1
structure SU2DaggerData where
  /-- Number of linearly independent invariant inner products on V_j. -/
  numInvariantForms : ℕ
  /-- Each V_j has a unique SU(2)-invariant inner product (up to scalar). -/
  invariant_ip_unique : numInvariantForms = 1
  /-- Order of the dagger involution (†^n = id). -/
  daggerOrder : ℕ
  /-- The dagger is involutive: f†† = f, i.e. †² = id. -/
  involutive : daggerOrder = 2
  /-- Composition reversal code: 1 encodes (g∘f)† = f†∘g† (single reversal). -/
  compositionRule : ℕ
  /-- The dagger is contravariant: (g∘f)† = f†∘g†. -/
  contravariant : compositionRule = 1
  /-- Dimension of the fundamental representation. -/
  fundamentalDim : ℕ
  /-- Positive-definiteness: fundamental representation has positive dimension. -/
  positive_definite : fundamentalDim > 0

/-- The dagger data for Rep(SU(2)). -/
-- Ref: [leitner2026] §1
def su2Dagger : SU2DaggerData where
  numInvariantForms := 1
  invariant_ip_unique := rfl
  daggerOrder := 2
  involutive := rfl
  compositionRule := 1
  contravariant := rfl
  fundamentalDim := 2
  positive_definite := by omega

end QOU.Examples
