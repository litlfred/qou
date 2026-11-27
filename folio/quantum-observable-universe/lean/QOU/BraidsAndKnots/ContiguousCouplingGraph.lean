/-
# A contiguous `3A` layout couples only CONSECUTIVE nucleons — so it carries a
# path, never the complete graph

`LayoutConflict.lean` proves that ONE interface `(k, k+1)` admits at most one
single-generator coupling, which is what the colour-tube deficit needed. This
file asks the neighbouring question the binding producer forces, and the answer
is stronger: **which nucleon PAIRS can be coupled at all.**

## Why this is asked (bean `qou-w6x3`; option 2 of `qou-hxz4` / PR #7173)

PR #7160 proved that a *level-local* braid word — one whose letters group into
consecutive blocks with pairwise disjoint generator sets — has a dimension-free
seminormal character. PR #7173 measured that the words
`hecke_core_legacy.unified_iterative_correction` hands its Rust kernel are NOT
level-local, and named the **fixed-`H_k` embedding** as the cause. Its option 2
was to re-embed on `3A` strands, the layout `atom_braid_word_3A` uses, where
nucleon `k` owns strands `3k, 3k+1, 3k+2` and its intra-nucleon crossings are
the single generators `σ_{3k}`, `σ_{3k+1}`.

The obstruction turns out not to be the cycling at all. Measured
(`computations/probes/binding_word_3A_reembedding_probe.py`, 18/18):

* the binding producer emits **one inter-nucleon letter per (new nucleon,
  earlier nucleon) pair** — `C(A,2)` of them, the **complete graph `K_A`**;
* `atom_braid_word_3A` emits its bond only between consecutive nucleons —
  `A-1` of them, the **path `P_A`**.

This file proves that the second is all a contiguous layout can supply.

## What is proved here, and what is measurement

**Proved here, for every `A`:** a single-generator coupling exists between
nucleons `i` and `j` only when they are consecutive (`coupling_forces_consecutive`);
hence a coupling relation containing every pair forces `A ≤ 2`
(`complete_coupling_forces_A_le_two`). Two arithmetic gaps are recorded
alongside: `C(A,2) > A-1` for `A ≥ 3` (`pair_count_exceeds_path_for_three_or_more`),
and `C(A,2) > 3A-1` for `A ≥ 7` (`pair_count_exceeds_adjacency_budget`) — the
latter is layout-free, since a linear arrangement of `3A` strands has only
`3A-1` adjacent pairs at all, so it excludes `K_A` for `A ≥ 7` even after
contiguity is abandoned.

Nothing here needs `q`, and nothing here is about energies.

**Measurement, and NOT proved here:** that the escape route — coupling a
non-adjacent pair by conjugating a boundary crossing — collapses the
segmentation from the mass word's `2A-1` segments of largest size 2 to three
segments whose largest holds `3A-3` of `3A-1` generators, and costs 118× at
`A = 3`; and that the re-embedding **moves the character** (9 of the 11
partitions of 6, at `A = 2` where both embeddings exist). Those are the probe's,
in `computations/probes/binding-word-3A-reembedding.witness.json`.
-/

import Mathlib.Data.Finset.Card
import Mathlib.Tactic

namespace QOU.Hecke.ContiguousCouplingGraph

/-- The block of `C` consecutive strand positions starting at `p`. Same shape as
`LayoutConflict.block`; restated so this file stands alone. -/
def block (p C : ℕ) : Finset ℕ := Finset.Ico p (p + C)

lemma mem_block {p C x : ℕ} : x ∈ block p C ↔ p ≤ x ∧ x < p + C := by
  simp [block]

/-- Nucleon `k`'s three strands in the canonical `atom_braid_word_3A` layout:
positions `3k`, `3k+1`, `3k+2`. -/
abbrev nucleonBlock (k : ℕ) : Finset ℕ := block (3 * k) 3

/-- `x` is the lower endpoint of a single-generator coupling between nucleons
`i` and `j`: the generator `σ_x` crosses strands `x` and `x+1`, so a coupling
puts `x` in nucleon `i` and `x+1` in nucleon `j`.

This is `LayoutConflict.IsCoupling` with the second nucleon left FREE rather
than fixed to `i+1` — which is the whole point, since the binding word needs
couplings between nucleons that are not neighbours. -/
def IsCoupling (i j x : ℕ) : Prop :=
  x ∈ nucleonBlock i ∧ x + 1 ∈ nucleonBlock j

/-- **The obstruction.** A single generator can only couple CONSECUTIVE
nucleons: a generator crosses two adjacent strands, blocks are three wide, so
reaching from nucleon `i` into a nucleon above it lands in `i+1` and nowhere
further.

Everything else in this file is arithmetic on top of this. -/
theorem coupling_forces_consecutive {i j x : ℕ} (h : IsCoupling i j x)
    (hij : i < j) : j = i + 1 := by
  obtain ⟨hx, hy⟩ := h
  rw [mem_block] at hx hy
  omega

/-- Contrapositive, in the form the counting argument uses: nucleons two or more
apart admit **no** single-generator coupling, in either direction. -/
theorem no_coupling_of_gap_two {i j x : ℕ} (hgap : i + 2 ≤ j) :
    ¬ IsCoupling i j x ∧ ¬ IsCoupling j i x := by
  constructor
  · intro h
    have : j = i + 1 := coupling_forces_consecutive h (by omega)
    omega
  · intro h
    obtain ⟨hx, hy⟩ := h
    rw [mem_block] at hx hy
    omega

/-- The unordered coupling relation: nucleons `i` and `j` are coupled when some
generator crosses a strand of one with a strand of the other. -/
def Coupled (i j : ℕ) : Prop := ∃ x, IsCoupling i j x ∨ IsCoupling j i x

/-- Coupled nucleons are adjacent in the layout order — the coupling graph of a
contiguous `3A` layout is contained in the **path** `P_A`. -/
theorem coupled_forces_adjacent {i j : ℕ} (h : Coupled i j) (hne : i ≠ j) :
    j = i + 1 ∨ i = j + 1 := by
  obtain ⟨x, hx | hx⟩ := h
  · rcases lt_or_gt_of_ne hne with hlt | hgt
    · exact Or.inl (coupling_forces_consecutive hx hlt)
    · obtain ⟨ha, hb⟩ := hx
      rw [mem_block] at ha hb
      omega
  · rcases lt_or_gt_of_ne hne with hlt | hgt
    · obtain ⟨ha, hb⟩ := hx
      rw [mem_block] at ha hb
      omega
    · exact Or.inr (coupling_forces_consecutive hx hgt)

/-- **The binding producer's coupling is unreachable.** If every pair of the `A`
nucleons is coupled — which is exactly what `_step_chain_generic` emits, one
inter-nucleon letter per (new nucleon, earlier nucleon) pair — then `A ≤ 2`.

So the deuteron re-embeds and nothing above it does: at `A = 2` the single pair
`{0,1}` IS the one adjacency, while from `A = 3` the pair `{0,2}` has no
generator to sit on. -/
theorem complete_coupling_forces_A_le_two {A : ℕ}
    (h : ∀ i j, i < A → j < A → i ≠ j → Coupled i j) : A ≤ 2 := by
  by_contra hA
  push_neg at hA
  have h02 : Coupled 0 2 := h 0 2 (by omega) (by omega) (by omega)
  have := coupled_forces_adjacent h02 (by omega)
  omega

/-- The counting gap the theorem above expresses: a contiguous layout supplies
`A-1` couplings (the path), and the all-pairs coupling needs `C(A,2)`. Stated
without division as `2·(A-1) < A·(A-1)`, which is the same inequality. -/
theorem pair_count_exceeds_path_for_three_or_more {A : ℕ} (hA : 3 ≤ A) :
    2 * (A - 1) < A * (A - 1) := by
  have h1 : 1 ≤ A - 1 := by omega
  have h2 : 2 < A := by omega
  calc 2 * (A - 1) < A * (A - 1) := by
        exact Nat.mul_lt_mul_of_lt_of_le h2 (le_refl _) h1

/-- **The layout-free bound**, which survives dropping contiguity. A linear
arrangement of `3A` strands has only `3A-1` adjacent position pairs, and each
can carry at most one nucleon pair, so no layout whatever realises the complete
coupling once `C(A,2) > 3A-1` — that is, from `A = 7`, which is `⁷Li`.

Stated without division as `2·(3A-1) < A·(A-1)`. At `A = 7` this is `40 < 42`;
the exhaustive search in the probe agrees, finding witnesses for `A = 2 … 6` and
none at `A = 7`. -/
theorem pair_count_exceeds_adjacency_budget {A : ℕ} (hA : 7 ≤ A) :
    2 * (3 * A - 1) < A * (A - 1) := by
  obtain ⟨m, rfl⟩ : ∃ m, A = 7 + m := ⟨A - 7, by omega⟩
  have h1 : 7 + m - 1 = 6 + m := by omega
  have h2 : 3 * (7 + m) - 1 = 20 + 3 * m := by omega
  rw [h1, h2]
  have hexp : (7 + m) * (6 + m) = 42 + 13 * m + m * m := by ring
  rw [hexp]
  have hsq : 0 ≤ m * m := Nat.zero_le _
  omega


/-- **Exact characterization of inter-nucleon single-generator coupling in the contiguous `3A` layout (`qou-8274`).**
For distinct nucleons `i ≠ j`, a strand index `x` couples nucleon `i` to nucleon `j` (`IsCoupling i j x`)
if and only if `x = 3 * i + 2` (the upper boundary strand of nucleon `i`) and `j = i + 1`. -/
theorem isCoupling_of_ne_iff_boundary_strand {i j x : ℕ} (hne : i ≠ j) :
    IsCoupling i j x ↔ x = 3 * i + 2 ∧ j = i + 1 := by
  unfold IsCoupling nucleonBlock
  rw [mem_block, mem_block]
  omega

/-- **Every consecutive nucleon pair `(i, i + 1)` is coupled at strand `3i + 2` (`qou-8274`).** -/
theorem coupled_consecutive_pair (i : ℕ) :
    IsCoupling i (i + 1) (3 * i + 2) ∧ Coupled i (i + 1) := by
  have h : IsCoupling i (i + 1) (3 * i + 2) :=
    (isCoupling_of_ne_iff_boundary_strand (by omega)).mpr ⟨rfl, rfl⟩
  exact ⟨h, ⟨3 * i + 2, Or.inl h⟩⟩

end QOU.Hecke.ContiguousCouplingGraph
