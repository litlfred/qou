-- Ref: [kashaev1997] Kashaev, The hyperbolic volume of knots from the quantum dilogarithm.
-- Ref: [murakami-murakami2001] Murakami-Murakami, The colored Jones polynomials and
--   the simplicial volume of a knot.
-- Vol(K) factors strictly through the QOU fibre functor τ : C → Arch.
--
-- **Proposition (conditional on `conj:kashaev-volume-conjecture`, per
-- AGENTS.md §3b-cond).**  The Kashaev-limit identification of the
-- hyperbolic volume is the conjectural input, axiomatised as the class
-- `QOU.Kashaev.VolumeConjecture`; conditional on an instance, the
-- factorization Vol(K_β) = τ_arch(Vol_q(β)) is *derived* below
-- (`vol_through_tau_of_volumeConjecture`).
--
-- The categorified `VolThroughTau` data packaging (with `Category C`)
-- lives in lean/QOU/MotivesArchimedean.lean; this sibling carries the
-- conditional derivation.
import Mathlib.Data.Real.Basic
import Mathlib.CategoryTheory.Functor.Basic
import QOU.Kashaev

namespace QOU.BraidsKnots

open QOU.Kashaev QOU.PhiQPiece

/-- Abstract archimedean target category Arch (e.g. smooth manifolds,
    real Hilbert spaces, or any chosen archimedean realization). -/
structure ArchimedeanCategory where
  /-- Carrier type of objects in `Arch`. -/
  Obj : Type*
  /-- The category structure on `Arch` — morphisms, composition, identities.
      This is what makes `τ : C ⥤ Arch.Obj` a genuine functor, and it is what
      this mirror was missing (bean `qou-u87j`). -/
  [cat : CategoryTheory.Category Obj]
  /-- Real-valued evaluation `π_∞ : Obj → ℝ` on the archimedean place
      (object-level; not functorial). -/
  archProj : Obj → Real

attribute [instance] ArchimedeanCategory.cat

/-- The QOU **fibre functor** `τ`, a genuine `C ⥤ Arch.Obj`.

    Brought into line with the library declaration
    (`lean/QOU/MotivesArchimedean.lean:102`), which is ahead of this mirror on
    both counts (bean `qou-u87j`):

    * this had `obj : C → Arch.Obj` — an action on **objects only**, with no
      action on morphisms and no functor laws. A structure named
      `FibreFunctor` that is not a functor.
    * `archRestriction` was a **free field**, so "the archimedean restriction
      `τ_arch = π_∞ ∘ τ`" could be any function `C → ℝ` unrelated to `τ`. It
      is now *derived*, which is what its own docstring always claimed.

    `archRestriction` is deliberately not a functor: it composes `τ` with the
    object-level evaluation `Arch.archProj`, and its codomain `ℝ` is a ring,
    not a category. -/
structure FibreFunctor (C : Type*) [CategoryTheory.Category C]
    (Arch : ArchimedeanCategory) where
  /-- The underlying genuine functor `τ : C ⥤ Arch.Obj`. -/
  functor : CategoryTheory.Functor C Arch.Obj

/-- The archimedean restriction `τ_arch = π_∞ ∘ τ`, derived from `τ.functor`
    and `Arch.archProj`. A plain function `C → ℝ`. -/
def FibreFunctor.archRestriction {C : Type*} [CategoryTheory.Category C]
    {Arch : ArchimedeanCategory} (τ : FibreFunctor C Arch) : C → Real :=
  fun c => Arch.archProj (τ.functor.obj c)

/-- **Vol(K) factors through τ (conditional on the Kashaev volume
    conjecture).**

    Hypotheses:
    * `[VolumeConjecture q]` — the class axiomatisation of
      `conj:kashaev-volume-conjecture`: the hyperbolic volume equals
      the Kashaev limit (`kvc_holds`).
    * `hcomp` — the computation rule of the archimedean realization
      functor: `τ_arch` evaluates the algebraic quantum volume
      `Vol_q(β)` as the Kashaev limit of `β` (per
      `def:archimedean-realization-functor`).

    Conclusion: the real-valued knot volume factors through the fibre
    functor, `Vol(K_β) = τ_arch(Vol_q(β))` — derived from `kvc_holds`,
    not assumed. -/
theorem vol_through_tau_of_volumeConjecture (q : ℝ) [inst : VolumeConjecture q]
    {C : Type*} [CategoryTheory.Category C] {Arch : ArchimedeanCategory}
    (τ : FibreFunctor C Arch) (β : Braid) (algVol : C)
    (hcomp : τ.archRestriction algVol = inst.kashaevLimit β) :
    inst.hypVolume β = τ.archRestriction algVol := by
  rw [hcomp]
  exact inst.kvc_holds β

end QOU.BraidsKnots
