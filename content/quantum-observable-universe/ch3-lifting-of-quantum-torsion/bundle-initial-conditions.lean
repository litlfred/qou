/-!
# QOU.BundleInitialConditions — Big bang state over the projective line

A bundle initial condition is a finite collection of localized knots
on CP¹.  This is the "position-only" specification at the initial
moment: positions are known exactly, momenta are undetermined.

## References

- [leitner2026] §3 Lifting of Quantum Torsion
-/

import Mathlib.Data.Real.Basic
import QOU.KnotTheory

namespace QOU

/-- A bundle initial condition: a finite set of localized knots on CP¹.
    Equivalently, a section of the free commutative monoid on the knot
    sheaf K → P(V). -/
structure BundleInitialConditions where
  /-- The localized knots (position + knot type pairs). -/
  particles : List LocalizedKnot
  /-- Must have at least one particle. -/
  -- Ref: [leitner2026] §3, Definition: Bundle initial conditions
  nonempty : particles.length ≥ 1

/-! ## Basic accessors -/

/-- Total number of particles in the bundle. -/
def BundleInitialConditions.size (b : BundleInitialConditions) : ℕ :=
  b.particles.length

/-- Total crossing number of all knots in the bundle. -/
def BundleInitialConditions.totalCrossings (b : BundleInitialConditions) : ℕ :=
  b.particles.foldl (fun acc p => acc + p.knot.crossingCount) 0

/-- The set of distinct base points in the bundle. -/
def BundleInitialConditions.basePoints (b : BundleInitialConditions) :
    List (ℝ × ℝ) :=
  (b.particles.map LocalizedKnot.basePoint).dedup

/-- Size is always positive. -/
theorem BundleInitialConditions.size_pos (b : BundleInitialConditions) :
    b.size ≥ 1 := b.nonempty

/-! ## Hadron decomposition

When several localized knots share a common base point, they form a
hadron.  A bundle initial condition decomposes as a disjoint union of
hadrons distributed across P(V). -/

/-- Particles at a given base point. -/
def BundleInitialConditions.particlesAt (b : BundleInitialConditions)
    (p : ℝ × ℝ) : List LocalizedKnot :=
  b.particles.filter (fun k => k.basePoint = p)

/-- All particles are accounted for by the base-point partition. -/
-- Ref: [leitner2026] §3, Definition: Bundle initial conditions
theorem BundleInitialConditions.partition_complete
    (b : BundleInitialConditions) :
    (b.basePoints.bind (b.particlesAt ·)).length = b.size := by
  -- Ref: [manuscript] §3, the base-point partition covers all particles
  sorry

/-- Total crossing number equals the sum over base-point clusters. -/
-- Ref: [leitner2026] §3
theorem BundleInitialConditions.totalCrossings_additive
    (b : BundleInitialConditions) :
    b.totalCrossings =
      b.basePoints.foldl
        (fun acc p =>
          acc + (b.particlesAt p).foldl
            (fun a k => a + k.knot.crossingCount) 0)
        0 := by
  -- Ref: [manuscript] §3, crossing numbers are additive over the partition
  sorry

/-! ## Equivalence of bundle initial conditions

Two BICs are equivalent if related by a permutation of indices σ ∈ S_N
and ambient isotopy within each fibre. We use knot-name equality as our
combinatorial proxy for ambient isotopy. -/

/-- Two BICs are equivalent: same multiset of (basePoint, knotName) pairs. -/
def BundleInitialConditions.equiv (b₁ b₂ : BundleInitialConditions) : Prop :=
  (b₁.particles.map (fun k => (k.basePoint, k.knot.name))).Perm
    (b₂.particles.map (fun k => (k.basePoint, k.knot.name)))

/-- BIC equivalence is reflexive. -/
theorem BundleInitialConditions.equiv_refl (b : BundleInitialConditions) :
    b.equiv b :=
  List.Perm.refl _

/-- BIC equivalence is symmetric. -/
theorem BundleInitialConditions.equiv_symm {b₁ b₂ : BundleInitialConditions}
    (h : b₁.equiv b₂) : b₂.equiv b₁ :=
  h.symm

/-- BIC equivalence is transitive. -/
theorem BundleInitialConditions.equiv_trans {b₁ b₂ b₃ : BundleInitialConditions}
    (h₁ : b₁.equiv b₂) (h₂ : b₂.equiv b₃) : b₁.equiv b₃ :=
  h₁.trans h₂

/-- Equivalent BICs have the same size. -/
theorem BundleInitialConditions.equiv_preserves_size
    {b₁ b₂ : BundleInitialConditions} (h : b₁.equiv b₂) :
    b₁.size = b₂.size := by
  unfold size
  have := h.length_eq
  simp [List.length_map] at this
  exact this

end QOU
