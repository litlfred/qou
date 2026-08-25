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

  Thurston's decomposition theorem itself is classical geometric
  topology and remains class-axiomatised below.  The *dilogarithm*
  half is no longer axiomatised — see the note immediately following.

  ═══ TWO AXIOMS DISCHARGED (2026-08-10) ═══

  This file previously declared BOTH `blochWigner` and its vanishing
  on ℝ as axioms, with this proof note:

    "Proof note (2026-08-03): Attempted to prove this using
     `Complex.ofReal_im`, but `blochWigner` is declared as an opaque
     `axiom` with no body, so there is nothing to unfold or apply
     lemmas to. Retaining axiom."

  That note was right about the mechanism and wrong about the
  conclusion: the opacity was a *choice made in this file*, not a
  constraint.  The corpus has a real, non-opaque Bloch–Wigner —
  `QOU.Archimedean.BlochWigner_lob`, defined as `Λ(θ₁)+Λ(θ₂)+Λ(θ₃)`
  in `QOU/Archimedean/BlochWignerLobachevsky.lean` — and pointing at
  it turns both axioms into a definition and a theorem.

  `blochWigner_real` is now `QOU.Knot.FlatTet.BlochWigner_lob_ofReal`,
  proved sorry-free for EVERY real `x` with no hypotheses.  (The
  corpus's older `BlochWigner_lob_real_eq_zero` assumed `0 < x < 1`,
  which would not have covered the trefoil's shapes `−1` and `2`.)

  This matters for the prose above: "torus-knot complements have zero
  hyperbolic volume" now rests on a theorem, rather than on an axiom
  asserting the very thing being used.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Topology.UnitInterval
import QOU.Knot.FlatTetrahedra

namespace QOU.ParticleInteractions

/-- The Bloch-Wigner dilogarithm `D : ℂ → ℝ`.

    **No longer an axiom.**  This is the corpus's real Bloch–Wigner,
    `QOU.Archimedean.BlochWigner_lob = Λ(θ₁)+Λ(θ₂)+Λ(θ₃)`, which
    `QOU/Knot/KummerRadial.lean` proves equals
    `Im (Li₂ z) + log‖z‖ · arg(1−z)` on the upper half plane. -/
-- Ref: [zagier1986] https://doi.org/10.1007/BF01388528 (Bloch-Wigner dilogarithm D(z))
noncomputable def blochWigner : ℂ → ℝ := QOU.Archimedean.BlochWigner_lob

/-- **Bloch-Wigner vanishes on the real line — now a theorem.**

    Discharges the former `axiom blochWigner_real`.  Holds for every
    real `x` with no hypotheses at all, including the junk-value cases
    `x = 0` and `x = 1`, where Lean's `1/0 = 0` still lands on `arg = 0`.

    This is the statement the block's prose uses to conclude that torus
    knots — whose shape parameters are all real — have zero volume. -/
-- Ref: [zagier1986] https://doi.org/10.1007/BF01388528 (Bloch-Wigner dilogarithm vanishes on ℝ)
theorem blochWigner_real (x : ℝ) : blochWigner (x : ℂ) = 0 :=
  QOU.Knot.FlatTet.BlochWigner_lob_ofReal x

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
