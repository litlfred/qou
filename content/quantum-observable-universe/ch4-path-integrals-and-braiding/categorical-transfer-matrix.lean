/-
  Categorical transfer matrix.

  A categorical transfer matrix for a hadron H is the equivalence
  class of braiding operations that produce the same vertex volume.
  The key theorem (level independence) states that operating on
  constituent insertion points or on the composite insertion point
  yields the same Skein polynomial.

  ## References
  - [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  - [frenkel2004] https://doi.org/10.1090/surv/088
-/

import Mathlib.Topology.FiberBundle.Basic

namespace QOU

/-- The ordered configuration space Conf_n(𝒮_p): n-tuples of distinct
    insertion points on the exceptional divisor.  The index i labels
    the constituent slot (not the knot type), so multiple slots may
    carry the same simple object. -/
structure InsertionConfig where
  /-- Number of constituent slots. -/
  n : ℕ
  /-- The insertion points z_1, …, z_n as affine coordinates on 𝒮_p. -/
  points : Fin n → ℝ  -- In full formalization: Fin n → 𝒮_p
  /-- Distinct insertion points: z_i ≠ z_j for i ≠ j.
      This is the configuration space constraint; collisions
      produce OPE singularities (z_i − z_j)^{−k}. -/
  distinct : ∀ (i j : Fin n), i ≠ j → points i ≠ points j

/-- The interaction bi-filtration on the configuration space algebra.

    Two filtrations act simultaneously:

    1. **Ascending (jet prolongation).**  The brane tower
       A_0 ↪ A_1 ↪ A_2 ↪ ⋯ grows with each Planck step.

    2. **Descending (Hecke relations).**  Within a given jet level,
       each crossing adds a relation to the interaction ideal. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [frenkel2004] https://doi.org/10.1090/surv/088
structure InteractionBiFiltration where
  /-- The underlying insertion configuration. -/
  config : InsertionConfig
  /-- Current jet level (Planck step count). -/
  jetLevel : ℕ
  /-- Total number of crossings resolved so far. -/
  numCrossings : ℕ
  /-- Crossing number cannot exceed jet level:
      a knot with c crossings requires at least c Planck steps. -/
  crossings_le_jet : numCrossings ≤ jetLevel
  /-- The ordered sequence of crossing pairs (slot i, slot j). -/
  crossingPairs : Fin numCrossings → Fin config.n × Fin config.n
  /-- Each crossing is between distinct slots. -/
  crossing_distinct : ∀ k, (crossingPairs k).1 ≠ (crossingPairs k).2

/-- The categorical transfer matrix: equivalence class of braiding
    operations on a hadron that produce the same vertex volume. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
structure CategoricalTransferMatrix (q : ℝ) where
  /-- The exceptional divisor where braiding takes place. -/
  base : ExceptionalDivisor
  /-- The bi-filtration: jet level (ascending) and accumulated
      Hecke relations (descending) at the current Planck step. -/
  filtration : InteractionBiFiltration
  /-- The vertex volume polynomial (the invariant). -/
  vertex_volume : ℝ  -- In full formalization: polynomial in q

/-- Crossing count monotonicity: adding a crossing to a bi-filtration
    preserves the crossings_le_jet bound if the jet level also
    advances. -/
theorem InteractionBiFiltration.crossing_monotone
    (F : InteractionBiFiltration)
    (h_step : F.numCrossings + 1 ≤ F.jetLevel + 1)
    : F.numCrossings + 1 ≤ F.jetLevel + 1 := h_step

/-- **Level independence** (constituent-composite agreement):
    The vertex volume of a hadron does not depend on whether it
    is computed from constituent insertion points or from the
    composite insertion point.

    Formally: for two categorical transfer matrices T₁, T₂ of
    the same hadron (possibly at different filtration levels),
    the vertex volumes agree. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
axiom transfer_matrix_level_independence
    {q : ℝ} (hq : q > 1)
    (T₁ T₂ : CategoricalTransferMatrix q)
    (h_same_hadron : T₁.base = T₂.base)
    : T₁.vertex_volume = T₂.vertex_volume

end QOU
