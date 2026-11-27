/-
  Nearness from a Gram matrix: the Schoenberg distance is a Euclidean metric.

  Owner's question (issue #7895): with no background spacetime, "nearness" of
  two states has to come from the interaction data.  An SDP solution is a
  positive-semidefinite Gram matrix `G i j = ⟪v i, v j⟫`, and the natural
  distance it carries is

      d(i, j)² = G i i + G j j − 2 G i j .

  This file proves that this IS the Euclidean distance between the realising
  vectors, hence a pseudometric (symmetric, zero on the diagonal, triangle
  inequality), and that `d(i, j) = 0` exactly when the two states have the same
  vector — for a trace form, exactly when they differ by an element of the
  radical, which is why the radical must be quotiented away
  (`prop:gram-degeneracy-blocks-connes`).

  Every real PSD matrix is a Gram matrix of vectors in `ℝ^rank` (spectral /
  Cholesky factorisation), so working with the vectors loses nothing; the
  embedding dimension is the rank of `G`.

  Archimedean (ℝ): real inner product spaces.
-/
import Mathlib.Analysis.InnerProductSpace.Basic

namespace QOU.Optimization.GramNearness

open RealInnerProductSpace

variable {ι E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The Gram matrix of a family of vectors. -/
noncomputable def gram (v : ι → E) (i j : ι) : ℝ := ⟪v i, v j⟫

/-- The Schoenberg squared distance read off the Gram matrix. -/
noncomputable def gramDistSq (v : ι → E) (i j : ι) : ℝ :=
  gram v i i + gram v j j - 2 * gram v i j

/-- **The Gram distance is the Euclidean distance** of the realising vectors. -/
theorem gramDistSq_eq (v : ι → E) (i j : ι) :
    gramDistSq v i j = ‖v i - v j‖ ^ 2 := by
  unfold gramDistSq gram
  rw [@norm_sub_sq_real, real_inner_self_eq_norm_sq, real_inner_self_eq_norm_sq]
  ring

theorem gramDistSq_nonneg (v : ι → E) (i j : ι) : 0 ≤ gramDistSq v i j := by
  rw [gramDistSq_eq]; positivity

/-- The distance itself. -/
noncomputable def gramDist (v : ι → E) (i j : ι) : ℝ := Real.sqrt (gramDistSq v i j)

theorem gramDist_eq_norm (v : ι → E) (i j : ι) : gramDist v i j = ‖v i - v j‖ := by
  unfold gramDist
  rw [gramDistSq_eq, Real.sqrt_sq (norm_nonneg _)]

theorem gramDist_self (v : ι → E) (i : ι) : gramDist v i i = 0 := by
  rw [gramDist_eq_norm, sub_self, norm_zero]

theorem gramDist_comm (v : ι → E) (i j : ι) : gramDist v i j = gramDist v j i := by
  rw [gramDist_eq_norm, gramDist_eq_norm, norm_sub_rev]

/-- **Triangle inequality.** -/
theorem gramDist_triangle (v : ι → E) (i j k : ι) :
    gramDist v i k ≤ gramDist v i j + gramDist v j k := by
  rw [gramDist_eq_norm, gramDist_eq_norm, gramDist_eq_norm]
  exact norm_sub_le_norm_sub_add_norm_sub _ _ _

/-- **Zero distance means the same point**: two states are indistinguishable
exactly when their Gram vectors coincide (for a trace form: they differ by a
radical element). -/
theorem gramDist_eq_zero_iff (v : ι → E) (i j : ι) : gramDist v i j = 0 ↔ v i = v j := by
  rw [gramDist_eq_norm, norm_eq_zero, sub_eq_zero]

end QOU.Optimization.GramNearness
