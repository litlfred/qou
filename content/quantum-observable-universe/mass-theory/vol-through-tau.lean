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
import QOU.Kashaev

namespace QOU.BraidsKnots

open QOU.Kashaev QOU.PhiQPiece

/-- Abstract archimedean target category Arch (e.g. smooth manifolds,
    real Hilbert spaces, or any chosen archimedean realization). -/
structure ArchimedeanCategory where
  /-- Carrier type of the archimedean target. -/
  Obj : Type*
  /-- Real-valued evaluation π_∞ : Obj → ℝ on the archimedean place. -/
  archProj : Obj → Real

/-- The fibre functor τ : C → Arch of a QOU.

    Composing τ with the archimedean projection π_∞ gives the unique
    archimedean route out of C; we name this composite τ_arch. -/
structure FibreFunctor (C : Type*) (Arch : ArchimedeanCategory) where
  /-- Action of τ on objects of C. -/
  obj : C → Arch.Obj
  /-- The archimedean restriction τ_arch = π_∞ ∘ τ on objects. -/
  archRestriction : C → Real

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
    {C : Type*} {Arch : ArchimedeanCategory}
    (τ : FibreFunctor C Arch) (β : Braid) (algVol : C)
    (hcomp : τ.archRestriction algVol = inst.kashaevLimit β) :
    inst.hypVolume β = τ.archRestriction algVol := by
  rw [hcomp]
  exact inst.kvc_holds β

end QOU.BraidsKnots
