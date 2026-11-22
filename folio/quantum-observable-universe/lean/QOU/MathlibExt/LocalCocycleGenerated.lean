import QOU.MathlibExt.LocalCocycleTransport
import Mathlib.CategoryTheory.Groupoid.Subgroupoid

/-!
# Conjugate monodromy from a generating set of arrows

Let `C₁, C₂` be local cocycles on `X` and `G : X → 𝒢` a candidate gauge.  An arrow
`p : x ⟶ y` of the fundamental groupoid is *compatible* if `T₁(p)⁻¹ · G x · T₂(p) = G y`.
Compatible arrows form a subgroupoid.  So if a set of compatible arrows generates a
subgroupoid containing every loop at `x₀`, the monodromies at `x₀` are conjugate by `G x₀`
(`LocalCocycle.conjMonodromy_of_generated`).

This is the form needed for a braid group: the generators are paths between *different*
base points (the half-turns of an ordered configuration), not loops.
-/

set_option autoImplicit false

namespace QOU.MathlibExt

open CategoryTheory

namespace LocalCocycle

variable {X : Type*} [TopologicalSpace X] {G : Type*} [Group G]

theorem transportQ_inv (C : LocalCocycle X G) {c d : FundamentalGroupoid X} (p : c ⟶ d) :
    C.transportQ (Groupoid.inv p) = (C.transportQ p)⁻¹ := by
  have h := congrArg C.transportQ (Groupoid.comp_inv p)
  rw [FundamentalGroupoid.comp_eq, FundamentalGroupoid.id_eq_path_refl] at h
  have h' : C.transportQ p * C.transportQ (Groupoid.inv p) = 1 := by
    rw [← C.transportQ_comp]
    exact h.trans (C.transport_refl _)
  exact eq_inv_of_mul_eq_one_right h'

variable (C₁ C₂ : LocalCocycle X G) (Gx : X → G)

/-- The subgroupoid of arrows along which `Gx` intertwines the two transports. -/
def compatible : Subgroupoid (FundamentalGroupoid X) where
  arrows c d := {p | (C₁.transportQ p)⁻¹ * Gx c.as * C₂.transportQ p = Gx d.as}
  inv := by
    intro c d p hp
    simp only [Set.mem_setOf_eq] at hp ⊢
    rw [C₁.transportQ_inv, C₂.transportQ_inv, ← hp]
    group
  mul := by
    intro c d e p hp q hq
    simp only [Set.mem_setOf_eq] at hp hq ⊢
    rw [FundamentalGroupoid.comp_eq, C₁.transportQ_comp, C₂.transportQ_comp, ← hq, ← hp]
    group

variable {C₁ C₂ Gx}

/-- **Conjugacy from generating arrows.** -/
theorem conjMonodromy_of_generated (x₀ : X)
    (S : ∀ c d : FundamentalGroupoid X, Set (c ⟶ d))
    (hS : ∀ c d, ∀ p ∈ S c d, (C₁.transportQ p)⁻¹ * Gx c.as * C₂.transportQ p = Gx d.as)
    (hgen : ∀ q : FundamentalGroupoid.mk x₀ ⟶ FundamentalGroupoid.mk x₀,
      q ∈ (Subgroupoid.generated S).arrows _ _) :
    ConjMonodromy C₁ C₂ x₀ (Gx x₀) := by
  intro l
  have hle := Subgroupoid.mem_sInf_arrows.mp (hgen ⟦l⟧) (compatible C₁ C₂ Gx)
    (fun c d p hp => hS c d p hp)
  exact hle

end LocalCocycle

end QOU.MathlibExt
