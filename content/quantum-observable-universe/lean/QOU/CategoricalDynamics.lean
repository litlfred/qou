/-
  Categorical Dynamics at the Planck Length
  Formalizing points as morphisms from the terminal object,
  and time evolution as a functorial operation.
-/
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.Limits.Shapes.Terminal

open CategoryTheory Limits

universe v u

namespace QOU.CategoricalDynamics

variable {C : Type u} [Category.{v} C] [HasTerminal C]

/-- The observable universe as an object in our abstract category. -/
variable (M : C)

/-- A Point is a morphism from the terminal object (pt) to M.
    Categorically, we avoid geometric coordinates. -/
def PointMorphism := ⊤_ C ⟶ M

/-- Discrete time step evolution as an endomorphism of the universe object M. -/
variable (TimeStep : M ⟶ M)

/-- A 'flowed' point is the composition of the original point morphism with the time step. -/
def flowPoint (p : PointMorphism M) : PointMorphism M :=
  p ≫ TimeStep

/-- A Particle is conceptually a section over points. 
    Given a bundle projection π : E ⟶ M, a section is a morphism s : M ⟶ E 
    such that s ≫ π = 𝟙 M. Over a specific point p, the particle has a state p ≫ s. -/
structure ParticleSection (E : C) (π : E ⟶ M) where
  section_map : M ⟶ E
  is_section : section_map ≫ π = 𝟙 M

/-- The state of a particle at a given point. -/
def particleStateAt {E : C} {π : E ⟶ M} (part : ParticleSection M E π) (p : PointMorphism M) : ⊤_ C ⟶ E :=
  p ≫ part.section_map

/-- Evolution of a point via a global endofunctor (if time acts on the whole category). -/
variable (TimeFunctor : C ⥤ C)
variable (term_iso : ⊤_ C ≅ TimeFunctor.obj (⊤_ C))

/-- The functorial flow of a point morphism under the TimeFunctor. -/
def functorialFlowPoint (p : PointMorphism M) : PointMorphism (TimeFunctor.obj M) :=
  term_iso.hom ≫ TimeFunctor.map p

end QOU.CategoricalDynamics
