/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPolygonalLink

set_option autoImplicit false

/-!
# The crossing parity of a plane polygon (issue #8902, Moise part B, step 1)

The first step towards the polygonal Jordan curve theorem and the PL Schoenflies theorem in the
plane. Mathlib has neither.

## What is a DEFINITION here

* `R2 = Fin 2 → ℝ`, the plane, with coordinates `x 0` (abscissa) and `x 1` (height).
* `cross a b x` — the cross product `(b - a) × (x - a)`.
* `crossInd a b x : ZMod 2` — `1` when the segment `[a, b]` lies strictly above `x` at the
  abscissa of `x`, counted with the half-open rule: exactly one endpoint has abscissa `≤ x 0`.
* `Polygon.parity P x : ZMod 2` — the sum of `crossInd` over the edges of `P`: the parity of the
  number of edges crossed by the vertical ray going up from `x`.

## What is a THEOREM here

* `Polygon.parity_eventually_eq` — **the parity is locally constant off the polygon**: for
  `x ∉ P.carrier`, `P.parity y = P.parity x` for all `y` near `x`. No simplicity is needed. The
  proof is the half-open bookkeeping at vertices on the vertical line through `x`: the
  contributions of the two edges at such a vertex telescope modulo 2.
* `Polygon.parity_const_of_isPreconnected` — so it is constant on every preconnected set that
  misses the polygon.

## Literature

The crossing-number (even–odd) argument for polygons is classical: R. Courant, H. Robbins,
*What is Mathematics?*, Oxford Univ. Press (1941), Ch. V §3.2; E. E. Moise, *Geometric Topology
in Dimensions 2 and 3*, Graduate Texts in Mathematics 47, Springer (1977),
doi:10.1007/978-1-4612-9906-6, Ch. 2.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

/-- The plane, with abscissa `x 0` and height `x 1`. -/
abbrev R2 := Fin 2 → ℝ

/-- The cross product `(b - a) × (x - a)`. -/
def cross (a b x : R2) : ℝ := (b 0 - a 0) * (x 1 - a 1) - (b 1 - a 1) * (x 0 - a 0)

open Classical in
/-- `1` when the segment `[a, b]` passes strictly above `x` at the abscissa of `x`, with the
half-open rule: exactly one endpoint has abscissa `≤ x 0`. -/
noncomputable def crossInd (a b x : R2) : ZMod 2 :=
  if Xor' (a 0 ≤ x 0) (b 0 ≤ x 0) ∧ cross a b x * (b 0 - a 0) < 0 then 1 else 0

open Classical in
/-- `1` when the abscissa of `a` is at most that of `x`. -/
noncomputable def leInd (a x : R2) : ZMod 2 := if a 0 ≤ x 0 then 1 else 0

lemma cross_swap_mul (a b x : R2) :
    cross b a x * (a 0 - b 0) = cross a b x * (b 0 - a 0) := by
  unfold cross; ring

lemma crossInd_swap (a b x : R2) : crossInd b a x = crossInd a b x := by
  unfold crossInd
  simp only [cross_swap_mul, xor_comm]

lemma ind_xor (p q : Prop) [Decidable p] [Decidable q] :
    (if Xor' p q then (1 : ZMod 2) else 0) = (if p then 1 else 0) + (if q then 1 else 0) := by
  by_cases hp : p <;> by_cases hq : q <;> (simp [hp, hq, Xor']; try decide)

lemma continuous_cross (a b : R2) : Continuous (cross a b) := by
  unfold cross
  fun_prop

/-- A point on the line of `[a, b]` at an abscissa between those of `a` and `b` lies on the
segment. -/
lemma mem_segment_of_cross_eq_zero {a b x : R2} (hab : a 0 ≠ b 0)
    (hx : (a 0 ≤ x 0 ∧ x 0 ≤ b 0) ∨ (b 0 ≤ x 0 ∧ x 0 ≤ a 0)) (hc : cross a b x = 0) :
    x ∈ segment ℝ a b := by
  have hd : b 0 - a 0 ≠ 0 := sub_ne_zero.mpr (Ne.symm hab)
  set t := (x 0 - a 0) / (b 0 - a 0) with ht
  have ht0 : 0 ≤ t ∧ t ≤ 1 := by
    rcases hx with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · have hpos : 0 < b 0 - a 0 := by
        rcases lt_or_eq_of_le (h1.trans h2) with h | h
        · linarith
        · exact absurd h hab
      exact ⟨div_nonneg (by linarith) hpos.le, (div_le_one hpos).mpr (by linarith)⟩
    · have hneg : b 0 - a 0 < 0 := by
        rcases lt_or_eq_of_le (h1.trans h2) with h | h
        · linarith
        · exact absurd h.symm hab
      exact ⟨div_nonneg_of_nonpos (by linarith) hneg.le, (div_le_one_of_neg hneg).mpr (by linarith)⟩
  have htd : t * (b 0 - a 0) = x 0 - a 0 := div_mul_cancel₀ _ hd
  have h1 : (b 0 - a 0) * (x 1 - a 1 - t * (b 1 - a 1)) = 0 := by
    unfold cross at hc
    linear_combination hc - (b 1 - a 1) * htd
  have h1' : x 1 - a 1 - t * (b 1 - a 1) = 0 := by
    rcases mul_eq_zero.mp h1 with h | h
    · exact absurd h hd
    · exact h
  refine ⟨1 - t, t, by linarith, ht0.1, by ring, ?_⟩
  funext k
  fin_cases k
  · simp only [Fin.zero_eta, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    linear_combination htd
  · simp only [Fin.mk_one, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    linear_combination -h1'

/-- `a` is on the vertical line through `x`, strictly above `x`. -/
def UpOf (a x : R2) : Prop := a 0 = x 0 ∧ x 1 < a 1

lemma eventually_le_iff_of_ne {a x : R2} (h : a 0 ≠ x 0) :
    ∀ᶠ y in 𝓝 x, (a 0 ≤ y 0 ↔ a 0 ≤ x 0) := by
  have hc : Continuous fun y : R2 => y 0 := continuous_apply 0
  rcases lt_or_gt_of_ne h with h | h
  · filter_upwards [continuousAt_const.eventually_lt hc.continuousAt h] with y hy
    exact ⟨fun _ => h.le, fun _ => hy.le⟩
  · filter_upwards [hc.continuousAt.eventually_lt continuousAt_const h] with y hy
    exact ⟨fun h' => absurd (h'.trans_lt hy) (lt_irrefl _), fun h' => absurd h' (not_le.mpr h)⟩

lemma leInd_eventually {a x : R2} (h : a 0 ≠ x 0) : ∀ᶠ y in 𝓝 x, leInd a y = leInd a x := by
  filter_upwards [eventually_le_iff_of_ne h] with y hy
  unfold leInd
  simp only [hy]

/-- The value of `cross a b · * (b 0 - a 0)` at a point on the vertical line through `a`. -/
lemma cross_mul_of_eq {a b x : R2} (h : a 0 = x 0) :
    cross a b x * (b 0 - a 0) = (b 0 - a 0) ^ 2 * (x 1 - a 1) := by
  unfold cross; rw [h]; ring

lemma segment_vertical {a b x : R2} (ha : a 0 = x 0) (hb : b 0 = x 0) (h1 : a 1 ≤ x 1)
    (h2 : x 1 ≤ b 1) : x ∈ segment ℝ a b := by
  rcases eq_or_lt_of_le (h1.trans h2) with h | h
  · have hx1 : x 1 = a 1 := le_antisymm (h ▸ h2) h1
    have : x = a := by
      funext k; fin_cases k
      · exact ha.symm
      · exact hx1
    rw [this]; exact left_mem_segment ℝ a b
  · set t := (x 1 - a 1) / (b 1 - a 1)
    have hpos : 0 < b 1 - a 1 := by linarith
    refine ⟨1 - t, t, ?_, div_nonneg (by linarith) hpos.le, by ring, ?_⟩
    · have : t ≤ 1 := (div_le_one hpos).mpr (by linarith)
      linarith
    funext k; fin_cases k
    · simp only [Fin.zero_eta, Pi.add_apply, Pi.smul_apply, smul_eq_mul, ha, hb]; ring
    · simp only [Fin.mk_one, Pi.add_apply, Pi.smul_apply, smul_eq_mul, t]
      field_simp; ring

/-- **One edge, when an endpoint is above `x` on its vertical line**: near `x` the indicator is
`leInd a + leInd b`. -/
lemma crossInd_eventually_of_up {a b x : R2} (hU : UpOf a x) :
    ∀ᶠ y in 𝓝 x, crossInd a b y = leInd a y + leInd b y := by
  classical
  obtain ⟨ha0, ha1⟩ := hU
  by_cases hb0 : b 0 = x 0
  · -- both endpoints on the line; `b` is above as well
    refine Eventually.of_forall fun y => ?_
    have hxor : ¬ Xor' (a 0 ≤ y 0) (b 0 ≤ y 0) := by rw [ha0, hb0]; simp [Xor']
    have : leInd a y = leInd b y := by unfold leInd; rw [ha0, hb0]
    unfold crossInd
    rw [if_neg (fun h => hxor h.1), this]
    exact (CharTwo.add_self_eq_zero _).symm
  · have hneg : cross a b x * (b 0 - a 0) < 0 := by
      rw [cross_mul_of_eq ha0]
      have : b 0 - a 0 ≠ 0 := by rw [ha0]; exact sub_ne_zero.mpr hb0
      exact mul_neg_of_pos_of_neg (by positivity) (by linarith)
    have hcont : Continuous fun y => cross a b y * (b 0 - a 0) :=
      (continuous_cross a b).mul continuous_const
    filter_upwards [hcont.continuousAt.eventually_lt continuousAt_const hneg] with y hy
    unfold crossInd leInd
    rw [← ind_xor]
    by_cases hxy : Xor' (a 0 ≤ y 0) (b 0 ≤ y 0)
    · rw [if_pos ⟨hxy, hy⟩, if_pos hxy]
    · rw [if_neg (fun h => hxy h.1), if_neg hxy]

/-- **One edge, when no endpoint is above `x` on its vertical line**: the indicator is constant
near `x`. -/
lemma crossInd_eventually_of_not_up {a b x : R2} (hx : x ∉ segment ℝ a b) (ha : ¬ UpOf a x)
    (hb : ¬ UpOf b x) : ∀ᶠ y in 𝓝 x, crossInd a b y = crossInd a b x := by
  classical
  have hxa : x ≠ a := fun h => hx (h ▸ left_mem_segment ℝ a b)
  have hxb : x ≠ b := fun h => hx (h ▸ right_mem_segment ℝ a b)
  have below : ∀ {c : R2}, c 0 = x 0 → ¬ UpOf c x → x ≠ c → c 1 < x 1 := by
    intro c hc hU hne
    rcases lt_trichotomy (c 1) (x 1) with h | h | h
    · exact h
    · exact absurd (by funext k; fin_cases k; exacts [hc.symm, h.symm]) hne
    · exact absurd ⟨hc, h⟩ hU
  have hcont : Continuous fun y => cross a b y * (b 0 - a 0) :=
    (continuous_cross a b).mul continuous_const
  by_cases ha0 : a 0 = x 0
  · have ha1 := below ha0 ha hxa
    by_cases hb0 : b 0 = x 0
    · refine Eventually.of_forall fun y => ?_
      unfold crossInd
      have : ¬ Xor' (a 0 ≤ y 0) (b 0 ≤ y 0) := by rw [ha0, hb0]; simp [Xor']
      have : ¬ Xor' (a 0 ≤ x 0) (b 0 ≤ x 0) := by rw [ha0, hb0]; simp [Xor']
      rw [if_neg (fun h => ‹¬ Xor' (a 0 ≤ y 0) _› h.1), if_neg (fun h => this h.1)]
    · have hpos : 0 < cross a b x * (b 0 - a 0) := by
        rw [cross_mul_of_eq ha0]
        have : b 0 - a 0 ≠ 0 := by rw [ha0]; exact sub_ne_zero.mpr hb0
        exact mul_pos (by positivity) (by linarith)
      filter_upwards [continuousAt_const.eventually_lt hcont.continuousAt hpos] with y hy
      unfold crossInd
      rw [if_neg (fun h => absurd h.2 (not_lt.mpr hy.le)),
        if_neg (fun h => absurd h.2 (not_lt.mpr hpos.le))]
  · by_cases hb0 : b 0 = x 0
    · have hb1 := below hb0 hb hxb
      have hpos : 0 < cross a b x * (b 0 - a 0) := by
        rw [← cross_swap_mul, cross_mul_of_eq hb0]
        have : a 0 - b 0 ≠ 0 := by rw [hb0]; exact sub_ne_zero.mpr ha0
        exact mul_pos (by positivity) (by linarith)
      filter_upwards [continuousAt_const.eventually_lt hcont.continuousAt hpos] with y hy
      unfold crossInd
      rw [if_neg (fun h => absurd h.2 (not_lt.mpr hy.le)),
        if_neg (fun h => absurd h.2 (not_lt.mpr hpos.le))]
    · -- neither endpoint on the vertical line: the straddle is locally constant
      have hxor : ∀ᶠ y in 𝓝 x, (Xor' (a 0 ≤ y 0) (b 0 ≤ y 0) ↔ Xor' (a 0 ≤ x 0) (b 0 ≤ x 0)) := by
        filter_upwards [eventually_le_iff_of_ne ha0, eventually_le_iff_of_ne hb0] with y h1 h2
        rw [h1, h2]
      by_cases hs : Xor' (a 0 ≤ x 0) (b 0 ≤ x 0)
      · have hne : cross a b x * (b 0 - a 0) ≠ 0 := by
          intro h0
          have hd : b 0 - a 0 ≠ 0 := by
            intro h; rcases hs with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;>
              exact h2 (by linarith)
          have hc : cross a b x = 0 := by
            rcases mul_eq_zero.mp h0 with h | h
            · exact h
            · exact absurd h hd
          refine hx (mem_segment_of_cross_eq_zero (fun h => hd (by rw [h]; ring)) ?_ hc)
          rcases hs with ⟨h1, h2⟩ | ⟨h1, h2⟩
          · exact Or.inl ⟨h1, (not_le.mp h2).le⟩
          · exact Or.inr ⟨h1, (not_le.mp h2).le⟩
        rcases lt_or_gt_of_ne hne with hneg | hpos
        · filter_upwards [hxor, hcont.continuousAt.eventually_lt continuousAt_const hneg] with y
            h1 h2
          unfold crossInd
          rw [if_pos ⟨h1.mpr hs, h2⟩, if_pos ⟨hs, hneg⟩]
        · filter_upwards [hxor, continuousAt_const.eventually_lt hcont.continuousAt hpos] with y
            _ h2
          unfold crossInd
          rw [if_neg (fun h => absurd h.2 (not_lt.mpr h2.le)),
            if_neg (fun h => absurd h.2 (not_lt.mpr hpos.le))]
      · filter_upwards [hxor] with y h1
        unfold crossInd
        rw [if_neg (fun h => hs (h1.mp h.1)), if_neg (fun h => hs h.1)]

namespace Polygon

variable (P : Polygon R2)

/-- The cyclic predecessor of a vertex index. -/
def prev (i : Fin (P.n + 1)) : Fin (P.n + 1) := (finRotate (P.n + 1)).symm i

@[simp] lemma next_prev (i : Fin (P.n + 1)) : P.next (P.prev i) = i :=
  (finRotate (P.n + 1)).apply_symm_apply i

@[simp] lemma prev_next (i : Fin (P.n + 1)) : P.prev (P.next i) = i :=
  (finRotate (P.n + 1)).symm_apply_apply i

/-- **The crossing parity**: the number of edges passing strictly above `x`, modulo 2, with the
half-open rule at vertices. -/
noncomputable def parity (x : R2) : ZMod 2 := ∑ i, crossInd (P.v i) (P.v (P.next i)) x

/-- **The crossing parity is locally constant off the polygon.** -/
theorem parity_eventually_eq {x : R2} (hx : x ∉ P.carrier) :
    ∀ᶠ y in 𝓝 x, P.parity y = P.parity x := by
  classical
  have hxe : ∀ i, x ∉ P.edge i := fun i h => hx (P.edge_subset_carrier i h)
  set U : Fin (P.n + 1) → Prop := fun i => UpOf (P.v i) x with hU
  set t : Fin (P.n + 1) → ZMod 2 := fun i => if U i ∨ U (P.next i) then 1 else 0 with ht
  -- each edge, near `x`
  have h1 : ∀ᶠ y in 𝓝 x, ∀ i, crossInd (P.v i) (P.v (P.next i)) y =
      if U i ∨ U (P.next i) then leInd (P.v i) y + leInd (P.v (P.next i)) y
      else crossInd (P.v i) (P.v (P.next i)) x := by
    rw [eventually_all]
    intro i
    by_cases hi : U i ∨ U (P.next i)
    · simp only [if_pos hi]
      rcases hi with hi | hi
      · exact crossInd_eventually_of_up hi
      · have := crossInd_eventually_of_up (a := P.v (P.next i)) (b := P.v i) hi
        filter_upwards [this] with y hy
        rw [crossInd_swap, hy, add_comm]
    · simp only [if_neg hi]
      push_neg at hi
      exact crossInd_eventually_of_not_up (hxe i) hi.1 hi.2
  -- a vertex next to an "up" vertex is off the vertical line, unless it is itself up
  have hoff : ∀ i, ¬ U i → (U (P.next i) ∨ U (P.prev i)) → P.v i 0 ≠ x 0 := by
    intro i hi hnb h0
    have hxi : x ≠ P.v i := fun h => hx (h ▸ P.vertex_mem_carrier i)
    have hlow : P.v i 1 < x 1 := by
      rcases lt_trichotomy (P.v i 1) (x 1) with h | h | h
      · exact h
      · exact absurd (by funext k; fin_cases k; exacts [h0.symm, h.symm]) hxi
      · exact absurd ⟨h0, h⟩ hi
    rcases hnb with ⟨hn0, hn1⟩ | ⟨hp0, hp1⟩
    · exact hxe i (segment_vertical h0 hn0 hlow.le hn1.le)
    · have := segment_vertical (a := P.v i) (b := P.v (P.prev i)) h0 hp0 hlow.le hp1.le
      apply hxe (P.prev i)
      rw [Polygon.edge, P.next_prev, segment_symm]
      exact this
  have h2 : ∀ᶠ y in 𝓝 x, ∀ i, (¬ U i ∧ (U (P.next i) ∨ U (P.prev i))) →
      leInd (P.v i) y = leInd (P.v i) x := by
    rw [eventually_all]
    intro i
    by_cases hi : ¬ U i ∧ (U (P.next i) ∨ U (P.prev i))
    · filter_upwards [leInd_eventually (hoff i hi.1 hi.2)] with y hy _
      exact hy
    · exact Eventually.of_forall fun y h => absurd h hi
  -- assemble
  have key : ∀ y, (∀ i, crossInd (P.v i) (P.v (P.next i)) y =
      if U i ∨ U (P.next i) then leInd (P.v i) y + leInd (P.v (P.next i)) y
      else crossInd (P.v i) (P.v (P.next i)) x) →
      P.parity y = (∑ i, if U i ∨ U (P.next i) then 0 else crossInd (P.v i) (P.v (P.next i)) x)
        + ∑ i, (t i + t (P.prev i)) * leInd (P.v i) y := by
    intro y hy
    unfold parity
    simp_rw [hy]
    have hsplit : ∀ i, (if U i ∨ U (P.next i) then leInd (P.v i) y + leInd (P.v (P.next i)) y
        else crossInd (P.v i) (P.v (P.next i)) x) =
        (if U i ∨ U (P.next i) then 0 else crossInd (P.v i) (P.v (P.next i)) x) +
          (t i * leInd (P.v i) y + t i * leInd (P.v (P.next i)) y) := by
      intro i
      simp only [ht]
      split_ifs <;> ring
    simp_rw [hsplit, Finset.sum_add_distrib, add_mul, Finset.sum_add_distrib]
    congr 2
    exact (Equiv.sum_comp (finRotate (P.n + 1))
      (fun j => t ((finRotate (P.n + 1)).symm j) * leInd (P.v j) y)).symm.trans (by
        refine Finset.sum_congr rfl fun i _ => ?_
        simp [next]) |>.symm
  filter_upwards [h1, h2] with y hy1 hy2
  rw [key y hy1, key x (h1.self_of_nhds)]
  congr 1
  refine Finset.sum_congr rfl fun i _ => ?_
  by_cases hUi : U i
  · have : t i + t (P.prev i) = 0 := by
      simp only [ht, P.next_prev]
      rw [if_pos (Or.inl hUi), if_pos (Or.inr hUi)]
      decide
    rw [this, zero_mul, zero_mul]
  · by_cases hnb : U (P.next i) ∨ U (P.prev i)
    · rw [hy2 i ⟨hUi, hnb⟩]
    · push_neg at hnb
      have : t i + t (P.prev i) = 0 := by
        simp only [ht, P.next_prev]
        rw [if_neg (by tauto), if_neg (by tauto)]
        ring
      rw [this, zero_mul, zero_mul]

/-- **The crossing parity is constant on a preconnected set missing the polygon.** -/
theorem parity_const_of_isPreconnected {s : Set R2} (hs : IsPreconnected s)
    (hsP : Disjoint s P.carrier) {x y : R2} (hx : x ∈ s) (hy : y ∈ s) :
    P.parity x = P.parity y := by
  letI : TopologicalSpace (ZMod 2) := ⊥
  haveI : DiscreteTopology (ZMod 2) := ⟨rfl⟩
  have hcont : ContinuousOn P.parity s := by
    intro z hz
    have hzP : z ∉ P.carrier := Set.disjoint_left.mp hsP hz
    refine ContinuousAt.continuousWithinAt ?_
    rw [ContinuousAt, nhds_discrete (ZMod 2), tendsto_pure]
    exact P.parity_eventually_eq hzP
  exact hs.constant hcont hx hy

/-! ### Far away, and across an edge -/

/-- The unit vectors of the plane. -/
def e0 : R2 := ![1, 0]

/-- The vertical unit vector. -/
def e1 : R2 := ![0, 1]

@[simp] lemma e0_zero : e0 0 = 1 := rfl
@[simp] lemma e0_one : e0 1 = 0 := rfl
@[simp] lemma e1_zero : e1 0 = 0 := rfl
@[simp] lemma e1_one : e1 1 = 1 := rfl

lemma decomp (z : R2) : z = z 0 • e0 + z 1 • e1 := by
  funext k; fin_cases k <;> simp [e0, e1]

lemma isCompact_segment_R2 (x y : R2) : IsCompact (segment ℝ x y) := by
  rw [segment_eq_image]
  exact isCompact_Icc.image (((continuous_const.sub continuous_id).smul continuous_const).add
    (continuous_id.smul continuous_const))

lemma carrier_subset_convexHull : P.carrier ⊆ convexHull ℝ (range P.v) :=
  iUnion_subset fun _ => segment_subset_convexHull (mem_range_self _) (mem_range_self _)

/-- Left of every vertex, the parity is `0`. -/
theorem parity_eq_zero_of_forall_lt {x : R2} (hx : ∀ i, x 0 < P.v i 0) : P.parity x = 0 := by
  unfold parity
  refine Finset.sum_eq_zero fun i _ => ?_
  unfold crossInd
  rw [if_neg]
  rintro ⟨h, -⟩
  have h1 := hx i
  have h2 := hx (P.next i)
  rcases h with ⟨h, -⟩ | ⟨h, -⟩ <;> linarith

/-- Right of (or level with) every vertex, the parity is `0`. -/
theorem parity_eq_zero_of_forall_le {x : R2} (hx : ∀ i, P.v i 0 ≤ x 0) : P.parity x = 0 := by
  unfold parity
  refine Finset.sum_eq_zero fun i _ => ?_
  unfold crossInd
  rw [if_neg]
  rintro ⟨h, -⟩
  rcases h with ⟨-, h⟩ | ⟨-, h⟩ <;> exact h (hx _)

/-- **Outside the convex hull of the vertices, the parity is `0`.** A separating half-plane
contains the point and points beyond every vertex abscissa. -/
theorem parity_eq_zero_of_not_mem_convexHull {x : R2} (hx : x ∉ convexHull ℝ (range P.v)) :
    P.parity x = 0 := by
  obtain ⟨f, u, hfx, hfb⟩ := geometric_hahn_banach_point_closed (convex_convexHull ℝ _)
    (Set.finite_range P.v).isCompact_convexHull.isClosed hx
  have hf0 : f e0 ≠ 0 ∨ f e1 ≠ 0 := by
    by_contra h
    push_neg at h
    have hz : ∀ z, f z = 0 := fun z => by
      rw [decomp z, map_add, map_smul, map_smul, h.1, h.2]; simp
    have := hfb (P.v 0) (subset_convexHull ℝ _ (mem_range_self 0))
    rw [hz] at this hfx
    linarith
  obtain ⟨d, hd, hd0⟩ : ∃ d : R2, f d < 0 ∧ d 0 ≠ 0 := by
    rcases lt_trichotomy (f e0) 0 with h | h | h
    · exact ⟨e0, h, by simp⟩
    · rcases lt_or_gt_of_ne (hf0.resolve_left (by simp [h])) with h1 | h1
      · exact ⟨e0 + e1, by rw [map_add, h]; simpa using h1, by simp⟩
      · exact ⟨e0 - e1, by rw [map_sub, h]; linarith, by simp⟩
    · exact ⟨-e0, by rw [map_neg]; linarith, by simp⟩
  set H := {z : R2 | f z < u} with hHdef
  have hH : Convex ℝ H := convex_halfSpace_lt f.isLinear u
  have hdisj : Disjoint H P.carrier := disjoint_left.mpr fun z hz hzP =>
    lt_asymm hz (hfb z (P.carrier_subset_convexHull hzP))
  have hmem : ∀ s : ℝ, 0 ≤ s → x + s • d ∈ H := fun s hs => by
    simp only [hHdef, mem_setOf_eq, map_add, map_smul, smul_eq_mul]
    nlinarith
  set M := ∑ i, |P.v i 0| with hM
  have hMi : ∀ i, |P.v i 0| ≤ M := fun i =>
    Finset.single_le_sum (f := fun i => |P.v i 0|) (fun _ _ => abs_nonneg _) (Finset.mem_univ i)
  set s := (M + |x 0| + 1) / |d 0| with hs
  have hd0' : 0 < |d 0| := abs_pos.mpr hd0
  have hs0 : 0 ≤ s := div_nonneg (by positivity) hd0'.le
  have hsd : s * |d 0| = M + |x 0| + 1 := div_mul_cancel₀ _ hd0'.ne'
  have hxs := hmem s hs0
  rw [P.parity_const_of_isPreconnected hH.isPreconnected hdisj (x := x) (y := x + s • d)
    hfx hxs]
  have hcoord : (x + s • d) 0 = x 0 + s * d 0 := by simp
  rcases lt_or_gt_of_ne hd0 with hneg | hpos
  · apply parity_eq_zero_of_forall_lt
    intro i
    rw [hcoord]
    rw [abs_of_neg hneg] at hsd
    have := hMi i
    have := neg_abs_le (P.v i 0)
    have := le_abs_self (x 0)
    nlinarith
  · apply parity_eq_zero_of_forall_le
    intro i
    rw [hcoord]
    rw [abs_of_pos hpos] at hsd
    have := hMi i
    have := le_abs_self (P.v i 0)
    have := neg_abs_le (x 0)
    nlinarith

lemma cross_add_smul_e1 (a b m : R2) (u : ℝ) :
    cross a b (m + u • e1) = cross a b m + (b 0 - a 0) * u := by
  unfold cross; simp; ring

lemma cross_of_mem_segment {a b m : R2} (hm : m ∈ segment ℝ a b) : cross a b m = 0 := by
  obtain ⟨s, t, -, -, hst, rfl⟩ := hm
  unfold cross
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  have : s = 1 - t := by linarith
  subst this
  ring

/-- **Crossing a non-vertical edge flips the parity.** Just below an interior point of a
non-vertical edge of a simple polygon the parity is one more than just above it. -/
theorem parity_flip (hP : P.IsSimple) (i : Fin (P.n + 1)) (h0 : P.v i 0 ≠ P.v (P.next i) 0)
    {m : R2} (hm : m ∈ openSegment ℝ (P.v i) (P.v (P.next i))) :
    ∃ r > 0, ∀ s : ℝ, 0 < s → s < r → m + s • e1 ∉ P.carrier ∧ m - s • e1 ∉ P.carrier ∧
      P.parity (m - s • e1) = P.parity (m + s • e1) + 1 := by
  classical
  set a := P.v i
  set b := P.v (P.next i)
  have hab : a ≠ b := fun h => h0 (by rw [h])
  have hma : m ≠ a := fun h => hab (left_mem_openSegment_iff.mp (h ▸ hm))
  have hmb : m ≠ b := fun h => hab (right_mem_openSegment_iff.mp (h ▸ hm))
  have hmseg : m ∈ segment ℝ a b := openSegment_subset_segment ℝ a b hm
  -- `m` misses every other edge
  have hmK : ∀ j, j ≠ i → m ∉ P.edge j := by
    intro j hj hmj
    have := hP.2 i j hj.symm
    have hmem : m ∈ P.edge i ∩ P.edge j := ⟨hmseg, hmj⟩
    rw [this] at hmem
    split_ifs at hmem with h1 h2
    · exact hmb (by rw [mem_singleton_iff.mp hmem, h1])
    · exact hma (mem_singleton_iff.mp hmem)
    · exact hmem
  set K := ⋃ j ∈ ({i}ᶜ : Finset (Fin (P.n + 1))), P.edge j with hK
  have hKc : IsClosed K := by
    refine Set.Finite.isClosed_biUnion (Finset.finite_toSet _) fun j _ => ?_
    exact (isCompact_segment_R2 _ _).isClosed
  have hmK' : m ∉ K := by
    simp only [hK, mem_iUnion, not_exists]
    intro j hj
    exact hmK j (by simpa using hj)
  obtain ⟨r, hr, hball⟩ := Metric.isOpen_iff.mp hKc.isOpen_compl m hmK'
  have hnorm : ∀ u : ℝ, ‖u • e1‖ ≤ |u| := by
    intro u
    refine (pi_norm_le_iff_of_nonneg (abs_nonneg u)).mpr fun k => ?_
    fin_cases k <;> simp [e1]
  have hinball : ∀ u : ℝ, |u| < r → m + u • e1 ∈ Metric.ball m r := by
    intro u hu
    rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left]
    exact (hnorm u).trans_lt hu
  have hoffK : ∀ u : ℝ, |u| < r → ∀ j, j ≠ i → m + u • e1 ∉ P.edge j := by
    intro u hu j hj hmem
    have := hball (hinball u hu)
    apply this
    simp only [hK, mem_iUnion]
    exact ⟨j, by simpa using hj, hmem⟩
  -- the edge itself is met only at `m` on the vertical through `m`
  obtain ⟨tm, htm0, htm1, hmeq⟩ : ∃ t : ℝ, 0 < t ∧ t < 1 ∧ m = a + t • (b - a) := by
    obtain ⟨s', t', hs', ht', hst, rfl⟩ := hm
    refine ⟨t', ht', by linarith, ?_⟩
    have : s' = 1 - t' := by linarith
    subst this
    funext k; simp; ring
  have hoffi : ∀ u : ℝ, u ≠ 0 → m + u • e1 ∉ P.edge i := by
    intro u hu hmem
    obtain ⟨s', t', -, -, hst, heq⟩ := hmem
    have h0' := congrFun heq 0
    have h1' := congrFun heq 1
    have hm0 := congrFun hmeq 0
    have hm1 := congrFun hmeq 1
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, e1_zero, e1_one, Pi.sub_apply,
      mul_zero, add_zero, mul_one] at h0' h1' hm0 hm1
    have hs' : s' = 1 - t' := by linarith
    subst hs'
    change (1 - t') * a 0 + t' * b 0 = m 0 at h0'
    change (1 - t') * a 1 + t' * b 1 = m 1 + u at h1'
    have hd : b 0 - a 0 ≠ 0 := sub_ne_zero.mpr (Ne.symm h0)
    have ht : t' = tm := by
      have : (t' - tm) * (b 0 - a 0) = 0 := by linear_combination h0' + hm0
      rcases mul_eq_zero.mp this with h | h
      · linarith
      · exact absurd h hd
    subst ht
    apply hu
    linear_combination -h1' - hm1
  refine ⟨r, hr, fun s hs hsr => ⟨?_, ?_, ?_⟩⟩
  · intro hmem
    obtain ⟨j, hj⟩ := mem_iUnion.mp hmem
    by_cases hji : j = i
    · exact hoffi s hs.ne' (hji ▸ hj)
    · exact hoffK s (by rw [abs_of_pos hs]; exact hsr) j hji hj
  · intro hmem
    obtain ⟨j, hj⟩ := mem_iUnion.mp hmem
    have hneg : m - s • e1 = m + (-s) • e1 := by rw [neg_smul, sub_eq_add_neg]
    rw [hneg] at hj
    by_cases hji : j = i
    · exact hoffi (-s) (by linarith) (hji ▸ hj)
    · exact hoffK (-s) (by rw [abs_neg, abs_of_pos hs]; exact hsr) j hji hj
  · -- termwise comparison
    have hneg : m - s • e1 = m + (-s) • e1 := by rw [neg_smul, sub_eq_add_neg]
    have hterm : ∀ j, crossInd (P.v j) (P.v (P.next j)) (m - s • e1) =
        crossInd (P.v j) (P.v (P.next j)) (m + s • e1) + if j = i then 1 else 0 := by
      intro j
      rw [hneg]
      set p := P.v j
      set q := P.v (P.next j)
      have hx0 : ∀ u : ℝ, (m + u • e1) 0 = m 0 := by intro u; simp
      unfold crossInd
      simp only [hx0, cross_add_smul_e1]
      by_cases hji : j = i
      · subst hji
        rw [if_pos rfl]
        have hcm : cross p q m = 0 := cross_of_mem_segment hmseg
        have hd : q 0 - p 0 ≠ 0 := sub_ne_zero.mpr (Ne.symm h0)
        have hsq : 0 < (q 0 - p 0) ^ 2 := by positivity
        have hxor : Xor' (p 0 ≤ m 0) (q 0 ≤ m 0) := by
          have hm0 := congrFun hmeq 0
          simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, Pi.sub_apply] at hm0
          rcases lt_or_gt_of_ne h0 with hlt | hgt
          · left
            exact ⟨by nlinarith, by nlinarith⟩
          · right
            exact ⟨by nlinarith, by nlinarith⟩
        rw [if_pos ⟨hxor, by rw [hcm]; nlinarith⟩, if_neg (fun h => by
          have := h.2; rw [hcm] at this; nlinarith)]
        decide
      · rw [if_neg hji, add_zero]
        by_cases hxor : Xor' (p 0 ≤ m 0) (q 0 ≤ m 0)
        · have hd : q 0 - p 0 ≠ 0 := by
            intro h; rcases hxor with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> exact h2 (by linarith)
          -- the sign cannot change between `-s` and `s`
          have hiff : (cross p q m + (q 0 - p 0) * -s) * (q 0 - p 0) < 0 ↔
              (cross p q m + (q 0 - p 0) * s) * (q 0 - p 0) < 0 := by
            constructor
            · intro hlo
              by_contra hhi
              push_neg at hhi
              set u := -(cross p q m) / (q 0 - p 0)
              have hcu : cross p q m + (q 0 - p 0) * u = 0 := by
                simp only [u]; field_simp; ring
              have hsq : 0 < (q 0 - p 0) ^ 2 := by positivity
              have hlo' : (q 0 - p 0) ^ 2 * (-s - u) < 0 := by
                have : (cross p q m + (q 0 - p 0) * -s) * (q 0 - p 0) =
                    (q 0 - p 0) ^ 2 * (-s - u) := by
                  linear_combination (q 0 - p 0) * hcu
                linarith
              have hhi' : 0 ≤ (q 0 - p 0) ^ 2 * (s - u) := by
                have : (cross p q m + (q 0 - p 0) * s) * (q 0 - p 0) =
                    (q 0 - p 0) ^ 2 * (s - u) := by
                  linear_combination (q 0 - p 0) * hcu
                linarith
              have hu1 : -s < u := by nlinarith
              have hu2 : u ≤ s := by nlinarith
              have hmem : m + u • e1 ∈ P.edge j := by
                refine mem_segment_of_cross_eq_zero (fun h => hd (sub_eq_zero.mpr h.symm)) ?_ ?_
                · simp only [hx0]
                  rcases hxor with ⟨h1, h2⟩ | ⟨h1, h2⟩
                  · exact Or.inl ⟨h1, (not_le.mp h2).le⟩
                  · exact Or.inr ⟨h1, (not_le.mp h2).le⟩
                · rw [cross_add_smul_e1]; exact hcu
              exact hoffK u (abs_lt.mpr ⟨by linarith, by linarith⟩) j hji hmem
            · intro hhi
              have hsq : 0 ≤ (q 0 - p 0) ^ 2 := sq_nonneg _
              nlinarith
          simp only [hxor, true_and, hiff]
        · simp only [hxor, false_and, if_false]
    unfold parity
    rw [Finset.sum_congr rfl fun j _ => hterm j, Finset.sum_add_distrib, Finset.sum_ite_eq']
    simp

end Polygon

end QOU.MathlibExt.PL
