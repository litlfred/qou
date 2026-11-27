import Mathlib.Data.List.Basic
import Mathlib.Tactic

/-!
# `QOU.OptionE.CrystalGraph` — Kashiwara crystal graph structure

**Option E infrastructure file 1/4** — basic crystal-graph
data structures.

The Kashiwara crystal of `sl_n` at level 1 is a directed graph
with vertex set = semistandard Young tableaux + edge set encoding
the action of the Chevalley generators `e_i`, `f_i` at the q → 0
limit ([kashiwara1991]).

For QOU's purposes:
- **Vertex set**: standard Young tableaux of shape `λ ⊢ n`
  (we restrict to SYT for the seminormal basis correspondence).
- **Crystal arrows**: per-strand `f_i` operations on the tableau.
- **Crystal weight**: a function `wt : V → ℤ^r` encoding the
  height in each `i`-string.

This file provides the abstract structure; concrete crystal
graphs for specific partitions live in `DeuteronVerification.lean`.

Refs:
- [kashiwara1991] DOI 10.1215/S0012-7094-91-06321-0
- [lecouvey2007] DOI 10.1016/j.jalgebra.2007.07.002
-/

namespace QOU.OptionE.CrystalGraph

/-- A **crystal vertex** for `sl_n` at partition `λ ⊢ n`:
    represented abstractly by an index. For concrete crystals,
    this index ranges over standard Young tableaux. -/
structure CrystalVertex (n : ℕ) where
  /-- Vertex index (in [0, dim_SYT(λ))). -/
  idx : ℕ
deriving DecidableEq

/-- A **crystal arrow** of color `i ∈ [0, rank)`: directed edge
    `src → dst` indicating `f_i(src) = dst` in the crystal. -/
structure CrystalArrow (n : ℕ) where
  src : CrystalVertex n
  color : ℕ  -- i ∈ [0, rank), where rank = n - 1 for sl_n
  dst : CrystalVertex n
deriving DecidableEq

/-- **Crystal graph** for `sl_n` at partition `λ ⊢ n`: a finite
    structure with vertex count + edge list. -/
structure CrystalGraph (n : ℕ) where
  /-- Number of vertices (= number of SYT of shape λ). -/
  vertexCount : ℕ
  /-- Edge list (directed). -/
  edges : List (CrystalArrow n)
  /-- All vertex indices are within bounds. -/
  vertices_well_formed : ∀ e ∈ edges,
    e.src.idx < vertexCount ∧ e.dst.idx < vertexCount

/-- **The trivial crystal graph** for `n = 1` (single vertex, no
    edges). -/
def trivial_crystal : CrystalGraph 1 where
  vertexCount := 1
  edges := []
  vertices_well_formed := by intro e he; cases he

/-- Verification: the trivial crystal has vertex count 1. -/
theorem trivial_crystal_vertex_count : trivial_crystal.vertexCount = 1 := rfl

/-- Verification: the trivial crystal has no edges. -/
theorem trivial_crystal_no_edges : trivial_crystal.edges = [] := rfl

/-- **The 2-vertex crystal** for `sl_2` at the standard partition
    (the simplest non-trivial case). One edge `0 → 1` of color 0
    encodes the single `f_0` operation. -/
def sl2_standard_crystal : CrystalGraph 2 where
  vertexCount := 2
  edges := [⟨⟨0⟩, 0, ⟨1⟩⟩]
  vertices_well_formed := by
    intro e he
    simp at he
    rcases he with rfl
    refine ⟨?_, ?_⟩ <;> decide

/-- Verification: sl_2 standard crystal has 2 vertices, 1 edge. -/
theorem sl2_standard_crystal_vertex_count :
    sl2_standard_crystal.vertexCount = 2 := rfl

theorem sl2_standard_crystal_edge_count :
    sl2_standard_crystal.edges.length = 1 := rfl

end QOU.OptionE.CrystalGraph
