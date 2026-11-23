import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import QOU.KnotTheory


/-!
# QOU.TorsionKnotFlow — q-Torsion driven evolution of knot positions

The torsion-driven knot flow evolves the positions of localized knots
on CP¹ ≅ S² according to the q-deformed Reeb vector field.  Each
knot carries intrinsic angular momentum proportional to its crossing
number, and nearby knots interact via short-range repulsion.

## References

- [leitner2026] §3 Lifting of Quantum Torsion

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- State of a single particle during evolution: position + velocity on S². -/
structure ParticleState where
  /-- Position θ ∈ [0, π]. -/
  theta : R_q
  /-- Position φ ∈ [0, 2π). -/
  phi : R_q
  /-- Angular velocity in θ direction. -/
  vTheta : R_q
  /-- Angular velocity in φ direction. -/
  vPhi : R_q
  /-- The knot type (invariant under evolution). -/
  knot : KnotTheory.BraidWord

/-- A bundle state at time t: collection of evolving particles. -/
structure BundleState where
  /-- Current time. -/
  time : R_q
  /-- Current particle states. -/
  particles : List ParticleState
  -- A `time_nonneg : time ≥ 0` field is intentionally omitted: the
  -- combinatorial ground ring `R_q` carries no order, so the
  -- non-negativity constraint is archimedean and lives in the ℝ
  -- specialisation, not here.
  -- Ref: [leitner2026] §3, Definition: Torsion-driven knot flow

/-- Total crossing content of a bundle state `S_t`. -/
def BundleState.totalCrossings (s : BundleState) : ℕ :=
  (s.particles.map (fun p => p.knot.crossingCount)).sum

/-- Evolving particle positions on `P(V)` while keeping each particle's knot type
    fixed preserves the total knot crossing content of the bundle state. -/
theorem BundleState.totalCrossings_preserved_of_knots_eq
    (s₁ s₂ : BundleState)
    (hknots : s₁.particles.map ParticleState.knot = s₂.particles.map ParticleState.knot) :
    s₁.totalCrossings = s₂.totalCrossings := by
  unfold totalCrossings
  have hmap := congrArg (List.map KnotTheory.BraidWord.crossingCount) hknots
  simp only [List.map_map] at hmap
  exact congrArg List.sum hmap

/-- Intrinsic angular momentum of a knot type, proportional to crossing
    number: `ω_K = c(K) · 2π`.  Archimedean specialisation over `ℝ`
    (AGENTS.md §7c) — the `2π` factor is genuinely real-valued, so this
    observable lands in `ℝ` rather than the combinatorial ground ring `R_q`. -/
-- Ref: [leitner2026] §3 Lifting of Quantum Torsion
noncomputable def intrinsicAngularMomentum (pd : KnotTheory.BraidWord) : ℝ :=
  (pd.crossingCount : ℝ) * (2 * Real.pi)

/-- Intrinsic angular momentum is always non-negative. -/
theorem intrinsicAngularMomentum_nonneg (pd : KnotTheory.BraidWord) :
    0 ≤ intrinsicAngularMomentum pd := by
  unfold intrinsicAngularMomentum
  have hpi : 0 < Real.pi := Real.pi_pos
  positivity

/-- Intrinsic angular momentum is strictly positive if and only if the knot has at least one crossing. -/
theorem intrinsicAngularMomentum_pos_iff (pd : KnotTheory.BraidWord) :
    0 < intrinsicAngularMomentum pd ↔ 0 < pd.crossingCount := by
  unfold intrinsicAngularMomentum
  have h2pi : (0 : ℝ) < 2 * Real.pi := by
    have := Real.pi_pos
    linarith
  constructor
  · intro h
    have hcast : (0 : ℝ) < (pd.crossingCount : ℝ) := pos_of_mul_pos_left h (le_of_lt h2pi)
    exact Nat.cast_pos.mp hcast
  · intro h
    have hcast : (0 : ℝ) < (pd.crossingCount : ℝ) := Nat.cast_pos.mpr h
    exact mul_pos hcast h2pi

/-- Short-range pairwise repulsive force between two localized knots within Planck-scale
    separation: `F_{ij} = (Δ_q(K_i) · Δ_q(K_j)) / (d(p_i, p_j)² + ℓ_P²)`. -/
noncomputable def pairwiseRepulsiveForce (delta_i delta_j dist ell_P : ℝ) : ℝ :=
  (delta_i * delta_j) / (dist ^ 2 + ell_P ^ 2)

/-- Pairwise repulsive force is symmetric under particle exchange `i ↔ j`. -/
theorem pairwiseRepulsiveForce_symm (delta_i delta_j dist ell_P : ℝ) :
    pairwiseRepulsiveForce delta_i delta_j dist ell_P =
      pairwiseRepulsiveForce delta_j delta_i dist ell_P := by
  unfold pairwiseRepulsiveForce
  ring

/-- For Planck cutoff `ℓ_P > 0` and same-sign Alexander weights `Δ_q(K_i) · Δ_q(K_j) > 0`,
    the short-range pairwise force is strictly repulsive (`F_{ij} > 0`) and nonsingular at all distances. -/
theorem pairwiseRepulsiveForce_pos {delta_i delta_j dist ell_P : ℝ}
    (hell : 0 < ell_P) (hdelta : 0 < delta_i * delta_j) :
    0 < pairwiseRepulsiveForce delta_i delta_j dist ell_P := by
  unfold pairwiseRepulsiveForce
  have hdenom : 0 < dist ^ 2 + ell_P ^ 2 := by positivity
  exact div_pos hdelta hdenom

end

end QOU
