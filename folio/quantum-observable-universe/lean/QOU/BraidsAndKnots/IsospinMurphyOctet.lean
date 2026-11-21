import QOU.BraidsAndKnots.StrangeStrandOctet

/-!
# Weighted Jucys–Murphy sums on the flavour strands

Second Jucys–Murphy element on two strands, `L₂ = Ř²`, for the level-`n` Jimbo braiding
`Ř = jimbo n q` of `StrangeStrandOctet` (`h = q - q⁻¹`).

## Results

1. `murphy2_diag`: the diagonal of `L₂` is `q²` on `eᵢ ⊗ eᵢ`, `1` on `eᵢ ⊗ eⱼ` with `i < j`, and
   `1 + h²` on `eᵢ ⊗ eⱼ` with `j < i`. So `L₂` sees the order of the two flavours.
2. `murphy2_pair_trace`: on `{eᵢ ⊗ eⱼ, eⱼ ⊗ eᵢ}` the trace of `L₂` is `2 + h²` for every pair
   of distinct flavours. A flavour-blind weight cannot split flavour pairs.
3. `weightedMurphy2_pair_trace`: with a flavour weight `w`, `w₁ L₁ + w₂ L₂` has trace
   `2 (wᵢ + wⱼ) + wᵢ h²` on that weight space. The `h²` term is position-sensitive.

Context (exact computation only, not in this file; probe
`computations/flavour_strange_strand/murphy_octet_probe.py`): on three strands, the hypercharge
weight `Y = (1/3, 1/3, -2/3)` gives zero splitting inside every octet isospin pair (it does not
distinguish `u` from `d`). The isospin weight `I₃ = (1/2, -1/2, 0)`, and hence the charge weight
`Q = I₃ + Y/2`, gives octet splittings that satisfy the Coleman–Glashow relation
`Σ = N + Ξ` exactly in `q`, with the position-sensitive coefficient
`α₂/α₁ = (2/3)(q - 1) + O((q - 1)²)`.

No numerical value enters.
-/

namespace QOU.BraidsAndKnots.IsospinMurphyOctet
open Matrix QOU.BraidsAndKnots.StrangeStrandOctet
variable {R : Type*} [Field R]

/-- The second Jucys–Murphy element on two strands, `L₂ = Ř²`. -/
def murphy2 (n : ℕ) (q : R) : Matrix (Fin n × Fin n) (Fin n × Fin n) R := jimbo n q * jimbo n q

theorem murphy2_diag {n : ℕ} (q : R) (x : Fin n × Fin n) :
    murphy2 n q x x =
      if x.1 = x.2 then q ^ 2 else if x.1 < x.2 then 1 else 1 + (q - q⁻¹) ^ 2 := by
  obtain ⟨i, j⟩ := x
  unfold murphy2
  rw [Matrix.mul_apply]
  by_cases hij : i = j
  · subst hij
    rw [Finset.sum_eq_single (i, i)]
    · simp [jimbo, sq]
    · intro z _ hz
      have : jimbo n q z (i, i) = 0 := by simp [jimbo, hz]
      simp [this]
    · simp
  · have hne : (i, j) ≠ (j, i) := by simp [hij]
    rw [Finset.sum_eq_add (i, j) (j, i) hne]
    · rcases lt_or_gt_of_ne hij with h | h
      · simp [jimbo, hij, Ne.symm hij, h, not_lt.mpr h.le]
      · simp [jimbo, hij, Ne.symm hij, h, not_lt.mpr h.le, sq]; ring
    · intro z _ hz
      have : jimbo n q z (i, j) = 0 := by
        by_contra hc
        rcases jimbo_entry_ne_zero q z (i, j) hc with e | e
        · exact hz.1 e
        · exact hz.2 e
      simp [this]
    · simp
    · simp

/-- On the two-strand weight space `{eᵢ ⊗ eⱼ, eⱼ ⊗ eᵢ}` (`i < j`) the trace of `L₂` is
`2 + h²`, the same for every pair of distinct flavours. So a flavour-blind weighting of `L₂`
cannot tell flavour pairs apart. -/
theorem murphy2_pair_trace {n : ℕ} (q : R) {i j : Fin n} (h : i < j) :
    murphy2 n q (i, j) (i, j) + murphy2 n q (j, i) (j, i) = 2 + (q - q⁻¹) ^ 2 := by
  rw [murphy2_diag, murphy2_diag]
  simp [h.ne, h.ne', h, not_lt.mpr h.le]
  ring

/-- **Weighted Murphy sum on two strands.** With a flavour weight `w` on each strand,
`M_w = w₁ · L₁ + w₂ · L₂` (`L₁ = 1`, `L₂ = Ř²`) has trace on `{eᵢ ⊗ eⱼ, eⱼ ⊗ eᵢ}`, `i < j`,
equal to `2 (wᵢ + wⱼ) + wᵢ · h²`. The `h²` term carries the weight of the flavour that comes
first in the order: the sum is sensitive to which flavour sits where. -/
theorem weightedMurphy2_pair_trace {n : ℕ} (q : R) (w : Fin n → R) {i j : Fin n} (h : i < j) :
    (w i + w j * murphy2 n q (i, j) (i, j)) + (w j + w i * murphy2 n q (j, i) (j, i)) =
      2 * (w i + w j) + w i * (q - q⁻¹) ^ 2 := by
  rw [murphy2_diag, murphy2_diag]
  simp [h.ne, h.ne', h, not_lt.mpr h.le]
  ring

end QOU.BraidsAndKnots.IsospinMurphyOctet
