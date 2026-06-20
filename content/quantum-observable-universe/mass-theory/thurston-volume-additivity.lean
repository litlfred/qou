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
-- Ref: [zagier1986] https://doi.org/10.1007/BF01388528 (Bloch-Wigner dilogarithm D(z))
axiom blochWigner : ℂ → ℝ

/-- Bloch-Wigner vanishes on the real line.
    Taken as an axiom because `blochWigner` is opaque and this
    is a real theorem of hyperbolic geometry (not a rfl). -/
-- Ref: [zagier1986] https://doi.org/10.1007/BF01388528 (Bloch-Wigner dilogarithm vanishes on ℝ)
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

/-- Class-axiomatisation of Thurston's existence theorem
    (AGENTS.md §3b-cond): for every hyperbolic 3-manifold `M`
    equipped with a hyperbolic-volume function `hypVol`, an ideal
    triangulation realising the volume exists.

    The single field `triangulation_exists` is the classical
    [thurston1978] result; an instance is the conjectural input
    that downstream conditional theorems consume. -/
class HasThurstonTriangulation
    (M : Type*) [TopologicalSpace M] (hypVol : M → ℝ) where
  /-- Per-point ideal triangulation realising the hyperbolic volume. -/
  triangulation : M → IdealTriangulation
  /-- The volume coincides with the Thurston sum of Bloch–Wigner
      values on the chosen triangulation.
      Ref: [thurston1978] http://library.msri.org/books/gt3m/ -/
  volume_eq_thurston :
    ∀ m : M, hypVol m = thurstonVolume (triangulation m)

/-- **Thurston volume additivity** (conditional theorem, §3b-cond).
    Given an instance of `HasThurstonTriangulation M hypVol`, every
    point of `M` admits an ideal triangulation whose shape-parameter
    Bloch–Wigner sum equals the hyperbolic volume.

    The proof body has no `sorry`; the only unproved input is the
    class instance, which is the classical [thurston1978] theorem. -/
theorem thurstonVolumeAdditivity
    (M : Type*) [TopologicalSpace M]
    (hypVol : M → ℝ)
    [inst : HasThurstonTriangulation M hypVol] :
    ∀ m : M, ∃ T : IdealTriangulation, hypVol m = thurstonVolume T := by
  intro m
  exact ⟨inst.triangulation m, inst.volume_eq_thurston m⟩

end QOU.ParticleInteractions
