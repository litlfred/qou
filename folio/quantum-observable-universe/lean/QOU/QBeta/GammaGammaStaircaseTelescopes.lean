import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic.Group

/-!
# The upward one-strand γγ staircase telescopes

A γγ collision on strands `i, i+1, i+2` is the vertex `V_i = σ_i σ_{i+1}⁻¹`.
Placing successive collisions one strand higher each time gives
`V_0 V_1 ⋯ V_{k-1}`, and in any group this product collapses:

  `V_0 V_1 ⋯ V_{k-1} = σ_0 σ_k⁻¹`.

So climbing the strand-count tower by one strand per collision, upward,
produces only two crossings at opposite ends, whatever `k` is. This is a
statement about that placement alone (scope a); it does not exclude other
placements. Pre-registration: `computations/probes/gg_ntower/preregistration.md` §2.

The lemma is stated for an arbitrary group, so it holds in the braid group
before any Hecke relation is imposed, and hence also for the images of the
generators in `H_n(q)`.
-/

namespace QOU.QBeta.GammaGammaStaircase

variable {G : Type*} [Group G]

/-- The staircase of `k` collisions at positions `0, 1, …, k-1`. -/
def staircase (g : ℕ → G) (k : ℕ) : G :=
  ((List.range k).map fun j => g j * (g (j + 1))⁻¹).prod

/-- Telescoping: `∏_{j<k} g_j g_{j+1}⁻¹ = g_0 g_k⁻¹`. -/
theorem staircase_eq (g : ℕ → G) (k : ℕ) :
    staircase g k = g 0 * (g k)⁻¹ := by
  induction k with
  | zero => simp [staircase]
  | succ k ih =>
    unfold staircase at ih ⊢
    rw [List.range_succ, List.map_append, List.prod_append, ih]
    simp [mul_assoc]

/-- Two collisions: `(σ_0 σ_1⁻¹)(σ_1 σ_2⁻¹) = σ_0 σ_2⁻¹`. -/
theorem two_collisions (a b c : G) : (a * b⁻¹) * (b * c⁻¹) = a * c⁻¹ := by
  group

end QOU.QBeta.GammaGammaStaircase
