import QOU.BraidKnot.SpechtClassification

/-!
# The lexicographic order on shapes — the order Mathas' Garnir lemma actually uses

Mathas' Lemma 3.12 (*Hecke algebras and Schur algebras of the symmetric group*) is
the Garnir relation the Murphy-basis spanning argument runs on.  It concludes with a
shape moving **up an order**, and the order is **lexicographic**, not dominance.

He says so in the sentence immediately before it, introduced for exactly these
lemmas:

> *"For the next few Lemmas we need another ordering on the set of partitions.
> Given partitions `λ` and `μ` we write `λ > μ` if `λ` is greater than `μ` in the
> lexicographic ordering.  That is, there exists an integer `j ≥ 1` such that
> `λᵢ = μᵢ` for `1 ≤ i < j` and `λⱼ > μⱼ`.  … Note that if `λ ⊵ μ` then `λ > μ`."*

## Why this file exists, rather than reusing `partitionDom`

The corpus already carries the **dominance** order
(`SpechtClassification.partitionDom`), and it is the natural thing to reach for.
**It is the wrong order here, and measurably so.**
[`garnir_shape_dominance_probe.py`](../../../../../computations/hecke/garnir_shape_dominance_probe.py)
checks both orders against Mathas' Garnir composition, exhaustively over every
partition and every Garnir node for `n = 2..11` — 910 nodes, exact integer
arithmetic:

    sorted(ν) >_lex λ    910 / 910
    sorted(ν) ⊳ λ        824 / 910    — 86 failures

The smallest counterexample needs no machine, and it is `dom_fails_lex_holds`
below: `λ = (3,3)` with Garnir node `(0,1)` gives `ν = (4,1,1)`, and `4 ≥ 3` but
`4 + 1 < 3 + 3`.

`lexGt_of_partitionDom_of_ne` is Mathas' own "note", and it is what lets an existing
dominance result feed a lex induction: dominance is **strictly stronger**, so every
`partitionDom` fact in the corpus is still usable here — the implication just does
not run the other way.

## Why the weaker order is the better one to induct on

Lex is **total** on the partitions of a fixed `n`, where dominance is only partial.
So a straightening induction that decreases in lex is comparing every pair, which is
what makes the well-founded recursion routine rather than delicate.  This is the
reason Mathas switches orders for these lemmas at all.
-/

open scoped BigOperators

namespace QOU.BraidKnot.PartitionLex

open QOU.BraidKnot.SpechtClassification

/-- **Lexicographic order on Young diagrams**: `μ >_lex ν` iff the first row length
at which they differ is larger in `μ`.

Stated with the witnessing index explicit, matching Mathas' phrasing ("there exists
an integer `j`"), and indexed from `0` rather than his `1`. -/
def partitionLexGt (μ ν : YoungDiagram) : Prop :=
  ∃ r : ℕ, (∀ s, s < r → μ.rowLen s = ν.rowLen s) ∧ ν.rowLen r < μ.rowLen r

@[inherit_doc] infixl:50 " >ₗ " => partitionLexGt

/-- Equal row lengths at every index means equal diagrams.

The same `mem_iff_lt_rowLen` step `partitionDom_antisymm` runs on, factored out
because both the irreflexivity and the dominance bridge below need it. -/
theorem eq_of_rowLen_eq {μ ν : YoungDiagram} (h : ∀ i, μ.rowLen i = ν.rowLen i) :
    μ = ν := by
  apply YoungDiagram.ext
  ext ⟨i, j⟩
  simp only [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen, h i]

/-- Lex is irreflexive. -/
theorem partitionLexGt_irrefl (μ : YoungDiagram) : ¬ (μ >ₗ μ) := by
  rintro ⟨r, -, hlt⟩
  exact lt_irrefl _ hlt

/-- A lex-greater shape is a different shape. -/
theorem ne_of_partitionLexGt {μ ν : YoungDiagram} (h : μ >ₗ ν) : μ ≠ ν := by
  rintro rfl
  exact partitionLexGt_irrefl _ h

/-- Lex is transitive.  The witness is the smaller of the two indices; the three
cases differ only in which side supplies the strict step. -/
theorem partitionLexGt_trans {μ ν ρ : YoungDiagram}
    (h₁ : μ >ₗ ν) (h₂ : ν >ₗ ρ) : μ >ₗ ρ := by
  obtain ⟨r₁, heq₁, hlt₁⟩ := h₁
  obtain ⟨r₂, heq₂, hlt₂⟩ := h₂
  rcases lt_trichotomy r₁ r₂ with hr | hr | hr
  · -- `μ` and `ν` first differ earlier, and `ν = ρ` still holds there
    refine ⟨r₁, fun s hs => ?_, ?_⟩
    · rw [heq₁ s hs, heq₂ s (hs.trans hr)]
    · rw [← heq₂ r₁ hr]; exact hlt₁
  · subst hr
    exact ⟨r₁, fun s hs => (heq₁ s hs).trans (heq₂ s hs), hlt₂.trans hlt₁⟩
  · -- `ν` and `ρ` first differ earlier, and `μ = ν` still holds there
    refine ⟨r₂, fun s hs => ?_, ?_⟩
    · rw [heq₁ s (hs.trans hr), heq₂ s hs]
    · rw [heq₁ r₂ hr]; exact hlt₂

/-- **Mathas' note: dominance implies lex.**  "Note that if `λ ⊵ μ` then `λ > μ`."

This is the bridge that keeps the corpus's existing dominance results usable: every
`partitionDom` fact still yields a lex fact, so switching the Garnir induction to lex
costs nothing already proved.  The converse is false — see `dom_fails_lex_holds`. -/
theorem lexGt_of_partitionDom_of_ne {μ ν : YoungDiagram}
    (hd : partitionDom μ ν) (hne : μ ≠ ν) : μ >ₗ ν := by
  classical
  have hex : ∃ r, μ.rowLen r ≠ ν.rowLen r := by
    by_contra hcon
    push_neg at hcon
    exact hne (eq_of_rowLen_eq hcon)
  refine ⟨Nat.find hex, fun s hs => ?_, ?_⟩
  · by_contra hc
    exact Nat.find_min hex hs hc
  · -- the prefix sums agree, so dominance one step further forces the strict step
    have hprefix : ∀ s, s < Nat.find hex → μ.rowLen s = ν.rowLen s := by
      intro s hs
      by_contra hc
      exact Nat.find_min hex hs hc
    have hsum : (∑ k ∈ Finset.range (Nat.find hex), ν.rowLen k)
        = ∑ k ∈ Finset.range (Nat.find hex), μ.rowLen k :=
      Finset.sum_congr rfl fun k hk => (hprefix k (Finset.mem_range.mp hk)).symm
    have h1 := hd (Nat.find hex + 1)
    rw [Finset.sum_range_succ, Finset.sum_range_succ, hsum] at h1
    have hne_r : μ.rowLen (Nat.find hex) ≠ ν.rowLen (Nat.find hex) := Nat.find_spec hex
    omega

/-! ## The two orders are genuinely different

Everything above would be consistent with lex and dominance agreeing, in which case
this file would be redundant and `partitionDom` could have been used directly.  They
do not agree, and the witness is the smallest Garnir counterexample the probe found.
-/

/-- `(3,3)`, the shape of the counterexample. -/
def lam33 : YoungDiagram := YoungDiagram.ofRowLens [3, 3] (by decide)

/-- `(4,1,1)`, the partition of Mathas' Garnir composition at `λ = (3,3)`, node
`(i,j) = (0,1)`: the composition is `(1, 4, 1)`, which sorts to this. -/
def nu411 : YoungDiagram := YoungDiagram.ofRowLens [4, 1, 1] (by decide)

@[simp] theorem rowLen_lam33_zero : lam33.rowLen 0 = 3 :=
  YoungDiagram.rowLen_ofRowLens (w := [3, 3]) ⟨0, by decide⟩

@[simp] theorem rowLen_lam33_one : lam33.rowLen 1 = 3 :=
  YoungDiagram.rowLen_ofRowLens (w := [3, 3]) ⟨1, by decide⟩

@[simp] theorem rowLen_nu411_zero : nu411.rowLen 0 = 4 :=
  YoungDiagram.rowLen_ofRowLens (w := [4, 1, 1]) ⟨0, by decide⟩

@[simp] theorem rowLen_nu411_one : nu411.rowLen 1 = 1 :=
  YoungDiagram.rowLen_ofRowLens (w := [4, 1, 1]) ⟨1, by decide⟩

/-- **The separating example: lex holds where dominance fails.**

`(4,1,1) >ₗ (3,3)` because `4 > 3` in the first row, but `(4,1,1)` does *not*
dominate `(3,3)` because `4 + 1 = 5 < 6 = 3 + 3`.

This is exactly the pair Mathas' Garnir composition produces at `λ = (3,3)`, node
`(0,1)`, so the failure is not a curiosity about the two orders — it is the
induction step of Lemma 3.12 refusing to be a dominance step.

Only rows `0` and `1` are ever inspected: the lex witness is row `0`, and dominance
already fails at the partial sum over `{0, 1}`. -/
theorem dom_fails_lex_holds : (nu411 >ₗ lam33) ∧ ¬ partitionDom nu411 lam33 := by
  refine ⟨⟨0, fun s hs => absurd hs (Nat.not_lt_zero s), ?_⟩, ?_⟩
  · simp
  · intro hdom
    have h := hdom 2
    simp only [Finset.sum_range_succ, Finset.sum_range_zero, rowLen_lam33_zero,
      rowLen_lam33_one, rowLen_nu411_zero, rowLen_nu411_one] at h
    omega

/-- The dominance bridge is therefore **strictly** one-directional. -/
theorem partitionDom_not_iff_lexGt :
    ¬ (∀ μ ν : YoungDiagram, μ >ₗ ν → partitionDom μ ν) := fun h =>
  dom_fails_lex_holds.2 (h _ _ dom_fails_lex_holds.1)

end QOU.BraidKnot.PartitionLex
