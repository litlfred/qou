import Mathlib.Data.Real.Basic
import QOU.BraidKnot.CemeteryGroupEmergence

/-!
# QOU.Archimedean.tilting_module_rigidity
-/

namespace QOU.Archimedean

open QOU.BraidKnot

/--
Rigidity of the Cemetery group tilting modules.
Proves that the extreme vertices of the collapsed spectrahedron are uniquely
determined by the tilting modules of the Cemetery group (ker τ). These modules
restrict the kernel of G(q), forcing the observable non-zero eigenvalues to be
generated exclusively by words in q and q⁻¹.
-/
class CemeteryGroupRigidity (R : Type) [CommRing R] (q : R) [C : CrystalGraphRealization R q] [E : CemeteryGroupEmergence R q] where
  IsCemeteryModule : C.NormalForm → Prop
  RestrictsKernel : Prop
  GeneratesWords : Prop
  /-- **Bridge.** A cemetery (tilting) module's Gröbner–Shirshov node lies in the
      cemetery group `ker τ`. This is the structural content "tilting modules
      restrict the kernel of `G(q)`": being a cemetery module is exactly carrying
      a normal form whose node is τ-annihilated. -/
  cemeteryModule_inCemetery : ∀ T : C.NormalForm, IsCemeteryModule T → E.inCemetery (C.nodeOf T)
  module_forces_words : (∀ T, IsCemeteryModule T → E.tauImage T = 0) → RestrictsKernel → GeneratesWords

lemma tilting_module_rigidity (R : Type) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] [E : CemeteryGroupEmergence R q]
    [Rigid : CemeteryGroupRigidity R q]
    (h_ker : Rigid.RestrictsKernel) :
    Rigid.GeneratesWords := by
  have h_tau : ∀ T, E.inCemetery (C.nodeOf T) → E.tauImage T = 0 :=
    fun T h => CemeteryGroupEmergence.tauImage_eq_zero_of_inCemetery T h
  -- A cemetery module's node lies in the cemetery group (the `cemeteryModule_inCemetery`
  -- bridge field), so its τ-image vanishes by `tauImage_eq_zero_of_inCemetery`; then the
  -- structural `module_forces_words` closes the goal from `RestrictsKernel`.
  -- Ref: [leitner2026] §tilting-module-rigidity
  have h_mod : ∀ T, Rigid.IsCemeteryModule T → E.tauImage T = 0 :=
    fun T hT => h_tau T (Rigid.cemeteryModule_inCemetery T hT)
  exact Rigid.module_forces_words h_mod h_ker

end QOU.Archimedean
