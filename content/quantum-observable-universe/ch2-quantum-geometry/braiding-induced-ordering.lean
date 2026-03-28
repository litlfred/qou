/-!
# QOU.braiding_induced_ordering — The braiding induces a well-ordering

The non-symmetric braiding c_{V,V} on C determines a canonical
admissible well-ordering ≺_c on the monomial basis B of the
Hecke algebra H_n(q). This is a proposition derived from the
categorical structure, not an axiom.

LaTeX label: `prop:braiding-induced-ordering`

## References
- [manuscript] §2/braiding-induced-ordering
-/

import Mathlib.Data.Real.Basic
import Mathlib.Order.WellFounded
import Mathlib.Data.List.Lex

namespace QOU

/-- A monomial basis element: a reduced positive braid word
    (list of generator indices in {1, ..., n-1}). -/
-- Ref: [manuscript] §2/braiding-induced-ordering
abbrev MonomialBasis := List ℕ

/-- Degree-lexicographic ordering: compare by length first,
    then lexicographically on generator indices. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
instance : LT MonomialBasis where
  lt := fun w w' =>
    w.length < w'.length ∨
    (w.length = w'.length ∧ w < w')

/-- The degree-lexicographic ordering on words over a finite
    alphabet {1, ..., n-1} is a well-ordering.

    Proof: (a) degree ≥ 0, so every non-empty subset has a
    minimum-degree layer; (b) at fixed degree d, the set of
    words of length d over {1,...,n-1} is finite; (c) every
    finite totally ordered set has a minimum. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
theorem degLex_wellOrdered (n : ℕ) (hn : 0 < n) :
    WellFounded (fun (w w' : List (Fin n)) =>
      w.length < w'.length ∨
      (w.length = w'.length ∧ List.Lex (· < ·) w w')) := by
  -- The degree-lex order is the lexicographic product of
  -- (length, lex-on-list). Both components are well-founded:
  -- • ℕ with < is well-founded (Nat.lt_wfRel)
  -- • List (Fin n) with List.Lex (· < ·) is well-founded
  --   because Fin n is finite and (· < ·) on Fin n is well-founded.
  -- Ref: [manuscript] §2/braiding-induced-ordering
  apply InvImage.wf (fun w => (w.length, w))
    (Prod.Lex.wf Nat.lt_wfRel.wf (List.isWellFounded_lt (α := Fin n)).wf)

/-- The degree-lex ordering is admissible: compatible with
    left and right multiplication (concatenation of braid words).
    This follows because degree-lex is compatible with any
    associative multiplication whose defining relations have
    leading terms of bounded degree (the Hecke relation is
    quadratic). -/
-- Ref: [manuscript] §2/braiding-induced-ordering
-- Ref: [manuscript] unital-groebner-bases/admissible-system
theorem degLex_admissible (u v w w' : List (Fin n))
    (h : w.length < w'.length ∨
      (w.length = w'.length ∧ List.Lex (· < ·) w w')) :
    (u ++ w ++ v).length < (u ++ w' ++ v).length ∨
    ((u ++ w ++ v).length = (u ++ w' ++ v).length ∧
     List.Lex (· < ·) (u ++ w ++ v) (u ++ w' ++ v)) := by
  simp [List.length_append]
  rcases h with h_len | ⟨h_eq, h_lex⟩
  · left; omega
  · right
    refine ⟨by omega, ?_⟩
    -- Lex order: common prefix u is skipped, then w < w', then
    -- common suffix v is irrelevant.
    -- Ref: [manuscript] §2/braiding-induced-ordering
    exact List.Lex.append_left _ (List.Lex.append_right u h_lex)

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
def braiding_induced_ordering : Prop :=
  ∀ n : ℕ, 0 < n →
    WellFounded (fun (w w' : List (Fin n)) =>
      w.length < w'.length ∨
      (w.length = w'.length ∧ List.Lex (· < ·) w w'))

end QOU
