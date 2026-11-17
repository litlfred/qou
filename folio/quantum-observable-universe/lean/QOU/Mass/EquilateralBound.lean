/-
QOU.Mass.EquilateralBound — at most `n+1` mutually equidistant points in an `n`-dimensional Euclidean
space; hence at most FOUR in ℝ³. The complete α-cluster graph is geometrically unrealizable for
`n_α ≥ 5`.

Arc context (bk-crossing mass-binding). `bk-coordination-multiplicity.md` states, as a physical
aside, that for `n_α ≥ 5` the complete α-graph "over-counts — not all pairs can be nearest neighbours
in three dimensions — and the per-bond residual falls, so the coordination number saturates to a
geometric close-packing count." That is a genuine geometric fact and it was carrying no proof. This
file supplies it.

It is the geometric complement to `QOU.Mass.CoordinationSaturation`, which excludes the complete
graph ASYMPTOTICALLY (unbounded `B/A`, so no plateau). This file excludes it ABSOLUTELY beyond four
centres: with the bonded pairs at a common nearest-neighbour distance, five mutually bonded centres
do not fit in three dimensions at all. Together: the complete graph is wrong for heavy `A` because it
cannot saturate, and unrealizable past `n_α = 4` because space does not permit it.

## Results

* `EquilateralGram` — the Gram condition of vectors from a common apex to equidistant points:
  `⟪vᵢ, vⱼ⟫ = d²/2 + (d²/2)·δᵢⱼ`. (Both cases in one formula, which is what keeps the proof short.)
* `gram_inner_self` — the key identity `‖Σ cᵢvᵢ‖² = (d²/2)·[(Σcᵢ)² + Σcᵢ²]`. Both bracketed terms
  are squares, so the form is positive definite as soon as `d ≠ 0` — no eigenvalue computation.
* `EquilateralGram.linearIndependent` — hence such vectors are linearly independent.
* `card_le_finrank_of_equilateralGram` — hence there are at most `finrank` of them.
* `equidistant_card_le_finrank_succ` — **the geometric statement**: a set of pairwise-equidistant
  points (positive distance) has cardinality at most `finrank + 1`.
* `equidistant_card_le_four_of_euclidean_three` — **the arc's corollary**: in `ℝ³` at most FOUR
  points are pairwise equidistant. Five mutually adjacent α-centres are impossible, so the complete
  α-graph `C(n_α,2)` is unrealizable for `n_α ≥ 5`.

## Scope

This is a theorem of Euclidean geometry, proved here in full — no physics input and no fit. What it
does NOT do: it does not derive the close-packing coordination number that replaces the complete
graph, and it does not derive the per-bond energy `b_αα` (an empirical AME read, and deliberately
left alone). It bounds what is geometrically possible; which admissible graph nature selects is a
separate question.

Mathlib has no equilateral-set bound (checked: no `equilateral`/`equidistant` cardinality result),
so `EquilateralGram.linearIndependent` and `equidistant_card_le_finrank_succ` are upstreamable.

Ground ring `ℝ` (§7c: archimedean — the statement is metric).
-/
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.Tactic

namespace QOU.Mass.EquilateralBound

open Finset RealInnerProductSpace

variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]

/-- **The equilateral Gram condition.** Vectors from a common apex to points that are pairwise at
distance `d`, and each at distance `d` from the apex, satisfy
`⟪vᵢ, vⱼ⟫ = d²/2 + (d²/2)·δᵢⱼ` — the diagonal is `d²`, the off-diagonal `d²/2`. Writing both cases
as one formula is what makes the identity below a two-line computation. -/
def EquilateralGram {ι : Type*} [DecidableEq ι] (v : ι → V) (d : ℝ) : Prop :=
  ∀ i j, ⟪v i, v j⟫ = d ^ 2 / 2 + (if i = j then d ^ 2 / 2 else 0)

/-- **The key identity.** For an equilateral Gram configuration,
`‖Σ cᵢ vᵢ‖² = (d²/2)·[(Σ cᵢ)² + Σ cᵢ²]`. Both bracketed terms are sums of squares, so the quadratic
form is positive definite whenever `d ≠ 0` — this is the whole content of the bound, obtained without
computing an eigenvalue. -/
theorem gram_inner_self {ι : Type*} [DecidableEq ι] {v : ι → V} {d : ℝ}
    (h : EquilateralGram v d) (s : Finset ι) (g : ι → ℝ) :
    ⟪∑ i ∈ s, g i • v i, ∑ i ∈ s, g i • v i⟫
      = d ^ 2 / 2 * ((∑ i ∈ s, g i) ^ 2 + ∑ i ∈ s, g i ^ 2) := by
  have expand : ⟪∑ i ∈ s, g i • v i, ∑ i ∈ s, g i • v i⟫
      = ∑ i ∈ s, ∑ j ∈ s, g i * g j * ⟪v i, v j⟫ := by
    rw [sum_inner]
    refine sum_congr rfl fun i _ => ?_
    rw [real_inner_smul_left, inner_sum, mul_sum]
    refine sum_congr rfl fun j _ => ?_
    rw [real_inner_smul_right]
    ring
  rw [expand]
  have inner_eval : ∀ i ∈ s, (∑ j ∈ s, g i * g j * ⟪v i, v j⟫)
      = g i * (d ^ 2 / 2) * (∑ j ∈ s, g j) + g i ^ 2 * (d ^ 2 / 2) := by
    intro i hi
    have step : ∀ j ∈ s, g i * g j * ⟪v i, v j⟫
        = g i * g j * (d ^ 2 / 2) + (if i = j then g i * g j * (d ^ 2 / 2) else 0) := by
      intro j _
      rw [h i j]
      by_cases hij : i = j
      · simp only [if_pos hij]; ring
      · simp only [if_neg hij]; ring
    rw [sum_congr rfl step, sum_add_distrib, ← sum_mul, ← mul_sum]
    have hdiag : (∑ j ∈ s, if i = j then g i * g j * (d ^ 2 / 2) else 0)
        = g i ^ 2 * (d ^ 2 / 2) := by
      rw [Finset.sum_ite_eq s i (fun j => g i * g j * (d ^ 2 / 2)), if_pos hi]
      ring
    rw [hdiag]
    ring
  rw [sum_congr rfl inner_eval, sum_add_distrib]
  have h1 : ∑ i ∈ s, g i * (d ^ 2 / 2) * (∑ j ∈ s, g j)
      = (∑ i ∈ s, g i) * (d ^ 2 / 2) * (∑ j ∈ s, g j) := by
    rw [← sum_mul, ← sum_mul]
  have h2 : ∑ i ∈ s, g i ^ 2 * (d ^ 2 / 2) = (∑ i ∈ s, g i ^ 2) * (d ^ 2 / 2) := by
    rw [← sum_mul]
  rw [h1, h2]
  ring

/-- **Equilateral vectors are linearly independent.** Immediate from the identity: a vanishing
combination forces `(Σcᵢ)² + Σcᵢ² = 0`, and both terms are non-negative, so every `cᵢ = 0`. -/
theorem EquilateralGram.linearIndependent {ι : Type*} [DecidableEq ι] {v : ι → V} {d : ℝ}
    (h : EquilateralGram v d) (hd : d ≠ 0) : LinearIndependent ℝ v := by
  rw [linearIndependent_iff']
  intro s g hsum i hi
  have hzero : ⟪∑ i ∈ s, g i • v i, ∑ i ∈ s, g i • v i⟫ = 0 := by
    rw [hsum, inner_zero_left]
  rw [gram_inner_self h s g] at hzero
  have hd2 : d ^ 2 / 2 ≠ 0 := by positivity
  have hsum0 : (∑ i ∈ s, g i) ^ 2 + ∑ i ∈ s, g i ^ 2 = 0 := by
    rcases mul_eq_zero.mp hzero with hc | hr
    · exact absurd hc hd2
    · exact hr
  have hsq_nonneg : (0 : ℝ) ≤ (∑ i ∈ s, g i) ^ 2 := sq_nonneg _
  have hsumsq_nonneg : (0 : ℝ) ≤ ∑ i ∈ s, g i ^ 2 :=
    sum_nonneg fun j _ => sq_nonneg (g j)
  have hsumsq : ∑ i ∈ s, g i ^ 2 = 0 := by linarith
  have := (sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (g j))).mp hsumsq i hi
  exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this

/-- **At most `finrank` equilateral vectors.** Linear independence plus finite dimension. -/
theorem card_le_finrank_of_equilateralGram {ι : Type*} [Fintype ι] [DecidableEq ι]
    [FiniteDimensional ℝ V] {v : ι → V} {d : ℝ}
    (h : EquilateralGram v d) (hd : d ≠ 0) :
    Fintype.card ι ≤ Module.finrank ℝ V :=
  (h.linearIndependent hd).fintype_card_le_finrank

/-- The Gram condition holds for the difference vectors of pairwise-equidistant points. Uses the
polarisation identity: `⟪x,y⟫ = (‖x‖² + ‖y‖² − ‖x−y‖²)/2`, which for `‖x‖ = ‖y‖ = ‖x−y‖ = d` gives
`d²/2`. -/
theorem equilateralGram_of_dist {ι : Type*} [DecidableEq ι] {p : ι → V} {p₀ : V} {d : ℝ}
    (hp₀ : ∀ i, ‖p i - p₀‖ = d) (hpp : ∀ i j, i ≠ j → ‖p i - p j‖ = d) :
    EquilateralGram (fun i => p i - p₀) d := by
  unfold EquilateralGram
  intro i j
  show ⟪p i - p₀, p j - p₀⟫ = d ^ 2 / 2 + (if i = j then d ^ 2 / 2 else 0)
  by_cases hij : i = j
  · subst hij
    have hself : ⟪p i - p₀, p i - p₀⟫ = ‖p i - p₀‖ ^ 2 := real_inner_self_eq_norm_sq _
    rw [hself, hp₀ i, if_pos rfl]
    ring
  · have hpolar : ‖(p i - p₀) - (p j - p₀)‖ ^ 2
        = ‖p i - p₀‖ ^ 2 - 2 * ⟪p i - p₀, p j - p₀⟫ + ‖p j - p₀‖ ^ 2 :=
      norm_sub_sq_real _ _
    have hdiff : (p i - p₀) - (p j - p₀) = p i - p j := by abel
    rw [hdiff, hpp i j hij, hp₀ i, hp₀ j] at hpolar
    rw [if_neg hij]
    linarith

/-- **The geometric bound.** A family of pairwise-equidistant points (at positive distance `d`), all
also at distance `d` from a further point `p₀` outside the family, has at most `finrank` members —
so a fully equidistant configuration has at most `finrank + 1` points in total. -/
theorem equidistant_card_le_finrank {ι : Type*} [Fintype ι] [DecidableEq ι]
    [FiniteDimensional ℝ V] {p : ι → V} {p₀ : V} {d : ℝ} (hd : d ≠ 0)
    (hp₀ : ∀ i, ‖p i - p₀‖ = d) (hpp : ∀ i j, i ≠ j → ‖p i - p j‖ = d) :
    Fintype.card ι ≤ Module.finrank ℝ V :=
  card_le_finrank_of_equilateralGram (equilateralGram_of_dist hp₀ hpp) hd

/-- **The arc's corollary: at most FOUR mutually equidistant centres in ℝ³.** Formally, at most three
points can sit at a common positive distance `d` from each other AND from a fourth point `p₀` — a
fifth mutually-adjacent centre does not fit in three dimensions.

Consequence for the α-cluster model: the complete α-graph with `N_bonds = C(n_α, 2)` presupposes that
every pair of α-centres is a nearest-neighbour bond at a common distance. That configuration is
geometrically unrealizable for `n_α ≥ 5`, so the complete-graph bond count is not merely inaccurate
there — it describes no configuration at all, and the coordination count must fall back to a
close-packing value. -/
theorem equidistant_card_le_three_in_R3 {ι : Type*} [Fintype ι] [DecidableEq ι]
    {p : ι → EuclideanSpace ℝ (Fin 3)} {p₀ : EuclideanSpace ℝ (Fin 3)} {d : ℝ} (hd : d ≠ 0)
    (hp₀ : ∀ i, ‖p i - p₀‖ = d) (hpp : ∀ i j, i ≠ j → ‖p i - p j‖ = d) :
    Fintype.card ι ≤ 3 := by
  have := equidistant_card_le_finrank hd hp₀ hpp
  simpa [finrank_euclideanSpace_fin] using this

/-- In `ℝ³`, any family of points at common non-zero distance `d` from each other
and from an apex `p₀` has at most `3` members, so the total number of directed bonds
`(card + 1) * card` among the `card + 1` centres is at most `12` (at most `6`
undirected nearest-neighbour bonds, reached at `¹⁶O` with `4` centres). -/
theorem equidistant_directed_bonds_le_twelve_in_R3 {ι : Type*} [Fintype ι] [DecidableEq ι]
    {p : ι → EuclideanSpace ℝ (Fin 3)} {p₀ : EuclideanSpace ℝ (Fin 3)} {d : ℝ} (hd : d ≠ 0)
    (hp₀ : ∀ i, ‖p i - p₀‖ = d) (hpp : ∀ i j, i ≠ j → ‖p i - p j‖ = d) :
    (Fintype.card ι + 1) * Fintype.card ι ≤ 12 := by
  have hcard : Fintype.card ι ≤ 3 :=
    equidistant_card_le_three_in_R3 hd hp₀ hpp
  nlinarith

end QOU.Mass.EquilateralBound
