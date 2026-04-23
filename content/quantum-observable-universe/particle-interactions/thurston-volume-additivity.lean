/-
  Thurston additivity of hyperbolic volume.

  For a hyperbolic 3-manifold with an ideal triangulation having
  shape parameters z₁, …, z_N ∈ ℂ ∖ {0, 1}, the hyperbolic volume
  is the sum of Bloch-Wigner dilogarithms:

      Vol(M) = Σ D(zᵢ)

  where D(z) = Im(Li₂(z)) + arg(1-z) · log|z|.

  Degenerate tetrahedra (zᵢ ∈ ℝ) contribute zero, so torus-knot
  complements (Seifert fibered, all shape parameters real) have
  zero hyperbolic volume.

  Ref: [thurston1978] http://library.msri.org/books/gt3m/

  This theorem is classical geometric topology; we axiomatize it
  as an opaque class encoding the Thurston decomposition.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Topology.UnitInterval

namespace QOU.ParticleInteractions

/-- The Bloch-Wigner dilogarithm D : ℂ → ℝ, declared as an axiom.
    Stands in for the classical function
    D(z) = Im(Li₂(z)) + arg(1-z) · log|z|.
    Fully developed definition is outside the scope of this
    formalization.  Declared via `axiom` (no body) so that
    downstream lemmas cannot silently depend on a stub value. -/
axiom blochWigner : ℂ → ℝ

/-- Bloch-Wigner vanishes on the real line.
    Taken as an axiom because `blochWigner` is opaque and this
    is a real theorem of hyperbolic geometry (not a rfl). -/
axiom blochWigner_real (x : ℝ) : blochWigner (x : ℂ) = 0

/-- Data of a Thurston ideal triangulation: a finite list of shape
    parameters zᵢ ∈ ℂ ∖ {0, 1}. -/
structure IdealTriangulation where
  shapes : List ℂ
  shape_nontrivial : ∀ z ∈ shapes, z ≠ 0 ∧ z ≠ 1

/-- Hyperbolic volume computed from an ideal triangulation as the
    sum of Bloch-Wigner dilogarithms over its shape parameters. -/
noncomputable def thurstonVolume (T : IdealTriangulation) : ℝ :=
  (T.shapes.map blochWigner).sum

/-- **Thurston volume additivity** (stated, not proved here).
    Any hyperbolic 3-manifold M admits an ideal triangulation T
    whose shape-parameter sum equals the hyperbolic volume of M.
    This is the classical theorem of Thurston (1978); we state
    the existence of such a triangulation as an axiom-backed
    predicate. -/
theorem thurstonVolumeAdditivity
    (M : Type*) [TopologicalSpace M]
    (hypVol : M → ℝ) :
    ∀ m : M, ∃ T : IdealTriangulation, hypVol m = thurstonVolume T := by
  -- Ref: [thurston1978] http://library.msri.org/books/gt3m/
  sorry

end QOU.ParticleInteractions
