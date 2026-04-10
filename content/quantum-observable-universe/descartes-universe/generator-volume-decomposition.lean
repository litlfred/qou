/-!
# QOU.Descartes.generator_volume_decomposition — Nuclear energy as sum of generator volumes

E = Σ_i V_i where V_i = |a_i| + |b_i| is the Hecke-reduced weight
at generator σ_i. The (a_i, b_i) follow a 2×2 transfer matrix
recurrence. O(A²) computation.

LaTeX label: `prop:generator-volume-decomposition`

## References
- [manuscript] §6/generator-volume-decomposition

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic

namespace QOU.Descartes

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The transfer matrix step: multiply (a σ + b)(c σ + d) and reduce
    via σ² = (q-q⁻¹)σ + 1 to get (a', b'). -/
-- Ref: [manuscript] §6/generator-volume-decomposition
noncomputable def transferStep (q : R_q) (a b c d : R_q) : R_q × R_q :=
  (a * c * (q - 1/q) + a * d + b * c, a * c + b * d)

/-- The generator volume: V_i = |a_i| + |b_i| after reducing all
    crossings at generator σ_i. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
noncomputable def generatorVolume (a b : R_q) : R_q :=
  |a| + |b|

/-- The generator volume is non-negative. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
theorem generatorVolume_nonneg (a b : R_q) :
    0 ≤ generatorVolume a b := by
  unfold generatorVolume
  positivity

/-- The total nuclear energy is the sum of generator volumes. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
noncomputable def nuclearEnergy (volumes : List R_q) : R_q :=
  volumes.sum

/-- The ideal volume at generator i: the energy absorbed by
    Hecke reduction. V_i^I = k_i - V_i where k_i is the number
    of crossings at generator i. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
noncomputable def idealVolume (k_i : ℕ) (V_i : R_q) : R_q :=
  k_i - V_i

/-- Crossing coefficients for proton-proton pair: (1, 0). -/
-- Ref: [manuscript] §6/generator-volume-decomposition
def crossingPP : R_q × R_q := (1, 0)

/-- Crossing coefficients for neutron-neutron pair. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
noncomputable def crossingNN (q : R_q) : R_q × R_q :=
  (q^2, -q * (q ^ (1/2 : R_q) - q ^ (-(1/2 : R_q))))

/-- Crossing coefficients for proton-neutron (mixed) pair. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
noncomputable def crossingMixed (q : R_q) : R_q × R_q :=
  ((1 + q^2) / 2, -q * (q ^ (1/2 : R_q) - q ^ (-(1/2 : R_q))) / 2)

/-- The chain reduction at one generator: start with (0, 1) (identity),
    multiply by each crossing's coefficients, reduce via transfer step. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
noncomputable def chainReduce (q : R_q) (crossings : List (R_q × R_q)) : R_q × R_q :=
  crossings.foldl (fun ⟨a, b⟩ ⟨c, d⟩ => transferStep q a b c d) (0, 1)

/-- The energy is additive over generators. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
theorem energy_additive (vols : List R_q) :
    nuclearEnergy vols = vols.sum := by
  rfl

/-- Only generators i ≤ p are affected by beta decay (the rest cancel
    between parent and daughter). -/
-- Ref: [manuscript] §6/generator-volume-decomposition
theorem beta_decay_locality (p : ℕ) (vols_par vols_dau : List R_q)
    (h_len : vols_par.length = vols_dau.length)
    (h_tail : ∀ i, p < i → i < vols_par.length →
      vols_par[i]! = vols_dau[i]!) :
    -- The energy difference comes only from generators 0..p
    nuclearEnergy vols_par - nuclearEnergy vols_dau =
      nuclearEnergy (vols_par.take (p + 1)) - nuclearEnergy (vols_dau.take (p + 1)) := by
  -- Ref: [manuscript] Ch. 6, §generator-volume-decomposition
  -- Generators i > p have identical volumes, so they cancel in the difference.
  -- Strategy: decompose each list as take (p+1) ++ drop (p+1), use sum_append,
  -- then show the drop-sums are equal so they cancel in the subtraction.
  unfold nuclearEnergy
  -- Rewrite each sum via take_append_drop: l = l.take n ++ l.drop n
  conv_lhs =>
    rw [show vols_par = vols_par.take (p + 1) ++ vols_par.drop (p + 1)
        from (List.take_append_drop (p + 1) vols_par).symm,
        show vols_dau = vols_dau.take (p + 1) ++ vols_dau.drop (p + 1)
        from (List.take_append_drop (p + 1) vols_dau).symm]
  rw [List.sum_append, List.sum_append]
  -- Suffices to show drop_sum_par = drop_sum_dau, then linarith cancels them.
  suffices h_drop : (vols_par.drop (p + 1)).sum = (vols_dau.drop (p + 1)).sum by linarith
  -- Show the two drop lists are actually equal (hence equal sums).
  congr 1
  apply List.ext_getElem
  · simp [List.length_drop, h_len]
  · intro i h₁ h₂
    simp only [List.getElem_drop]
    have h_bound₁ : p + 1 + i < vols_par.length := by
      simp [List.length_drop] at h₁; omega
    have h_bound₂ : p + 1 + i < vols_dau.length := by
      simp [List.length_drop] at h₂; omega
    have h₃ := h_tail (p + 1 + i) (by omega) h_bound₁
    rwa [getElem!_pos h_bound₁, getElem!_pos h_bound₂] at h₃

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [manuscript] §6/generator-volume-decomposition
noncomputable def generator_volume_decomposition (q : R_q)
    (crossings_per_gen : List (List (R_q × R_q))) : R_q :=
  let volumes := crossings_per_gen.map fun cs =>
    let ⟨a, b⟩ := chainReduce q cs
    generatorVolume a b
  nuclearEnergy volumes

end QOU.Descartes
