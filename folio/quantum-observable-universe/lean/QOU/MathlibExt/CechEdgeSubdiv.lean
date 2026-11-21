import QOU.MathlibExt.CechPLComplex

/-!
# Stellar subdivision of an edge, as a homeomorphism (route R3, step S3b)

Let `F` be a finite simplicial complex on `V` and `a ≠ b` two vertices. Subdividing
the edge `{a, b}` adds a vertex (index `none` in `Option V`) and replaces every
face `f ⊇ {a, b}` by the two faces `(f \ {b}) ∪ {m}` and `(f \ {a}) ∪ {m}`;
faces not containing both `a` and `b` are kept. Geometrically `m` is the
midpoint of the edge.

## Results, all sorry-free

* `sub F a b`: the subdivided complex on `Option V`.
* `fwd`, `bwd`: the linear map `q ↦ p` (half of the `m`-coordinate goes to each of
  `a`, `b`) and its piecewise-linear inverse (`q_m = 2 min(p_a, p_b)`).
* `homeo`: they restrict to a homeomorphism `PSpace (sub F a b) ≃ₜ PSpace F`.
* `bwd_none_pos`, `bwd_a_pos`, `bwd_b_pos`, `bwd_some_pos`: in the old barycentric
  coordinates `p`, the new stars are `p_a, p_b > 0`, `p_a > p_b`, `p_b > p_a`, and
  `p_w > 0` (`w ≠ a, b`).

## What this does NOT do

It does not compare Čech `H²` (that is `CechSubdivCover`), and it does not
control mesh. The identification of any realised complex with Bring's curve is
a citation, and `hχ` (Poincaré–Hopf) stays a hypothesis downstream.
Bean `qou-skn4`.

-- Ref: [leitner2026] lifting-and-descent, route R3, surface step S3/S4
-/
open Topology TopologicalSpace

set_option linter.unusedSectionVars false

namespace QOU.CentralExtension.Cech.PL

variable {V : Type} [Fintype V] [DecidableEq V]

/-- The complex after subdividing the edge `{a, b}`; the new vertex is `none`. -/
def sub (F : Finset (Finset V)) (a b : V) : Finset (Finset (Option V)) :=
  (F.filter (fun f => ¬ (a ∈ f ∧ b ∈ f))).image (fun f => f.image some) ∪
    (F.filter (fun f => a ∈ f ∧ b ∈ f)).biUnion
      (fun f => {insert none ((f.erase b).image some), insert none ((f.erase a).image some)})

variable {F : Finset (Finset V)} {a b : V}

theorem mem_sub {g : Finset (Option V)} :
    g ∈ sub F a b ↔ (∃ f ∈ F, ¬ (a ∈ f ∧ b ∈ f) ∧ g = f.image some) ∨
      (∃ f ∈ F, a ∈ f ∧ b ∈ f ∧
        (g = insert none ((f.erase b).image some) ∨ g = insert none ((f.erase a).image some))) := by
  simp only [sub, Finset.mem_union, Finset.mem_image, Finset.mem_filter, Finset.mem_biUnion,
    Finset.mem_insert, Finset.mem_singleton]
  constructor
  · rintro (⟨f, ⟨hf, h⟩, rfl⟩ | ⟨f, ⟨hf, ha, hb⟩, h⟩)
    · exact Or.inl ⟨f, hf, h, rfl⟩
    · exact Or.inr ⟨f, hf, ha, hb, h⟩
  · rintro (⟨f, hf, h, rfl⟩ | ⟨f, hf, ha, hb, h⟩)
    · exact Or.inl ⟨f, ⟨hf, h⟩, rfl⟩
    · exact Or.inr ⟨f, ⟨hf, ha, hb⟩, h⟩

/-- Every new face lies over an old face. -/
theorem sub_over {g : Finset (Option V)} (hg : g ∈ sub F a b) :
    ∃ f ∈ F, (∀ w, some w ∈ g → w ∈ f) ∧ (none ∈ g → a ∈ f ∧ b ∈ f) := by
  rcases mem_sub.1 hg with ⟨f, hf, h, rfl⟩ | ⟨f, hf, ha, hb, rfl | rfl⟩
  · exact ⟨f, hf, fun w hw => by simpa using hw, fun hn => by simp at hn⟩
  · exact ⟨f, hf, fun w hw => by
      simp only [Finset.mem_insert, Finset.mem_image, Finset.mem_erase] at hw
      rcases hw with h | ⟨u, ⟨-, hu⟩, e⟩
      · cases h
      · cases e; exact hu, fun _ => ⟨ha, hb⟩⟩
  · exact ⟨f, hf, fun w hw => by
      simp only [Finset.mem_insert, Finset.mem_image, Finset.mem_erase] at hw
      rcases hw with h | ⟨u, ⟨-, hu⟩, e⟩
      · cases h
      · cases e; exact hu, fun _ => ⟨ha, hb⟩⟩

/-- No new face contains both `a` and `b`. -/
theorem sub_not_both {g : Finset (Option V)} (hg : g ∈ sub F a b) :
    ¬ (some a ∈ g ∧ some b ∈ g) := by
  rintro ⟨ha, hb⟩
  rcases mem_sub.1 hg with ⟨f, hf, h, rfl⟩ | ⟨f, hf, -, -, rfl | rfl⟩
  · exact h ⟨by simpa using ha, by simpa using hb⟩
  · simp at hb
  · simp at ha

/-! ### The two maps -/

/-- Weight with which the new vertex feeds `w`. -/
noncomputable def hw (a b w : V) : ℝ := if w = a ∨ w = b then 1 / 2 else 0

/-- New barycentric coordinates to old ones. -/
noncomputable def fwd (a b : V) (q : Option V → ℝ) : V → ℝ :=
  fun w => q (some w) + hw a b w * q none

/-- Old barycentric coordinates to new ones. -/
noncomputable def bwd (a b : V) (p : V → ℝ) : Option V → ℝ
  | none => 2 * min (p a) (p b)
  | some w => p w - 2 * hw a b w * min (p a) (p b)

theorem sum_hw (hab : a ≠ b) : ∑ w, hw a b w = 1 := by
  have : ∀ w, hw a b w = (if w = a then 1 / 2 else 0) + (if w = b then 1 / 2 else 0) := by
    intro w; unfold hw
    by_cases h1 : w = a
    · subst h1; simp [hab]
    · by_cases h2 : w = b
      · subst h2; simp [h1]
      · simp [h1, h2]
  simp only [this, Finset.sum_add_distrib, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  norm_num

theorem hw_nonneg (w : V) : 0 ≤ hw a b w := by unfold hw; split_ifs <;> norm_num

theorem hw_a : hw a b a = 1 / 2 := by simp [hw]
theorem hw_b : hw a b b = 1 / 2 := by simp [hw]
theorem hw_other {w : V} (ha : w ≠ a) (hb : w ≠ b) : hw a b w = 0 := by simp [hw, ha, hb]

theorem sum_option (q : Option V → ℝ) : ∑ x, q x = q none + ∑ w, q (some w) :=
  Fintype.sum_option q

theorem fwd_mem (hab : a ≠ b) {q : Option V → ℝ} (hq : q ∈ Real4 (sub F a b)) :
    fwd a b q ∈ Real4 F := by
  obtain ⟨hq0, hq1, g, hg, hqg⟩ := hq
  obtain ⟨f, hf, hsome, hnone⟩ := sub_over hg
  refine ⟨fun w => add_nonneg (hq0 _) (mul_nonneg (hw_nonneg w) (hq0 _)), ?_, f, hf, fun w hw' => ?_⟩
  · unfold fwd
    rw [Finset.sum_add_distrib, ← Finset.sum_mul, sum_hw hab, one_mul, ← hq1, sum_option]
    ring
  · unfold fwd at hw'
    by_cases h1 : 0 < q (some w)
    · exact hsome w (hqg _ h1)
    · have h2 : 0 < hw a b w * q none := by linarith [hq0 (some w)]
      have hn : 0 < q none := pos_of_mul_pos_right h2 (hw_nonneg w)
      have hw0 : hw a b w ≠ 0 := fun h => by rw [h, zero_mul] at h2; exact lt_irrefl _ h2
      obtain ⟨ha, hb⟩ := hnone (hqg _ hn)
      unfold hw at hw0
      split_ifs at hw0 with h
      · rcases h with rfl | rfl <;> assumption
      · exact (hw0 rfl).elim

theorem bwd_mem (hab : a ≠ b) {p : V → ℝ} (hp : p ∈ Real4 F) : bwd a b p ∈ Real4 (sub F a b) := by
  obtain ⟨hp0, hp1, f, hf, hpf⟩ := hp
  set m := min (p a) (p b) with hm
  have hm0 : 0 ≤ m := le_min (hp0 a) (hp0 b)
  have hnn : ∀ w, 0 ≤ p w - 2 * hw a b w * m := by
    intro w
    by_cases h1 : w = a
    · subst h1; rw [hw_a]; linarith [min_le_left (p w) (p b)]
    · by_cases h2 : w = b
      · subst h2; rw [hw_b]; linarith [min_le_right (p a) (p w)]
      · rw [hw_other h1 h2]; linarith [hp0 w]
  refine ⟨fun x => ?_, ?_, ?_⟩
  · cases x with
    | none => simp only [bwd]; linarith
    | some w => exact hnn w
  · rw [sum_option]
    simp only [bwd]
    rw [Finset.sum_sub_distrib, hp1, ← Finset.sum_mul, ← Finset.mul_sum, sum_hw hab]
    ring
  · by_cases hboth : a ∈ f ∧ b ∈ f
    · rcases le_total (p a) (p b) with hle | hle
      · refine ⟨insert none ((f.erase a).image some), mem_sub.2 (Or.inr ⟨f, hf, hboth.1, hboth.2,
          Or.inr rfl⟩), fun x hx => ?_⟩
        cases x with
        | none => simp
        | some w =>
          simp only [bwd] at hx
          simp only [Finset.mem_insert, Finset.mem_image, Finset.mem_erase, reduceCtorEq, false_or,
            Option.some.injEq]
          refine ⟨w, ⟨fun e => ?_, ?_⟩, rfl⟩
          · subst e; rw [hw_a, min_eq_left hle] at hx; linarith
          · exact hpf w (by linarith [mul_nonneg (mul_nonneg (by norm_num : (0:ℝ) ≤ 2)
              (hw_nonneg (a := a) (b := b) w)) hm0])
      · refine ⟨insert none ((f.erase b).image some), mem_sub.2 (Or.inr ⟨f, hf, hboth.1, hboth.2,
          Or.inl rfl⟩), fun x hx => ?_⟩
        cases x with
        | none => simp
        | some w =>
          simp only [bwd] at hx
          simp only [Finset.mem_insert, Finset.mem_image, Finset.mem_erase, reduceCtorEq, false_or,
            Option.some.injEq]
          refine ⟨w, ⟨fun e => ?_, ?_⟩, rfl⟩
          · subst e; rw [hw_b, min_eq_right hle] at hx; linarith
          · exact hpf w (by linarith [mul_nonneg (mul_nonneg (by norm_num : (0:ℝ) ≤ 2)
              (hw_nonneg (a := a) (b := b) w)) hm0])
    · have hm' : m = 0 := by
        by_cases ha : a ∈ f
        · have hb : b ∉ f := fun hb => hboth ⟨ha, hb⟩
          have : p b = 0 := le_antisymm (not_lt.1 fun h => hb (hpf b h)) (hp0 b)
          rw [hm, this]; exact min_eq_right (hp0 a)
        · have : p a = 0 := le_antisymm (not_lt.1 fun h => ha (hpf a h)) (hp0 a)
          rw [hm, this]; exact min_eq_left (hp0 b)
      refine ⟨f.image some, mem_sub.2 (Or.inl ⟨f, hf, hboth, rfl⟩), fun x hx => ?_⟩
      cases x with
      | none => simp only [bwd] at hx; rw [← hm, hm'] at hx; simp at hx
      | some w =>
        simp only [bwd] at hx; rw [← hm, hm'] at hx
        simp only [mul_zero, sub_zero] at hx
        exact Finset.mem_image_of_mem _ (hpf w hx)

theorem fwd_bwd (hab : a ≠ b) (p : V → ℝ) : fwd a b (bwd a b p) = p := by
  funext w
  simp only [fwd, bwd]
  ring

theorem min_eq_zero_of_mem {q : Option V → ℝ} (hq : q ∈ Real4 (sub F a b)) :
    min (q (some a)) (q (some b)) = 0 := by
  obtain ⟨hq0, -, g, hg, hqg⟩ := hq
  by_cases ha : 0 < q (some a)
  · have hb : q (some b) = 0 := le_antisymm
      (not_lt.1 fun hb => sub_not_both hg ⟨hqg _ ha, hqg _ hb⟩) (hq0 _)
    rw [hb]; exact min_eq_right (hq0 _)
  · have : q (some a) = 0 := le_antisymm (not_lt.1 ha) (hq0 _)
    rw [this]; exact min_eq_left (hq0 _)

theorem bwd_fwd (hab : a ≠ b) {q : Option V → ℝ} (hq : q ∈ Real4 (sub F a b)) :
    bwd a b (fwd a b q) = q := by
  have hmin : min (fwd a b q a) (fwd a b q b) = q none / 2 := by
    simp only [fwd, hw_a, hw_b]
    rw [show q (some a) + 1 / 2 * q none = q none / 2 + q (some a) by ring,
      show q (some b) + 1 / 2 * q none = q none / 2 + q (some b) by ring, min_add_add_left,
      min_eq_zero_of_mem hq, add_zero]
  funext x
  cases x with
  | none => simp only [bwd]; rw [hmin]; ring
  | some w => simp only [bwd]; rw [hmin]; simp only [fwd]; ring

theorem continuous_fwd : Continuous (fwd (V := V) a b) :=
  continuous_pi fun w => (continuous_apply _).add (continuous_const.mul (continuous_apply _))

theorem continuous_bwd : Continuous (bwd (V := V) a b) := by
  have hm : Continuous fun p : V → ℝ => min (p a) (p b) :=
    (continuous_apply a).min (continuous_apply b)
  refine continuous_pi fun x => ?_
  cases x with
  | none => exact continuous_const.mul hm
  | some w => exact (continuous_apply w).sub (continuous_const.mul hm)

/-- **Edge subdivision is a homeomorphism of realisations.** -/
noncomputable def homeo (F : Finset (Finset V)) (hab : a ≠ b) : PSpace (sub F a b) ≃ₜ PSpace F where
  toFun q := ⟨fwd a b q.1, fwd_mem hab q.2⟩
  invFun p := ⟨bwd a b p.1, bwd_mem hab p.2⟩
  left_inv q := Subtype.ext (bwd_fwd hab q.2)
  right_inv p := Subtype.ext (fwd_bwd hab p.1)
  continuous_toFun := (continuous_fwd.comp continuous_subtype_val).subtype_mk _
  continuous_invFun := (continuous_bwd.comp continuous_subtype_val).subtype_mk _

theorem homeo_apply (hab : a ≠ b) (q : PSpace (sub F a b)) :
    (homeo F hab q).1 = fwd a b q.1 := rfl

theorem homeo_symm_apply (hab : a ≠ b) (p : PSpace F) :
    ((homeo F hab).symm p).1 = bwd a b p.1 := rfl

/-! ### The new stars in old coordinates -/

theorem bwd_none_pos {p : V → ℝ} : 0 < bwd a b p none ↔ 0 < p a ∧ 0 < p b := by
  simp only [bwd]
  constructor
  · intro h; have := lt_min_iff.1 (by linarith : 0 < min (p a) (p b)); exact this
  · intro h; have := lt_min_iff.2 h; linarith

theorem bwd_a_pos (hab : a ≠ b) {p : V → ℝ} : 0 < bwd a b p (some a) ↔ p b < p a := by
  simp only [bwd, hw_a]
  rw [show p a - 2 * (1 / 2) * min (p a) (p b) = p a - min (p a) (p b) by ring, sub_pos,
    min_lt_iff]
  simp

theorem bwd_b_pos (hab : a ≠ b) {p : V → ℝ} : 0 < bwd a b p (some b) ↔ p a < p b := by
  simp only [bwd, hw_b]
  rw [show p b - 2 * (1 / 2) * min (p a) (p b) = p b - min (p a) (p b) by ring, sub_pos,
    min_lt_iff]
  simp

theorem bwd_some_pos {w : V} (ha : w ≠ a) (hb : w ≠ b) {p : V → ℝ} :
    0 < bwd a b p (some w) ↔ 0 < p w := by
  simp [bwd, hw_other ha hb]

end QOU.CentralExtension.Cech.PL
