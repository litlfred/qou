import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.Tactic.Abel

/-!
# QOU.MathlibExt.MonoidalCalcVar — Monoidal calculus of variations

A skeleton framework for variational equations of motion in
monoidal categories. Candidate for upstream contribution to
`Mathlib/CategoryTheory/CalculusOfVariations/Basic.lean` (the
module does not yet exist; this is greenfield).

## What this module provides

- `PairingSpace C X Y` — the **field space** `X ⊗ Y ⟶ 𝟙_ C`: the pairings on
  an ordered pair of objects.  Two tensor slots, so a member of it is a rank-2
  object, and that is a fact about its *type*, not a claim about its name.
- `HasAction` — a typeclass on a monoidal preadditive category `C` with a pair
  of objects `X Y`: an `R`-valued action functional **on the field space**.
- `contract η` — the additive trace `PairingSpace C X Y →+ End(𝟙_C)` against a
  co-pairing `η : 𝟙_ C ⟶ X ⊗ Y`.  This is the map that recovers the scalar.
- `VariationalData` / `ExternalCurrents` — the Lagrangian decomposition and its
  sources, with the **Einstein/stress/gravity triple rank-2** and the
  gauge/matter pair left scalar (see "What is and is not retyped" below).
- `HasMonoidalEOM` typeclass — packaging the equations of motion.
- `einstein_contracted` / `einstein_contracted_comp` — **the bridge**: the old
  scalar Einstein equation is the contraction of the rank-2 one.
- `subsingleton_of_contract_reflects` — and the converse fails.

## Retyped 2026-09-15 (owner-authorised; bean `qou-h0ou`)

This module previously declared

```
class HasAction (R : Type*) (C : Type u) … where
  action : ((𝟙_ C) ⟶ (𝟙_ C)) → R
```

whose domain is `End(𝟙_C)` — the **scalars**.  A variational derivative is an
object on the *field space*, the thing being varied; an action whose field
space is the scalars has a scalar derivative, and nothing in the type mentioned
the objects being paired.  Downstream, `ExternalCurrents.einsteinTensor` was
typed `(𝟙_ C) ⟶ (𝟙_ C)`: a scalar wearing a tensor's name.  Einstein's
equation is a rank-2 identity and a scalar cannot state one.

The domain is now `PairingSpace C X Y`.  The rank-2-ness is carried by *what is
varied*, never by what the action's values are — see
`QOU.Variational.QuadraticAction.ofFunctional_variation`
(`QOU/FrobeniusHopfData/PairingVariationalDerivative.lean`), where an action
built entirely out of a scalar reading still has a bilinear derivative.

### What is and is not retyped

`gravity`, `einsteinTensor` and `stressTensor` are rank-2.  `gauge`,
`gaugeCurrent` and `matter` are **unchanged** and remain scalars.  That split
is not a physical claim about which currents "are" tensors — it is forced by
the equation `gravity = einsteinTensor + stressTensor`, whose three terms must
inhabit one additive group.  The Yang-Mills and transport equations relate
different objects and are left exactly as they were, so the diff shows only
what the Einstein identity requires.

### The bridge, and why this is a refactor rather than a replacement

`contract η T = η ≫ T` composes a rank-2 field with a co-pairing
`η : 𝟙_ C ⟶ X ⊗ Y` and lands in `End(𝟙_C)` — the slot the module used to
store.  `einstein_contracted` derives the old scalar equation from the new
rank-2 one, so nothing that was previously statable has been lost.

`subsingleton_of_contract_reflects` is the other half: if equality of
contractions implied equality of the rank-2 fields, uniformly in the
co-pairing, the field space would have at most one element.  The invariant is
`zero_comp` — the degenerate co-pairing `η = 0` contracts every field to the
same scalar.  So the scalar form is **strictly weaker** in any `Preadditive`
monoidal category with two distinct pairings, and the retype is a strengthening
rather than a rename.

### What the retype does NOT fix

`hasMonoidalEOM_of_def` still proves all three equations by `rfl`, because it
*defines* `vd` as `⟨ec.einsteinTensor + ec.stressTensor, ec.gaugeCurrent, 0⟩`.
Retyping does not touch that: the tautology is orthogonal to rank, and an
honest report of this change has to say so rather than imply the `rfl` was the
defect being removed.  `einstein_split_iff` states the residual problem
exactly — the Einstein identity says only that the stress term *is* the
residual `gravity − einsteinTensor`, and places no condition whatever on
`einsteinTensor`.  That is AGENTS.md §"Defined residual ≠ derived
decomposition" in Lean, and it remains open.

### What is NOT claimed

No gravitational content: no metric, no curvature, no stress-energy realisation,
no Newton constant, no `8π`, no numerical constant of any kind.  This module is
about which *types* the equations of motion can be stated in.  `HasMonoidalEOM`
remains a typeclass — the equations are assumed at every use site, not derived,
and retyping them does not make them proved.

## What this module does NOT yet prove

The classical calculus of variations (Wald, Bleecker, Kobayashi-
Nomizu) lives in differential geometry. The categorical
generalisation requires:
- A categorical Lagrangian with respect to a connection
- Internal variations as morphisms in `C`
- An adjoint theory making the action functional varied with
  respect to a connection morphism

The **quadratic** case is an exception and is now available: for a quadratic
action the Gateaux derivative is algebraic, no limit is needed, and
`QOU.Variational.QuadraticAction` supplies it sorry-free.  Everything beyond
quadratic remains open.

## Base ring (§7c)

Generic `{R : Type*}` throughout — nothing here performs an archimedean
operation on the action value (no ordering, no `Real.*`, no numeric literal).
A concrete instance at a real-analytic category supplies `(R := ℝ)`.

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

/-! ## §0  The field space -/

/-- **The field space**: the pairings `X ⊗ Y ⟶ 𝟙_ C` on an ordered pair of
    objects.  A member has two tensor slots, so it is a rank-2 object by its
    type rather than by its name — which is the whole difference between this
    and `End(𝟙_C)`. -/
abbrev PairingSpace (C : Type u) [Category.{v} C] [MonoidalCategory C]
    (X Y : C) : Type v := X ⊗ Y ⟶ 𝟙_ C

section Contraction

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]

/-- **Contraction** of a rank-2 field against a co-pairing
    `η : 𝟙_ C ⟶ X ⊗ Y`, landing in the scalars `End(𝟙_C)` — the slot this
    module used to store directly.  Additivity is the content: `map_zero'` and
    `map_add'` are what make this a trace rather than an arbitrary function,
    and they are what lets `einstein_contracted` push a sum through. -/
def contract {X Y : C} (η : (𝟙_ C) ⟶ X ⊗ Y) :
    PairingSpace C X Y →+ ((𝟙_ C) ⟶ (𝟙_ C)) where
  toFun T := η ≫ T
  map_zero' := by simp
  map_add' := by intro T T'; simp

/-- Definitional unfolding, recorded for `simp`.  Not a mathematical claim. -/
@[simp] lemma contract_apply {X Y : C} (η : (𝟙_ C) ⟶ X ⊗ Y)
    (T : PairingSpace C X Y) : contract η T = η ≫ T := rfl

end Contraction

/-! ## §1  The action functional -/

/-- **Action functional** as a typeclass: a scalar-valued map from the **field
    space** `PairingSpace C X Y` to a coefficient ring `R`.  Stated abstractly
    so concrete categories supply their own action.

    The domain is the pairings, not `End(𝟙_C)`: an action must be a functional
    on the thing that is varied, or it has no variational derivative worth the
    name.  See the module docstring.

    **Base ring (§7c).** The action codomain is a generic
    `{R : Type*}` — nothing in this skeleton performs an archimedean
    operation on the action value (no ordering, no `Real.*`), so the
    `ℝ` specialisation would be gratuitous. A concrete instance at a
    real-analytic category supplies `(R := ℝ)`. -/
class HasAction (R : Type*) (C : Type u) [Category.{v} C] [MonoidalCategory C]
    [Preadditive C] (X Y : C) where
  /-- The action functional, on the field space. -/
  action : PairingSpace C X Y → R

/-- **Existence constructor.**  Contract a rank-2 field against a co-pairing
    `η`, then read the resulting scalar with `ε`.

    This is what the previous typing could not support.  With domain
    `End(𝟙_C)` the class was declared and never inhabited anywhere in the
    corpus, and an instance would have had nothing to vary; here the same
    scalar ingredients give an action **on the pairings**, whose variational
    derivative is a bilinear form
    (`QOU.Variational.QuadraticAction.ofFunctional_variation`). -/
def HasAction.ofContraction {R : Type*} {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] {X Y : C} (η : (𝟙_ C) ⟶ X ⊗ Y)
    (ε : ((𝟙_ C) ⟶ (𝟙_ C)) → R) : HasAction R C X Y where
  action T := ε (contract η T)

/-- Definitional unfolding of the existence constructor. -/
@[simp] lemma HasAction.ofContraction_action {R : Type*} {C : Type u}
    [Category.{v} C] [MonoidalCategory C] [Preadditive C] {X Y : C}
    (η : (𝟙_ C) ⟶ X ⊗ Y) (ε : ((𝟙_ C) ⟶ (𝟙_ C)) → R) (T : PairingSpace C X Y) :
    (HasAction.ofContraction η ε).action T = ε (η ≫ T) := rfl

/-! ## §2  Variational data -/

/-- **Variational data** — three components of a Lagrangian
    decomposition: gravity, gauge, matter.

    `gravity` is rank-2 (a pairing); `gauge` and `matter` are scalars, exactly
    as before.  Only `gravity` moved, because only it is summed against the
    Einstein and stress terms. -/
structure VariationalData (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] (X Y : C) where
  /-- Einstein / gravity term — **rank-2**. -/
  gravity : PairingSpace C X Y
  /-- Yang-Mills / gauge term. -/
  gauge : (𝟙_ C) ⟶ (𝟙_ C)
  /-- Matter / transport term. -/
  matter : (𝟙_ C) ⟶ (𝟙_ C)

/-- **External-current data** — sources for the equations of motion.
    Einstein tensor, stress-energy, gauge current.

    The Einstein and stress terms are **rank-2**; the gauge current is a scalar,
    unchanged. -/
structure ExternalCurrents (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] (X Y : C) where
  /-- Einstein tensor `G_λ` — **rank-2**. -/
  einsteinTensor : PairingSpace C X Y
  /-- Stress-energy tensor `T_q` — **rank-2**. -/
  stressTensor : PairingSpace C X Y
  /-- Gauge current density `J_ψ`. -/
  gaugeCurrent : (𝟙_ C) ⟶ (𝟙_ C)

/-! ## §3  Equations of motion (the headline conjecture)

The Wald-Bleecker-Kobayashi-Nomizu trio of EOMs in the categorical
setting:
- **Einstein**: `gravity = G_λ + T_q` — now an identity between **pairings**
- **Yang-Mills**: `gauge = J_ψ`
- **Transport**: `matter = 0`

The full proof requires a categorical calculus of variations. The
skeleton packages these three claims into a typeclass; concrete
instances are the conjectural input. -/

/-- **Categorical equations of motion typeclass**: bundles the
    three on-shell variational identities.  The Einstein field is now stated
    where a rank-2 identity can live. -/
-- Ref: [wald1984] §4.3 (Einstein); [bleecker1981] Ch VII (YM)
-- Ref: [kobayashi1963] Vol I Ch II (transport)
class HasMonoidalEOM (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] {X Y : C}
    (vd : VariationalData C X Y) (ec : ExternalCurrents C X Y) : Prop where
  /-- **Einstein**: `gravity = G_λ + T_q`, as pairings. -/
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
    then `HasMonoidalEOM` follows by `rfl`.

    **This survived the 2026-09-15 retype unchanged, and that is the honest
    report**: rank and tautology are independent defects.  A `HasMonoidalEOM`
    obtained this way carries no information about `ec` — see
    `einstein_split_iff` for the exact statement of what the identity does and
    does not constrain. -/
instance hasMonoidalEOM_of_def (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] {X Y : C}
    (ec : ExternalCurrents C X Y) :
    let vd : VariationalData C X Y :=
      ⟨ec.einsteinTensor + ec.stressTensor, ec.gaugeCurrent, 0⟩
    HasMonoidalEOM C vd ec := by
  refine ⟨?_, ?_, ?_⟩
  · rfl
  · rfl
  · rfl

/-! ## §4  The bridge to the scalar form

The point of the retype is that nothing previously statable is lost: the old
scalar Einstein equation is a *theorem* about the new rank-2 one, obtained by
contracting.  The converse direction fails, which is what makes the rank-2 form
strictly stronger. -/

section Bridge

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
variable {X Y : C}

/-- **The bridge.**  Contracting the rank-2 Einstein identity against any
    co-pairing `η` yields the scalar equation this module used to state
    directly.  The proof rewrites by the rank-2 identity and then uses
    additivity of `contract` — so the scalar form is recovered, not assumed,
    and the retype is a refactor rather than a replacement. -/
theorem einstein_contracted (vd : VariationalData C X Y)
    (ec : ExternalCurrents C X Y) [h : HasMonoidalEOM C vd ec]
    (η : (𝟙_ C) ⟶ X ⊗ Y) :
    contract η vd.gravity
      = contract η ec.einsteinTensor + contract η ec.stressTensor := by
  rw [h.einstein, map_add]

/-- The same bridge with the contraction unfolded, so the recovered statement
    is visibly the old one: an equation in `End(𝟙_C)` between the gravity
    scalar and the sum of the Einstein and stress scalars. -/
theorem einstein_contracted_comp (vd : VariationalData C X Y)
    (ec : ExternalCurrents C X Y) [HasMonoidalEOM C vd ec]
    (η : (𝟙_ C) ⟶ X ⊗ Y) :
    η ≫ vd.gravity = η ≫ ec.einsteinTensor + η ≫ ec.stressTensor := by
  simpa using einstein_contracted vd ec η

/-- **The converse fails: a scalar contraction cannot state a rank-2
    identity.**  If equality of contractions implied equality of the rank-2
    fields, uniformly in the co-pairing, then there would be at most one
    pairing `X ⊗ Y ⟶ 𝟙_ C`.

    The invariant is `zero_comp`: the degenerate co-pairing `η = 0` contracts
    every field to the same scalar, so it separates nothing.  Hence in any
    `Preadditive` monoidal category whose pairing space has two distinct
    elements, the scalar Einstein-shaped equation this module used to carry is
    **strictly weaker** than the rank-2 identity it is named after. -/
theorem subsingleton_of_contract_reflects
    (h : ∀ (η : (𝟙_ C) ⟶ X ⊗ Y) (G T : PairingSpace C X Y),
        contract η G = contract η T → G = T) :
    Subsingleton (PairingSpace C X Y) :=
  ⟨fun G T => h 0 G T (by simp)⟩

/-- Contrapositive form: two distinct rank-2 fields that a contraction cannot
    tell apart. -/
theorem exists_contract_not_reflecting (G T : PairingSpace C X Y) (hGT : G ≠ T) :
    ∃ η : (𝟙_ C) ⟶ X ⊗ Y, contract η G = contract η T ∧ G ≠ T :=
  ⟨0, by simp, hGT⟩

/-- **What the Einstein identity constrains, exactly.**  `gravity = G + T` says
    precisely that `T` is the residual `gravity − G`; it says nothing at all
    about `G`.  So the identity **defines** the stress term once the Einstein
    term is chosen, and **decomposes** neither — AGENTS.md §"Defined residual ≠
    derived decomposition", stated in Lean.

    This is orthogonal to the rank of the objects and is untouched by the
    2026-09-15 retype: it is the reason `hasMonoidalEOM_of_def` can discharge
    all three equations by `rfl`, and it stays open. -/
theorem einstein_split_iff (g G T : PairingSpace C X Y) :
    g = G + T ↔ T = g - G := by
  constructor
  · intro h; rw [h]; abel
  · intro h; rw [h]; abel

/-- The Einstein identity is solvable for **every** choice of Einstein term, so
    it excludes no candidate `G` whatever.  Immediate from
    `einstein_split_iff`, and recorded separately because it is the form the
    anti-laundering rule is usually stated in. -/
theorem exists_stress_for_every_einstein (g G : PairingSpace C X Y) :
    ∃ T : PairingSpace C X Y, g = G + T :=
  ⟨g - G, (einstein_split_iff g G (g - G)).2 rfl⟩

end Bridge

end QOU.MathlibExt.MonoidalCalcVar
