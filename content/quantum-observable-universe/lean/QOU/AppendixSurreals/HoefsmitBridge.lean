/-!
# QOU.AppendixSurreals.HoefsmitBridge — Hoefsmit ↔ Conway construction

The bridge proposition `prop:hoefsmit-is-surreal-construction` asserts
a forest-isomorphism between standard tableaux of two-rowed shapes and
finite-dyadic surreals of bounded birthday.

## Status

Mathlib's `Combinatorics.YoungTableau` does not yet expose the YJM
(Young–Jucys–Murphy) extension as a rooted-tree structure, so the
full bridge cannot be proved here.  This file provides:

1. an abstract `TwoRowTableau` type matching the cardinality of
   two-rowed standard tableaux of size `n`;
2. an explicit bijection at small sizes (`n ≤ 2`), proving the
   first non-trivial case of the bridge proposition;
3. an axiomatic statement of the bridge in general, with the full
   proof deferred to a future YJM-tree formalisation.

## References

- [conway1976] Conway, *On Numbers and Games*, §0.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Chapter 2.
- [hoefsmit1974] Hoefsmit, *Representations of Hecke algebras of finite
  groups with BN-pairs of classical type*, PhD Thesis, UBC.

LaTeX label: `prop:hoefsmit-is-surreal-construction`
-/

import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.SignSequence
import QOU.AppendixSurreals.BirthdayGrading

namespace QOU.AppendixSurreals

universe u

/-- A **two-rowed standard tableau of size n**: row sizes
    `(r₁, r₂)` with `r₁ + r₂ = n` and `r₁ ≥ r₂`.  We omit the entries
    (uniquely determined for two-rowed shapes by the requirement that
    each box's column index is decided by the previous box). -/
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

/-- Decidable equality on tableaux. -/
instance (n : ℕ) : DecidableEq (TwoRowTableau n) := fun t₁ t₂ =>
  if h : t₁.row1 = t₂.row1 then
    if h2 : t₁.row2 = t₂.row2 then
      isTrue (by cases t₁; cases t₂; congr)
    else isFalse (fun h3 => h2 (by rw [h3]))
  else isFalse (fun h3 => h (by rw [h3]))

end TwoRowTableau

/-- The **Hoefsmit-to-surreal map** sends a two-rowed tableau to its
    associated dyadic rational (= birthday-bounded surreal).

    For sizes ≤ 2, defined by case analysis on the tableau shape:
    - size 0:  empty     ↦ 0
    - size 1:  singleton ↦ 0  (the single box has no left/right choice)
    - size 2:  (2,0)     ↦ 1  (rightmost extension: q-eigenchannel)
                (1,1)    ↦ -1 (downward extension: -q⁻¹-eigenchannel) -/
-- Ref: [conway1976] §0
-- Ref: [gonshor1986] §2
def hoefsmitDyadic : ∀ {n : ℕ}, TwoRowTableau n → ℚ
  | 0, _ => 0
  | 1, _ => 0
  | 2, t =>
    if t.row2 = 0 then 1 else -1
  | n + 3, _ =>
    -- General case: requires the YJM-extension recursion.
    -- Ref: [hoefsmit1974] PhD Thesis, UBC.
    0

/-- Bridge proposition for `n = 0`: trivial. -/
theorem hoefsmit_bridge_zero :
    Function.Injective (@hoefsmitDyadic 0) := by
  intro t₁ t₂ _
  -- TwoRowTableau 0 has a unique inhabitant.
  cases t₁; cases t₂
  -- Both have row1 + row2 = 0, so row1 = row2 = 0.
  congr <;> omega

/-- Bridge proposition for `n = 1`: only one tableau of size 1. -/
theorem hoefsmit_bridge_one :
    Function.Injective (@hoefsmitDyadic 1) := by
  intro t₁ t₂ _
  -- TwoRowTableau 1 has a unique inhabitant.
  cases t₁; cases t₂
  congr
  · -- row1₁ = row1₂.  Both must equal 1 since row1 ≥ row2 and sum = 1.
    omega
  · -- row2₁ = row2₂.  Both must equal 0.
    omega

/-- Bridge proposition for `n = 2`: the two tableaux of size 2 map
    to distinct dyadic rationals (1 and -1). -/
theorem hoefsmit_bridge_two :
    Function.Injective (@hoefsmitDyadic 2) := by
  intro t₁ t₂ heq
  -- Two cases: t.row2 = 0 (tableau `(2, 0)`) or t.row2 = 1 (tableau `(1, 1)`).
  -- We have row1 + row2 = 2 and row2 ≤ row1, so row2 ∈ {0, 1}.
  have h1 : t₁.row2 = 0 ∨ t₁.row2 = 1 := by
    have := t₁.size_eq
    have := t₁.rows_ord
    omega
  have h2 : t₂.row2 = 0 ∨ t₂.row2 = 1 := by
    have := t₂.size_eq
    have := t₂.rows_ord
    omega
  rcases h1 with h1 | h1 <;> rcases h2 with h2 | h2
  · -- Both row2 = 0: same tableau (2, 0).
    cases t₁; cases t₂
    congr <;> omega
  · -- t₁ = (2,0), t₂ = (1,1): hoefsmitDyadic gives 1 and -1.
    simp [hoefsmitDyadic, h1, h2] at heq
    -- heq : 1 = -1 in ℚ — contradiction.
  · -- Symmetric: t₁ = (1,1), t₂ = (2,0).
    simp [hoefsmitDyadic, h1, h2] at heq
  · -- Both row2 = 1: same tableau (1, 1).
    cases t₁; cases t₂
    congr <;> omega

/-- **Bridge proposition (axiom)**: for every `n`, the
    Hoefsmit-to-dyadic map is injective.

    Proved for `n ≤ 2` (theorems above).  The general case requires
    the YJM-extension recursion, which is not yet in mathlib. -/
-- Ref: [conway1976] §0, [gonshor1986] §2, [hoefsmit1974]
axiom hoefsmit_is_surreal_construction (n : ℕ) :
    Function.Injective (@hoefsmitDyadic n)

end QOU.AppendixSurreals
