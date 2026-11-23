import QOU.MassTheory.FlipSymmetryAtOne

/-!
# The q = 1 input of `FlipSymmetryAtOne`, proved

`FlipSymmetryAtOne` proves that mirror blocks of `(hol − 1)^k` have equal trace when `hol` is a
product of strand-permutation matrices, and states (without proof) that at `q = 1` every braid
word acts that way and the `T³` term of the jet derivative drops out. This file proves that input.

Over any commutative ring `R`, with `h` standing for `q − q⁻¹` and `qi` for `q⁻¹` (both carried as
parameters, so no inverse is needed):

* `gen q h i j` is the Hecke R-matrix on strands `i, j`, column action on the bits `(t i, t j)`
  (`false = 0`, `true = 1`): `|00⟩ ↦ q|00⟩`, `|01⟩ ↦ |10⟩`, `|10⟩ ↦ |01⟩ + h|10⟩`,
  `|11⟩ ↦ q|11⟩`; the inverse letter is `gen q h i j − h • 1`.
* `gen_one`: `gen 1 0 i j = permMat (Equiv.swap i j)`, in the convention of `permMat`
  (`P s t = 1` iff `s = t ∘ π`), with no adjustment; `invLetter_one`: the inverse letter is the
  same matrix.
* `jetD qi hol T3 = qi • (hol − 1) + (1 − qi) • T3` is `𝒟 = (hol − 1)/q + (1 − q⁻¹)·T³`;
  `jetD_one`: at `qi = 1` it is `hol − 1` for every `T3`.
* `blockTr_jetD_pow_word_at_one`: for every braid word (a list of adjacent-generator indices with
  a sign bit), the mirror blocks of `𝒟^k` at `q = 1` have equal trace.
-/

namespace QOU.MassTheory.FlipSymmetryAtOne

open Matrix

variable {n : ℕ} {R : Type*} [CommRing R]

/-- The Hecke generator on strands `i, j` at parameter `q`, with `h = q − q⁻¹`. Entry `(s, t)` is
the coefficient of `|s⟩` in the image of `|t⟩`. -/
def gen (q h : R) (i j : Fin n) : Matrix (St n) (St n) R := fun s t =>
  if t i = t j then (if s = t then q else 0)
  else if t i = false then (if s = t ∘ Equiv.swap i j then 1 else 0)
  else (if s = t ∘ Equiv.swap i j then 1 else 0) + (if s = t then h else 0)

lemma comp_swap_of_eq {i j : Fin n} {t : St n} (h : t i = t j) : t ∘ Equiv.swap i j = t := by
  funext k
  simp only [Function.comp]
  rcases eq_or_ne k i with rfl | hki
  · simp [h]
  rcases eq_or_ne k j with rfl | hkj
  · simp [h]
  rw [Equiv.swap_apply_of_ne_of_ne hki hkj]

/-- At `q = 1`, `h = 0` the generator is the strand swap. -/
theorem gen_one (i j : Fin n) : gen (1 : R) 0 i j = permMat (Equiv.swap i j) := by
  funext s t
  unfold gen permMat
  by_cases hij : t i = t j
  · rw [if_pos hij, comp_swap_of_eq hij]
  · rw [if_neg hij]
    split_ifs <;> simp

/-- At `q = 1`, `h = 0` the inverse letter `σ − h·1` is the same swap. -/
theorem invLetter_one (i j : Fin n) :
    gen (1 : R) 0 i j - (0 : R) • (1 : Matrix (St n) (St n) R) = permMat (Equiv.swap i j) := by
  rw [zero_smul, sub_zero, gen_one]

/-- Lower strand of the adjacent generator `σ_i`, `i : Fin (n - 1)`. -/
def loStrand (i : Fin (n - 1)) : Fin n := ⟨i.val, by have := i.isLt; omega⟩

/-- Upper strand of the adjacent generator `σ_i`. -/
def hiStrand (i : Fin (n - 1)) : Fin n := ⟨i.val + 1, by have := i.isLt; omega⟩

/-- A letter of a braid word: generator index and sign (`true` = `σ_i`, `false` = `σ_i⁻¹`). -/
def letter (q h : R) (l : Fin (n - 1) × Bool) : Matrix (St n) (St n) R :=
  if l.2 then gen q h (loStrand l.1) (hiStrand l.1)
  else gen q h (loStrand l.1) (hiStrand l.1) - h • (1 : Matrix (St n) (St n) R)

/-- The strand permutation a letter becomes at `q = 1`. -/
def swapOf (l : Fin (n - 1) × Bool) : Equiv.Perm (Fin n) :=
  Equiv.swap (loStrand l.1) (hiStrand l.1)

theorem letter_one (l : Fin (n - 1) × Bool) :
    letter (1 : R) 0 l = permMat (swapOf l) := by
  unfold letter swapOf
  cases l.2
  · simpa using invLetter_one (R := R) (loStrand l.1) (hiStrand l.1)
  · simpa using gen_one (R := R) (loStrand l.1) (hiStrand l.1)

/-- The holonomy of a braid word. -/
def holWord (q h : R) (w : List (Fin (n - 1) × Bool)) : Matrix (St n) (St n) R :=
  (w.map (letter q h)).prod

/-- At `q = 1` every braid word is a product of strand-permutation matrices. -/
theorem holWord_one (w : List (Fin (n - 1) × Bool)) :
    holWord (1 : R) 0 w = ((w.map swapOf).map (permMat (R := R))).prod := by
  induction w with
  | nil => simp [holWord]
  | cons l w ih =>
    simp only [holWord, List.map_cons, List.prod_cons] at ih ⊢
    rw [ih, letter_one]

/-- The jet derivative `𝒟 = (hol − 1)/q + (1 − q⁻¹)·T³`, with `qi = q⁻¹`. -/
def jetD (qi : R) (hol T3 : Matrix (St n) (St n) R) : Matrix (St n) (St n) R :=
  qi • (hol - 1) + (1 - qi) • T3

/-- At `q = 1` the `T³` coefficient vanishes. -/
theorem jetD_one (hol T3 : Matrix (St n) (St n) R) : jetD (1 : R) hol T3 = hol - 1 := by
  simp [jetD]

/-- **n − p = 0 at q = 1 for every braid word.** For any word `w`, any `T3`, any `k`, the mirror
blocks of `𝒟^k` at `q = 1` have equal trace. -/
theorem blockTr_jetD_pow_word_at_one (w : List (Fin (n - 1) × Bool))
    (T3 : Matrix (St n) (St n) R) (k : ℕ) {m : ℕ} (hm : m ≤ n) :
    blockTr (jetD (1 : R) (holWord 1 0 w) T3 ^ k) m
      = blockTr (jetD (1 : R) (holWord 1 0 w) T3 ^ k) (n - m) := by
  rw [jetD_one, holWord_one]
  exact blockTr_hol_sub_one_pow _ k hm

end QOU.MassTheory.FlipSymmetryAtOne
