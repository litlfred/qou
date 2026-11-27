import Mathlib.Algebra.Group.Hom.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic

/-!
# The proposed `TetraplecticDilogBridge` conjecture is vacuous as stated

An external discussion (owner upload, 2026-11-27; see
`docs/audits/2026-11-27-dilog-bloch-pre-archimedean.md`) proposed a Lean statement
for an "algebraic–geometric dilogarithm equivalence via tetraplectic Bruhat
reduction": a structure `TetraplecticDilogBridge B S H` whose fields
(`algBruhatVolume`, `tetraShapes`, `dilogEval`, `archimedeanRegulator`,
`hypVolume`, `figureEightBraid`, `figureEight_pos`) are all **free**, and a
`Prop` asserting, for every braid in an admissible class, that the algebraic
volume is the sum of `dilogEval` over the shapes and that its regulator is the
hyperbolic volume.

This file reproduces that statement and proves it is **inhabited for every
admissible class with a witness**, by a bridge built to satisfy it
(`exists_bridge`). The guard `figureEight_pos` does not prevent this. So the
`Prop` carries no content until its fields are *defined* from QOU objects
(the Hecke algebra `H_n(q)`, the corpus's `Li₂^q`, an actual Bloch group, and the
hyperbolic volume) rather than supplied by the caller. It is recorded so that
the statement is not added to the corpus in this form.

Nothing here is a claim about knots; it is a claim about the logical form of
the proposed statement.
-/

namespace QOU.Archimedean.TetraplecticDilogBridgeVacuity

/-- The proposed bridge, field for field. -/
structure TetraplecticDilogBridge (B S H : Type*) [AddCommGroup H] where
  algBruhatVolume : B → H
  tetraShapes : B → List S
  dilogEval : S → H
  archimedeanRegulator : H →+ ℝ
  hypVolume : B → ℝ
  figureEightBraid : B
  figureEight_pos : 0 < hypVolume figureEightBraid

/-- The proposed conjecture. -/
def ConjAlgebraicGeometricDilogEquiv {B S H : Type*} [AddCommGroup H]
    (bridge : TetraplecticDilogBridge B S H) (IsHyperbolic : B → Prop) : Prop :=
  IsHyperbolic bridge.figureEightBraid ∧
    ∀ β, IsHyperbolic β →
      bridge.algBruhatVolume β = ((bridge.tetraShapes β).map bridge.dilogEval).sum ∧
        bridge.archimedeanRegulator (bridge.algBruhatVolume β) = bridge.hypVolume β

/-- **Vacuity.** For any braid type `B`, any inhabited shape type `S`, and any
admissible class with at least one member, some bridge satisfies the conjecture. -/
theorem exists_bridge {B S : Type*} (s₀ : S) (IsHyperbolic : B → Prop) (b₀ : B)
    (hb₀ : IsHyperbolic b₀) :
    ∃ bridge : TetraplecticDilogBridge B S ℝ,
      ConjAlgebraicGeometricDilogEquiv bridge IsHyperbolic :=
  ⟨{ algBruhatVolume := fun _ => 1
     tetraShapes := fun _ => [s₀]
     dilogEval := fun _ => 1
     archimedeanRegulator := AddMonoidHom.id ℝ
     hypVolume := fun _ => 1
     figureEightBraid := b₀
     figureEight_pos := one_pos },
   hb₀, fun _ _ => ⟨by simp, rfl⟩⟩

/-- **Fixing the volume does not help.** Even with `hypVolume` pinned to a
prescribed function `V` (for instance the true hyperbolic volume), a bridge with
real shapes satisfies the conjecture, by reading the shape list off `V`. Content
requires `tetraShapes`, `dilogEval` and `algBruhatVolume` to be defined, not chosen. -/
theorem exists_bridge_with_volume {B : Type*} (V : B → ℝ) (IsHyperbolic : B → Prop) (b₀ : B)
    (hb₀ : IsHyperbolic b₀) (hV : 0 < V b₀) :
    ∃ bridge : TetraplecticDilogBridge B ℝ ℝ,
      bridge.hypVolume = V ∧ ConjAlgebraicGeometricDilogEquiv bridge IsHyperbolic :=
  ⟨{ algBruhatVolume := V
     tetraShapes := fun β => [V β]
     dilogEval := id
     archimedeanRegulator := AddMonoidHom.id ℝ
     hypVolume := V
     figureEightBraid := b₀
     figureEight_pos := hV },
   rfl, hb₀, fun _ _ => ⟨by simp, rfl⟩⟩

end QOU.Archimedean.TetraplecticDilogBridgeVacuity
