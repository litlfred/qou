import QOU.MathlibExt.CechSphereBoxes

/-!
# Fine box covers of `S²` reached from the hemispheres by splits

Steps P3c–P3d of the C2 comparison (route R3, surface case).

A **box family** lists, for each index, a box `a < u₀ < b`, `c < u₁ < d` inside a
core box of some hemisphere. A family is **reached** if pulling `H²` back from
the hemisphere cover to it is a bijection. The core boxes are reached
(`hemi_core_bijective`). Cutting one box at the middle of a side, with the two
halves overlapping in the middle half, is a split in the sense of
`split_pull_bijective`, so it keeps the family reached and covering. Halving
every box repeatedly gives, for each `η > 0`, a reached covering box family
whose boxes have both sides at most `η`.

## Results, all sorry-free

* `H2.pull_pull'`: pulling twice is pulling along the composite.
* `BoxData`, `BoxData.fam`, `Reach`, `Covers`.
* `reach_split`: a split keeps a family reached.
* `BoxData.split0`, `BoxData.split1`: halving one box in `u₀` or `u₁`.
* `exists_fine`: reached covering box families with all sides `≤ η`.

## What this does NOT do

It does not bound the diameter of a small box or apply the Lebesgue number
lemma; that is step P4 in `CechSphereGood`, which gives the instance
`HemiComputesCech`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step C2
-/
open CategoryTheory Opposite TopologicalSpace
namespace QOU.CentralExtension.Cech
open CechGerbe

section PullPull
variable {X : Type} [TopologicalSpace X] {G : Type} [TopologicalSpace G] [Group G]
  [IsTopologicalGroup G]

theorem H2.pull_pull' {ι κ μ : Type} {U : ι → Opens X} {V : κ → Opens X} {W : μ → Opens X}
    (r : κ → ι) (f : ∀ j, V j ⟶ U (r j)) (r' : μ → κ) (f' : ∀ m, W m ⟶ V (r' m))
    (z : H2 U (contPresheaf X G)) :
    H2.pull r' f' (H2.pull r f z) = H2.pull (r ∘ r') (fun m => f' m ≫ f (r' m)) z := by
  induction z using Quot.ind with
  | mk c => rfl

end PullPull

variable (G : Type) [TopologicalSpace G] [CommGroup G] [IsTopologicalGroup G] [DiscreteTopology G]

/-- A family is **reached** if pulling `H²` back from the hemispheres to it is a
bijection, along some refinement. -/
def Reach {κ : Type} (U : κ → Opens S2) : Prop :=
  ∃ (r : κ → Fin 4) (hr : ∀ j, U j ≤ hemi (r j)),
    Function.Bijective (H2.pull (𝒜 := contPresheaf S2 G) (U := hemi) r (fun j => homOfLE (hr j)))

/-- A family **covers** the sphere. -/
def Covers {κ : Type} (U : κ → Opens S2) : Prop := ∀ p : S2, ∃ j, p ∈ U j

variable {G}

/-- **A split keeps a family reached.** -/
theorem reach_split {κ : Type} {U : κ → Opens S2} {v : κ} {A B : Opens S2}
    (hA : A ≤ U v) (hB : B ≤ U v) (hcov : U v ≤ A ⊔ B) (hU : ConnFamily U)
    (hU' : ConnFamily (splitFam U v A B)) (h : Reach G U) : Reach G (splitFam U v A B) := by
  obtain ⟨r, hr, hb⟩ := h
  refine ⟨r ∘ splitR v, fun x => (splitFam_le hA hB x).trans (hr _), ?_⟩
  have hc := (split_pull_bijective (G := G) hA hB hcov hU hU').comp hb
  have e : H2.pull (𝒜 := contPresheaf S2 G) (U := hemi) (r ∘ splitR v)
      (fun x => homOfLE ((splitFam_le hA hB x).trans (hr _))) =
      (H2.pull (splitR v) (fun x => homOfLE (splitFam_le hA hB x))) ∘
        (H2.pull r (fun j => homOfLE (hr j))) :=
    funext fun z => (H2.pull_pull' _ _ _ _ z).symm
  rw [e]; exact hc

theorem covers_split {κ : Type} {U : κ → Opens S2} {v : κ} {A B : Opens S2}
    (hcov : U v ≤ A ⊔ B) (h : Covers U) : Covers (splitFam U v A B) := by
  intro p
  obtain ⟨j, hj⟩ := h p
  by_cases hjv : j = v
  · subst hjv
    rcases hcov hj with h | h
    · exact ⟨none, h⟩
    · exact ⟨some j, by simpa using h⟩
  · exact ⟨some j, by rw [splitFam_some_ne hjv]; exact hj⟩

/-! ### Box geometry -/

theorem tfun_pos_of_mem_box {i : Fin 4} {a b c d : ℝ} (hab : a < b) {p : S2}
    (hp : p ∈ box i a b c d) : 0 < tfun i p.1 := box_le_hemi hab hp

theorem box_mono {i : Fin 4} {a b c d a' b' c' d' : ℝ} (ha : a ≤ a') (hb : b' ≤ b)
    (hc : c ≤ c') (hd : d' ≤ d) (hab : a' < b') : box i a' b' c' d' ≤ box i a b c d := by
  intro p hp
  have ht := tfun_pos_of_mem_box hab hp
  obtain ⟨h1, h2, h3, h4⟩ := mem_box.1 hp
  refine mem_box.2 ⟨?_, ?_, ?_, ?_⟩ <;> nlinarith

theorem box_cover0 {i : Fin 4} {a b c d lo hi : ℝ} (hab : a < b) (hlh : lo < hi) :
    box i a b c d ≤ box i a hi c d ⊔ box i lo b c d := by
  intro p hp
  have ht := tfun_pos_of_mem_box hab hp
  obtain ⟨h1, h2, h3, h4⟩ := mem_box.1 hp
  by_cases h : p.1 0 < hi * tfun i p.1
  · exact Or.inl (mem_box.2 ⟨h1, h, h3, h4⟩)
  · exact Or.inr (mem_box.2 ⟨by nlinarith, h2, h3, h4⟩)

theorem box_cover1 {i : Fin 4} {a b c d lo hi : ℝ} (hab : a < b) (hlh : lo < hi) :
    box i a b c d ≤ box i a b c hi ⊔ box i a b lo d := by
  intro p hp
  have ht := tfun_pos_of_mem_box hab hp
  obtain ⟨h1, h2, h3, h4⟩ := mem_box.1 hp
  by_cases h : p.1 1 < hi * tfun i p.1
  · exact Or.inl (mem_box.2 ⟨h1, h2, h3, h⟩)
  · exact Or.inr (mem_box.2 ⟨h1, h2, by nlinarith, h4⟩)

/-! ### Box families -/

/-- A family of boxes inside the core boxes. -/
structure BoxData (κ : Type) where
  i : κ → Fin 4
  a : κ → ℝ
  b : κ → ℝ
  c : κ → ℝ
  d : κ → ℝ
  hab : ∀ j, a j < b j
  hcd : ∀ j, c j < d j
  ha : ∀ j, -3 ≤ a j
  hb : ∀ j, b j ≤ 3
  hc : ∀ j, -3 ≤ c j
  hd : ∀ j, d j ≤ 3

namespace BoxData

variable {κ : Type}

/-- The boxes of a box family. -/
noncomputable def fam (D : BoxData κ) (j : κ) : Opens S2 :=
  box (D.i j) (D.a j) (D.b j) (D.c j) (D.d j)

theorem connFamily (D : BoxData κ) : ConnFamily D.fam := connFamily_of_lc (box_isLC _ _ _ _ _)

open Classical in
/-- Halve box `v` in `u₀`: the halves are `a < u₀ < (a+3b)/4` (index `none`) and
`(3a+b)/4 < u₀ < b` (index `some v`). -/
noncomputable def split0 (D : BoxData κ) (v : κ) : BoxData (Option κ) where
  i x := D.i (splitR v x)
  a x := x.elim (D.a v) fun j => if j = v then (3 * D.a v + D.b v) / 4 else D.a j
  b x := x.elim ((D.a v + 3 * D.b v) / 4) D.b
  c x := D.c (splitR v x)
  d x := D.d (splitR v x)
  hab x := by
    have := D.hab v
    cases x with
    | none => simp only [Option.elim]; linarith
    | some j =>
      simp only [Option.elim]
      split_ifs with h
      · subst h; linarith
      · exact D.hab j
  hcd x := D.hcd _
  ha x := by
    have := D.ha v; have := D.hab v
    cases x with
    | none => exact D.ha v
    | some j =>
      simp only [Option.elim]
      split_ifs with h
      · subst h; linarith
      · exact D.ha j
  hb x := by
    have := D.hb v; have := D.hab v
    cases x with
    | none => simp only [Option.elim]; linarith
    | some j => exact D.hb j
  hc x := D.hc _
  hd x := D.hd _

theorem split0_fam (D : BoxData κ) (v : κ) :
    (D.split0 v).fam = splitFam D.fam v
      (box (D.i v) (D.a v) ((D.a v + 3 * D.b v) / 4) (D.c v) (D.d v))
      (box (D.i v) ((3 * D.a v + D.b v) / 4) (D.b v) (D.c v) (D.d v)) := by
  funext x
  cases x with
  | none => rfl
  | some j =>
    by_cases h : j = v
    · subst h; simp [fam, split0]
    · rw [splitFam_some_ne h]; simp [fam, split0, h]

open Classical in
/-- Halve box `v` in `u₁`. -/
noncomputable def split1 (D : BoxData κ) (v : κ) : BoxData (Option κ) where
  i x := D.i (splitR v x)
  a x := D.a (splitR v x)
  b x := D.b (splitR v x)
  c x := x.elim (D.c v) fun j => if j = v then (3 * D.c v + D.d v) / 4 else D.c j
  d x := x.elim ((D.c v + 3 * D.d v) / 4) D.d
  hab x := D.hab _
  hcd x := by
    have := D.hcd v
    cases x with
    | none => simp only [Option.elim]; linarith
    | some j =>
      simp only [Option.elim]
      split_ifs with h
      · subst h; linarith
      · exact D.hcd j
  ha x := D.ha _
  hb x := D.hb _
  hc x := by
    have := D.hc v; have := D.hcd v
    cases x with
    | none => exact D.hc v
    | some j =>
      simp only [Option.elim]
      split_ifs with h
      · subst h; linarith
      · exact D.hc j
  hd x := by
    have := D.hd v; have := D.hcd v
    cases x with
    | none => simp only [Option.elim]; linarith
    | some j => exact D.hd j

theorem split1_fam (D : BoxData κ) (v : κ) :
    (D.split1 v).fam = splitFam D.fam v
      (box (D.i v) (D.a v) (D.b v) (D.c v) ((D.c v + 3 * D.d v) / 4))
      (box (D.i v) (D.a v) (D.b v) ((3 * D.c v + D.d v) / 4) (D.d v)) := by
  funext x
  cases x with
  | none => rfl
  | some j =>
    by_cases h : j = v
    · subst h; simp [fam, split1]
    · rw [splitFam_some_ne h]; simp [fam, split1, h]

theorem reach_split0 (D : BoxData κ) (v : κ) (h : Reach G D.fam) (hc : Covers D.fam) :
    Reach G (D.split0 v).fam ∧ Covers (D.split0 v).fam := by
  have h1 := D.hab v
  have hA : box (D.i v) (D.a v) ((D.a v + 3 * D.b v) / 4) (D.c v) (D.d v) ≤ D.fam v :=
    box_mono le_rfl (by linarith) le_rfl le_rfl (by linarith)
  have hB : box (D.i v) ((3 * D.a v + D.b v) / 4) (D.b v) (D.c v) (D.d v) ≤ D.fam v :=
    box_mono (by linarith) le_rfl le_rfl le_rfl (by linarith)
  have hcov := box_cover0 (i := D.i v) (c := D.c v) (d := D.d v) h1
    (show (3 * D.a v + D.b v) / 4 < (D.a v + 3 * D.b v) / 4 by linarith)
  rw [split0_fam]
  refine ⟨reach_split hA hB hcov D.connFamily ?_ h, covers_split hcov hc⟩
  rw [← split0_fam]; exact (D.split0 v).connFamily

theorem reach_split1 (D : BoxData κ) (v : κ) (h : Reach G D.fam) (hc : Covers D.fam) :
    Reach G (D.split1 v).fam ∧ Covers (D.split1 v).fam := by
  have h1 := D.hcd v
  have h0 := D.hab v
  have hA : box (D.i v) (D.a v) (D.b v) (D.c v) ((D.c v + 3 * D.d v) / 4) ≤ D.fam v :=
    box_mono le_rfl le_rfl le_rfl (by linarith) h0
  have hB : box (D.i v) (D.a v) (D.b v) ((3 * D.c v + D.d v) / 4) (D.d v) ≤ D.fam v :=
    box_mono le_rfl le_rfl (by linarith) le_rfl h0
  have hcov := box_cover1 (i := D.i v) (a := D.a v) (b := D.b v) (c := D.c v) (d := D.d v) h0
    (show (3 * D.c v + D.d v) / 4 < (D.c v + 3 * D.d v) / 4 by linarith)
  rw [split1_fam]
  refine ⟨reach_split hA hB hcov D.connFamily ?_ h, covers_split hcov hc⟩
  rw [← split1_fam]; exact (D.split1 v).connFamily

end BoxData

/-! ### Halving every box -/

/-- One round in `u₀`: all `u₀`-sides `≤ L` become `≤ 3L/4`, `u₁`-sides `≤ M` stay. -/
theorem halve0 (L M : ℝ) (n : ℕ) :
    ∀ (κ : Type) [Fintype κ] [DecidableEq κ] (D : BoxData κ), Reach G D.fam → Covers D.fam →
      (∀ j, D.b j - D.a j ≤ L) → (∀ j, D.d j - D.c j ≤ M) →
      (Finset.univ.filter (fun j => 3 * L / 4 < D.b j - D.a j)).card ≤ n →
      ∃ (κ' : Type) (_ : Fintype κ') (D' : BoxData κ'), Reach G D'.fam ∧ Covers D'.fam ∧
        (∀ j, D'.b j - D'.a j ≤ 3 * L / 4) ∧ (∀ j, D'.d j - D'.c j ≤ M) := by
  induction n with
  | zero =>
    intro κ _ _ D h hc hL hM hn
    refine ⟨κ, inferInstance, D, h, hc, fun j => ?_, hM⟩
    by_contra hj
    have : j ∈ Finset.univ.filter (fun j => 3 * L / 4 < D.b j - D.a j) := by simp; linarith
    have := Finset.card_pos.2 ⟨j, this⟩
    omega
  | succ n ih =>
    intro κ _ _ D h hc hL hM hn
    by_cases hbad : ∃ v, 3 * L / 4 < D.b v - D.a v
    · obtain ⟨v, hv⟩ := hbad
      obtain ⟨h', hc'⟩ := D.reach_split0 v h hc
      refine ih (Option κ) (D.split0 v) h' hc' (fun x => ?_) (fun x => hM _) ?_
      · have := hL v
        cases x with
        | none => simp only [BoxData.split0, Option.elim]; linarith
        | some j =>
          simp only [BoxData.split0, Option.elim]
          split_ifs with hj
          · subst hj; linarith
          · exact hL j
      · have hsub : (Finset.univ.filter
            (fun x => 3 * L / 4 < (D.split0 v).b x - (D.split0 v).a x)) ⊆
            ((Finset.univ.filter (fun j => 3 * L / 4 < D.b j - D.a j)).erase v).map
              ⟨some, Option.some_injective _⟩ := by
          intro x hx
          simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hx
          have := hL v
          cases x with
          | none => simp only [BoxData.split0, Option.elim] at hx; linarith
          | some j =>
            simp only [BoxData.split0, Option.elim] at hx
            split_ifs at hx with hj
            · subst hj; linarith
            · simp [hj, hx]
        have hlt := Finset.card_erase_of_mem
          (s := Finset.univ.filter (fun j => 3 * L / 4 < D.b j - D.a j)) (a := v) (by simpa using hv)
        have := Finset.card_le_card hsub
        rw [Finset.card_map, hlt] at this
        omega
    · push_neg at hbad
      exact ⟨κ, inferInstance, D, h, hc, hbad, hM⟩

/-- One round in `u₁`. -/
theorem halve1 (L M : ℝ) (n : ℕ) :
    ∀ (κ : Type) [Fintype κ] [DecidableEq κ] (D : BoxData κ), Reach G D.fam → Covers D.fam →
      (∀ j, D.b j - D.a j ≤ L) → (∀ j, D.d j - D.c j ≤ M) →
      (Finset.univ.filter (fun j => 3 * M / 4 < D.d j - D.c j)).card ≤ n →
      ∃ (κ' : Type) (_ : Fintype κ') (D' : BoxData κ'), Reach G D'.fam ∧ Covers D'.fam ∧
        (∀ j, D'.b j - D'.a j ≤ L) ∧ (∀ j, D'.d j - D'.c j ≤ 3 * M / 4) := by
  induction n with
  | zero =>
    intro κ _ _ D h hc hL hM hn
    refine ⟨κ, inferInstance, D, h, hc, hL, fun j => ?_⟩
    by_contra hj
    have : j ∈ Finset.univ.filter (fun j => 3 * M / 4 < D.d j - D.c j) := by simp; linarith
    have := Finset.card_pos.2 ⟨j, this⟩
    omega
  | succ n ih =>
    intro κ _ _ D h hc hL hM hn
    by_cases hbad : ∃ v, 3 * M / 4 < D.d v - D.c v
    · obtain ⟨v, hv⟩ := hbad
      obtain ⟨h', hc'⟩ := D.reach_split1 v h hc
      refine ih (Option κ) (D.split1 v) h' hc' (fun x => hL _) (fun x => ?_) ?_
      · have := hM v
        cases x with
        | none => simp only [BoxData.split1, Option.elim]; linarith
        | some j =>
          simp only [BoxData.split1, Option.elim]
          split_ifs with hj
          · subst hj; linarith
          · exact hM j
      · have hsub : (Finset.univ.filter
            (fun x => 3 * M / 4 < (D.split1 v).d x - (D.split1 v).c x)) ⊆
            ((Finset.univ.filter (fun j => 3 * M / 4 < D.d j - D.c j)).erase v).map
              ⟨some, Option.some_injective _⟩ := by
          intro x hx
          simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hx
          have := hM v
          cases x with
          | none => simp only [BoxData.split1, Option.elim] at hx; linarith
          | some j =>
            simp only [BoxData.split1, Option.elim] at hx
            split_ifs at hx with hj
            · subst hj; linarith
            · simp [hj, hx]
        have hlt := Finset.card_erase_of_mem
          (s := Finset.univ.filter (fun j => 3 * M / 4 < D.d j - D.c j)) (a := v) (by simpa using hv)
        have := Finset.card_le_card hsub
        rw [Finset.card_map, hlt] at this
        omega
    · push_neg at hbad
      exact ⟨κ, inferInstance, D, h, hc, hL, hbad⟩

/-- The core boxes as a box family. -/
noncomputable def coreData : BoxData (Fin 4) where
  i := id
  a _ := -3
  b _ := 3
  c _ := -3
  d _ := 3
  hab _ := by norm_num
  hcd _ := by norm_num
  ha _ := le_rfl
  hb _ := le_rfl
  hc _ := le_rfl
  hd _ := le_rfl

theorem reach_core : Reach G coreData.fam :=
  ⟨id, core_le_hemi, hemi_core_bijective⟩

theorem covers_core : Covers coreData.fam := exists_core

/-- `k` rounds of halving: all sides `≤ 6 (3/4)^k`. -/
theorem exists_round (k : ℕ) :
    ∃ (κ : Type) (_ : Fintype κ) (D : BoxData κ), Reach G D.fam ∧ Covers D.fam ∧
      (∀ j, D.b j - D.a j ≤ 6 * (3 / 4) ^ k) ∧ (∀ j, D.d j - D.c j ≤ 6 * (3 / 4) ^ k) := by
  induction k with
  | zero =>
    refine ⟨Fin 4, inferInstance, coreData, reach_core, covers_core, fun _ => ?_, fun _ => ?_⟩ <;>
      simp [coreData] <;> norm_num
  | succ k ih =>
    obtain ⟨κ, _, D, h, hc, hL, hM⟩ := ih
    classical
    obtain ⟨κ₁, _, D₁, h₁, hc₁, hL₁, hM₁⟩ :=
      halve0 (G := G) _ _ _ κ D h hc hL hM le_rfl
    classical
    obtain ⟨κ₂, _, D₂, h₂, hc₂, hL₂, hM₂⟩ :=
      halve1 (G := G) _ _ _ κ₁ D₁ h₁ hc₁ hL₁ hM₁ le_rfl
    refine ⟨κ₂, inferInstance, D₂, h₂, hc₂, fun j => ?_, fun j => ?_⟩
    · have := hL₂ j; rw [pow_succ]; linarith
    · have := hM₂ j; rw [pow_succ]; linarith

/-- **Fine box covers.** For every `η > 0` some reached covering box family has
all sides at most `η`. -/
theorem exists_fine {η : ℝ} (hη : 0 < η) :
    ∃ (κ : Type) (_ : Fintype κ) (D : BoxData κ), Reach G D.fam ∧ Covers D.fam ∧
      (∀ j, D.b j - D.a j ≤ η) ∧ (∀ j, D.d j - D.c j ≤ η) := by
  obtain ⟨k, hk⟩ := exists_pow_lt_of_lt_one (show 0 < η / 6 by positivity)
    (show (3 / 4 : ℝ) < 1 by norm_num)
  obtain ⟨κ, i, D, h, hc, hL, hM⟩ := exists_round (G := G) k
  refine ⟨κ, i, D, h, hc, fun j => ?_, fun j => ?_⟩
  · have := hL j; linarith
  · have := hM j; linarith

end QOU.CentralExtension.Cech
