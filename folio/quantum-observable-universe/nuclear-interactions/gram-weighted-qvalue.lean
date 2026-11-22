/-
  Gram-weighted Q-value from Frobenius norm of conversion channels.

  Q = (Σ_k w_k^G × Δ_k) × N × m_e

  where w_k^G is the normalised Frobenius norm of the difference
  between parent and k-th daughter typed Garside elements.

  Ref: [leitner2026] §6.3c, Proposition prop:gram-weighted-qvalue
-/

import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.BilinearForm.Basic

namespace QOU.Archimedean

/-- The Gram matrix G_{ij} = tr_M(b_i · b_j) of the Iwahori-Hecke
    algebra restricted to a finite-dimensional NF subspace. -/
-- Ref: [leitner2026] Proposition prop:frobenius-gram-matrix
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
-- Ref: [leitner2026] Equation eq:nf-reduction-cost
noncomputable def nfReductionCost
    (parentL1 : ℝ) (daughterL1 : ℝ) : ℝ :=
  parentL1 - daughterL1

/-- The Gram weight for neutron k:
    w_k^G = ||δ_k||_F / Σ_j ||δ_j||_F -/
-- Ref: [leitner2026] Equation eq:gram-weight
noncomputable def gramWeight {n N : ℕ}
    (G : GramMatrix n)
    (deltas : Fin N → (Fin n → ℝ)) -- δ_k for each neutron
    (k : Fin N) : ℝ :=
  let norms := fun j => frobeniusNorm G (deltas j)
  let total := ∑ j, norms j
  if total = 0 then 1 / N else norms k / total

/-- The Gram-weighted Q-value:
    Q = (Σ_k w_k^G × Δ_k) × N × m_e -/
-- Ref: [leitner2026] Equation eq:gram-weighted-qvalue
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
  -- Ref: [leitner2026] Proposition prop:gram-weighted-qvalue
  -- Each weight = norms k / total (else-branch since total ≠ 0);
  -- summing gives (Σ norms) / total = total / total = 1.
  simp only [gramWeight, if_neg h_nonzero]
  rw [← Finset.sum_div]
  exact div_self h_nonzero

/-- Each Gram weight is non-negative: w_k ≥ 0. -/
theorem gramWeight_nonneg {n N : ℕ}
    (G : GramMatrix n)
    (deltas : Fin N → (Fin n → ℝ))
    (k : Fin N) :
    0 ≤ gramWeight G deltas k := by
  -- Ref: [leitner2026] Proposition prop:gram-weighted-qvalue
  -- frobeniusNorm = √|·| ≥ 0; sum of nonneg ≥ 0; ratio of nonneg ≥ 0.
  simp only [gramWeight]
  split_ifs with h
  · positivity
  · apply div_nonneg
    · unfold frobeniusNorm
      exact Real.sqrt_nonneg _
    · apply Finset.sum_nonneg
      intro j _
      unfold frobeniusNorm
      exact Real.sqrt_nonneg _

/-- If all δ_k have the same Frobenius norm, the weights are uniform:
    w_k = 1/N for all k. -/
theorem gramWeight_uniform_when_equal {n N : ℕ} (hN : 0 < N)
    (G : GramMatrix n)
    (deltas : Fin N → (Fin n → ℝ))
    (h_equal : ∀ j k, frobeniusNorm G (deltas j) = frobeniusNorm G (deltas k)) :
    ∀ k, gramWeight G deltas k = 1 / N := by
  -- Ref: [leitner2026] Proposition prop:gram-weighted-qvalue
  intro k
  simp only [gramWeight]
  -- Every j-th norm equals the k-th norm.
  have h_const : (fun j : Fin N => frobeniusNorm G (deltas j)) =
      fun _ => frobeniusNorm G (deltas k) := funext (fun j => h_equal j k)
  -- Sum collapses to N * (frobeniusNorm G (deltas k)).
  have h_total : (∑ j, frobeniusNorm G (deltas j))
      = (N : ℝ) * frobeniusNorm G (deltas k) := by
    rw [h_const]
    simp [Finset.sum_const, Finset.card_univ, Fintype.card_fin, mul_comm]
  rw [h_total]
  by_cases h_zero : frobeniusNorm G (deltas k) = 0
  · -- All norms 0: total = 0, the if-branch gives 1/N directly.
    simp [h_zero]
  · -- Nonzero norm: total = N · norm ≠ 0; ratio = 1/N.
    have hN' : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.pos_iff_ne_zero.mp hN)
    have h_total_nz : (N : ℝ) * frobeniusNorm G (deltas k) ≠ 0 :=
      mul_ne_zero hN' h_zero
    rw [if_neg h_total_nz]
    field_simp

end QOU.Archimedean
