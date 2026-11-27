import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Fintype.Card
import Mathlib.GroupTheory.Perm.Basic


/-!
# QOU.S3Group — Glossary: symmetric group S₃

S₃ = B₃ / ⟨σᵢ² = id⟩, the quotient of the braid group by
the involution relations.

LaTeX label: `rem:glossary-s3-group`
-/

namespace QOU

/-- The symmetric group S₃ as the quotient B₃/⟨σᵢ²=id⟩.

    Maps to Mathlib: `Equiv.Perm (Fin 3)`. -/
-- Ref: [leitner2026] Ch. 8 Glossary
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
abbrev S3Group := Equiv.Perm (Fin 3)

/-- S₃ has order 6. -/
-- Ref: [leitner2026] Ch. 8 Glossary
theorem s3_card : Fintype.card S3Group = 6 := by
  simp [S3Group]
  decide

end QOU
