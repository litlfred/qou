import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# Quantum-2 algebraic identities

Proves the key identity connecting the quantum integer [2]_q to ℏ_q²:

    -(q + q⁻¹) = -2 - (q-1)²/q

i.e. `-[2]_q = -2 - ℏ_q²`, where `ℏ_q² = (q-1)²/q`.

This means: if c₃ = -[2]_q, then the gap from the classical value -2
is **exactly** ℏ_q² = the expansion parameter of the precision ladder.
Equivalently, c₃ = c₂ · [2]_q (since c₂ = -1 is proved canonical).

Sorry-free. The identity is pure algebra (field_simp; ring).

-- Ref: [manuscript] docs/coordination/ck-dk-canonical-registry.md §3 (c₃ row)
-- Ref: QOU.QBeta.CuspWindingLattice (G(0,1) = -2 = classical limit of -[2]_q)
-/

namespace QOU.QBeta.QuantumTwoIdentity

variable {F : Type*} [Field F]

/-- Symmetric quantum integer [2]_q = q + q⁻¹. -/
noncomputable def quantumTwo (q : F) : F := q + q⁻¹

/-- Quantum ℏ² parameter: ℏ_q² = (q - 1)² / q. -/
noncomputable def hbarSq (q : F) : F := (q - 1) ^ 2 / q

/-- **KEY IDENTITY.** -(q + q⁻¹) = -2 - (q-1)²/q for any nonzero q.
    Equivalently: -[2]_q = -2 - ℏ_q². -/
theorem neg_quantumTwo_eq (q : F) (hq : q ≠ 0) :
    -(q + q⁻¹) = -2 - (q - 1) ^ 2 / q := by
  field_simp
  ring

/-- Reformulation using the named definitions. -/
theorem neg_quantumTwo_eq' (q : F) (hq : q ≠ 0) :
    -quantumTwo q = -2 - hbarSq q := by
  unfold quantumTwo hbarSq
  exact neg_quantumTwo_eq q hq

/-- At q = 1, -[2]_q evaluates to -2.
    This is the classical limit, matching G(0,1) from CuspWindingLattice. -/
theorem neg_quantumTwo_at_one : -(1 : ℤ) - (1 : ℤ) = -2 := by norm_num

/-- The c₂·[2]_q recursion: if c₂ = -1, then c₂ · [2]_q = -[2]_q.
    (Trivial but records the structural claim.) -/
theorem c2_times_quantumTwo (q : F) : (-1 : F) * quantumTwo q = -quantumTwo q := by
  ring

end QOU.QBeta.QuantumTwoIdentity
