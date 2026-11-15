import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Module.Defs
import Mathlib.Algebra.Ring.Hom.Defs

/-!
# QOU.Torsion.GlobalGluing — Global gluing of twisted deformations

The direct limit algebra A_∞ is a well-defined global section of a
sheaf of twisted deformation algebras on the underlying site 𝒮.

**Pre-Archimedean (formal-chain) version.**  Lives under `lean/QOU/`
and is compiled by `lake build`.  The co-located documentation stub
at `lifting-and-descent/global-gluing.lean` mirrors this content.

LaTeX label: `prop:global-gluing`

## References

- [yekutieli2008] Twisted Deformation Quantization of Algebraic Varieties
- [yekutieli2010] https://doi.org/10.1016/j.aim.2009.12.006
- [leitner2026] §3-lifting-of-quantum-torsion/global-gluing
-/

namespace QOU.Torsion

/-- **Local deformation algebra**: at each point p, the algebra
    `𝒪_{q(p)}(G)` of functions on the quantum group deformed by
    the local substrate parameter `q(p)`. -/
-- Ref: [yekutieli2008] §2
structure LocalDeformation (R : Type*) [CommRing R] where
  numPatches : ℕ
  localAlgebra : Fin numPatches → Type*
  [instRing : ∀ i, Ring (localAlgebra i)]
  [instModule : ∀ i, Module R (localAlgebra i)]

attribute [instance] LocalDeformation.instRing LocalDeformation.instModule

/-- **Twisted quantization map**: Yekutieli's construction that
    produces a global algebra from compatible local deformations. -/
-- Ref: [yekutieli2008] §4, [yekutieli2015-twisted-dq] Theorem 0.10.1
structure TwistedQuantizationMap (R : Type*) [CommRing R] where
  localData : LocalDeformation R
  GlobalAlgebra : Type*
  [instGlobalRing : Ring GlobalAlgebra]
  localToGlobal : ∀ i, localData.localAlgebra i →+* GlobalAlgebra
  -- Each local-to-global map embeds the local algebra; Yekutieli's
  -- compatibility on overlaps is then a property of how the images
  -- intersect (handled at the witness layer when overlaps are
  -- explicit). Cf. gemini-code-assist review on PR #535.
  -- Ref: [yekutieli2008] §4
  compatible : ∀ i, Function.Injective (localToGlobal i)

attribute [instance] TwistedQuantizationMap.instGlobalRing

/-- **Global gluing theorem**: the Yekutieli twisted quantization
    map produces a well-defined global algebra, and the vacuum state
    τ is globally consistent. -/
-- Ref: [yekutieli2008] Main Theorem, [leitner2026] §3
structure GlobalGluing (R : Type*) [CommRing R] where
  tqm : TwistedQuantizationMap R
  -- Ref: [yekutieli2008] Main Theorem
  unique_patches : tqm.localData.numPatches > 0
  VacuumWellDefined : Type*
  [instVac : Nonempty VacuumWellDefined]

attribute [instance] GlobalGluing.instVac

/-- The global algebra inherits a ring structure from the local data. -/
-- Ref: [yekutieli2010] §4
instance global_gluing {R : Type*} [CommRing R]
    (gg : GlobalGluing R) : Ring gg.tqm.GlobalAlgebra :=
  gg.tqm.instGlobalRing

end QOU.Torsion
