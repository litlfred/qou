import QOU.MassTheory.StaircaseNearMin2
import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Finset.Max
import Mathlib.Tactic.Linarith

/-!
# The `q`-hook divisibility `∏_{c} [h(c)] ∣ [n]!`

Partition count behind `conj:cyclotomic-boundary-at-keystone`. The files `QHookTop`,
`StaircaseNearMin` and `StaircaseNearMin2` carry the divisibility `[n]! = g · H(s)` as a
hypothesis (`_of_eq`). This file proves it (Stanley, EC2, §7.21; `[stanley1999]`), so the
hypothesis can be dropped.

* `qint_eq_prod_cyclotomic`, `hookProd_dvd_qfact_of_count`: since `[k] = ∏_{1 < d ∣ k} Φ_d`,
  the divisibility holds if, for every `d ≥ 2`, at most as many cells have `d ∣ h(c)` as there
  are multiples of `d` in `1, …, n`.
* `bead_bound`: on a `d`-abacus, `d · #(bead–gap pairs) + C(|B|, 2) ≤ ∑ B`.
* `mul_card_hook_dvd_le`: `d · #{c : d ∣ h(c)} ≤ n`. A cell `(i, j)` gives the bead
  `β_i = λ_i + L - 1 - i` and the gap `β_i - h(i,j) = L + j - λ'_j`, and `∑ β = n + C(L, 2)`.
* `hookProd_dvd_qfact`: `H(s) ∣ [n]!` for every Young diagram `s`.
* `coeff_sum_qHook`, `coeff_sum_sym_qHook`, `coeff_sum_sym_qHook_two_uncond`: the leading,
  `a₁` and `a₂` coefficient statements with the quotient `qHookQuot s = [n]! / H(s)`, no
  hypothesis.
-/

namespace QOU.Mass.StaircaseMinimisers

open Finset Polynomial

/-- `[k]` is the product of the cyclotomic polynomials `Φ_d`, `1 < d ∣ k`. -/
theorem qint_eq_prod_cyclotomic {k M : ℕ} (hk : 1 ≤ k) (hkM : k ≤ M) :
    qint k = ∏ d ∈ (range (M + 1)).filter (2 ≤ ·),
      (if d ∣ k then cyclotomic d ℤ else 1) := by
  rw [qint, ← prod_cyclotomic_eq_geom_sum (by omega) ℤ, ← prod_filter]
  congr 1
  ext d
  simp only [mem_erase, Nat.mem_divisors, mem_filter, mem_range]
  constructor
  · rintro ⟨h1, h2, -⟩
    have := Nat.le_of_dvd (by omega) h2
    have : d ≠ 0 := by rintro rfl; simp at h2; omega
    omega
  · rintro ⟨⟨-, h2⟩, h3⟩; exact ⟨by omega, h3, by omega⟩

theorem prod_qint_eq {ι : Type*} (I : Finset ι) (f : ι → ℕ) (M : ℕ)
    (hf : ∀ i ∈ I, 1 ≤ f i ∧ f i ≤ M) :
    ∏ i ∈ I, qint (f i) = ∏ d ∈ (range (M + 1)).filter (2 ≤ ·),
      cyclotomic d ℤ ^ (I.filter (fun i => d ∣ f i)).card := by
  rw [prod_congr rfl fun i hi => qint_eq_prod_cyclotomic (hf i hi).1 (hf i hi).2, prod_comm]
  refine prod_congr rfl fun d _ => ?_
  rw [← prod_filter, prod_const]

/-- **The `q`-hook divisibility reduces to counting.** If for every `d ≥ 2` at most as many hooks
of `s` as integers in `1..n` are divisible by `d`, then `∏ [h] ∣ [n]!`. -/
theorem hookProd_dvd_qfact_of_count (s : Finset (ℕ × ℕ))
    (hcount : ∀ d, 2 ≤ d → (s.filter (fun c => d ∣ hook s c)).card ≤
      ((range s.card).filter (fun k => d ∣ k + 1)).card) :
    hookProd s ∣ qfact s.card := by
  set M := ∑ c ∈ s, hook s c + s.card
  have h1 : hookProd s = ∏ d ∈ (range (M + 1)).filter (2 ≤ ·),
      cyclotomic d ℤ ^ (s.filter (fun c => d ∣ hook s c)).card := by
    refine prod_qint_eq s (hook s) M fun c hc => ⟨hook_pos s c, ?_⟩
    have := single_le_sum (f := hook s) (fun _ _ => Nat.zero_le _) hc
    omega
  have h2 : qfact s.card = ∏ d ∈ (range (M + 1)).filter (2 ≤ ·),
      cyclotomic d ℤ ^ ((range s.card).filter (fun k => d ∣ k + 1)).card := by
    refine prod_qint_eq (range s.card) (fun k => k + 1) M fun k hk => ⟨Nat.le_add_left 1 k, ?_⟩
    simp only [mem_range] at hk; show k + 1 ≤ M; omega
  rw [h1, h2]
  exact prod_dvd_prod_of_dvd _ _ fun d hd =>
    pow_dvd_pow _ (hcount d (mem_filter.1 hd).2)

end QOU.Mass.StaircaseMinimisers


namespace QOU.Mass.StaircaseMinimisers

open Finset

/-- Bead–gap pairs on a `d`-abacus: a bead `b ∈ B` and an empty position `x < b` on its runner. -/
def beadGaps (d : ℕ) (B : Finset ℕ) : Finset (ℕ × ℕ) :=
  (B ×ˢ B.biUnion range).filter (fun p => p.2 < p.1 ∧ p.2 ∉ B ∧ d ∣ p.1 - p.2)

theorem mem_beadGaps {d : ℕ} {B : Finset ℕ} {p : ℕ × ℕ} :
    p ∈ beadGaps d B ↔ p.1 ∈ B ∧ p.2 < p.1 ∧ p.2 ∉ B ∧ d ∣ p.1 - p.2 := by
  simp only [beadGaps, mem_filter, mem_product, mem_biUnion, mem_range]
  constructor
  · rintro ⟨⟨h1, -⟩, h2⟩; exact ⟨h1, h2⟩
  · rintro ⟨h1, h2⟩; exact ⟨⟨h1, p.1, h1, h2.1⟩, h2⟩

/-- `ℓ` distinct naturals sum to at least `C(ℓ, 2)`. -/
theorem choose_two_le_sum (B : Finset ℕ) : B.card.choose 2 ≤ ∑ b ∈ B, b := by
  induction B using Finset.induction_on_max with
  | h0 => simp
  | step a s ha ih =>
    have has : a ∉ s := fun h => lt_irrefl a (ha a h)
    rw [card_insert_of_notMem has, sum_insert has, show (s.card + 1).choose 2 = s.card.choose 1 + s.card.choose 2 from
      Nat.choose_succ_succ _ 1, Nat.choose_one_right]
    have : s.card ≤ a := by
      calc s.card ≤ (range a).card := card_le_card fun x hx => mem_range.2 (ha x hx)
        _ = a := card_range a
    omega

theorem dvd_sub_cases {d x y : ℕ} (h : d ∣ y - x) (hxy : x < y) : y - x = d ∨ 2 * d ≤ y - x := by
  obtain ⟨t, ht⟩ := h
  rcases t with _ | _ | t
  · omega
  · left; simpa using ht
  · right; rw [ht]; nlinarith [Nat.zero_le (d * t)]

theorem dvd_sub_sub {d x y : ℕ} (h : d ∣ y - x) : d ∣ y - x - d :=
  Nat.dvd_sub h (dvd_refl d)

/-- Pushing a bead one step down its runner removes exactly one bead–gap pair (here: at least
all but one survive). -/
theorem card_beadGaps_le_push {d : ℕ} (hd : 0 < d) {B : Finset ℕ} {b : ℕ} (hb : b ∈ B)
    (hbd : d ≤ b) (hgap : b - d ∉ B) :
    (beadGaps d B).card ≤ (beadGaps d (insert (b - d) (B.erase b))).card + 1 := by
  set B' := insert (b - d) (B.erase b) with hB'
  have memB' : ∀ y, y ∈ B' ↔ y = b - d ∨ (y ≠ b ∧ y ∈ B) := by
    intro y; simp [hB', mem_insert, mem_erase]
  let φ : ℕ × ℕ → ℕ × ℕ := fun p =>
    if p.1 = b then (b - d, p.2) else if p.2 = b - d then (p.1, b) else p
  have hmaps : ∀ p ∈ (beadGaps d B).erase (b, b - d), φ p ∈ beadGaps d B' := by
    rintro ⟨y, x⟩ hp
    rw [mem_erase, mem_beadGaps] at hp
    obtain ⟨hne, hy, hxy, hx, hdv⟩ := hp
    simp only at hy hxy hx hdv
    simp only [φ]
    by_cases h1 : y = b
    · subst h1
      have hx' : x ≠ y - d := fun h => hne (by rw [h])
      rw [if_pos rfl, mem_beadGaps]
      rcases dvd_sub_cases hdv hxy with h | h
      · exact absurd (by omega) hx'
      · refine ⟨(memB' _).2 (Or.inl rfl), by omega, fun h' => ?_, ?_⟩
        · rcases (memB' x).1 h' with h'' | ⟨-, h''⟩
          · exact hx' h''
          · exact hx h''
        · have : y - d - x = y - x - d := by omega
          rw [this]; exact dvd_sub_sub hdv
    · rw [if_neg h1]
      by_cases h2 : x = b - d
      · subst h2
        rw [if_pos rfl, mem_beadGaps]
        have hlt : b < y := by
          rcases dvd_sub_cases hdv hxy with h | h
          · omega
          · omega
        refine ⟨(memB' _).2 (Or.inr ⟨h1, hy⟩), hlt, fun h' => ?_, ?_⟩
        · rcases (memB' b).1 h' with h'' | ⟨h'', -⟩
          · omega
          · exact h'' rfl
        · have : y - b = y - (b - d) - d := by omega
          rw [this]; exact dvd_sub_sub hdv
      · rw [if_neg h2, mem_beadGaps]
        refine ⟨(memB' _).2 (Or.inr ⟨h1, hy⟩), hxy, fun h' => ?_, hdv⟩
        rcases (memB' x).1 h' with h'' | ⟨-, h''⟩
        · exact h2 h''
        · exact hx h''
  have hinj : Set.InjOn φ ((beadGaps d B).erase (b, b - d)) := by
    rintro ⟨y, x⟩ hp ⟨y', x'⟩ hp' heq
    simp only [mem_coe, mem_erase, mem_beadGaps] at hp hp'
    simp only [φ] at heq
    obtain ⟨-, hy, -, hx, -⟩ := hp
    obtain ⟨-, hy', -, hx', -⟩ := hp'
    have hbB : b - d ≠ y := fun h => hgap (h ▸ hy)
    have hbB' : b - d ≠ y' := fun h => hgap (h ▸ hy')
    have hxb : x ≠ b := fun h => hx (h ▸ hb)
    have hxb' : x' ≠ b := fun h => hx' (h ▸ hb)
    split_ifs at heq <;> simp only [Prod.mk.injEq] at heq <;>
      exact Prod.ext (by simp only; omega) (by simp only; omega)
  have h1 := card_le_card_of_injOn φ hmaps hinj
  have h2 := pred_card_le_card_erase (s := beadGaps d B) (a := (b, b - d))
  omega

/-- **Abacus bound.** For a finite set `B` of bead positions on a `d`-abacus,
`d · #(bead–gap pairs) + C(|B|, 2) ≤ ∑ B`. (Push beads down their runners: each push lowers the
sum by `d` and the pair count by at most one; a fully pushed abacus has no pairs.) -/
theorem bead_bound {d : ℕ} (hd : 0 < d) (B : Finset ℕ) :
    d * (beadGaps d B).card + B.card.choose 2 ≤ ∑ b ∈ B, b := by
  induction h : ∑ b ∈ B, b using Nat.strong_induction_on generalizing B with
  | _ S ih =>
    by_cases hex : ∃ b ∈ B, d ≤ b ∧ b - d ∉ B
    · obtain ⟨b, hb, hbd, hgap⟩ := hex
      set B' := insert (b - d) (B.erase b)
      have hnot : b - d ∉ B.erase b := fun h' => hgap (mem_of_mem_erase h')
      have hsum : ∑ x ∈ B', x + d = ∑ x ∈ B, x := by
        rw [sum_insert hnot, ← sum_erase_add _ _ hb]; omega
      have hcard : B'.card = B.card := by
        rw [card_insert_of_notMem hnot, card_erase_of_mem hb]
        have := card_pos.2 ⟨b, hb⟩; omega
      have hih := ih (∑ x ∈ B', x) (by omega) B' rfl
      have hle : (beadGaps d B).card ≤ (beadGaps d B').card + 1 :=
        card_beadGaps_le_push hd hb hbd hgap
      have := Nat.mul_le_mul_left d hle
      rw [mul_add, mul_one] at this
      rw [hcard] at hih
      rw [← h, ← hsum]
      omega
    · push_neg at hex
      have hempty : beadGaps d B = ∅ := by
        rw [eq_empty_iff_forall_notMem]
        rintro ⟨y, x⟩ hp
        rw [mem_beadGaps] at hp
        obtain ⟨hy, hxy, hx, ⟨T, hT⟩⟩ := hp
        simp only at hy hxy hx hT
        have key : ∀ t, d * t ≤ y - x → y - d * t ∈ B := by
          intro t
          induction t with
          | zero => intro _; simpa using hy
          | succ t iht =>
            intro ht
            have h1 := iht (by nlinarith)
            have h2 := hex _ h1 (by rw [mul_add, mul_one] at ht; omega)
            have : y - d * t - d = y - d * (t + 1) := by rw [mul_add, mul_one]; omega
            rwa [this] at h2
        have := key T (by rw [hT])
        rw [← hT, show y - (y - x) = x by omega] at this
        exact hx this
      rw [hempty, card_empty, mul_zero, zero_add, ← h]
      exact choose_two_le_sum B

end QOU.Mass.StaircaseMinimisers


namespace QOU.Mass.StaircaseMinimisers

open Finset

section Rows

variable {s : Finset (ℕ × ℕ)}

/-- Length of row `i`. -/
def rowLen (s : Finset (ℕ × ℕ)) (i : ℕ) : ℕ := (s.filter (fun c => c.1 = i)).card

/-- Length of column `j`. -/
def colLen (s : Finset (ℕ × ℕ)) (j : ℕ) : ℕ := (s.filter (fun c => c.2 = j)).card

/-- A finite down-closed set of naturals is `range` of its size. -/
theorem mem_iff_lt_card_of_downClosed {T : Finset ℕ} (hT : ∀ a b, b ≤ a → a ∈ T → b ∈ T) (t : ℕ) :
    t ∈ T ↔ t < T.card := by
  constructor
  · intro ht
    have : range (t + 1) ⊆ T := fun x hx => hT t x (by simp at hx; omega) ht
    have := card_le_card this
    simp at this; omega
  · intro ht
    by_contra hn
    have : T ⊆ range t := by
      intro x hx
      rw [mem_range]
      by_contra hx'
      exact hn (hT x t (by omega) hx)
    have := card_le_card this
    simp at this; omega

theorem mem_iff_lt_rowLen (hs : IsLowerSet (s : Set (ℕ × ℕ))) (i t : ℕ) :
    (i, t) ∈ s ↔ t < rowLen s i := by
  have hcard : rowLen s i = ((s.filter (fun c => c.1 = i)).image Prod.snd).card := by
    rw [rowLen, card_image_of_injOn]
    intro a ha b hb h
    simp only [coe_filter, Set.mem_setOf_eq] at ha hb
    exact Prod.ext (ha.2.trans hb.2.symm) h
  rw [hcard, ← mem_iff_lt_card_of_downClosed]
  · simp
  · intro a b hab ha
    simp only [mem_image, mem_filter] at ha ⊢
    obtain ⟨c, ⟨hc, rfl⟩, rfl⟩ := ha
    exact ⟨(c.1, b), ⟨hs (show ((c.1, b) : ℕ × ℕ) ≤ c from Prod.le_def.2 ⟨le_rfl, hab⟩) hc, rfl⟩, rfl⟩

theorem mem_iff_lt_colLen (hs : IsLowerSet (s : Set (ℕ × ℕ))) (t j : ℕ) :
    (t, j) ∈ s ↔ t < colLen s j := by
  have hcard : colLen s j = ((s.filter (fun c => c.2 = j)).image Prod.fst).card := by
    rw [colLen, card_image_of_injOn]
    intro a ha b hb h
    simp only [coe_filter, Set.mem_setOf_eq] at ha hb
    exact Prod.ext h (ha.2.trans hb.2.symm)
  rw [hcard, ← mem_iff_lt_card_of_downClosed]
  · simp
  · intro a b hab ha
    simp only [mem_image, mem_filter] at ha ⊢
    obtain ⟨c, ⟨hc, rfl⟩, rfl⟩ := ha
    exact ⟨(b, c.2), ⟨hs (show ((b, c.2) : ℕ × ℕ) ≤ c from Prod.le_def.2 ⟨hab, le_rfl⟩) hc, rfl⟩, rfl⟩

theorem arm_eq (hs : IsLowerSet (s : Set (ℕ × ℕ))) {i j : ℕ} :
    arm s (i, j) = rowLen s i - 1 - j := by
  have : s.filter (fun d => d.1 = (i, j).1 ∧ (i, j).2 < d.2) = (Ioo j (rowLen s i)).image (i, ·) := by
    ext ⟨a, b⟩
    simp only [mem_filter, mem_image, mem_Ioo, Prod.mk.injEq]
    constructor
    · rintro ⟨h, rfl, hb⟩; exact ⟨b, ⟨hb, (mem_iff_lt_rowLen hs _ _).1 h⟩, rfl, rfl⟩
    · rintro ⟨t, ⟨h1, h2⟩, rfl, rfl⟩; exact ⟨(mem_iff_lt_rowLen hs _ _).2 h2, rfl, h1⟩
  rw [arm, this, card_image_of_injective _ (fun a b h => by simpa using h), Nat.card_Ioo]; omega

theorem leg_eq (hs : IsLowerSet (s : Set (ℕ × ℕ))) {i j : ℕ} :
    leg s (i, j) = colLen s j - 1 - i := by
  have : s.filter (fun d => d.2 = (i, j).2 ∧ (i, j).1 < d.1) = (Ioo i (colLen s j)).image (·, j) := by
    ext ⟨a, b⟩
    simp only [mem_filter, mem_image, mem_Ioo, Prod.mk.injEq]
    constructor
    · rintro ⟨h, rfl, ha⟩; exact ⟨a, ⟨ha, (mem_iff_lt_colLen hs _ _).1 h⟩, rfl, rfl⟩
    · rintro ⟨t, ⟨h1, h2⟩, rfl, rfl⟩; exact ⟨(mem_iff_lt_colLen hs _ _).2 h2, rfl, h1⟩
  rw [leg, this, card_image_of_injective _ (fun a b h => by simpa using h), Nat.card_Ioo]; omega

theorem rowLen_anti (hs : IsLowerSet (s : Set (ℕ × ℕ))) {i i' : ℕ} (h : i ≤ i') :
    rowLen s i' ≤ rowLen s i := by
  by_contra hc
  push_neg at hc
  have h1 := (mem_iff_lt_rowLen hs i' (rowLen s i)).2 hc
  have h2 := hs (Prod.le_def.2 ⟨h, le_rfl⟩ : ((i, rowLen s i) : ℕ × ℕ) ≤ (i', rowLen s i)) h1
  exact lt_irrefl _ ((mem_iff_lt_rowLen hs i _).1 h2)

theorem colLen_anti (hs : IsLowerSet (s : Set (ℕ × ℕ))) {j j' : ℕ} (h : j ≤ j') :
    colLen s j' ≤ colLen s j := by
  by_contra hc
  push_neg at hc
  have h1 := (mem_iff_lt_colLen hs (colLen s j) j').2 hc
  have h2 := hs (Prod.le_def.2 ⟨le_rfl, h⟩ : ((colLen s j, j) : ℕ × ℕ) ≤ (colLen s j, j')) h1
  exact lt_irrefl _ ((mem_iff_lt_colLen hs _ j).1 h2)

theorem colLen_le_card (j : ℕ) : colLen s j ≤ s.card := card_filter_le _ _

end Rows

section Beta

variable {s : Finset (ℕ × ℕ)}

/-- Beta numbers of `s` with `L = s.card` rows: `β i = λ_i + L - 1 - i`. -/
def beta (s : Finset (ℕ × ℕ)) (i : ℕ) : ℕ := rowLen s i + s.card - 1 - i

theorem fst_lt_card (hs : IsLowerSet (s : Set (ℕ × ℕ))) {c : ℕ × ℕ} (hc : c ∈ s) :
    c.1 < s.card :=
  lt_of_lt_of_le ((mem_iff_lt_colLen hs c.1 c.2).1 hc) (colLen_le_card _)

theorem beta_strictAnti (hs : IsLowerSet (s : Set (ℕ × ℕ))) {i i' : ℕ} (h : i < i')
    (hi' : i' < s.card) : beta s i' < beta s i := by
  have := rowLen_anti hs h.le
  unfold beta; omega

theorem beta_injOn (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    Set.InjOn (beta s) (range s.card : Set ℕ) := by
  intro i hi i' hi' h
  simp only [coe_range, Set.mem_Iio] at hi hi'
  rcases lt_trichotomy i i' with hlt | heq | hgt
  · exact absurd h (beta_strictAnti hs hlt hi').ne'
  · exact heq
  · exact absurd h (beta_strictAnti hs hgt hi).ne

theorem sum_rowLen (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    ∑ i ∈ range s.card, rowLen s i = s.card := by
  exact (card_eq_sum_card_fiberwise (f := Prod.fst) (t := range s.card)
    (fun c hc => mem_range.2 (fst_lt_card hs hc))).symm

theorem sum_range_sub (L : ℕ) : ∑ i ∈ range L, (L - 1 - i) = L.choose 2 := by
  rw [Finset.sum_range_reflect (fun i => i) L, Finset.sum_range_id, Nat.choose_two_right]

theorem sum_beta (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    ∑ b ∈ (range s.card).image (beta s), b = s.card + s.card.choose 2 := by
  rw [sum_image (beta_injOn hs)]
  calc ∑ i ∈ range s.card, beta s i
      = ∑ i ∈ range s.card, (rowLen s i + (s.card - 1 - i)) :=
        sum_congr rfl (fun i hi => by rw [mem_range] at hi; unfold beta; omega)
    _ = _ := by rw [sum_add_distrib, sum_rowLen hs, sum_range_sub]

/-- The gap `β_i - h(i,j) = L + j - colLen j` is not a beta number. -/
theorem gap_not_mem (hs : IsLowerSet (s : Set (ℕ × ℕ))) (j : ℕ) :
    s.card + j - colLen s j ∉ (range s.card).image (beta s) := by
  rw [mem_image]
  rintro ⟨k, hk, hb⟩
  rw [mem_range] at hk
  have hcl := colLen_le_card (s := s) j
  unfold beta at hb
  by_cases hkj : k < colLen s j
  · have := (mem_iff_lt_rowLen hs k j).1 ((mem_iff_lt_colLen hs k j).2 hkj)
    omega
  · have : ¬ j < rowLen s k := fun h =>
      hkj ((mem_iff_lt_colLen hs k j).1 ((mem_iff_lt_rowLen hs k j).2 h))
    omega

/-- **Hook count bound.** At most `n / d` cells of a Young diagram with `n` cells have hook
length divisible by `d` (Stanley EC2 §7.21, via beta-sets and beads). -/
theorem mul_card_hook_dvd_le (hs : IsLowerSet (s : Set (ℕ × ℕ))) {d : ℕ} (hd : 0 < d) :
    d * (s.filter (fun c => d ∣ hook s c)).card ≤ s.card := by
  set B := (range s.card).image (beta s)
  have hB := bead_bound hd B
  rw [sum_beta hs, card_image_of_injOn (beta_injOn hs), card_range] at hB
  have key : (s.filter (fun c => d ∣ hook s c)).card ≤ (beadGaps d B).card := by
    refine card_le_card_of_injOn (fun c => (beta s c.1, beta s c.1 - hook s c)) ?_ ?_
    · intro c hc
      rw [coe_filter] at hc
      obtain ⟨hcs, hdv⟩ := hc
      obtain ⟨i, j⟩ := c
      have hj := (mem_iff_lt_rowLen hs i j).1 hcs
      have hi := (mem_iff_lt_colLen hs i j).1 hcs
      have hcl := colLen_le_card (s := s) j
      have ha := arm_eq hs (i := i) (j := j)
      have hl := leg_eq hs (i := i) (j := j)
      have hiL : i < s.card := by omega
      have hx : beta s i - hook s (i, j) = s.card + j - colLen s j := by
        unfold beta hook; omega
      have hle : hook s (i, j) ≤ beta s i := by unfold beta hook; omega
      have hpos : 1 ≤ hook s (i, j) := by unfold hook; omega
      rw [mem_coe, mem_beadGaps]; dsimp only
      refine ⟨mem_image.2 ⟨i, mem_range.2 hiL, rfl⟩, by omega, ?_, ?_⟩
      · rw [hx]; exact gap_not_mem hs j
      · rwa [Nat.sub_sub_self hle]
    · intro c hc c' hc' h
      rw [coe_filter] at hc hc'
      obtain ⟨i, j⟩ := c
      obtain ⟨i', j'⟩ := c'
      simp only [Prod.mk.injEq] at h
      obtain ⟨h1, h2⟩ := h
      have hiL := fst_lt_card hs hc.1
      have hiL' := fst_lt_card hs hc'.1
      have hii : i = i' := beta_injOn hs (by simpa using hiL) (by simpa using hiL') h1
      subst hii
      have hx : ∀ t, (i, t) ∈ s → beta s i - hook s (i, t) = s.card + t - colLen s t := by
        intro t ht
        have := (mem_iff_lt_rowLen hs i t).1 ht
        have := (mem_iff_lt_colLen hs i t).1 ht
        have := colLen_le_card (s := s) t
        have := arm_eq hs (i := i) (j := t)
        have := leg_eq hs (i := i) (j := t)
        unfold beta hook; omega
      rw [hx j hc.1, hx j' hc'.1] at h2
      have hcj := colLen_le_card (s := s) j
      have hcj' := colLen_le_card (s := s) j'
      rcases lt_trichotomy j j' with hlt | heq | hgt
      · have := colLen_anti hs hlt.le; omega
      · rw [heq]
      · have := colLen_anti hs hgt.le; omega
  have := Nat.mul_le_mul_left d key
  omega

/-- If `d m ≤ n` then at least `m` of `1, …, n` are multiples of `d`. -/
theorem le_card_multiples {d m n : ℕ} (hd : 0 < d) (h : d * m ≤ n) :
    m ≤ ((range n).filter (fun k => d ∣ k + 1)).card := by
  have : (range m).image (fun t => d * (t + 1) - 1) ⊆ (range n).filter (fun k => d ∣ k + 1) := by
    intro k hk
    obtain ⟨t, ht, rfl⟩ := mem_image.1 hk
    rw [mem_range] at ht
    have h1 : d * (t + 1) ≤ d * m := Nat.mul_le_mul_left d ht
    have h2 : 1 ≤ d * (t + 1) := Nat.one_le_iff_ne_zero.2 (by positivity)
    rw [mem_filter, mem_range, Nat.sub_add_cancel h2]
    exact ⟨by omega, dvd_mul_right _ _⟩
  have hinj : Set.InjOn (fun t => d * (t + 1) - 1) (range m : Set ℕ) := by
    intro a _ b _ hab
    have ha : 1 ≤ d * (a + 1) := Nat.one_le_iff_ne_zero.2 (by positivity)
    have hb : 1 ≤ d * (b + 1) := Nat.one_le_iff_ne_zero.2 (by positivity)
    have : d * (a + 1) = d * (b + 1) := by simp only at hab; omega
    have := Nat.eq_of_mul_eq_mul_left hd this
    omega
  calc m = ((range m).image (fun t => d * (t + 1) - 1)).card := by
        rw [card_image_of_injOn hinj, card_range]
    _ ≤ _ := card_le_card this

/-- **q-hook divisibility.** For a Young diagram `s`, `∏_{c ∈ s} [h(c)]_q` divides `[n]_q!`
in `ℤ[q]` (Stanley EC2 §7.21). -/
theorem hookProd_dvd_qfact (hs : IsLowerSet (s : Set (ℕ × ℕ))) : hookProd s ∣ qfact s.card :=
  hookProd_dvd_qfact_of_count s (fun d hd =>
    le_card_multiples (by omega) (mul_card_hook_dvd_le hs (by omega)))

end Beta

end QOU.Mass.StaircaseMinimisers

namespace QOU.Mass.StaircaseMinimisers

open Finset Polynomial

/-- The `q`-hook quotient `[n]! / ∏_{c} [h(c)]`. -/
noncomputable def qHookQuot (s : Finset (ℕ × ℕ)) : ℤ[X] := by
  classical
  exact if hs : IsLowerSet (s : Set (ℕ × ℕ)) then (hookProd_dvd_qfact hs).choose else 0

theorem qfact_eq_qHookQuot_mul {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    qfact s.card = qHookQuot s * hookProd s := by
  classical
  rw [qHookQuot, dif_pos hs, mul_comm]
  exact (hookProd_dvd_qfact hs).choose_spec

theorem qfact_eq_qHookQuot_mul_of_mem {n : ℕ} {s : Finset (ℕ × ℕ)} (hs : s ∈ shapes n) :
    qfact n = qHookQuot s * hookProd s := by
  obtain ⟨-, hcard, hlow⟩ := mem_shapes.1 hs
  rw [← hcard]; exact qfact_eq_qHookQuot_mul hlow

/-- **Leading coefficient of `∑_s [n]!/H(s)`** is `C(m+1, r)`, `n = T_m + r`. -/
theorem coeff_sum_qHook {m r : ℕ} (hr1 : 1 ≤ r) (hr : r ≤ m + 1) :
    (∑ s ∈ shapes ((stair m).card + r), qHookQuot s).coeff
        (((stair m).card + r) * ((stair m).card + r - 1) / 2 - (N (stair m) + r * m)) =
      ((m + 1).choose r : ℤ) :=
  coeff_sum_qHook_of_eq hr1 hr qHookQuot (fun _ hs => qfact_eq_qHookQuot_mul_of_mem hs)

/-- **`a₁` as a coefficient**, with no divisibility hypothesis. -/
theorem coeff_sum_sym_qHook (k r : ℕ) (hr : 1 ≤ r) (hr' : r ≤ k + 2) :
    (∑ s ∈ shapes ((stair (k + 1)).card + r), X ^ N s * expand ℤ 2 (qHookQuot s)).coeff
        (2 * (((stair (k + 1)).card + r) * ((stair (k + 1)).card + r - 1) / 2) -
          (N (stair (k + 1)) + r * (k + 1)) - 1) =
      ((2 * (if 2 ≤ r then (k + 1).choose (r - 2) else 0) +
        (k + 1) * (if 3 ≤ r then k.choose (r - 3) else 0) + (k + 1) * k.choose (r + 1) : ℕ) : ℤ) :=
  coeff_sum_sym_qHook_of_eq k r hr hr' qHookQuot (fun _ hs => qfact_eq_qHookQuot_mul_of_mem hs)

/-- **`a₂` as a coefficient**, with no divisibility hypothesis. -/
theorem coeff_sum_sym_qHook_two_uncond (k r : ℕ) (hr : 1 ≤ r) (hr' : r ≤ k + 2) (h3 : 2 ≤ k + r) :
    (∑ s ∈ shapes ((stair (k + 1)).card + r), X ^ N s * expand ℤ 2 (qHookQuot s)).coeff
        (2 * (((stair (k + 1)).card + r) * ((stair (k + 1)).card + r - 1) / 2) -
          (N (stair (k + 1)) + r * (k + 1)) - 2) =
      ((r * (k + 2).choose r + (k + 1) * k.choose r : ℕ) : ℤ) - ((k + 2).choose r : ℤ) +
      (((3 * g20 k r 2 + 3 * k * g20 k r 3 + k.choose 2 * g20 k r 4) +
        (2 * k * h11 k r 1 + 2 * k.choose 2 * h11 k r 2) +
        (k * (k - 1).choose (r + 2) + k.choose 2 * (k - 2).choose (r + 2)) : ℕ) : ℤ) :=
  coeff_sum_sym_qHook_two k r hr hr' h3 qHookQuot (fun _ hs => qfact_eq_qHookQuot_mul_of_mem hs)

end QOU.Mass.StaircaseMinimisers
