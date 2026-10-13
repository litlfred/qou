import QOU.MathlibExt.TemperleyLiebNormalForm
import Mathlib.Combinatorics.Enumerative.DyckWord

/-!
# `card (NormalIdx m) = catalan (m+1)` for every `m`

`TemperleyLiebNormalForm` checks the count of Jones normal-form indices against
`catalan` by `decide` at `m ≤ 6` only, and names the general statement as open.
This file proves it for every `m`, by an explicit equivalence

    NormalIdx m  ≃  { p : DyckWord // p.semilength = m + 1 }

with Mathlib's Dyck words, then `DyckWord.card_dyckWord_semilength_eq_catalan`.

## The bijection

A pair `(I, J)` is a word of length `m` in four letters — `J`-only, `I`-only,
both, neither — and the threshold condition says the height
`#J-prefix − #I-prefix` never goes negative and returns to `0`. Double every
letter and wrap the result in `U … D`:

    J-only ↦ U U,   I-only ↦ D D,   neither ↦ U D,   both ↦ D U .

So position `0` is `U`, positions `2y+1, 2y+2` encode the letter at `y < m`, and
position `2m+1` is `D`. The inverse reads `y ∈ I ↔ w[2y+1] = D` and
`y ∈ J ↔ w[2y+2] = U`. The prefix counts at odd positions are

    #U(2x+1) + |I ∩ [0,x)| = 1 + x + |J ∩ [0,x)|,
    #D(2x+1) + |J ∩ [0,x)| = |I ∩ [0,x)| + x,

(`cnt_odd`), from which the Dyck prefix condition is exactly the threshold
condition, and the total balance is exactly `|I| = |J|`.

## Scope

This is the **counting** half only: the index type of the Jones normal forms has
exactly `catalan (m+1)` elements. It does **not** prove that the elements
`NormalIdx.elt δ p` span `TL_{m+1}(δ)`, nor that they are linearly independent,
so it does **not** prove `dim TL_{m+1}(δ) = catalan (m+1)`. What remains for that:
(1) spanning — closure of `span (range (NormalIdx.elt δ))` under left multiplication
by each `e k`, on the `(I, J)` index (`TemperleyLiebDeltaRule.e_mul_elt_eq_smul`
covers one branch only); (2) linear independence — a representation of
`TL_{m+1}(δ)` (e.g. the planar-diagram algebra) separating the normal forms.
With (1) this file gives `finrank ≤ catalan (m+1)`; with (1) and (2), equality.

-- Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.MathlibExt.TemperleyLiebNormalIdxCatalan

open QOU.MathlibExt.TemperleyLiebNormalForm
open DyckStep Finset

/-! ## Prefix counts on `ℕ` -/

/-- Number of `k < x` lying in `S`. -/
def pc (S : Finset ℕ) (x : ℕ) : ℕ := ∑ k ∈ range x, if k ∈ S then 1 else 0

theorem pc_zero (S : Finset ℕ) : pc S 0 = 0 := by simp [pc]

theorem pc_succ (S : Finset ℕ) (x : ℕ) :
    pc S (x + 1) = pc S x + if x ∈ S then 1 else 0 := Finset.sum_range_succ _ _

/-- Number of `k < t` with `f k = a`. -/
def cnt (f : ℕ → DyckStep) (a : DyckStep) (t : ℕ) : ℕ :=
  ∑ k ∈ range t, if f k = a then 1 else 0

theorem cnt_zero (f : ℕ → DyckStep) (a : DyckStep) : cnt f a 0 = 0 := by simp [cnt]

theorem cnt_succ (f : ℕ → DyckStep) (a : DyckStep) (t : ℕ) :
    cnt f a (t + 1) = cnt f a t + if f t = a then 1 else 0 := Finset.sum_range_succ _ _

theorem cnt_add_two (f : ℕ → DyckStep) (a : DyckStep) (t : ℕ) :
    cnt f a (t + 2) = cnt f a t + (if f t = a then 1 else 0)
      + (if f (t + 1) = a then 1 else 0) := by
  rw [show t + 2 = t + 1 + 1 by ring, cnt_succ f a (t + 1), cnt_succ f a t]

theorem count_map_range (f : ℕ → DyckStep) (a : DyckStep) (t : ℕ) :
    ((List.range t).map f).count a = cnt f a t := by
  induction t with
  | zero => simp [cnt]
  | succ t ih =>
      rw [List.range_succ, List.map_append, List.count_append, ih, cnt_succ]
      simp [List.count_singleton]

/-! ## The doubled word -/

/-- The step at position `k` of the Dyck word attached to `(I, J)` on `m` letters. -/
def step (m : ℕ) (I J : Finset ℕ) (k : ℕ) : DyckStep :=
  if k = 0 then U else if k = 2 * m + 1 then D
  else if k % 2 = 1 then (if k / 2 ∈ I then D else U)
  else (if k / 2 - 1 ∈ J then U else D)

theorem step_zero (m : ℕ) (I J : Finset ℕ) : step m I J 0 = U := by simp [step]

theorem step_last (m : ℕ) (I J : Finset ℕ) : step m I J (2 * m + 1) = D := by
  simp [step]

theorem step_odd {m : ℕ} (I J : Finset ℕ) {y : ℕ} (hy : y < m) :
    step m I J (2 * y + 1) = if y ∈ I then D else U := by
  have h1 : 2 * y + 1 ≠ 0 := by omega
  have h2 : 2 * y + 1 ≠ 2 * m + 1 := by omega
  have h3 : (2 * y + 1) % 2 = 1 := by omega
  have h4 : (2 * y + 1) / 2 = y := by omega
  simp only [step, h1, h2, h3, h4, if_false, if_true]

theorem step_even {m : ℕ} (I J : Finset ℕ) (y : ℕ) :
    step m I J (2 * y + 2) = if y ∈ J then U else D := by
  have h1 : 2 * y + 2 ≠ 0 := by omega
  have h2 : 2 * y + 2 ≠ 2 * m + 1 := by omega
  have h3 : ¬ (2 * y + 2) % 2 = 1 := by omega
  have h4 : (2 * y + 2) / 2 - 1 = y := by omega
  simp only [step, h1, h2, h3, h4, if_false]

/-- **The prefix counts at odd positions.** -/
theorem cnt_odd {m : ℕ} (I J : Finset ℕ) :
    ∀ x ≤ m, cnt (step m I J) U (2 * x + 1) + pc I x = 1 + x + pc J x ∧
      cnt (step m I J) D (2 * x + 1) + pc J x = pc I x + x := by
  intro x
  induction x with
  | zero =>
      intro _
      rw [show 2 * 0 + 1 = 0 + 1 from rfl, cnt_succ, cnt_succ, cnt_zero, cnt_zero, step_zero,
        pc_zero, pc_zero]
      simp
  | succ x ih =>
      intro hx
      obtain ⟨ihU, ihD⟩ := ih (by omega)
      rw [show 2 * (x + 1) + 1 = 2 * x + 1 + 2 by ring, cnt_add_two _ U (2 * x + 1),
        cnt_add_two _ D (2 * x + 1), show 2 * x + 1 + 1 = 2 * x + 2 by ring,
        step_odd I J (by omega : x < m), step_even I J x, pc_succ, pc_succ]
      by_cases hI : x ∈ I <;> by_cases hJ : x ∈ J <;> simp [hI, hJ] <;> omega

/-- **The prefix counts at even positions** (one step past an odd one). -/
theorem cnt_even {m : ℕ} (I J : Finset ℕ) {x : ℕ} (hx : x < m) :
    cnt (step m I J) U (2 * x + 2) = cnt (step m I J) U (2 * x + 1)
        + (if x ∈ I then 0 else 1) ∧
      cnt (step m I J) D (2 * x + 2) = cnt (step m I J) D (2 * x + 1)
        + (if x ∈ I then 1 else 0) := by
  rw [show 2 * x + 2 = 2 * x + 1 + 1 by ring, cnt_succ _ U (2 * x + 1), cnt_succ _ D (2 * x + 1),
    step_odd I J hx]
  by_cases hI : x ∈ I <;> simp [hI]

/-- **The final position** is `D`. -/
theorem cnt_last {m : ℕ} (I J : Finset ℕ) :
    cnt (step m I J) U (2 * m + 2) = cnt (step m I J) U (2 * m + 1) ∧
      cnt (step m I J) D (2 * m + 2) = cnt (step m I J) D (2 * m + 1) + 1 := by
  rw [show 2 * m + 2 = 2 * m + 1 + 1 by ring, cnt_succ _ U (2 * m + 1), cnt_succ _ D (2 * m + 1),
    step_last]
  simp

/-- The Dyck word attached to `(I, J)` on `m` letters. -/
def wordOf (m : ℕ) (I J : Finset ℕ) : List DyckStep :=
  (List.range (2 * m + 2)).map (step m I J)

theorem count_take_wordOf (m : ℕ) (I J : Finset ℕ) (a : DyckStep) (i : ℕ) :
    ((wordOf m I J).take i).count a = cnt (step m I J) a (min i (2 * m + 2)) := by
  rw [wordOf, ← List.map_take, List.take_range, count_map_range]

theorem count_wordOf (m : ℕ) (I J : Finset ℕ) (a : DyckStep) :
    (wordOf m I J).count a = cnt (step m I J) a (2 * m + 2) := by
  rw [wordOf, count_map_range]

/-! ## Dyck conditions ↔ the normal-form conditions -/

/-- Threshold domination at every `x ≤ m`, from the `x+1 ≤ m` form. -/
theorem pc_le_of_dom {m : ℕ} {I J : Finset ℕ}
    (hdom : ∀ x < m, pc I (x + 1) ≤ pc J (x + 1)) : ∀ x ≤ m, pc I x ≤ pc J x := by
  intro x hx
  cases x with
  | zero => simp [pc_zero]
  | succ x => exact hdom x (by omega)

/-- **Forward:** the normal-form conditions make `wordOf` a Dyck word. -/
theorem prefix_of_dom {m : ℕ} {I J : Finset ℕ}
    (hdom : ∀ x < m, pc I (x + 1) ≤ pc J (x + 1)) (t : ℕ) (ht : t ≤ 2 * m + 2) :
    cnt (step m I J) D t ≤ cnt (step m I J) U t := by
  have hle := pc_le_of_dom hdom
  rcases Nat.even_or_odd t with ⟨y, hy⟩ | ⟨x, hx⟩
  · cases y with
    | zero =>
        have : t = 0 := by omega
        subst this; simp [cnt_zero]
    | succ x =>
        have ht' : t = 2 * x + 2 := by omega
        subst ht'
        obtain ⟨oU, oD⟩ := cnt_odd (m := m) I J x (by omega)
        by_cases hxm : x < m
        · obtain ⟨eU, eD⟩ := cnt_even I J hxm
          have hd := hdom x hxm
          rw [pc_succ, pc_succ] at hd
          rw [eU, eD]
          by_cases hI : x ∈ I <;> by_cases hJ : x ∈ J <;> simp [hI, hJ] at hd ⊢ <;> omega
        · have hxm' : x = m := by omega
          subst hxm'
          obtain ⟨lU, lD⟩ := cnt_last (m := x) I J
          rw [lU, lD]
          have := hle x le_rfl
          omega
  · subst hx
    obtain ⟨oU, oD⟩ := cnt_odd (m := m) I J x (by omega)
    have := hle x (by omega)
    omega

theorem balance_of_card {m : ℕ} {I J : Finset ℕ} (hcard : pc J m = pc I m) :
    cnt (step m I J) U (2 * m + 2) = cnt (step m I J) D (2 * m + 2) := by
  obtain ⟨oU, oD⟩ := cnt_odd I J m le_rfl
  obtain ⟨lU, lD⟩ := cnt_last (m := m) I J
  omega

theorem semilength_of_card {m : ℕ} {I J : Finset ℕ} (hcard : pc J m = pc I m) :
    cnt (step m I J) U (2 * m + 2) = m + 1 := by
  obtain ⟨oU, oD⟩ := cnt_odd I J m le_rfl
  obtain ⟨lU, lD⟩ := cnt_last (m := m) I J
  omega

/-- **Converse:** a Dyck prefix condition on `wordOf` gives threshold domination. -/
theorem dom_of_prefix {m : ℕ} {I J : Finset ℕ}
    (hpre : ∀ t ≤ 2 * m + 2, cnt (step m I J) D t ≤ cnt (step m I J) U t) :
    ∀ x < m, pc I (x + 1) ≤ pc J (x + 1) := by
  intro x hx
  obtain ⟨oU, oD⟩ := cnt_odd (m := m) I J (x + 1) (by omega)
  have := hpre (2 * (x + 1) + 1) (by omega)
  omega

theorem card_of_balance {m : ℕ} {I J : Finset ℕ}
    (hbal : cnt (step m I J) U (2 * m + 2) = cnt (step m I J) D (2 * m + 2)) :
    pc J m = pc I m := by
  obtain ⟨oU, oD⟩ := cnt_odd I J m le_rfl
  obtain ⟨lU, lD⟩ := cnt_last (m := m) I J
  omega

/-! ## From `Finset (Fin m)` to `Finset ℕ` -/

/-- The image of a set of generators in `ℕ`. -/
def toNat {m : ℕ} (I : Finset (Fin m)) : Finset ℕ := I.map Fin.valEmbedding

theorem mem_toNat {m : ℕ} (I : Finset (Fin m)) (k : ℕ) :
    k ∈ toNat I ↔ ∃ h : k < m, (⟨k, h⟩ : Fin m) ∈ I := by
  simp only [toNat, Finset.mem_map, Fin.valEmbedding_apply]
  constructor
  · rintro ⟨y, hy, rfl⟩; exact ⟨y.isLt, hy⟩
  · rintro ⟨h, hk⟩; exact ⟨⟨k, h⟩, hk, rfl⟩

theorem pc_toNat {m : ℕ} (I : Finset (Fin m)) (n : ℕ) :
    pc (toNat I) n = (I.filter (fun y => y.val < n)).card := by
  rw [pc, ← Finset.card_filter]
  have : (range n).filter (· ∈ toNat I) = (I.filter (fun y => y.val < n)).map
      Fin.valEmbedding := by
    ext k
    simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_map, Fin.valEmbedding_apply,
      mem_toNat]
    constructor
    · rintro ⟨hk, h, hI⟩; exact ⟨⟨k, h⟩, ⟨hI, hk⟩, rfl⟩
    · rintro ⟨y, ⟨hy, hyn⟩, rfl⟩; exact ⟨hyn, y.isLt, hy⟩
  rw [this, Finset.card_map]

theorem pc_toNat_le {m : ℕ} (I : Finset (Fin m)) (x : Fin m) :
    pc (toNat I) (x.val + 1) = (I.filter (· ≤ x)).card := by
  rw [pc_toNat]
  congr 1
  apply Finset.filter_congr
  intro y _
  rw [Fin.le_iff_val_le_val]; omega

theorem pc_toNat_card {m : ℕ} (I : Finset (Fin m)) : pc (toNat I) m = I.card := by
  rw [pc_toNat, Finset.filter_true_of_mem (fun y _ => y.isLt)]

/-- The normal-form conditions in the `ℕ`-encoded form. -/
theorem normal_iff {m : ℕ} (I J : Finset (Fin m)) :
    (J.card = I.card ∧ ∀ x : Fin m, (I.filter (· ≤ x)).card ≤ (J.filter (· ≤ x)).card) ↔
      (pc (toNat J) m = pc (toNat I) m ∧
        ∀ x < m, pc (toNat I) (x + 1) ≤ pc (toNat J) (x + 1)) := by
  rw [pc_toNat_card, pc_toNat_card]
  refine and_congr Iff.rfl ⟨fun h x hx => ?_, fun h x => ?_⟩
  · have := h ⟨x, hx⟩
    rwa [← pc_toNat_le, ← pc_toNat_le] at this
  · rw [← pc_toNat_le, ← pc_toNat_le]; exact h x.val x.isLt

/-! ## The equivalence -/

/-- The Dyck word of a normal-form index. -/
def toDyck {m : ℕ} (p : NormalIdx m) : DyckWord where
  toList := wordOf m (toNat p.1.1) (toNat p.1.2)
  count_U_eq_count_D := by
    have h := ((normal_iff p.1.1 p.1.2).mp p.2).1
    rw [count_wordOf, count_wordOf]; exact balance_of_card h
  count_D_le_count_U i := by
    have h := ((normal_iff p.1.1 p.1.2).mp p.2).2
    rw [count_take_wordOf, count_take_wordOf]
    exact prefix_of_dom h _ (min_le_right _ _)

theorem semilength_toDyck {m : ℕ} (p : NormalIdx m) : (toDyck p).semilength = m + 1 := by
  have h := ((normal_iff p.1.1 p.1.2).mp p.2).1
  show (wordOf m _ _).count U = m + 1
  rw [count_wordOf]; exact semilength_of_card h

/-- The `I`-set read off a list: `y ∈ I ↔ w[2y+1] = D`. -/
def readI {m : ℕ} (w : List DyckStep) : Finset (Fin m) :=
  univ.filter (fun y : Fin m => w[2 * y.val + 1]? = some D)

/-- The `J`-set read off a list: `y ∈ J ↔ w[2y+2] = U`. -/
def readJ {m : ℕ} (w : List DyckStep) : Finset (Fin m) :=
  univ.filter (fun y : Fin m => w[2 * y.val + 2]? = some U)

theorem mem_toNat_readI {m : ℕ} (w : List DyckStep) {y : ℕ} (hy : y < m) :
    y ∈ toNat (readI (m := m) w) ↔ w[2 * y + 1]? = some D := by
  rw [mem_toNat]; simp [readI, hy]

theorem mem_toNat_readJ {m : ℕ} (w : List DyckStep) {y : ℕ} (hy : y < m) :
    y ∈ toNat (readJ (m := m) w) ↔ w[2 * y + 2]? = some U := by
  rw [mem_toNat]; simp [readJ, hy]

/-- **Every Dyck word of semilength `m+1` is the doubled word of what it reads.** -/
theorem toList_eq_wordOf {m : ℕ} (d : DyckWord) (hd : d.semilength = m + 1) :
    d.toList = wordOf m (toNat (readI (m := m) d.toList)) (toNat (readJ (m := m) d.toList)) := by
  have hlen : d.toList.length = 2 * m + 2 := by
    rw [← d.two_mul_semilength_eq_length, hd]; ring
  have hne : d.toList ≠ [] := by
    intro h; rw [h] at hlen; simp at hlen
  apply List.ext_getElem?
  intro k
  by_cases hk : k < 2 * m + 2
  · rw [wordOf, List.getElem?_map, List.getElem?_range hk, List.getElem?_eq_getElem (by omega)]
    simp only [Option.map_some, Option.some.injEq]
    by_cases h0 : k = 0
    · subst h0
      rw [step_zero, ← List.head_eq_getElem (h := hne)]
      exact d.head_eq_U hne
    by_cases hl : k = 2 * m + 1
    · subst hl
      rw [step_last]
      have := d.getLast_eq_D hne
      rw [List.getLast_eq_getElem] at this
      simpa [hlen] using this
    obtain ⟨y, hy | hy⟩ : ∃ y, k = 2 * y + 1 ∨ k = 2 * y + 2 := ⟨(k - 1) / 2, by omega⟩
    · subst hy
      have hym : y < m := by omega
      have hm := mem_toNat_readI (m := m) d.toList hym
      rw [List.getElem?_eq_getElem (by omega : 2 * y + 1 < d.toList.length)] at hm
      rw [step_odd _ _ hym]
      rcases (d.toList[2 * y + 1]).dichotomy with h | h <;> simp [h] at hm <;> simp [h, hm]
    · subst hy
      have hym : y < m := by omega
      have hm := mem_toNat_readJ (m := m) d.toList hym
      rw [List.getElem?_eq_getElem (by omega : 2 * y + 2 < d.toList.length)] at hm
      rw [step_even]
      rcases (d.toList[2 * y + 2]).dichotomy with h | h <;> simp [h] at hm <;> simp [h, hm]
  · rw [List.getElem?_eq_none (by omega), List.getElem?_eq_none (by simp [wordOf]; omega)]

/-- The normal-form index of a Dyck word of semilength `m+1`. -/
def ofDyck {m : ℕ} (d : {d : DyckWord // d.semilength = m + 1}) : NormalIdx m :=
  ⟨(readI d.1.toList, readJ d.1.toList), by
    rw [normal_iff]
    have hw := toList_eq_wordOf d.1 d.2
    have hbal := d.1.count_U_eq_count_D
    have hpre := d.1.count_D_le_count_U
    rw [hw, count_wordOf, count_wordOf] at hbal
    refine ⟨card_of_balance hbal, dom_of_prefix fun t ht => ?_⟩
    have := hpre t
    rw [hw, count_take_wordOf, count_take_wordOf, min_eq_left ht] at this
    exact this⟩

theorem readI_wordOf {m : ℕ} (I J : Finset (Fin m)) :
    readI (m := m) (wordOf m (toNat I) (toNat J)) = I := by
  ext y
  simp only [readI, Finset.mem_filter, Finset.mem_univ, true_and, wordOf, List.getElem?_map,
    List.getElem?_range, show 2 * y.val + 1 < 2 * m + 2 by omega, Option.map_some,
    Option.some.injEq, step_odd _ _ y.isLt, mem_toNat]
  by_cases h : y ∈ I
  · simp [h]
  · simp [h]

theorem readJ_wordOf {m : ℕ} (I J : Finset (Fin m)) :
    readJ (m := m) (wordOf m (toNat I) (toNat J)) = J := by
  ext y
  simp only [readJ, Finset.mem_filter, Finset.mem_univ, true_and, wordOf, List.getElem?_map,
    List.getElem?_range, show 2 * y.val + 2 < 2 * m + 2 by omega, Option.map_some,
    Option.some.injEq, step_even, mem_toNat]
  by_cases h : y ∈ J
  · simp [h]
  · simp [h]

/-- **Jones normal-form indices ≃ Dyck words of semilength `m+1`.** -/
def equivDyck (m : ℕ) : NormalIdx m ≃ {d : DyckWord // d.semilength = m + 1} where
  toFun p := ⟨toDyck p, semilength_toDyck p⟩
  invFun := ofDyck
  left_inv p := by
    apply Subtype.ext
    show (readI (m := m) (wordOf m _ _), readJ (m := m) (wordOf m _ _)) = p.1
    rw [readI_wordOf, readJ_wordOf]
  right_inv d := by
    apply Subtype.ext
    apply DyckWord.ext
    exact (toList_eq_wordOf d.1 d.2).symm

/-- **The number of Jones normal forms of `TL_{m+1}(δ)` is `catalan (m+1)`, for every
`m`.** Generalises `card_zero … card_six`, which were `decide` at `m ≤ 6`. -/
theorem card_normalIdx (m : ℕ) : Fintype.card (NormalIdx m) = catalan (m + 1) := by
  rw [Fintype.card_congr (equivDyck m), DyckWord.card_dyckWord_semilength_eq_catalan]

/-- Cross-check against the corpus's `decide` value at `m = 6`. -/
example : Fintype.card (NormalIdx 6) = catalan 7 := card_normalIdx 6

end QOU.MathlibExt.TemperleyLiebNormalIdxCatalan
