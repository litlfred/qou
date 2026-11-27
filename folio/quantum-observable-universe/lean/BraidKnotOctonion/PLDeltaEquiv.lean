/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLPerturb
import BraidKnotOctonion.PLSubdivide

set_option autoImplicit false

/-!
# General-position single-corner perturbations and elementary Δ-equivalence (#8902, #9114)

Stage 2 of the piecewise-linear knot-topology build compares PL ambient isotopy with
Reidemeister's combinatorial `Δ`-equivalence (`DeltaEquiv`). Per the 2026-11-22 general-position
design (`#9114`, Burde–Zieschang, *Knots*, Prop. 1.10), perturbing a PL isotopy into general
position separates vertex merges so that:

1. off finitely many event times (`PLTies`), vertex counts are constant and the link evolves
   continuously through simple polygons (`PLPerturb.deltaEquiv_of_preconnected`);
2. at each isolated event time `t₁`, **a single corner is born or dies** at an interior point
   `c₀ ∈ openSegment ℝ a b` of one edge `[a, b]`.

This module proves the three combinatorial-topological theorems needed to cross those general-
position event times without `sorry`:

* **`PolygonalLink.eventually_exists_single_deltaMove`**: around *any* interior point
  `c₀ ∈ openSegment ℝ a b` of the closing edge of component `m` of a simple link `L`, there is a
  full neighbourhood `U ∈ 𝓝 c₀` in the ambient normed space `E` such that *every* `c ∈ U` (on or
  off the line `a b`) satisfies all four hypotheses of `PolygonalLink.deltaMove` and executes a
  **single elementary `Move.delta`** from `L`.
* **`PolygonalLink.eventually_deltaEquiv_cornerBirth` / `..._cornerDeath`**: under simultaneous
  continuous motion of **all** vertices of **all** components near a parameter `x₀` where a new
  corner `c(x)` detaches from `c₀ ∈ openSegment ℝ a₀ b₀` into general position, every nearby
  `N`-vertex realization `L_lo` and `(N_m + 1)`-vertex realization `L_hi` satisfy
  `DeltaEquiv L_lo L_hi`.
* **`PolygonalLink.deltaEquiv_across_cornerBirth_Icc` & `deltaEquiv_of_generalPositionChain`**:
  gluing a fixed-count continuous link family on `[t₀, t₁]` to an `(N_m + 1)`-vertex continuous
  link family on `[t₁, t₂]` across a collinear corner birth at `t₁` yields `DeltaEquiv L₀ L₂`, and
  any finite `ReflTransGen GeneralPositionStep` chain of fixed-count intervals and elementary
  corner births/deaths implies `DeltaEquiv`.

Reference: G. Burde, H. Zieschang, *Knots*, 2nd ed., de Gruyter 2003, Prop. 1.10.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

section AffineOpenSegment

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- If `c` lies in the open segment `(a, b)` with `a ≠ b`, then `a` does not lie in `[b, c]`. -/
theorem left_notMem_segment_of_mem_openSegment {a b c : E} (hab : a ≠ b)
    (hc : c ∈ openSegment ℝ a b) : a ∉ segment ℝ b c := by
  obtain ⟨α, β, hα, hβ, hαβ, rfl⟩ := hc
  rw [segment_eq_image']
  rintro ⟨t, ⟨ht0, ht1⟩, ht⟩
  simp only at ht
  have hba : a - b ≠ 0 := sub_ne_zero.mpr hab
  have key : (1 - t * α) • (a - b) = 0 := by
    have e : (1 - t * α) • (a - b) = a - (b + t • ((α • a + β • b) - b)) := by
      have hβ' : β = 1 - α := by linarith
      rw [hβ']
      module
    rw [e, ht, sub_self]
  have hcoef : 1 - t * α = 0 := (smul_eq_zero.mp key).resolve_right hba
  have hα1 : α < 1 := by linarith
  nlinarith

/-- If `c` lies in the open segment `(a, b)` with `a ≠ b`, then `b` does not lie in `[a, c]`. -/
theorem right_notMem_segment_of_mem_openSegment {a b c : E} (hab : a ≠ b)
    (hc : c ∈ openSegment ℝ a b) : b ∉ segment ℝ a c := by
  have hc' : c ∈ openSegment ℝ b a := by rwa [openSegment_symm] at hc
  exact left_notMem_segment_of_mem_openSegment hab.symm hc'

end AffineOpenSegment

section Normed

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

namespace PolygonalLink

/-! ### 1. Open-ball admissibility of a single elementary `Δ`-move -/

/-- **Open-ball `Δ`-move admissibility.** Around any interior point `c₀` of the closing edge
`[a, b]` of component `m`, all four hypotheses of `PolygonalLink.deltaMove` hold on an entire
ambient neighbourhood `𝓝 c₀` in `E`. -/
theorem eventually_deltaMove_conds_nhds (L : PolygonalLink E) (m : Fin L.k) {c₀ : E}
    (hc₀ : c₀ ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) :
    ∀ᶠ c in 𝓝 c₀,
      c ≠ (L.comp m).v (Fin.last _) ∧
      c ≠ (L.comp m).v 0 ∧
      segment ℝ ((L.comp m).v (Fin.last _)) c ∩ segment ℝ c ((L.comp m).v 0) ⊆ {c} ∧
      convexHull ℝ {(L.comp m).v (Fin.last _), (L.comp m).v 0, c} ∩ L.carrier =
        segment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0) := by
  set P := L.comp m
  set a := P.v (Fin.last P.n)
  set b := P.v 0
  have hP : P.IsSimple := L.simple m
  have hab : a ≠ b := hP.v_last_ne_v_zero
  have hc₀a : c₀ ≠ a := fun h => hab (left_mem_openSegment_iff.mp (h ▸ hc₀))
  have hc₀b : c₀ ≠ b := fun h => hab (right_mem_openSegment_iff.mp (h ▸ hc₀))
  have ev_ca : ∀ᶠ c in 𝓝 c₀, c ≠ a := isOpen_ne.mem_nhds hc₀a
  have ev_cb : ∀ᶠ c in 𝓝 c₀, c ≠ b := isOpen_ne.mem_nhds hc₀b
  have ev_seg : ∀ᶠ c in 𝓝 c₀, segment ℝ a c ∩ segment ℝ c b ⊆ {c} := by
    have h0 : segment ℝ c₀ a ∩ segment ℝ c₀ b ⊆ {c₀} := by
      rw [segment_symm ℝ c₀ a]
      exact segment_inter_segment_subset_of_mem_openSegment hab hc₀
    have ev := eventually_segment_inter_segment_subset (X := E) (x₀ := c₀)
      (o := id) (w := fun _ => a) (y := fun _ => b)
      continuous_id continuous_const continuous_const h0 hc₀b.symm hc₀a.symm
    filter_upwards [ev] with c hc
    rw [segment_symm ℝ a c]
    exact hc
  -- Triangle clearance against every edge of every component
  have hconv₀ : convexHull ℝ ({a, b, c₀} : Set E) = segment ℝ a b :=
    convexHull_triple_of_mem_segment (openSegment_subset_segment ℝ a b hc₀)
  have ev_other : ∀ i : Fin L.k, i ≠ m → ∀ j : Fin ((L.comp i).n + 1),
      ∀ᶠ c in 𝓝 c₀, (L.comp i).edge j ∩ convexHull ℝ {a, b, c} ⊆ segment ℝ a b := by
    intro i hi j
    have hdisj : (L.comp i).edge j ∩ convexHull ℝ {a, b, c₀} = ∅ := by
      rw [hconv₀, ← Polygon.edge_last]
      refine eq_empty_iff_forall_notMem.mpr fun x ⟨hx1, hx2⟩ => ?_
      exact Set.disjoint_left.mp (L.disjoint hi)
        ((L.comp i).edge_subset_carrier j hx1) (P.edge_subset_carrier _ hx2)
    filter_upwards [eventually_segment_inter_convexHull_eq_empty (X := E) (x₀ := c₀)
      (a := fun _ => (L.comp i).v j) (b := fun _ => (L.comp i).v ((L.comp i).next j))
      (p := fun _ => a) (q := fun _ => b) (r := id)
      continuous_const continuous_const continuous_const continuous_const continuous_id
      hdisj] with c hc
    simp only [Polygon.edge, id] at hc ⊢
    rw [hc]
    exact empty_subset _
  have ev_same : ∀ j : Fin (P.n + 1),
      ∀ᶠ c in 𝓝 c₀, P.edge j ∩ convexHull ℝ {a, b, c} ⊆ segment ℝ a b := by
    intro j
    by_cases hj : j = Fin.last P.n
    · subst hj
      exact Filter.Eventually.of_forall fun c => by
        rw [Polygon.edge_last]
        exact inter_subset_left
    · have h0 := hP.2 j (Fin.last P.n) hj
      rw [Polygon.edge_last] at h0
      by_cases h1 : Fin.last P.n = P.next j
      · -- Edge `j` ends at `a`
        have hvj_ne : P.v j ≠ a := fun he => hj (hP.1 he)
        have hsub₀ : segment ℝ a (P.v j) ∩ convexHull ℝ {a, b, c₀} ⊆ {a} := by
          rw [hconv₀, segment_symm ℝ a (P.v j)]
          have hej : P.edge j = segment ℝ (P.v j) a := by
            simp only [Polygon.edge, ← h1, a]
          rw [← hej, h0, if_pos h1]
        have ha_not : a ∉ segment ℝ b c₀ :=
          left_notMem_segment_of_mem_openSegment hab hc₀
        have ev := eventually_segment_inter_convexHull_subset (X := E) (x₀ := c₀)
          (o := fun _ => a) (w := fun _ => P.v j) (y := fun _ => b) (z := id)
          continuous_const continuous_const continuous_const continuous_id
          hsub₀ ha_not hvj_ne
        filter_upwards [ev] with c hc
        have hej : P.edge j = segment ℝ a (P.v j) := by
          rw [Polygon.edge, ← h1, segment_symm]
        simp only [id] at hc
        rw [hej]
        exact hc.trans (Set.singleton_subset_iff.mpr (left_mem_segment ℝ a b))
      · by_cases h2 : j = P.next (Fin.last P.n)
        · -- Edge `j` starts at `b = P.v 0`
          have hj0 : j = 0 := h2.trans P.next_last
          have hvn_ne : P.v (P.next 0) ≠ b := fun he =>
            P.next_ne 0 (hP.1 he)
          have hpair : ∀ x : E, ({b, a, x} : Set E) = {a, b, x} := fun x => by
            ext z; simp [or_left_comm]
          have hsub₀ : segment ℝ b (P.v (P.next 0)) ∩ convexHull ℝ {b, a, c₀} ⊆ {b} := by
            rw [hpair c₀, hconv₀]
            have hej : P.edge j = segment ℝ b (P.v (P.next 0)) := by
              simp only [Polygon.edge, hj0, b]
            rw [← hej, h0, if_neg h1, if_pos h2, hj0]
          have hb_not : b ∉ segment ℝ a c₀ :=
            right_notMem_segment_of_mem_openSegment hab hc₀
          have ev := eventually_segment_inter_convexHull_subset (X := E) (x₀ := c₀)
            (o := fun _ => b) (w := fun _ => P.v (P.next 0)) (y := fun _ => a) (z := id)
            continuous_const continuous_const continuous_const continuous_id
            hsub₀ hb_not hvn_ne
          filter_upwards [ev] with c hc
          have hej : P.edge j = segment ℝ b (P.v (P.next 0)) := by
            simp only [Polygon.edge, hj0, b]
          simp only [id] at hc
          rw [hej, ← hpair c]
          exact hc.trans (Set.singleton_subset_iff.mpr (right_mem_segment ℝ a b))
        · -- Non-adjacent edge of `P`
          have hdisj : P.edge j ∩ convexHull ℝ {a, b, c₀} = ∅ := by
            rw [hconv₀, h0, if_neg h1, if_neg h2]
          filter_upwards [eventually_segment_inter_convexHull_eq_empty (X := E) (x₀ := c₀)
            (a := fun _ => P.v j) (b := fun _ => P.v (P.next j))
            (p := fun _ => a) (q := fun _ => b) (r := id)
            continuous_const continuous_const continuous_const continuous_const continuous_id
            hdisj] with c hc
          simp only [Polygon.edge, id] at hc ⊢
          rw [hc]
          exact empty_subset _
  have ev_all_edges : ∀ᶠ c in 𝓝 c₀, ∀ (i : Fin L.k) (j : Fin ((L.comp i).n + 1)),
      (L.comp i).edge j ∩ convexHull ℝ {a, b, c} ⊆ segment ℝ a b := by
    refine Filter.eventually_all.mpr fun i => Filter.eventually_all.mpr fun j => ?_
    by_cases hi : i = m
    · subst hi; exact ev_same j
    · exact ev_other i hi j
  filter_upwards [ev_ca, ev_cb, ev_seg, ev_all_edges] with c hca hcb hseg hall
  refine ⟨hca, hcb, hseg, Subset.antisymm ?_ ?_⟩
  · rintro x ⟨hxT, hxL⟩
    simp only [PolygonalLink.carrier, Polygon.carrier, mem_iUnion] at hxL
    obtain ⟨i, j, hxj⟩ := hxL
    exact hall i j ⟨hxj, hxT⟩
  · intro x hx
    refine ⟨segment_subset_convexHull (by simp) (by simp) hx, ?_⟩
    have hxedge : x ∈ P.edge (Fin.last P.n) := by rwa [Polygon.edge_last]
    exact L.comp_carrier_subset m (P.edge_subset_carrier _ hxedge)

/-- **Every point in a neighbourhood of an interior edge point `c₀` defines a single elementary
`Move.delta` from `L`.** -/
theorem eventually_exists_single_deltaMove (L : PolygonalLink E) (m : Fin L.k) {c₀ : E}
    (hc₀ : c₀ ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) :
    ∀ᶠ c in 𝓝 c₀, ∃ L' : PolygonalLink E,
      ∃ h : L'.k = L.k,
        (∀ i, L'.comp i = Function.update L.comp m ((L.comp m).subdivideLast c) (Fin.cast h i)) ∧
        Move L L' := by
  filter_upwards [L.eventually_deltaMove_conds_nhds m hc₀] with c ⟨hca, hcb, hseg, htri⟩
  exact ⟨L.deltaMove m c hca hcb hseg htri, rfl, fun _ => rfl,
    L.move_deltaMove m c hca hcb hseg htri⟩

/-! ### 2. General-position single-corner birth and death under all-vertex perturbation -/

/-- Increment the vertex count parameter `N` at component `m` by `1`. -/
def bumpCount {k : ℕ} (N : Fin k → ℕ) (m : Fin k) (i : Fin k) : ℕ :=
  if i = m then N m + 1 else N i

/-- Vertex configuration obtained by appending `c` at the end of component `m` of `W`. -/
def insertCornerConfig {k : ℕ} {N : Fin k → ℕ}
    (W : (i : Fin k) → Fin (N i + 3) → E) (m : Fin k) (c : E) (i : Fin k) :
    Fin (bumpCount N m i + 3) → E :=
  if h : i = m then
    fun j => Fin.snoc (α := fun _ => E) (W m) c (Fin.cast (by subst h; simp [bumpCount]) j)
  else
    fun j => W i (Fin.cast (by simp [bumpCount, h]) j)

/-- `insertCollinear` realizes `insertCornerConfig` at the degenerate corner `c₀`. -/
theorem realizes_insertCornerConfig {k : ℕ} {N : Fin k → ℕ}
    {W : (i : Fin k) → Fin (N i + 3) → E} {L : PolygonalLink E}
    (hL : Realizes W L) (m : Fin k) {c : E}
    (hc : c ∈ openSegment ℝ (W m (Fin.last (N m + 2))) (W m 0)) :
    ∃ L_hi : PolygonalLink E, Move L L_hi ∧ Realizes (insertCornerConfig W m c) L_hi := by
  obtain ⟨hk, hcomp⟩ := hL
  set m' : Fin L.k := Fin.cast hk m
  have hm_eq : L.comp m' = polyOf (W m) := hcomp m
  have hva : (L.comp m').v (Fin.last _) = W m (Fin.last (N m + 2)) := by
    cases h : L.comp m' with
    | mk n two_le v =>
      have hn : n = N m + 2 := by
        have := congrArg Polygon.n (h.symm.trans hm_eq)
        simpa [polyOf] using this
      subst hn
      have hv : v = W m := by
        have := h.symm.trans hm_eq
        simpa [polyOf] using this
      simp [hv]
  have hvb : (L.comp m').v 0 = W m 0 := by
    cases h : L.comp m' with
    | mk n two_le v =>
      have hn : n = N m + 2 := by
        have := congrArg Polygon.n (h.symm.trans hm_eq)
        simpa [polyOf] using this
      subst hn
      have hv : v = W m := by
        have := h.symm.trans hm_eq
        simpa [polyOf] using this
      simp [hv]
  have hc' : c ∈ openSegment ℝ ((L.comp m').v (Fin.last _)) ((L.comp m').v 0) := by
    rwa [hva, hvb]
  refine ⟨L.insertCollinear m' c hc', L.move_insertCollinear m' c hc', hk, fun i => ?_⟩
  change Function.update L.comp m' ((L.comp m').subdivideLast c) (Fin.cast hk i) =
    polyOf (insertCornerConfig W m c i)
  by_cases hi : i = m
  · subst hi
    rw [Function.update_self, hm_eq]
    refine Polygon.ext' (by simp [Polygon.subdivideLast, polyOf, bumpCount]) (fun j => ?_)
    simp [Polygon.subdivideLast, polyOf, insertCornerConfig]
  · have hi' : Fin.cast hk i ≠ m' := fun he => hi (Fin.cast_injective hk he)
    rw [Function.update_of_ne hi', hcomp i]
    refine Polygon.ext' (by simp [polyOf, bumpCount, hi]) (fun j => ?_)
    simp [polyOf, insertCornerConfig, hi]

/-- **General-position single-corner birth perturbation (`#9114`).**
Let `V_lo` (`N` vertices) and `V_hi` (`N_m + 1` vertices) vary continuously with `x : X`, such that
at `x₀`, `V_lo x₀` realizes `L₀`, `c₀` lies in the open closing edge of component `m`, and `V_hi x₀`
is `insertCornerConfig (V_lo x₀) m c₀`. Then for all `x` near `x₀` (including `x` where the new
corner moves off the edge into general position), any realizations `L_lo` of `V_lo x` and `L_hi` of
`V_hi x` satisfy `DeltaEquiv L_lo L_hi`. -/
theorem eventually_deltaEquiv_cornerBirth {X : Type*} [TopologicalSpace X] {x₀ : X}
    {k : ℕ} {N : Fin k → ℕ}
    (V_lo : X → (i : Fin k) → Fin (N i + 3) → E)
    (hV_lo : ∀ i, Continuous fun x => V_lo x i)
    {L₀ : PolygonalLink E} (h₀ : Realizes (V_lo x₀) L₀)
    (m : Fin k) {c₀ : E}
    (hc₀ : c₀ ∈ openSegment ℝ (V_lo x₀ m (Fin.last (N m + 2))) (V_lo x₀ m 0))
    (V_hi : X → (i : Fin k) → Fin (bumpCount N m i + 3) → E)
    (hV_hi : ∀ i, Continuous fun x => V_hi x i)
    (h₀_hi : V_hi x₀ = insertCornerConfig (V_lo x₀) m c₀) :
    ∀ᶠ x in 𝓝 x₀, ∀ L_lo L_hi : PolygonalLink E,
      Realizes (V_lo x) L_lo → Realizes (V_hi x) L_hi → DeltaEquiv L_lo L_hi := by
  obtain ⟨L₀_hi, hmove, hreal_hi⟩ := realizes_insertCornerConfig h₀ m hc₀
  have hreal_hi' : Realizes (V_hi x₀) L₀_hi := h₀_hi.symm ▸ hreal_hi
  have ev_lo := eventually_deltaEquiv_realizes V_lo hV_lo h₀
  have ev_hi := eventually_deltaEquiv_realizes V_hi hV_hi hreal_hi'
  filter_upwards [ev_lo, ev_hi] with x hx_lo hx_hi L_lo L_hi hL_lo hL_hi
  exact Relation.EqvGen.trans _ _ _
    (Relation.EqvGen.symm _ _ (hx_lo L_lo hL_lo))
    (Relation.EqvGen.trans _ _ _ (Relation.EqvGen.rel _ _ hmove) (hx_hi L_hi hL_hi))

/-- **General-position single-corner death perturbation (`#9114`).** Symmetric form of
`eventually_deltaEquiv_cornerBirth` when an `(N_m + 1)`-vertex link collapses one corner onto an
open edge at `x₀`. -/
theorem eventually_deltaEquiv_cornerDeath {X : Type*} [TopologicalSpace X] {x₀ : X}
    {k : ℕ} {N : Fin k → ℕ}
    (V_lo : X → (i : Fin k) → Fin (N i + 3) → E)
    (hV_lo : ∀ i, Continuous fun x => V_lo x i)
    {L₀ : PolygonalLink E} (h₀ : Realizes (V_lo x₀) L₀)
    (m : Fin k) {c₀ : E}
    (hc₀ : c₀ ∈ openSegment ℝ (V_lo x₀ m (Fin.last (N m + 2))) (V_lo x₀ m 0))
    (V_hi : X → (i : Fin k) → Fin (bumpCount N m i + 3) → E)
    (hV_hi : ∀ i, Continuous fun x => V_hi x i)
    (h₀_hi : V_hi x₀ = insertCornerConfig (V_lo x₀) m c₀) :
    ∀ᶠ x in 𝓝 x₀, ∀ L_hi L_lo : PolygonalLink E,
      Realizes (V_hi x) L_hi → Realizes (V_lo x) L_lo → DeltaEquiv L_hi L_lo := by
  filter_upwards [eventually_deltaEquiv_cornerBirth V_lo hV_lo h₀ m hc₀ V_hi hV_hi h₀_hi]
    with x hx L_hi L_lo hL_hi hL_lo
  exact Relation.EqvGen.symm _ _ (hx L_lo L_hi hL_lo hL_hi)

/-! ### 3. Interval gluing across general-position corner events -/

/-- **Gluing across a single-corner birth at an event time `t₁ ∈ [t₀, t₂]`.**
On `[t₀, t₁]` the link evolves with fixed vertex counts `N`; at `t₁` a new corner is inserted at
`c₀` in the open closing edge of component `m`; on `[t₁, t₂]` the `(N_m + 1)`-vertex link evolves
continuously in general position. Any link `L₀` at `t₀` and `L₂` at `t₂` are `DeltaEquiv`. -/
theorem deltaEquiv_across_cornerBirth_Icc {t₀ t₁ t₂ : ℝ} (ht₀₁ : t₀ ≤ t₁) (ht₁₂ : t₁ ≤ t₂)
    {k : ℕ} {N : Fin k → ℕ}
    (V_lo : Icc t₀ t₁ → (i : Fin k) → Fin (N i + 3) → E)
    (hV_lo : ∀ i, Continuous fun t => V_lo t i)
    (hreal_lo : ∀ t, ∃ L, Realizes (V_lo t) L)
    (m : Fin k) {c₀ : E}
    (hc₀ : c₀ ∈ openSegment ℝ
      (V_lo ⟨t₁, ht₀₁, le_rfl⟩ m (Fin.last (N m + 2))) (V_lo ⟨t₁, ht₀₁, le_rfl⟩ m 0))
    (V_hi : Icc t₁ t₂ → (i : Fin k) → Fin (bumpCount N m i + 3) → E)
    (hV_hi : ∀ i, Continuous fun t => V_hi t i)
    (hreal_hi : ∀ t, ∃ L, Realizes (V_hi t) L)
    (hglue : V_hi ⟨t₁, le_rfl, ht₁₂⟩ = insertCornerConfig (V_lo ⟨t₁, ht₀₁, le_rfl⟩) m c₀)
    {L₀ L₂ : PolygonalLink E}
    (hL₀ : Realizes (V_lo ⟨t₀, le_rfl, ht₀₁⟩) L₀)
    (hL₂ : Realizes (V_hi ⟨t₂, ht₁₂, le_rfl⟩) L₂) :
    DeltaEquiv L₀ L₂ := by
  haveI : PreconnectedSpace (Icc t₀ t₁) := Subtype.preconnectedSpace isPreconnected_Icc
  haveI : PreconnectedSpace (Icc t₁ t₂) := Subtype.preconnectedSpace isPreconnected_Icc
  obtain ⟨L₁_lo, hL₁_lo⟩ := hreal_lo ⟨t₁, ht₀₁, le_rfl⟩
  have hd₁ : DeltaEquiv L₀ L₁_lo :=
    deltaEquiv_of_preconnected V_lo hV_lo hreal_lo
      ⟨t₀, le_rfl, ht₀₁⟩ ⟨t₁, ht₀₁, le_rfl⟩ hL₀ hL₁_lo
  obtain ⟨L₁_hi, hmove, hL₁_hi⟩ := realizes_insertCornerConfig hL₁_lo m hc₀
  have hL₁_hi' : Realizes (V_hi ⟨t₁, le_rfl, ht₁₂⟩) L₁_hi := hglue.symm ▸ hL₁_hi
  have hd₂ : DeltaEquiv L₁_hi L₂ :=
    deltaEquiv_of_preconnected V_hi hV_hi hreal_hi
      ⟨t₁, le_rfl, ht₁₂⟩ ⟨t₂, ht₁₂, le_rfl⟩ hL₁_hi' hL₂
  exact Relation.EqvGen.trans _ _ _ hd₁
    (Relation.EqvGen.trans _ _ _ (Relation.EqvGen.rel _ _ hmove) hd₂)

/-- Elementary step of a general-position piecewise-linear link evolution (`#9114`):
either a continuous fixed-vertex-count interval evolution or a single elementary `Δ`-move
(birth/relabelling) or its reverse (corner death). -/
inductive GeneralPositionStep : PolygonalLink E → PolygonalLink E → Prop
  | fixedCountIcc {a b : ℝ} (hab : a ≤ b) {k : ℕ} {N : Fin k → ℕ}
      (V : Icc a b → (i : Fin k) → Fin (N i + 3) → E)
      (hV : ∀ i, Continuous fun t => V t i)
      (hreal : ∀ t, ∃ L, Realizes (V t) L)
      {L L' : PolygonalLink E}
      (hL : Realizes (V ⟨a, le_rfl, hab⟩) L)
      (hL' : Realizes (V ⟨b, hab, le_rfl⟩) L') : GeneralPositionStep L L'
  | singleMove {L L' : PolygonalLink E} (h : Move L L') : GeneralPositionStep L L'
  | singleMoveRev {L L' : PolygonalLink E} (h : Move L' L) : GeneralPositionStep L L'

/-- Every general-position step is a `DeltaEquiv`. -/
theorem GeneralPositionStep.deltaEquiv {L L' : PolygonalLink E}
    (h : GeneralPositionStep L L') : DeltaEquiv L L' := by
  cases h with
  | @fixedCountIcc a b hab _ _ V hV hreal _ _ hL hL' =>
    haveI : PreconnectedSpace (Icc a b) := Subtype.preconnectedSpace isPreconnected_Icc
    exact deltaEquiv_of_preconnected V hV hreal ⟨a, le_rfl, hab⟩ ⟨b, hab, le_rfl⟩ hL hL'
  | singleMove hm => exact Relation.EqvGen.rel _ _ hm
  | singleMoveRev hm => exact Relation.EqvGen.symm _ _ (Relation.EqvGen.rel _ _ hm)

/-- **Any finite chain of general-position interval evolutions and single-corner births/deaths
implies `DeltaEquiv`.** -/
theorem deltaEquiv_of_generalPositionChain {L L' : PolygonalLink E}
    (h : Relation.ReflTransGen GeneralPositionStep L L') : DeltaEquiv L L' := by
  induction h with
  | refl => exact Relation.EqvGen.refl _
  | tail _ hstep ih => exact Relation.EqvGen.trans _ _ _ ih hstep.deltaEquiv

end PolygonalLink

end Normed

end QOU.MathlibExt.PL
