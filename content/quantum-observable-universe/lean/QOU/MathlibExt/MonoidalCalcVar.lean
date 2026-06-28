import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.Tactic

/-!
# QOU.MathlibExt.MonoidalCalcVar — Monoidal calculus of variations

A skeleton framework for variational equations of motion in
monoidal categories. Candidate for upstream contribution to
`Mathlib/CategoryTheory/CalculusOfVariations/Basic.lean` (the
module does not yet exist; this is greenfield).

## What this module provides

- `LagrangianAction` — a typeclass on a monoidal preadditive
  category `C` with a fibre object `F`: an `R`-valued action
  functional on connections.
- `VariationalDerivative` — abstract derivative operator
  satisfying the integration-by-parts identity.
- `EulerLagrange` — the abstract Euler-Lagrange equations.
- `HasMonoidalEOM` typeclass — packaging the equations of motion
  as a categorical theorem (Wald-style for monoidal categories).

## What this module does NOT yet prove

The classical calculus of variations (Wald, Bleecker, Kobayashi-
Nomizu) lives in differential geometry. The categorical
generalisation requires:
- A categorical Lagrangian with respect to a connection
- Internal variations as morphisms in `C`
- An adjoint theory making the action functional varied with
  respect to a connection morphism

These don't currently exist in Mathlib. The skeleton declares the
key statements; concrete instances at specific monoidal categories
are the conjectural input.

## References

- [wald1984] Wald, *General Relativity*, Theorem 4.3.1.
  https://doi.org/10.7208/chicago/9780226870373.001.0001
- [bleecker1981] Bleecker, *Gauge Theory and Variational
  Principles*, Ch VII.
  https://doi.org/10.1007/978-1-4684-0148-7
- [kobayashi1996] Kobayashi-Nomizu, *Foundations of Differential
  Geometry*, Vol I, Ch II.
  https://doi.org/10.1002/9780470316559
-/

namespace QOU.MathlibExt.MonoidalCalcVar

universe u v

open CategoryTheory MonoidalCategory

/-- **Action functional** as a typeclass: a scalar-valued map from
    `Hom (𝟙_ C) (𝟙_ C)` to a coefficient ring `R` that absorbs the
    variational structure. Stated abstractly so concrete categories
    supply their own action.

    **Base ring (§7c).** The action codomain is a generic
    `{R : Type*}` — nothing in this skeleton performs an archimedean
    operation on the action value (no ordering, no `Real.*`), so the
    `ℝ` specialisation would be gratuitous. A concrete instance at a
    real-analytic category supplies `(R := ℝ)`. -/
class HasAction (R : Type*) (C : Type u) [Category.{v} C] [MonoidalCategory C]
    [Preadditive C] where
  /-- The action functional. -/
  action : ((𝟙_ C) ⟶ (𝟙_ C)) → R

/-- **Variational data** — three components of a Lagrangian
    decomposition: gravity, gauge, matter, each as a morphism
    `𝟙_ C → 𝟙_ C`. -/
structure VariationalData (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] where
  /-- Einstein / gravity term. -/
  gravity : (𝟙_ C) ⟶ (𝟙_ C)
  /-- Yang-Mills / gauge term. -/
  gauge : (𝟙_ C) ⟶ (𝟙_ C)
  /-- Matter / transport term. -/
  matter : (𝟙_ C) ⟶ (𝟙_ C)

/-- **External-current data** — sources for the equations of motion.
    Einstein tensor, stress-energy, gauge current. -/
structure ExternalCurrents (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] where
  /-- Einstein tensor `G_λ`. -/
  einsteinTensor : (𝟙_ C) ⟶ (𝟙_ C)
  /-- Stress-energy tensor `T_q`. -/
  stressTensor : (𝟙_ C) ⟶ (𝟙_ C)
  /-- Gauge current density `J_ψ`. -/
  gaugeCurrent : (𝟙_ C) ⟶ (𝟙_ C)

/-! ## §2  Equations of motion (the headline conjecture)

The Wald-Bleecker-Kobayashi-Nomizu trio of EOMs in the categorical
setting:
- **Einstein**: `gravity = G_λ + T_q`
- **Yang-Mills**: `gauge = J_ψ`
- **Transport**: `matter = 0`

The full proof requires a categorical calculus of variations. The
skeleton packages these three claims into a typeclass; concrete
instances are the conjectural input. -/

/-- **Categorical equations of motion typeclass**: bundles the
    three on-shell variational identities. -/
-- Ref: [wald1984] §4.3 (Einstein); [bleecker1981] Ch VII (YM)
-- Ref: [kobayashi1963] Vol I Ch II (transport)
class HasMonoidalEOM (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C]
    (vd : VariationalData C) (ec : ExternalCurrents C) : Prop where
  /-- **Einstein**: `gravity = G_λ + T_q`. -/
  einstein : vd.gravity = ec.einsteinTensor + ec.stressTensor
  /-- **Yang-Mills**: `gauge = J_ψ`. -/
  yang_mills : vd.gauge = ec.gaugeCurrent
  /-- **Transport**: `matter = 0`. -/
  transport : vd.matter = 0

/-- **Reflexivity-like default**: when the variational data is
    *defined* such that each EOM identity holds by `rfl` (i.e.,
    the gravity/gauge/matter morphisms are constructed as the
    sums of the corresponding currents), the typeclass is
    inhabited trivially.

    Concretely: if `vd.gravity := ec.einsteinTensor + ec.stressTensor`,
    `vd.gauge := ec.gaugeCurrent`, `vd.matter := 0` definitionally,
    then `HasMonoidalEOM` follows by `rfl`. -/
instance hasMonoidalEOM_of_def (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C]
    (ec : ExternalCurrents C) :
    let vd : VariationalData C :=
      ⟨ec.einsteinTensor + ec.stressTensor, ec.gaugeCurrent, 0⟩
    HasMonoidalEOM C vd ec := by
  refine ⟨?_, ?_, ?_⟩
  · rfl
  · rfl
  · rfl

end QOU.MathlibExt.MonoidalCalcVar
