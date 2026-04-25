-- Ref: [kashaev1997] Kashaev, The hyperbolic volume of knots from the quantum dilogarithm.
-- Ref: [murakami-murakami2001] Murakami-Murakami, The colored Jones polynomials and
--   the simplicial volume of a knot.
-- Vol(K) factors strictly through the QOU fibre functor τ : C → Arch.
--
-- Canonical declaration lives in: lean/QOU/MotivesArchimedean.lean
-- This sibling is a documentation-mirror of the QOU library declaration.

namespace QOU.BraidsKnots

/-- Abstract archimedean target category Arch (e.g. smooth manifolds,
    real Hilbert spaces, or any chosen archimedean realization). -/
structure ArchimedeanCategory where
  /-- Carrier type of the archimedean target. -/
  Obj : Type*
  /-- Real-valued evaluation π_∞ : Obj → ℝ on the archimedean place. -/
  archProj : Obj → ℝ

/-- The fibre functor τ : C → Arch of a QOU. Acts on objects of C
    by `obj`; the archimedean restriction τ_arch = π_∞ ∘ τ is the
    derived `def FibreFunctor.archRestriction` below (not a field),
    so it cannot disagree with `Arch.archProj ∘ obj`. -/
structure FibreFunctor (C : Type*) (Arch : ArchimedeanCategory) where
  /-- Action of τ on objects of C. -/
  obj : C → Arch.Obj

/-- The archimedean restriction τ_arch = π_∞ ∘ τ of a fibre functor. -/
def FibreFunctor.archRestriction {C : Type*} {Arch : ArchimedeanCategory}
    (τ : FibreFunctor C Arch) : C → ℝ :=
  fun c => Arch.archProj (τ.obj c)

/-- **Vol(K) factors through τ.**

    The real-valued knot volume of the closure of a braid β equals
    the τ_arch-image of its algebraic quantum volume Vol_q(β).
    This is the QOU statement of the volume conjecture as a
    factorization through the fibre functor. -/
structure VolThroughTau (C : Type*) (Arch : ArchimedeanCategory) where
  /-- The QOU fibre functor. -/
  τ : FibreFunctor C Arch
  /-- The algebraic quantum volume of a braid (as an element of C). -/
  algVol : C
  /-- The real-valued knot volume of the braid closure. -/
  knotVol : ℝ
  /-- Factorization: knotVol = τ_arch(algVol). -/
  factors : knotVol = τ.archRestriction algVol

end QOU.BraidsKnots
