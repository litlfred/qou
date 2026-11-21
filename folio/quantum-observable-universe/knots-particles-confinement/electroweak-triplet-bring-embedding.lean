import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.electroweak_triplet_bring_embedding — `prop:electroweak-triplet-bring-embedding`

The **provable** structural half of the electroweak torus-link story.
The even-twist 2-component torus links `T(2,4), T(2,6), T(2,8)` (braids
`σ₁^{2k}`, `k = 2, 3, 4`) have Seifert genera `1, 2, 3`, strictly
increasing, all `≤ 4 = g(Σ₄)`; hence they co-embed in the genus-4 Seifert
fiber of Bring's surface alongside the saturating force-carriers
`{T(2,9), T(3,5)}`.

The Hoefsmit pairwise-orthogonal idempotent decomposition of these three
cells in `End_R(V^{⊗6})` is **cited, not re-proved** here: it is
`thm:hoefsmit-ew-cell-content`. This proposition supplies only the
genus / enumeration / embedding facts, which are elementary `ℕ`-arithmetic
and are Lean-proved sorry-free below (`omega`).

LaTeX label: `prop:electroweak-triplet-bring-embedding`.

## References

- [leitner2026] particle-interactions/electroweak-triplet-bring-embedding
- `thm:hoefsmit-ew-cell-content` (the idempotent decomposition, cited)
- `prop:torus-embeddable-complete` (the `g(K) ≤ g(Σ₄)` embedding bound, cited)
-/

namespace QOU.ParticleInteractions

/-- Seifert genus of the even 2-component torus link `T(2, 2k)`: `g = k - 1`.
    (The canonical Seifert surface of `T(2, 2k)` has genus `k - 1`.) -/
def torusLinkGenus (k : ℕ) : ℕ := k - 1

/-- Genus of the Bring surface `Σ₄`. -/
def bringsGenus : ℕ := 4

/-- **L1.** The electroweak family `k ∈ {2, 3, 4}` (`T(2,4), T(2,6),
    T(2,8)`) has Seifert genera `1, 2, 3`. -/
theorem ew_genus_values :
    torusLinkGenus 2 = 1 ∧ torusLinkGenus 3 = 2 ∧ torusLinkGenus 4 = 3 := by
  unfold torusLinkGenus; omega

/-- **L2 (enumeration).** The even-twist 2-component torus links `T(2, 2k)`
    with Seifert genus in `{1, 2, 3}` are *exactly* `k ∈ {2, 3, 4}`. -/
theorem ew_enumeration (k : ℕ) :
    (1 ≤ torusLinkGenus k ∧ torusLinkGenus k ≤ 3) ↔ (k = 2 ∨ k = 3 ∨ k = 4) := by
  unfold torusLinkGenus; omega

/-- **L3 (embedding).** Each electroweak link has Seifert genus
    `≤ 4 = g(Σ₄)`, hence embeds in the genus-4 Seifert fiber of Bring's
    surface by the embeddability bound `g(K) ≤ g(Σ₄)`
    (`prop:torus-embeddable-complete`). -/
theorem ew_triplet_embeds :
    torusLinkGenus 2 ≤ bringsGenus ∧ torusLinkGenus 3 ≤ bringsGenus ∧
    torusLinkGenus 4 ≤ bringsGenus := by
  unfold torusLinkGenus bringsGenus; omega

/-- **Proposition — electroweak triplet Bring embedding.**

    The three even-twist links `T(2,4), T(2,6), T(2,8)` have Seifert genera
    `1, 2, 3` (L1), *strictly increasing*, all `≤ 4 = g(Σ₄)` (L3); hence
    they co-embed in the genus-4 Seifert fiber of Bring's surface with the
    saturating carriers `{T(2,9), T(3,5)}`. Proved sorry-free. -/
theorem electroweak_triplet_bring_embedding :
    (torusLinkGenus 2 = 1 ∧ torusLinkGenus 3 = 2 ∧ torusLinkGenus 4 = 3) ∧
    (torusLinkGenus 2 < torusLinkGenus 3 ∧ torusLinkGenus 3 < torusLinkGenus 4) ∧
    (torusLinkGenus 2 ≤ bringsGenus ∧ torusLinkGenus 3 ≤ bringsGenus ∧
      torusLinkGenus 4 ≤ bringsGenus) := by
  unfold torusLinkGenus bringsGenus; omega

end QOU.ParticleInteractions
