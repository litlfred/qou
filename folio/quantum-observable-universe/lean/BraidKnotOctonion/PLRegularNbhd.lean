/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLBarycentric

set_option autoImplicit false

/-!
# Regular neighbourhoods: existence and the neighbourhood property (issue #8902, Moise build A)

## What is a THEOREM here

* `IsDerived.faces_finite` — a derived subdivision of a finite complex is finite.
* `subset_simplicialNbhd` — `L.space ⊆ simplicialNbhd K L` for a subcomplex `L`.
* `simplicialNbhd_subset` — `simplicialNbhd K L ⊆ K.space`.
* `simplicialNbhd_mem_nhdsWithin` — for finite `K`, the simplicial neighbourhood of `L` is a
  neighbourhood in `K.space` of every point of `L.space`.
* `isSubcomplex_baryComplex` — barycentric subdivision preserves subcomplexes.
* `exists_isRegularNbhd` — **regular neighbourhoods exist**: if `K` triangulates `M` and a
  subcomplex triangulates `P`, then `P` has a regular neighbourhood in `M`.
* `IsRegularNbhd.subset`, `IsRegularNbhd.superset`, `IsRegularNbhd.mem_nhdsWithin` — `P ⊆ N ⊆ M`
  and `N` is a neighbourhood of every point of `P` in `M`.

## What is NOT proved here

Uniqueness of regular neighbourhoods up to PL homeomorphism, and that a regular neighbourhood of
a point in a PL `n`-manifold is a PL `n`-ball (Rourke–Sanderson Ch. 3).
-/

namespace QOU.MathlibExt.PL

open Set Geometry Finset Topology

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

theorem IsDerived.faces_finite {K' K : SimplicialComplex ℝ E} (h : IsDerived K' K)
    (hK : K.faces.Finite) : K'.faces.Finite := by
  classical
  obtain ⟨a, -, hfaces⟩ := h
  refine ((hK.toFinset.powerset : Finset (Finset (Finset E))).finite_toSet.image
    (fun C => C.image a)).subset ?_
  intro s hs
  rw [hfaces] at hs
  obtain ⟨C, -, hKC, -, hsC⟩ := hs
  refine ⟨C, mem_coe.mpr (mem_powerset.mpr fun σ hσ => hK.mem_toFinset.mpr (hKC σ hσ)), ?_⟩
  exact coe_injective (by rw [coe_image, hsC])

theorem subset_simplicialNbhd {L K : SimplicialComplex ℝ E} (hL : IsSubcomplex L K) :
    L.space ⊆ simplicialNbhd K L := by
  intro x hx
  obtain ⟨s, hs, hxs⟩ := SimplicialComplex.mem_space_iff.mp hx
  exact Set.mem_biUnion (x := s) ⟨hL hs, x, hxs, hx⟩ hxs

theorem simplicialNbhd_subset (K L : SimplicialComplex ℝ E) : simplicialNbhd K L ⊆ K.space :=
  iUnion₂_subset fun s hs => fun _ hx => SimplicialComplex.mem_space_iff.mpr ⟨s, hs.1, hx⟩

/-- **The simplicial neighbourhood is a neighbourhood.** -/
theorem simplicialNbhd_mem_nhdsWithin {K L : SimplicialComplex ℝ E} (hK : K.faces.Finite)
    {x : E} (hx : x ∈ L.space) : simplicialNbhd K L ∈ 𝓝[K.space] x := by
  set Z := ⋃ s ∈ {s | s ∈ K.faces ∧ convexHull ℝ (s : Set E) ∩ L.space = ∅},
    convexHull ℝ (s : Set E) with hZ
  have hZc : IsClosed Z := (hK.subset fun s hs => hs.1).isClosed_biUnion fun s _ =>
    s.finite_toSet.isCompact_convexHull.isClosed
  have hxZ : x ∉ Z := by
    rw [hZ, mem_iUnion₂]
    rintro ⟨s, hs, hxs⟩
    exact (Set.eq_empty_iff_forall_notMem.mp hs.2) x ⟨hxs, hx⟩
  refine Filter.mem_of_superset (inter_mem_nhdsWithin K.space (hZc.isOpen_compl.mem_nhds hxZ))
    ?_
  rintro y ⟨hy, hyZ⟩
  obtain ⟨s, hs, hys⟩ := SimplicialComplex.mem_space_iff.mp hy
  rcases (convexHull ℝ (s : Set E) ∩ L.space).eq_empty_or_nonempty with he | hne
  · refine absurd ?_ hyZ
    rw [hZ]
    exact Set.mem_iUnion₂.mpr ⟨s, ⟨hs, he⟩, hys⟩
  · exact Set.mem_biUnion (x := s) ⟨hs, hne⟩ hys

theorem isSubcomplex_baryComplex [DecidableEq E] {L K : SimplicialComplex ℝ E}
    (h : IsSubcomplex L K) : IsSubcomplex (baryComplex L) (baryComplex K) := by
  rintro s ⟨C, ⟨hne, hL, hch⟩, rfl⟩
  exact ⟨C, ⟨hne, fun σ hσ => h (hL σ hσ), hch⟩, rfl⟩

/-- **Regular neighbourhoods exist.** -/
theorem exists_isRegularNbhd {K L : SimplicialComplex ℝ E} {M P : Set E} (hK : Triangulates K M)
    (hL : IsSubcomplex L K) (hLP : L.space = P) : ∃ N, IsRegularNbhd N P M := by
  classical
  refine ⟨_, K, baryComplex K, baryComplex (baryComplex K), baryComplex (baryComplex L), hK,
    ⟨L, hL, hLP⟩, isDerived_baryComplex K, subdivides_baryComplex K,
    isDerived_baryComplex _, subdivides_baryComplex _,
    isSubcomplex_baryComplex (isSubcomplex_baryComplex hL), ?_, rfl⟩
  rw [baryComplex_space, baryComplex_space, hLP]

theorem IsRegularNbhd.subset {N P M : Set E} (h : IsRegularNbhd N P M) : N ⊆ M := by
  obtain ⟨K, K', K'', L'', hK, -, -, hK', -, hK'', -, -, rfl⟩ := h
  rw [← hK.2, ← hK'.1, ← hK''.1]
  exact simplicialNbhd_subset _ _

theorem IsRegularNbhd.superset {N P M : Set E} (h : IsRegularNbhd N P M) : P ⊆ N := by
  obtain ⟨K, K', K'', L'', -, -, -, -, -, -, hL'', hP, rfl⟩ := h
  rw [← hP]
  exact subset_simplicialNbhd hL''

/-- **A regular neighbourhood of `P` is a neighbourhood of `P` in `M`.** -/
theorem IsRegularNbhd.mem_nhdsWithin {N P M : Set E} (h : IsRegularNbhd N P M) {x : E}
    (hx : x ∈ P) : N ∈ 𝓝[M] x := by
  obtain ⟨K, K', K'', L'', hK, -, hd', hK', hd'', hK'', -, hP, rfl⟩ := h
  rw [← hK.2, ← hK'.1, ← hK''.1]
  exact simplicialNbhd_mem_nhdsWithin ((hd''.faces_finite (hd'.faces_finite hK.1))) (hP ▸ hx)

end QOU.MathlibExt.PL
