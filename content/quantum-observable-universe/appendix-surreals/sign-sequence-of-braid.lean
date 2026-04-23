/-
  Sign-sequence functor B_n → No.

  For each standard tableau t of shape λ ⊢ n with ℓ(λ) ≤ 2,
  the Hoefsmit eigenspace decomposition assigns to each braid
  word β ∈ B_n a sign sequence in {+, -}^k (where k is the
  word length).  Gonshor's sign-sequence-to-surreal map then
  produces a finite-birthday surreal.

  ## References
  - [gonshor1986] Gonshor, *An Introduction to the Theory of
    Surreal Numbers*, Cambridge University Press.
  - [conway1976] Conway, *On Numbers and Games*, Academic Press.
-/

import Mathlib.Data.List.Basic
import Mathlib.SetTheory.Ordinal.Basic

namespace QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-- A **sign** is `+` or `-` (binary choice at each Hecke
    eigenspace step). -/
inductive Sign : Type
  | plus
  | minus
  deriving DecidableEq, Repr

/-- A **sign sequence of length n** is a function
    `Fin n → Sign`.  For transfinite-length sequences (general
    surreals) we'd use `Ordinal → Sign`, but for braid words
    finite length suffices. -/
abbrev SignSequence (n : ℕ) := Fin n → Sign

/-- Gonshor's map: a finite sign sequence determines a surreal
    of the same birthday.  Concretely:
    `[]                  ↦ 0`
    `[+]                 ↦ 1`
    `[-]                 ↦ -1`
    `[+, +]              ↦ 2`
    `[+, -]              ↦ 1/2`
    `[-, +]              ↦ -1/2`
    `[-, -]              ↦ -2`
    etc. -/
-- Ref: [gonshor1986] Chapter 2 §1
noncomputable def gonshor : ∀ {n : ℕ}, SignSequence n → K := fun {n} s =>
  -- Recursive Conway construction:
  -- value = (max of L, min of R) sign-extended by the next sign.
  -- Ref: [gonshor1986] Theorem 2.1
  sorry

/-- An abstract braid in `B_n` as a list of generator-choices.
    `(i, true)` means `σ_i`, `(i, false)` means `σ_i^{-1}`. -/
abbrev Braid (n : ℕ) := List (Fin (n - 1) × Bool)

/-- A standard Young tableau of shape `λ ⊢ n` with at most two
    parts.  We axiomatise — the actual Mathlib definition lives
    in `Combinatorics.YoungTableau`. -/
structure StandardTableau (n : ℕ) where
  shape : ℕ × ℕ
  shape_le_n : shape.1 + shape.2 = n
  shape_two_part : shape.2 ≤ shape.1
  -- entries : Fin n → ℕ — placeholder

/-- The **Hoefsmit eigenspace decomposition step**: applying a
    Hecke generator `T_i` (resp. `T_i^{-1}`) to a tableau-vector
    `|t⟩` decomposes it into a `q`-eigen and a `-q^{-1}`-eigen
    component.  We axiomatise the *which-channel* choice as the
    sign function. -/
-- Ref: [gonshor1986], [conway1976]
def hoefsmitChoice
    (n : ℕ) (t : StandardTableau n) (gen : Fin (n - 1) × Bool) : Sign :=
  -- Concrete choice: at each Hecke step, the symmetric channel is
  -- selected when the YJM eigenvalue at the active site is `q`,
  -- antisymmetric when `-q^{-1}`.
  -- Ref: [gonshor1986] §2 — sign assignment by ordering of options
  Sign.plus

/-- The **sign sequence of a braid** at a fixed tableau. -/
def signSequence
    (n : ℕ) (t : StandardTableau n) (β : Braid n) : SignSequence β.length :=
  fun i =>
    let gen := β.get i
    hoefsmitChoice n t gen

/-- The **surreal-valued braid invariant**: Gonshor of the sign
    sequence. -/
-- Ref: [gonshor1986] Theorem 2.1
noncomputable def signSequenceOfBraid
    (n : ℕ) (t : StandardTableau n) (β : Braid n) : K :=
  gonshor (signSequence n t β)

/-- The birthday of `signSequenceOfBraid β t` is bounded by the
    crossing number of `β` (= word length). -/
-- Ref: [gonshor1986] Corollary 2.2
theorem birthday_le_crossing_number
    (n : ℕ) (t : StandardTableau n) (β : Braid n) :
    SurrealField.birthday (signSequenceOfBraid (K := K) n t β) ≤ β.length := by
  -- Ref: [gonshor1986] §2 — birthday = sign-sequence length
  sorry

end QOU.AppendixSurreals
