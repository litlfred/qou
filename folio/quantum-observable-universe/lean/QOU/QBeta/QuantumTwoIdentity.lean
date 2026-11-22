import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# Quantum-2 algebraic identities

Proves the key identity connecting the quantum integer [2]_q to `q · ℏ_q²`:

    -(q + q⁻¹) = -2 - (q-1)²/q

i.e. `-[2]_q = -2 - q·ℏ_q²`.

**Corrected 2026-08-30 (bean `qou-6bla`): this file said `ℏ_q² = (q-1)²/q`,
and that is false.** `ℏ_q = 1 - q⁻¹`, so `ℏ_q² = (q-1)²/q²` — a factor of `q`
smaller. At `q₀ = 1.1099785827513808`, `(hbarQ q)^2 = 0.0098171865` against
`(q-1)²/q = 0.0108968667`, a ratio of 1.1100. The identity itself is correct
and untouched; only its reading was wrong.

**What this does NOT settle.** The old text went on to say the gap from the
classical value `-2` is "**exactly** ℏ_q² = the expansion parameter of the
precision ladder". The gap is `(q-1)²/q`, so it is `q·ℏ_q²`, not `ℏ_q²` —
but whether the ladder's parameter `u = b·ℏ_q² ≈ 0.00852` is the one or the
other cannot be read off here, since `b` is not fixed in this file. That is a
question for the `c_k` ladder owner (`qou-cds1`), not something this
correction resolves; the claim is withdrawn rather than replaced.

Sorry-free. The identity is pure algebra (field_simp; ring).

-- Ref: [leitner2026] docs/coordination/ck-dk-canonical-registry.md §3 (c₃ row)
-- Ref: QOU.QBeta.CuspWindingLattice (G(0,1) = -2 = classical limit of -[2]_q)
-/

namespace QOU.QBeta.QuantumTwoIdentity

variable {F : Type*} [Field F]

/-- Symmetric quantum integer [2]_q = q + q⁻¹. -/
noncomputable def quantumTwo (q : F) : F := q + q⁻¹

/-- `q · ℏ_q² = (q - 1)² / q`, the combination appearing in the `[2]_q`
identity below.

**This is NOT `ℏ_q²`, and the declaration used to be called `hbarSq` and
documented as such** (bean `qou-6bla`). `ℏ_q = 1 - q⁻¹`, so
`ℏ_q² = (q - 1)²/q²` — a factor of `q` smaller:

    (hbarQ q)^2  = 0.0098171865
    (q - 1)^2/q  = 0.0108968667      1.1100x larger

at `q₀ = 1.1099785827513808`. The theorem below is correct as stated and is
unchanged; only the name and the docstring's identification were wrong. -/
noncomputable def qHbarSq (q : F) : F := (q - 1) ^ 2 / q

/-- **KEY IDENTITY.** -(q + q⁻¹) = -2 - (q-1)²/q for any nonzero q.
    Equivalently: -[2]_q = -2 - q·ℏ_q², NOT -2 - ℏ_q² (see the module
    docstring: `ℏ_q² = (q-1)²/q²`, a factor of `q` smaller). -/
theorem neg_quantumTwo_eq (q : F) (hq : q ≠ 0) :
    -(q + q⁻¹) = -2 - (q - 1) ^ 2 / q := by
  field_simp
  ring

/-- Reformulation using the named definitions. -/
theorem neg_quantumTwo_eq' (q : F) (hq : q ≠ 0) :
    -quantumTwo q = -2 - qHbarSq q := by
  unfold quantumTwo qHbarSq
  exact neg_quantumTwo_eq q hq

/-- At q = 1, -[2]_q evaluates to -2.
    This is the classical limit, matching G(0,1) from CuspWindingLattice. -/
theorem neg_quantumTwo_at_one : -(1 : ℤ) - (1 : ℤ) = -2 := by norm_num

/-- The c₂·[2]_q recursion: if c₂ = -1, then c₂ · [2]_q = -[2]_q.
    (Trivial but records the structural claim.) -/
theorem c2_times_quantumTwo (q : F) : (-1 : F) * quantumTwo q = -quantumTwo q := by
  ring

end QOU.QBeta.QuantumTwoIdentity
