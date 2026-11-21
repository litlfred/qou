import Mathlib.CategoryTheory.Groupoid
import Mathlib.CategoryTheory.Endomorphism
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Group.Submonoid.Basic

/-!
# Gauge action groupoid

The gauge symmetry of a framework built on extended (knotted) objects
is not a Lie group acting on points but a *groupoid* of reversible
topological deformations acting on states. This file formalises the
minimal structure carrying that idea: a groupoid of topological
states equipped with an additive action functional on morphisms.

* Objects — topological states (knot / braid configurations).
* Morphisms — gauge transformations: reversible deformations,
  braiding operations, cobordism moves.
* `act` — the action cost of executing a gauge transformation,
  additive under composition and vanishing on identities.

Everything here is proved, generic over an additive commutative
group of action values (AGENTS.md §7c: no archimedean
specialisation). The *physical* claims — that the QOU knot-state
groupoid realises inside the Hecke algebra, and that its archimedean
truncation contains the Standard Model gauge group — are stated
separately as conjecture classes in `gauge-hecke-realization.lean`
and `sm-gauge-truncation.lean`; nothing in this file depends on
them.

## References

- [leitner2026] Appendix: Toward the Standard Model
- [baez2004] Baez–Lauda, Higher-dimensional algebra V: 2-groups
-/

namespace QOU.StandardModel

open CategoryTheory

universe u v

/-- A **gauge action groupoid** over an additive commutative group
`R` of action values: a groupoid of topological states whose
morphisms (gauge transformations) carry an action functional `act`
that vanishes on identities and is additive under composition.
Reversibility of gauge transformations is exactly the groupoid
axiom. -/
structure GaugeActionGroupoid (R : Type*) [AddCommGroup R] where
  /-- The topological states (objects: knot / braid configurations). -/
  states : Type u
  /-- Gauge transformations form a groupoid: every deformation is reversible. -/
  [grpd : Groupoid.{v} states]
  /-- The action cost of a gauge transformation. -/
  act : ∀ {X Y : states}, (X ⟶ Y) → R
  /-- Doing nothing costs nothing. -/
  act_id : ∀ X : states, act (𝟙 X) = 0
  /-- The action is additive under composition of deformations. -/
  act_comp : ∀ {X Y Z : states} (f : X ⟶ Y) (g : Y ⟶ Z),
    act (f ≫ g) = act f + act g

attribute [instance] GaugeActionGroupoid.grpd

namespace GaugeActionGroupoid

variable {R : Type*} [AddCommGroup R] (G : GaugeActionGroupoid R)

/-- Undoing a gauge transformation refunds its action: a closed
gauge loop `f ≫ f⁻¹` costs zero, so `act f⁻¹ = -act f`. -/
theorem act_inv {X Y : G.states} (f : X ⟶ Y) :
    G.act (Groupoid.inv f) = -G.act f := by
  have h : G.act (f ≫ Groupoid.inv f) = G.act f + G.act (Groupoid.inv f) :=
    G.act_comp f (Groupoid.inv f)
  rw [Groupoid.comp_inv, G.act_id] at h
  exact eq_neg_of_add_eq_zero_right h.symm

/-- **Gauge equivalence**: two states are gauge equivalent when some
gauge transformation connects them. -/
def GaugeEquiv (X Y : G.states) : Prop := Nonempty (X ⟶ Y)

/-- Gauge equivalence is an equivalence relation — reflexive via the
identity, symmetric via groupoid inversion, transitive via
composition. -/
theorem gaugeEquiv_equivalence : Equivalence G.GaugeEquiv where
  refl X := ⟨𝟙 X⟩
  symm := fun ⟨f⟩ => ⟨Groupoid.inv f⟩
  trans := fun ⟨f⟩ ⟨g⟩ => ⟨f ≫ g⟩

/-- The automorphisms of a fixed state with zero action form a
submonoid of `End X`: the **residual (unbroken) symmetries** of that
state. Closure is additivity of the action; the identity is free. -/
def zeroActionEnd (X : G.states) : Submonoid (End X) where
  carrier := { f | G.act f = 0 }
  one_mem' := G.act_id X
  mul_mem' := by
    intro f g hf hg
    show G.act (g ≫ f) = 0
    rw [G.act_comp, hg, hf, add_zero]

end GaugeActionGroupoid

end QOU.StandardModel
