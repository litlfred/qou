import QOU.Mass.LinearLayoutNoBulk
import QOU.OneDim.GammaGammaForcesTheLayout

/-!
# A γγ word on the contiguous layout has a linear-layout coordination graph

Bean `qou-brng` (owner pick 2026-11-15, "Both, salvage then Lean").
`QOU/OneDim/GammaGammaForcesTheLayout.lean` derives the contiguous strand layout from the
γγ vertex but, as its own docstring says, never produces the predicate
`QOU.Mass.LinearLayoutNoBulk.LinearLayout`, which lives on `SimpleGraph (Fin n)`. This file is
that missing bridge.

## Statement

The nucleon blocks sit on the strand line contiguously: block `k` holds strands `3k, 3k+1,
3k+2`, so strand `s` belongs to block `s / 3`. A letter of the word touches a run of strands
`{i, …, i + w}`:

* a single crossing `σᵢ` touches `{i, i+1}` (`w = 1`);
* a γγ vertex `[σᵢ, σᵢ₊₁⁻¹]` touches `vertexStrands i = {i, i+1, i+2}` (`w = 2`).

Two blocks are **coordinated** when some letter touches a strand of each. The point is
arithmetic: a run of at most three consecutive strands meets **at most two** blocks of three
consecutive strands, and if it meets two they are consecutive (`run_blocks_adjacent`). So the
coordination graph of **any** word whose letters are such runs is a linear layout
(`coordGraph_linearLayout`), and by `QOU.Mass.LinearLayoutNoBulk` every block then has at most
two neighbours (`coordGraph_degree_le_two`).

The γγ case is `gammaGammaGraph_linearLayout`: whatever list of vertex positions a γγ
selection produces, internal or straddling a block boundary, its coordination graph on the
contiguous layout is a linear layout. Mixing γγ vertices with single crossings (the production
word's `g_{3k+2}` interface letters) changes nothing, since both are runs of width `≤ 2`.

## Scope

* The block assignment `s ↦ s / 3` **is** the contiguous layout; this file takes it as the
  definition, as `GammaGammaForcesTheLayout` derives it. It says nothing about other layouts:
  `residue_layout_is_the_excluded_triangle` there shows the residue layout is not linear.
* `vertexStrands` is the hand-transcribed strand support of `GammaGammaWordSelection.vertex`,
  flagged as such in `GammaGammaForcesTheLayout`. Formalising `support (vertex i)` remains open.
* A width-`3` run (e.g. `σᵢσᵢ₊₁σᵢ₊₂`) can meet three blocks only if it straddles two
  boundaries, which needs four strands; `run_blocks_adjacent` is sharp at `w ≤ 2`, and
  `wide_run_meets_three_blocks` shows `w = 4` already fails.

Pure `ℕ` / `Fin n` arithmetic: no `ℝ`, no `q`, no data.
-/

namespace QOU.OneDim.GammaGammaLinearLayout

open QOU.Mass.LinearLayoutNoBulk
open QOU.OneDim.GammaGammaForcesTheLayout

/-- The contiguous layout: strand `s` belongs to block `s / 3`. -/
def blockOf (s : ℕ) : ℕ := s / 3

/-- **The arithmetic core.** Two strands in a run of at most three consecutive strands lie in
the same block or in consecutive blocks. -/
theorem run_blocks_adjacent {i w x y : ℕ} (hw : w ≤ 2)
    (hx : i ≤ x ∧ x ≤ i + w) (hy : i ≤ y ∧ y ≤ i + w) :
    blockOf x = blockOf y ∨ blockOf x + 1 = blockOf y ∨ blockOf y + 1 = blockOf x := by
  unfold blockOf
  omega

/-- The bound is sharp in the right place: a run of five strands can meet three blocks. -/
theorem wide_run_meets_three_blocks :
    ∃ i x y : ℕ, i ≤ x ∧ x ≤ i + 4 ∧ i ≤ y ∧ y ≤ i + 4 ∧ blockOf x + 2 = blockOf y :=
  ⟨2, 2, 6, by decide, by decide, by decide, by decide, by decide⟩

/-- A letter, recorded by the run of strands it touches: start `i`, width `w`
(it touches `i, …, i + w`). -/
structure Run where
  start : ℕ
  width : ℕ

/-- Strand `x` is touched by run `r`. -/
def Run.Touches (r : Run) (x : ℕ) : Prop := r.start ≤ x ∧ x ≤ r.start + r.width

/-- The coordination graph of a word on `n` contiguous blocks: distinct blocks `j, k` are
adjacent when some letter touches a strand of each. -/
def coordGraph (n : ℕ) (W : List Run) : SimpleGraph (Fin n) where
  Adj j k := j ≠ k ∧ ∃ r ∈ W, ∃ x y : ℕ, r.Touches x ∧ r.Touches y ∧
    blockOf x = j.val ∧ blockOf y = k.val
  symm := by
    rintro j k ⟨hne, r, hr, x, y, hx, hy, hxj, hyk⟩
    exact ⟨Ne.symm hne, r, hr, y, x, hy, hx, hyk, hxj⟩
  loopless := by
    rintro j ⟨hne, _⟩
    exact hne rfl

/-- **The bridge.** If every letter touches at most three consecutive strands, the coordination
graph on the contiguous layout is a linear layout. -/
theorem coordGraph_linearLayout {n : ℕ} {W : List Run} (hW : ∀ r ∈ W, r.width ≤ 2) :
    LinearLayout (coordGraph n W) := by
  rintro j k ⟨hne, r, hr, x, y, hx, hy, hxj, hyk⟩
  have hjk : j.val ≠ k.val := fun h => hne (Fin.ext h)
  rcases run_blocks_adjacent (hW r hr) hx hy with h | h | h
  · exact absurd (hxj ▸ hyk ▸ h) hjk
  · left; omega
  · right; omega

/-- Hence every block has at most two coordination neighbours. -/
theorem coordGraph_degree_le_two {n : ℕ} {W : List Run} (hW : ∀ r ∈ W, r.width ≤ 2)
    [DecidableRel (coordGraph n W).Adj] (v : Fin n) :
    (coordGraph n W).degree v ≤ 2 :=
  degree_le_two (coordGraph n W) (coordGraph_linearLayout hW) v

/-- A γγ vertex at position `i`, as a run: it touches `vertexStrands i = {i, i+1, i+2}`. -/
def ggRun (i : ℕ) : Run := ⟨i, 2⟩

/-- The run of `ggRun i` is exactly `vertexStrands i`, the support recorded in
`GammaGammaForcesTheLayout`. -/
theorem ggRun_touches_iff (i x : ℕ) : (ggRun i).Touches x ↔ x ∈ vertexStrands i := by
  rw [vertexStrands_eq_triple, mem_triple]
  simp only [Run.Touches, ggRun]
  omega

/-- A single crossing `σᵢ`, as a run: it touches `{i, i+1}`. -/
def crossingRun (i : ℕ) : Run := ⟨i, 1⟩

/-- **γγ words.** For any list of γγ vertex positions, the coordination graph on the contiguous
layout is a linear layout. -/
theorem gammaGammaGraph_linearLayout (n : ℕ) (V : List ℕ) :
    LinearLayout (coordGraph n (V.map ggRun)) := by
  apply coordGraph_linearLayout
  intro r hr
  obtain ⟨i, -, rfl⟩ := List.mem_map.mp hr
  simp [ggRun]

/-- **Mixed words.** γγ vertices together with single crossings (the production word's interface
letters) still give a linear layout. -/
theorem mixedGraph_linearLayout (n : ℕ) (V C : List ℕ) :
    LinearLayout (coordGraph n (V.map ggRun ++ C.map crossingRun)) := by
  apply coordGraph_linearLayout
  intro r hr
  rcases List.mem_append.mp hr with h | h
  · obtain ⟨i, -, rfl⟩ := List.mem_map.mp h; simp [ggRun]
  · obtain ⟨i, -, rfl⟩ := List.mem_map.mp h; simp [crossingRun]

/-- Non-vacuity: a γγ vertex straddling the boundary between blocks `0` and `1`
(position `1`, strands `1, 2, 3`) does coordinate them. -/
theorem straddling_vertex_coordinates :
    (coordGraph 2 [ggRun 1]).Adj ⟨0, by decide⟩ ⟨1, by decide⟩ :=
  ⟨by decide, ggRun 1, List.mem_singleton_self _, 1, 3,
    ⟨by decide, by decide⟩, ⟨by decide, by decide⟩, rfl, rfl⟩

end QOU.OneDim.GammaGammaLinearLayout
