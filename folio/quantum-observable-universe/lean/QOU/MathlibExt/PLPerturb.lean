/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLMoveVertexGlue

set_option autoImplicit false

/-!
# Small perturbations of a polygonal link are Δ-equivalences (issue #8902)

Let the vertices of every component of a polygonal link `L₀` depend continuously on a
parameter `x`, with `L₀` the configuration at `x₀`. Then for `x` near `x₀` every polygonal link
with the vertices at `x` is Δ-equivalent to `L₀`. The components are moved one at a time with
`PolygonalLink.eventually_reaches_polyOf`; the other components enter as a finite family of
segments.

## What is a THEOREM here

* `PolygonalLink.ext'` — links agree when their component counts and components do.
* `PolygonalLink.rest_eq_iUnion_segment` — the rest of a link of `polyOf` components is the
  union of the edges of the other components.
* `PolygonalLink.eventually_deltaEquiv` — **small vertex perturbations are Δ-equivalences.**
-/

namespace QOU.MathlibExt.PL

open Set Topology

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

namespace PolygonalLink

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
/-- **Extensionality** with a component-count equation. -/
theorem ext' {E : Type*} [AddCommGroup E] [Module ℝ E] {A B : PolygonalLink E} (hk : A.k = B.k)
    (h : ∀ i, B.comp (Fin.cast hk i) = A.comp i) : A = B := by
  cases A with
  | mk k comp s d =>
    cases B with
    | mk k' comp' s' d' =>
      simp only at hk
      subst hk
      simp only [PolygonalLink.mk.injEq, true_and, heq_eq_eq]
      funext i
      exact (h i).symm

variable {L₀ : PolygonalLink E} {N : Fin L₀.k → ℕ}

/-- The edges of the components other than `c`, indexed by component and edge. -/
abbrev OtherEdges (N : Fin L₀.k → ℕ) (c : Fin L₀.k) : Type :=
  Σ i : {i : Fin L₀.k // i ≠ c}, Fin (N i.1 + 3)

/-- **The rest as a union of segments.** -/
theorem rest_eq_iUnion_segment (L : PolygonalLink E) (hk : L₀.k = L.k)
    (W : (i : Fin L₀.k) → Fin (N i + 3) → E) (hc : ∀ i, L.comp (Fin.cast hk i) = polyOf (W i))
    (c : Fin L₀.k) :
    L.rest (Fin.cast hk c) = ⋃ j : OtherEdges N c,
      segment ℝ (W j.1.1 j.2) (W j.1.1 (finRotate _ j.2)) := by
  ext z
  simp only [rest, mem_iUnion, exists_prop]
  constructor
  · rintro ⟨i', hi', hz⟩
    obtain ⟨i, rfl⟩ : ∃ i, Fin.cast hk i = i' := ⟨Fin.cast hk.symm i', by simp⟩
    rw [hc, Polygon.carrier] at hz
    simp only [mem_iUnion] at hz
    obtain ⟨e, he⟩ := hz
    exact ⟨⟨⟨i, fun h => hi' (by rw [h])⟩, e⟩, he⟩
  · rintro ⟨⟨⟨i, hi⟩, e⟩, hz⟩
    refine ⟨Fin.cast hk i, fun h => hi (Fin.cast_injective _ h), ?_⟩
    rw [hc, Polygon.carrier]
    exact mem_iUnion.mpr ⟨e, hz⟩

variable {X : Type*} [TopologicalSpace X] {x₀ : X}

/-- Components `i < c` at `x`, the others at `x₀`. -/
def hybridL (V : X → (i : Fin L₀.k) → Fin (N i + 3) → E) (x₀ : X) (c : ℕ) (x : X) :
    (i : Fin L₀.k) → Fin (N i + 3) → E :=
  fun i => if i.val < c then V x i else V x₀ i

/-- **Small vertex perturbations of a polygonal link are Δ-equivalences.** Let `V x i` be the
vertex list of component `i`, continuous in `x`, with `L₀.comp i = polyOf (V x₀ i)`. Then for
all `x` near `x₀`, every polygonal link whose components are `polyOf (V x i)` is
Δ-equivalent to `L₀`. -/
theorem eventually_deltaEquiv (V : X → (i : Fin L₀.k) → Fin (N i + 3) → E)
    (hV : ∀ i, Continuous fun x => V x i) (h₀ : ∀ i, L₀.comp i = polyOf (V x₀ i)) :
    ∀ᶠ x in 𝓝 x₀, ∀ (L : PolygonalLink E) (hk : L₀.k = L.k),
      (∀ i, L.comp (Fin.cast hk i) = polyOf (V x i)) → DeltaEquiv L₀ L := by
  have hH : ∀ c i, Continuous fun x => hybridL V x₀ c x i := fun c i => by
    simp only [hybridL]
    split_ifs
    · exact hV i
    · exact continuous_const
  have hH0 : ∀ c, hybridL V x₀ c x₀ = V x₀ := fun c => by funext i; simp [hybridL]
  -- one application of `eventually_reaches_polyOf` per component
  have step : ∀ c : Fin L₀.k, ∀ᶠ x in 𝓝 x₀, ∀ (L : PolygonalLink E) (m : Fin L.k),
      L.comp m = polyOf (V x₀ c) →
      L.rest m = (⋃ j : OtherEdges N c, segment ℝ (hybridL V x₀ c.val x j.1.1 j.2)
        (hybridL V x₀ c.val x j.1.1 (finRotate _ j.2))) →
      L.Reaches m (polyOf (V x c)) := by
    intro c
    have hP : (polyOf (V x₀ c)).IsSimple := by rw [← h₀]; exact L₀.simple c
    have hR : ∀ j : OtherEdges N c, Disjoint (segment ℝ (hybridL V x₀ c.val x₀ j.1.1 j.2)
        (hybridL V x₀ c.val x₀ j.1.1 (finRotate _ j.2))) (polyOf (V x₀ c)).carrier := by
      intro j
      rw [hH0]
      have hd : Disjoint (L₀.comp j.1.1).carrier (L₀.comp c).carrier := L₀.disjoint j.1.2
      rw [h₀, h₀] at hd
      exact hd.mono_left ((polyOf (V x₀ j.1.1)).edge_subset_carrier j.2)
    exact eventually_reaches_polyOf (x₀ := x₀) (V := fun x => V x c) (hV c) hP
      (s := fun (j : OtherEdges N c) x => hybridL V x₀ c.val x j.1.1 j.2)
      (t := fun (j : OtherEdges N c) x => hybridL V x₀ c.val x j.1.1 (finRotate _ j.2))
      (fun j => (continuous_apply _).comp (hH _ _)) (fun j => (continuous_apply _).comp (hH _ _))
      hR
  filter_upwards [Filter.eventually_all.mpr step] with x hx
  -- induction over the number of components already moved
  have key : ∀ c, c ≤ L₀.k → ∃ (L' : PolygonalLink E), DeltaEquiv L₀ L' ∧
      ∃ hk : L₀.k = L'.k, ∀ i, L'.comp (Fin.cast hk i) = polyOf (hybridL V x₀ c x i) := by
    intro c
    induction c with
    | zero =>
      intro _
      exact ⟨L₀, Relation.EqvGen.refl _, rfl, fun i => by simp [hybridL, h₀]⟩
    | succ c ih =>
      intro hc
      obtain ⟨L', hd, hk, hcomp⟩ := ih (by omega)
      set c' : Fin L₀.k := ⟨c, by omega⟩
      have hm : L'.comp (Fin.cast hk c') = polyOf (V x₀ c') := by
        rw [hcomp]; simp [hybridL, c']
      have hr := rest_eq_iUnion_segment L' hk _ hcomp c'
      obtain ⟨L'', hd', hk', hcomp'⟩ := hx c' L' _ hm hr
      refine ⟨L'', Relation.EqvGen.trans _ _ _ hd hd', hk.trans hk', fun i => ?_⟩
      have := hcomp' (Fin.cast hk i)
      rw [Fin.cast_cast] at this
      rw [this]
      by_cases hi : i = c'
      · subst hi
        simp [hybridL, c']
      · rw [Function.update_of_ne (fun h => hi (Fin.cast_injective _ h)), hcomp]
        have : i.val ≠ c := fun h => hi (Fin.ext h)
        simp only [hybridL]
        congr 2
        exact propext ⟨fun h => by omega, fun h => by omega⟩
  intro L hk hc
  obtain ⟨L', hd, hk', hcomp⟩ := key L₀.k le_rfl
  have : L' = L := ext' (hk'.symm.trans hk) fun i => by
    obtain ⟨i0, rfl⟩ : ∃ i0, Fin.cast hk' i0 = i := ⟨Fin.cast hk'.symm i, by simp⟩
    rw [hcomp, Fin.cast_cast, hc]
    simp [hybridL]
  exact this ▸ hd

end PolygonalLink

end QOU.MathlibExt.PL
