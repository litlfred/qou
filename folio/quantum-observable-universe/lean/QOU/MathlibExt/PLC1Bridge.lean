/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLReachAll
import QOU.MathlibExt.PLC1Uniform
import QOU.MathlibExt.PLSampleBuild

set_option autoImplicit false

/-!
# C¹ ambient isotopy implies Δ-equivalence (issue #8902, C¹ bridge)

An ambient isotopy whose homeomorphisms are C¹ with C¹ inverses, jointly continuous in time,
carries a polygonal link to a Δ-equivalent one.

## What is a DEFINITION here

* `C1AmbientIsotopy L L'` — an `AmbientIsotopy` whose family `H` is a `C1Family`.

## What is a THEOREM here

* `C1AmbientIsotopy.deltaEquiv` — **a C¹ ambient isotopy gives Δ-equivalence.**

## Proof outline

Sample each component at a fine set of times containing its vertex times and the times that
the end reparametrization sends to vertex times. Inscribe the moving homeomorphism `H t` in
the sample: by `Polygon.isSimple_image` and `Polygon.disjoint_image_carrier`, with constants
from `C1Family.exists_inv_bound` and `C1Family.uniform_fderiv`, the inscribed link is a link for
every `t`. `deltaEquiv_of_preconnected` joins its two ends, and `reaches_sampleVerts`,
`reaches_reparam` join the ends to `L` and `L'`.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

namespace Polygon

theorem carrier_eq_image_Icc (Q : Polygon E) : Q.carrier = Q.param '' Icc 0 1 := by
  apply Subset.antisymm
  · rw [← Q.range_param]
    rintro _ ⟨t, rfl⟩
    exact ⟨Int.fract t, ⟨Int.fract_nonneg t, (Int.fract_lt_one t).le⟩, Q.param_fract t⟩
  · rw [← Q.range_param]
    exact image_subset_range _ _

theorem isCompact_carrier (Q : Polygon E) : IsCompact Q.carrier := by
  rw [carrier_eq_image_Icc]
  exact isCompact_Icc.image Q.continuous_param

lemma norm_sub_le_of_mem_edge (P : Polygon E) {i : Fin (P.n + 1)} {z : E} (hz : z ∈ P.edge i) :
    ‖z - P.v i‖ ≤ ‖P.v (P.next i) - P.v i‖ ∧
      ‖z - P.v (P.next i)‖ ≤ ‖P.v (P.next i) - P.v i‖ := by
  obtain ⟨s, ⟨hs0, hs1⟩, rfl⟩ := (P.mem_edge_iff).mp hz
  constructor
  · rw [add_sub_cancel_left, norm_smul, Real.norm_of_nonneg hs0]
    exact mul_le_of_le_one_left (norm_nonneg _) hs1
  · rw [show P.v i + s • (P.v (P.next i) - P.v i) - P.v (P.next i) =
        (s - 1) • (P.v (P.next i) - P.v i) by module, norm_smul, Real.norm_eq_abs,
      abs_of_nonpos (by linarith)]
    exact mul_le_of_le_one_left (norm_nonneg _) (by linarith)

lemma ofList_eq_of_ofFn {P : Polygon E} {l : List E} (h : 3 ≤ l.length)
    (hl : List.ofFn P.v = l) : ofList l h = P := by
  subst hl; exact ofList_ofFn P

lemma ofFn_orderEmbOfFin {α : Type*} (S : Finset ℝ) {m : ℕ} (hcard : S.card = m)
    (f : ℝ → α) :
    List.ofFn (fun k => f (S.orderEmbOfFin hcard k)) = (S.sort (· ≤ ·)).map f := by
  apply List.ext_getElem
  · simp [hcard]
  · intro n h1 h2
    rw [List.getElem_ofFn]
    simp only [Finset.orderEmbOfFin_apply, List.getElem_map]
    rfl

section Fine

variable (g : E → E) (P : Polygon E) {K : Set E} {M ε δ : ℝ}

lemma v_mem_carrier' (i : Fin (P.n + 1)) : P.v i ∈ P.carrier :=
  mem_iUnion.mpr ⟨i, left_mem_segment ℝ _ _⟩

lemma v_next_mem_carrier (i : Fin (P.n + 1)) : P.v (P.next i) ∈ P.carrier :=
  mem_iUnion.mpr ⟨i, right_mem_segment ℝ _ _⟩

/-- The derivative along a short edge stays close to its value at either endpoint. -/
lemma fderiv_near_ends (hPK : P.carrier ⊆ K)
    (hlen : ∀ i, ‖P.v (P.next i) - P.v i‖ ≤ δ)
    (hη : ∀ x ∈ K, ∀ y ∈ K, ‖x - y‖ ≤ δ → ‖fderiv ℝ g x - fderiv ℝ g y‖ ≤ ε) :
    ∀ i, ∀ z ∈ P.edge i, ‖fderiv ℝ g z - fderiv ℝ g (P.v i)‖ ≤ ε ∧
      ‖fderiv ℝ g z - fderiv ℝ g (P.v (P.next i))‖ ≤ ε := fun i z hz => by
  have hzK := hPK (P.edge_subset_carrier i hz)
  have h := P.norm_sub_le_of_mem_edge hz
  exact ⟨hη _ hzK _ (hPK (P.v_mem_carrier' i)) (h.1.trans (hlen i)),
    hη _ hzK _ (hPK (P.v_next_mem_carrier i)) (h.2.trans (hlen i))⟩

/-- **Simplicity of the inscribed polygon, from bounds on a set `K` holding it.** -/
theorem isSimple_image_of_fine {d κ : ℝ} (hM : 0 ≤ M) (hinj : Function.Injective P.v)
    (hd : ∀ z, DifferentiableAt ℝ g z) (hPK : P.carrier ⊆ K)
    (hlip : ∀ a ∈ K, ∀ b ∈ K, ‖a - b‖ ≤ M * ‖g a - g b‖)
    (hinv : ∀ x ∈ K, ∀ u, ‖u‖ ≤ M * ‖fderiv ℝ g x u‖)
    (hlen : ∀ i, ‖P.v (P.next i) - P.v i‖ ≤ δ)
    (hη : ∀ x ∈ K, ∀ y ∈ K, ‖x - y‖ ≤ δ → ‖fderiv ℝ g x - fderiv ℝ g y‖ ≤ ε)
    (hsep : ∀ i j, i ≠ j → j ≠ P.next i → i ≠ P.next j →
      ∀ a ∈ P.edge i, ∀ b ∈ P.edge j, d ≤ ‖a - b‖)
    (hangle : ∀ i α β, 0 ≤ α → 0 ≤ β →
      κ * (α * ‖P.v i - P.v (P.next i)‖ + β * ‖P.v (P.next (P.next i)) - P.v (P.next i)‖) ≤
        ‖α • (P.v i - P.v (P.next i)) - β • (P.v (P.next (P.next i)) - P.v (P.next i))‖)
    (h4 : 4 * M * ε * δ < d) (hκ : M * ε < κ) : (P.image g).IsSimple :=
  P.isSimple_image g hM hinj (fun i => fderiv ℝ g (P.v i)) (fun _ z _ => hd z)
    (P.fderiv_near_ends g hPK hlen hη)
    (fun i u => hinv _ (hPK (P.v_mem_carrier' i)) u) hlen
    (fun a ha b hb => hlip a (hPK ha) b (hPK hb)) hsep hangle h4 hκ

/-- **Disjointness of two inscribed polygons, from bounds on a set `K` holding both.** -/
theorem disjoint_image_of_fine (Q : Polygon E) {d : ℝ} (hM : 0 ≤ M)
    (hd : ∀ z, DifferentiableAt ℝ g z) (hPK : P.carrier ⊆ K) (hQK : Q.carrier ⊆ K)
    (hlip : ∀ a ∈ K, ∀ b ∈ K, ‖a - b‖ ≤ M * ‖g a - g b‖)
    (hlenP : ∀ i, ‖P.v (P.next i) - P.v i‖ ≤ δ) (hlenQ : ∀ i, ‖Q.v (Q.next i) - Q.v i‖ ≤ δ)
    (hη : ∀ x ∈ K, ∀ y ∈ K, ‖x - y‖ ≤ δ → ‖fderiv ℝ g x - fderiv ℝ g y‖ ≤ ε)
    (hsep : ∀ a ∈ P.carrier, ∀ b ∈ Q.carrier, d ≤ ‖a - b‖) (h4 : 4 * M * ε * δ < d) :
    Disjoint (P.image g).carrier (Q.image g).carrier :=
  P.disjoint_image_carrier g Q hM (fun i => fderiv ℝ g (P.v i)) (fun i => fderiv ℝ g (Q.v i))
    (fun _ z _ => hd z) (fun _ z _ => hd z)
    (fun i z hz => (P.fderiv_near_ends g hPK hlenP hη i z hz).1)
    (fun i z hz => (Q.fderiv_near_ends g hQK hlenQ hη i z hz).1) hlenP hlenQ
    (fun a ha b hb => hlip a (hPK ha) b (hQK hb)) hsep h4

end Fine

lemma eventually_div_lt (C : ℝ) {r : ℝ} (hr : 0 < r) : ∀ᶠ p : ℕ in atTop, C / p < r :=
  (tendsto_const_div_atTop_nhds_zero_nat C).eventually (gt_mem_nhds hr)

/-- **Fine samples exist.** For `p` large, a finite set `R ⊆ [0, 1)` of times containing the
vertex times extends to a sample with `γ = 1/p`, `Γ = 3/p`. -/
theorem eventually_exists_sample (Q : Polygon E) (R : Finset ℝ)
    (hR : ∀ x ∈ R, 0 ≤ x ∧ x < 1) (hV : Q.vertexTimes ⊆ R) :
    ∀ᶠ p : ℕ in atTop, ∃ (N : ℕ) (S : Finset ℝ) (hcard : S.card = N + 3), R ⊆ S ∧
      (∀ x ∈ S, 0 ≤ x ∧ x < 1) ∧
      Q.IsSample (fun k => S.orderEmbOfFin hcard k) (1 / p) (3 / p) := by
  have h1 : ∀ᶠ p : ℕ in atTop, ∀ x ∈ R, x ≤ 1 - 2 / p := by
    rw [Filter.eventually_all_finset]
    intro x hx
    filter_upwards [eventually_div_lt 2 (sub_pos.mpr (hR x hx).2)] with p hp
    linarith
  have h2 : ∀ᶠ p : ℕ in atTop, ∀ x ∈ R, ∀ y ∈ R, x < y → 2 / p ≤ y - x := by
    rw [Filter.eventually_all_finset]
    intro x _
    rw [Filter.eventually_all_finset]
    intro y _
    by_cases hxy : x < y
    · filter_upwards [eventually_div_lt 2 (sub_pos.mpr hxy)] with p hp _
      exact hp.le
    · exact Filter.Eventually.of_forall fun _ h => absurd h hxy
  filter_upwards [h1, h2, eventually_gt_atTop 0] with p hp1 hp2 hp0
  have hpR : (0 : ℝ) < p := by exact_mod_cast hp0
  obtain ⟨S, hRS, hS, hsep, hnext⟩ :=
    exists_fill R hp0 (fun x hx => ⟨(hR x hx).1, hp1 x hx⟩) hp2
  have h3 := Q.three_le_card (hV.trans hRS)
  have hp1' : (0 : ℝ) < 1 / p := by positivity
  refine ⟨S.card - 3, S, by omega, hRS,
    fun x hx => ⟨(hS x hx).1, (hS x hx).2.trans_lt (by linarith)⟩, ?_⟩
  refine isSample_of_finset S _ (by positivity) hS ?_ (hV.trans hRS) hsep ?_
  · exact hRS (hV (Finset.mem_image.mpr ⟨0, Finset.mem_univ _, by simp [vtime]⟩))
  · intro x hx
    obtain ⟨y, h1, h2, h3⟩ := hnext x hx
    exact ⟨y, h1, h2, h3⟩

namespace IsSample

variable {Q : Polygon E} {m : ℕ} {σ : Fin (m + 1) → ℝ} {γ Γ : ℝ} (hS : Q.IsSample σ γ Γ)
include hS

lemma carrier_subset (hm : 2 ≤ m) : (Q.sampled hm σ).carrier ⊆ Q.carrier := by
  intro a ha
  simp only [carrier, mem_iUnion] at ha
  obtain ⟨k, hk⟩ := ha
  obtain ⟨x, -, -, rfl⟩ := hS.mem_edge_time hm hk
  rw [← Q.range_param]; exact mem_range_self x

end IsSample

end Polygon

namespace OrientedReparam

variable {φ : ℝ → ℝ} (h : OrientedReparam φ)
include h

lemma add_int (t : ℝ) (z : ℤ) : φ (t + z) = φ t + z := by
  cases z with
  | ofNat n => simpa using h.add_nat t n
  | negSucc n =>
    have := h.sub_nat t (n + 1)
    rw [Int.cast_negSucc, ← sub_eq_add_neg, ← sub_eq_add_neg]
    push_cast at this ⊢
    exact this

lemma fract_apply_fract_symm (v : ℝ) (hv0 : 0 ≤ v) (hv1 : v < 1) :
    Int.fract (φ (Int.fract (h.toOrderIso.symm v))) = v := by
  set x := h.toOrderIso.symm v
  have hx : Int.fract x = x + ((-⌊x⌋ : ℤ) : ℝ) := by rw [Int.fract]; push_cast; ring
  rw [hx, h.add_int, h.apply_symm, Int.cast_neg, ← sub_eq_add_neg, Int.fract_sub_intCast,
    Int.fract_eq_self.mpr ⟨hv0, hv1⟩]

end OrientedReparam

omit [InnerProductSpace ℝ E] in
lemma exists_pos_sep_of_disjoint {A B : Set E} (hA : IsCompact A) (hB : IsCompact B)
    (h : Disjoint A B) : ∃ d > 0, ∀ a ∈ A, ∀ b ∈ B, d ≤ ‖a - b‖ := by
  by_cases hne : (A ×ˢ B).Nonempty
  · obtain ⟨p, hp, hmin⟩ := (hA.prod hB).exists_isMinOn hne
      (continuous_norm.comp (continuous_fst.sub continuous_snd)).continuousOn
    refine ⟨‖p.1 - p.2‖, norm_pos_iff.mpr (sub_ne_zero.mpr fun he => ?_), fun a ha b hb => ?_⟩
    · exact Set.disjoint_left.mp h hp.1 (he ▸ hp.2)
    · exact hmin (show (a, b) ∈ A ×ˢ B from ⟨ha, hb⟩)
  · refine ⟨1, one_pos, fun a ha b hb => absurd ⟨(a, b), ha, hb⟩ hne⟩

section Bridge

variable [FiniteDimensional ℝ E]

/-- **A C¹ ambient isotopy**: an ambient isotopy whose homeomorphisms, and their inverses, are
C¹ with derivatives jointly continuous in time and space. -/
structure C1AmbientIsotopy (L L' : PolygonalLink E) extends AmbientIsotopy L L' where
  /-- The family is C¹. -/
  c1 : C1Family H

namespace C1AmbientIsotopy

variable {L L' : PolygonalLink E}

/-- **A C¹ ambient isotopy gives Δ-equivalence.** -/
theorem deltaEquiv (I : C1AmbientIsotopy L L') : DeltaEquiv L L' := by
  classical
  choose φ hφ hfin using I.finish
  set Q : Fin L.k → Polygon E := L.comp with hQdef
  -- the times to sample: vertex times, and the times sent to vertex times at the end
  let R : Fin L.k → Finset ℝ := fun i => (Q i).vertexTimes ∪
    Finset.univ.image (fun v => Int.fract ((hφ i).toOrderIso.symm ((L'.comp (I.e i)).vtime v)))
  have hR : ∀ i, ∀ x ∈ R i, 0 ≤ x ∧ x < 1 := by
    intro i x hx
    rcases Finset.mem_union.mp hx with h | h
    · obtain ⟨v, -, rfl⟩ := Finset.mem_image.mp h
      exact (Q i).vtime_mem_Ico v
    · obtain ⟨v, -, rfl⟩ := Finset.mem_image.mp h
      exact ⟨Int.fract_nonneg _, Int.fract_lt_one _⟩
  have hRV : ∀ i, (Q i).vertexTimes ⊆ R i := fun i => Finset.subset_union_left
  -- the compact set holding the link
  set K : Set E := ⋃ i, (Q i).carrier with hKdef
  have hK : IsCompact K := isCompact_iUnion fun i => (Q i).isCompact_carrier
  have hQK : ∀ i, (Q i).carrier ⊆ K := fun i => subset_iUnion (fun i => (Q i).carrier) i
  -- separation constant of the parametrizations
  choose ci hci0 hci using fun i => (L.simple i).exists_param_sep
  obtain ⟨c, hc0, hcle⟩ := exists_pos_forall_le_of_finite ci hci0
  have hc : ∀ i, ∀ γ s t : ℝ, 0 ≤ γ → γ ≤ t - s → t - s ≤ 1 - γ →
      c * γ ≤ ‖(Q i).param s - (Q i).param t‖ := fun i γ s t h0 h1 h2 =>
    (mul_le_mul_of_nonneg_right (hcle i) h0).trans (hci i γ s t h0 h1 h2)
  -- edge-length bound
  choose B hB using fun i => Finite.exists_le fun j => ‖(Q i).v ((Q i).next j) - (Q i).v j‖
  obtain ⟨B0, hB0⟩ := Finite.exists_le B
  set Lm : ℝ := max B0 1 with hLmdef
  have hLm0 : 0 < Lm := lt_max_of_lt_right one_pos
  have hLm : ∀ i j, ‖(Q i).v ((Q i).next j) - (Q i).v j‖ ≤ Lm := fun i j =>
    (hB i j).trans ((hB0 i).trans (le_max_left _ _))
  -- bound on the number of vertices
  obtain ⟨N1, hN1⟩ := Finite.exists_le fun i => ((Q i).n : ℝ) + 1
  set N0 : ℝ := max N1 1 with hN0def
  have hN00 : 0 < N0 := lt_max_of_lt_right one_pos
  have hN0 : ∀ i, ((Q i).n : ℝ) + 1 ≤ N0 := fun i => (hN1 i).trans (le_max_left _ _)
  -- separation of distinct components
  have hDs : ∀ ij : Fin L.k × Fin L.k, ∃ d > 0, ij.1 ≠ ij.2 →
      ∀ a ∈ (Q ij.1).carrier, ∀ b ∈ (Q ij.2).carrier, d ≤ ‖a - b‖ := by
    rintro ⟨i, j⟩
    by_cases hij : i = j
    · exact ⟨1, one_pos, fun h => absurd hij h⟩
    · obtain ⟨d, hd, h⟩ := exists_pos_sep_of_disjoint (Q i).isCompact_carrier
        (Q j).isCompact_carrier (L.disjoint hij)
      exact ⟨d, hd, fun _ => h⟩
  choose dij hdij0 hdij using hDs
  obtain ⟨D0, hD00, hD0le⟩ := exists_pos_forall_le_of_finite dij hdij0
  have hD0 : ∀ i j, i ≠ j → ∀ a ∈ (Q i).carrier, ∀ b ∈ (Q j).carrier, D0 ≤ ‖a - b‖ :=
    fun i j hij a ha b hb => (hD0le (i, j)).trans (hdij (i, j) hij a ha b hb)
  -- inverse bounds
  obtain ⟨M, hM0, hMb⟩ := I.c1.exists_inv_bound hK
  -- the tolerance on derivatives
  have hκ0 : 0 < c / (N0 * Lm) := by positivity
  have hρ : 0 < min c D0 := lt_min hc0 hD00
  have ht : Tendsto (fun ε : ℝ => M * ε) (𝓝[>] 0) (𝓝 0) := by
    have := (continuous_const.mul continuous_id : Continuous fun ε : ℝ => M * ε).tendsto 0
    rw [mul_zero] at this
    exact this.mono_left nhdsWithin_le_nhds
  have he1 := ht.eventually (gt_mem_nhds hκ0)
  have he2 : ∀ᶠ ε in 𝓝[>] (0 : ℝ), 12 * N0 * Lm * (M * ε) < min c D0 := by
    have := ht.const_mul (12 * N0 * Lm)
    rw [mul_zero] at this
    exact this.eventually (gt_mem_nhds hρ)
  obtain ⟨ε, hε0, hε1, hε2⟩ :=
    ((eventually_mem_nhdsWithin : ∀ᶠ ε in 𝓝[>] (0 : ℝ), ε ∈ Ioi 0).and (he1.and he2)).exists
  have hε0 : (0 : ℝ) < ε := hε0
  obtain ⟨η, hη0, hη⟩ := I.c1.uniform_fderiv hK hε0
  -- the sampling step
  have hev := Filter.eventually_all.mpr fun i =>
    Polygon.eventually_exists_sample (Q i) (R i) (hR i) (hRV i)
  obtain ⟨p, hpS, hpΓ, hpη, hp1⟩ := (hev.and ((Polygon.eventually_div_lt 3 (by norm_num : (0:ℝ) < 1 / 4)).and
    ((Polygon.eventually_div_lt (N0 * Lm * 3) hη0).and (eventually_ge_atTop 1)))).exists
  choose N S hcard hRS hS01 hsamp using hpS
  have hpR : (1 : ℝ) ≤ p := by exact_mod_cast hp1
  have hp0 : (0 : ℝ) < p := by linarith
  have hΓ : (3 : ℝ) / p ≤ 1 / 4 := hpΓ.le
  set δ : ℝ := N0 * Lm * (3 / p) with hδdef
  have hδη : δ < η := by rw [hδdef, ← mul_div_assoc]; exact hpη
  let σ : (i : Fin L.k) → Fin (N i + 3) → ℝ := fun i k => (S i).orderEmbOfFin (hcard i) k
  have hm : ∀ i, 2 ≤ N i + 2 := fun _ => by omega
  let P : Fin L.k → Polygon E := fun i => (Q i).sampled (hm i) (σ i)
  have hPK : ∀ i, (P i).carrier ⊆ K := fun i => ((hsamp i).carrier_subset (hm i)).trans (hQK i)
  have hPQ : ∀ i, (P i).carrier ⊆ (Q i).carrier := fun i => (hsamp i).carrier_subset (hm i)
  have hlen : ∀ i k, ‖(P i).v ((P i).next k) - (P i).v k‖ ≤ δ := fun i k =>
    ((hsamp i).edge_len (hm i) (hLm i) k).trans (mul_le_mul
      (mul_le_mul_of_nonneg_right (hN0 i) hLm0.le) ((hsamp i).gap_le k)
      (sub_nonneg.mpr ((hsamp i).lt_snext k).le) (by positivity))
  have hηK : ∀ t, ∀ x ∈ K, ∀ y ∈ K, ‖x - y‖ ≤ δ →
      ‖fderiv ℝ (I.H t) x - fderiv ℝ (I.H t) y‖ ≤ ε :=
    fun t x hx y hy hxy => (hη t x hx y hy (hxy.trans_lt hδη)).le
  have h4eq : 4 * M * ε * δ = 12 * N0 * Lm * (M * ε) * (1 / p) := by rw [hδdef]; ring
  have h4c : 4 * M * ε * δ < c * (1 / p) := by
    rw [h4eq]
    exact mul_lt_mul_of_pos_right (hε2.trans_le (min_le_left _ _)) (by positivity)
  have h4D : 4 * M * ε * δ < D0 := by
    rw [h4eq]
    have h1p : 1 / (p : ℝ) ≤ 1 := by rw [div_le_one hp0]; exact hpR
    have hnn : 0 ≤ 12 * N0 * Lm * (M * ε) := by positivity
    exact (mul_le_of_le_one_right hnn h1p).trans_lt (hε2.trans_le (min_le_right _ _))
  have hsimple : ∀ t i, ((P i).image (I.H t)).IsSimple := fun t i =>
    (P i).isSimple_image_of_fine (I.H t) hM0 ((hsamp i).injective (L.simple i) (hm i))
      (I.c1.diff t) (hPK i) (hMb t).1 (hMb t).2 (hlen i) (hηK t)
      (fun k l hkl h1 h2 => (hsamp i).sep (hm i) (hc i) (by positivity) k l hkl h1 h2)
      ((hsamp i).angle (hm i) hc0 hLm0 (hc i) (hLm i) hΓ) h4c
      (hε1.trans_le (div_le_div_of_nonneg_left hc0.le (by positivity)
        (mul_le_mul_of_nonneg_right (hN0 i) hLm0.le)))
  have hdisj : ∀ t, Pairwise fun i j =>
      Disjoint ((P i).image (I.H t)).carrier ((P j).image (I.H t)).carrier :=
    fun t i j hij => (P i).disjoint_image_of_fine (I.H t) (P j) hM0 (I.c1.diff t) (hPK i)
      (hPK j) (hMb t).1 (hlen i) (hlen j) (hηK t)
      (fun a ha b hb => hD0 i j hij a (hPQ i ha) b (hPQ j hb)) h4D
  -- the inscribed links
  let Lt : unitInterval → PolygonalLink E := fun t =>
    ⟨L.k, fun i => (P i).image (I.H t), hsimple t, hdisj t⟩
  let V : unitInterval → (i : Fin L.k) → Fin (N i + 3) → E := fun t i k => I.H t ((P i).v k)
  have hV : ∀ i, Continuous fun t => V t i := fun i => continuous_pi fun k =>
    I.continuous.comp (continuous_id.prodMk continuous_const)
  have hreal : ∀ t, PolygonalLink.Realizes (V t) (Lt t) := fun t => ⟨rfl, fun i => rfl⟩
  have h01 : DeltaEquiv (Lt 0) (Lt 1) :=
    PolygonalLink.deltaEquiv_of_preconnected V hV (fun t => ⟨_, hreal t⟩) 0 1 (hreal 0) (hreal 1)
  -- `L` to the start
  have hP0 : ∀ i, (Lt 0).comp i = P i := fun i =>
    Polygon.ext' rfl fun k => by simp [Lt, Polygon.image_v, I.start]
  have hL0 : DeltaEquiv L (Lt 0) := by
    refine PolygonalLink.deltaEquiv_of_reaches_all L P (fun L'' m i him => ?_) (Lt 0) rfl
      (fun i => hP0 i)
    have h := PolygonalLink.reaches_sampleVerts L'' m (S i) (hS01 i)
      (by rw [him]; exact (hRV i).trans (hRS i))
    rwa [Polygon.ofList_eq_of_ofFn _ (by rw [him]; exact Polygon.ofFn_sampled (S i) (hcard i) (hm i))] at h
  -- the end to `L'`
  let L3 : PolygonalLink E := ⟨L'.k, fun j => (Lt 1).comp (I.e.symm j), fun j => (Lt 1).simple _,
    fun j j' h => (Lt 1).disjoint (I.e.symm.injective.ne h)⟩
  have h13 : DeltaEquiv (Lt 1) L3 :=
    Relation.EqvGen.rel _ _ (Move.relabel (Lt 1) L3 I.e (fun _ => 0) fun i => by
      show (Lt 1).comp (I.e.symm (I.e i)) = (Lt 1).comp i
      rw [Equiv.symm_apply_apply])
  have h3 : DeltaEquiv L' L3 := by
    refine PolygonalLink.deltaEquiv_of_reaches_all L' (fun j => (Lt 1).comp (I.e.symm j))
      (fun L'' m j hjm => ?_) L3 rfl (fun j => rfl)
    set i := I.e.symm j
    have hm' : L''.comp m = L'.comp (I.e i) := by rw [hjm, Equiv.apply_symm_apply]
    have key : ∀ Q' : Polygon E, Q' = L'.comp (I.e i) →
        ∀ v : Fin (Q'.n + 1), ∃ s ∈ S i, Int.fract (φ i s) = Q'.vtime v := by
      rintro _ rfl v
      exact ⟨_, hRS i (Finset.mem_union_right _ (Finset.mem_image_of_mem _ (Finset.mem_univ v))),
        (hφ i).fract_apply_fract_symm _ ((L'.comp (I.e i)).vtime_mem_Ico v).1
          ((L'.comp (I.e i)).vtime_mem_Ico v).2⟩
    have h := PolygonalLink.reaches_reparam L'' m (S i) (hS01 i) (hφ i) (key _ hm')
    rw [Polygon.ofList_eq_of_ofFn (P := (Lt 1).comp i) _ (by
      rw [hm', ← Polygon.ofFn_orderEmbOfFin (S i) (hcard i)]
      exact congrArg List.ofFn (funext fun k => hfin i (σ i k)))] at h
    exact h
  exact deltaEquiv_equivalence.trans hL0 (deltaEquiv_equivalence.trans h01
    (deltaEquiv_equivalence.trans h13 (deltaEquiv_equivalence.symm h3)))

end C1AmbientIsotopy

end Bridge

end QOU.MathlibExt.PL
