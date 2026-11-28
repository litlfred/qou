import QOU.SchurWeyl.SpinSectorMeasure
import QOU.SchurWeyl.MarkovConventionD

/-!
# The mass as a sum over spin sectors

At convention D the Markov trace on `H_n(q)` is `tr = ∑_{|ν| = n} W_ν · χ^ν` with
`W = ocneanuWeight q z_D`, and the framed mass of `def:mass-identity` is
`𝔪(β) = [2]ⁿ · q^{−2w(β)} · tr(β)`. This file proves the **sector formula**

`𝔪(β) = q^{−2w(β)} · ∑_{k} [n − 2k + 1]_q · χ^{(n−k,k)}(β)`,

in the denominator-free form: for every diagram `ν` of size `n` (`sector_weight`)

`[2]ⁿ · (q − q⁻¹) · W_ν = q^{d+1} − q^{−(d+1)}` if `ν = (n − k, k)` has at most two rows,
`d = n − 2k`, and `0` if `ν` has a third row;

and summed against any class function `χ` over any finite set of diagrams of size `n`
(`sector_formula`). Multiplying by `q^{−2w}` and dividing by `q − q⁻¹` gives the displayed formula.

It combines `SpinSector.ocneanuWeight_twoRow_conventionD` (two-row weights), the convention-D
vanishing `ocneanuWeight_conventionD_eq_zero_of_three_rows`, and
`eq_twoRow_of_rowLen_two_eq_zero` (a diagram with an empty third row is a `twoRow`).

What this rests on: "the Markov trace is `∑ W_ν χ^ν`" uses Ocneanu/Jones uniqueness, and reading
the summands as spin sectors uses quantum Schur–Weyl duality (G3.4); see `SpinSectorMeasure`.
Neither is used in the proofs below, which are identities between explicit expressions.

Bean `qou-078y`. Base ring (§7c): generic `[Field K]`, no ordering.
-/

namespace QOU.SchurWeyl.SpinSector

open Finset QOU.SchurWeyl

variable {K : Type*} [Field K]

/-- **Per-diagram sector weight at convention D.** -/
theorem sector_weight (q : K) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1) (ν : YoungDiagram) :
    (q + q⁻¹) ^ ν.cells.card * (q - q⁻¹) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν
      = if ν.rowLen 2 = 0 then
          q ^ (ν.rowLen 0 - ν.rowLen 1 + 1) - q⁻¹ ^ (ν.rowLen 0 - ν.rowLen 1 + 1)
        else 0 := by
  by_cases h2 : ν.rowLen 2 = 0
  · rw [if_pos h2]
    obtain ⟨m, k, hkm, rfl⟩ : ∃ m k, ∃ h : k ≤ m, ν = twoRow m k h :=
      ⟨_, _, _, eq_twoRow_of_rowLen_two_eq_zero ν h2⟩
    rw [rowLen_twoRow_zero, rowLen_twoRow_one, card_twoRow,
      ← ocneanuWeight_twoRow_conventionD q hq hq21 hgen hkm]
    ring
  · rw [if_neg h2,
      ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 ν (Nat.pos_of_ne_zero h2), mul_zero]

/-- **The sector formula.** For any finite set of diagrams of size `n` and any `χ`,
`[2]ⁿ (q − q⁻¹) ∑ W_ν χ_ν = ∑_{two-row ν} (q^{d+1} − q^{−(d+1)}) χ_ν`. -/
theorem sector_formula (q : K) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1) (n : ℕ) (S : Finset YoungDiagram)
    (hS : ∀ ν ∈ S, ν.cells.card = n) (χ : YoungDiagram → K) :
    (q + q⁻¹) ^ n * (q - q⁻¹) * ∑ ν ∈ S, ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν * χ ν
      = ∑ ν ∈ S.filter (fun ν => ν.rowLen 2 = 0),
          (q ^ (ν.rowLen 0 - ν.rowLen 1 + 1) - q⁻¹ ^ (ν.rowLen 0 - ν.rowLen 1 + 1)) * χ ν := by
  rw [Finset.mul_sum, Finset.sum_filter]
  refine Finset.sum_congr rfl fun ν hν => ?_
  have hw := sector_weight q hq hq21 hgen ν
  rw [hS ν hν] at hw
  split_ifs with h2
  · rw [if_pos h2] at hw
    rw [← hw]; ring
  · rw [if_neg h2] at hw
    rw [← mul_assoc, hw, zero_mul]

end QOU.SchurWeyl.SpinSector
