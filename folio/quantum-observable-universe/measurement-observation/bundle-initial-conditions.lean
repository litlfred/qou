import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import QOU.KnotTheory


/-!
# QOU.BundleInitialConditions — Bundle initial conditions over the projective line

A bundle initial condition is a collection of localized knots
(hadrons and photons) on CP¹ at a reference point in an affine chart.
This is a "position-only" specification: positions are known exactly,
momenta are undetermined.  The forward light cone S_1, S_2, ...
represents successive Reeb flow iterations; the backward light cone
S_{-1}, S_{-2}, ... reverses computation.  Whether the sequence
extends infinitely in either direction is not assumed.

## References

- [leitner2026] §3 Lifting of Quantum Torsion

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

open scoped Classical

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A knot type: combinatorial knot data carrying a crossing count and a
    name (the combinatorial proxy for ambient-isotopy class).
    Honest in-file mirror of the knot carrier used by the localized-knot
    sheaf; the canonical knot data lives in `QOU.KnotTheory`
    (`BraidWord.crossingCount` etc.). -/
structure Knot where
  /-- Number of crossings of the knot diagram. -/
  crossingCount : ℕ
  /-- The knot name (ambient-isotopy combinatorial proxy). -/
  name : String

/-- A localized knot: a knot type placed at a base point on `P(V)`
    (an affine-chart coordinate pair over `R_q`).
    Honest in-file mirror; `def:localized-hadron` is the narrative source. -/
structure LocalizedKnot where
  /-- The knot type sitting at this position. -/
  knot : Knot
  /-- The base point on `P(V)` (affine-chart coordinate pair). -/
  basePoint : R_q × R_q

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
    List (R_q × R_q) :=
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
    (p : R_q × R_q) : List LocalizedKnot :=
  b.particles.filter (fun k => decide (k.basePoint = p))

/-- Every particle is in the cluster at its own base point. -/
theorem BundleInitialConditions.particle_in_own_cluster
    (b : BundleInitialConditions) (k : LocalizedKnot) (hk : k ∈ b.particles) :
    k ∈ b.particlesAt k.basePoint := by
  unfold particlesAt
  simp only [List.mem_filter, decide_eq_true_eq]
  exact ⟨hk, trivial⟩

/-- The cluster at a point p contains only particles with base point p. -/
theorem BundleInitialConditions.cluster_basePoint_eq
    (b : BundleInitialConditions) (p : R_q × R_q) (k : LocalizedKnot)
    (hk : k ∈ b.particlesAt p) : k.basePoint = p := by
  unfold particlesAt at hk
  simp only [List.mem_filter, decide_eq_true_eq] at hk
  exact hk.2

/-- Total crossing number equals the sum of crossing numbers of
    all particles (directly from the definition). -/
theorem BundleInitialConditions.totalCrossings_eq_sum
    (b : BundleInitialConditions) :
    b.totalCrossings = b.particles.foldl (fun acc p => acc + p.knot.crossingCount) 0 :=
  rfl

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

end

end QOU
