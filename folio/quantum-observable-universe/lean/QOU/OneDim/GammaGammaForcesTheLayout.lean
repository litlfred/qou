/-
# γγ production forces the strand layout — and that is why there is no 3-cell

`QOU/OneDim/NoThreeCellOnTheChain.lean` proves that a **linear layout** carries
no triangle, hence no 3-cell, taking `LinearLayout` as a *hypothesis*.  This
file reaches the same conclusion from the corpus's own γγ vertex, by an
**independent combinatorial route**.

🛑 **It does not discharge that hypothesis, and an earlier version of this
docstring said it did.**  Nothing here imports, mentions, or produces
`LinearLayout`: that predicate is about `SimpleGraph (Fin n)` and everything
below is about `Finset ℕ`, with no bridge lemma between them.  Read this file
as a second, independent derivation of "no 3-cell on the chain", not as the
cited theorem with its hypothesis supplied.  Building the bridge — a lemma
producing `LinearLayout G` for the contiguous block graph — is the work that
would make the stronger sentence true, and it has not been done.

**Update 2026-11-15:** the bridge now exists, in
`QOU/OneDim/GammaGammaLinearLayout.lean` (`gammaGammaGraph_linearLayout`,
`mixedGraph_linearLayout`): on the contiguous layout the coordination graph of
any word built from γγ vertices and single crossings is a `LinearLayout`.

## The one input

`QOU/Mass/GammaGammaWordSelection.lean` defines the pair-production vertex as

    vertex i = [σᵢ, σᵢ₊₁⁻¹]

— **adjacent** Artin generators.  A crossing `σⱼ` exchanges strands `j` and
`j+1`, so `vertex i` touches exactly the three strands `{i, i+1, i+2}`; the
docstring there says so in words ("one photon on strands `(i, i+1)` and one
anti-photon on `(i+1, i+2)`").  A nucleon's internal word is
`β_Bor = (σ₀σ₁⁻¹)³`, three such vertices, and it is *internal* to a nucleon
exactly when every strand it touches belongs to that nucleon's own block.

That single demand is the whole hypothesis.  Nothing here reads AME, CODATA,
a census, or a q-value.

**One step is by eye, and is flagged rather than hidden.**  `vertexStrands` is
a *definition* in this file, hand-transcribed from `GammaGammaWordSelection
.vertex`; it is not a theorem *about* that object.  The transcription is
correct — `vertex i = [σᵢ, σᵢ₊₁⁻¹]` and `σⱼ` exchanges strands `j, j+1`, so the
support is `{i,i+1} ∪ {i+1,i+2} = {i,i+1,i+2}` — but it is checked by reading,
not by the compiler.  Formalising it would mean giving `Word` a strand-support
function and proving `support (vertex i) = vertexStrands i`.

## What is proved

* `eq_triple_of_internal` — **the crux.**  A three-strand block admitting any
  internal γγ vertex *is* an interval `{a, a+1, a+2}`.  Not "is contained in"
  and not "is adjacent to": the block is determined by the vertex.
* `internal_triple` — the converse, so the predicate is not vacuously false.
* `bonded_iff_base_succ` — two **disjoint** triples are bonded (some strand of
  one is the immediate successor of a strand of the other) **iff** their bases
  differ by exactly `3`.  This is what makes the coordination graph a path: a
  block's only possible neighbours are the triples immediately left and right.
* `no_triangle_of_triples` — three pairwise-disjoint, pairwise-bonded triples
  do not exist.  So under the γγ demand the coordination graph carries no
  triangle, hence no 3-cell, with `LinearLayout` *derived* rather than assumed.
* `residue_layout_bonded_pairwise` **and** `residue_block_not_internal` —
  together these are the load-bearing pair.  The interleaved layout
  `{0,3,6}, {1,4,7}, {2,5,8}` **is** pairwise bonded, so its coordination graph
  *is* a triangle: a 3-cell is combinatorially available and the braid group
  does not forbid it.  It is excluded only because not one of its blocks admits
  an internal γγ vertex.  Without this pair, `no_triangle_of_triples` would be
  a statement about an empty option space.

## Scope of the negative (AGENTS.md §"Before declaring refuted")

Scope **(b)**, structural, invariant named: `σⱼ` joins only *consecutive*
strands, so a three-strand set closed under a γγ vertex is an interval.

It excludes a non-contiguous layout from the **Artin-adjacent** reading of the
vertex, which is the reading `GammaGammaWordSelection` encodes.  It does **not**
exclude a band-generator reading: `a_{ts}` crosses two non-adjacent strands and
has writhe `1`, so a band vertex `a_{ts} a_{t's'}⁻¹` has writhe `0` and passes
`GammaGammaWordSelection.writhe_eq_zero` while not being a `GammaGammaWord`
under that file's inductive definition.  Under a band reading the
non-contiguous layouts reopen.  Which reading the physics means is
definitional and is deliberately left open — choosing the one that yields a
3-cell would be selection against the target.

Companion probe (15/15, exact combinatorics, exhaustive over all 3-uniform
partitions at `A = 2, 3, 4`):
`computations/onedim/gamma_gamma_forces_the_layout_probe.py`.
Bean `qou-u5qs`.

## Base ring (§7c)

Pure combinatorics on `ℕ` and `Finset ℕ`.  No ordering on a coefficient ring,
no `Real`, no `q`.
-/
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

namespace QOU.OneDim.GammaGammaForcesTheLayout

/-! ## Strands, vertices, blocks -/

/-- The three strands the γγ vertex `σᵢ σᵢ₊₁⁻¹` touches.  `σⱼ` exchanges
strands `j` and `j+1`, and the vertex uses generators `i` and `i+1`. -/
def vertexStrands (i : ℕ) : Finset ℕ := {i, i + 1, i + 2}

/-- A run of three consecutive strands based at `a`. -/
def triple (a : ℕ) : Finset ℕ := {a, a + 1, a + 2}

theorem vertexStrands_eq_triple (i : ℕ) : vertexStrands i = triple i := rfl

/-- A block is **γγ-internal** when some pair-production vertex lies entirely
inside it — i.e. the nucleon can braid itself without reaching another
nucleon's strand. -/
def Internal (B : Finset ℕ) : Prop := ∃ i, vertexStrands i ⊆ B

/-- Two blocks are **bonded** when some strand of one is the immediate
successor of a strand of the other.  This is exactly an edge of the strand
path `s — (s+1)` crossing between the two blocks. -/
def Bonded (B C : Finset ℕ) : Prop :=
  (∃ s, s ∈ B ∧ s + 1 ∈ C) ∨ (∃ s, s ∈ C ∧ s + 1 ∈ B)

theorem bonded_symm {B C : Finset ℕ} (h : Bonded B C) : Bonded C B := by
  rcases h with h | h
  · exact Or.inr h
  · exact Or.inl h

/-! ## The crux: an internal vertex forces the block to be an interval -/

theorem card_triple (a : ℕ) : (triple a).card = 3 := by
  unfold triple
  rw [Finset.card_insert_of_notMem (by simp), Finset.card_insert_of_notMem (by simp),
    Finset.card_singleton]

theorem mem_triple {a x : ℕ} : x ∈ triple a ↔ x = a ∨ x = a + 1 ∨ x = a + 2 := by
  simp [triple]

/-- **A three-strand block admitting an internal γγ vertex IS an interval.**

This is the whole structural content: the vertex's own support already has
three elements, so a three-element block containing it *equals* it. -/
theorem eq_triple_of_internal {B : Finset ℕ} (hcard : B.card = 3) (h : Internal B) :
    ∃ a, B = triple a := by
  obtain ⟨i, hi⟩ := h
  refine ⟨i, ?_⟩
  rw [vertexStrands_eq_triple] at hi
  exact (Finset.eq_of_subset_of_card_le hi (by rw [hcard, card_triple])).symm

/-- The converse: an interval *does* admit an internal vertex, so `Internal` is
not vacuously false and `eq_triple_of_internal` is not an empty implication. -/
theorem internal_triple (a : ℕ) : Internal (triple a) :=
  ⟨a, by rw [vertexStrands_eq_triple]⟩

/-- Restated as an equivalence on three-strand blocks. -/
theorem internal_iff_isTriple {B : Finset ℕ} (hcard : B.card = 3) :
    Internal B ↔ ∃ a, B = triple a := by
  constructor
  · exact eq_triple_of_internal hcard
  · rintro ⟨a, rfl⟩; exact internal_triple a

/-! ## Disjoint triples bond only when consecutive -/

/-- Disjointness of two triples, read on their bases. -/
theorem triple_disjoint_iff {a b : ℕ} :
    Disjoint (triple a) (triple b) ↔ (b + 3 ≤ a ∨ a + 3 ≤ b) := by
  constructor
  · intro h
    by_contra hcon
    push_neg at hcon
    obtain ⟨h1, h2⟩ := hcon
    -- `a < b + 3` and `b < a + 3`, so the two runs overlap at some strand.
    have : ∃ x, x ∈ triple a ∧ x ∈ triple b := by
      rcases le_or_gt a b with hab | hab
      · exact ⟨b, by rw [mem_triple]; omega, by rw [mem_triple]; omega⟩
      · exact ⟨a, by rw [mem_triple]; omega, by rw [mem_triple]; omega⟩
    obtain ⟨x, hxa, hxb⟩ := this
    exact (Finset.disjoint_left.mp h hxa) hxb
  · intro h
    rw [Finset.disjoint_left]
    intro x hxa hxb
    rw [mem_triple] at hxa hxb
    omega

/-- **Two disjoint triples are bonded iff their bases differ by exactly three.**

A block's only possible neighbours are the triples immediately to its left and
right — which is why the coordination graph is a path. -/
theorem bonded_iff_base_succ {a b : ℕ} (hd : Disjoint (triple a) (triple b)) :
    Bonded (triple a) (triple b) ↔ (b = a + 3 ∨ a = b + 3) := by
  rw [triple_disjoint_iff] at hd
  constructor
  · rintro (⟨s, hs, hs'⟩ | ⟨s, hs, hs'⟩) <;>
      · rw [mem_triple] at hs hs'; omega
  · rintro (rfl | rfl)
    · exact Or.inl ⟨a + 2, by rw [mem_triple]; omega, by rw [mem_triple]; omega⟩
    · exact Or.inr ⟨b + 2, by rw [mem_triple]; omega, by rw [mem_triple]; omega⟩

/-! ## Hence no triangle -/

/-- **No triangle.**  Three pairwise-disjoint triples cannot be pairwise
bonded: bonding forces each pair of bases to differ by exactly `3`, and three
distinct naturals cannot pairwise differ by `3`.

This is the `Finset ℕ` analogue of `NoThreeCellOnTheChain.no_triangle`, reached
from the γγ vertex instead of from a `LinearLayout` hypothesis.  The two are
independent routes to the same conclusion; neither is derived from the other
(see the 🛑 note at the top). -/
theorem no_triangle_of_triples {a b c : ℕ}
    (hab : Disjoint (triple a) (triple b)) (hbc : Disjoint (triple b) (triple c))
    (hac : Disjoint (triple a) (triple c))
    (bab : Bonded (triple a) (triple b)) (bbc : Bonded (triple b) (triple c))
    (bac : Bonded (triple a) (triple c)) : False := by
  rw [bonded_iff_base_succ hab] at bab
  rw [bonded_iff_base_succ hbc] at bbc
  rw [bonded_iff_base_succ hac] at bac
  omega

/-- A block's neighbours among disjoint triples number at most two — the bases
`a - 3` and `a + 3`.  Stated as: three pairwise-distinct triples all bonded to
`triple a` and pairwise disjoint from it cannot exist. -/
theorem degree_le_two {a b c d : ℕ}
    (hb : Disjoint (triple a) (triple b)) (hc : Disjoint (triple a) (triple c))
    (hd : Disjoint (triple a) (triple d))
    (bb : Bonded (triple a) (triple b)) (bc : Bonded (triple a) (triple c))
    (bd : Bonded (triple a) (triple d))
    (hbc : b ≠ c) (hbd : b ≠ d) (hcd : c ≠ d) : False := by
  rw [bonded_iff_base_succ hb] at bb
  rw [bonded_iff_base_succ hc] at bc
  rw [bonded_iff_base_succ hd] at bd
  omega

/-! ## The exclusion has content: the interleaved layout IS a triangle

Without this section `no_triangle_of_triples` would be a theorem about an
option space that might be empty.  It is not: the interleaved layout's blocks
are pairwise bonded — its coordination graph *is* a triangle — and the braid
group permits it.  What excludes it is precisely that no block of it admits an
internal γγ vertex. -/

/-- Block `k` of the interleaved ("residue") layout at `A = 3`: strands
`{k, k+3, k+6}`. -/
def residueBlock (k : ℕ) : Finset ℕ := {k, k + 3, k + 6}

theorem mem_residueBlock {k x : ℕ} :
    x ∈ residueBlock k ↔ x = k ∨ x = k + 3 ∨ x = k + 6 := by
  simp [residueBlock]

theorem card_residueBlock (k : ℕ) : (residueBlock k).card = 3 := by
  unfold residueBlock
  rw [Finset.card_insert_of_notMem (by simp), Finset.card_insert_of_notMem (by simp),
    Finset.card_singleton]

/-- The three interleaved blocks are pairwise disjoint. -/
theorem residue_disjoint {j k : ℕ} (hjk : j < k) (h : k < j + 3) :
    Disjoint (residueBlock j) (residueBlock k) := by
  rw [Finset.disjoint_left]
  intro x hj hk
  rw [mem_residueBlock] at hj hk
  omega

/-- **The interleaved layout's coordination graph is a triangle.**  Each pair of
blocks is bonded, including the wrap-around pair `{2,5,8}`–`{0,3,6}`. -/
theorem residue_layout_bonded_pairwise :
    Bonded (residueBlock 0) (residueBlock 1) ∧
    Bonded (residueBlock 1) (residueBlock 2) ∧
    Bonded (residueBlock 0) (residueBlock 2) := by
  refine ⟨Or.inl ⟨0, ?_, ?_⟩, Or.inl ⟨1, ?_, ?_⟩, Or.inr ⟨2, ?_, ?_⟩⟩ <;>
    · rw [mem_residueBlock]; omega

/-- **But no interleaved block admits an internal γγ vertex.**  By
`eq_triple_of_internal` such a block would be a run of three consecutive
strands; an interleaved block contains no two consecutive strands at all. -/
theorem residue_block_not_internal (k : ℕ) : ¬ Internal (residueBlock k) := by
  intro h
  obtain ⟨a, ha⟩ := eq_triple_of_internal (card_residueBlock k) h
  have h0 : a ∈ residueBlock k := by rw [ha, mem_triple]; omega
  have h1 : a + 1 ∈ residueBlock k := by rw [ha, mem_triple]; omega
  rw [mem_residueBlock] at h0 h1
  omega

/-- Packaged: the interleaved layout carries a triangle **and** is γγ-excluded.
The two halves together are the statement that the γγ demand, not the braid
group, is what removes the 3-cell. -/
theorem residue_layout_is_the_excluded_triangle :
    (Bonded (residueBlock 0) (residueBlock 1) ∧
      Bonded (residueBlock 1) (residueBlock 2) ∧
      Bonded (residueBlock 0) (residueBlock 2)) ∧
    (∀ k, ¬ Internal (residueBlock k)) :=
  ⟨residue_layout_bonded_pairwise, residue_block_not_internal⟩

/-! ## The contiguous layout, for contrast -/

/-- Block `k` of the contiguous layout: strands `{3k, 3k+1, 3k+2}`. -/
def contigBlock (k : ℕ) : Finset ℕ := triple (3 * k)

theorem contig_internal (k : ℕ) : Internal (contigBlock k) := internal_triple _

theorem contig_disjoint {j k : ℕ} (h : j ≠ k) :
    Disjoint (contigBlock j) (contigBlock k) := by
  unfold contigBlock
  rw [triple_disjoint_iff]
  omega

/-- **The contiguous layout is a chain.**  Blocks `j` and `k` are bonded exactly
when they are consecutive — degree at most two, no triangle. -/
theorem contig_bonded_iff {j k : ℕ} (h : j ≠ k) :
    Bonded (contigBlock j) (contigBlock k) ↔ (k = j + 1 ∨ j = k + 1) := by
  unfold contigBlock
  rw [bonded_iff_base_succ (by rw [triple_disjoint_iff]; omega)]
  omega

/-- **No 3-cell on the contiguous layout**, as a corollary of the above rather
than as a hypothesis about the graph. -/
theorem contig_no_triangle {i j k : ℕ} (hij : i ≠ j) (hjk : j ≠ k) (hik : i ≠ k)
    (bij : Bonded (contigBlock i) (contigBlock j))
    (bjk : Bonded (contigBlock j) (contigBlock k))
    (bik : Bonded (contigBlock i) (contigBlock k)) : False := by
  rw [contig_bonded_iff hij] at bij
  rw [contig_bonded_iff hjk] at bjk
  rw [contig_bonded_iff hik] at bik
  omega

end QOU.OneDim.GammaGammaForcesTheLayout
