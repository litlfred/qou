/-
  The 3D-realizability cap on max-contact coordination.

  Context (arc: bk-crossing mass-binding; beans `qou-vibo` / `qou-brng`).
  `QOU.Mass.CoordinationSaturation` proves the dichotomy — the complete graph
  `K_A` cannot saturate (`complete_graph_no_saturation`), a bounded-degree
  coordination does (`bounded_degree_saturates`) — but it selects between them
  using an EMPIRICAL premise: the audit's reasoning is "the complete-graph
  coordination cannot saturate; saturation is *observed*; therefore the complete
  graph is excluded for heavy `A`".

  This file removes the empirical step for the max-contact regime. A max-contact
  cluster is one in which every pair of nucleons is bonded at the SAME bond
  distance `d` — i.e. the centres are pairwise equidistant. In a Euclidean space
  of dimension 3 there are at most 4 such points, so the complete contact graph
  is 3D-realizable only for `A ≤ 4`. The prose form of this ("a tetrahedron is
  the largest all-mutually-adjacent point set in ℝ³") is already in
  `docs/audits/2026-07-11-bk-coordination-degree-and-alpha-contact.md`; that
  audit filed the Lean as a follow-up it could not build in-sandbox. This is
  that follow-up.

  What is proved here is the GEOMETRY, not the physics: that a pairwise-equidistant
  family in a rank-`n` inner-product space has at most `n + 1` members. Reading
  the max-contact cluster as such a family is a modelling step, stated in the
  audit and NOT claimed here as derived.

  Base ring (§7c): `ℝ` is required — this is an archimedean statement (norms,
  an inner product, positivity of a sum of squares).
-/
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas

namespace QOU.Mass

open Finset RealInnerProductSpace

variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]

/-- **The Gram identity for an equidistant family.**

If `v : Fin n → V` has `⟪v i, v j⟫ = (d²/2)·(1 + δᵢⱼ)` — which is exactly the
Gram matrix of the difference vectors `pᵢ − p₀` of a pairwise-equidistant point
family at common distance `d` — then for any coefficients `c`,

    ‖Σ cᵢ vᵢ‖²  =  (d²/2) · ( (Σ cᵢ)² + Σ cᵢ² ).

Both bracketed terms are squares, which is what forces independence below. -/
theorem inner_self_sum_of_equidistant_gram
    {n : ℕ} (v : Fin n → V) (d : ℝ)
    (hg : ∀ i j, ⟪v i, v j⟫ = (d ^ 2 / 2) * (1 + if i = j then 1 else 0))
    (c : Fin n → ℝ) :
    ⟪∑ i, c i • v i, ∑ i, c i • v i⟫
      = (d ^ 2 / 2) * ((∑ i, c i) ^ 2 + ∑ i, c i ^ 2) := by
  -- Expand the double sum, then substitute the Gram hypothesis.
  have expand : ⟪∑ i, c i • v i, ∑ j, c j • v j⟫
      = ∑ i, ∑ j, c i * c j * ⟪v i, v j⟫ := by
    simp only [sum_inner, inner_sum, real_inner_smul_left, real_inner_smul_right,
      mul_assoc]
    exact Finset.sum_congr rfl fun i _ =>
      Finset.sum_congr rfl fun j _ => by rw [real_inner_comm]
  rw [expand]
  -- Per-row: the `1` gives `c i * Σ c`, the Kronecker `δ` gives `c i * c i`.
  have row : ∀ i : Fin n,
      (∑ j, c i * c j * ⟪v i, v j⟫)
        = (d ^ 2 / 2) * (c i * (∑ j, c j)) + (d ^ 2 / 2) * (c i * c i) := by
    intro i
    have hterm : ∀ j : Fin n, c i * c j * ⟪v i, v j⟫
        = (d ^ 2 / 2) * (c i * c j)
          + (d ^ 2 / 2) * (if i = j then c i * c j else 0) := by
      intro j
      rw [hg i j]
      by_cases h : i = j <;> simp [h] <;> ring
    rw [Finset.sum_congr rfl (fun j _ => hterm j), Finset.sum_add_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum]
    simp [Finset.sum_ite_eq]
  rw [Finset.sum_congr rfl (fun i _ => row i), Finset.sum_add_distrib,
    ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.sum_mul]
  have hsq : ∀ i : Fin n, c i * c i = c i ^ 2 := fun i => by ring
  rw [Finset.sum_congr rfl (fun i _ => hsq i)]
  ring

/-- **Equidistant ⇒ linearly independent.**

The difference vectors of a pairwise-equidistant point family (common distance
`d ≠ 0`) are linearly independent: `‖Σ cᵢ vᵢ‖²` is `(d²/2)` times a sum of two
squares, so it vanishes only when every `cᵢ` does. -/
theorem linearIndependent_of_equidistant_gram
    {n : ℕ} (v : Fin n → V) (d : ℝ) (hd : d ≠ 0)
    (hg : ∀ i j, ⟪v i, v j⟫ = (d ^ 2 / 2) * (1 + if i = j then 1 else 0)) :
    LinearIndependent ℝ v := by
  rw [Fintype.linearIndependent_iff]
  intro c hc
  have hzero : ⟪∑ i, c i • v i, ∑ i, c i • v i⟫ = 0 := by rw [hc]; simp
  rw [inner_self_sum_of_equidistant_gram v d hg c] at hzero
  have hd2 : (d ^ 2 / 2) ≠ 0 := by positivity
  have hsum : (∑ i, c i) ^ 2 + ∑ i, c i ^ 2 = 0 := by
    rcases mul_eq_zero.mp hzero with h | h
    · exact absurd h hd2
    · exact h
  have hnn : (0 : ℝ) ≤ (∑ i, c i) ^ 2 := sq_nonneg _
  have hnn2 : (0 : ℝ) ≤ ∑ i, c i ^ 2 :=
    Finset.sum_nonneg fun i _ => sq_nonneg _
  have hsq : ∑ i, c i ^ 2 = 0 := by linarith
  intro i
  have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (c j))).mp hsq i
    (Finset.mem_univ i)
  exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this

/-- **The cap.** A pairwise-equidistant family of difference vectors in a space
of finite rank `r` has at most `r` members — so a max-contact cluster of `A`
nucleons (whose `A − 1` difference vectors are such a family) satisfies
`A - 1 ≤ r`. In `r = 3` this is `A ≤ 4`: the tetrahedron is the largest
all-mutually-adjacent point set in ℝ³, and the complete contact graph `K_A` is
**not 3D-realizable for `A ≥ 5`**. -/
theorem equidistant_card_le_finrank
    [Module.Finite ℝ V] {n : ℕ} (v : Fin n → V) (d : ℝ) (hd : d ≠ 0)
    (hg : ∀ i j, ⟪v i, v j⟫ = (d ^ 2 / 2) * (1 + if i = j then 1 else 0)) :
    n ≤ Module.finrank ℝ V := by
  have hli : LinearIndependent ℝ v := linearIndependent_of_equidistant_gram v d hd hg
  simpa using hli.fintype_card_le_finrank

end QOU.Mass
