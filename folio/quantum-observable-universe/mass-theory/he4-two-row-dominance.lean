/-
He-4 two-row stratum dominance and exact convention-D support.

LaTeX label:        prop:he4-two-row-dominance
Computational ref:  computations/probe_he4_canonical_tr_m_fingerprint.py
Witness:            computations/he4-canonical-tr-m-block-fingerprint.witness.json
Audit:              docs/audits/2026-05-15-three-pr-integration.md §F1 ⁴He

For β_{⁴He} = canonical atomic braid word (mass_at_3A_proper.atom_braid_word_3A(2,2))
on H_12(q), and c_λ(q_0) := y_λ(q_0) · χ^λ_q(β_{⁴He}), under canonical
convention D (`z_D = q³/(q²+1)`, Wenzl level `r = 2`) every partition λ ⊢ 12
with ℓ(λ) > 2 has weight `y_λ = 0` identically (`QOU.MassTheory.TwoRowCap`), so

  Σ_{λ ∈ Λ²(12)} c_λ(q_0) / Σ_{λ ⊢ 12} c_λ(q_0) = 1

unconditionally whenever the Wedderburn sum is nonzero, where
Λ²(12) = {(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)}.

The algebraic two-row support identity is specialized below from
`QOU.MassTheory.TwoRowCap.twoRow_share_eq_one_of_wenzl`, while
`HasHe4TwoRowDominance` records `ratio := 1` (`ratio_eq_one : ratio = 1`,
retiring the superseded convention-C `866/1000` numeral) and
`HasHe4DominantBlock` records the empirical within-stratum block ranking
(`[9, 3]` as the leading non-trivial block vs `[12]` overall).

Ref: [leitner2026] §F1 ⁴He compositional probe (audit doc)
Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-/

import Mathlib.Tactic.Linarith
import QOU.BraidKnot.TwoRowStratum
import QOU.MassTheory.TwoRowCapDerived

namespace QOU.BraidKnot.He4TwoRowDominance

open Finset QOU.BraidKnot.TwoRowStratum QOU.QBeta.WenzlWeight QOU.MassTheory.TwoRowCap

/-! ## Unconditional convention-D two-row support (`ratio = 1`)

Specialized from `QOU.MassTheory.TwoRowCap`: at convention D (`r = 2`), every
`≥ 3`-row partition vanishes through the Wenzl weight `schurPrincipal 2 Q μ / Z`,
so the two-row stratum carries 100 % (`ratio = 1`) of any nonzero Wedderburn
trace sum on `H₁₂(q)`. -/

/-- The `≥ 3`-row complement of the ⁴He Wedderburn trace sum vanishes identically
    under convention D (`r = 2`), by `threeRowPart_eq_zero_of_wenzl`. -/
theorem he4_threeRowPart_eq_zero_of_wenzl {R : Type*} [Field R] {Q Z : R}
    (hQ0 : Q ≠ 0) (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0)
    (s : Finset YoungDiagram) (χ : YoungDiagram → R) :
    ∑ μ ∈ s.filter (fun μ => ¬ μ.colLen 0 ≤ 2), (schurPrincipal 2 Q μ / Z) * χ μ = 0 :=
  threeRowPart_eq_zero_of_wenzl hQ0 hQ hZ s χ

/-- The two-row stratum share of a nonzero ⁴He Wedderburn trace sum is
    unconditionally `1` under convention D (`r = 2`), specializing
    `QOU.MassTheory.TwoRowCap.twoRow_share_eq_one_of_wenzl`. -/
theorem he4_twoRow_share_eq_one_of_wenzl {R : Type*} [Field R] {Q Z : R}
    (hQ0 : Q ≠ 0) (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0)
    (s : Finset YoungDiagram) (χ : YoungDiagram → R)
    (hne : ∑ μ ∈ s, (schurPrincipal 2 Q μ / Z) * χ μ ≠ 0) :
    (∑ μ ∈ s.filter (fun μ => μ.colLen 0 ≤ 2), (schurPrincipal 2 Q μ / Z) * χ μ)
      / (∑ μ ∈ s, (schurPrincipal 2 Q μ / Z) * χ μ) = 1 :=
  twoRow_share_eq_one_of_wenzl hQ0 hQ hZ s χ hne

/-- The two-row stratum's share of `tr_M(β_⁴He)` under canonical convention D.
    Because convention D (`z_D = q³/(q²+1)`, Wenzl level `r = 2`) kills every
    partition with `ℓ(λ) > 2` identically (`he4_twoRow_share_eq_one_of_wenzl`),
    the two-row share is `ratio = 1` unconditionally (`ratio_eq_one`), which a
    fortiori satisfies the `4/5 ≤ ratio ≤ 1` bounds consumed by downstream
    propositions (`bean qou-58w3`). -/
class HasHe4TwoRowDominance where
  /-- The two-row stratum's share of the trace (`1` under convention D). -/
  ratio : ℚ
  /-- Exact convention-D support: the two-row stratum carries the full trace. -/
  ratio_eq_one : ratio = 1
  /-- Lower bound: at least 80 % (corollary of `ratio_eq_one`). -/
  ratio_lower_bound : (4 : ℚ) / 5 ≤ ratio
  /-- Upper bound: at most 100 % (corollary of `ratio_eq_one`). -/
  ratio_upper_bound : ratio ≤ 1

/-- The dominant non-trivial block λ* for ⁴He is `(9, 3)`, while the largest
    block overall (including the trivial representation) is `(12)`.  Empirically
    verified at 50 dps in `he4-canonical-tr-m-block-fingerprint.witness.json`. -/
class HasHe4DominantBlock where
  /-- The leading NON-TRIVIAL block: the largest `|c_λ|` among the blocks
      whose character is not fixed by construction.  This is the quantity
      the magic-shell reading refers to. -/
  dominant_partition : List ℕ
  /-- It is two-row. -/
  dominant_is_two_row : IsTwoRow dominant_partition
  /-- It sums to 12. -/
  dominant_sums_to_12 : dominant_partition.sum = 12
  /-- The empirical value. -/
  dominant_eq : dominant_partition = [9, 3]
  /-- The largest block by `|c_λ|` OVERALL, trivial representation included. -/
  largest_partition : List ℕ
  /-- It is two-row (a one-row partition has length 1 ≤ 2). -/
  largest_is_two_row : IsTwoRow largest_partition
  /-- It sums to 12. -/
  largest_sums_to_12 : largest_partition.sum = 12
  /-- The empirical value: the trivial representation. -/
  largest_eq : largest_partition = [12]
  /-- **The two are different**, and that is the content of this class.
      Before the 2026-09-05 intra-nucleon ordering ruling the two notions
      picked out the same block, so one field expressed both and nothing
      recorded which was meant.  Under the canonical ordering the trivial
      representation `[12]` leads at 85.4 % against `(9,3)`'s 64.4 % —
      not because it rose (its character is a product of per-letter
      scalars and no reordering can move it) but because every other block
      fell past it.  It leads in six of the eight atoms tabulated, so it
      is not a fingerprint of ⁴He; `(9,3)` is.  Carrying both, and
      asserting they differ, is what keeps the distinction visible. -/
  leading_ne_largest : dominant_partition ≠ largest_partition

/-- Canonical convention-D instance for ⁴He: `ratio := 1` unconditionally
    (matching both `he4_twoRow_share_eq_one_of_wenzl` and the 50-dps witness
    `he4-canonical-tr-m-block-fingerprint.witness.json`, and retiring the
    superseded convention-C `866/1000` numeral; `bean qou-58w3`). -/
instance : HasHe4TwoRowDominance where
  ratio := 1
  ratio_eq_one := rfl
  ratio_lower_bound := by norm_num
  ratio_upper_bound := by norm_num

/-- Empirical instance pinning the leading non-trivial block to `(9, 3)` and the
    overall largest block to `(12)`. -/
instance : HasHe4DominantBlock where
  dominant_partition := [9, 3]
  dominant_is_two_row := by decide
  dominant_sums_to_12 := by decide
  dominant_eq := rfl
  largest_partition := [12]
  largest_is_two_row := by decide
  largest_sums_to_12 := by decide
  largest_eq := rfl
  leading_ne_largest := by decide

/-! ## Derived theorems

The following theorems are PROVED from the class instances above
(no `sorry`). -/

/-- Under convention D (`ratio = 1`), the non-two-row complement share is
    identically `0`. -/
theorem he4_complement_eq_zero
    [h : HasHe4TwoRowDominance] :
    1 - h.ratio = 0 := by
  rw [h.ratio_eq_one, sub_self]

/-- The complement (non-two-row) contribution is at most 20% of
    `|tr_M(β_⁴He)|`.  Direct corollary of `ratio_lower_bound`. -/
theorem he4_complement_at_most_20_percent
    [h : HasHe4TwoRowDominance] :
    1 - h.ratio ≤ 1 / 5 := by
  have hL := h.ratio_lower_bound
  linarith

/-- The dominant block (9, 3) belongs to the two-row stratum
    Λ²(12).  Composes `dominant_is_two_row` and `dominant_sums_to_12`
    via `twoRow_of_length_le_two`. -/
def dominant_in_two_row_stratum
    [h : HasHe4DominantBlock] :
    TwoRowStratum 12 h.dominant_partition :=
  ⟨h.dominant_sums_to_12, h.dominant_is_two_row⟩

/-- The largest block overall also lies in Λ²(12).  It is the trivial
    representation `[12]`, a ONE-row partition — `IsTwoRow` is `length ≤ 2`,
    so Λ²(12) contains it, which is why the stratum ratio is exactly 1 with
    the trivial block included. -/
def largest_in_two_row_stratum
    [h : HasHe4DominantBlock] :
    TwoRowStratum 12 h.largest_partition :=
  ⟨h.largest_sums_to_12, h.largest_is_two_row⟩

/-- The leading non-trivial block is not the trivial representation.  Derived
    from `leading_ne_largest` and `largest_eq`, so it holds for any instance
    rather than being read off this one. -/
theorem dominant_ne_trivial_rep
    [h : HasHe4DominantBlock] :
    h.dominant_partition ≠ [12] := by
  rw [← h.largest_eq]
  exact h.leading_ne_largest

/-- Concrete consequence: the dominant block (9, 3) is in Λ²(12)
    even when stated using the explicit witness value rather than
    the class-field abstraction. -/
theorem dominant_eq_nine_three_in_stratum
    [h : HasHe4DominantBlock] :
    TwoRowStratum 12 [9, 3] := by
  rw [← h.dominant_eq]
  exact dominant_in_two_row_stratum

end QOU.BraidKnot.He4TwoRowDominance
