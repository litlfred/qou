/-!
# QOU.BraidKnot.crystal_isospin_degeneracy

Proposition: the crystal-limit shadow-price sum `S_crystal(β)` is
invariant under sign inversion of any subset of generators in the
atomic braid word `β`.

Conditional on `conj:crystal-graph-realization`
(see `QOU.BraidKnot.CrystalGraphRealization`).  Per CLAUDE.md
§3b-cond, this `theorem` lives downstream of a conjecture but
preserves its provable kind by carrying the
`[CrystalSignBlind ℤ]` class hypothesis as an explicit instance.

The instance fields encode:
- `χ : ℕ → ℤ` — the signed-permutation crystal character,
  evaluated on a single generator index `i` (sign-agnostic by
  construction in the implementation `crystal_chi_lambda`);
- `χ_chi_inv` — the conjectural fact that the crystal action of
  `σ_i⁻¹` equals the crystal action of `σ_i` on every SYT
  eigenline (Hecke-skein limit at `q = 0`).

Downstream consequence: any two atomic braid words differing only
by signed-generator inversions evaluate to the same character.

LaTeX label: `prop:crystal-isospin-degeneracy`

References:
- Brundan, J. & Kleshchev, A. (2009).
- Kashiwara, M. (1991). Duke Math. J. 63(2).
- Lecouvey, C. (2007). MSJ Memoirs 17.
-/

import QOU.Basic
import QOU.BraidKnot.CrystalGraphRealization

namespace QOU.BraidKnot

universe u

/-- **A signed braid letter.**  Either `+i` (positive crossing
    `σ_i`, `pos`) or `-i` (negative crossing `σ_i⁻¹`, `neg`). -/
inductive SignedLetter where
  | pos (i : ℕ) : SignedLetter
  | neg (i : ℕ) : SignedLetter
  deriving DecidableEq, Repr

/-- The generator index of a signed letter (the `|i|` of `σ_i^±`). -/
def SignedLetter.idx : SignedLetter → ℕ
  | .pos i => i
  | .neg i => i

/-- Inversion of a signed letter swaps `pos ↔ neg`. -/
def SignedLetter.invert : SignedLetter → SignedLetter
  | .pos i => .neg i
  | .neg i => .pos i

@[simp] lemma SignedLetter.idx_invert (ℓ : SignedLetter) :
    ℓ.invert.idx = ℓ.idx := by
  cases ℓ <;> rfl

/-- A signed braid word is a list of signed letters. -/
abbrev SignedBraidWord : Type := List SignedLetter

/-- Invert a chosen subset of the letters of a word (specified by
    a predicate on positions).  Letters with index `k` such that
    `flip k = true` are inverted; others are unchanged.  Implemented
    via a recursive helper `flipAux` rather than `List.mapIdx` so
    the induction step in `crystal_isospin_degeneracy` proceeds by
    pattern-matching without reasoning about `mapIdx`'s internal
    counter. -/
def SignedBraidWord.flipAux
    (flip : ℕ → Bool) (offset : ℕ)
    : SignedBraidWord → SignedBraidWord
  | []      => []
  | ℓ :: w  =>
      (if flip offset then ℓ.invert else ℓ)
        :: flipAux flip (offset + 1) w

/-- Top-level word-flipping operation. -/
def SignedBraidWord.flipAt
    (flip : ℕ → Bool) (w : SignedBraidWord) : SignedBraidWord :=
  SignedBraidWord.flipAux flip 0 w

/-- **Conjectural class.**  A `CrystalSignBlind R` instance asserts
    that the crystal-limit character `χ` factors through the
    *unsigned* generator index — equivalently, `χ(σ_i) = χ(σ_i⁻¹)`
    for every `i`.  This is the conjectural content of
    `crystal_chi_lambda`'s use of `abs(i)` in the implementation
    `term7_alpha5_crystal_derivation.py`. -/
class CrystalSignBlind (R : Type u) [Ring R] where
  /-- Crystal character on a single signed letter. -/
  charLetter : SignedLetter → R
  /-- Crystal character on a word — the product (or sum, depending
      on convention) of per-letter characters along the word. -/
  charWord : SignedBraidWord → R
  /-- The conjectural input: `χ(pos i) = χ(neg i)`.  Witnessed by
      the `abs(i)` reduction at `q = 0` in
      `term7_alpha5_crystal_derivation.py`. -/
  -- Ref: [kashiwara1991] https://doi.org/10.1215/S0012-7094-91-06321-0
  charLetter_sign_blind :
    ∀ i : ℕ, charLetter (.pos i) = charLetter (.neg i)
  /-- The character on a word is determined by the multiset of
      letters along the word (multiplicativity along generators). -/
  -- Ref: [lecouvey2007] https://doi.org/10.2969/msjmemoirs/01701C040
  charWord_cons :
    ∀ (ℓ : SignedLetter) (w : SignedBraidWord),
      charWord (ℓ :: w) = charLetter ℓ * charWord w

namespace CrystalSignBlind

variable {R : Type u} [Ring R] [C : CrystalSignBlind R]

/-- A flipped letter has the same crystal character as the
    original.  Direct consequence of `charLetter_sign_blind`. -/
-- Ref: [manuscript] braids-and-knots/crystal-isospin-degeneracy
theorem charLetter_invert (ℓ : SignedLetter) :
    C.charLetter ℓ.invert = C.charLetter ℓ := by
  cases ℓ with
  | pos i =>
    simp only [SignedLetter.invert]
    exact (C.charLetter_sign_blind i).symm
  | neg i =>
    simp only [SignedLetter.invert]
    exact C.charLetter_sign_blind i

/-- A flipped letter under any predicate has the same crystal
    character as the original. -/
-- Ref: [manuscript] braids-and-knots/crystal-isospin-degeneracy
theorem charLetter_flipAt (flip : Bool) (ℓ : SignedLetter) :
    C.charLetter (if flip then ℓ.invert else ℓ) = C.charLetter ℓ := by
  cases flip with
  | true => simpa using charLetter_invert ℓ
  | false => rfl

end CrystalSignBlind

/-- **Auxiliary lemma (depth-shifted invariance).**

    Conditional on `[CrystalSignBlind R]`, the crystal character of
    `flipAux flip offset w` equals the crystal character of `w` for
    every offset `offset : ℕ`.  Proof: induction on `w`, using
    `charLetter_flipAt` on the head and `charWord_cons` to factor
    the per-letter contribution. -/
-- Ref: [manuscript] braids-and-knots/crystal-isospin-degeneracy
theorem crystal_isospin_degeneracy_aux
    {R : Type u} [Ring R] [C : CrystalSignBlind R]
    (flip : ℕ → Bool) (offset : ℕ) (w : SignedBraidWord) :
    C.charWord (SignedBraidWord.flipAux flip offset w) = C.charWord w := by
  induction w generalizing offset with
  | nil => rfl
  | cons ℓ tail ih =>
    -- LHS = charWord ((if flip offset then ℓ.invert else ℓ) :: flipAux flip (offset+1) tail)
    --     = charLetter (if … then ℓ.invert else ℓ) * charWord (flipAux flip (offset+1) tail)
    --     = charLetter ℓ * charWord tail   (by charLetter_flipAt and ih)
    --     = charWord (ℓ :: tail)           (by charWord_cons)
    simp only [SignedBraidWord.flipAux, C.charWord_cons,
               CrystalSignBlind.charLetter_flipAt, ih]

/-- **Theorem (crystal isospin degeneracy).**

    Conditional on `[CrystalSignBlind R]`, the crystal character
    `charWord` is invariant under sign-inversion of any subset of
    the letters of the word.  Concretely, for any predicate
    `flip : ℕ → Bool`,

      `charWord (flipAt flip w) = charWord w`.

    Proof: instance of `crystal_isospin_degeneracy_aux` at
    `offset = 0`. -/
-- Ref: [manuscript] braids-and-knots/crystal-isospin-degeneracy
-- Ref: [kashiwara1991] https://doi.org/10.1215/S0012-7094-91-06321-0
theorem crystal_isospin_degeneracy
    {R : Type u} [Ring R] [_C : CrystalSignBlind R]
    (flip : ℕ → Bool) (w : SignedBraidWord) :
    CrystalSignBlind.charWord (R := R)
        (SignedBraidWord.flipAt flip w)
      = CrystalSignBlind.charWord (R := R) w := by
  unfold SignedBraidWord.flipAt
  exact crystal_isospin_degeneracy_aux flip 0 w

/-- **Corollary (T--³He crystal degeneracy).**

    Under `[CrystalSignBlind R]`, two atomic braid words that
    differ only at a single position by `σ_i ↔ σ_i⁻¹` have the
    same crystal character.  Specialised to T (`σ_5⁻¹` at index 4)
    and ³He (`σ_5` at index 4), this gives
    `S_crystal(T) = S_crystal(³He)`.

    Witness:
    `folio-assistant/computations/term7-alpha5-crystal-derivation.witness.json`
    records both at 50 dps as `0.0020612874779541296`. -/
-- Ref: [manuscript] braids-and-knots/crystal-isospin-degeneracy
theorem crystal_T_helium3_degeneracy
    {R : Type u} [Ring R] [_C : CrystalSignBlind R]
    (w_T w_He3 : SignedBraidWord)
    (h_diff : w_He3 = SignedBraidWord.flipAt (fun k => k = 4) w_T) :
    CrystalSignBlind.charWord (R := R) w_He3
      = CrystalSignBlind.charWord (R := R) w_T := by
  rw [h_diff]
  exact crystal_isospin_degeneracy _ _

end QOU.BraidKnot
