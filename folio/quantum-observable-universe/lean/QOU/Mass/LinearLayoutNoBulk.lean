import QOU.Mass.CoordinationBulkCriterion
import Mathlib.Combinatorics.SimpleGraph.DegreeSum
import Mathlib.Logic.Relation
import Mathlib.Tactic

/-!
# A linear layout has no bulk — the invariant that decides Avenue 2

Bean `qou-brng`, Avenue 2 (owner, 2026-09-08): *"both derived edge sets on main are affine and an
affine count can never be a surface term, so ask what edge set has a bulk at all; that is
decidable by a proved invariant rather than a fit."*

The framework's nuclear encoding lays the `A` nucleon blocks on a **line** of `3A` strands
(`mass_at_3A_proper.atom_braid_word_3A`: block `k` on strands `3k, 3k+1, 3k+2`, every
inter-nucleon letter at generator `3k+2`, i.e. between blocks `k` and `k+1` of the ordering).
Whatever the ordering, whatever the multiplicities, the nucleon pairs that ever cross are pairs
**consecutive in the ordering**. So the coordination graph `G` of any word this constructor can
produce is a **linear-layout graph**: a subgraph of the path on the ordering. This file proves
what such a graph can and cannot be, over `Fin n` with Mathlib's `SimpleGraph`:

* `degree_le_two` — every vertex has at most two neighbours (`k−1` and `k+1`);
* `not_linearLayout_of_degree_ge_three`, `card_edgeFinset_le` — any graph with a vertex of degree
  `≥ 3`, or with more than `n` edges, is **not** a linear-layout graph. The corpus's one bulk-carrying edge set — the max-contact sphere packing,
  degree up to 12 (`MaxContactHasBulk`) — is therefore **not expressible** by this encoding, for
  any `A ≥ 4`; neither is the complete graph the pyhecke normal-form count corresponds to;
* `chained_linearLayout_adj_succ` — a **connected** linear-layout graph contains every
  consecutive edge, i.e. it is the whole path (a missing edge `{k, k+1}` disconnects `k` from
  `k+1`: no chain of adjacencies in a subgraph of the path crosses it);
* `card_edgeFinset_eq` — hence its bond count is exactly `n − 1`: affine, the `p = 1` law
  (`CoordinationBulkCriterion.chain_is_affine`);
* `surface_eq_two` — and its surface count (vertices with fewer than two neighbours) is exactly
  `2` for every `n ≥ 2`;
* `linearLayout_family_not_hasBulk` — so a family of connected linear-layout graphs, one per
  `A`, has a surface count with **no bulk** in the sense of
  `CoordinationBulkCriterion.HasBulk` (`A_surf → ∞` and `A_surf / A → 0`).

Connectivity is stated as `Chained`: every two vertices are joined by a chain of adjacencies
(`Relation.ReflTransGen G.Adj`). That is what `SimpleGraph.Connected` means (a walk is such a
chain); it is spelled out here so the file depends on nothing but the adjacency relation.

**What this closes.** Within the framework's encoding — every word `atom_braid_word_3A` can build,
for every ordering — **no edge set has a bulk**: a connected assembly is the path (surface `2`,
no bulk); a disconnected one is a disjoint union of paths, whose surface count is twice its
component count, so a "bulk" there would be fragmentation into unboundedly many chains, which
the closure of a single braid word is not. The scope-(a) narrowing of
`2026-09-05-coordination-bulk-criterion.md` §5(i) — *"no affine edge set has a bulk"* — becomes
scope-(b) over the encoding: **no edge set the encoding can express has a bulk**, invariant =
linear layout. A bulk needs a non-linear layout (a strand interleaving that lets one block touch
three or more others), and the corpus derives no such layout; choosing one to reproduce the
surface term would be selection against the target.

Base type: `Fin n`, Mathlib `SimpleGraph`; no `ℝ` in the graph theory. `ℝ` enters only in the
last theorem, through the corpus's real-valued `HasBulk`.
-/

namespace QOU.Mass.LinearLayoutNoBulk

open SimpleGraph Finset

/-- A graph on `Fin n` is a *linear layout* if every edge joins consecutive vertices. -/
def LinearLayout {n : ℕ} (G : SimpleGraph (Fin n)) : Prop :=
  ∀ i j : Fin n, G.Adj i j → (i.val + 1 = j.val ∨ j.val + 1 = i.val)

/-- Every two vertices are joined by a chain of adjacencies (connectedness, spelled out as the
reflexive-transitive closure of `G.Adj`). -/
def Chained {n : ℕ} (G : SimpleGraph (Fin n)) : Prop :=
  ∀ u w : Fin n, Relation.ReflTransGen G.Adj u w

variable {n : ℕ} (G : SimpleGraph (Fin n)) [DecidableRel G.Adj]

/-- The predecessor filter `{w | w + 1 = v}` has one element if `0 < v`, none otherwise. -/
theorem card_filter_pred (v : Fin n) :
    (Finset.univ.filter fun w : Fin n => w.val + 1 = v.val).card =
      if 0 < v.val then 1 else 0 := by
  split_ifs with h
  · rw [Finset.card_eq_one]
    refine ⟨⟨v.val - 1, by omega⟩, ?_⟩
    ext w
    simp only [mem_filter, mem_univ, true_and, mem_singleton]
    constructor
    · intro hw
      exact Fin.ext (by show w.val = v.val - 1; omega)
    · rintro rfl
      show v.val - 1 + 1 = v.val
      omega
  · rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
    intro w _
    omega

/-- The successor filter `{w | v + 1 = w}` has one element if `v + 1 < n`, none otherwise. -/
theorem card_filter_succ (v : Fin n) :
    (Finset.univ.filter fun w : Fin n => v.val + 1 = w.val).card =
      if v.val + 1 < n then 1 else 0 := by
  split_ifs with h
  · rw [Finset.card_eq_one]
    refine ⟨⟨v.val + 1, h⟩, ?_⟩
    ext w
    simp only [mem_filter, mem_univ, true_and, mem_singleton]
    constructor
    · intro hw
      exact Fin.ext (by show w.val = v.val + 1; omega)
    · rintro rfl
      rfl
  · rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
    intro w _
    omega

/-- The neighbours of `v` in a linear layout lie in `{v−1, v+1}`, so there are at most two. -/
theorem degree_le_two (hL : LinearLayout G) (v : Fin n) : G.degree v ≤ 2 := by
  have hsub : G.neighborFinset v ⊆
      (Finset.univ.filter fun w : Fin n => w.val + 1 = v.val) ∪
      (Finset.univ.filter fun w : Fin n => v.val + 1 = w.val) := by
    intro w hw
    rw [mem_neighborFinset] at hw
    rcases hL v w hw with h | h
    · exact mem_union_right _ (mem_filter.mpr ⟨mem_univ _, h⟩)
    · exact mem_union_left _ (mem_filter.mpr ⟨mem_univ _, h⟩)
  calc G.degree v = (G.neighborFinset v).card := rfl
    _ ≤ _ := Finset.card_le_card hsub
    _ ≤ _ + _ := Finset.card_union_le _ _
    _ ≤ 1 + 1 := by
      rw [card_filter_pred, card_filter_succ]
      split_ifs <;> omega

/-- A vertex of degree three or more is impossible in a linear layout: the max-contact packing
(degree up to 12) and the complete graph (degree `n − 1`) are not linear-layout graphs. -/
theorem not_linearLayout_of_degree_ge_three (v : Fin n) (hv : 3 ≤ G.degree v) :
    ¬ LinearLayout G := fun hL => by
  have := degree_le_two G hL v
  omega

/-- **Any linear layout has at most `n` edges** (degree sum `≤ 2n`). So an edge set with more
than `n` bonds — the max-contact / deltahedron count `3n − 6` for `n ≥ 4`, the complete graph's
`n(n−1)/2` for `n ≥ 4`, the sub-affine true packing's `≈ 6n` — is not a linear-layout graph, and
the encoding cannot express it. -/
theorem card_edgeFinset_le (hL : LinearLayout G) : G.edgeFinset.card ≤ n := by
  have hsum := G.sum_degrees_eq_twice_card_edges
  have hle : ∑ v : Fin n, G.degree v ≤ ∑ _v : Fin n, 2 :=
    Finset.sum_le_sum fun v _ => degree_le_two G hL v
  simp only [Finset.sum_const, card_univ, Fintype.card_fin, smul_eq_mul] at hle
  omega

/-- An edge set with more than `n` bonds is not a linear layout. -/
theorem not_linearLayout_of_card_edge_gt (h : n < G.edgeFinset.card) : ¬ LinearLayout G :=
  fun hL => absurd (card_edgeFinset_le G hL) (not_le.mpr h)

omit [DecidableRel G.Adj] in
/-- In a linear layout with the edge `{k, k+1}` absent, no chain of adjacencies from a vertex
`≤ k` ever reaches a vertex `> k`. -/
theorem chain_le_of_missing_edge (hL : LinearLayout G) (k : ℕ)
    (hmiss : ∀ i j : Fin n, i.val = k → j.val = k + 1 → ¬ G.Adj i j) :
    ∀ {u w : Fin n}, Relation.ReflTransGen G.Adj u w → u.val ≤ k → w.val ≤ k := by
  intro u w p
  induction p with
  | refl => exact id
  | @tail b c _ hbc ih =>
    intro hu
    have hb := ih hu
    rcases hL b c hbc with h | h
    · -- c = b + 1: if b = k this would be the missing edge
      by_contra hc'
      exact hmiss b c (by omega) (by omega) hbc
    · omega

omit [DecidableRel G.Adj] in
/-- A **connected** linear-layout graph contains every consecutive edge: it is the whole path. -/
theorem chained_linearLayout_adj_succ (hL : LinearLayout G) (hc : Chained G)
    (i j : Fin n) (hij : i.val + 1 = j.val) : G.Adj i j := by
  by_contra hne
  have hmiss : ∀ a b : Fin n, a.val = i.val → b.val = i.val + 1 → ¬ G.Adj a b := by
    intro a b ha hb hab
    have ha' : a = i := Fin.ext ha
    have hb' : b = j := Fin.ext (by omega)
    subst ha' hb'
    exact hne hab
  have := chain_le_of_missing_edge G hL i.val hmiss (hc i j) le_rfl
  omega

omit [DecidableRel G.Adj] in
/-- Adjacency in a connected linear layout is exactly consecutiveness. -/
theorem adj_iff (hL : LinearLayout G) (hc : Chained G) (i j : Fin n) :
    G.Adj i j ↔ (i.val + 1 = j.val ∨ j.val + 1 = i.val) := by
  constructor
  · exact hL i j
  · rintro (h | h)
    · exact chained_linearLayout_adj_succ G hL hc i j h
    · exact (chained_linearLayout_adj_succ G hL hc j i h).symm

/-- The degree of `v` in a connected linear layout: one for each existing neighbour
`v − 1`, `v + 1`. -/
theorem degree_eq (hL : LinearLayout G) (hc : Chained G) (v : Fin n) :
    G.degree v = (if 0 < v.val then 1 else 0) + (if v.val + 1 < n then 1 else 0) := by
  have hN : G.neighborFinset v =
      (Finset.univ.filter fun w : Fin n => w.val + 1 = v.val) ∪
      (Finset.univ.filter fun w : Fin n => v.val + 1 = w.val) := by
    ext w
    simp only [mem_neighborFinset, mem_union, mem_filter, mem_univ, true_and]
    rw [adj_iff G hL hc]
    exact Or.comm
  have hdisj : Disjoint (Finset.univ.filter fun w : Fin n => w.val + 1 = v.val)
      (Finset.univ.filter fun w : Fin n => v.val + 1 = w.val) := by
    rw [Finset.disjoint_left]
    intro w h1 h2
    have := (mem_filter.mp h1).2
    have := (mem_filter.mp h2).2
    omega
  calc G.degree v = (G.neighborFinset v).card := rfl
    _ = _ := by rw [hN, Finset.card_union_of_disjoint hdisj, card_filter_pred, card_filter_succ]

/-- `#{v : Fin n | 0 < v} = n − 1`. -/
theorem card_filter_pos (hn : 1 ≤ n) :
    (Finset.univ.filter fun v : Fin n => 0 < v.val).card = n - 1 := by
  have h := Finset.filter_card_add_filter_neg_card_eq_card
    (s := (Finset.univ : Finset (Fin n))) (fun v : Fin n => 0 < v.val)
  have hneg : (Finset.univ.filter fun v : Fin n => ¬ 0 < v.val).card = 1 := by
    rw [Finset.card_eq_one]
    refine ⟨⟨0, by omega⟩, ?_⟩
    ext w
    simp only [mem_filter, mem_univ, true_and, mem_singleton]
    constructor
    · intro hw
      exact Fin.ext (by show w.val = 0; omega)
    · rintro rfl
      show ¬ 0 < 0
      omega
  rw [card_univ, Fintype.card_fin] at h
  omega

/-- `#{v : Fin n | v + 1 < n} = n − 1`. -/
theorem card_filter_lt (hn : 1 ≤ n) :
    (Finset.univ.filter fun v : Fin n => v.val + 1 < n).card = n - 1 := by
  have h := Finset.filter_card_add_filter_neg_card_eq_card
    (s := (Finset.univ : Finset (Fin n))) (fun v : Fin n => v.val + 1 < n)
  have hneg : (Finset.univ.filter fun v : Fin n => ¬ v.val + 1 < n).card = 1 := by
    rw [Finset.card_eq_one]
    refine ⟨⟨n - 1, by omega⟩, ?_⟩
    ext w
    simp only [mem_filter, mem_univ, true_and, mem_singleton]
    constructor
    · intro hw
      exact Fin.ext (by show w.val = n - 1; omega)
    · rintro rfl
      show ¬ n - 1 + 1 < n
      omega
  rw [card_univ, Fintype.card_fin] at h
  omega

/-- **Bond count of a connected linear layout is `n − 1`** — affine in `n`, the `p = 1` law. -/
theorem card_edgeFinset_eq (hL : LinearLayout G) (hc : Chained G) (hn : 1 ≤ n) :
    G.edgeFinset.card = n - 1 := by
  have hsum := G.sum_degrees_eq_twice_card_edges
  have hdeg : ∑ v : Fin n, G.degree v = 2 * (n - 1) := by
    simp_rw [degree_eq G hL hc]
    rw [Finset.sum_add_distrib, Finset.sum_boole, Finset.sum_boole, Nat.cast_id, Nat.cast_id,
      card_filter_pos hn, card_filter_lt hn]
    omega
  omega

/-- The **surface** of a graph: the number of vertices with fewer than two neighbours. -/
def surface : ℕ := (Finset.univ.filter fun v : Fin n => G.degree v ≤ 1).card

/-- **Surface count of a connected linear layout is `2`** for every `n ≥ 2`: the two ends of the
path. Constant — the shape `CoordinationBulkCriterion.boundedSurface_not_hasBulk` rules out. -/
theorem surface_eq_two (hL : LinearLayout G) (hc : Chained G) (hn : 2 ≤ n) :
    surface G = 2 := by
  unfold surface
  have hset : (Finset.univ.filter fun v : Fin n => G.degree v ≤ 1) =
      {(⟨0, by omega⟩ : Fin n), ⟨n - 1, by omega⟩} := by
    ext v
    simp only [mem_filter, mem_univ, true_and, mem_insert, mem_singleton, Fin.ext_iff,
      degree_eq G hL hc]
    split_ifs <;> omega
  rw [hset, Finset.card_pair]
  intro h
  have := congrArg Fin.val h
  simp only at this
  omega

/-- **No family of connected linear-layout graphs has a bulk.** Take one such graph `G A` on
`Fin A` for every `A`; its surface count is `2` from `A = 2` on, so it neither diverges nor is
`o(A)`. This is the scope-(b) closure of Avenue 2 over the framework's encoding: the invariant is
linear layout, and every word `atom_braid_word_3A` builds has it. -/
theorem linearLayout_family_not_hasBulk
    (G : ∀ A : ℕ, SimpleGraph (Fin A)) [∀ A, DecidableRel (G A).Adj]
    (hL : ∀ A, LinearLayout (G A)) (hc : ∀ A, Chained (G A)) :
    ¬ CoordinationBulkCriterion.HasBulk (fun A : ℝ => (surface (G ⌊A⌋₊) : ℝ)) := by
  rintro ⟨hdiv, _⟩
  obtain ⟨A, hA3, hA2⟩ :=
    ((hdiv.eventually_ge_atTop 3).and (Filter.eventually_ge_atTop (2 : ℝ))).exists
  have hfloor : 2 ≤ ⌊A⌋₊ := Nat.le_floor (by exact_mod_cast hA2)
  rw [surface_eq_two (G ⌊A⌋₊) (hL _) (hc _) hfloor] at hA3
  norm_num at hA3

/-- **Vanishing difference form of `surface_eq_two` (`qou-5ax1`).**
For a connected linear-layout graph `G` on `Fin n` with `2 ≤ n`, `surface G - 2 = 0`. -/
theorem surface_sub_two_eq_zero (hL : LinearLayout G) (hc : Chained G) (hn : 2 ≤ n) :
    surface G - 2 = 0 := by
  rw [surface_eq_two G hL hc hn]

end QOU.Mass.LinearLayoutNoBulk
