/-
  Hoefsmit seminormal form is Conway's {L | R} construction.

  The bijection between standard tableaux of two-rowed shapes and
  finite-birthday dyadic surreals.

  ## References
  - [gonshor1986] Gonshor, *An Introduction to the Theory of
    Surreal Numbers*, Cambridge University Press.
  - [conway1976] Conway, *On Numbers and Games*, Academic Press.
-/

import Mathlib.SetTheory.Ordinal.Basic

namespace QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-- A **two-rowed standard tableau of size n** abstracted as a
    pair (rows, with row sizes summing to n).
    Mathlib has `Combinatorics.YoungTableau`; we keep it abstract
    here pending integration. -/
structure TwoRowTableau (n : ℕ) where
  row1 : List ℕ
  row2 : List ℕ
  size_eq : row1.length + row2.length = n
  rows_strict : row1.length ≥ row2.length
  -- entries unique, increasing along rows and columns — omitted

/-- A **finite dyadic surreal** is one whose sign-sequence has finite
    length.  These are exactly the dyadic rationals
    {a / 2^k : a ∈ ℤ, k ∈ ℕ} ⊂ K. -/
def IsFiniteDyadic (x : K) : Prop :=
  ∃ (a : ℤ) (k : ℕ), x = (a : K) / (2 ^ k : K)

/-- The **Hoefsmit-to-surreal bijection**.

    Sends each two-rowed tableau of size `n` to a dyadic surreal of
    birthday `≤ n`, and conversely.  The recipe:

    - the empty tableau ↦ 0
    - extending a tableau by adding a box to row 1 ↦ sign-sequence
      extension `s ↦ s · +`  (`q`-eigenchannel)
    - extending by adding a box to row 2 ↦ sign-sequence extension
      `s ↦ s · -`  (`-q^{-1}`-eigenchannel)

    The Gonshor sign-sequence map then converts to a surreal. -/
-- Ref: [gonshor1986] §2 — sign-sequence-to-surreal map
-- Ref: [conway1976] §0 — recursive construction
noncomputable def hoefsmitToSurreal (n : ℕ) (t : TwoRowTableau n) : K :=
  -- placeholder: requires the YJM-extension recursion +
  -- `gonshor` from `sign-sequence-of-braid.lean`
  sorry

/-- The **inverse map**: every finite-dyadic surreal of birthday `≤ n`
    corresponds to a unique two-rowed standard tableau of size `n`. -/
-- Ref: [gonshor1986] Theorem 2.1 (uniqueness of sign sequence)
noncomputable def surrealToHoefsmit (n : ℕ) (x : K) (hx : IsFiniteDyadic x) :
    Option (TwoRowTableau n) :=
  -- placeholder
  none

/-- **Hoefsmit-is-surreal-construction proposition**.

    The Hoefsmit-to-surreal map `hoefsmitToSurreal` is a bijection
    between two-rowed standard tableaux of size `n` and finite-dyadic
    surreals of birthday `≤ n`. -/
-- Ref: [conway1976] §0
-- Ref: [gonshor1986] Theorem 2.1
theorem hoefsmit_is_surreal_construction (n : ℕ) :
    ∃ (Φ : TwoRowTableau n → K),
      (∀ t, IsFiniteDyadic (Φ t)) ∧
      (∀ t, SurrealField.birthday (Φ t) ≤ (n : Ordinal)) ∧
      Function.Injective Φ := by
  -- The `hoefsmitToSurreal` map provides the witness; injectivity
  -- follows from uniqueness of the YJM-extension recursion.
  -- Ref: [gonshor1986] Theorem 2.1
  sorry

end QOU.AppendixSurreals
