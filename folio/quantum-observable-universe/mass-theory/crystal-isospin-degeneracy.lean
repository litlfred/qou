import QOU.Basic
import QOU.BraidKnot.CrystalGraphRealization


/-!
# QOU.BraidKnot.crystal_isospin_degeneracy

Proposition: the crystal-limit shadow-price sum `S_crystal(β)` is
invariant under sign inversion of any subset of generators in the
atomic braid word `β`.

This file axiomatises the **per-SYT-eigenline content** of
`conj:crystal-graph-realization` (Lake-tracked in
`QOU.BraidKnot.CrystalGraphRealization`) into a smaller class
`CrystalEigenlineSignBlind R` that captures only the single fact
this proposition needs — that on every SYT eigenline, the q=0
actions of σ_i and σ_i⁻¹ agree.  Per AGENTS.md §3b-cond, this
`theorem` lives downstream of a conjecture but preserves its
provable kind by carrying `[CrystalEigenlineSignBlind R]` as an
explicit class hypothesis.  The implication
`CrystalGraphRealization R q ⟹ CrystalEigenlineSignBlind R` is
the bridge to the upstream conjecture; the import is preserved so
downstream callers can compose with the full
`CrystalGraphRealization` interface, even though the proofs in
this file use only the smaller `CrystalEigenlineSignBlind` class.

Mathematical clarification: `eigWord` here denotes the *eigenvalue
product on a single SYT eigenline* — it is **not** the irreducible
character `χ^λ`.  The character is the trace
`χ^λ(β) = Σ_{T ∈ SYT(λ)} (eigWord on the line through T)`, which
is *not* multiplicative in `β`.  Multiplicativity holds per
eigenline; the trace inherits sign-flip invariance because each
summand does.

Downstream consequence: any two atomic braid words differing only
by signed-generator inversions evaluate to the same per-eigenline
eigenvalue product, and therefore (by linearity of trace) the same
crystal character.

LaTeX label: `prop:crystal-isospin-degeneracy`

References:
- Brundan, J. & Kleshchev, A. (2009).
- Kashiwara, M. (1991). Duke Math. J. 63(2).
- Lecouvey, C. (2007). MSJ Memoirs 17.
-/

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

/-- **Conjectural class.**  A `CrystalEigenlineSignBlind R` instance
    encodes the **per-SYT-eigenline** action of a single signed
    Hecke letter at the crystal limit `q = 0`.

    For a fixed standard Young tableau `T` of shape `λ`, the
    crystal-limit Hecke generator `σ_i` acts diagonally on the
    SYT-basis eigenline through `T` with eigenvalue
    `eigLetter (.pos i) ∈ R`.  The product of these per-letter
    eigenvalues along a braid word `w` is `eigWord w ∈ R` — the
    *eigenvalue product on the line through `T`*, **not** the
    full irreducible character `χ^λ`, which is the *trace*

      `χ^λ(w) = ∑_{T ∈ SYT(λ)} (eigWord w on the line through T)`.

    The full character is therefore a *sum* of `eigWord` values
    over a finite SYT-basis; multiplicativity holds *per
    eigenline*, not on the trace.

    The conjectural content (per `conj:crystal-graph-realization`):
    on every SYT eigenline, the q→0 actions of `σ_i` and
    `σ_i⁻¹` agree.  This is implemented by the `abs(i)` reduction
    in `term7_alpha5_crystal_derivation.py`.

    Scope (2026-11-16): this field is a modelling choice, not a
    consequence of the Hecke relation `(σ - q)(σ + q⁻¹) = 0`, which
    cannot be specialised at `q = 0`.  In `H_n(q)` the eigenvalues of
    `σ_i` are `q, -q⁻¹` and those of `σ_i⁻¹` are `q⁻¹, -q`.  The
    implication `CrystalGraphRealization ⟹ CrystalEigenlineSignBlind`
    named in the module docstring is not proved anywhere. -/
class CrystalEigenlineSignBlind (R : Type u) [Ring R] where
  /-- Per-eigenline eigenvalue of a single signed letter. -/
  eigLetter : SignedLetter → R
  /-- Per-eigenline eigenvalue product along a word. -/
  eigWord : SignedBraidWord → R
  /-- The empty-word eigenvalue product is the multiplicative
      identity.  Without this axiom `eigWord _ = 0` would
      vacuously satisfy `eigWord_cons`, making the proposition
      trivially provable for the wrong reason. -/
  eigWord_nil : eigWord [] = 1
  /-- The conjectural input: on every SYT eigenline, σ and σ⁻¹
      have the same q=0 eigenvalue. -/
  -- Ref: [kashiwara1991] https://doi.org/10.1215/S0012-7094-91-06321-0
  eigLetter_sign_blind :
    ∀ i : ℕ, eigLetter (.pos i) = eigLetter (.neg i)
  /-- Per-eigenline multiplicativity: applying generators in
      sequence multiplies their eigenvalues on the same SYT line.
      *Note*: this is multiplicativity of *eigenvalues on a fixed
      SYT line*, not of the irreducible character `χ^λ` (which is
      a trace = sum over SYTs and is **not** multiplicative as a
      function of the braid word). -/
  -- Ref: [lecouvey2007] https://doi.org/10.2969/msjmemoirs/01701C040
  eigWord_cons :
    ∀ (ℓ : SignedLetter) (w : SignedBraidWord),
      eigWord (ℓ :: w) = eigLetter ℓ * eigWord w

namespace CrystalEigenlineSignBlind

variable {R : Type u} [Ring R] [C : CrystalEigenlineSignBlind R]

/-- A flipped letter has the same crystal character as the
    original.  Direct consequence of `eigLetter_sign_blind`. -/
-- Ref: [leitner2026] braids-and-knots/crystal-isospin-degeneracy
theorem eigLetter_invert (ℓ : SignedLetter) :
    C.eigLetter ℓ.invert = C.eigLetter ℓ := by
  cases ℓ with
  | pos i =>
    simp only [SignedLetter.invert]
    exact (C.eigLetter_sign_blind i).symm
  | neg i =>
    simp only [SignedLetter.invert]
    exact C.eigLetter_sign_blind i

/-- A flipped letter under any predicate has the same crystal
    character as the original. -/
-- Ref: [leitner2026] braids-and-knots/crystal-isospin-degeneracy
theorem eigLetter_flipAt (flip : Bool) (ℓ : SignedLetter) :
    C.eigLetter (if flip then ℓ.invert else ℓ) = C.eigLetter ℓ := by
  cases flip with
  | true => simpa using eigLetter_invert ℓ
  | false => rfl

end CrystalEigenlineSignBlind

/-- **Auxiliary lemma (depth-shifted invariance).**

    Conditional on `[CrystalEigenlineSignBlind R]`, the crystal character of
    `flipAux flip offset w` equals the crystal character of `w` for
    every offset `offset : ℕ`.  Proof: induction on `w`, using
    `eigLetter_flipAt` on the head and `eigWord_cons` to factor
    the per-letter contribution. -/
-- Ref: [leitner2026] braids-and-knots/crystal-isospin-degeneracy
theorem crystal_isospin_degeneracy_aux
    {R : Type u} [Ring R] [C : CrystalEigenlineSignBlind R]
    (flip : ℕ → Bool) (offset : ℕ) (w : SignedBraidWord) :
    C.eigWord (SignedBraidWord.flipAux flip offset w) = C.eigWord w := by
  induction w generalizing offset with
  | nil => rfl
  | cons ℓ tail ih =>
    -- LHS = eigWord ((if flip offset then ℓ.invert else ℓ) :: flipAux flip (offset+1) tail)
    --     = eigLetter (if … then ℓ.invert else ℓ) * eigWord (flipAux flip (offset+1) tail)
    --     = eigLetter ℓ * eigWord tail   (by eigLetter_flipAt and ih)
    --     = eigWord (ℓ :: tail)           (by eigWord_cons)
    simp only [SignedBraidWord.flipAux, C.eigWord_cons,
               CrystalEigenlineSignBlind.eigLetter_flipAt, ih]

/-- **Theorem (crystal isospin degeneracy).**

    Conditional on `[CrystalEigenlineSignBlind R]`, the crystal character
    `eigWord` is invariant under sign-inversion of any subset of
    the letters of the word.  Concretely, for any predicate
    `flip : ℕ → Bool`,

      `eigWord (flipAt flip w) = eigWord w`.

    Proof: instance of `crystal_isospin_degeneracy_aux` at
    `offset = 0`. -/
-- Ref: [leitner2026] braids-and-knots/crystal-isospin-degeneracy
-- Ref: [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue of universal enveloping algebras," Duke Math. J. 63 (1991)
theorem crystal_isospin_degeneracy
    {R : Type u} [Ring R] [_C : CrystalEigenlineSignBlind R]
    (flip : ℕ → Bool) (w : SignedBraidWord) :
    CrystalEigenlineSignBlind.eigWord (R := R)
        (SignedBraidWord.flipAt flip w)
      = CrystalEigenlineSignBlind.eigWord (R := R) w := by
  unfold SignedBraidWord.flipAt
  exact crystal_isospin_degeneracy_aux flip 0 w

/-- **Corollary (T--³He crystal degeneracy, legacy convention).**

    Under `[CrystalEigenlineSignBlind R]`, two atomic braid words that
    differ only by signed-generator inversions at a finite set
    of positions have the same crystal character.  Specialised
    to the legacy disjoint-product words

      `w_T   = σ_1 σ_2 σ_1⁻¹ σ_4 σ_5⁻¹ σ_4   σ_7 σ_8⁻¹ σ_7`
      `w_He3 = σ_1 σ_2 σ_1⁻¹ σ_4 σ_5   σ_4⁻¹ σ_7 σ_8⁻¹ σ_7`

    they differ at positions 5 and 6 (zero-based indices 4 and 5)
    by paired inversions of `σ_5 ↔ σ_5⁻¹` and `σ_4 ↔ σ_4⁻¹`.
    Therefore `S_crystal(T) = S_crystal(³He)`.

    Witness:
    `computations/term7-alpha5-crystal-derivation.witness.json`
    records both at 50 dps as `0.0020612874779541296`. -/
-- Ref: [leitner2026] braids-and-knots/crystal-isospin-degeneracy
theorem crystal_T_helium3_degeneracy
    {R : Type u} [Ring R] [_C : CrystalEigenlineSignBlind R]
    (w_T w_He3 : SignedBraidWord)
    (h_diff : w_He3 = SignedBraidWord.flipAt
                          (fun k => decide (k = 4 ∨ k = 5)) w_T) :
    CrystalEigenlineSignBlind.eigWord (R := R) w_He3
      = CrystalEigenlineSignBlind.eigWord (R := R) w_T := by
  rw [h_diff]
  exact crystal_isospin_degeneracy _ _

end QOU.BraidKnot
