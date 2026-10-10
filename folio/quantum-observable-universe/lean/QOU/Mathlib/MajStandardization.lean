import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Data.Fintype.Card
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Order.Interval.Finset.Fin

/-!
# QOU.Mathlib.MajStandardization — Stanley's standardization bijection

First half of the `maj` / fake-degree formula
`Σ_{S ∈ SYT(λ)} q^{maj S} = q^{n(λ)} [n]_q! / ∏_{x ∈ λ} [h(x)]_q` (bean `qou-q3q2`).

A **reverse semistandard tableau** of shape `μ` is a filling by naturals with rows weakly
decreasing and columns strictly decreasing. This file proves, sorry-free:

* `stdEquivSigma μ : (Σ S : SYTe μ, DecSeq n) ≃ RSSYT μ` — reverse semistandard tableaux are in
  bijection with pairs (standard tableau `S`, weakly decreasing sequence `b₀ ≥ ⋯ ≥ b_{n−1} ≥ 0`);
* `sum_stdEquivSigma` — under it `|T| = maj S + |b|`.

As generating functions this is
`Σ_{T ∈ RSSYT(λ)} q^{|T|} = (Σ_{S ∈ SYT(λ)} q^{maj S}) / ∏_{i=1}^{n} (1 − q^i)`,
since weakly decreasing length-`n` sequences are partitions with at most `n` parts.

## Construction

`Φ(S, b)` writes `b_k + D_k` in the cell carrying entry `k`, where `D_k` is the number of descents
`j ≥ k` of `S` (a descent: entry `j + 1` lies in a strictly lower row than `j`). Rows decrease
because `b` and `D` do; columns decrease strictly because a cell strictly below another forces a
descent in between (`run_no_des`: a descent-free run of entries moves weakly up and strictly
right). The inverse standardizes `T`: order cells by value, larger first, ties left to right
(`stdSYT`), and subtract `D`. Strictness at descents (`aN_step`) is where the column-strict
condition is used.

Orientation: the *reverse* convention makes the weight shift exactly `maj S = Σ_{descents} j`
(1-indexed); the ordinary semistandard orientation gives `Σ_{descents} (n − j)` instead.

## What is NOT proved here

The second half — `Σ_{T ∈ RSSYT(λ)} q^{|T|} = q^{n(λ)} / ∏_x (1 − q^{h(x)})` — is not proved, so
the `maj` formula itself, and the nonnegativity of `[n]_q!/c_λ` it would give, stay open
(bean `qou-q3q2`). `SYTe` is an ordering-based presentation of standard tableaux; it is not yet
bridged to `QOU.Mathlib.StandardYoungTableau`.

Pure finite combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.MajStandardization

open Finset YoungDiagram

/-- The cells of `μ`, as a finite type. -/
abbrev Cell (μ : YoungDiagram) := {x : ℕ × ℕ // x ∈ μ.cells}

/-- A **standard Young tableau** presented as an ordering of the cells: `e c` is the
(0-indexed) entry of cell `c`; entries increase along rows and down columns. -/
structure SYTe (μ : YoungDiagram) where
  e : Cell μ ≃ Fin μ.cells.card
  row_lt : ∀ c c' : Cell μ, c.1.1 = c'.1.1 → c.1.2 < c'.1.2 → e c < e c'
  col_lt : ∀ c c' : Cell μ, c.1.2 = c'.1.2 → c.1.1 < c'.1.1 → e c < e c'

namespace SYTe

variable {μ : YoungDiagram} (S : SYTe μ)

/-- Row of the cell carrying entry `k` (junk `0` for `k ≥ n`). -/
def rowN (k : ℕ) : ℕ := if h : k < μ.cells.card then (S.e.symm ⟨k, h⟩).1.1 else 0

/-- Column of the cell carrying entry `k` (junk `0` for `k ≥ n`). -/
def colN (k : ℕ) : ℕ := if h : k < μ.cells.card then (S.e.symm ⟨k, h⟩).1.2 else 0

/-- `k` is a **descent** (0-indexed): entry `k + 1` sits in a strictly lower row than `k`. -/
def IsDes (k : ℕ) : Prop := k + 1 < μ.cells.card ∧ S.rowN k < S.rowN (k + 1)

instance (k : ℕ) : Decidable (S.IsDes k) := by unfold IsDes; infer_instance

/-- The **major index** `maj S = Σ_{descents k} (k + 1)` (1-indexed descents). -/
def maj : ℕ := ∑ k ∈ (range μ.cells.card).filter S.IsDes, (k + 1)

/-- `D k = #{descents j ≥ k}`: the strictness budget below entry `k`. -/
def D (k : ℕ) : ℕ := ((range μ.cells.card).filter (fun j => k ≤ j ∧ S.IsDes j)).card

theorem rowN_of_lt {k : ℕ} (h : k < μ.cells.card) : S.rowN k = (S.e.symm ⟨k, h⟩).1.1 := dif_pos h
theorem colN_of_lt {k : ℕ} (h : k < μ.cells.card) : S.colN k = (S.e.symm ⟨k, h⟩).1.2 := dif_pos h

/-- **No descent at `k` ⟹ entry `k + 1` is strictly to the right of entry `k`.** -/
theorem colN_lt_of_not_des {k : ℕ} (hk : k + 1 < μ.cells.card) (hd : ¬ S.IsDes k) :
    S.colN k < S.colN (k + 1) := by
  have hk0 : k < μ.cells.card := by omega
  have hrow : S.rowN (k + 1) ≤ S.rowN k := by
    unfold IsDes at hd; push_neg at hd; exact hd hk
  rw [rowN_of_lt S hk0, rowN_of_lt S hk] at hrow
  rw [colN_of_lt S hk0, colN_of_lt S hk]
  set c := S.e.symm ⟨k, hk0⟩ with hc
  set c' := S.e.symm ⟨k + 1, hk⟩ with hc'
  have ec : S.e c = ⟨k, hk0⟩ := by simp [hc]
  have ec' : S.e c' = ⟨k + 1, hk⟩ := by simp [hc']
  by_contra hcol
  push_neg at hcol
  rcases lt_or_eq_of_le hrow with hr | hr
  · -- `x = (row c', col c)` lies directly above `c`
    have hx : (c'.1.1, c.1.2) ∈ μ.cells := by
      rw [mem_cells]
      exact μ.up_left_mem hr.le le_rfl ((mem_cells _).mp c.2)
    let x : Cell μ := ⟨(c'.1.1, c.1.2), hx⟩
    have h1 : S.e x < S.e c := S.col_lt x c rfl hr
    rw [ec] at h1
    rcases lt_or_eq_of_le hcol with hl | hl
    · have h2 : S.e c' < S.e x := S.row_lt c' x rfl hl
      rw [ec'] at h2
      have := Fin.lt_def.mp h1; have := Fin.lt_def.mp h2; simp at *; omega
    · have hxc : x = c' := Subtype.ext (Prod.ext rfl hl.symm)
      rw [hxc, ec'] at h1
      exact absurd h1 (by simp [Fin.lt_def])
  · rcases lt_or_eq_of_le hcol with hl | hl
    · have h2 : S.e c' < S.e c := S.row_lt c' c hr hl
      rw [ec, ec'] at h2
      exact absurd h2 (by simp [Fin.lt_def])
    · have : c' = c := Subtype.ext (Prod.ext hr hl)
      have h3 := congrArg S.e this
      rw [ec, ec'] at h3
      have := congrArg Fin.val h3; simp at this

/-- **A descent-free run moves weakly up and strictly right.** -/
theorem run_no_des {k l : ℕ} (hkl : k ≤ l) (hl : l < μ.cells.card)
    (hnd : ∀ j, k ≤ j → j < l → ¬ S.IsDes j) :
    S.rowN l ≤ S.rowN k ∧ (k < l → S.colN k < S.colN l) := by
  induction l, hkl using Nat.le_induction with
  | base => exact ⟨le_rfl, fun h => absurd h (lt_irrefl _)⟩
  | succ l hkl ih =>
    have ih' := ih (by omega) (fun j h1 h2 => hnd j h1 (by omega))
    have hd := hnd l hkl (by omega)
    have hrow : S.rowN (l + 1) ≤ S.rowN l := by
      unfold IsDes at hd; push_neg at hd; exact hd hl
    have hcol := S.colN_lt_of_not_des hl hd
    refine ⟨hrow.trans ih'.1, fun _ => ?_⟩
    rcases Nat.lt_or_ge k l with h | h
    · exact (ih'.2 h).trans hcol
    · have : k = l := by omega
      subst this; exact hcol

theorem D_le_of_le {k l : ℕ} (h : k ≤ l) : S.D l ≤ S.D k :=
  card_le_card fun j hj => by
    simp only [mem_filter, mem_range] at hj ⊢
    exact ⟨hj.1, by omega, hj.2.2⟩

/-- A descent in `[k, l)` makes the strictness budget drop from `k` to `l`. -/
theorem D_lt_of_des {k j l : ℕ} (hkj : k ≤ j) (hjl : j < l) (hj : S.IsDes j) : S.D l < S.D k := by
  apply card_lt_card
  rw [ssubset_iff_of_subset]
  · refine ⟨j, ?_, ?_⟩
    · simp only [mem_filter, mem_range]; exact ⟨by have := hj.1; omega, hkj, hj⟩
    · simp only [mem_filter, mem_range, not_and]; intro _ h; omega
  · intro i hi
    simp only [mem_filter, mem_range] at hi ⊢
    exact ⟨hi.1, by omega, hi.2.2⟩

/-- If entry `l > k` sits strictly below entry `k`, the strictness budget drops. -/
theorem D_lt_of_rowN_lt {k l : ℕ} (hkl : k < l) (hl : l < μ.cells.card)
    (hrow : S.rowN k < S.rowN l) : S.D l < S.D k := by
  have : ∃ j, k ≤ j ∧ j < l ∧ S.IsDes j := by
    by_contra hcon
    push_neg at hcon
    have := (S.run_no_des hkl.le hl (fun j h1 h2 => hcon j h1 h2)).1
    omega
  obtain ⟨j, hj1, hj2, hj⟩ := this
  exact S.D_lt_of_des hj1 hj2 hj

/-- Equal budgets at `k < l` force a descent-free run, hence entry `l` strictly right of `k`. -/
theorem colN_lt_of_D_eq {k l : ℕ} (hkl : k < l) (hl : l < μ.cells.card) (hD : S.D l = S.D k) :
    S.colN k < S.colN l :=
  (S.run_no_des hkl.le hl fun _ h1 h2 hj => absurd hD (S.D_lt_of_des h1 h2 hj).ne).2 hkl

/-- `D k = D (k+1) + [k is a descent]`. -/
theorem D_succ (k : ℕ) : S.D k = S.D (k + 1) + if S.IsDes k then 1 else 0 := by
  unfold D
  have : (range μ.cells.card).filter (fun j => k ≤ j ∧ S.IsDes j) =
      (range μ.cells.card).filter (fun j => k + 1 ≤ j ∧ S.IsDes j) ∪
        (range μ.cells.card).filter (fun j => j = k ∧ S.IsDes j) := by
    ext j; simp only [mem_filter, mem_union, mem_range]
    by_cases hj : S.IsDes j <;> simp only [hj, and_true, and_false, or_false]; omega
  rw [this, card_union_of_disjoint]
  · congr 1
    split_ifs with h
    · rw [card_eq_one]; refine ⟨k, ?_⟩
      ext j; simp only [mem_filter, mem_range, mem_singleton]
      constructor
      · rintro ⟨_, rfl, _⟩; rfl
      · rintro rfl; exact ⟨by have := h.1; omega, rfl, h⟩
    · rw [card_eq_zero, filter_eq_empty_iff]; rintro j _ ⟨rfl, hj⟩; exact h hj
  · rw [disjoint_left]; intro j h1 h2
    simp only [mem_filter] at h1 h2; omega

/-- `Σ_{k<n} D k = maj S`. -/
theorem sum_D : ∑ k ∈ range μ.cells.card, S.D k = S.maj := by
  unfold D maj
  simp_rw [card_filter]
  rw [Finset.sum_comm, sum_filter]
  refine sum_congr rfl fun j hj => ?_
  by_cases hd : S.IsDes j
  · simp only [hd, and_true, if_true]
    rw [← card_filter]
    have : (range μ.cells.card).filter (fun k => k ≤ j) = range (j + 1) := by
      ext k; simp only [mem_filter, mem_range]; have := mem_range.mp hj; omega
    rw [this, card_range]
  · simp [hd]

theorem ext' {S S' : SYTe μ} (h : S.e = S'.e) : S = S' := by
  cases S; cases S'; cases h; rfl

end SYTe

/-! ## Reverse semistandard tableaux and the standardization bijection -/

/-- A **reverse semistandard tableau**: rows weakly decrease, columns strictly decrease. -/
def IsRSSYT {μ : YoungDiagram} (T : Cell μ → ℕ) : Prop :=
  (∀ c c' : Cell μ, c.1.1 = c'.1.1 → c.1.2 < c'.1.2 → T c' ≤ T c) ∧
  (∀ c c' : Cell μ, c.1.2 = c'.1.2 → c.1.1 < c'.1.1 → T c' < T c)

/-- Reverse semistandard tableaux of shape `μ`. -/
def RSSYT (μ : YoungDiagram) := {T : Cell μ → ℕ // IsRSSYT T}

/-- Weakly decreasing sequences of naturals of length `n` (partitions with at most `n` parts). -/
def DecSeq (n : ℕ) := {b : Fin n → ℕ // Antitone b}

namespace SYTe

variable {μ : YoungDiagram} (S : SYTe μ)

/-- `Φ(S, b)`: put `b_k + D_k` in the cell carrying entry `k`. -/
def phiFun (b : Fin μ.cells.card → ℕ) (c : Cell μ) : ℕ := b (S.e c) + S.D (S.e c)

theorem rowN_e (c : Cell μ) : S.rowN (S.e c) = c.1.1 := by
  rw [rowN_of_lt S (S.e c).2]; simp

theorem colN_e (c : Cell μ) : S.colN (S.e c) = c.1.2 := by
  rw [colN_of_lt S (S.e c).2]; simp

theorem phiFun_isRSSYT {b : Fin μ.cells.card → ℕ} (hb : Antitone b) : IsRSSYT (S.phiFun b) := by
  constructor
  · intro c c' hr hc
    have h := S.row_lt c c' hr hc
    have h1 := hb h.le
    have h2 := S.D_le_of_le (Fin.le_def.mp h.le)
    unfold phiFun; omega
  · intro c c' hcol hr
    have h := S.col_lt c c' hcol hr
    have h1 := hb h.le
    have h2 := S.D_lt_of_rowN_lt (Fin.lt_def.mp h) (S.e c').2
      (by rw [rowN_e, rowN_e]; exact hr)
    unfold phiFun; omega

theorem sum_phiFun (b : Fin μ.cells.card → ℕ) :
    ∑ c, S.phiFun b c = S.maj + ∑ k, b k := by
  unfold phiFun
  rw [Equiv.sum_comp S.e (fun k => b k + S.D k), sum_add_distrib, add_comm (∑ k, b k),
    Fin.sum_univ_eq_sum_range (fun k => S.D k), sum_D]

end SYTe

section Standardize

variable {μ : YoungDiagram} (T : Cell μ → ℕ)

/-- `before c' c`: cell `c'` precedes `c` in the standardization order (larger value first,
ties broken left to right). -/
def Before (c' c : Cell μ) : Prop := T c < T c' ∨ (T c' = T c ∧ c'.1.2 < c.1.2)

instance (c' c : Cell μ) : Decidable (Before T c' c) := by unfold Before; infer_instance

/-- Rank of a cell in the standardization order. -/
def rank (c : Cell μ) : ℕ := (univ.filter (fun c' => Before T c' c)).card

variable {T}

theorem before_irrefl (c : Cell μ) : ¬ Before T c c := by
  unfold Before; omega

theorem before_trans {a b c : Cell μ} (h1 : Before T a b) (h2 : Before T b c) : Before T a c := by
  unfold Before at *; omega

theorem before_total (hT : IsRSSYT T) {c c' : Cell μ} (hne : c ≠ c') :
    Before T c c' ∨ Before T c' c := by
  unfold Before
  rcases lt_trichotomy (T c) (T c') with h | h | h
  · right; left; exact h
  · rcases lt_trichotomy c.1.2 c'.1.2 with hc | hc | hc
    · left; right; exact ⟨h, hc⟩
    · exfalso
      rcases lt_trichotomy c.1.1 c'.1.1 with hr | hr | hr
      · have := hT.2 c c' hc hr; omega
      · exact hne (Subtype.ext (Prod.ext hr hc))
      · have := hT.2 c' c hc.symm hr; omega
    · right; right; exact ⟨h.symm, hc⟩
  · left; left; exact h

theorem rank_lt_rank {c c' : Cell μ} (h : Before T c c') : rank T c < rank T c' := by
  apply card_lt_card
  rw [ssubset_iff_of_subset]
  · exact ⟨c, by simp [h], by simp [before_irrefl]⟩
  · intro d hd
    simp only [mem_filter, mem_univ, true_and] at hd ⊢
    exact before_trans hd h

theorem rank_lt_card (c : Cell μ) : rank T c < μ.cells.card := by
  have : rank T c < Fintype.card (Cell μ) := by
    apply card_lt_card
    rw [ssubset_iff_of_subset (subset_univ _)]
    exact ⟨c, mem_univ _, by simp [before_irrefl]⟩
  simpa using this

theorem rank_injective (hT : IsRSSYT T) : Function.Injective (rank T) := by
  intro c c' h
  by_contra hne
  rcases before_total hT hne with h1 | h1
  · exact absurd h (rank_lt_rank h1).ne
  · exact absurd h.symm (rank_lt_rank h1).ne

/-- The standardization equivalence `cells ≃ Fin n`. -/
noncomputable def stdEquiv (hT : IsRSSYT T) : Cell μ ≃ Fin μ.cells.card :=
  Equiv.ofBijective (fun c => ⟨rank T c, rank_lt_card c⟩) <| by
    rw [Fintype.bijective_iff_injective_and_card]
    refine ⟨fun c c' h => rank_injective hT (congrArg Fin.val h), by simp⟩

theorem stdEquiv_lt_iff (hT : IsRSSYT T) {c c' : Cell μ} :
    stdEquiv hT c < stdEquiv hT c' ↔ Before T c c' := by
  show rank T c < rank T c' ↔ _
  constructor
  · intro h
    have hne : c ≠ c' := fun he => by subst he; exact lt_irrefl _ h
    rcases before_total hT hne with h1 | h1
    · exact h1
    · exact absurd h (not_lt.mpr (rank_lt_rank h1).le)
  · exact rank_lt_rank

/-- The **standardization** of a reverse semistandard tableau: a standard Young tableau. -/
noncomputable def stdSYT (hT : IsRSSYT T) : SYTe μ where
  e := stdEquiv hT
  row_lt c c' hr hc := by
    rw [stdEquiv_lt_iff]
    have := hT.1 c c' hr hc
    unfold Before; omega
  col_lt c c' hc hr := by
    rw [stdEquiv_lt_iff]
    have := hT.2 c c' hc hr
    unfold Before; omega

end Standardize

namespace SYTe

variable {μ : YoungDiagram} (S : SYTe μ)

theorem D_eq_zero {k : ℕ} (hk : μ.cells.card ≤ k + 1) : S.D k = 0 := by
  rw [D, card_eq_zero, filter_eq_empty_iff]
  rintro j _ ⟨hkj, hj⟩
  have := hj.1; omega

end SYTe

section Inverse

variable {μ : YoungDiagram} {T : Cell μ → ℕ} (hT : IsRSSYT T)

/-- The value of `T` at the cell carrying standardized entry `k` (junk `0` past `n`). -/
noncomputable def aN (k : ℕ) : ℕ :=
  if h : k < μ.cells.card then T ((stdSYT hT).e.symm ⟨k, h⟩) else 0

theorem aN_step {k : ℕ} (hk : k + 1 < μ.cells.card) :
    aN hT (k + 1) + (if (stdSYT hT).IsDes k then 1 else 0) ≤ aN hT k := by
  have hk0 : k < μ.cells.card := by omega
  unfold aN
  rw [dif_pos hk, dif_pos hk0]
  set c := (stdSYT hT).e.symm ⟨k, hk0⟩ with hc
  set c' := (stdSYT hT).e.symm ⟨k + 1, hk⟩ with hc'
  have hlt : (stdSYT hT).e c < (stdSYT hT).e c' := by
    simp only [hc, hc', Equiv.apply_symm_apply, Fin.mk_lt_mk]; omega
  have hb : Before T c c' := (stdEquiv_lt_iff hT).mp hlt
  split_ifs with hd
  · have hrow : c.1.1 < c'.1.1 := by
      have := hd.2
      rwa [SYTe.rowN_of_lt _ hk0, SYTe.rowN_of_lt _ hk] at this
    unfold Before at hb
    rcases hb with hb | ⟨heq, hcol⟩
    · omega
    · exfalso
      have hx : (c'.1.1, c.1.2) ∈ μ.cells := by
        rw [mem_cells]
        exact μ.up_left_mem le_rfl hcol.le ((mem_cells _).mp c'.2)
      let x : Cell μ := ⟨(c'.1.1, c.1.2), hx⟩
      have h1 : T c' ≤ T x := hT.1 x c' rfl hcol
      have h2 : T x < T c := hT.2 c x rfl hrow
      omega
  · unfold Before at hb; omega

theorem D_le_aN {k : ℕ} (hk : k < μ.cells.card) : (stdSYT hT).D k ≤ aN hT k := by
  induction h : μ.cells.card - 1 - k generalizing k with
  | zero => rw [(stdSYT hT).D_eq_zero (by omega)]; exact Nat.zero_le _
  | succ m ih =>
    have hk1 : k + 1 < μ.cells.card := by omega
    have := ih hk1 (by omega)
    have hstep := aN_step hT hk1
    rw [(stdSYT hT).D_succ k]
    omega

/-- The decreasing sequence `b_k = T(cell k) − D_k`. -/
noncomputable def bN (k : ℕ) : ℕ := aN hT k - (stdSYT hT).D k

theorem bN_antitone : Antitone (bN hT) := by
  refine antitone_nat_of_succ_le fun k => ?_
  unfold bN
  by_cases hk : k + 1 < μ.cells.card
  · have h1 := aN_step hT hk
    have h2 := D_le_aN hT hk
    have h3 := (stdSYT hT).D_succ k
    split_ifs at h1 h3 <;> omega
  · have : aN hT (k + 1) = 0 := by unfold aN; rw [dif_neg (by omega)]
    omega

/-- The decreasing sequence attached to `T`, as a `DecSeq`. -/
noncomputable def bSeq : DecSeq μ.cells.card :=
  ⟨fun k => bN hT k, fun _ _ h => bN_antitone hT (Fin.le_def.mp h)⟩

theorem phiFun_std : (stdSYT hT).phiFun (bSeq hT).1 = T := by
  funext c
  simp only [SYTe.phiFun, bSeq, bN]
  have h := D_le_aN hT ((stdSYT hT).e c).2
  have ha : aN hT ((stdSYT hT).e c) = T c := by
    unfold aN; rw [dif_pos ((stdSYT hT).e c).2]; simp
  omega

end Inverse

namespace SYTe

variable {μ : YoungDiagram} (S : SYTe μ)

theorem before_phiFun_iff {b : Fin μ.cells.card → ℕ} (hb : Antitone b) {c' c : Cell μ} :
    Before (S.phiFun b) c' c ↔ S.e c' < S.e c := by
  have back : ∀ {c' c : Cell μ}, S.e c' < S.e c → Before (S.phiFun b) c' c := by
    intro c' c h
    have h1 := hb h.le
    have h2 := S.D_le_of_le (Fin.le_def.mp h.le)
    unfold Before phiFun
    by_cases heq : b (S.e c) + S.D (S.e c) = b (S.e c') + S.D (S.e c')
    · right
      refine ⟨heq.symm, ?_⟩
      have hD : S.D (S.e c) = S.D (S.e c') := by omega
      have := S.colN_lt_of_D_eq (Fin.lt_def.mp h) (S.e c).2 hD
      rwa [colN_e, colN_e] at this
    · left; omega
  refine ⟨fun h => ?_, back⟩
  by_contra hn
  rcases lt_or_eq_of_le (not_lt.mp hn) with hlt | heq
  · exact before_irrefl c (before_trans (back hlt) h)
  · rw [S.e.injective heq] at h; exact before_irrefl _ h

theorem stdSYT_phiFun {b : Fin μ.cells.card → ℕ} (hb : Antitone b) :
    stdSYT (S.phiFun_isRSSYT hb) = S := by
  apply ext'
  ext c
  show rank (S.phiFun b) c = (S.e c).val
  rw [rank, ← Fin.card_Iio (S.e c)]
  refine card_equiv S.e fun c' => ?_
  simp only [mem_filter, mem_univ, true_and, mem_Iio]
  exact S.before_phiFun_iff hb

end SYTe

/-- **Stanley's standardization bijection.** Reverse semistandard tableaux of shape `μ` correspond
to pairs (standard tableau `S`, weakly decreasing sequence `b` of length `n = |μ|`). -/
noncomputable def stdEquivSigma (μ : YoungDiagram) :
    (Σ _ : SYTe μ, DecSeq μ.cells.card) ≃ RSSYT μ :=
  Equiv.ofBijective (fun x => ⟨x.1.phiFun x.2.1, x.1.phiFun_isRSSYT x.2.2⟩) <| by
    constructor
    · rintro ⟨S, b, hb⟩ ⟨S', b', hb'⟩ h
      have hT : S.phiFun b = S'.phiFun b' := congrArg Subtype.val h
      have hS : S = S' := by
        rw [← S.stdSYT_phiFun hb, ← S'.stdSYT_phiFun hb']
        congr 1
      subst hS
      have hbb : b = b' := by
        funext k
        have := congrFun hT (S.e.symm k)
        simp only [SYTe.phiFun, Equiv.apply_symm_apply] at this
        omega
      subst hbb
      rfl
    · rintro ⟨T, hT⟩
      exact ⟨⟨stdSYT hT, bSeq hT⟩, Subtype.ext (phiFun_std hT)⟩

/-- **Weight bookkeeping.** `|Φ(S, b)| = maj S + |b|`. -/
theorem sum_stdEquivSigma {μ : YoungDiagram} (x : Σ _ : SYTe μ, DecSeq μ.cells.card) :
    ∑ c, (stdEquivSigma μ x).1 c = x.1.maj + ∑ k, x.2.1 k :=
  x.1.sum_phiFun x.2.1

end QOU.Mathlib.MajStandardization
