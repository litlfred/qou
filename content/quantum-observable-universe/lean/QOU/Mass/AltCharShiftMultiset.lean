/-
# The alternating character is blind to ordering — so no re-ordering of a
# corpus nucleon word is γγ-produced

Bean `qou-99qc`. Companion to
`computations/qbeta/qbeta_altchar_is_a_shift_multiset_invariant_probe.py`,
which measures the same statements symbolically over `ℚ(q)`.

## The question this settles

The owner ruling of 2026-09-08 (`qou-ales`) says every canonical braid word is
selected through γγ pair-production and the confinement SDP, never by census;
R2 of that ruling applied it to pick the nucleon **ordering**.
`QOU.Mass.GammaGammaWordSelection.altChar_eq_one` (sorry-free) fixes the
alternating character `σᵢ ↦ −q⁻¹` at `1` on every γγ-produced word.

The alternating character is a **one-dimensional representation**, so on a word
it is a product of scalars — and a product of scalars does not depend on the
order of its factors, nor on which Artin generator each factor came from. Hence
the two choices the corpus has argued over (generator assignment, ordering) are
exactly the two things this invariant cannot see, and a single computation
decides the whole census at once.

## What is proved (all sorry-free, none tautological)

* `altChar_regen` — re-assigning every crossing of a braid word to a different
  generator leaves `altChar` unchanged. Generator blindness, in the existing
  `Crossing` model.
* `wordChar_of_perm` — the character of a *shifted-letter* word depends only on
  the multiset of its letters. Ordering blindness.
* `letterChar_eq_shift` — the three letter characters are exactly `S + d` for
  the corpus's three shifts `d ∈ {0, −h/2, −h}` with `S = −q⁻¹`, `h = q − q⁻¹`.
  This is what ties the model below to the corpus rather than to an invented
  constant; without it the rest would be about nothing.
* `core_char` — the three-vertex core `(σ₀σ₁⁻¹)³` has character `1`. The
  positive control: a model that could not see a γγ word would be vacuous.
* `protonWord_char` / `neutronWord_char` — the closed forms
  `−(q²+1)²/(4q⁵)` and `−(q²+1)²/(4q³)`.
* `ud_mul_ne_one` — **the obstruction, isolated.** For `0 < q`, `q ≠ 1`, the
  mixed letter's character multiplies with *no* letter of the alphabet
  (itself included) to give `1`. Every corpus nucleon carries exactly two of
  these letters.
* `protonWord_ne_one` / `neutronWord_ne_one` and
  `perm_protonWord_ne_one` / `perm_neutronWord_ne_one` — **the headline**: no
  re-ordering of either nucleon word has character `1`, hence none is a
  γγ-produced word.

## Scope

Scope-(b) exclusion with the invariant named: the alternating character. It
excludes each word from being a **pure γγ word** (a product of vertices). It
says nothing about a word built from γγ vertices *plus* other letters, and
`wordChar = 1` is **necessary, not sufficient** — being a product of vertices
is a statement about the order, which this invariant is deliberately blind to.

## Base ring (§7c)

`Letter` and `wordChar` are stated over a generic `[Field R] [CharZero R]` —
`CharZero` only so that `2 ≠ 0` for the `−h/2` shift; no ordering, no `Real`.
Only the final section, where negativity is used to separate the value from
`1`, specialises to `ℝ`. Nothing here reads AME, CODATA, or a census.
-/
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic
import QOU.Mass.GammaGammaWordSelection

namespace QOU.Mass.AltCharShiftMultiset

open QOU.Mass.GammaGammaWordSelection

/-! ## Generator blindness, in the existing braid-word model -/

/-- **Re-assigning generators does not move the alternating character.**
`altChar` reads `Crossing.pos` and never `Crossing.gen`, so any relabelling
`f : ℕ → ℕ` of the Artin indices leaves it fixed. -/
theorem altChar_regen {R : Type*} [Field R] (q : R) (f : ℕ → ℕ) (w : Word) :
    altChar q (w.map fun c => ⟨f c.gen, c.pos⟩) = altChar q w := by
  simp [altChar, List.map_map, Function.comp_def]

/-! ## Shifted letters -/

/-- The corpus nucleon alphabet: a letter is `σᵢ + d` with the shift `d` drawn
from `{0, −h/2, −h}`, named after the quark pair it encodes (`uu` a positive
crossing, `ud` the mixed pair, `dd` the inverse `σᵢ⁻¹`). The generator index is
deliberately absent — `altChar_regen` above is why that loses nothing. -/
inductive Letter
  | uu
  | ud
  | dd
  deriving DecidableEq, Repr

variable {R : Type*} [Field R] [CharZero R]

/-- The alternating character of a single shifted letter. Since the character
is an algebra hom, `χ(σᵢ + d·1) = χ(σᵢ) + d = −q⁻¹ + d`; `letterChar_eq_shift`
checks that these three values are exactly that, for the three corpus shifts. -/
def letterChar (q : R) : Letter → R
  | .uu => -q⁻¹
  | .ud => -(q ^ 2 + 1) / (2 * q)
  | .dd => -q

/-- The alternating character of a shifted-letter word. -/
def wordChar (q : R) (w : List Letter) : R := (w.map (letterChar q)).prod

/-- **The three letter characters are `S + d` for the corpus shifts**, with
`S = −q⁻¹` and `h = q − q⁻¹`. This is the tie to the corpus; without it the
constants below would be free-floating. -/
theorem letterChar_eq_shift {q : R} (hq : q ≠ 0) :
    letterChar q .uu = -q⁻¹ + 0 ∧
    letterChar q .ud = -q⁻¹ + -(q - q⁻¹) / 2 ∧
    letterChar q .dd = -q⁻¹ + -(q - q⁻¹) := by
  refine ⟨by simp [letterChar], ?_, ?_⟩ <;>
    · simp only [letterChar]
      field_simp
      ring

omit [CharZero R] in
theorem wordChar_nil (q : R) : wordChar q [] = 1 := by simp [wordChar]

omit [CharZero R] in
theorem wordChar_append (q : R) (u v : List Letter) :
    wordChar q (u ++ v) = wordChar q u * wordChar q v := by
  simp [wordChar, List.map_append, List.prod_append]

omit [CharZero R] in
/-- **Ordering blindness.** The character of a shifted-letter word depends only
on the multiset of its letters — it is a product of scalars, and `R` is
commutative. This is the lemma that makes the exclusion below cover every
ordering at once, and so covers whatever ordering the γγ ruling picks. -/
theorem wordChar_of_perm {q : R} {u v : List Letter} (h : u.Perm v) :
    wordChar q u = wordChar q v :=
  (h.map (letterChar q)).prod_eq

omit [CharZero R] in
/-- One γγ vertex, as a pair of shifted letters: `(−q⁻¹)(−q) = 1`. -/
theorem uu_mul_dd {q : R} (hq : q ≠ 0) :
    letterChar q .uu * letterChar q .dd = 1 := by
  simp only [letterChar]
  field_simp

/-! ## The corpus words -/

/-- `β_Bor = (σ₀σ₁⁻¹)³` as shifted letters: three γγ vertices. -/
def core : List Letter := [.uu, .dd, .uu, .dd, .uu, .dd]

/-- `pyhecke.atom.build_atom_nf_exact` for the proton: the core, the `uu ud ud`
quark block, and the two-letter gluon dressing. -/
def protonWord : List Letter := core ++ [.uu, .ud, .ud] ++ [.uu, .uu]

/-- The same for the neutron: quark block `ud ud dd`. -/
def neutronWord : List Letter := core ++ [.ud, .ud, .dd] ++ [.uu, .uu]

omit [CharZero R] in
/-- **Positive control.** The three-vertex core has character `1`, so the model
can see a γγ word. -/
theorem core_char {q : R} (hq : q ≠ 0) : wordChar q core = 1 := by
  simp only [wordChar, core, letterChar, List.map_cons, List.map_nil,
    List.prod_cons, List.prod_nil]
  field_simp

theorem protonWord_char {q : R} (hq : q ≠ 0) :
    wordChar q protonWord = -(q ^ 2 + 1) ^ 2 / (4 * q ^ 5) := by
  simp only [wordChar, protonWord, core, letterChar, List.map_append,
    List.map_cons, List.map_nil, List.prod_append, List.prod_cons,
    List.prod_nil]
  field_simp
  ring

theorem neutronWord_char {q : R} (hq : q ≠ 0) :
    wordChar q neutronWord = -(q ^ 2 + 1) ^ 2 / (4 * q ^ 3) := by
  simp only [wordChar, neutronWord, core, letterChar, List.map_append,
    List.map_cons, List.map_nil, List.prod_append, List.prod_cons,
    List.prod_nil]
  field_simp
  ring

/-! ## The obstruction, and the exclusion -/

section Real

variable {q : ℝ}

/-- `0 < q`, `q ≠ 1` forces `q ^ 2 ≠ 1`. -/
private theorem sq_ne_one (hq : 0 < q) (hq1 : q ≠ 1) : q ^ 2 ≠ 1 := by
  intro h
  have : (q - 1) * (q + 1) = 0 := by nlinarith
  rcases mul_eq_zero.mp this with h' | h'
  · exact hq1 (by linarith)
  · linarith

/-- **The obstruction, isolated.** The mixed letter's character multiplies with
*no* letter of the alphabet — itself included — to give `1`, at any `q > 0`
other than `q = 1`. Every corpus nucleon word carries exactly two of these
letters, so no pairing of them can be absorbed. -/
theorem ud_mul_ne_one (hq : 0 < q) (hq1 : q ≠ 1) (l : Letter) :
    letterChar q .ud * letterChar q l ≠ 1 := by
  have hq0 : q ≠ 0 := hq.ne'
  have hs := sq_ne_one hq hq1
  cases l
  · intro hcon
    simp only [letterChar] at hcon
    field_simp at hcon
    exact hs (by nlinarith)
  · intro hcon
    simp only [letterChar] at hcon
    field_simp at hcon
    exact hs (by nlinarith)
  · intro hcon
    simp only [letterChar] at hcon
    field_simp at hcon
    exact hs (by nlinarith)

theorem protonWord_char_neg (hq : 0 < q) : wordChar q protonWord < 0 := by
  rw [protonWord_char hq.ne']
  apply div_neg_of_neg_of_pos
  · nlinarith [sq_nonneg (q ^ 2 + 1), sq_nonneg q]
  · positivity

theorem neutronWord_char_neg (hq : 0 < q) : wordChar q neutronWord < 0 := by
  rw [neutronWord_char hq.ne']
  apply div_neg_of_neg_of_pos
  · nlinarith [sq_nonneg (q ^ 2 + 1), sq_nonneg q]
  · positivity

/-- The proton word is **not** a γγ-produced word: its alternating character is
strictly negative, and `altChar_eq_one` makes every γγ word's character `1`. -/
theorem protonWord_ne_one (hq : 0 < q) : wordChar q protonWord ≠ 1 := by
  have := protonWord_char_neg hq; linarith

theorem neutronWord_ne_one (hq : 0 < q) : wordChar q neutronWord ≠ 1 := by
  have := neutronWord_char_neg hq; linarith

/-- **The headline.** *No re-ordering* of the proton word has character `1`, so
no ordering of its letters is a γγ-produced word. The γγ ruling picked an
ordering; the invariant cannot see one. -/
theorem perm_protonWord_ne_one {w : List Letter} (hq : 0 < q)
    (h : w.Perm protonWord) : wordChar q w ≠ 1 := by
  rw [wordChar_of_perm h]
  exact protonWord_ne_one hq

theorem perm_neutronWord_ne_one {w : List Letter} (hq : 0 < q)
    (h : w.Perm neutronWord) : wordChar q w ≠ 1 := by
  rw [wordChar_of_perm h]
  exact neutronWord_ne_one hq

/-- The difference of the two characters vanishes only at `q = 1`. If both legs
were γγ-produced their characters would both be `1`, so the difference would be
exactly `0`; it is not, at any `q > 0` with `q ≠ 1`. -/
theorem char_difference_ne_zero (hq : 0 < q) (hq1 : q ≠ 1) :
    wordChar q neutronWord - wordChar q protonWord ≠ 0 := by
  have h0 : q ≠ 0 := hq.ne'
  have hs := sq_ne_one hq hq1
  rw [neutronWord_char h0, protonWord_char h0]
  have key : -(q ^ 2 + 1) ^ 2 / (4 * q ^ 3) - -(q ^ 2 + 1) ^ 2 / (4 * q ^ 5)
      = (q ^ 2 + 1) ^ 2 * (1 - q ^ 2) / (4 * q ^ 5) := by
    field_simp
    ring
  rw [key]
  intro hcon
  apply hs
  rw [div_eq_zero_iff] at hcon
  rcases hcon with h | h
  · rcases mul_eq_zero.mp h with h' | h'
    · exact absurd h' (by positivity)
    · linarith
  · exact absurd h (by positivity)

end Real

end QOU.Mass.AltCharShiftMultiset
