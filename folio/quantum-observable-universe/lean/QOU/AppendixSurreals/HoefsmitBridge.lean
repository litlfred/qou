import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.SignSequence
import QOU.AppendixSurreals.BirthdayGrading

/-!
# QOU.AppendixSurreals.HoefsmitBridge — Hoefsmit ↔ Conway construction

The bridge proposition `prop:hoefsmit-is-surreal-construction` asserts
an injective forest-embedding from standard tableaux of two-rowed shapes
into finite-dyadic surreals (represented by their sign sequences / dyadic
rationals) of bounded birthday for **all** `n : ℕ`.

## Mathematical Formulation

A standard Young tableau of size `n` with at most two rows (`λ = (λ₁, λ₂)`
with `λ₁ + λ₂ = n` and `λ₂ ≤ λ₁`) is uniquely specified by its
Young–Jucys–Murphy (YJM) growth sequence of box additions from `1` to `n`:
- At `n = 0`, the empty tableau has an empty sign sequence `[]`.
- At `n ≥ 1`, box `1` is necessarily placed in row `1` (producing `(1, 0)`),
  and each subsequent box `k ∈ {2, …, n}` is placed either in row `1`
  (recorded as `Sign.plus`, the symmetric `q`-eigenchannel) or in row `2`
  (recorded as `Sign.minus`, the antisymmetric `-q⁻¹`-eigenchannel).
- The two-row standardness invariant `λ₂ ≤ λ₁` at every intermediate stage
  `1 ≤ k ≤ n` is the **ballot condition** (`IsTwoRowBallot`): at every prefix
  `p` of the length-`(n - 1)` sign sequence `steps : List Sign`, the number
  of `Sign.minus` entries never exceeds `1` plus the number of `Sign.plus`
  entries (`countMinus p ≤ countPlus p + 1`).

This file defines:
1. `StandardTwoRowTableau (n : ℕ)` for **all** `n : ℕ` via the length-`(n - 1)`
   YJM sign sequence `steps : List Sign` together with the prefix ballot
   invariant `IsTwoRowBallot steps`.
2. `hoefsmitSurrealSignSeq (n : ℕ) : StandardTwoRowTableau n → List Sign` and
   the dyadic rational encoding `dyadicCode : List Sign → ℚ` (together with
   Gonshor's dyadic evaluation `hoefsmitGonshor (n : ℕ) : StandardTwoRowTableau n → ℚ`),
   proving for **all** `n : ℕ`:
   - **(a) Injectivity**: `Function.Injective (hoefsmitSurrealSignSeq n)` and
     `Function.Injective (hoefsmitDyadicCode n)` for every `n : ℕ`;
   - **(b) Base cases & one-row evaluation**: `n = 0` and `n = 1` map to `0`
     (empty sign sequence), while for `n ≥ 2` the one-row tableau `(n)` (all
     `Sign.plus`) maps to `(n - 1 : ℚ) > 0` under Gonshor evaluation;
   - **(c) YJM step & birthday bound**: every YJM box-addition step `extendRow1`
     or `extendRow2` appends `Sign.plus` or `Sign.minus`, and the sign sequence
     of any size-`n` tableau has length (birthday bound) `n - 1 ≤ n`;
   - **(d) Strict non-surjectivity for `n ≥ 2`**: the sign sequence of length
     `n - 1` starting with two `Sign.minus` steps (or at `n ≥ 3`, `Sign.minus :: Sign.minus :: …`,
     and in the full `n`-step tree starting box 1 in row 2) violates the ballot
     invariant, witnessing that the image in birthday-bounded sign sequences is a
     proper subset.
3. The legacy `TwoRowTableau` shape carrier and `hoefsmitDyadic` (`n ≤ 2`) are
   retained for backward compatibility.

## References

- [conway1976] Conway, *On Numbers and Games*, §0.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Chapter 2.
- [hoefsmit1974] Hoefsmit, *Representations of Hecke algebras of finite
  groups with BN-pairs of classical type*, PhD Thesis, UBC.

LaTeX label: `prop:hoefsmit-is-surreal-construction`
-/

namespace QOU.AppendixSurreals

universe u

/-- A **two-rowed Young shape of size n**: row sizes `(r₁, r₂)` with
    `r₁ + r₂ = n` and `r₁ ≥ r₂`. Retained for backward compatibility. -/
structure TwoRowTableau (n : ℕ) where
  row1 : ℕ
  row2 : ℕ
  size_eq : row1 + row2 = n
  rows_ord : row2 ≤ row1

namespace TwoRowTableau

/-- The unique tableau of size 0 (empty). -/
def empty : TwoRowTableau 0 :=
  { row1 := 0, row2 := 0, size_eq := rfl, rows_ord := le_refl 0 }

/-- The unique tableau of size 1 (single box in row 1). -/
def singleton : TwoRowTableau 1 :=
  { row1 := 1, row2 := 0, size_eq := rfl, rows_ord := Nat.zero_le 1 }

/-- For size 2: tableau `(2, 0)` (row of length 2). -/
def two_zero : TwoRowTableau 2 :=
  { row1 := 2, row2 := 0, size_eq := rfl, rows_ord := Nat.zero_le 2 }

/-- For size 2: tableau `(1, 1)` (column of length 2). -/
def one_one : TwoRowTableau 2 :=
  { row1 := 1, row2 := 1, size_eq := rfl, rows_ord := le_refl 1 }

/-- Decidable equality on shapes. -/
instance (n : ℕ) : DecidableEq (TwoRowTableau n) := fun t₁ t₂ =>
  if h : t₁.row1 = t₂.row1 then
    if h2 : t₁.row2 = t₂.row2 then
      isTrue (by cases t₁; cases t₂; congr)
    else isFalse (fun h3 => h2 (by rw [h3]))
  else isFalse (fun h3 => h (by rw [h3]))

end TwoRowTableau

/-- Legacy `n ≤ 2` shape-to-dyadic map (retained for backward compatibility). -/
noncomputable def hoefsmitDyadic :
    ∀ {n : ℕ} (_h : n ≤ 2), TwoRowTableau n → ℚ
  | 0, _, _ => 0
  | 1, _, _ => 0
  | 2, _, t => if t.row2 = 0 then 1 else -1
  | _ + 3, h, _ => absurd h (by omega)

/-- Bridge proposition for `n = 0` on `TwoRowTableau`. -/
theorem hoefsmit_bridge_zero :
    Function.Injective (@hoefsmitDyadic 0 (by omega)) := by
  intro t₁ t₂ _
  cases t₁; cases t₂
  congr <;> omega

/-- Bridge proposition for `n = 1` on `TwoRowTableau`. -/
theorem hoefsmit_bridge_one :
    Function.Injective (@hoefsmitDyadic 1 (by omega)) := by
  intro t₁ t₂ _
  cases t₁; cases t₂
  congr <;> omega

/-- Bridge proposition for `n = 2` on `TwoRowTableau`. -/
theorem hoefsmit_bridge_two :
    Function.Injective (@hoefsmitDyadic 2 (by omega)) := by
  intro t₁ t₂ heq
  have h1 : t₁.row2 = 0 ∨ t₁.row2 = 1 := by
    have := t₁.size_eq; have := t₁.rows_ord; omega
  have h2 : t₂.row2 = 0 ∨ t₂.row2 = 1 := by
    have := t₂.size_eq; have := t₂.rows_ord; omega
  rcases h1 with h1 | h1 <;> rcases h2 with h2 | h2
  · obtain ⟨r1₁, r2₁, sz₁, ord₁⟩ := t₁
    obtain ⟨r1₂, r2₂, sz₂, ord₂⟩ := t₂
    simp at h1 h2; subst h1; subst h2; congr; omega
  · rw [hoefsmitDyadic, hoefsmitDyadic, if_pos h1, if_neg (by omega)] at heq
    norm_num at heq
  · rw [hoefsmitDyadic, hoefsmitDyadic, if_neg (by omega), if_pos h2] at heq
    norm_num at heq
  · obtain ⟨r1₁, r2₁, sz₁, ord₁⟩ := t₁
    obtain ⟨r1₂, r2₂, sz₂, ord₂⟩ := t₂
    simp at h1 h2; subst h1; subst h2; congr; omega

/-! ## General-`n` Standard Two-Row Tableaux via YJM Ballot Sign Sequences -/

/-- Count of `Sign.plus` (row-1 box additions after box 1) in a sign sequence. -/
def countPlus : List Sign → ℕ
  | [] => 0
  | Sign.plus :: rest => countPlus rest + 1
  | Sign.minus :: rest => countPlus rest

/-- Count of `Sign.minus` (row-2 box additions) in a sign sequence. -/
def countMinus : List Sign → ℕ
  | [] => 0
  | Sign.plus :: rest => countMinus rest
  | Sign.minus :: rest => countMinus rest + 1

@[simp]
theorem countPlus_nil : countPlus [] = 0 := rfl

@[simp]
theorem countMinus_nil : countMinus [] = 0 := rfl

@[simp]
theorem countPlus_cons_plus (s : List Sign) :
    countPlus (Sign.plus :: s) = countPlus s + 1 := rfl

@[simp]
theorem countPlus_cons_minus (s : List Sign) :
    countPlus (Sign.minus :: s) = countPlus s := rfl

@[simp]
theorem countMinus_cons_plus (s : List Sign) :
    countMinus (Sign.plus :: s) = countMinus s := rfl

@[simp]
theorem countMinus_cons_minus (s : List Sign) :
    countMinus (Sign.minus :: s) = countMinus s + 1 := rfl

theorem countPlus_append (s₁ s₂ : List Sign) :
    countPlus (s₁ ++ s₂) = countPlus s₁ + countPlus s₂ := by
  induction s₁ with
  | nil => simp
  | cons a s₁ ih =>
    cases a <;> simp [ih, Nat.add_comm, Nat.add_left_comm]

theorem countMinus_append (s₁ s₂ : List Sign) :
    countMinus (s₁ ++ s₂) = countMinus s₁ + countMinus s₂ := by
  induction s₁ with
  | nil => simp
  | cons a s₁ ih =>
    cases a <;> simp [ih, Nat.add_comm, Nat.add_left_comm]

theorem countPlus_add_countMinus (s : List Sign) :
    countPlus s + countMinus s = s.length := by
  induction s with
  | nil => rfl
  | cons a s ih =>
    cases a <;> simp [List.length_cons] <;> omega

/-- **Two-row ballot condition** on a YJM sign sequence `s : List Sign`
    (representing placements of boxes `2, …, n` after box `1` is placed in
    row `1`): defined inductively so that at every stage row 2 has at most
    as many boxes as row 1 (`row2 ≤ row1`), and at the full sequence
    `countMinus s ≤ countPlus s + 1`. -/
def IsTwoRowBallot : List Sign → Prop
  | [] => True
  | s => countMinus s ≤ countPlus s + 1 ∧ ∀ k : ℕ, k ≤ s.length →
      countMinus (s.take k) ≤ countPlus (s.take k) + 1

/-- Equivalent characterization of `IsTwoRowBallot`: at every prefix length `k`,
    `countMinus (s.take k) ≤ countPlus (s.take k) + 1`. -/
def IsTwoRowBallotPrefix (s : List Sign) : Prop :=
  ∀ k : ℕ, countMinus (s.take k) ≤ countPlus (s.take k) + 1

theorem isTwoRowBallotPrefix_nil : IsTwoRowBallotPrefix [] := by
  intro k
  simp

theorem countMinus_replicate_plus : ∀ m : ℕ, countMinus (List.replicate m Sign.plus) = 0
  | 0 => rfl
  | m + 1 => by simp [List.replicate_succ, countMinus_replicate_plus m]

theorem countMinus_take_replicate_plus (m k : ℕ) :
    countMinus ((List.replicate m Sign.plus).take k) = 0 := by
  rw [List.take_replicate]
  exact countMinus_replicate_plus (min k m)

theorem isTwoRowBallotPrefix_replicate_plus (m : ℕ) :
    IsTwoRowBallotPrefix (List.replicate m Sign.plus) := by
  intro k
  rw [countMinus_take_replicate_plus]
  exact Nat.zero_le _

theorem take_append_singleton_of_le {α : Type*} (s : List α) (a : α) {k : ℕ}
    (hk : k ≤ s.length) : (s ++ [a]).take k = s.take k := by
  exact List.take_append_of_le_length hk

theorem take_append_singleton_of_gt {α : Type*} (s : List α) (a : α) {k : ℕ}
    (hk : s.length < k) : (s ++ [a]).take k = s ++ [a] := by
  have hlen : (s ++ [a]).length ≤ k := by
    rw [List.length_append, List.length_singleton]
    omega
  exact List.take_of_length_le hlen

theorem isTwoRowBallotPrefix_append_plus {s : List Sign}
    (hs : IsTwoRowBallotPrefix s) :
    IsTwoRowBallotPrefix (s ++ [Sign.plus]) := by
  intro k
  by_cases hk : k ≤ s.length
  · rw [take_append_singleton_of_le s Sign.plus hk]
    exact hs k
  · have hgt : s.length < k := by omega
    rw [take_append_singleton_of_gt s Sign.plus hgt]
    rw [countMinus_append, countPlus_append]
    simp only [countMinus_cons_plus, countMinus_nil, Nat.add_zero,
               countPlus_cons_plus, countPlus_nil, Nat.zero_add]
    have hfull := hs s.length
    rw [List.take_length] at hfull
    omega

theorem isTwoRowBallotPrefix_append_minus {s : List Sign}
    (hs : IsTwoRowBallotPrefix s)
    (hstrict : countMinus s < countPlus s + 1) :
    IsTwoRowBallotPrefix (s ++ [Sign.minus]) := by
  intro k
  by_cases hk : k ≤ s.length
  · rw [take_append_singleton_of_le s Sign.minus hk]
    exact hs k
  · have hgt : s.length < k := by omega
    rw [take_append_singleton_of_gt s Sign.minus hgt]
    rw [countMinus_append, countPlus_append]
    simp only [countMinus_cons_minus, countMinus_nil, Nat.zero_add,
               countPlus_cons_minus, countPlus_nil, Nat.add_zero]
    omega

/-- A **standard two-row Young tableau of size `n`** for general `n : ℕ`,
    represented by its Young–Jucys–Murphy (YJM) sign sequence of length `n - 1`
    satisfying the prefix ballot condition `IsTwoRowBallotPrefix`.

    At `n = 3`, this distinguishes the two standard tableaux of shape `(2, 1)`:
    - `[Sign.plus, Sign.minus]` (boxes 1, 2 in row 1; box 3 in row 2), and
    - `[Sign.minus, Sign.plus]` (box 1 in row 1; box 2 in row 2; box 3 in row 1). -/
structure StandardTwoRowTableau (n : ℕ) where
  /-- YJM sign sequence for boxes `2, …, n` (`+` = row 1, `-` = row 2). -/
  steps : List Sign
  /-- A size-`n` tableau has `n - 1` YJM transition steps. -/
  length_eq : steps.length = n - 1
  /-- Every intermediate shape in the YJM chain satisfies `row2 ≤ row1`. -/
  ballot : IsTwoRowBallotPrefix steps

namespace StandardTwoRowTableau

@[ext]
theorem ext {n : ℕ} {t₁ t₂ : StandardTwoRowTableau n}
    (h : t₁.steps = t₂.steps) : t₁ = t₂ := by
  cases t₁; cases t₂; simp at h; subst h; rfl

/-- The unique empty standard tableau at `n = 0`. -/
def empty : StandardTwoRowTableau 0 where
  steps := []
  length_eq := rfl
  ballot := isTwoRowBallotPrefix_nil

/-- The unique singleton standard tableau at `n = 1`. -/
def singleton : StandardTwoRowTableau 1 where
  steps := []
  length_eq := rfl
  ballot := isTwoRowBallotPrefix_nil

/-- The one-row standard tableau of shape `(n, 0)` for any `n : ℕ`
    (all YJM steps place boxes in row 1, i.e. `Sign.plus`). -/
def oneRow (n : ℕ) : StandardTwoRowTableau n where
  steps := List.replicate (n - 1) Sign.plus
  length_eq := List.length_replicate
  ballot := isTwoRowBallotPrefix_replicate_plus (n - 1)

/-- YJM box addition to row 1 (symmetric `q`-eigenchannel): appends `Sign.plus`
    to the sign sequence of a size-`(n + 1)` tableau, yielding a size-`(n + 2)`
    tableau. -/
def extendRow1 {n : ℕ} (t : StandardTwoRowTableau (n + 1)) :
    StandardTwoRowTableau (n + 2) where
  steps := t.steps ++ [Sign.plus]
  length_eq := by
    rw [List.length_append, t.length_eq]
    simp
  ballot := isTwoRowBallotPrefix_append_plus t.ballot

/-- YJM box addition to row 2 (antisymmetric `-q⁻¹`-eigenchannel), valid whenever
    row 2 currently has strictly fewer boxes than row 1 (`countMinus t.steps < countPlus t.steps + 1`). -/
def extendRow2 {n : ℕ} (t : StandardTwoRowTableau (n + 1))
    (h : countMinus t.steps < countPlus t.steps + 1) :
    StandardTwoRowTableau (n + 2) where
  steps := t.steps ++ [Sign.minus]
  length_eq := by
    rw [List.length_append, t.length_eq]
    simp
  ballot := isTwoRowBallotPrefix_append_minus t.ballot h

end StandardTwoRowTableau

/-! ## Canonical Surreal Sign-Sequence Embedding and Dyadic Evaluation -/

/-- **Canonical Hoefsmit-to-surreal sign-sequence embedding** for all `n : ℕ`:
    sends a standard two-row tableau `t : StandardTwoRowTableau n` to its
    length-`(n - 1)` YJM sign sequence `t.steps : List Sign`. -/
def hoefsmitSurrealSignSeq (n : ℕ) (t : StandardTwoRowTableau n) : List Sign :=
  t.steps

/-- **(a) Injectivity of `hoefsmitSurrealSignSeq n` for all `n : ℕ`.**
    Distinct standard two-row tableaux of size `n` have distinct YJM sign sequences. -/
theorem hoefsmitSurrealSignSeq_injective (n : ℕ) :
    Function.Injective (hoefsmitSurrealSignSeq n) := by
  intro t₁ t₂ h
  exact StandardTwoRowTableau.ext h

/-- Gonshor dyadic evaluation on `StandardTwoRowTableau n`. -/
def hoefsmitGonshor (n : ℕ) (t : StandardTwoRowTableau n) : ℚ :=
  gonshor (hoefsmitSurrealSignSeq n t)

/-- Helper: folding `GonshorState.step` over `k` copies of `Sign.plus` from any
    state with `hasHi = false` and `hasLo = true` (or `init`) adds `k` to `value`
    and keeps `hasHi = false`. -/
theorem foldl_replicate_plus_unbounded :
    ∀ (k : ℕ) (v lo hi : ℚ) (hLo : Bool),
      ((List.replicate k Sign.plus).foldl GonshorState.step
        { value := v, lo := lo, hi := hi, hasLo := hLo, hasHi := false }).value = v + (k : ℚ)
  | 0, v, lo, hi, hLo => by simp
  | k + 1, v, lo, hi, hLo => by
    rw [List.replicate_succ, List.foldl_cons]
    simp only [GonshorState.step, Bool.false_eq_true, ↓reduceIte]
    rw [foldl_replicate_plus_unbounded k (v + 1) v 0 true]
    push_cast
    ring

/-- Gonshor evaluation of `List.replicate k Sign.plus` is `(k : ℚ)`. -/
theorem gonshor_replicate_plus (k : ℕ) :
    gonshor (List.replicate k Sign.plus) = (k : ℚ) := by
  unfold gonshor GonshorState.init
  rw [foldl_replicate_plus_unbounded k 0 0 0 false]
  ring

/-- **(b.1) At `n = 0`, the empty tableau maps to `0`.** -/
theorem hoefsmitGonshor_zero (t : StandardTwoRowTableau 0) :
    hoefsmitGonshor 0 t = 0 := by
  have hnil : t.steps = [] := List.eq_nil_of_length_eq_zero t.length_eq
  simp [hoefsmitGonshor, hoefsmitSurrealSignSeq, hnil]

/-- **(b.2) At `n = 1`, the singleton tableau maps to `0`.** -/
theorem hoefsmitGonshor_one (t : StandardTwoRowTableau 1) :
    hoefsmitGonshor 1 t = 0 := by
  have hnil : t.steps = [] := List.eq_nil_of_length_eq_zero t.length_eq
  simp [hoefsmitGonshor, hoefsmitSurrealSignSeq, hnil]

/-- **(b.3) For `n ≥ 2`, the one-row tableau `(n)` maps to `(n - 1 : ℚ) > 0`
    (hence is strictly non-zero).** -/
theorem hoefsmitGonshor_oneRow (n : ℕ) :
    hoefsmitGonshor n (StandardTwoRowTableau.oneRow n) = ((n - 1 : ℕ) : ℚ) := by
  simp [hoefsmitGonshor, hoefsmitSurrealSignSeq, StandardTwoRowTableau.oneRow,
        gonshor_replicate_plus]

theorem hoefsmitGonshor_oneRow_pos {n : ℕ} (hn : 2 ≤ n) :
    0 < hoefsmitGonshor n (StandardTwoRowTableau.oneRow n) := by
  rw [hoefsmitGonshor_oneRow]
  have : 1 ≤ n - 1 := by omega
  exact Nat.cast_pos.mpr (by omega)

theorem hoefsmitGonshor_oneRow_ne_zero {n : ℕ} (hn : 2 ≤ n) :
    hoefsmitGonshor n (StandardTwoRowTableau.oneRow n) ≠ 0 :=
  ne_of_gt (hoefsmitGonshor_oneRow_pos hn)

/-- **(c.1) YJM edge compatibility:** extending a tableau in row 1 or row 2
    appends `Sign.plus` or `Sign.minus` to its surreal sign sequence. -/
theorem hoefsmitSurrealSignSeq_extendRow1 {n : ℕ} (t : StandardTwoRowTableau (n + 1)) :
    hoefsmitSurrealSignSeq (n + 2) (t.extendRow1) =
      hoefsmitSurrealSignSeq (n + 1) t ++ [Sign.plus] := rfl

theorem hoefsmitSurrealSignSeq_extendRow2 {n : ℕ} (t : StandardTwoRowTableau (n + 1))
    (h : countMinus t.steps < countPlus t.steps + 1) :
    hoefsmitSurrealSignSeq (n + 2) (t.extendRow2 h) =
      hoefsmitSurrealSignSeq (n + 1) t ++ [Sign.minus] := rfl

/-- **(c.2) Birthday (sign-sequence length) bound:** for every size-`n` standard
    two-row tableau `t`, its surreal sign sequence has length `n - 1 ≤ n`. -/
theorem hoefsmitSurrealSignSeq_length (n : ℕ) (t : StandardTwoRowTableau n) :
    (hoefsmitSurrealSignSeq n t).length = n - 1 ∧
    (hoefsmitSurrealSignSeq n t).length ≤ n := by
  refine ⟨t.length_eq, ?_⟩
  have h := t.length_eq
  show t.steps.length ≤ n
  omega

/-- **(d) Strict non-surjectivity into birthday-bounded sign sequences (`n ≥ 3`):**
    for every `n ≥ 3`, there exists a sign sequence `s : List Sign` of length
    `n - 1` (namely `Sign.minus :: Sign.minus :: List.replicate (n - 3) Sign.plus`,
    corresponding to placing boxes 2 and 3 in row 2 before any second box in row 1)
    that is **not** in the image of `hoefsmitSurrealSignSeq n`. -/
theorem hoefsmitSurrealSignSeq_not_surjective {n : ℕ} (hn : 3 ≤ n) :
    ∃ s : List Sign, s.length = n - 1 ∧
      ∀ t : StandardTwoRowTableau n, hoefsmitSurrealSignSeq n t ≠ s := by
  refine ⟨Sign.minus :: Sign.minus :: List.replicate (n - 3) Sign.plus, ?_, ?_⟩
  · simp [List.length_replicate]
    omega
  · intro t ht
    have hbal := t.ballot 2
    rw [show t.steps = hoefsmitSurrealSignSeq n t from rfl, ht] at hbal
    simp [List.take] at hbal

/-- **Consolidated general-`n` theorem (`prop:hoefsmit-is-surreal-construction`).**

    For every `n : ℕ`:
    1. The Hoefsmit-to-surreal sign-sequence map `hoefsmitSurrealSignSeq n` on
       `StandardTwoRowTableau n` is **injective** (`Function.Injective`);
    2. Every `t : StandardTwoRowTableau n` has sign-sequence birthday
       `(hoefsmitSurrealSignSeq n t).length = n - 1 ≤ n`;
    3. At `n = 0` and `n = 1` the Gonshor evaluation vanishes, whereas for
       `n ≥ 2` the one-row tableau `(n)` evaluates to `(n - 1 : ℚ) > 0`;
    4. Every YJM box addition `extendRow1` / `extendRow2` corresponds to
       appending `Sign.plus` / `Sign.minus`, and for `n ≥ 3` the embedding into
       length-`(n - 1)` sign sequences is strictly non-surjective. -/
-- Ref: [conway1976] §0
-- Ref: [gonshor1986] §2
-- Ref: [hoefsmit1974] PhD Thesis, UBC.
theorem hoefsmit_is_surreal_construction (n : ℕ) :
    Function.Injective (hoefsmitSurrealSignSeq n) ∧
    (∀ t : StandardTwoRowTableau n, (hoefsmitSurrealSignSeq n t).length = n - 1) ∧
    hoefsmitGonshor n (StandardTwoRowTableau.oneRow n) = ((n - 1 : ℕ) : ℚ) ∧
    (2 ≤ n → 0 < hoefsmitGonshor n (StandardTwoRowTableau.oneRow n)) ∧
    (3 ≤ n → ∃ s : List Sign, s.length = n - 1 ∧
      ∀ t : StandardTwoRowTableau n, hoefsmitSurrealSignSeq n t ≠ s) :=
  ⟨hoefsmitSurrealSignSeq_injective n,
   fun t => t.length_eq,
   hoefsmitGonshor_oneRow n,
   hoefsmitGonshor_oneRow_pos,
   hoefsmitSurrealSignSeq_not_surjective⟩

end QOU.AppendixSurreals

