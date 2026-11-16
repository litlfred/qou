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

🛑 **`Letter` has three constructors, and the corpus has four templates.**
`word_to_mpfr` also recognises `averaged_weighted`, carrying the substrate
flavour split `δ(q) = (q−1)²(1 − q⁻⁴)/3` and the shift `d = −h(1/2 − δ/4)`. No
census reading uses it, so nothing stated here is weakened — but the 2026-08-15
owner ruling R3 makes `bring_color_weighted` canonical as the p/n convention,
so a word built *next* may carry it. It is deliberately absent from `Letter`
because the argument does not extend: its character carries an irreducible
sextic rather than a power of `q` or of `(q²+1)/2`, so `ud_mul_ne_one`'s
finite case analysis has no analogue and the unique-factorisation route is
unavailable. The companion probe measures the sixteen four-letter pairings and
records that **the general word-level exclusion over the four-letter alphabet
is open**; adding a fourth constructor here without that argument would state
less than it appears to.

## What is NOT new here

`qou-avt6` (completed 2026-08-26) already derives the monomial shape
`eps(word) = q^m ([2]_q/2)^c` — for the **counit / trivial** representation
`σ ↦ q`, not for the alternating one used here, and without stating the
order-blindness or drawing its consequence for the γγ ruling's choice of
ordering. The two shapes agree up to a fold, `(q²+1)/(2q) = [2]_q/2`.

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

/-! ## What the γγ ruling leaves free on three strands

The exclusion below says no census reading is γγ-produced. The natural next
question is what a γγ-*derived* word could be instead — and on three strands
the answer is that there is almost nothing to choose. `H₃(q)` has two Artin
generators, so a vertex `σᵢσᵢ₊₁⁻¹` needs `i + 1 < 2`, i.e. `i = 0`: the only
pair-production vertex available is `σ₀σ₁⁻¹`, and every γγ word is one of its
powers. The γγ-admissible subset of `H₃` is a **cyclic monoid on one
generator**, with a single integer of freedom. -/

/-- The word built from a list of vertex indices: `vertexWord [i, j, k]` is
`vertex i ++ vertex j ++ vertex k`. -/
def vertexWord : List ℕ → Word
  | [] => []
  | i :: is => vertex i ++ vertexWord is

/-- **γγ words are exactly the free monoid on the vertices.** The content of
`GammaGammaWord` is that a word carries an index list and nothing else; the
strand count then bounds which indices are available, and every collapse below
is a corollary of that bound rather than of anything about `H_n`. -/
theorem gammaGamma_iff_vertexWord {w : Word} :
    GammaGammaWord w ↔ ∃ is : List ℕ, w = vertexWord is := by
  constructor
  · intro h
    induction h with
    | nil => exact ⟨[], rfl⟩
    | @cons i w' _ ih =>
      obtain ⟨is, his⟩ := ih
      exact ⟨i :: is, by simp [vertexWord, his]⟩
  · rintro ⟨is, rfl⟩
    induction is with
    | nil => exact .nil
    | cons i _ ih => exact .cons i ih

/-- **On `n` strands there are `n − 2` vertices available**, because `vertex i`
occupies generators `i` and `i + 1` and the Artin generators are `σ₀ … σ_{n−2}`.
Stated as the bound that is actually used: if every crossing of a γγ word lies
below generator `m`, every vertex index lies below `m − 1`. -/
theorem gammaGamma_index_lt {w : Word} {m : ℕ} (h : GammaGammaWord w)
    (hw : ∀ c ∈ w, c.gen < m) :
    ∃ is : List ℕ, w = vertexWord is ∧ ∀ i ∈ is, i + 1 < m := by
  induction h with
  | nil => exact ⟨[], rfl, by simp⟩
  | @cons i w' _ ih =>
    have hi : i + 1 < m := hw ⟨i + 1, false⟩ (by simp [vertex])
    obtain ⟨is, his, hb⟩ := ih fun c hc => hw c (by simp [vertex, hc])
    refine ⟨i :: is, by simp [vertexWord, his], ?_⟩
    intro j hj
    rcases List.mem_cons.mp hj with rfl | hj
    · exact hi
    · exact hb j hj

/-- `(σ₀σ₁⁻¹)^k`, the only shape a γγ word can take on three strands. `k = 3`
is `borromean`. -/
def coreWord : ℕ → Word
  | 0 => []
  | k + 1 => vertex 0 ++ coreWord k

theorem coreWord_eq_vertexWord : ∀ k, coreWord k = vertexWord (List.replicate k 0)
  | 0 => rfl
  | k + 1 => by
    simp [coreWord, List.replicate_succ, vertexWord, coreWord_eq_vertexWord k]

theorem coreWord_gammaGamma : ∀ k, GammaGammaWord (coreWord k)
  | 0 => .nil
  | k + 1 => .cons 0 (coreWord_gammaGamma k)

theorem coreWord_length : ∀ k, (coreWord k).length = 2 * k
  | 0 => rfl
  | k + 1 => by
    simp only [coreWord, length_vertex_append, coreWord_length k]
    ring

/-- Every crossing of `coreWord k` lives on generator `0` or `1`. -/
theorem coreWord_gen_lt_two : ∀ k, ∀ c ∈ coreWord k, c.gen < 2
  | 0 => by simp [coreWord]
  | k + 1 => by
    intro c hc
    simp only [coreWord, vertex, List.cons_append, List.nil_append,
      List.mem_cons] at hc
    rcases hc with rfl | rfl | hc
    · norm_num
    · norm_num
    · exact coreWord_gen_lt_two k c hc

/-- **On three strands there is only one γγ word per length.** A γγ-produced
word all of whose crossings lie on the two Artin generators of `H₃` is exactly
`(σ₀σ₁⁻¹)^k`. So the γγ ruling, applied inside `H₃`, leaves a single natural
number of freedom — not a space of orderings, and not a choice of letters. -/
theorem gammaGamma_threeStrand {w : Word} (h : GammaGammaWord w)
    (hw : ∀ c ∈ w, c.gen < 2) : ∃ k, w = coreWord k := by
  induction h with
  | nil => exact ⟨0, rfl⟩
  | @cons i w' _ ih =>
    have hi : i + 1 < 2 := hw ⟨i + 1, false⟩ (by simp [vertex])
    have hi0 : i = 0 := by omega
    subst hi0
    obtain ⟨k, hk⟩ := ih fun c hc => hw c (by simp [vertex, hc])
    exact ⟨k + 1, by simp [coreWord, hk]⟩

/-- Corollary: a γγ word on three strands has even length `2k`, so the corpus's
eleven-letter nucleon cannot be one — and neither can any word of odd length,
whatever its letters. -/
theorem gammaGamma_threeStrand_length_eq {w : Word} (h : GammaGammaWord w)
    (hw : ∀ c ∈ w, c.gen < 2) : ∃ k, w.length = 2 * k := by
  obtain ⟨k, rfl⟩ := gammaGamma_threeStrand h hw
  exact ⟨k, coreWord_length k⟩

/-- **Four strands: two vertices, and the collapse stops.** On `H₄` the indices
available are `0` and `1`, so a γγ word carries an arbitrary binary list and the
one-integer argument of `gammaGamma_threeStrand` does not apply. This is stated
rather than proved-nontrivial on purpose: it is the *negation* of a collapse,
and what it buys is that the `H₃` result must not be quoted for `H₄`. -/
theorem gammaGamma_fourStrand_indices {w : Word} (h : GammaGammaWord w)
    (hw : ∀ c ∈ w, c.gen < 3) :
    ∃ is : List ℕ, w = vertexWord is ∧ ∀ i ∈ is, i = 0 ∨ i = 1 := by
  obtain ⟨is, hw', hb⟩ := gammaGamma_index_lt h hw
  exact ⟨is, hw', fun i hi => by have := hb i hi; omega⟩

/-- Both four-strand vertices really are γγ words, so the index set above is
inhabited at both values and `gammaGamma_fourStrand_indices` is not vacuous. -/
theorem vertex_one_gammaGamma : GammaGammaWord (vertex 1) :=
  gammaGamma_iff_vertexWord.mpr ⟨[1], by simp [vertexWord]⟩

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

/-! ### Sign parity — the character's sign is `(−1)^{length}`, for EVERY word

The two theorems immediately below (`protonWord_char_neg`, `neutronWord_char_neg`)
each prove negativity for **one** word, by computing that word's closed form.
This section proves the *mechanism*, which is stronger and is what generalises:
every letter of the alphabet has negative character, so the sign of a product of
them is decided by nothing but how many there are.

🛑 **SCOPE — this is a READING-1 statement, and reading 1 is PARKED (corrected
2026-09-14, bean `qou-99qc`).** The theorems below are unaffected; what was
wrong is what they were said to exclude. The corpus enumerates three PSD
readings, and the owner selected **3** on 2026-09-12 (*"try PSD condfinement 3
for now, but keep 1 2 for later"*, bean `qou-ales`):

* **reading 1** — literal `Matrix.PosSemidef` on every Wedderburn block. Parked.
* **reading 2** — symmetric-part PSD. Parked.
* **reading 3** — Frobenius positivity, `χ_λ(w) ≥ 0` on every block with
  `y_λ > 0`. **Selected.**

The 2026-09-13 `(B) whole element` answer moved reading 3's **letter** scope; it
did not change the reading. And under convention D `y_(1³) = 0` — the Ocneanu
weight of every shape with a third row vanishes at `z = q³/(q²+1)`
(`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`, general `n`,
unconditional over any field with `q² + 1 ≠ 0`; at `n = 3` in this variable frame,
`QOU.BraidsAndKnots.FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu`) —
so **reading 3 does not constrain the alternating block at all**, and measured, it admits odd lengths in
quantity (9 and 11 both, both nucleons;
`qbeta_reading3_does_not_constrain_the_budget_probe`, 8/8).

🛑 **This cited `markovWeights_eq_jones_of_threeRow_eq_zero` until 2026-09-26,
and that lemma proves the CONVERSE** (bean `qou-6moa`). Its `hTL : y₁₃ = 0` is a
*hypothesis* and `z * (q + qi) = q ^ 2` is its *conclusion*, so it gives TL ⟹ D —
the direction `docs/coordination/trace-convention-registry.json` correctly cites
it for, and the opposite of what this paragraph needs. It also carries
`hfaith : y₂₁ ≠ 0`, which is load-bearing rather than decorative: the sibling
`markovWeights_degenerate_root` proves that dropping it makes the conclusion
**false** (the `y = (1,0,0)` trivial character at `z = q`). **The reading is
unaffected — only its citation was.**

So what these theorems give is: under **reading 1**, PSD in the one-dimensional
alternating block is just `0 ≤ character`, hence an odd-length word is excluded
outright — whatever its letters, order, or generators. That is not vacuous, it
is *annihilating*: all three nucleon constructions in the tree are odd (9, 11,
11; bean `qou-1qsw`), so reading 1 would empty the selection rather than narrow
it, and a survivor would need an even-length model or a letter with shift
`d ≥ 1/(q² − 1) ≈ 4.31`. Read this section as evidence about reading 1's
viability for this corpus — not as a live exclusion. -/

/-- **Every letter of the alphabet has strictly negative alternating
character**, at every `q > 0`.

Falsifiable and checked at all three constructors rather than asserted: it is
the reason the parity below holds, and it fails the moment a letter with shift
`d ≥ 1/(q² − 1)` is admitted — none of the corpus letters is remotely near that
(`d ∈ {0, −1/2, −1}` against a threshold of `≈ 4.31` at the substrate pin). -/
theorem letterChar_neg (hq : 0 < q) (l : Letter) : letterChar q l < 0 := by
  cases l
  · simp only [letterChar]
    exact neg_lt_zero.mpr (inv_pos.mpr hq)
  · simp only [letterChar]
    exact div_neg_of_neg_of_pos (by nlinarith [sq_nonneg q]) (by linarith)
  · simp only [letterChar]
    exact neg_lt_zero.mpr hq

/-- **The sign of a word's alternating character is `(−1)^{length}`.**

Stated as the two halves at once, because that is what the induction proves:
prepending a letter flips both the parity and the sign together. -/
theorem wordChar_sign (hq : 0 < q) (w : List Letter) :
    (Even w.length → 0 < wordChar q w) ∧ (Odd w.length → wordChar q w < 0) := by
  induction w with
  | nil =>
      refine ⟨fun _ => by simp [wordChar], fun h => ?_⟩
      simp at h
  | cons l t ih =>
      have hl := letterChar_neg hq l
      have hcons : wordChar q (l :: t) = letterChar q l * wordChar q t := by
        simp [wordChar]
      refine ⟨fun he => ?_, fun ho => ?_⟩
      · rw [hcons]
        have ht : Odd t.length := by
          rw [List.length_cons, Nat.even_add_one, Nat.not_even_iff_odd] at he
          exact he
        exact mul_pos_of_neg_of_neg hl (ih.2 ht)
      · rw [hcons]
        have ht : Even t.length := by
          rw [List.length_cons, Nat.odd_add_one, Nat.not_odd_iff_even] at ho
          exact ho
        exact mul_neg_of_neg_of_pos hl (ih.1 ht)

/-- An **odd-length** word has strictly negative alternating character. -/
theorem wordChar_neg_of_odd (hq : 0 < q) {w : List Letter} (h : Odd w.length) :
    wordChar q w < 0 :=
  (wordChar_sign hq w).2 h

/-- An **even-length** word has strictly positive alternating character. -/
theorem wordChar_pos_of_even (hq : 0 < q) {w : List Letter} (h : Even w.length) :
    0 < wordChar q w :=
  (wordChar_sign hq w).1 h

/-- **The headline: no 11-letter word can be PSD in the alternating block.**

The alternating block is one-dimensional, so `Matrix.PosSemidef` there is
exactly `0 ≤ wordChar`. Eleven is odd, so the character is strictly negative —
for every assignment of letters, every ordering, every generator labelling.

🛑 **Under READING 1 only** (see the section note above; reading 3 is the live
one and does not constrain this block). Within reading 1 it is a **scope-(b)
structural exclusion** of the entire 11-crossing nucleon construction, with the
invariant named: the sign of the alternating character. It is independent of
which letters carry the proton/neutron asymmetry, so no choice among them can
repair it — which is why it excludes *every* corpus nucleon model rather than
selecting among them. -/
theorem no_eleven_letter_word_is_alt_psd (hq : 0 < q) {w : List Letter}
    (h : w.length = 11) : wordChar q w < 0 := by
  refine wordChar_neg_of_odd hq ?_
  rw [h]
  decide

/-- The companion positive statement, recorded so the exclusion above is not
mistaken for "the character is always negative": at **even** length it is always
positive, so the parity is a real discriminator rather than a blanket sign.
Together with `GammaGammaWordSelection.altChar_eq_one` (every γγ word has
character `1 > 0`) this is consistent — γγ words have even length. -/
theorem alt_psd_iff_even (hq : 0 < q) (w : List Letter) :
    0 < wordChar q w ↔ Even w.length := by
  refine ⟨fun hpos => ?_, wordChar_pos_of_even hq⟩
  by_contra hodd
  rw [Nat.not_even_iff_odd] at hodd
  exact absurd hpos (not_lt.mpr (wordChar_neg_of_odd hq hodd).le)

/-! ### Where the obstruction LIVES: the crossing budget, block by block

The corpus builds a nucleon as `B₃ core · quark block · gluon dressing`, with
the core `(σ₀σ₁⁻¹)³` at **6** letters and the quark block at **3**. Six is
even and three is odd, so by the parity above the admissibility of the whole
word is decided by **one** thing: whether the gluon dressing has odd length.

That localises a question the corpus has argued over repeatedly. The live
`pyhecke.atom.nucleon_word_letters` emits **11** (6 + 3 + 2);
`build_nucleon_nf` emits **9** (6 + 3, its docstring saying "B₃ IS the gluon
structure"). Those two differ by **2**, so they have the *same* parity and the
9-vs-11 question cannot bear on this at all. -/

/-- **The gluon dressing must have ODD length.**

Given an even-length core and an odd-length quark block — which is what the
corpus construction supplies — the assembled word is admissible in the
alternating block exactly when the gluon dressing is odd.

This is the crossing-budget statement *as reading 1 sees it*: it does not name a
number, it fixes a parity, and every gluon count the corpus has proposed (2, and
the retracted 4) is even and therefore fails it.

🛑 **It has no force under the live reading 3** (section note above). Measured
across every generator assignment and every dressing over the alphabet, reading
3 admits *every* count `k = 0…3` for both nucleons — 4/8, 18/48, 149/288,
594/1728 for the proton — so there is no parity signal and no monotone in `k`.
**Reading 3 does not decide the crossing budget.** Keep this theorem for the
parked reading, and do not cite it as excluding a corpus gluon count today. -/
theorem gluon_dressing_must_be_odd (hq : 0 < q) (core quark gluon : List Letter)
    (hc : Even core.length) (hk : Odd quark.length) :
    0 < wordChar q (core ++ quark ++ gluon) ↔ Odd gluon.length := by
  rw [alt_psd_iff_even hq]
  simp only [List.append_assoc, List.length_append]
  rw [Nat.even_iff] at hc
  rw [Nat.odd_iff] at hk
  rw [Nat.even_iff, Nat.odd_iff]
  omega

/-- **An even-length dressing can never repair an inadmissible word.**

This closes the obvious repair route. Given the result above, the natural move
is to add structure until the parity comes right — and the structure the ruling
supplies is γγ pair-production, whose words are **even** by
`GammaGammaWordSelection.length_even`. Appending an even-length dressing
preserves the parity, so it preserves inadmissibility.

So a nucleon that fails here cannot be fixed by adding γγ vertices, however
many. Whatever supplies the missing odd letter is by that very fact **not**
γγ-produced — which is the same boundary the parity bound already draws around
the quark block, arrived at from the other side. -/
theorem even_dressing_cannot_repair (hq : 0 < q) (base dressing : List Letter)
    (hd : Even dressing.length) (hbase : ¬ (0 < wordChar q base)) :
    ¬ (0 < wordChar q (base ++ dressing)) := by
  rw [alt_psd_iff_even hq] at hbase ⊢
  simp only [List.length_append]
  rw [Nat.even_iff] at hd
  rw [Nat.even_iff] at hbase ⊢
  omega

/-- **Neither of the corpus's two crossing budgets is admissible**, and they
fail for the same reason: `6 + 3 + 2 = 11` and `6 + 3 = 9` are both odd.

Stated on the lengths alone, so it is checkable without reference to any
particular letters. The point is the one the 9-vs-11 argument keeps missing:
those two budgets differ by 2, so no choice between them changes the parity. -/
theorem both_corpus_budgets_are_odd :
    ¬ Even (6 + 3 + 2) ∧ ¬ Even (6 + 3) := by
  constructor <;> decide

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

/-! ### Four-letter alphabet extension: the colour-weighted letter `averaged_weighted` (`qou-efqx`)

Under owner ruling R3 (`bring_color_weighted`), the p–n interface uses a fourth crossing template
with shift `d_cw = -h(1/2 - δ(q)/4)` where `δ(q) = (q - 1)²(1 - q⁻⁴)/3`. Its alternating character
`altCharCw q = -q⁻¹ + d_cw` rationalizes to `(q² + 1)(q⁶ - 2q⁵ - 7q⁴ + 4q³ - q² - 2q + 1)/(12q⁵)`,
carrying an irreducible sextic factor. While unique monomial factorization does not apply to the
sextic, on the physical regime `1 < q` with `0 < δ(q) < 2` (at `q₀`, `δ(q₀) ≈ 0.0013757`),
`altCharCw q` is strictly sandwiched between `letterChar q .ud` (`-(q²+1)/(2q)`) and
`letterChar q .uu` (`-q⁻¹`), hence strictly negative, and its pairings with `.uu` and with itself
remain strictly below `1` whenever `-1 < altCharCw q < 0`. -/

/-- The leading flavour-split rational function `δ(q) = (q - 1)²(1 - q⁻⁴)/3`. -/
noncomputable def flavorSplitLeading (q : ℝ) : ℝ :=
  (q - 1) ^ 2 * (1 - (q⁻¹) ^ 4) / 3

/-- Alternating character of the fourth (`averaged_weighted`) letter template:
`altCharCw q = -q⁻¹ - (q - q⁻¹)(1/2 - δ(q)/4)`. -/
noncomputable def altCharCw (q : ℝ) : ℝ :=
  -q⁻¹ - (q - q⁻¹) * (1 / 2 - flavorSplitLeading q / 4)

/-- Exact sextic rational closed form of the colour-weighted alternating character (`qou-efqx`):
`altCharCw q = (q² + 1)(q⁶ - 2q⁵ - 7q⁴ + 4q³ - q² - 2q + 1) / (12 q⁵)`. -/
theorem altCharCw_sextic_closed_form (hq : q ≠ 0) :
    altCharCw q =
      (q ^ 2 + 1) * (q ^ 6 - 2 * q ^ 5 - 7 * q ^ 4 + 4 * q ^ 3 - q ^ 2 - 2 * q + 1) /
        (12 * q ^ 5) := by
  unfold altCharCw flavorSplitLeading
  field_simp
  ring

/-- Exact difference between `altCharCw q` and the `.ud` letter character `-(q² + 1)/(2q)`. -/
theorem altCharCw_sub_ud (hq : q ≠ 0) :
    altCharCw q - letterChar q .ud = (q - q⁻¹) * (flavorSplitLeading q / 4) := by
  unfold altCharCw letterChar
  field_simp
  ring

/-- Exact difference between the `.uu` letter character `-q⁻¹` and `altCharCw q`. -/
theorem uu_sub_altCharCw :
    letterChar q .uu - altCharCw q = (q - q⁻¹) * (1 / 2 - flavorSplitLeading q / 4) := by
  unfold altCharCw letterChar
  ring

/-- **Strict sandwich on the physical band (`qou-efqx`):** For `1 < q` with `0 < δ(q) < 2`,
the colour-weighted letter character lies strictly between `.ud` and `.uu` and is strictly
negative: `letterChar q .ud < altCharCw q < letterChar q .uu < 0`. -/
theorem altCharCw_strict_sandwich (hq1 : 1 < q)
    (hd_pos : 0 < flavorSplitLeading q) (hd_lt : flavorSplitLeading q < 2) :
    letterChar q .ud < altCharCw q ∧ altCharCw q < letterChar q .uu ∧ altCharCw q < 0 := by
  have hq0 : 0 < q := by linarith
  have hqne : q ≠ 0 := hq0.ne'
  have hh_eq : q - q⁻¹ = (q - 1) * (q + 1) / q := by
    field_simp
    ring
  have hh_pos : 0 < q - q⁻¹ := by
    rw [hh_eq]
    exact div_pos (mul_pos (by linarith) (by linarith)) hq0
  have hdiff_ud : 0 < altCharCw q - letterChar q .ud := by
    rw [altCharCw_sub_ud hqne]
    exact mul_pos hh_pos (by linarith)
  have hdiff_uu : 0 < letterChar q .uu - altCharCw q := by
    rw [uu_sub_altCharCw]
    exact mul_pos hh_pos (by linarith)
  have huu_neg : letterChar q .uu < 0 := by
    unfold letterChar
    linarith
  refine ⟨by linarith, by linarith, by linarith⟩

end Real

end QOU.Mass.AltCharShiftMultiset

