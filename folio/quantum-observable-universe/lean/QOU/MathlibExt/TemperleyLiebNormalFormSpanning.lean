import QOU.MathlibExt.TemperleyLiebNormalIdxCatalan
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# The Jones normal forms span `TL_{m+1}(δ)`, hence `finrank ≤ catalan (m+1)`

Spanning half of `dim TL_{m+1}(δ) = catalan (m+1)`, for every `m`, over any
commutative ring.

## Route, and why no left-multiplication closure rule is needed

The corpus tried to close `span (range NormalIdx.elt)` under **left**
multiplication by a generator, on the `(I, J)` index, and recorded the branch
"where no loop forms" as open (`TemperleyLiebDeltaRule`). This file does not take
that route. It works with **right** multiplication and inducts on the number of
generators, peeling off the block with the largest top. Done that way, only two
operations ever touch the normal forms.

1. **Appending a block whose top exceeds every top already present**
   (`exists_append_block`). When the new bottom `j` collides with existing
   bottoms, the rule

       [a'↓b'] · [a↓j] = [a'↓j] · [a↓b'+2]     (a' < a, j ≤ b' ≤ a')

   (`blk_ins`) moves `j` down and lifts the displaced bottom by two. This
   cascades through the list but stays a normal form. Its core is the
   two-block identity `[x↓y][x+1↓y] = [x↓y][x+1↓y+2]` (`blkL_G`).
2. **Five right-multiplication rules for the top block** `[m↓j] · e_k`
   (`blk_mul_E_*`). Each one either yields `δ·[m↓j]`, yields a block with top
   `m`, or factors as `[k-2↓j]·[m↓k]`. In the last case the lower factor is
   absorbed by the induction hypothesis on `m` generators.

Blocks are `blk a b = e_a e_{a-1} ⋯ e_b`. A normal form is stored as a
**reversed** list of `(top, bottom)` pairs, last block first (`NFr`, `prodR`).
`exists_normalIdx_elt_eq` then identifies each one with the corpus's
`NormalIdx.elt`, so the spanning statement is about the corpus's own family.

## What is proved

* `span_range_elt_eq_top : span R (range (NormalIdx.elt δ)) = ⊤`, for every `m`;
* `finrank_le_catalan : finrank R (TLFin R δ m) ≤ catalan (m+1)`
  (with `[StrongRankCondition R]`), via `card_normalIdx`.

## 🛑 What is NOT proved

Linear independence of the normal forms, and hence `finrank = catalan`, is
**not** here. It needs a representation that separates them.

-- Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.MathlibExt.TemperleyLiebNormalFormSpanning

open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebNormalForm
open QOU.MathlibExt.TemperleyLiebNormalIdxCatalan (card_normalIdx)

variable {R : Type*} [CommRing R] {δ : R} {M : ℕ}

local notation "A" => TLFin R δ M

/-! ## Generators indexed by `ℕ` -/

/-- `E i = e_i` for `i < M`, and `0` otherwise. -/
noncomputable def E (R : Type*) [CommRing R] (δ : R) (M : ℕ) (i : ℕ) : TLFin R δ M :=
  if h : i < M then e R δ (adjFin (n := M)) ⟨i, h⟩ else 0

theorem E_fin (i : Fin M) : e R δ (adjFin (n := M)) i = E R δ M i.val := by
  simp [E, i.isLt]

theorem E_sq {i : ℕ} (h : i < M) :
    E R δ M i * E R δ M i = algebraMap R A δ * E R δ M i := by
  simp only [E, h, dif_pos]; exact e_sq_fin _

theorem E_adj1 {i : ℕ} (h : i + 1 < M) :
    E R δ M i * E R δ M (i + 1) * E R δ M i = E R δ M i := by
  simp only [E, h, show i < M by omega, dif_pos]
  exact e_adjacent_fin (Or.inl rfl)

theorem E_adj2 {i : ℕ} (h : i + 1 < M) :
    E R δ M (i + 1) * E R δ M i * E R δ M (i + 1) = E R δ M (i + 1) := by
  simp only [E, h, show i < M by omega, dif_pos]
  exact e_adjacent_fin (Or.inr rfl)

theorem E_comm {i j : ℕ} (h : i + 2 ≤ j ∨ j + 2 ≤ i) :
    E R δ M i * E R δ M j = E R δ M j * E R δ M i := by
  by_cases hi : i < M
  · by_cases hj : j < M
    · simp only [E, hi, hj, dif_pos]
      exact e_commute_fin (by simpa using h)
    · simp [E, hj]
  · simp [E, hi]

/-! ## Runs -/

/-- `runL y d = E (y+d-1) ⋯ E (y+1) E y` — the descending run of length `d` with
bottom `y`. -/
noncomputable def runL (R : Type*) [CommRing R] (δ : R) (M : ℕ) : ℕ → ℕ → TLFin R δ M
  | _, 0 => 1
  | y, d + 1 => runL R δ M (y + 1) d * E R δ M y

/-- The block `[a↓b] = e_a ⋯ e_b`, empty when `b = a + 1`. -/
noncomputable def blk (R : Type*) [CommRing R] (δ : R) (M : ℕ) (a b : ℕ) : TLFin R δ M :=
  runL R δ M b (a + 1 - b)

local notation "L" => runL R δ M
local notation "Bk" => blk R δ M
local notation "Ee" => E R δ M

theorem runL_zero (y : ℕ) : L y 0 = 1 := rfl

theorem runL_succ (y d : ℕ) : L y (d + 1) = L (y + 1) d * Ee y := rfl

theorem runL_succ_top (y d : ℕ) : L y (d + 1) = Ee (y + d) * L y d := by
  induction d generalizing y with
  | zero => simp [runL_succ, runL_zero]
  | succ d ih =>
      rw [runL_succ, ih (y + 1), runL_succ y d, mul_assoc,
        show y + 1 + d = y + (d + 1) by ring]

theorem runL_add (y d d' : ℕ) : L (y + d) d' * L y d = L y (d + d') := by
  induction d generalizing y with
  | zero => simp [runL_zero]
  | succ d ih =>
      rw [runL_succ y d, ← mul_assoc, show y + (d + 1) = (y + 1) + d by ring, ih,
        show d + 1 + d' = (d + d') + 1 by ring, runL_succ]

theorem E_comm_runL (k : ℕ) :
    ∀ (d y : ℕ), (∀ t, y ≤ t → t < y + d → t + 2 ≤ k ∨ k + 2 ≤ t) →
      Ee k * L y d = L y d * Ee k := by
  intro d
  induction d with
  | zero => intro y _; simp [runL_zero]
  | succ d ih =>
      intro y h
      rw [runL_succ, ← mul_assoc, ih (y + 1) (fun t h1 h2 => h t (by omega) (by omega)),
        mul_assoc, E_comm (h y le_rfl (by omega)).symm, mul_assoc]

/-- Runs whose letters are at distance `≥ 2` commute. -/
theorem runL_comm (y d y' d' : ℕ) (h : y + d + 1 ≤ y') :
    L y d * L y' d' = L y' d' * L y d := by
  induction d generalizing y with
  | zero => simp [runL_zero]
  | succ d ih =>
      rw [runL_succ, mul_assoc, E_comm_runL y d' y' (fun t h1 _ => Or.inr (by omega)),
        ← mul_assoc, ih (y + 1) (by omega), mul_assoc]

/-! ## The block identities -/

/-- `[x↓y][x+1↓y] = [x↓y][x+1↓y+2]`, in run form (`x = y + d`). -/
theorem blkL_G (y : ℕ) :
    ∀ d, y + d + 1 < M → L y (d + 1) * L y (d + 2) = L y (d + 1) * L (y + 2) d := by
  intro d
  induction d with
  | zero =>
      intro hM
      rw [runL_zero, mul_one, runL_succ_top y 1, runL_succ_top y 0, runL_zero, mul_one,
        ← mul_assoc]
      exact E_adj1 (by omega)
  | succ d ih =>
      intro hM
      have hc : L y (d + 1) * Ee (y + d + 2) = Ee (y + d + 2) * L y (d + 1) :=
        (E_comm_runL _ _ _ (fun t _ h2 => Or.inl (by omega))).symm
      rw [runL_succ_top y (d + 1), runL_succ_top y (d + 2), runL_succ_top y (d + 1),
        show y + (d + 2) = y + d + 2 by ring, show y + (d + 1) = y + d + 1 by ring]
      calc Ee (y + d + 1) * L y (d + 1) * (Ee (y + d + 2) * (Ee (y + d + 1) * L y (d + 1)))
          = Ee (y + d + 1) * Ee (y + d + 2) *
              (L y (d + 1) * (Ee (y + d + 1) * L y (d + 1))) := by
            simp only [mul_assoc]
            rw [← mul_assoc (L y (d + 1)) (Ee (y + d + 2)), hc]; simp only [mul_assoc]
        _ = Ee (y + d + 1) * Ee (y + d + 2) * (L y (d + 1) * L y (d + 2)) := by
            rw [runL_succ_top y (d + 1), show y + (d + 1) = y + d + 1 by ring]
        _ = Ee (y + d + 1) * Ee (y + d + 2) * (L y (d + 1) * L (y + 2) d) := by
            rw [ih (by omega)]
        _ = Ee (y + d + 1) * L y (d + 1) * (Ee (y + d + 2) * L (y + 2) d) := by
            simp only [mul_assoc]
            rw [← mul_assoc (Ee (y + d + 2)) (L y (d + 1)), ← hc]; simp only [mul_assoc]
        _ = Ee (y + d + 1) * L y (d + 1) * L (y + 2) (d + 1) := by
            rw [runL_succ_top (y + 2) d, show y + 2 + d = y + d + 2 by ring]

/-- `[x↓y][x+1↓z] = [x↓z][x+1↓y+2]` for `z ≤ y ≤ x`, in run form
(`y = z + c`, `x = y + d`). -/
theorem blkL_H (z c d : ℕ) (hM : z + c + d + 1 < M) :
    L (z + c) (d + 1) * L z (c + d + 2) = L z (c + d + 1) * L (z + c + 2) d := by
  rw [show c + d + 2 = c + (d + 2) by ring, ← runL_add z c (d + 2), ← mul_assoc,
    blkL_G (z + c) d hM, mul_assoc, ← runL_comm z c (z + c + 2) d (by omega), ← mul_assoc,
    runL_add, show c + (d + 1) = c + d + 1 by ring]

/-- **The insertion rule.** `[a'↓b'][a↓j] = [a'↓j][a↓b'+2]` for `a' < a`,
`j ≤ b' ≤ a'`. -/
theorem blk_ins {a' b' a j : ℕ} (h1 : a' < a) (h2 : j ≤ b') (h3 : b' ≤ a') (hM : a < M) :
    Bk a' b' * Bk a j = Bk a' j * Bk a (b' + 2) := by
  obtain ⟨c, rfl⟩ : ∃ c, b' = j + c := ⟨b' - j, by omega⟩
  obtain ⟨d, rfl⟩ : ∃ d, a' = j + c + d := ⟨a' - (j + c), by omega⟩
  obtain ⟨e', rfl⟩ : ∃ e', a = j + c + d + 1 + e' := ⟨a - (j + c + d + 1), by omega⟩
  simp only [blk]
  rw [show j + c + d + 1 - (j + c) = d + 1 by omega,
    show j + c + d + 1 + e' + 1 - j = (c + d + 2) + e' by omega,
    show j + c + d + 1 - j = c + d + 1 by omega,
    show j + c + d + 1 + e' + 1 - (j + c + 2) = d + e' by omega,
    ← runL_add j (c + d + 2) e', show j + (c + d + 2) = j + c + d + 2 by ring]
  rw [← mul_assoc, runL_comm (j + c) (d + 1) (j + c + d + 2) e' (by omega), mul_assoc,
    blkL_H j c d (by omega), ← mul_assoc,
    ← runL_comm j (c + d + 1) (j + c + d + 2) e' (by omega), mul_assoc,
    ← runL_add (j + c + 2) d e', show j + c + 2 + d = j + c + d + 2 by ring]

/-- `[a↓a] = e_a`. -/
theorem blk_self (a : ℕ) : Bk a a = Ee a := by
  simp [blk, show a + 1 - a = 1 by omega, runL_succ, runL_zero]

/-- The empty block. -/
theorem blk_empty (a : ℕ) : Bk a (a + 1) = 1 := by
  simp [blk, runL_zero]

/-! ## Right multiplication of a block by a generator -/

theorem blk_mul_E_far {m j k : ℕ} (h : k + 2 ≤ j) : Bk m j * Ee k = Ee k * Bk m j :=
  (E_comm_runL _ _ _ (fun t h1 _ => Or.inr (by omega))).symm

theorem blk_mul_E_down {m k : ℕ} (h : k ≤ m) : Bk m (k + 1) * Ee k = Bk m k := by
  simp only [blk]
  rw [show m + 1 - k = (m - k) + 1 by omega, runL_succ, show m + 1 - (k + 1) = m - k by omega]

theorem blk_mul_E_loop {m j : ℕ} (h : j ≤ m) (hM : m < M) :
    Bk m j * Ee j = algebraMap R A δ * Bk m j := by
  simp only [blk]
  rw [show m + 1 - j = (m - j) + 1 by omega, runL_succ, mul_assoc, E_sq (by omega),
    ← mul_assoc, ← Algebra.commutes, mul_assoc]

theorem blk_mul_E_up {m j : ℕ} (h : j + 1 ≤ m) (hM : m < M) :
    Bk m j * Ee (j + 1) = Bk m (j + 1) := by
  simp only [blk]
  rw [show m + 1 - j = (m - j - 1) + 1 + 1 by omega, runL_succ, runL_succ,
    show m + 1 - (j + 1) = (m - j - 1) + 1 by omega, runL_succ, mul_assoc, mul_assoc,
    ← mul_assoc (Ee (j + 1)), E_adj2 (by omega)]

theorem blk_mul_E_split {m j k : ℕ} (h : j + 2 ≤ k) (hk : k ≤ m) (hM : m < M) :
    Bk m j * Ee k = Bk (k - 2) j * Bk m k := by
  obtain ⟨c, rfl⟩ : ∃ c, k = j + 2 + c := ⟨k - (j + 2), by omega⟩
  obtain ⟨d, rfl⟩ : ∃ d, m = j + 2 + c + d := ⟨m - (j + 2 + c), by omega⟩
  simp only [blk]
  rw [show j + 2 + c + d + 1 - j = (c + 1) + (d + 2) by omega,
    show j + 2 + c - 2 + 1 - j = c + 1 by omega,
    show j + 2 + c + d + 1 - (j + 2 + c) = d + 1 by omega,
    ← runL_add j (c + 1) (d + 2), show j + (c + 1) = j + c + 1 by ring,
    runL_succ (j + c + 1) (d + 1), show j + c + 1 + 1 = j + 2 + c by ring,
    runL_succ (j + 2 + c) d]
  have hc : L j (c + 1) * Ee (j + 2 + c) = Ee (j + 2 + c) * L j (c + 1) :=
    (E_comm_runL _ _ _ (fun t _ h2 => Or.inl (by omega))).symm
  have hadj : Ee (j + 2 + c) * Ee (j + c + 1) * Ee (j + 2 + c) = Ee (j + 2 + c) := by
    have := E_adj2 (R := R) (δ := δ) (M := M) (i := j + c + 1) (by omega)
    rwa [show j + c + 1 + 1 = j + 2 + c by ring] at this
  calc L (j + 2 + c + 1) d * Ee (j + 2 + c) * Ee (j + c + 1) * L j (c + 1) * Ee (j + 2 + c)
      = L (j + 2 + c + 1) d * (Ee (j + 2 + c) * Ee (j + c + 1) * Ee (j + 2 + c))
          * L j (c + 1) := by
        rw [mul_assoc _ (L j (c + 1)), hc]; simp only [mul_assoc]
    _ = L (j + 2 + c + 1) d * Ee (j + 2 + c) * L j (c + 1) := by rw [hadj, mul_assoc]
    _ = L j (c + 1) * (L (j + 2 + c + 1) d * Ee (j + 2 + c)) := by
        rw [← runL_succ, runL_comm j (c + 1) (j + 2 + c) (d + 1) (by omega)]

/-! ## Normal forms as reversed block lists -/

/-- Normal-form condition on a **reversed** block list (last block first):
bottoms `≤` tops, tops and bottoms strictly decreasing. -/
def NFr : List (ℕ × ℕ) → Prop
  | [] => True
  | p :: x => p.2 ≤ p.1 ∧ (∀ q ∈ x, q.1 < p.1 ∧ q.2 < p.2) ∧ NFr x

/-- The product of a reversed block list, in word order. -/
noncomputable def prodR (R : Type*) [CommRing R] (δ : R) (M : ℕ) :
    List (ℕ × ℕ) → TLFin R δ M
  | [] => 1
  | p :: x => prodR R δ M x * blk R δ M p.1 p.2

local notation "P" => prodR R δ M

/-- Normal forms with all tops `< m`. -/
def NFset (R : Type*) [CommRing R] (δ : R) (M m : ℕ) : Set (TLFin R δ M) :=
  {z | ∃ x, NFr x ∧ (∀ q ∈ x, q.1 < m) ∧ z = prodR R δ M x}

/-- Their span. -/
noncomputable def S (R : Type*) [CommRing R] (δ : R) (M m : ℕ) : Submodule R (TLFin R δ M) :=
  Submodule.span R (NFset R δ M m)

theorem NFset_mono {m m' : ℕ} (h : m ≤ m') : NFset R δ M m ⊆ NFset R δ M m' := by
  rintro z ⟨x, hx, ht, rfl⟩; exact ⟨x, hx, fun q hq => by have := ht q hq; omega, rfl⟩

theorem S_mono {m m' : ℕ} (h : m ≤ m') : S R δ M m ≤ S R δ M m' :=
  Submodule.span_mono (NFset_mono h)

/-- **Appending a block whose top exceeds every existing top** stays a normal
form, with bottoms controlled. -/
theorem exists_append_block :
    ∀ (x : List (ℕ × ℕ)), NFr x → ∀ (a j γ : ℕ), (∀ q ∈ x, q.1 < a) → a < M →
      j ≤ a + 1 → (∀ q ∈ x, q.2 < γ) → j ≤ γ →
      ∃ y, NFr y ∧ (∀ q ∈ y, q.1 ≤ a) ∧ (∀ q ∈ y, q.2 < γ + 2) ∧
        P x * Bk a j = P y := by
  intro x
  induction x with
  | nil =>
      intro _ a j γ _ hM hj _ hjγ
      by_cases hja : j ≤ a
      · refine ⟨[(a, j)], ⟨hja, by simp, trivial⟩, by simp, by simp; omega, ?_⟩
        simp [prodR]
      · refine ⟨[], trivial, by simp, by simp, ?_⟩
        rw [show j = a + 1 by omega, blk_empty]; simp [prodR]
  | cons p x' ih =>
      obtain ⟨a', b'⟩ := p
      rintro ⟨hb'a', hx'lt, hx'⟩ a j γ htop hM hj hbot hjγ
      have ha'a : a' < a := htop (a', b') (by simp)
      have hb'γ : b' < γ := hbot (a', b') (by simp)
      by_cases hbj : b' < j
      · by_cases hja : j ≤ a
        · refine ⟨(a, j) :: (a', b') :: x', ⟨hja, ?_, hb'a', hx'lt, hx'⟩, ?_, ?_, rfl⟩
          · intro q hq
            simp only [List.mem_cons] at hq
            rcases hq with rfl | hq
            · exact ⟨ha'a, hbj⟩
            · have := hx'lt q hq; exact ⟨by omega, by omega⟩
          · intro q hq
            simp only [List.mem_cons] at hq
            rcases hq with rfl | rfl | hq
            · exact le_rfl
            · exact ha'a.le
            · exact (htop q (by simp [hq])).le
          · intro q hq
            simp only [List.mem_cons] at hq
            rcases hq with rfl | rfl | hq
            · simp; omega
            · simp; omega
            · have := hbot q (by simp [hq]); omega
        · refine ⟨(a', b') :: x', ⟨hb'a', hx'lt, hx'⟩, ?_, ?_, ?_⟩
          · intro q hq; exact (htop q hq).le
          · intro q hq; have := hbot q hq; omega
          · rw [show j = a + 1 by omega, blk_empty, mul_one]
      · obtain ⟨y', hy', hy'top, hy'bot, hy'eq⟩ :=
          ih hx' a' j b' (fun q hq => (hx'lt q hq).1) (by omega) (by omega)
            (fun q hq => (hx'lt q hq).2) (by omega)
        have hprod : P ((a', b') :: x') * Bk a j = P y' * Bk a (b' + 2) := by
          show P x' * Bk a' b' * Bk a j = _
          rw [mul_assoc, blk_ins ha'a (by omega) hb'a' hM, ← mul_assoc, hy'eq]
        by_cases hb2 : b' + 2 ≤ a
        · refine ⟨(a, b' + 2) :: y', ⟨hb2, ?_, hy'⟩, ?_, ?_, hprod⟩
          · intro q hq; exact ⟨by have := hy'top q hq; omega, hy'bot q hq⟩
          · intro q hq
            simp only [List.mem_cons] at hq
            rcases hq with rfl | hq
            · exact le_rfl
            · have := hy'top q hq; omega
          · intro q hq
            simp only [List.mem_cons] at hq
            rcases hq with rfl | hq
            · simp; omega
            · have := hy'bot q hq; omega
        · refine ⟨y', hy', fun q hq => by have := hy'top q hq; omega,
            fun q hq => by have := hy'bot q hq; omega, ?_⟩
          rw [hprod, show b' + 2 = a + 1 by omega, blk_empty, mul_one]

theorem append_mem {m : ℕ} (hM : m < M) {z : A} (hz : z ∈ NFset R δ M m) {j : ℕ}
    (hj : j ≤ m + 1) : z * Bk m j ∈ NFset R δ M (m + 1) := by
  obtain ⟨x, hx, ht, rfl⟩ := hz
  obtain ⟨y, hy, hyt, -, heq⟩ := exists_append_block (R := R) (δ := δ) x hx m j (m + 1) ht hM hj
    (fun q hq => by
      induction x with
      | nil => simp at hq
      | cons p x' _ =>
          simp only [List.mem_cons] at hq
          rcases hq with rfl | hq
          · have := ht _ (List.mem_cons_self ..); have := hx.1; omega
          · have := (hx.2.1 q hq).2; have := hx.1; have := ht p (by simp); omega) hj
  exact ⟨y, hy, fun q hq => by have := hyt q hq; omega, heq⟩

/-- Right multiplication by a fixed element, checked on a spanning set. -/
theorem span_mul_mem {s : Set A} {T : Submodule R A} {r : A} (h : ∀ z ∈ s, z * r ∈ T) :
    ∀ w ∈ Submodule.span R s, w * r ∈ T := by
  have : Submodule.span R s ≤ T.comap (LinearMap.mulRight R r) :=
    Submodule.span_le.mpr fun z hz => by simpa using h z hz
  intro w hw; simpa using this hw

theorem S_mul_blk {m : ℕ} (hM : m < M) {j : ℕ} (hj : j ≤ m + 1) :
    ∀ w ∈ S R δ M m, w * Bk m j ∈ S R δ M (m + 1) :=
  span_mul_mem fun _z hz => Submodule.subset_span (append_mem hM hz hj)

/-! ## Right closure, by induction on the number of generators -/

/-- `span NF_m` is closed under right multiplication by `e_k`, `k < m`. -/
def RightClosed (R : Type*) [CommRing R] (δ : R) (M m : ℕ) : Prop :=
  ∀ k < m, ∀ w ∈ S R δ M m, w * E R δ M k ∈ S R δ M m

theorem rightClosed_runL {m : ℕ} (hrc : RightClosed R δ M m) :
    ∀ d y, y + d ≤ m → ∀ w ∈ S R δ M m, w * L y d ∈ S R δ M m := by
  intro d
  induction d with
  | zero => intro y _ w hw; simpa [runL_zero] using hw
  | succ d ih =>
      intro y hyd w hw
      rw [runL_succ, ← mul_assoc]
      exact hrc y (by omega) _ (ih (y + 1) (by omega) w hw)

theorem rightClosed_succ {m : ℕ} (hM : m < M) (hrc : RightClosed R δ M m) :
    RightClosed R δ M (m + 1) := by
  intro k hk
  apply span_mul_mem
  rintro z ⟨x, hx, ht, rfl⟩
  -- either every top is `< m`, or the last block has top `m`
  rcases x with _ | ⟨⟨a, b⟩, x'⟩
  · have hz : P [] ∈ NFset R δ M m := ⟨[], trivial, by simp, rfl⟩
    by_cases hkm : k < m
    · exact S_mono (Nat.le_succ m) (hrc k hkm _ (Submodule.subset_span hz))
    · rw [show k = m by omega, ← blk_self]
      exact S_mul_blk hM (by omega) _ (Submodule.subset_span hz)
  obtain ⟨hba, hlt, hx'⟩ := hx
  have hx'S : P x' ∈ S R δ M m := Submodule.subset_span
    ⟨x', hx', fun q hq => by have := (hlt q hq).1; have := ht (a, b) (by simp); omega, rfl⟩
  by_cases ham : a < m
  · have hz : P ((a, b) :: x') ∈ NFset R δ M m :=
      ⟨(a, b) :: x', ⟨hba, hlt, hx'⟩, fun q hq => by
        simp only [List.mem_cons] at hq
        rcases hq with rfl | hq
        · exact ham
        · have := (hlt q hq).1; omega, rfl⟩
    by_cases hkm : k < m
    · exact S_mono (Nat.le_succ m) (hrc k hkm _ (Submodule.subset_span hz))
    · rw [show k = m by omega, ← blk_self]
      exact S_mul_blk hM (by omega) _ (Submodule.subset_span hz)
  have ha : a = m := by have := ht (a, b) (by simp); omega
  subst ha
  show P x' * Bk a b * Ee k ∈ _
  have hk' : k ≤ a := by omega
  rcases (show k + 2 ≤ b ∨ k + 1 = b ∨ k = b ∨ k = b + 1 ∨ b + 2 ≤ k by omega) with
    h | h | h | h | h
  · rw [mul_assoc, blk_mul_E_far h, ← mul_assoc]
    exact S_mul_blk hM (by omega) _ (hrc k (by omega) _ hx'S)
  · rw [mul_assoc, ← h, blk_mul_E_down hk']
    exact S_mul_blk hM (by omega) _ hx'S
  · rw [mul_assoc, ← h, blk_mul_E_loop (by omega) hM, ← mul_assoc,
      ← Algebra.commutes, mul_assoc, ← Algebra.smul_def, h]
    refine Submodule.smul_mem _ _ (Submodule.subset_span ?_)
    exact ⟨(a, b) :: x', ⟨hba, hlt, hx'⟩, ht, rfl⟩
  · rw [mul_assoc, h, blk_mul_E_up (by omega) hM]
    exact S_mul_blk hM (by omega) _ hx'S
  · rw [mul_assoc, blk_mul_E_split h hk' hM, ← mul_assoc]
    refine S_mul_blk hM (by omega) _ ?_
    exact rightClosed_runL hrc _ _ (by omega) _ hx'S

theorem rightClosed : ∀ m, m ≤ M → RightClosed R δ M m := by
  intro m
  induction m with
  | zero => intro _ k hk; omega
  | succ m ih => intro hm; exact rightClosed_succ (by omega) (ih (by omega))

/-- **The normal forms span `TL_{M+1}(δ)`** (reversed-block-list form). -/
theorem S_eq_top : S R δ M M = ⊤ := by
  have hrc := rightClosed (R := R) (δ := δ) M le_rfl
  have h1 : (1 : A) ∈ S R δ M M := Submodule.subset_span ⟨[], trivial, by simp, rfl⟩
  -- closure under right multiplication by anything
  have hall : ∀ y : A, ∀ w ∈ S R δ M M, w * y ∈ S R δ M M := by
    intro y
    have hy : y ∈ Algebra.adjoin R (Set.range (e R δ (adjFin (n := M)))) := by
      rw [QOU.MathlibExt.HeckeToTemperleyLieb.adjoin_range_e_eq_top]; trivial
    induction hy using Algebra.adjoin_induction with
    | mem y hy =>
        obtain ⟨i, rfl⟩ := hy
        intro w hw; rw [E_fin]; exact hrc _ i.isLt w hw
    | algebraMap r =>
        intro w hw
        rw [← Algebra.commutes, ← Algebra.smul_def]; exact Submodule.smul_mem _ _ hw
    | add y₁ y₂ _ _ h₁ h₂ => intro w hw; rw [mul_add]; exact Submodule.add_mem _ (h₁ w hw) (h₂ w hw)
    | mul y₁ y₂ _ _ h₁ h₂ => intro w hw; rw [← mul_assoc]; exact h₂ _ (h₁ w hw)
  rw [eq_top_iff]
  intro y _
  simpa using hall y 1 h1

/-! ## Back to the corpus's `NormalIdx.elt` -/

theorem NFr_pairwise : ∀ x : List (ℕ × ℕ), NFr x →
    x.Pairwise (fun p q => q.1 < p.1 ∧ q.2 < p.2) := by
  intro x
  induction x with
  | nil => intro _; exact List.Pairwise.nil
  | cons p x ih => intro h; exact List.Pairwise.cons h.2.1 (ih h.2.2)

theorem NFr_bot_lt_top : ∀ x : List (ℕ × ℕ), NFr x → ∀ q ∈ x, q.2 ≤ q.1 := by
  intro x
  induction x with
  | nil => simp
  | cons p x ih =>
      intro h q hq
      simp only [List.mem_cons] at hq
      rcases hq with rfl | hq
      · exact h.1
      · exact ih h.2.2 q hq

/-- Tops strictly increasing in word order. -/
theorem sorted_tops (x : List (ℕ × ℕ)) (hx : NFr x) :
    ((x.map Prod.fst).reverse).Sorted (· < ·) := by
  rw [List.Sorted, List.pairwise_reverse, List.pairwise_map]
  exact (NFr_pairwise x hx).imp fun h => h.1

theorem sorted_bots (x : List (ℕ × ℕ)) (hx : NFr x) :
    ((x.map Prod.snd).reverse).Sorted (· < ·) := by
  rw [List.Sorted, List.pairwise_reverse, List.pairwise_map]
  exact (NFr_pairwise x hx).imp fun h => h.2

/-- The `Fin M`-set of a list of naturals. -/
def finSet (l : List ℕ) : Finset (Fin M) := Finset.univ.filter (fun y : Fin M => y.val ∈ l)

theorem map_val_elems {l : List ℕ} (hs : l.Sorted (· < ·)) (hlt : ∀ k ∈ l, k < M) :
    (elems (finSet (M := M) l)).map Fin.val = l := by
  have hs' : ((elems (finSet (M := M) l)).map Fin.val).Sorted (· < ·) := by
    rw [List.Sorted, List.pairwise_map]
    exact (List.pairwise_lt_finRange M).sublist List.filter_sublist
  apply List.Sorted.eq_of_mem_iff hs' hs
  intro k
  simp only [List.mem_map, elems, List.mem_filter, List.mem_finRange, true_and, finSet,
    Finset.mem_filter, Finset.mem_univ, decide_eq_true_eq]
  constructor
  · rintro ⟨y, hy, rfl⟩; exact hy
  · intro hk; exact ⟨⟨k, hlt k hk⟩, hk, rfl⟩

theorem card_filter_finSet {l : List ℕ} (hlt : ∀ k ∈ l, k < M) (t : ℕ) :
    ((finSet (M := M) l).filter (fun y => y.val ≤ t)).card
      = (l.toFinset.filter (· ≤ t)).card := by
  rw [← Finset.card_map Fin.valEmbedding]
  congr 1
  ext k
  simp only [Finset.mem_map, Finset.mem_filter, finSet, Finset.mem_univ, true_and,
    Fin.valEmbedding_apply, List.mem_toFinset]
  constructor
  · rintro ⟨y, ⟨hy, hyt⟩, rfl⟩; exact ⟨hy, hyt⟩
  · rintro ⟨hk, hkt⟩; exact ⟨⟨k, hlt k hk⟩, ⟨hk, hkt⟩, rfl⟩

/-- Threshold domination for a normal form. -/
theorem threshold (x : List (ℕ × ℕ)) (hx : NFr x) (t : ℕ) :
    ((x.map Prod.fst).toFinset.filter (· ≤ t)).card
      ≤ ((x.map Prod.snd).toFinset.filter (· ≤ t)).card := by
  induction x with
  | nil => simp
  | cons p x ih =>
      obtain ⟨hp, hlt, hx'⟩ := hx
      have h1 : p.1 ∉ (x.map Prod.fst).toFinset := by
        simp only [List.mem_toFinset, List.mem_map]
        rintro ⟨q, hq, hqe⟩; have := (hlt q hq).1; omega
      have h2 : p.2 ∉ (x.map Prod.snd).toFinset := by
        simp only [List.mem_toFinset, List.mem_map]
        rintro ⟨q, hq, hqe⟩; have := (hlt q hq).2; omega
      simp only [List.map_cons, List.toFinset_cons, Finset.filter_insert]
      have := ih hx'
      by_cases ht1 : p.1 ≤ t
      · rw [if_pos ht1, if_pos (by omega), Finset.card_insert_of_notMem (by simp [h1]),
          Finset.card_insert_of_notMem (by simp [h2])]
        omega
      · rw [if_neg ht1]
        split_ifs
        · rw [Finset.card_insert_of_notMem (by simp [h2])]; omega
        · exact this

theorem card_toFinset_map (x : List (ℕ × ℕ)) (hx : NFr x) :
    (x.map Prod.fst).toFinset.card = x.length ∧ (x.map Prod.snd).toFinset.card = x.length := by
  have hp := NFr_pairwise x hx
  constructor
  · rw [List.toFinset_card_of_nodup, List.length_map]
    exact List.pairwise_map.mpr (hp.imp fun h => ne_of_gt h.1)
  · rw [List.toFinset_card_of_nodup, List.length_map]
    exact List.pairwise_map.mpr (hp.imp fun h => ne_of_gt h.2)

theorem prod_descRun (i j : Fin M) :
    ((descRun i j).map (e R δ (adjFin (n := M)))).prod = Bk i.val j.val := by
  simp only [descRun, List.map_map, blk]
  have key : ∀ n y, y + n = i.val + 1 →
      ((List.range n).map (fun t => E R δ M (i.val - t))).prod = L y n := by
    intro n
    induction n with
    | zero => intro y _; simp [runL_zero]
    | succ n ih =>
        intro y hy
        rw [List.range_succ, List.map_append, List.prod_append, ih (y + 1) (by omega),
          runL_succ]
        simp [show i.val - n = y by omega]
  by_cases hji : j.val ≤ i.val + 1
  · rw [← key (i.val + 1 - j.val) j.val (by omega)]
    congr 1
    apply List.map_congr_left
    intro t _
    simp [E_fin]
  · rw [show i.val + 1 - j.val = 0 by omega]; simp [runL_zero]

theorem prodR_eq (x : List (ℕ × ℕ)) :
    P x = (x.reverse.map (fun p => Bk p.1 p.2)).prod := by
  induction x with
  | nil => simp [prodR]
  | cons p x ih => simp [prodR, ih]

theorem zipWith_fst_snd {β : Type*} (f : ℕ → ℕ → β) (l : List (ℕ × ℕ)) :
    List.zipWith f (l.map Prod.fst) (l.map Prod.snd) = l.map (fun p => f p.1 p.2) := by
  induction l with
  | nil => rfl
  | cons p l ih => simp [ih]

/-- **Every normal form is a `NormalIdx.elt`.** -/
theorem exists_normalIdx_elt_eq (x : List (ℕ × ℕ)) (hx : NFr x) (ht : ∀ q ∈ x, q.1 < M) :
    ∃ p : NormalIdx M, p.elt δ = P x := by
  have hb : ∀ q ∈ x, q.2 < M := fun q hq =>
    lt_of_le_of_lt (NFr_bot_lt_top x hx q hq) (ht q hq)
  set T := (x.map Prod.fst).reverse
  set B := (x.map Prod.snd).reverse
  have hT : ∀ k ∈ T, k < M := by
    intro k hk; simp only [T, List.mem_reverse, List.mem_map] at hk
    obtain ⟨q, hq, rfl⟩ := hk; exact ht q hq
  have hB : ∀ k ∈ B, k < M := by
    intro k hk; simp only [B, List.mem_reverse, List.mem_map] at hk
    obtain ⟨q, hq, rfl⟩ := hk; exact hb q hq
  refine ⟨⟨(finSet T, finSet B), ?_, ?_⟩, ?_⟩
  · have h1 : (finSet (M := M) T).card = T.toFinset.card := by
      have := card_filter_finSet (M := M) hT (M + T.sum)
      rw [Finset.filter_true_of_mem (fun y _ => by have := y.isLt; omega),
        Finset.filter_true_of_mem (fun k hk => by
          have := hT k (List.mem_toFinset.mp hk); omega)] at this
      exact this
    have h2 : (finSet (M := M) B).card = B.toFinset.card := by
      have := card_filter_finSet (M := M) hB (M + B.sum)
      rw [Finset.filter_true_of_mem (fun y _ => by have := y.isLt; omega),
        Finset.filter_true_of_mem (fun k hk => by
          have := hB k (List.mem_toFinset.mp hk); omega)] at this
      exact this
    show (finSet B).card = (finSet T).card
    rw [h1, h2]
    simp only [T, B, List.toFinset_reverse]
    rw [(card_toFinset_map x hx).1, (card_toFinset_map x hx).2]
  · intro t
    have e1 : ((finSet (M := M) T).filter (· ≤ t)).card
        = ((finSet (M := M) T).filter (fun y => y.val ≤ t.val)).card := by
      congr 1
    have e2 : ((finSet (M := M) B).filter (· ≤ t)).card
        = ((finSet (M := M) B).filter (fun y => y.val ≤ t.val)).card := by
      congr 1
    rw [e1, e2, card_filter_finSet hT, card_filter_finSet hB]
    simp only [T, B, List.toFinset_reverse]
    exact threshold x hx t.val
  · simp only [NormalIdx.elt, NormalIdx.word, List.map_flatten, List.prod_flatten,
      List.map_map]
    have hzip : ((List.zipWith descRun (elems (finSet (M := M) T)) (elems (finSet B))).map
        (List.prod ∘ List.map (e R δ (adjFin (n := M))))) =
        List.zipWith (fun i j => Bk i j) ((elems (finSet (M := M) T)).map Fin.val)
          ((elems (finSet (M := M) B)).map Fin.val) := by
      rw [List.map_zipWith, List.zipWith_map_left, List.zipWith_map_right]
      congr 1
      funext i j
      exact prod_descRun i j
    rw [hzip, map_val_elems (sorted_tops x hx) hT, map_val_elems (sorted_bots x hx) hB,
      prodR_eq]
    simp only [← List.map_reverse, zipWith_fst_snd]

/-! ## The theorems -/

/-- **The Jones normal forms span `TL_{m+1}(δ)`**, for every `m`, over any
commutative ring. -/
theorem span_range_elt_eq_top (δ : R) (m : ℕ) :
    Submodule.span R (Set.range (NormalIdx.elt (m := m) (R := R) δ)) = ⊤ := by
  rw [eq_top_iff, ← S_eq_top (R := R) (δ := δ) (M := m)]
  apply Submodule.span_le.mpr
  rintro z ⟨x, hx, ht, rfl⟩
  obtain ⟨p, hp⟩ := exists_normalIdx_elt_eq (δ := δ) x hx ht
  exact Submodule.subset_span ⟨p, hp⟩

/-- **`finrank TL_{m+1}(δ) ≤ catalan (m+1)`**, for every `m`. -/
theorem finrank_le_catalan [StrongRankCondition R] (δ : R) (m : ℕ) :
    Module.finrank R (TLFin R δ m) ≤ catalan (m + 1) := by
  rw [← card_normalIdx m, ← finrank_top R (TLFin R δ m), ← span_range_elt_eq_top δ m]
  exact finrank_range_le_card (R := R) _

end QOU.MathlibExt.TemperleyLiebNormalFormSpanning
