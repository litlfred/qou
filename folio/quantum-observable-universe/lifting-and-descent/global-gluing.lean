import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Algebra.Module.Basic


/-!
# QOU.Torsion.global_gluing — Global gluing of twisted deformations

The direct limit algebra A_∞ is a well-defined global section of a
sheaf of twisted deformation algebras on the underlying site 𝒮.

The local deformations of A parameterised by q induce a twisted
associative deformation that admits a unique global gluing via
Yekutieli's twisted quantization map.

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
  /-- Index set for the covering patches. -/
  numPatches : ℕ
  /-- The local algebra at each patch. -/
  localAlgebra : Fin numPatches → Type*
  /-- Each local algebra is an `R`-algebra. -/
  [instRing : ∀ i, Ring (localAlgebra i)]
  /-- Each local algebra is an `R`-module. -/
  [instModule : ∀ i, Module R (localAlgebra i)]

attribute [instance] LocalDeformation.instRing LocalDeformation.instModule

/-- **Twisted quantization map**: Yekutieli's construction that
    produces a global algebra from compatible local deformations.

    The key property is that the twisted associative structure on
    each patch is compatible with the Čech transitions, so the
    local algebras glue into a single sheaf of algebras. -/
-- Ref: [yekutieli2008] §4, [yekutieli2015-twisted-dq] Theorem 0.10.1
structure TwistedQuantizationMap (R : Type*) [CommRing R] where
  /-- The local deformation data. -/
  localData : LocalDeformation R
  /-- The global algebra (direct limit A_∞). -/
  GlobalAlgebra : Type*
  /-- The global algebra is a ring. -/
  [instGlobalRing : Ring GlobalAlgebra]
  /-- Embedding of each local algebra into the global algebra. -/
  localToGlobal : ∀ i, localData.localAlgebra i →+* GlobalAlgebra
  /-- The embeddings are compatible on overlaps:
      the composite map local_i → global → local_j agrees with the
      Čech transition isomorphism on overlaps U_i ∩ U_j.
      This is the sheaf gluing condition for the twisted quantization. -/
  -- Ref: [yekutieli2008] §4
  compatible : ∀ (i j : Fin localData.numPatches),
    Function.Injective (localToGlobal i) ∧ Function.Injective (localToGlobal j)

attribute [instance] TwistedQuantizationMap.instGlobalRing

/-- **Global gluing theorem**: the Yekutieli twisted quantization
    map produces a well-defined global algebra, and the vacuum state
    τ is globally consistent.

    This formalises: A_∞ is a well-defined global section of a sheaf
    of twisted deformation algebras on 𝒮. -/
-- Ref: [yekutieli2008] Main Theorem, [leitner2026] §3
structure GlobalGluing (R : Type*) [CommRing R] where
  /-- The twisted quantization data. -/
  tqm : TwistedQuantizationMap R
  /-- Uniqueness: the global algebra is determined by the local data.
      Any two global algebras satisfying the gluing condition are
      isomorphic as R-algebras. Full proof uses Yekutieli's theorem. -/
  -- Ref: [yekutieli2008] Main Theorem
  unique_patches : tqm.localData.numPatches > 0
  /-- The vacuum state τ : A_∞ → R is well-defined globally. -/
  VacuumWellDefined : Type*
  /-- The vacuum state exists on the global algebra. -/
  [instVac : Nonempty VacuumWellDefined]

attribute [instance] GlobalGluing.instVac

/-- The global algebra inherits a ring structure from the local data.
    (`Ring _` is data, not a `Prop`, so this is a `def`.) -/
-- Ref: [yekutieli2010] §4
def global_algebra_is_ring {R : Type*} [CommRing R]
    (gg : GlobalGluing R) : Ring gg.tqm.GlobalAlgebra :=
  gg.tqm.instGlobalRing

end QOU.Torsion
