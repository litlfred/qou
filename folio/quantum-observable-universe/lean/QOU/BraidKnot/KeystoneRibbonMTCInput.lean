/-
Copyright (c) 2026 litlfred. All rights reserved.

# Input (RT), toward Mathlib: the ribbon-category quantum dimension grounds `bwS0`'s `d`

`KeystoneRTSurgeryConstruction.lean` reduced the `bwse` hinge to two named irreducible inputs, one
of which — **(RT)** — is the Reshetikhin–Turaev requirement that the gauge datum `bwS0` is the RT
surgery weight `S_{0λ} = d_λ/D` of a **ribbon / modular tensor category**. There, the quantum
dimension `d_λ` was an *abstract field element* (`VerlindeVacuumRow.d : ι → R`). This file takes the
next step **toward a genuine Mathlib ribbon-category statement**: it defines `d_λ` as the actual
**categorical quantum dimension** — the right trace of the identity — computed in a real Mathlib
`[BraidedCategory C] [RightRigidCategory C]`, and grounds the vacuum row in it.

## What is proved (sorry-free)

* `qDimObj X : 𝟙_C ⟶ 𝟙_C` — the categorical (right) quantum dimension of an object `X` in a braided
  right-rigid category, as the endomorphism of the unit
  `η_ X Xᘁ ≫ (β_ X Xᘁ).hom ≫ ε_ X Xᘁ` (coevaluation, braid, evaluation) — the standard ribbon
  trace `tr(𝟙_X)`, built on Mathlib's own duality (`η_`, `ε_`) and braiding (`β_`).
* `RibbonMTCInput` — the RT input requirement over a Mathlib braided right-rigid category: a family
  of simple objects `S : ι → C`, a scalar evaluation `evalUnit : End(𝟙_C) → R`, and the vacuum
  object's categorical dimension being `1`.
* `catQDim` — the base-ring quantum dimension `d_λ = evalUnit(qDimObj (S λ))`.
* `toVerlindeVacuumRow` + `vacuumRow_S0_eq_catQDim` (proved) — the modular S-matrix vacuum row of
  the RT input **is** the categorical quantum dimension normalized: `S_{0λ} = catQDim λ / D`. So the
  abstract `bwS0` value step is now grounded in Mathlib's categorical dimension, not a free scalar.

## Honest scope (STRICT, §Axiomatization-is-NOT-a-Proof)

This grounds the *quantum-dimension* half of input (RT) in Mathlib's braided-rigid category theory.
It does **NOT** close `bwse`: the two irreducible inputs remain — (RT) that the localization
category's simple-object dimensions are *these* categorical dimensions and that `bwS0` is their RT
surgery weight (the cited Kirby-invariance theorem; the full ribbon-functor + surgery calculus is
absent from Mathlib), and (BW=Hecke) that the category is the Hecke MTC. `evalUnit` and
`vac_dim_one` are carried as the RT-input data/hypothesis (content-bearing, not `True`); the
theorem *derives* the vacuum-row identity from them. No fit; nothing wired; L2 unchanged (2/7).

Base ring (§7c): the scalar side is generic `{R : Type*} [Field R]`; the categorical side is any
Mathlib braided right-rigid category `C`.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/
import QOU.BraidKnot.BWVacuumRowIsHecke
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

namespace QOU.BraidKnot.RibbonMTC

open CategoryTheory MonoidalCategory BraidedCategory
open QOU.BraidKnot

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] [RightRigidCategory C]

/-- **The categorical (right) quantum dimension** of an object `X` in a braided right-rigid
category, as an endomorphism of the unit object: the *braided*, **twistless** closure of the
identity, `𝟙_C --η_X--> X ⊗ Xᘁ --β--> Xᘁ ⊗ X --ε_X--> 𝟙_C`.  This is the `dim_q(X) ∈ End(𝟙_C)` that
the abstract `VerlindeVacuumRow.d` stands for.

**Not the ribbon trace** (a borrowed name this docstring used to carry): the ribbon trace carries
the balancing twist and there is no `BalancedCategory` in the variable block above, so no `θ`
appears here and none can.  See `QOU.MathlibExt.qDimTwistedWith` for the twisted version.  Nothing
downstream of this definition is affected — `qDim_unit` and the vacuum-row results are true of the
object actually defined here, and since `θ_𝟙 = 𝟙` they read the same either way. -/
noncomputable def qDimObj (X : C) : (𝟙_ C ⟶ 𝟙_ C) :=
  η_ X Xᘁ ≫ (β_ X Xᘁ).hom ≫ ε_ X Xᘁ

/-- **RT input over a Mathlib ribbon category.** The data the Reshetikhin–Turaev construction needs
to produce the vacuum row `bwS0`: a family of simple objects `S : ι → C` (the fusion labels), a
scalar evaluation `evalUnit : End(𝟙_C) → R` (the ribbon category's `End(𝟙_C) ≅ R`), a total
quantum dimension `D ≠ 0`, and the vacuum object of categorical quantum dimension `1`. -/
structure RibbonMTCInput (ι : Type*) (C : Type*) [Category C] [MonoidalCategory C]
    [BraidedCategory C] [RightRigidCategory C] (R : Type*) [Field R] where
  /-- The simple objects indexed by the fusion labels. -/
  S : ι → C
  /-- The scalar evaluation `End(𝟙_C) → R` (the ribbon category's ground-ring identification). -/
  evalUnit : (𝟙_ C ⟶ 𝟙_ C) → R
  /-- The vacuum (trivial-object) label. -/
  vac : ι
  /-- Total quantum dimension `D = √(Σ d²)` (abstract; only `D ≠ 0` used). -/
  D : R
  /-- `D ≠ 0`. -/
  D_ne : D ≠ 0
  /-- The vacuum object has categorical quantum dimension `1`. -/
  vac_dim_one : evalUnit (qDimObj (S vac)) = 1

namespace RibbonMTCInput

variable {ι R : Type*} [Field R] (H : RibbonMTCInput ι C R)

/-- The base-ring quantum dimension `d_λ = evalUnit(qDimObj (S λ))` — the categorical dimension of
the `λ`-th simple object, evaluated into `R`. -/
noncomputable def catQDim (lam : ι) : R := H.evalUnit (qDimObj (H.S lam))

/-- The RT input assembles into a `VerlindeVacuumRow` whose quantum dimension is the categorical
`catQDim`. -/
noncomputable def toVerlindeVacuumRow : VerlindeVacuumRow ι R where
  d := H.catQDim
  D := H.D
  vac := H.vac
  d_vac := H.vac_dim_one
  D_ne := H.D_ne

/-- **The modular S-matrix vacuum row of the RT input is the categorical quantum dimension,
normalized.** `S_{0λ} = catQDim λ / D` — the value `bwS0` must equal, now grounded in Mathlib's
braided-rigid categorical dimension rather than an abstract field element. -/
theorem vacuumRow_S0_eq_catQDim (lam : ι) :
    H.toVerlindeVacuumRow.S0 lam = H.catQDim lam / H.D := rfl

/-- The vacuum entry is `S_{00} = 1/D` (the vacuum object's categorical dimension is `1`). -/
theorem vacuumRow_S0_vac : H.toVerlindeVacuumRow.S0 H.vac = 1 / H.D := by
  rw [vacuumRow_S0_eq_catQDim]
  unfold catQDim
  rw [H.vac_dim_one]

/-- **The value-step ratio, categorically:** `S_{0λ}/S_{00} = catQDim λ` — the categorical quantum
dimension of the `λ`-th simple object. This is `bwS0` recognised as the Verlinde vacuum row of the
*Mathlib* ribbon category, the content input (RT) supplies. -/
theorem vacuumRow_S0_ratio (lam : ι) :
    H.toVerlindeVacuumRow.S0 lam / H.toVerlindeVacuumRow.S0 H.vac = H.catQDim lam :=
  H.toVerlindeVacuumRow.S0_ratio lam

end RibbonMTCInput

end QOU.BraidKnot.RibbonMTC
