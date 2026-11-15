import Mathlib.Tactic

/-!
# QOU.Su2Generators

**Canonical declaration** for content block at
[`quantum-observable-universe/brings-surface/su2-generators.ts`](quantum-observable-universe/brings-surface/su2-generators.ts).

Formalises the manuscript **definition** of the binary dihedral group
`Dic₃ ⊂ SU(2)` (order 12) — the `SU(2)`-lift of `S₃ ≅ D₃` — by its two
generators `α` (a lift of the 3-cycle) and `β` (a lift of a transposition),
with `α³ = β² = -I`, the dihedral relation `βαβ⁻¹ = α⁻¹`, and the derived
commutator `[β,α] = α⁻²`. Stated over an ambient group `G` with the central
element `z = -I` (pure group theory — §7c-clean, no archimedean structure).
-/

namespace QOU

/-- The binary dihedral group `Dic₃` presented inside an ambient group `G`.

    A `definition` carrier: generators `α, β`, the central element `z = -I`,
    and the defining relations `α³ = z`, `β² = z`, `z² = 1`, `z` central, and
    the dihedral relation `βαβ⁻¹ = α⁻¹`. -/
structure Su2Generators (G : Type*) [Group G] where
  /-- Lift of the 3-cycle. -/
  α : G
  /-- Lift of a transposition. -/
  β : G
  /-- The central element `-I`. -/
  z : G
  /-- `z` is central. -/
  z_central : ∀ g : G, z * g = g * z
  /-- `(-I)² = I`. -/
  z_sq : z ^ 2 = 1
  /-- `α³ = -I`. -/
  α_cubed : α ^ 3 = z
  /-- `β² = -I`. -/
  β_squared : β ^ 2 = z
  /-- Dihedral relation `βαβ⁻¹ = α⁻¹`. -/
  dihedral : β * α * β⁻¹ = α⁻¹

-- Ref: [leitner2026] quantum-observable-universe/brings-surface/su2-generators.ts

/-- The commutator relation `[β,α] = βαβ⁻¹α⁻¹ = α⁻²` follows from the
    dihedral relation (manuscript). -/
theorem commutator {G : Type*} [Group G] (S : Su2Generators G) :
    S.β * S.α * S.β⁻¹ * S.α⁻¹ = S.α⁻¹ * S.α⁻¹ := by
  rw [S.dihedral]

/-- `α` has order dividing 6: `α⁶ = 1` (since `α³ = z` and `z² = 1`). -/
theorem alpha_pow_six {G : Type*} [Group G] (S : Su2Generators G) :
    S.α ^ 6 = 1 := by
  have h : S.α ^ 6 = (S.α ^ 3) ^ 2 := by
    rw [show (6 : ℕ) = 3 * 2 from rfl, pow_mul]
  rw [h, S.α_cubed, S.z_sq]

end QOU
