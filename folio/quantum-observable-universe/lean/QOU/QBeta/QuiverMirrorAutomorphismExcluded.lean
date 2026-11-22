import QOU.QBeta.ChiralityGradedCount

set_option autoImplicit false

/-!
# QOU.QBeta.QuiverMirrorAutomorphismExcluded — M1 search-space pruning (D1, first rung)

Formalize-first for the `qou-q9ih` (Q,W) construction: before scanning quivers,
prune the implementation class. The target datum is the `5₂` chirality split
`(S⁺, S⁻) = (4, 3)` read as a pair of DT counts exchanged by the mirror. The
candidate implementations split into two classes:

* **count-invariant symmetries** — the mirror acts by a structure map that
  *preserves* the DT count: a quiver automorphism, the opposite-quiver duality
  `Q ↦ Q^op` (DT-invariant), or any DT-preserving equivalence of the sector
  category;
* **sector-moving actions** — the mirror moves the stability datum to a
  genuinely different ray (the M2 finding: distinct Borel rays in the abelian
  spectrum, `RouteCM3CategoryIdentification`).

**The theorems below exclude the whole first class**: if the count `Ω` is
invariant under the mirror implementation `σ`, every readable pair is
amphichiral (bar-odd `0`), so the `(4, 3)` datum is unreachable — and
conversely the datum *forces* `Ω(σd) ≠ Ω(d)`, i.e. any faithful M1
construction must break count-invariance, which a quiver (anti)automorphism
cannot. The M1 search space is therefore **(quiver, potential, TWO stability
rays)** — never (quiver + automorphism). This extends
`Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_datum`
(no scalar *reading* works) one level up: no count-preserving *symmetry
implementation* works either.

Same species as `ChiralityGradedCount`: input-free statements about arbitrary
count functions — the knot numbers enter only through the existing literature
`def`s (`dtSplit52`), quoted in the exclusion corollary. Nothing here
constructs a (Q,W) or derives a DT integer (anti-laundering: the search
remains open; this only says where not to search).

## References

- [kontsevich-soibelman2008] https://doi.org/10.48550/arXiv.0811.2435 (DT counts; op-invariance)
- [leitner2026] docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md (D1/M1);
  QOU/QBeta/ChiralityGradedCount.lean (the pair machinery);
  QOU/QBeta/RouteCM3CategoryIdentification.lean (distinct Borel rays, M2).
-/

namespace QOU.QBeta.QuiverMirrorAutomorphismExcluded

open QOU.QBeta.ChiralityGradedCount

universe u

variable {D : Type u}

/-- The chirality pair read off a sector `d` under a mirror implementation
`σ`: `(Ω d, Ω (σ d))` — "the count here, the count at the mirror sector". -/
def sectorPair (Ω : D → Int) (σ : D → D) (d : D) : Split :=
  (Ω d, Ω (σ d))

/-- For an involutive `σ`, moving the base sector across the mirror swaps the
pair — `sectorPair` is a well-formed chirality split in the sense of
`ChiralityGradedCount.mirror`. -/
theorem sectorPair_swap_of_involutive (Ω : D → Int) (σ : D → D)
    (hinv : ∀ e, σ (σ e) = e) (d : D) :
    sectorPair Ω σ (σ d) = ChiralityGradedCount.mirror (sectorPair Ω σ d) := by
  unfold sectorPair ChiralityGradedCount.mirror
  rw [hinv d]

/-- **The exclusion**: a count-invariant mirror implementation forces every
readable pair amphichiral — the bar-odd part vanishes identically. -/
theorem barOdd_zero_of_count_invariant (Ω : D → Int) (σ : D → D)
    (hσ : ∀ e, Ω (σ e) = Ω e) (d : D) :
    barOdd (sectorPair Ω σ d) = 0 := by
  unfold sectorPair barOdd
  rw [hσ d]
  omega

/-- A count-invariant implementation can never read a genuinely chiral pair. -/
theorem not_chiral_of_count_invariant (Ω : D → Int) (σ : D → D)
    (hσ : ∀ e, Ω (σ e) = Ω e) (d : D) :
    ¬ IsChiral (sectorPair Ω σ d) := by
  intro hchi
  exact (chiral_iff_odd_ne_zero _).mp hchi
    (barOdd_zero_of_count_invariant Ω σ hσ d)

/-- **Corollary at the literature datum**: no count-invariant implementation
reaches the `5₂` split `(4, 3)` — quiver automorphisms and op-duality are
excluded as mirror implementations for M1. -/
theorem count_invariant_excludes_five_two (Ω : D → Int) (σ : D → D)
    (hσ : ∀ e, Ω (σ e) = Ω e) (d : D) :
    sectorPair Ω σ d ≠ dtSplit52 := by
  intro h
  have h0 := barOdd_zero_of_count_invariant Ω σ hσ d
  rw [h] at h0
  exact absurd h0 (by decide)

/-- **The positive direction**: reading the `(4, 3)` datum *forces* the mirror
implementation to change the count — `Ω(σd) ≠ Ω(d)`. Any faithful M1
construction must implement the mirror as a sector-moving action (distinct
stability rays), never as a DT-preserving symmetry. -/
theorem five_two_forces_count_breaking (Ω : D → Int) (σ : D → D) (d : D)
    (h : sectorPair Ω σ d = dtSplit52) : Ω (σ d) ≠ Ω d := by
  unfold sectorPair dtSplit52 at h
  have h1 := congrArg Prod.fst h
  have h2 := congrArg Prod.snd h
  simp at h1 h2
  omega

end QOU.QBeta.QuiverMirrorAutomorphismExcluded
