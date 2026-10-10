import QOU.Mathlib.Bialternant
import QOU.Mathlib.MajStandardization

/-!
# QOU.Mathlib.RSSYTSchur — reverse tableaux with bounded entries are counted by `schur`

For a Young diagram `μ` with at most `N` rows, the weighted sum over reverse semistandard
tableaux with entries in `{0, …, N − 1}`

    Σ_T ∏_{c ∈ μ} x_{T(c)}

equals `Bialternant.schur N ν x` with `ν_j = μ.rowLen (N − 1 − j)` (the row lengths, smallest
first). The proof peels off the cells holding `0`: they form a horizontal strip at the outer
boundary, and removing them and lowering the remaining entries by one gives a tableau of the
smaller shape with entries below `N − 1`. That is exactly the branching recursion `schur` is
defined by.

## Base ring (§7c)

Generic `[CommRing R]`.
-/

namespace QOU.Mathlib.RSSYTSchur

open Finset YoungDiagram QOU.Mathlib.MajStandardization QOU.Mathlib.Bialternant

variable {R : Type*} [CommRing R]

/-- A tableau with entries in `Fin M` that is reverse semistandard. -/
def IsBT {μ : YoungDiagram} {M : ℕ} (T : Cell μ → Fin M) : Prop :=
  IsRSSYT (fun c => (T c : ℕ))

/-- The weighted sum over reverse semistandard tableaux with entries below `M`. -/
noncomputable def bsum (μ : YoungDiagram) (M : ℕ) (x : Fin M → R) : R := by
  classical
  exact ∑ T ∈ univ.filter (fun T : Cell μ → Fin M => IsBT T), ∏ c, x (T c)

/-- Row lengths of `μ`, smallest first, padded to length `N`. -/
def seq (N : ℕ) (μ : YoungDiagram) : Fin N → ℕ := fun j => μ.rowLen (N - 1 - j)

theorem seq_monotone (N : ℕ) (μ : YoungDiagram) : Monotone (seq N μ) := by
  intro a b h
  exact μ.rowLen_anti _ _ (by have := Fin.le_def.mp h; omega)

/-- Entries drop strictly down a column, so the entry in row `r` is at most `M − r`. -/
theorem val_add_row_le {μ : YoungDiagram} {M : ℕ} (T : Cell μ → Fin (M + 1)) (hT : IsBT T) :
    ∀ (r col : ℕ) (h : (r, col) ∈ μ.cells), (T ⟨(r, col), h⟩ : ℕ) + r ≤ M := by
  intro r
  induction r with
  | zero => intro col h; have := (T ⟨(0, col), h⟩).2; omega
  | succ r ih =>
    intro col h
    have h' : (r, col) ∈ μ.cells := by
      rw [mem_cells] at h ⊢; exact μ.up_left_mem (Nat.le_succ r) le_rfl h
    have hlt := hT.2 ⟨(r, col), h'⟩ ⟨(r + 1, col), h⟩ rfl (Nat.lt_succ_self r)
    have := ih col h'
    simp only at hlt
    omega

/-- A down-closed subset of `range m` is an initial segment. -/
theorem filter_range_eq_range {p : ℕ → Prop} [DecidablePred p] (hp : ∀ c, p (c + 1) → p c)
    (m : ℕ) : (range m).filter p = range ((range m).filter p).card := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [range_add_one, filter_insert]
    by_cases hm : p m
    · have hall : ∀ c, c ≤ m → p c := by
        intro c hc
        induction hc using Nat.decreasingInduction with
        | self => exact hm
        | of_succ k _ h => exact hp k h
      have hr : (range m).filter p = range m :=
        filter_true_of_mem fun c hc => hall c (le_of_lt (mem_range.mp hc))
      rw [if_pos hm, hr, card_insert_of_notMem (by simp), card_range, ← range_add_one]
    · rw [if_neg hm]
      exact ih

/-! ## The zero cells of a tableau -/

section Strip

variable {μ : YoungDiagram} {N : ℕ}

open Classical in
/-- The entry of `T` at `(r, col)`, read as a natural number, and `0` off the diagram. -/
noncomputable def tv (T : Cell μ → Fin (N + 1)) (r col : ℕ) : ℕ :=
  if h : (r, col) ∈ μ.cells then T ⟨(r, col), h⟩ else 0

theorem tv_of_mem (T : Cell μ → Fin (N + 1)) {r col : ℕ} (h : (r, col) ∈ μ.cells) :
    tv T r col = T ⟨(r, col), h⟩ := by
  simp [tv, h]

theorem tv_pos_left (T : Cell μ → Fin (N + 1)) (hT : IsBT T) (r col : ℕ)
    (h : 1 ≤ tv T r (col + 1)) : 1 ≤ tv T r col := by
  by_cases hm : (r, col + 1) ∈ μ.cells
  · have hm' : (r, col) ∈ μ.cells := by
      rw [mem_cells] at hm ⊢; exact μ.up_left_mem le_rfl (Nat.le_succ col) hm
    rw [tv_of_mem T hm] at h
    rw [tv_of_mem T hm']
    have := hT.1 ⟨(r, col), hm'⟩ ⟨(r, col + 1), hm⟩ rfl (Nat.lt_succ_self col)
    simp only at this
    omega
  · simp [tv, hm] at h

/-- The number of nonzero entries in row `r`. -/
noncomputable def cnt (T : Cell μ → Fin (N + 1)) (r : ℕ) : ℕ := by
  classical
  exact ((range (μ.rowLen r)).filter (fun col => 1 ≤ tv T r col)).card

theorem lt_cnt_iff (T : Cell μ → Fin (N + 1)) (hT : IsBT T) (r col : ℕ)
    (hc : col < μ.rowLen r) : col < cnt T r ↔ 1 ≤ tv T r col := by
  classical
  have h := filter_range_eq_range (p := fun col => 1 ≤ tv T r col)
    (fun c hc => tv_pos_left T hT r c hc) (μ.rowLen r)
  have hmem : col ∈ (range (μ.rowLen r)).filter (fun col => 1 ≤ tv T r col)
      ↔ col ∈ range (cnt T r) := by
    rw [h]; unfold cnt; convert Iff.rfl
  rw [mem_filter, mem_range, mem_range] at hmem
  constructor
  · intro h1; exact (hmem.mpr h1).2
  · intro h1; exact hmem.mp ⟨hc, h1⟩

theorem cnt_le (T : Cell μ → Fin (N + 1)) (r : ℕ) : cnt T r ≤ μ.rowLen r := by
  classical
  unfold cnt
  exact (card_filter_le _ _).trans (card_range _).le

theorem rowLen_succ_le_cnt (T : Cell μ → Fin (N + 1)) (hT : IsBT T) (r : ℕ) :
    μ.rowLen (r + 1) ≤ cnt T r := by
  by_contra hlt
  push_neg at hlt
  have h1 : cnt T r < μ.rowLen (r + 1) := hlt
  have h2 : μ.rowLen (r + 1) ≤ μ.rowLen r := μ.rowLen_anti _ _ (Nat.le_succ r)
  have hbelow : (r + 1, cnt T r) ∈ μ.cells := by
    rw [mem_cells]; exact mem_iff_lt_rowLen.mpr h1
  have habove : (r, cnt T r) ∈ μ.cells := by
    rw [mem_cells]; exact mem_iff_lt_rowLen.mpr (by omega)
  have hlt' := hT.2 ⟨(r, cnt T r), habove⟩ ⟨(r + 1, cnt T r), hbelow⟩ rfl (Nat.lt_succ_self r)
  simp only at hlt'
  have := (lt_cnt_iff T hT r (cnt T r) (by omega)).not.mp (lt_irrefl _)
  rw [tv_of_mem T habove] at this
  omega

/-! ### The interlacing index and the stripped diagram -/

/-- The branching index of `schur (N + 1) (seq (N + 1) μ)`. -/
abbrev KIdx (μ : YoungDiagram) (N : ℕ) :=
  (j : Fin N) → Fin (seq (N + 1) μ j.succ + 1 - seq (N + 1) μ j.castSucc)

theorem seq_succ_succ (μ : YoungDiagram) (j : Fin N) :
    seq (N + 1) μ j.succ = μ.rowLen (N - 1 - j) := by
  simp only [seq, Fin.val_succ]; rw [show N + 1 - 1 - (↑j + 1) = N - 1 - ↑j by omega]

theorem seq_succ_castSucc (μ : YoungDiagram) (j : Fin N) :
    seq (N + 1) μ j.castSucc = μ.rowLen (N - j) := by
  simp only [seq, Fin.coe_castSucc]; rw [show N + 1 - 1 - ↑j = N - ↑j by omega]

theorem kIdx_lt (k : KIdx μ N) (j : Fin N) :
    (k j : ℕ) < μ.rowLen (N - 1 - j) + 1 - μ.rowLen (N - j) := by
  have := (k j).2
  have h1 := seq_succ_succ μ j
  have h2 := seq_succ_castSucc μ j
  omega

/-- Row lengths after the strip of zeros is removed. -/
def Lk (k : KIdx μ N) (r : ℕ) : ℕ :=
  if h : r < N then μ.rowLen (r + 1) + k ⟨N - 1 - r, by omega⟩ else 0

theorem Lk_of_lt (k : KIdx μ N) {r : ℕ} (h : r < N) :
    Lk k r = μ.rowLen (r + 1) + k ⟨N - 1 - r, by omega⟩ := dif_pos h

theorem Lk_of_le (k : KIdx μ N) {r : ℕ} (h : N ≤ r) : Lk k r = 0 := dif_neg (by omega)

theorem Lk_le (k : KIdx μ N) (r : ℕ) : Lk k r ≤ μ.rowLen r := by
  by_cases h : r < N
  · rw [Lk_of_lt k h]
    have hb := kIdx_lt k ⟨N - 1 - r, by omega⟩
    have h1 : N - 1 - (N - 1 - r) = r := by omega
    have h2 : N - (N - 1 - r) = r + 1 := by omega
    simp only [h1, h2] at hb
    have := μ.rowLen_anti r (r + 1) (Nat.le_succ r)
    omega
  · rw [Lk_of_le k (by omega)]; exact Nat.zero_le _

theorem rowLen_succ_le_Lk (k : KIdx μ N) {r : ℕ} (h : r < N) : μ.rowLen (r + 1) ≤ Lk k r := by
  rw [Lk_of_lt k h]; omega

theorem Lk_anti (k : KIdx μ N) {r r' : ℕ} (h : r' ≤ r) : Lk k r ≤ Lk k r' := by
  rcases h.lt_or_eq with h | h
  · by_cases hr : r < N
    · calc Lk k r ≤ μ.rowLen r := Lk_le k r
        _ ≤ μ.rowLen (r' + 1) := μ.rowLen_anti _ _ h
        _ ≤ Lk k r' := rowLen_succ_le_Lk k (by omega)
    · rw [Lk_of_le k (by omega)]; exact Nat.zero_le _
  · rw [h]

theorem rowLen_eq_of_mem_iff' {ν : YoungDiagram} {i k : ℕ}
    (h : ∀ j, (i, j) ∈ ν ↔ j < k) : ν.rowLen i = k := by
  have h1 : ¬ (ν.rowLen i < k) := fun hlt =>
    absurd (mem_iff_lt_rowLen.mp ((h _).mpr hlt)) (lt_irrefl _)
  have h2 : ¬ (k < ν.rowLen i) := fun hlt =>
    absurd ((h k).mp (mem_iff_lt_rowLen.mpr hlt)) (lt_irrefl _)
  omega

/-- The diagram left after removing the strip of zeros prescribed by `k`. -/
def dk (k : KIdx μ N) : YoungDiagram where
  cells := μ.cells.filter (fun c => c.2 < Lk k c.1)
  isLowerSet := by
    intro a b hba ha
    simp only [coe_filter, Set.mem_setOf_eq] at ha ⊢
    refine ⟨μ.isLowerSet hba ha.1, ?_⟩
    exact lt_of_le_of_lt hba.2 (lt_of_lt_of_le ha.2 (Lk_anti k hba.1))

theorem mem_dk (k : KIdx μ N) (c : ℕ × ℕ) : c ∈ (dk k).cells ↔ c ∈ μ.cells ∧ c.2 < Lk k c.1 := by
  simp [dk]

theorem rowLen_dk (k : KIdx μ N) (r : ℕ) : (dk k).rowLen r = Lk k r := by
  apply rowLen_eq_of_mem_iff'
  intro col
  rw [← mem_cells, mem_dk, mem_cells, mem_iff_lt_rowLen]
  have := Lk_le k r
  constructor
  · exact fun h => h.2
  · exact fun h => ⟨by omega, h⟩

theorem seq_dk (k : KIdx μ N) : seq N (dk k) = fun j => seq (N + 1) μ j.castSucc + k j := by
  funext j
  rw [seq, rowLen_dk, Lk_of_lt k (by omega)]
  have e1 := seq_succ_castSucc μ j
  have h1 : N - 1 - j + 1 = N - j := by omega
  have h2 : (⟨N - 1 - (N - 1 - j), by omega⟩ : Fin N) = j := Fin.ext (by simp; omega)
  have h3 : (k ⟨N - 1 - (N - 1 - j), by omega⟩ : ℕ) = k j := congrArg (fun i => (k i : ℕ)) h2
  rw [h1]
  omega

theorem colLen_dk_le (k : KIdx μ N) : (dk k).colLen 0 ≤ N := by
  by_contra h
  push_neg at h
  have hm : (N, 0) ∈ (dk k).cells := by rw [mem_cells]; exact mem_iff_lt_colLen.mpr h
  have := ((mem_dk k _).mp hm).2
  rw [Lk_of_le k le_rfl] at this
  exact Nat.not_lt_zero _ this

theorem Lk_rev (k : KIdx μ N) (j : Fin N) : Lk k (N - 1 - j) = μ.rowLen (N - j) + k j := by
  rw [Lk_of_lt k (by omega)]
  have h1 : N - 1 - j + 1 = N - j := by omega
  have h2 : (⟨N - 1 - (N - 1 - j), by omega⟩ : Fin N) = j := Fin.ext (by simp; omega)
  have h3 : (k ⟨N - 1 - (N - 1 - j), by omega⟩ : ℕ) = k j := congrArg (fun i => (k i : ℕ)) h2
  rw [h1]
  omega

/-! ### Every tableau has exactly one strip index -/

/-- `T` has zeros exactly outside `dk k`. -/
def P (k : KIdx μ N) (T : Cell μ → Fin (N + 1)) : Prop :=
  ∀ c : Cell μ, (1 ≤ (T c : ℕ) ↔ c.1.2 < Lk k c.1.1)

/-- The strip index of a tableau: row `N − 1 − j` keeps `cnt` nonzero entries. -/
noncomputable def kOf (T : Cell μ → Fin (N + 1)) (hT : IsBT T) : KIdx μ N := fun j =>
  ⟨cnt T (N - 1 - j) - μ.rowLen (N - j), by
    have e1 := seq_succ_succ μ j
    have e2 := seq_succ_castSucc μ j
    have h1 := cnt_le T (N - 1 - j)
    have h2 := rowLen_succ_le_cnt T hT (N - 1 - j)
    rw [show N - 1 - j + 1 = N - j by omega] at h2
    omega⟩

theorem Lk_kOf (T : Cell μ → Fin (N + 1)) (hT : IsBT T) {r : ℕ} (hr : r < N) :
    Lk (kOf T hT) r = cnt T r := by
  rw [Lk_of_lt _ hr]
  simp only [kOf]
  rw [show N - 1 - (N - 1 - r) = r by omega, show N - (N - 1 - r) = r + 1 by omega]
  have := rowLen_succ_le_cnt T hT r
  omega

theorem P_kOf (T : Cell μ → Fin (N + 1)) (hT : IsBT T) : P (kOf T hT) T := by
  rintro ⟨⟨r, col⟩, hc⟩
  simp only
  by_cases hr : r < N
  · rw [Lk_kOf T hT hr]
    have hcol : col < μ.rowLen r := mem_iff_lt_rowLen.mp ((mem_cells _).mp hc)
    rw [lt_cnt_iff T hT r col hcol, tv_of_mem T hc]
  · rw [Lk_of_le _ (by omega)]
    have := val_add_row_le T hT r col hc
    constructor
    · intro h; omega
    · intro h; exact absurd h (Nat.not_lt_zero _)

theorem P_unique {k k' : KIdx μ N} {T : Cell μ → Fin (N + 1)} (h : P k T) (h' : P k' T) :
    k = k' := by
  have hL : ∀ r, r < N → Lk k r = Lk k' r := by
    intro r hr
    have key : ∀ {a b : KIdx μ N}, P a T → P b T → ¬ Lk a r < Lk b r := by
      intro a b ha hb hlt
      have hmem : (r, Lk a r) ∈ μ.cells := by
        rw [mem_cells]; exact mem_iff_lt_rowLen.mpr (lt_of_lt_of_le hlt (Lk_le b r))
      have h1 := (ha ⟨_, hmem⟩).not.mpr (lt_irrefl _)
      have h2 := (hb ⟨_, hmem⟩).mpr hlt
      exact h1 h2
    have := key h h'
    have := key h' h
    omega
  funext j
  apply Fin.ext
  have := hL (N - 1 - j) (by omega)
  rw [Lk_rev, Lk_rev] at this
  omega

/-! ### Removing the strip: a bijection for each fixed index -/

theorem row_lt_of_mem_dk (k : KIdx μ N) {c : ℕ × ℕ} (h : c ∈ (dk k).cells) : c.1 < N := by
  by_contra hr
  have := ((mem_dk k c).mp h).2
  rw [Lk_of_le k (by omega)] at this
  exact Nat.not_lt_zero _ this

/-- A cell of the stripped diagram, as a cell of `μ`. -/
def incl (k : KIdx μ N) (c : Cell (dk k)) : Cell μ := ⟨c.1, ((mem_dk k c.1).mp c.2).1⟩

/-- Restrict to the stripped diagram and lower every entry by one. -/
def res (k : KIdx μ N) (T : Cell μ → Fin (N + 1)) : Cell (dk k) → Fin N := fun c =>
  ⟨(T (incl k c) : ℕ) - 1, by
    have := row_lt_of_mem_dk k c.2
    have := (T (incl k c)).2
    omega⟩

open Classical in
/-- Raise every entry by one and fill the strip with zeros. -/
noncomputable def ext (k : KIdx μ N) (T : Cell (dk k) → Fin N) : Cell μ → Fin (N + 1) := fun c =>
  if h : c.1 ∈ (dk k).cells then (T ⟨c.1, h⟩).succ else 0

theorem ext_val (k : KIdx μ N) (T : Cell (dk k) → Fin N) (c : Cell μ) :
    ((ext k T c : Fin (N + 1)) : ℕ) = if h : c.1 ∈ (dk k).cells then (T ⟨c.1, h⟩ : ℕ) + 1 else 0 := by
  unfold ext
  split_ifs <;> simp

theorem res_isBT (k : KIdx μ N) {T : Cell μ → Fin (N + 1)} (hT : IsBT T) (hP : P k T) :
    IsBT (res k T) := by
  have hpos : ∀ c : Cell (dk k), 1 ≤ (T (incl k c) : ℕ) :=
    fun c => (hP (incl k c)).mpr ((mem_dk k c.1).mp c.2).2
  constructor
  · intro c c' h1 h2
    have := hT.1 (incl k c) (incl k c') h1 h2
    have := hpos c; have := hpos c'
    beta_reduce at *
    simp only [res]; omega
  · intro c c' h1 h2
    have := hT.2 (incl k c) (incl k c') h1 h2
    have := hpos c; have := hpos c'
    beta_reduce at *
    simp only [res]; omega

theorem ext_isBT (k : KIdx μ N) (hμ : μ.colLen 0 ≤ N + 1) {T : Cell (dk k) → Fin N}
    (hT : IsBT T) : IsBT (ext k T) ∧ P k (ext k T) := by
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · intro c c' h1 h2
    beta_reduce
    rw [ext_val, ext_val]
    by_cases hc' : c'.1 ∈ (dk k).cells
    · have hc : c.1 ∈ (dk k).cells :=
        (dk k).isLowerSet (show c.1 ≤ c'.1 from ⟨le_of_eq h1, le_of_lt h2⟩) hc'
      rw [dif_pos hc, dif_pos hc']
      have := hT.1 ⟨c.1, hc⟩ ⟨c'.1, hc'⟩ h1 h2
      simp only at this; omega
    · rw [dif_neg hc']; exact Nat.zero_le _
  · intro c c' h1 h2
    beta_reduce
    rw [ext_val, ext_val]
    have hc : c.1 ∈ (dk k).cells := by
      rw [mem_dk]
      refine ⟨c.2, ?_⟩
      have hc'mem : (c'.1.1, c'.1.2) ∈ μ := c'.2
      have hrow : c'.1.2 < μ.rowLen c'.1.1 := mem_iff_lt_rowLen.mp hc'mem
      have hr : c.1.1 < N := by
        have : c'.1.1 < μ.colLen 0 := by
          have := mem_iff_lt_colLen.mp (μ.up_left_mem le_rfl (Nat.zero_le _) hc'mem)
          exact this
        omega
      calc c.1.2 = c'.1.2 := h1
        _ < μ.rowLen c'.1.1 := hrow
        _ ≤ μ.rowLen (c.1.1 + 1) := μ.rowLen_anti _ _ h2
        _ ≤ Lk k c.1.1 := rowLen_succ_le_Lk k hr
    rw [dif_pos hc]
    by_cases hc' : c'.1 ∈ (dk k).cells
    · rw [dif_pos hc']
      have := hT.2 ⟨c.1, hc⟩ ⟨c'.1, hc'⟩ h1 h2
      simp only at this; omega
    · rw [dif_neg hc']; omega
  · intro c
    rw [ext_val]
    by_cases hc : c.1 ∈ (dk k).cells
    · rw [dif_pos hc]
      exact ⟨fun _ => ((mem_dk k c.1).mp hc).2, fun _ => by omega⟩
    · rw [dif_neg hc]
      constructor
      · intro h; exact absurd h (by omega)
      · intro h; exact absurd ((mem_dk k c.1).mpr ⟨c.2, h⟩) hc

open Classical in
/-- The number of zeros a tableau in the fibre of `k` carries. -/
noncomputable def Zc (k : KIdx μ N) : ℕ :=
  (univ.filter fun c : Cell μ => c.1 ∉ (dk k).cells).card

open Classical in
theorem sum_fiber (k : KIdx μ N) (hμ : μ.colLen 0 ≤ N + 1) (x : Fin (N + 1) → R) :
    ∑ T ∈ univ.filter (fun T : Cell μ → Fin (N + 1) => IsBT T ∧ P k T), ∏ c, x (T c)
      = x 0 ^ Zc k * bsum (dk k) N (Fin.tail x) := by
  unfold bsum
  rw [mul_sum]
  refine sum_nbij' (res k) (ext k) ?_ ?_ ?_ ?_ ?_
  · intro T hT
    rw [mem_filter] at hT ⊢
    exact ⟨mem_univ _, res_isBT k hT.2.1 hT.2.2⟩
  · intro T hT
    rw [mem_filter] at hT ⊢
    exact ⟨mem_univ _, ext_isBT k hμ hT.2⟩
  · intro T hT
    rw [mem_filter] at hT
    funext c
    apply Fin.ext
    rw [ext_val]
    by_cases hc : c.1 ∈ (dk k).cells
    · rw [dif_pos hc]
      have hpos := (hT.2.2 c).mpr ((mem_dk k c.1).mp hc).2
      simp only [res, incl, Subtype.coe_eta]
      omega
    · rw [dif_neg hc]
      have := (hT.2.2 c).not.mpr (fun h => hc ((mem_dk k c.1).mpr ⟨c.2, h⟩))
      omega
  · intro T _
    funext c
    apply Fin.ext
    simp only [res, incl]
    rw [ext_val, dif_pos c.2]
    simp
  · intro T hT
    rw [mem_filter] at hT
    rw [← prod_filter_mul_prod_filter_not univ (fun c : Cell μ => c.1 ∈ (dk k).cells), mul_comm]
    congr 1
    · rw [Zc, ← prod_const]
      refine prod_congr rfl fun c hc => ?_
      rw [mem_filter] at hc
      have := (hT.2.2 c).not.mpr (fun h => hc.2 ((mem_dk k c.1).mpr ⟨c.2, h⟩))
      congr 1
      apply Fin.ext
      simp only [Fin.val_zero]
      omega
    · refine prod_bij' (fun c hc => ⟨c.1, (mem_filter.mp hc).2⟩) (fun c _ => incl k c)
        (fun _ _ => mem_univ _) (fun c _ => by rw [mem_filter]; exact ⟨mem_univ _, c.2⟩)
        (fun _ _ => rfl) (fun _ _ => rfl) ?_
      intro c hc
      rw [mem_filter] at hc
      have hpos := (hT.2.2 c).mpr ((mem_dk k c.1).mp hc.2).2
      simp only [Fin.tail]
      congr 1
      apply Fin.ext
      simp only [res, incl, Fin.val_succ, Subtype.coe_eta]
      omega

open Classical in
/-- **Strip decomposition.** -/
theorem bsum_succ (hμ : μ.colLen 0 ≤ N + 1) (x : Fin (N + 1) → R) :
    bsum μ (N + 1) x = ∑ k : KIdx μ N, x 0 ^ Zc k * bsum (dk k) N (Fin.tail x) := by
  have h1 : bsum μ (N + 1) x = ∑ T ∈ univ.filter (fun T : Cell μ → Fin (N + 1) => IsBT T),
      ∑ k : KIdx μ N, if P k T then ∏ c, x (T c) else 0 := by
    unfold bsum
    refine sum_congr rfl fun T hT => ?_
    rw [mem_filter] at hT
    rw [sum_eq_single (kOf T hT.2)]
    · rw [if_pos (P_kOf T hT.2)]
    · intro k _ hk
      rw [if_neg]
      intro hP
      exact hk (P_unique hP (P_kOf T hT.2))
    · intro h; exact absurd (mem_univ _) h
  rw [h1, sum_comm]
  refine sum_congr rfl fun k _ => ?_
  rw [← sum_fiber k hμ x, sum_filter, sum_filter]
  refine sum_congr rfl fun T _ => ?_
  by_cases h : IsBT T <;> by_cases h' : P k T <;> simp [h, h']

open Classical in
theorem Zc_eq_sum (k : KIdx μ N) (hμ : μ.colLen 0 ≤ N + 1) :
    Zc k = ∑ r ∈ range (N + 1), (μ.rowLen r - Lk k r) := by
  have hset : (univ.filter fun c : Cell μ => c.1 ∉ (dk k).cells).map (Function.Embedding.subtype _)
      = (range (N + 1)).biUnion (fun r => (Ico (Lk k r) (μ.rowLen r)).image (fun col => (r, col))) := by
    ext ⟨r, col⟩
    simp only [mem_map, mem_filter, mem_univ, true_and, Function.Embedding.coe_subtype,
      mem_biUnion, mem_range, mem_image, mem_Ico, mem_dk, not_and, not_lt, Prod.mk.injEq]
    constructor
    · rintro ⟨⟨⟨r', col'⟩, hm⟩, hc, heq⟩
      simp only [Prod.mk.injEq] at heq
      obtain ⟨rfl, rfl⟩ := heq
      have hm : (r', col') ∈ μ := hm
      refine ⟨r', ?_, col', ⟨hc ((mem_cells _).mpr hm), mem_iff_lt_rowLen.mp hm⟩, rfl, rfl⟩
      have := mem_iff_lt_colLen.mp (μ.up_left_mem le_rfl (Nat.zero_le _) hm)
      omega
    · rintro ⟨r', _, col', ⟨h1, h2⟩, rfl, rfl⟩
      exact ⟨⟨(r', col'), (mem_cells _).mpr (mem_iff_lt_rowLen.mpr h2)⟩, fun _ => h1, rfl⟩
  rw [Zc, ← card_map (Function.Embedding.subtype _), hset, card_biUnion]
  · refine sum_congr rfl fun r _ => ?_
    rw [card_image_of_injective _ (fun a b h => (Prod.mk.inj h).2), Nat.card_Ico]
  · intro r _ r' _ hne
    simp only [Function.onFun]
    rw [disjoint_left]
    intro a ha ha'
    rw [mem_image] at ha ha'
    obtain ⟨_, _, rfl⟩ := ha
    obtain ⟨_, _, h⟩ := ha'
    exact hne (Prod.mk.inj h).1.symm

theorem Zc_eq (k : KIdx μ N) (hμ : μ.colLen 0 ≤ N + 1) :
    Zc k = seq (N + 1) μ 0 + ∑ j : Fin N,
      (seq (N + 1) μ j.succ - (seq (N + 1) μ j.castSucc + k j)) := by
  rw [Zc_eq_sum k hμ, sum_range_succ, Lk_of_le k le_rfl, Nat.sub_zero, add_comm]
  have hs : seq (N + 1) μ 0 = μ.rowLen N := by simp [seq]
  rw [hs]
  congr 1
  rw [← Fin.sum_univ_eq_sum_range (fun r => μ.rowLen r - Lk k r) N,
    ← Equiv.sum_comp Fin.revPerm]
  refine sum_congr rfl fun j _ => ?_
  simp only [Fin.revPerm_apply, Fin.val_rev]
  rw [show N - (j + 1) = N - 1 - j by omega, Lk_rev]
  have e1 := seq_succ_succ μ j
  have e2 := seq_succ_castSucc μ j
  omega

end Strip

/-! ## The theorem -/

/-- **Reverse tableaux with entries below `N` are counted by the Schur polynomial.** -/
theorem bsum_eq_schur (N : ℕ) (μ : YoungDiagram) (hμ : μ.colLen 0 ≤ N) (x : Fin N → R) :
    bsum μ N x = schur N (seq N μ) x := by
  classical
  induction N generalizing μ with
  | zero =>
    have hempty : μ.cells = ∅ := by
      ext ⟨r, col⟩
      simp only [Finset.notMem_empty, iff_false]
      intro h
      have := mem_iff_lt_colLen.mp
        (μ.up_left_mem (Nat.zero_le r) (Nat.zero_le col) ((mem_cells _).mp h))
      omega
    have hno : ∀ a, a ∉ μ.cells := by rw [hempty]; simp
    have hcell : IsEmpty (Cell μ) := ⟨fun c => hno _ c.2⟩
    unfold bsum
    rw [schur]
    have huniv : (univ.filter fun T : Cell μ → Fin 0 => IsBT T) = univ := by
      apply filter_true_of_mem
      intro T _
      exact ⟨fun c => isEmptyElim c, fun c => isEmptyElim c⟩
    rw [huniv]
    simp
  | succ N ih =>
    rw [bsum_succ hμ, schur]
    refine sum_congr rfl fun k _ => ?_
    rw [ih (dk k) (colLen_dk_le k) (Fin.tail x), seq_dk, Zc_eq k hμ]

end QOU.Mathlib.RSSYTSchur
