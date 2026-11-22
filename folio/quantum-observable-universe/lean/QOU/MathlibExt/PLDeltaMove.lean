/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLDeltaIsotopy
import Mathlib.Topology.Algebra.Order.Floor

set_option autoImplicit false

/-!
# A Δ-move is an ambient isotopy (issue #8902, stage 2, part 6)

This file turns the body of `PLDeltaIsotopy.lean` into an isotopy, and proves the main result
of stage 2's first half, over any real normed space `E`:

* `DeltaEquiv.ambientIsotopic` — **Δ-equivalent polygonal links are ambient isotopic.**
  The isotopy for one Δ-move is a push of the midpoint of the closing edge to the new vertex,
  supported in a convex body around the triangle (`ambientIsotopic_of_delta`).

## What is a THEOREM here

* `OrientedReparam.ofUnit` — a strictly increasing continuous `ψ` with `ψ 0 = 0`, `ψ 1 = 1`
  gives an orientation-preserving reparametrization `t ↦ ⌊t⌋ + ψ (fract t)`.
* `deltaIso` — the isotopy `s ↦ m + push (s • (c - m)) (· - m)` built from the body, with
  `deltaIso_of_not_mem` (it fixes everything outside the interior of the body) and
  `deltaIso_one_left` / `deltaIso_one_right` (at time `1` it maps `[a, m]` onto `[a, c]` and
  `[m, b]` onto `[c, b]`, affinely).
* `ambientIsotopic_of_delta`, `Move.ambientIsotopic`, `DeltaEquiv.ambientIsotopic`.

## What is NOT proved here

* The converse (ambient isotopy implies Δ-equivalence) and the PL-isotopy comparison: later
  parts of stage 2.
-/

namespace QOU.MathlibExt.PL

open Set Metric

namespace OrientedReparam

/-- **Reparametrizations from a map of the unit interval.** -/
theorem ofUnit {ψ : ℝ → ℝ} (hc : Continuous ψ) (hm : StrictMono ψ) (h0 : ψ 0 = 0)
    (h1 : ψ 1 = 1) : OrientedReparam (fun t => t + (ψ (Int.fract t) - Int.fract t)) := by
  have e : ∀ x : ℝ, x + (ψ (Int.fract x) - Int.fract x) = ⌊x⌋ + ψ (Int.fract x) := by
    intro x; have := Int.self_sub_fract x; linarith
  refine ⟨?_, ?_, ?_⟩
  · have : Continuous ((fun s => ψ s - s) ∘ Int.fract) :=
      ContinuousOn.comp_fract'' (hc.sub continuous_id).continuousOn (by simp [h0, h1])
    exact continuous_id.add this
  · intro t t' htt'
    simp only [e]
    rcases (Int.floor_mono htt'.le).lt_or_eq with hlt | heq
    · have hlt' : (⌊t⌋ : ℝ) + 1 ≤ ⌊t'⌋ := by exact_mod_cast hlt
      have h1' : ψ (Int.fract t) < 1 := h1 ▸ hm (Int.fract_lt_one t)
      have h0' : 0 ≤ ψ (Int.fract t') := h0 ▸ hm.monotone (Int.fract_nonneg t')
      linarith
    · have : Int.fract t < Int.fract t' := by
        rw [Int.fract, Int.fract, heq]; linarith
      rw [heq]; linarith [hm this]
  · intro t
    simp only [Int.fract_add_one]
    ring

end OrientedReparam

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] {a b c : E} {ρ : ℝ}

/-- The open convex set of the push: the interior of the body, centred at the midpoint. -/
def deltaSet (a b c : E) (ρ : ℝ) : Set E :=
  (fun x => midpoint ℝ a b + x) ⁻¹' interior (deltaBody a b c ρ)

lemma deltaSet_comm : deltaSet a b c ρ = deltaSet b a c ρ := by
  unfold deltaSet; rw [deltaBody_comm, midpoint_comm]

lemma isOpen_deltaSet : IsOpen (deltaSet a b c ρ) :=
  isOpen_interior.preimage (continuous_const.add continuous_id)

lemma convex_deltaSet : Convex ℝ (deltaSet a b c ρ) :=
  convex_deltaBody.interior.translate_preimage_right _

lemma zero_mem_deltaSet (hρ : 0 < ρ) : (0 : E) ∈ deltaSet a b c ρ := by
  show midpoint ℝ a b + 0 ∈ interior (deltaBody a b c ρ)
  rw [add_zero]; exact midpoint_mem_interior_deltaBody hρ

lemma deltaSet_mem_nhds (hρ : 0 < ρ) : deltaSet a b c ρ ∈ nhds (0 : E) :=
  isOpen_deltaSet.mem_nhds (zero_mem_deltaSet hρ)

lemma gauge_apex_lt (hρ : 0 < ρ) : gauge (deltaSet a b c ρ) (c - midpoint ℝ a b) < 1 :=
  gauge_lt_one_of_mem_of_isOpen isOpen_deltaSet (by
    show midpoint ℝ a b + (c - midpoint ℝ a b) ∈ interior (deltaBody a b c ρ)
    rw [add_sub_cancel]; exact mem_interior_deltaBody hρ)

lemma one_le_gauge_of_not_mem (hρ : 0 < ρ) {x : E} (hx : x ∉ interior (deltaBody a b c ρ)) :
    1 ≤ gauge (deltaSet a b c ρ) (x - midpoint ℝ a b) := by
  apply one_le_gauge_of_notMem (convex_deltaSet.starConvex (zero_mem_deltaSet hρ))
    (absorbent_nhds_zero (deltaSet_mem_nhds hρ)).absorbs
  show ¬ midpoint ℝ a b + (x - midpoint ℝ a b) ∈ interior (deltaBody a b c ρ)
  rwa [add_sub_cancel]

lemma gauge_left_le_one (hρ : 0 < ρ) : gauge (deltaSet a b c ρ) (a - midpoint ℝ a b) ≤ 1 := by
  by_contra hg
  push_neg at hg
  set g := gauge (deltaSet a b c ρ) (a - midpoint ℝ a b)
  have hg0 : 0 < g := by linarith
  have hr0 : 0 < 1 / g := by positivity
  have hr1 : 1 / g < 1 := by rw [div_lt_one hg0]; exact hg
  have hmem : (1 / g) • (a - midpoint ℝ a b) ∈ deltaSet a b c ρ := by
    show midpoint ℝ a b + (1 / g) • (a - midpoint ℝ a b) ∈ interior (deltaBody a b c ρ)
    have := convex_deltaBody.combo_interior_self_mem_interior
      (midpoint_mem_interior_deltaBody hρ) (left_mem_deltaBody (a := a) (b := b) (c := c) (ρ := ρ))
      (sub_pos.mpr hr1) hr0.le (by ring)
    convert this using 1
    module
  have := gauge_lt_one_of_mem_of_isOpen isOpen_deltaSet hmem
  rw [gauge_smul_of_nonneg hr0.le, smul_eq_mul, one_div, inv_mul_cancel₀ hg0.ne'] at this
  exact lt_irrefl _ this

/-- **The corner `a` is on the boundary of the push set.** -/
lemma gauge_left_eq_one (hρ : 0 < ρ) (ha : a ∉ interior (deltaBody a b c ρ)) :
    gauge (deltaSet a b c ρ) (a - midpoint ℝ a b) = 1 :=
  le_antisymm (gauge_left_le_one hρ) (one_le_gauge_of_not_mem hρ ha)

/-- **The corner `b` is on the boundary of the push set.** -/
lemma gauge_right_eq_one (hρ : 0 < ρ) (hb : b ∉ interior (deltaBody a b c ρ)) :
    gauge (deltaSet a b c ρ) (b - midpoint ℝ a b) = 1 := by
  rw [deltaSet_comm, midpoint_comm]
  rw [deltaBody_comm] at hb
  exact gauge_left_eq_one hρ hb

/-- **The Δ-isotopy**: push the midpoint `m` of `[a, b]` to `c` inside the body. -/
noncomputable def deltaIso (a b c : E) {ρ : ℝ} (hρ : 0 < ρ) (s : unitInterval) : E ≃ₜ E :=
  ((Homeomorph.addLeft (-midpoint ℝ a b)).trans
    (pushFamily (convex_deltaSet (a := a) (b := b) (c := c) (ρ := ρ)) (deltaSet_mem_nhds hρ)
      (gauge_apex_lt hρ) s)).trans
    (Homeomorph.addLeft (midpoint ℝ a b))

lemma deltaIso_apply (hρ : 0 < ρ) (s : unitInterval) (x : E) :
    deltaIso a b c hρ s x = midpoint ℝ a b +
      push (deltaSet a b c ρ) ((s : ℝ) • (c - midpoint ℝ a b)) (x - midpoint ℝ a b) := by
  simp [deltaIso, pushFamily_apply, neg_add_eq_sub]

lemma deltaIso_symm_apply (hρ : 0 < ρ) (s : unitInterval) (y : E) :
    (deltaIso a b c hρ s).symm y = midpoint ℝ a b +
      (pushFamily (convex_deltaSet (a := a) (b := b) (c := c) (ρ := ρ)) (deltaSet_mem_nhds hρ)
        (gauge_apex_lt hρ) s).symm
        (y - midpoint ℝ a b) := by
  simp [deltaIso, Homeomorph.addLeft_symm, neg_add_eq_sub]

lemma deltaIso_zero (hρ : 0 < ρ) (x : E) : deltaIso a b c hρ 0 x = x := by
  simp [deltaIso_apply, push, pushCoef]

lemma continuous_deltaIso (hρ : 0 < ρ) :
    Continuous fun p : unitInterval × E => deltaIso a b c hρ p.1 p.2 := by
  simp only [deltaIso_apply]
  exact continuous_const.add ((continuous_pushFamily (convex_deltaSet (a := a) (b := b)
    (c := c) (ρ := ρ)) (deltaSet_mem_nhds hρ) (gauge_apex_lt hρ)).comp (continuous_fst.prodMk (continuous_snd.sub continuous_const)))

lemma continuous_deltaIso_symm (hρ : 0 < ρ) :
    Continuous fun p : unitInterval × E => (deltaIso a b c hρ p.1).symm p.2 := by
  simp only [deltaIso_symm_apply]
  exact continuous_const.add ((continuous_pushFamily_symm (convex_deltaSet (a := a) (b := b)
    (c := c) (ρ := ρ)) (deltaSet_mem_nhds hρ) (gauge_apex_lt hρ)).comp
    (continuous_fst.prodMk (continuous_snd.sub continuous_const)))

/-- **The Δ-isotopy fixes everything outside the interior of the body.** -/
lemma deltaIso_of_not_mem (hρ : 0 < ρ) (s : unitInterval) {x : E}
    (hx : x ∉ interior (deltaBody a b c ρ)) : deltaIso a b c hρ s x = x := by
  rw [deltaIso_apply, push_of_one_le_gauge _ (one_le_gauge_of_not_mem hρ hx)]
  abel

/-- **At time `1`, the half `[a, m]` goes onto `[a, c]`.** -/
lemma deltaIso_one_left (hρ : 0 < ρ) (ha : a ∉ interior (deltaBody a b c ρ)) {u : ℝ}
    (hu0 : 0 ≤ u) (hu1 : u ≤ 1 / 2) :
    deltaIso a b c hρ 1 ((1 - u) • a + u • b) = (1 - 2 * u) • a + (2 * u) • c := by
  have hx : (1 - u) • a + u • b - midpoint ℝ a b = (1 - 2 * u) • (a - midpoint ℝ a b) := by
    simp only [midpoint_eq_smul_add, invOf_eq_inv]; module
  rw [deltaIso_apply, hx, push_smul_of_gauge_eq_one _ (gauge_left_eq_one hρ ha) (by linarith)
    (by linarith), Set.Icc.coe_one, one_smul]
  module

/-- **At time `1`, the half `[m, b]` goes onto `[c, b]`.** -/
lemma deltaIso_one_right (hρ : 0 < ρ) (hb : b ∉ interior (deltaBody a b c ρ)) {u : ℝ}
    (hu0 : 1 / 2 ≤ u) (hu1 : u ≤ 1) :
    deltaIso a b c hρ 1 ((1 - u) • a + u • b) = (2 - 2 * u) • c + (2 * u - 1) • b := by
  have hx : (1 - u) • a + u • b - midpoint ℝ a b = (2 * u - 1) • (b - midpoint ℝ a b) := by
    simp only [midpoint_eq_smul_add, invOf_eq_inv]; module
  rw [deltaIso_apply, hx, push_smul_of_gauge_eq_one _ (gauge_right_eq_one hρ hb) (by linarith)
    (by linarith), Set.Icc.coe_one, one_smul]
  module

/-! ### Polygon facts used by the Δ-move -/

lemma isCompact_segment' (x y : E) : IsCompact (segment ℝ x y) := by
  rw [segment_eq_image]
  exact isCompact_Icc.image (((continuous_const.sub continuous_id).smul continuous_const).add
    (continuous_id.smul continuous_const))

/-- If `a ≠ b`, `a ≠ c` and `[a, c] ∩ [c, b] ⊆ {c}`, then `a ∉ [m, c]`, `m` the midpoint of
`[a, b]`. -/
lemma apex_seg_ne_zero {a b c : E} (hab : a ≠ b) (hac : a ≠ c)
    (hseg : segment ℝ a c ∩ segment ℝ c b ⊆ {c}) :
    ∀ θ ∈ Icc (0 : ℝ) 1, (1 - θ) • (midpoint ℝ a b - a) + θ • (c - a) ≠ 0 := by
  rintro θ ⟨hθ0, hθ1⟩ h0
  have key : (2 * θ) • (c - a) + (1 - θ) • (b - a) = 0 := by
    simp only [midpoint_eq_smul_add, invOf_eq_inv] at h0
    linear_combination (norm := module) (2 : ℝ) • h0
  rcases hθ0.lt_or_eq with hθ | hθ
  · have hp : (1 + θ) ≠ 0 := by linarith
    have h1 : (1 + θ) • a = (2 * θ) • c + (1 - θ) • b := by
      linear_combination (norm := module) -key
    have ha : a = (2 * θ / (1 + θ)) • c + ((1 - θ) / (1 + θ)) • b := by
      calc a = (1 + θ)⁻¹ • ((1 + θ) • a) := by rw [smul_smul, inv_mul_cancel₀ hp, one_smul]
        _ = _ := by rw [h1, smul_add, smul_smul, smul_smul, div_eq_inv_mul, div_eq_inv_mul]
    have hmem : a ∈ segment ℝ c b :=
      ⟨_, _, div_nonneg (by linarith) (by linarith), div_nonneg (by linarith) (by linarith),
        by rw [← add_div, div_eq_one_iff_eq hp]; ring, ha.symm⟩
    exact hac (hseg ⟨left_mem_segment ℝ a c, hmem⟩)
  · subst hθ
    have : b = a := by simpa [sub_eq_zero] using key
    exact hab this.symm

namespace Polygon

variable (P : Polygon E)

lemma next_ne_self (i : Fin (P.n + 1)) : P.next i ≠ i := by
  intro h
  have h1 : (1 : Fin (P.n + 1)) = 0 := by
    have : i + 1 = i := by simpa [next, finRotate_succ_apply] using h
    simpa using this
  rw [Fin.one_eq_zero_iff] at h1
  have := P.two_le
  omega

lemma last_ne_zero : Fin.last P.n ≠ 0 := by
  intro h
  have := congrArg Fin.val h
  simp only [Fin.val_last, Fin.val_zero] at this
  have := P.two_le
  omega

/-- The vertex before `a = v n`. -/
lemma exists_prev_last : ∃ ia : Fin (P.n + 1), P.next ia = Fin.last P.n :=
  (finRotate (P.n + 1)).surjective _

/-- **The edge arriving at `a = v n` leaves any set meeting the polygon only in `[a, b]`.** -/
lemma apex_ray_not_mem (hP : P.IsSimple) {K : Set E}
    (hK : ∀ x ∈ P.carrier, x ∈ K → x ∈ P.edge (Fin.last P.n)) {ia : Fin (P.n + 1)}
    (hia : P.next ia = Fin.last P.n) {t : ℝ} (ht0 : 0 < t) (ht1 : t ≤ 1) :
    P.v (Fin.last P.n) + t • (P.v ia - P.v (Fin.last P.n)) ∉ K := by
  intro hx
  have hne : ia ≠ Fin.last P.n := by
    rintro rfl; exact P.next_ne_self _ hia
  have hmem : P.v (Fin.last P.n) + t • (P.v ia - P.v (Fin.last P.n)) ∈ P.edge ia := by
    rw [edge, hia]
    exact ⟨t, 1 - t, ht0.le, by linarith, by ring, by module⟩
  have h2 := hK _ (P.edge_subset_carrier ia hmem) hx
  have h3 := hP.2 ia (Fin.last P.n) hne
  rw [if_pos hia.symm] at h3
  have h4 : P.v (Fin.last P.n) + t • (P.v ia - P.v (Fin.last P.n)) ∈
      ({P.v (Fin.last P.n)} : Set E) := h3 ▸ (⟨hmem, h2⟩ : _ ∈ P.edge ia ∩ P.edge (Fin.last P.n))
  rw [mem_singleton_iff, add_eq_left, smul_eq_zero, sub_eq_zero] at h4
  rcases h4 with h | h
  · exact ht0.ne' h
  · exact hne (hP.1 h)

/-- **The edge leaving `b = v 0` leaves any set meeting the polygon only in `[a, b]`.** -/
lemma base_ray_not_mem (hP : P.IsSimple) {K : Set E}
    (hK : ∀ x ∈ P.carrier, x ∈ K → x ∈ P.edge (Fin.last P.n)) {t : ℝ} (ht0 : 0 < t)
    (ht1 : t ≤ 1) : P.v 0 + t • (P.v (P.next 0) - P.v 0) ∉ K := by
  intro hx
  have hmem : P.v 0 + t • (P.v (P.next 0) - P.v 0) ∈ P.edge 0 :=
    ⟨1 - t, t, by linarith, ht0.le, by ring, by module⟩
  have h2 := hK _ (P.edge_subset_carrier 0 hmem) hx
  have h3 := hP.2 (Fin.last P.n) 0 P.last_ne_zero
  rw [if_pos P.next_last.symm] at h3
  have h4 : P.v 0 + t • (P.v (P.next 0) - P.v 0) ∈ ({P.v 0} : Set E) :=
    h3 ▸ (⟨h2, hmem⟩ : _ ∈ P.edge (Fin.last P.n) ∩ P.edge 0)
  rw [mem_singleton_iff, add_eq_left, smul_eq_zero, sub_eq_zero] at h4
  rcases h4 with h | h
  · exact ht0.ne' h
  · exact P.next_ne_self 0 (hP.1 h)

/-- **Only the two neighbouring edges meet the closing edge.** -/
lemma eq_of_meets_last (hP : P.IsSimple) {i : Fin (P.n + 1)} (hi : i ≠ Fin.last P.n)
    (h : (P.edge i ∩ P.edge (Fin.last P.n)).Nonempty) :
    P.next i = Fin.last P.n ∨ i = 0 := by
  have h3 := hP.2 i _ hi
  by_contra hc
  push_neg at hc
  rw [if_neg (fun h' => hc.1 h'.symm), if_neg (by rw [P.next_last]; exact hc.2)] at h3
  rw [h3] at h
  exact not_nonempty_empty h

/-- What simplicity of the subdivided polygon says about `a`, `b`, `c`. -/
lemma subdivideLast_facts (c : E) (hQ : (P.subdivideLast c).IsSimple) :
    c ≠ P.v (Fin.last P.n) ∧ c ≠ P.v 0 ∧
      segment ℝ (P.v (Fin.last P.n)) c ∩ segment ℝ c (P.v 0) ⊆ {c} := by
  refine ⟨fun h => ?_, fun h => ?_, ?_⟩
  · have := hQ.1 (show (P.subdivideLast c).v (Fin.last (P.n + 1)) =
      (P.subdivideLast c).v (Fin.last P.n).castSucc by
        rw [subdivideLast_v_last, subdivideLast_v_castSucc, h])
    exact (Fin.castSucc_lt_last _).ne' this
  · have := hQ.1 (show (P.subdivideLast c).v (Fin.last (P.n + 1)) =
      (P.subdivideLast c).v (0 : Fin (P.n + 1)).castSucc by
        rw [subdivideLast_v_last, subdivideLast_v_castSucc, h])
    exact (Fin.castSucc_lt_last _).ne' this
  · have h3 := hQ.2 (Fin.last P.n).castSucc (Fin.last (P.n + 1)) (Fin.castSucc_lt_last _).ne
    rw [if_pos (P.subdivideLast_next_castSucc_last c).symm, subdivideLast_edge_castSucc_last,
      subdivideLast_edge_last, subdivideLast_v_last] at h3
    exact h3.le

/-- The parametrization on a piece, inside the first period. -/
lemma param_piece (i : Fin (P.n + 1)) {u : ℝ} (h0 : 0 ≤ u) (h1 : u ≤ 1)
    (hlt : ((i : ℝ) + u) / (P.n + 1) < 1) :
    P.param (((i : ℝ) + u) / (P.n + 1)) = (1 - u) • P.v i + u • P.v (P.next i) := by
  rw [param, Int.fract_eq_self.mpr ⟨by positivity, hlt⟩, P.pathRaw_piece i h0 h1]

end Polygon

/-! ### The reparametrization of the Δ-move -/

/-- The unit map: the first `n` pieces are squeezed to `n` of `n + 2`, the closing piece is
stretched over the last two. -/
noncomputable def deltaPsi (n : ℕ) (s : ℝ) : ℝ :=
  max ((n + 1) * s) (2 * (n + 1) * s - n) / (n + 2)

lemma deltaPsi_reparam (n : ℕ) :
    OrientedReparam (fun t => t + (deltaPsi n (Int.fract t) - Int.fract t)) := by
  have hn : (0 : ℝ) < n + 2 := by positivity
  apply OrientedReparam.ofUnit
  · unfold deltaPsi
    exact ((continuous_const.mul continuous_id).max
      ((continuous_const.mul continuous_id).sub continuous_const)).div_const _
  · intro s t hst
    unfold deltaPsi
    apply div_lt_div_of_pos_right _ hn
    have h1 : (n + 1 : ℝ) * s < (n + 1) * t := by
      have : (0 : ℝ) < n + 1 := by positivity
      nlinarith
    exact max_lt (lt_max_of_lt_left h1) (lt_max_of_lt_right (by linarith))
  · unfold deltaPsi
    rw [max_eq_left (by simp)]
    simp
  · unfold deltaPsi
    rw [max_eq_right (by linarith), div_eq_one_iff_eq hn.ne']
    ring

lemma deltaPsi_low (n : ℕ) {x : ℝ} (hx : x ≤ n) :
    deltaPsi n (x / (n + 1)) = x / (n + 2) := by
  have hN : (n + 1 : ℝ) ≠ 0 := by positivity
  have e : (n + 1 : ℝ) * (x / (n + 1)) = x := by field_simp
  have e2 : 2 * (n + 1 : ℝ) * (x / (n + 1)) - n = 2 * x - n := by
    rw [mul_assoc, e]
  unfold deltaPsi
  rw [e, e2, max_eq_left (by linarith)]

lemma deltaPsi_high (n : ℕ) {u : ℝ} (hu : 0 ≤ u) :
    deltaPsi n ((n + u) / (n + 1)) = (n + 2 * u) / (n + 2) := by
  have hN : (n + 1 : ℝ) ≠ 0 := by positivity
  have e : (n + 1 : ℝ) * ((n + u) / (n + 1)) = n + u := by field_simp
  have e2 : 2 * (n + 1 : ℝ) * ((n + u) / (n + 1)) - n = n + 2 * u := by
    rw [mul_assoc, e]; ring
  unfold deltaPsi
  rw [e, e2, max_eq_right (by linarith)]

/-! ### A Δ-move is an ambient isotopy -/

/-- **A Δ-move is realized by an ambient isotopy** of `E`, supported in a convex body around
the triangle. -/
theorem ambientIsotopic_of_delta (L L' : PolygonalLink E) (e : Fin L.k ≃ Fin L'.k)
    (m : Fin L.k) (c : E) (hother : ∀ i, i ≠ m → L'.comp (e i) = L.comp i)
    (hm : L'.comp (e m) = (L.comp m).subdivideLast c)
    (htri : convexHull ℝ {(L.comp m).v (Fin.last _), (L.comp m).v 0, c} ∩ L.carrier =
      segment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) : AmbientIsotopic L L' := by
  set P := L.comp m with hPdef
  set a := P.v (Fin.last P.n) with ha_def
  set b := P.v 0 with hb_def
  have hP : P.IsSimple := L.simple m
  have hQ : (P.subdivideLast c).IsSimple := hm ▸ L'.simple (e m)
  obtain ⟨hca, hcb, hseg⟩ := P.subdivideLast_facts c hQ
  have hab : a ≠ b := fun h => P.last_ne_zero (hP.1 h)
  have hK : ∀ x ∈ P.carrier, x ∈ convexHull ℝ {a, b, c} → x ∈ P.edge (Fin.last P.n) := by
    intro x hx hxT
    rw [P.edge_last, ← htri]
    exact ⟨hxT, L.comp_carrier_subset m hx⟩
  obtain ⟨ia, hia⟩ := P.exists_prev_last
  -- everything of the link that misses the closing edge
  set R' : Set E := ⋃ (j : Fin L.k) (i : Fin ((L.comp j).n + 1))
      (_ : Disjoint ((L.comp j).edge i) (segment ℝ a b)), (L.comp j).edge i with hR'_def
  have hR' : IsCompact R' :=
    isCompact_iUnion fun _ => isCompact_iUnion fun _ => isCompact_iUnion fun _ =>
      isCompact_segment' _ _
  have hdisj : Disjoint R' (convexHull ℝ {a, b, c}) := by
    simp only [hR'_def, Set.disjoint_iUnion_left]
    intro j i hd
    rw [Set.disjoint_left]
    intro x hx hxT
    have hxs : x ∈ segment ℝ a b := by
      rw [← htri]
      exact ⟨hxT, L.comp_carrier_subset j ((L.comp j).edge_subset_carrier i hx)⟩
    exact Set.disjoint_left.mp hd hx hxs
  have hsb : segment ℝ b c ∩ segment ℝ c a ⊆ {c} := by
    rw [segment_symm ℝ b c, segment_symm ℝ c a, inter_comm]; exact hseg
  obtain ⟨ρ, hρ, hA, hB, hR⟩ := exists_deltaBody (a := a) (b := b) (c := c)
    (apex_seg_ne_zero hab hca.symm hseg) (apex_seg_ne_zero hab.symm hcb.symm hsb)
    (fun t ht0 ht1 => P.apex_ray_not_mem hP hK hia ht0 ht1)
    (fun t ht0 ht1 => P.base_ray_not_mem hP hK ht0 ht1) hR' hdisj
  have haI : a ∉ interior (deltaBody a b c ρ) := not_mem_interior_of_ray hA
  have hbI : b ∉ interior (deltaBody a b c ρ) := not_mem_interior_of_ray hB
  have hR'I : ∀ x ∈ R', x ∉ interior (deltaBody a b c ρ) := fun x hx hxI =>
    Set.disjoint_left.mp hR hx (interior_subset hxI)
  -- points of the other components are fixed
  have hfixOther : ∀ j, j ≠ m → ∀ x ∈ (L.comp j).carrier, x ∉ interior (deltaBody a b c ρ) := by
    intro j hj x hx
    obtain ⟨i, hi⟩ := Set.mem_iUnion.mp hx
    apply hR'I
    simp only [hR'_def, Set.mem_iUnion]
    refine ⟨j, i, ?_, hi⟩
    refine (L.disjoint hj).mono ((L.comp j).edge_subset_carrier i) ?_
    rw [← P.edge_last]
    exact P.edge_subset_carrier _
  -- points of the other edges of `comp m` are fixed
  have hfixM : ∀ i : Fin (P.n + 1), i ≠ Fin.last P.n → ∀ x ∈ P.edge i,
      x ∉ interior (deltaBody a b c ρ) := by
    intro i hi x hx
    by_cases hd : Disjoint (P.edge i) (segment ℝ a b)
    · apply hR'I
      simp only [hR'_def, Set.mem_iUnion]
      exact ⟨m, i, hd, hx⟩
    · rw [Set.not_disjoint_iff_nonempty_inter, ← P.edge_last] at hd
      rcases P.eq_of_meets_last hP hi hd with h | h
      · have hi' : i = ia := (finRotate (P.n + 1)).injective (h.trans hia.symm)
        subst hi'
        rw [Polygon.edge, hia] at hx
        obtain ⟨p, q, hp, hq, hpq, rfl⟩ := hx
        have hx' : p • P.v i + q • a = a + p • (P.v i - a) := by
          rw [show q = 1 - p by linarith]; module
        rw [hx']
        rcases hp.lt_or_eq with hp | hp
        · exact fun h' => hA p hp (interior_subset h')
        · rw [← hp, zero_smul, add_zero]; exact haI
      · subst h
        obtain ⟨p, q, hp, hq, hpq, rfl⟩ := hx
        have hx' : p • b + q • P.v (P.next 0) = b + q • (P.v (P.next 0) - b) := by
          rw [show p = 1 - q by linarith]; module
        rw [hx']
        rcases hq.lt_or_eq with hq | hq
        · exact fun h' => hB q hq (interior_subset h')
        · rw [← hq, zero_smul, add_zero]; exact hbI
  -- the component `m`
  have hQn : ((P.subdivideLast c).n : ℝ) + 1 = P.n + 2 := by
    simp only [Polygon.subdivideLast]; push_cast; ring
  have hN : (0 : ℝ) < P.n + 1 := by positivity
  have hfinm : ∀ t, deltaIso a b c hρ 1 (P.param t) =
      (P.subdivideLast c).param (t + (deltaPsi P.n (Int.fract t) - Int.fract t)) := by
    intro t
    have e1 : t + (deltaPsi P.n (Int.fract t) - Int.fract t) =
        deltaPsi P.n (Int.fract t) + ((⌊t⌋ : ℤ) : ℝ) := by
      have := Int.self_sub_fract t; linarith
    rw [e1, Polygon.param_add_int, show P.param t = P.pathRaw (Int.fract t) from rfl]
    obtain ⟨i, u, hu0, hu1, hs⟩ := P.exists_piece (Int.fract_nonneg t) (Int.fract_lt_one t)
    rw [hs, P.pathRaw_piece i hu0 hu1.le]
    induction i using Fin.lastCases with
    | last =>
      rw [P.next_last, Fin.val_last, deltaPsi_high _ hu0]
      rcases le_total u (1 / 2) with hu | hu
      · rw [deltaIso_one_left hρ haI hu0 hu]
        have hx : ((P.n : ℝ) + 2 * u) / (P.n + 2) =
            ((((Fin.last P.n).castSucc : Fin ((P.subdivideLast c).n + 1)) : ℕ) + 2 * u) /
              ((P.subdivideLast c).n + 1) := by
          rw [hQn]; simp
        have hlt : ((P.n : ℝ) + 2 * u) / (P.n + 2) < 1 := by
          rw [div_lt_one (by positivity)]; linarith
        rw [hx] at hlt ⊢
        rw [(P.subdivideLast c).param_piece _ (by linarith) (by linarith) hlt,
          Polygon.subdivideLast_v_castSucc, Polygon.subdivideLast_next_castSucc_last,
          Polygon.subdivideLast_v_last]
      · rw [deltaIso_one_right hρ hbI hu hu1.le]
        have hx : ((P.n : ℝ) + 2 * u) / (P.n + 2) =
            (((Fin.last (P.n + 1) : Fin ((P.subdivideLast c).n + 1)) : ℕ) + (2 * u - 1)) /
              ((P.subdivideLast c).n + 1) := by
          rw [hQn]; simp
        have hlt : ((P.n : ℝ) + 2 * u) / (P.n + 2) < 1 := by
          rw [div_lt_one (by positivity)]; linarith
        rw [hx] at hlt ⊢
        have h0 : (0 : Fin (P.n + 1 + 1)) = (0 : Fin (P.n + 1)).castSucc := rfl
        rw [(P.subdivideLast c).param_piece _ (by linarith) (by linarith) hlt,
          Polygon.subdivideLast_v_last, Polygon.subdivideLast_next_last, h0,
          Polygon.subdivideLast_v_castSucc]
        module
    | cast k =>
      have hk : (k : ℝ) + 1 ≤ P.n := by exact_mod_cast k.isLt
      have hmem : (1 - u) • P.v k.castSucc + u • P.v (P.next k.castSucc) ∈ P.edge k.castSucc :=
        ⟨1 - u, u, by linarith, hu0, by ring, rfl⟩
      rw [deltaIso_of_not_mem hρ 1 (hfixM _ (Fin.castSucc_lt_last k).ne _ hmem),
        Fin.coe_castSucc, deltaPsi_low _ (by linarith)]
      have hx : ((k : ℝ) + u) / (P.n + 2) =
          (((k.castSucc.castSucc : Fin ((P.subdivideLast c).n + 1)) : ℕ) + u) /
            ((P.subdivideLast c).n + 1) := by
        rw [hQn]; simp
      have hlt : ((k : ℝ) + u) / (P.n + 2) < 1 := by
        rw [div_lt_one (by positivity)]; linarith
      rw [hx] at hlt ⊢
      rw [(P.subdivideLast c).param_piece _ hu0 hu1.le hlt, Polygon.subdivideLast_v_castSucc,
        Polygon.subdivideLast_next_castSucc _ _ (Fin.castSucc_lt_last k).ne,
        Polygon.subdivideLast_v_castSucc]
  refine ⟨{ H := deltaIso a b c hρ
            continuous := continuous_deltaIso hρ
            continuous_symm := continuous_deltaIso_symm hρ
            start := deltaIso_zero hρ
            e := e
            finish := fun i => ?_ }⟩
  by_cases him : i = m
  · subst him
    exact ⟨_, deltaPsi_reparam P.n, fun t => by rw [hm]; exact hfinm t⟩
  · refine ⟨id, OrientedReparam.id, fun t => ?_⟩
    rw [hother i him]
    exact deltaIso_of_not_mem hρ 1
      (hfixOther i him _ (by rw [← Polygon.range_param]; exact ⟨t, rfl⟩))

/-- **Every move is an ambient isotopy.** -/
theorem Move.ambientIsotopic {L L' : PolygonalLink E} (h : Move L L') : AmbientIsotopic L L' := by
  cases h with
  | relabel e r h => exact AmbientIsotopic.of_relabel e r h
  | delta e m c hother hm htri => exact ambientIsotopic_of_delta L L' e m c hother hm htri

/-- **Δ-equivalent links are ambient isotopic.** -/
theorem DeltaEquiv.ambientIsotopic {L L' : PolygonalLink E} (h : DeltaEquiv L L') :
    AmbientIsotopic L L' := by
  induction h with
  | rel _ _ h => exact h.ambientIsotopic
  | refl L => exact AmbientIsotopic.refl L
  | symm _ _ _ ih => exact ih.symm
  | trans _ _ _ _ _ ih₁ ih₂ => exact ih₁.trans ih₂

end QOU.MathlibExt.PL
