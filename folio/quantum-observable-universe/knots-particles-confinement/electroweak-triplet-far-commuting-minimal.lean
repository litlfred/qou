import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.electroweak_triplet_far_commuting_minimal — `thm:ew-triplet-far-commuting-minimal`

The **physics-free** mathematical core of the electroweak selection principle
(C1 of `conj:electroweak-higgs-torus-link-triplet`). Two elementary facts,
both Lean-proved sorry-free:

* **Far-commuting minimality.** Three pairwise *far-commuting* braid
  generators `σ_a, σ_b, σ_c` (`|a−b|, |b−c|, |a−c| ≥ 2`, the
  far-commutativity range `σ_i σ_j = σ_j σ_i` for `|i−j| ≥ 2`) require at
  least `6` strands, and `6` is attained *uniquely* by the consecutive
  odd triple `(a, b, c) = (1, 3, 5)`. In `B_n` a generator `σ_i` needs
  `1 ≤ i ≤ n − 1`; three indices with pairwise gap `≥ 2` force the top
  index `c ≥ 5`, hence `n ≥ 6`. This is the mathematical statement behind
  the `n = 6` minimality realised physically in
  `thm:hoefsmit-ew-cell-content` (three disjoint strand-pairs
  `{1,2}, {3,4}, {5,6}`).

* **Sub-saturating enumeration.** The even-twist `2`-component torus links
  `T(2, 2k)` (braid `σ_1^{2k}`) with Seifert genus `g = k − 1` strictly
  between the trivial Hopf endpoint (`g = 0`) and the genus-`4` Bring
  saturation (`g = 4`) — i.e. `1 ≤ g ≤ 3` — are *exactly*
  `{T(2,4), T(2,6), T(2,8)}` (`k ∈ {2,3,4}`).

The enumeration half is the identical arithmetic proved as `ew_enumeration`
in the sibling `prop:electroweak-triplet-bring-embedding`. Content-block
sibling `.lean` files compile standalone (Mathlib-only) and cannot import
one another, so the one-line `omega` fact is reproduced here for
self-containment; the sibling proposition is the canonical statement and is
cited, not re-derived structurally.

LaTeX label: `thm:ew-triplet-far-commuting-minimal`.

## References

- [leitner2026] particle-interactions/electroweak-triplet-far-commuting-minimal
- `prop:electroweak-triplet-bring-embedding` (`ew_enumeration`, the canonical
  genus enumeration; reproduced inline per the self-containment note above)
- `thm:hoefsmit-ew-cell-content` (the `n = 6` minimality *physical*
  realisation: three disjoint strand-pairs of the Hoefsmit projectors)
-/

namespace QOU.ParticleInteractions

/-! ## Far-commuting minimality -/

/-- Number of strands a braid generator `σ_i` (index `i`) lives in: `σ_i`
    acts on strands `i, i+1` of `B_{i+1}`, i.e. needs `i + 1` strands. -/
def strandsFor (i : ℕ) : ℕ := i + 1

/-- **Far-commuting lower bound.** Three positive generator indices
    `a < b < c` that are pairwise *far-commuting* (pairwise gap `≥ 2`,
    encoded `a + 2 ≤ b` and `b + 2 ≤ c` with `1 ≤ a`) force the top index
    `c ≥ 5`. Hence they need at least `strandsFor c = c + 1 ≥ 6` strands. -/
theorem far_commuting_top_index_ge
    (a b c : ℕ) (ha : 1 ≤ a) (hab : a + 2 ≤ b) (hbc : b + 2 ≤ c) :
    5 ≤ c := by omega

/-- **Minimum strand count.** Under the same far-commuting hypotheses, the
    three generators fit only in `B_n` with `n = strandsFor c ≥ 6`. -/
theorem far_commuting_min_strands
    (a b c : ℕ) (ha : 1 ≤ a) (hab : a + 2 ≤ b) (hbc : b + 2 ≤ c) :
    6 ≤ strandsFor c := by
  unfold strandsFor; omega

/-- **The consecutive odd triple `(1, 3, 5)` realises the minimum.** It is
    far-commuting, its top index is `5`, and it fits in `B_6`
    (`strandsFor 5 = 6`); moreover among far-commuting triples it is the
    *unique* one attaining `strandsFor c = 6` (any far-commuting triple with
    `c + 1 = 6` must be `(1, 3, 5)`). -/
theorem far_commuting_min_witness :
    (1 ≤ 1 ∧ 1 + 2 ≤ 3 ∧ 3 + 2 ≤ 5) ∧ strandsFor 5 = 6 ∧
      (∀ a b c : ℕ, 1 ≤ a → a + 2 ≤ b → b + 2 ≤ c → strandsFor c = 6 →
        a = 1 ∧ b = 3 ∧ c = 5) := by
  refine ⟨⟨?_, ?_, ?_⟩, ?_, ?_⟩
  · omega
  · omega
  · omega
  · rfl
  · intro a b c ha hab hbc hn
    unfold strandsFor at hn
    omega

/-! ## Sub-saturating enumeration (reproduces `ew_enumeration`) -/

/-- Seifert genus of the even `2`-component torus link `T(2, 2k)`: `g = k − 1`
    (identical to `torusLinkGenus` of `prop:electroweak-triplet-bring-embedding`). -/
def torusLinkGenus (k : ℕ) : ℕ := k - 1

/-- **Sub-saturating enumeration.** The even-twist links `T(2, 2k)` whose
    Seifert genus lies strictly between the Hopf endpoint and the genus-`4`
    Bring saturation — `1 ≤ g ≤ 3` — are *exactly* `k ∈ {2, 3, 4}`, i.e. the
    triplet `T(2,4), T(2,6), T(2,8)`. This is the sorry-free `ew_enumeration`
    of the sibling proposition, reproduced inline (self-containment note). -/
theorem sub_saturating_enumeration (k : ℕ) :
    (1 ≤ torusLinkGenus k ∧ torusLinkGenus k ≤ 3) ↔ (k = 2 ∨ k = 3 ∨ k = 4) := by
  unfold torusLinkGenus; omega

/-! ## The theorem — far-commuting minimality + enumeration together -/

/-- **Theorem — electroweak triplet far-commuting minimality.**

    Three pairwise far-commuting even-twist `2`-component torus-link
    generators `σ_a, σ_b, σ_c` (`1 ≤ a`, pairwise gap `≥ 2`)

    1. require at least `6` strands (`6 ≤ strandsFor c`), attained *uniquely*
       by `(a, b, c) = (1, 3, 5)` in `B_6`; and

    2. the nontrivial strictly-sub-saturating even-twist links (Seifert genus
       `g` with `1 ≤ g ≤ 3`) are exactly `{T(2,4), T(2,6), T(2,8)}`
       (`k ∈ {2,3,4}`).

    Both halves are elementary `ℕ`-arithmetic, Lean-proved sorry-free. The
    `n = 6` minimality is physically realised by the three disjoint
    strand-pairs of `thm:hoefsmit-ew-cell-content`; the enumeration is the
    canonical `ew_enumeration` of `prop:electroweak-triplet-bring-embedding`. -/
theorem electroweak_triplet_far_commuting_minimal :
    (∀ a b c : ℕ, 1 ≤ a → a + 2 ≤ b → b + 2 ≤ c → 6 ≤ strandsFor c) ∧
    (strandsFor 5 = 6 ∧ (1 ≤ 1 ∧ 1 + 2 ≤ 3 ∧ 3 + 2 ≤ 5)) ∧
    (∀ k : ℕ,
      (1 ≤ torusLinkGenus k ∧ torusLinkGenus k ≤ 3) ↔ (k = 2 ∨ k = 3 ∨ k = 4)) := by
  refine ⟨?_, ⟨?_, ?_, ?_, ?_⟩, ?_⟩
  · intro a b c ha hab hbc; exact far_commuting_min_strands a b c ha hab hbc
  · rfl
  · omega
  · omega
  · omega
  · intro k; exact sub_saturating_enumeration k

end QOU.ParticleInteractions
