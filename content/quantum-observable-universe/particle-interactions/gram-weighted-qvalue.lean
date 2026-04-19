/-
  Gram-weighted Q-value from Frobenius norm of conversion channels.

  Q = (Σ_k w_k^G × Δ_k) × N × m_e

  where w_k^G is the normalised Frobenius norm of the difference
  between parent and k-th daughter typed Garside elements.

  Ref: [manuscript] §6.3c, Proposition prop:gram-weighted-qvalue
-/

import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.BilinearForm.Basic

namespace QOU.Descartes

/-- The Gram matrix G_{ij} = tr_M(b_i · b_j) of the Iwahori-Hecke
    algebra restricted to a finite-dimensional NF subspace. -/
-- Ref: [manuscript] Proposition prop:frobenius-gram-matrix
structure GramMatrix (n : ℕ) where
  entries : Fin n → Fin n → ℝ
  symmetric : ∀ i j, entries i j = entries j i

/-- The Frobenius norm squared of a vector v with respect to Gram matrix G:
    ||v||²_F = v · G · v = Σ_{ij} v_i G_{ij} v_j -/
noncomputable def frobeniusNormSq {n : ℕ} (G : GramMatrix n) (v : Fin n → ℝ) : ℝ :=
  ∑ i, ∑ j, v i * G.entries i j * v j

/-- The Frobenius norm: ||v||_F = √|v · G · v|. -/
noncomputable def frobeniusNorm {n : ℕ} (G : GramMatrix n) (v : Fin n → ℝ) : ℝ :=
  Real.sqrt (|frobeniusNormSq G v|)

/-- The NF reduction cost Δ_k: change in L1 norm when neutron k converts.
    Δ_k = ||N_par||₁ - ||N_dau^(k)||₁ -/
-- Ref: [manuscript] Equation eq:nf-reduction-cost
noncomputable def nfReductionCost
    (parentL1 : ℝ) (daughterL1 : ℝ) : ℝ :=
  parentL1 - daughterL1

/-- The Gram weight for neutron k:
    w_k^G = ||δ_k||_F / Σ_j ||δ_j||_F -/
-- Ref: [manuscript] Equation eq:gram-weight
noncomputable def gramWeight {n N : ℕ}
    (G : GramMatrix n)
    (deltas : Fin N → (Fin n → ℝ)) -- δ_k for each neutron
    (k : Fin N) : ℝ :=
  let norms := fun j => frobeniusNorm G (deltas j)
  let total := ∑ j, norms j
  if total = 0 then 1 / N else norms k / total

/-- The Gram-weighted Q-value:
    Q = (Σ_k w_k^G × Δ_k) × N × m_e -/
-- Ref: [manuscript] Equation eq:gram-weighted-qvalue
noncomputable def gramWeightedQ {n : ℕ}
    (G : GramMatrix n)
    (N : ℕ) -- number of neutrons
    (deltas : Fin N → (Fin n → ℝ)) -- δ_k vectors
    (costs : Fin N → ℝ) -- Δ_k reduction costs
    (m_e : ℝ) : ℝ :=
  (∑ k, gramWeight G deltas k * costs k) * N * m_e

/-- The Gram weight is a probability distribution: Σ_k w_k = 1. -/
theorem gramWeight_sum_one {n N : ℕ} (hN : 0 < N)
    (G : GramMatrix n)
    (deltas : Fin N → (Fin n → ℝ))
    (h_nonzero : ∑ j, frobeniusNorm G (deltas j) ≠ 0) :
    ∑ k, gramWeight G deltas k = 1 := by
  -- Ref: [manuscript] Proposition prop:gram-weighted-qvalue
  sorry

/-- Each Gram weight is non-negative: w_k ≥ 0. -/
theorem gramWeight_nonneg {n N : ℕ}
    (G : GramMatrix n)
    (deltas : Fin N → (Fin n → ℝ))
    (k : Fin N) :
    0 ≤ gramWeight G deltas k := by
  -- Ref: [manuscript] Proposition prop:gram-weighted-qvalue
  -- Follows from frobeniusNorm ≥ 0 (it's a sqrt of |·|)
  sorry

/-- If all δ_k have the same Frobenius norm, the weights are uniform:
    w_k = 1/N for all k. -/
theorem gramWeight_uniform_when_equal {n N : ℕ} (hN : 0 < N)
    (G : GramMatrix n)
    (deltas : Fin N → (Fin n → ℝ))
    (h_equal : ∀ j k, frobeniusNorm G (deltas j) = frobeniusNorm G (deltas k)) :
    ∀ k, gramWeight G deltas k = 1 / N := by
  -- Ref: [manuscript] Proposition prop:gram-weighted-qvalue
  -- When all norms equal, the normalisation gives 1/N each.
  sorry


/-- **prop:gram-weighted-qvalue** — placeholder stub; full proof TBD. -/
theorem gram_weighted_qvalue : ∃ (witness : ℝ), 0 < witness := by
  -- Ref: [manuscript] §particle-interactions/gram-weighted-qvalue
  sorry
end QOU.Descartes
