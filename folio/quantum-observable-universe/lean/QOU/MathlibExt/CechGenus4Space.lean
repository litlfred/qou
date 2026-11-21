import QOU.MathlibExt.CechGenus4Nerve
import QOU.MathlibExt.CechNerveValues
import Mathlib.Analysis.Convex.PathConnected

/-!
# The genus-4 surface as a space, and its open-star cover (route R3, step S2a)

`Space face` is the geometric realisation of a finite simplicial 2-complex with
vertices `Fin N` and faces `face : Fin m → Finset (Fin N)`: barycentric points of
`ℝ^N` (nonnegative, summing to `1`) whose support lies in one face. The open
star of a vertex `v` is the set where the `v`-coordinate is positive.

## Results, all sorry-free

* `inter_nonempty_iff`: the stars of a nonempty vertex set `S` meet iff `S` lies
  in a face. So the nerve of the star cover is the complex itself.
* `inter_starConvex`, `stars_isPreconnected`: every intersection of stars is
  star-convex about the barycentre of `S`, hence preconnected.
* `stars_cover`: the stars cover the space.
* For the genus-4 triangulation of `CechGenus4Nerve` (faces `{fA f, fB f, fC f}`):
  `connFamily_star` (the star cover is a `ConnFamily`) and
  `star3_nonempty_iff` (a triple of stars meets iff the three vertices lie in
  one face).

## What this does NOT do

It does not identify this space with Bring's curve (that is the classification
of closed surfaces, a citation), and it does not compute the colimit `Ȟ²` over
all covers (steps S3–S4). Bean `qou-skn4`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step S2
-/
open Topology

namespace QOU.CentralExtension.Cech.Genus4

section Realize


variable {N m : ℕ} (face : Fin m → Finset (Fin N))

/-- Geometric realisation inside the standard simplex of `ℝ^N`. -/
def Real4 : Set (Fin N → ℝ) :=
  {p | (∀ i, 0 ≤ p i) ∧ ∑ i, p i = 1 ∧ ∃ f, ∀ i, 0 < p i → i ∈ face f}

abbrev Space := {p : Fin N → ℝ // p ∈ Real4 face}

/-- Points where every vertex of `S` has positive barycentric coordinate. -/
def inter (S : Finset (Fin N)) : Set (Fin N → ℝ) := {p | p ∈ Real4 face ∧ ∀ v ∈ S, 0 < p v}

noncomputable def unif (S : Finset (Fin N)) : Fin N → ℝ :=
  fun v => if v ∈ S then ((S.card : ℝ))⁻¹ else 0

theorem unif_sum {S : Finset (Fin N)} (hS : S.Nonempty) : ∑ v, unif S v = 1 := by
  unfold unif
  rw [Finset.sum_ite_mem, Finset.univ_inter, Finset.sum_const, nsmul_eq_mul]
  have : (S.card : ℝ) ≠ 0 := by exact_mod_cast hS.card_pos.ne'
  field_simp

theorem unif_pos {S : Finset (Fin N)} {v : Fin N} (hv : v ∈ S) : 0 < unif S v := by
  have : 0 < (S.card : ℝ) := by exact_mod_cast Finset.card_pos.mpr ⟨v, hv⟩
  simp [unif, hv, this]

theorem unif_nonneg (S : Finset (Fin N)) (v : Fin N) : 0 ≤ unif S v := by
  unfold unif; split_ifs <;> positivity

theorem unif_pos_mem {S : Finset (Fin N)} {v : Fin N} (h : 0 < unif S v) : v ∈ S := by
  by_contra hv; simp [unif, hv] at h

/-- Nerve: the stars of `S` meet iff `S` lies in a face. -/
theorem inter_nonempty_iff {S : Finset (Fin N)} (hS : S.Nonempty) :
    (inter face S).Nonempty ↔ ∃ f, S ⊆ face f := by
  constructor
  · rintro ⟨p, ⟨-, -, f, hf⟩, hp⟩
    exact ⟨f, fun v hv => hf v (hp v hv)⟩
  · rintro ⟨f, hf⟩
    refine ⟨unif S, ⟨unif_nonneg S, unif_sum hS, f, fun i hi => hf (unif_pos_mem hi)⟩,
      fun v hv => unif_pos hv⟩

theorem inter_starConvex {S : Finset (Fin N)} (hS : S.Nonempty) :
    StarConvex ℝ (unif S) (inter face S) := by
  intro p ⟨⟨hp0, hp1, g, hg⟩, hpS⟩ a b ha hb hab
  have hpos : ∀ v ∈ S, 0 < a * unif S v + b * p v := by
    intro v hv
    rcases ha.eq_or_lt with h | h
    · subst h; have : b = 1 := by linarith
      subst this; simpa using hpS v hv
    · exact add_pos_of_pos_of_nonneg (mul_pos h (unif_pos hv)) (mul_nonneg hb (hp0 v))
  refine ⟨⟨fun i => ?_, ?_, g, fun i hi => ?_⟩, fun v hv => ?_⟩
  · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    exact add_nonneg (mul_nonneg ha (unif_nonneg S i)) (mul_nonneg hb (hp0 i))
  · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum, unif_sum hS, hp1]; linarith
  · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul] at hi
    by_cases hu : 0 < unif S i
    · exact hg i (hpS i (unif_pos_mem hu))
    · by_cases hpi : 0 < p i
      · exact hg i hpi
      · exfalso
        have h1 : unif S i = 0 := le_antisymm (not_lt.mp hu) (unif_nonneg S i)
        have h2 : p i = 0 := le_antisymm (not_lt.mp hpi) (hp0 i)
        rw [h1, h2] at hi; simp at hi
  · simpa only [Pi.add_apply, Pi.smul_apply, smul_eq_mul] using hpos v hv

theorem inter_isPreconnected (S : Finset (Fin N)) (hS : S.Nonempty) :
    IsPreconnected (inter face S) := by
  rcases (inter face S).eq_empty_or_nonempty with h | h
  · rw [h]; exact isPreconnected_empty
  · have hu : unif S ∈ inter face S := by
      obtain ⟨f, hf⟩ := (inter_nonempty_iff face hS).mp h
      exact ⟨⟨unif_nonneg S, unif_sum hS, f, fun i hi => hf (unif_pos_mem hi)⟩,
        fun v hv => unif_pos hv⟩
    exact ((inter_starConvex face hS).isPathConnected hu).isConnected.isPreconnected

/-- The open star of a vertex. -/
def star (v : Fin N) : TopologicalSpace.Opens (Space face) :=
  ⟨{x | 0 < x.1 v}, isOpen_lt continuous_const ((continuous_apply v).comp continuous_subtype_val)⟩

theorem star_set_eq (S : Finset (Fin N)) :
    Subtype.val '' {x : Space face | ∀ v ∈ S, 0 < x.1 v} = inter face S := by
  ext p; constructor
  · rintro ⟨x, hx, rfl⟩; exact ⟨x.2, hx⟩
  · rintro ⟨hp, hS⟩; exact ⟨⟨p, hp⟩, hS, rfl⟩

theorem stars_isPreconnected (S : Finset (Fin N)) (hS : S.Nonempty) :
    IsPreconnected {x : Space face | ∀ v ∈ S, 0 < x.1 v} := by
  rw [← Topology.IsInducing.subtypeVal.isPreconnected_image, star_set_eq]
  exact inter_isPreconnected face S hS

theorem stars_cover (x : Space face) : ∃ v, x ∈ star face v := by
  by_contra h; push_neg at h
  have : ∑ i, x.1 i ≤ 0 := Finset.sum_nonpos fun i _ => not_lt.mp (h i)
  rw [x.2.2.1] at this; linarith



end Realize

/-! ### The genus-4 instance -/

/-- The three vertices of face `f`. -/
def face4 (f : Fin 50) : Finset (Fin 19) := {fA f, fB f, fC f}

/-- The genus-4 surface: realisation of the 50-face triangulation. -/
abbrev Surf := Space face4

/-- The open-star cover, one open set per vertex. -/
def U4 : Fin 19 → TopologicalSpace.Opens Surf := star face4

theorem U4_inter3 (i j k : Fin 19) :
    ((U4 i ⊓ U4 j ⊓ U4 k : TopologicalSpace.Opens Surf) : Set Surf) =
      {x : Surf | ∀ v ∈ ({i, j, k} : Finset (Fin 19)), 0 < x.1 v} := by
  ext x; simp [U4, star, and_assoc]

theorem U4_inter2 (i j : Fin 19) :
    ((U4 i ⊓ U4 j : TopologicalSpace.Opens Surf) : Set Surf) =
      {x : Surf | ∀ v ∈ ({i, j} : Finset (Fin 19)), 0 < x.1 v} := by
  ext x; simp [U4, star]

theorem connFamily_star : ConnFamily U4 where
  pre3 i j k := by
    rw [U4_inter3]; exact stars_isPreconnected face4 _ (by simp)
  pre2 i j := by
    rw [U4_inter2]; exact stars_isPreconnected face4 _ (by simp)

theorem U4_covers (x : Surf) : ∃ v, x ∈ U4 v := stars_cover face4 x

/-- **Nerve.** Three stars meet iff the three vertices lie in one face. -/
theorem star3_nonempty_iff (i j k : Fin 19) :
    ((U4 i ⊓ U4 j ⊓ U4 k : TopologicalSpace.Opens Surf) : Set Surf).Nonempty ↔
      ∃ f, ({i, j, k} : Finset (Fin 19)) ⊆ face4 f := by
  rw [U4_inter3, ← inter_nonempty_iff face4 (by simp : ({i, j, k} : Finset (Fin 19)).Nonempty),
    ← star_set_eq, Set.image_nonempty]

end QOU.CentralExtension.Cech.Genus4
