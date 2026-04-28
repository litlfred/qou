import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.SignSequence
import QOU.AppendixSurreals.BirthdayGrading

/-!
# QOU.AppendixSurreals.HoefsmitBridge — Hoefsmit ↔ Conway construction

The bridge proposition `prop:hoefsmit-is-surreal-construction` asserts
a forest-isomorphism between standard tableaux of two-rowed shapes and
finite-dyadic surreals of bounded birthday.

## Status

Mathlib's `Combinatorics.YoungTableau` does not yet expose the YJM
(Young–Jucys–Murphy) extension as a rooted-tree structure, so the
full bridge cannot be proved here.  This file provides:

1. an abstract `TwoRowTableau` type recording only the row sizes
   `(row1, row2)` of a two-rowed Young shape.  This matches the
   set of two-rowed *shapes* (one shape per partition), which
   coincides with the set of two-rowed *standard tableaux* only
   for `n ≤ 2`; for `n ≥ 3` distinct standard tableaux of the
   same shape (e.g. the two tableaux of shape `(2, 1)` at `n = 3`)
   are not distinguished by `TwoRowTableau`;
2. an explicit injectivity proof at small sizes (`n ≤ 2`), the
   first non-trivial cases of the bridge proposition;
3. a typeclass formulation of the bridge in general (per
   CLAUDE.md §3b), with the witness deferred to a future
   entry-aware refactor of `TwoRowTableau` plus a YJM-tree
   formalisation.

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
--
-- IMPORTANT: the `TwoRowTableau n` structure used here records only
-- row sizes (row1, row2), not the full entry data.  For `n ≥ 3` this
-- is insufficient to distinguish distinct standard tableaux of the
-- same shape (e.g. the two tableaux of shape (2,1) at n=3).
--
-- The definition is therefore given constructively only for `n ≤ 2`
-- and deferred (via `sorry`, not a bogus `0` value) for `n ≥ 3`.
-- Providing a non-zero value for `n ≥ 3` without distinguishing
-- tableaux would produce an injectivity failure that directly
-- contradicts `hoefsmit_is_surreal_construction`.
--
-- To discharge the deferred case, refactor `TwoRowTableau` to include
-- the entry map (a bijection `Fin n → row-position`) and then:
--   - define a YJM-extension recursion on the entry data, and
--   - prove injectivity by induction on `n` using Gonshor's
--     simplicity theorem.
noncomputable def hoefsmitDyadic : ∀ {n : ℕ}, TwoRowTableau n → ℚ
  | 0, _ => 0
  | 1, _ => 0
  | 2, t =>
    if t.row2 = 0 then 1 else -1
  | n + 3, _ =>
    -- Ref: [hoefsmit1974] PhD Thesis, UBC.
    -- Ref: [gonshor1986] §2 — sign-sequence / YJM extension.
    sorry

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
    obtain ⟨r1₁, r2₁, sz₁, ord₁⟩ := t₁
    obtain ⟨r1₂, r2₂, sz₂, ord₂⟩ := t₂
    simp at h1 h2
    subst h1; subst h2
    congr <;> omega
  · -- t₁ = (2,0), t₂ = (1,1): hoefsmitDyadic gives 1 and -1.
    -- After simp, heq becomes `1 = -1` in ℚ; close via norm_num.
    simp [hoefsmitDyadic, h1, h2] at heq
    exact absurd heq (by norm_num)
  · -- Symmetric: t₁ = (1,1), t₂ = (2,0); heq : -1 = 1 in ℚ.
    simp [hoefsmitDyadic, h1, h2] at heq
    exact absurd heq (by norm_num)
  · -- Both row2 = 1: same tableau (1, 1).
    obtain ⟨r1₁, r2₁, sz₁, ord₁⟩ := t₁
    obtain ⟨r1₂, r2₂, sz₂, ord₂⟩ := t₂
    simp at h1 h2
    subst h1; subst h2
    congr <;> omega

/-- **Bridge proposition as a conjecture class** (per CLAUDE.md §3b).

    Encodes the general-`n` injectivity of the Hoefsmit-to-dyadic
    bijection as a typeclass.  The conjecture's full statement
    references a hypothetical entry-aware refactor
    `ExtendedTableau n`: a type equipped with (a) a map to
    `TwoRowTableau n` (forgetting entries) and (b) an extended
    Hoefsmit function agreeing with `hoefsmitDyadic` for `n ≤ 2`.
    The conjecture asserts the existence of such a refactor with
    globally injective extended-Hoefsmit.

    The proved cases for the **current** partial definition are
    `hoefsmit_bridge_zero`, `hoefsmit_bridge_one`,
    `hoefsmit_bridge_two`.  The current partial `hoefsmitDyadic`
    cannot satisfy general-`n` injectivity (size-3 tableaux of
    shape (2,1) both map to `sorry`). -/
-- Ref: [conway1976] §0, [gonshor1986] §2, [hoefsmit1974]
class HoefsmitIsSurrealConstruction where
  /-- There exists an entry-aware refactored tableau type for
      which the Hoefsmit-to-dyadic map is globally injective, and
      which agrees with the current `hoefsmitDyadic` on the
      proved `n ≤ 2` cases.

      Proving this requires the tableau-entry refactor plus the
      inductive Gonshor-simplicity argument (see appendix §
      `prop:hoefsmit-is-surreal-construction`).  Until that
      infrastructure lands, an instance of this class is created
      by `sorry` (understood per CLAUDE.md §3b as the conjecture). -/
  exists_injective_extension :
    ∃ (ExtendedTableau : ℕ → Type)
      (forgetEntries : ∀ n, ExtendedTableau n → TwoRowTableau n)
      (extendedHoefsmit : ∀ n, ExtendedTableau n → ℚ),
      -- Global injectivity of the extended map:
      (∀ n, Function.Injective (extendedHoefsmit n))
      -- Compatibility for n ≤ 2: agrees with the base partial def.
      ∧ (∀ (t : ExtendedTableau 0),
          extendedHoefsmit 0 t = hoefsmitDyadic (forgetEntries 0 t))
      ∧ (∀ (t : ExtendedTableau 1),
          extendedHoefsmit 1 t = hoefsmitDyadic (forgetEntries 1 t))
      ∧ (∀ (t : ExtendedTableau 2),
          extendedHoefsmit 2 t = hoefsmitDyadic (forgetEntries 2 t))
      -- Surjectivity at n = 2 onto the base codomain
      -- (prevents trivial `Unit` inhabitation of ExtendedTableau):
      ∧ (∀ (t : TwoRowTableau 2),
          ∃ (t' : ExtendedTableau 2), forgetEntries 2 t' = t)
  -- Ref: [gonshor1986] §2 — sign-sequence length = birthday.

end QOU.AppendixSurreals
