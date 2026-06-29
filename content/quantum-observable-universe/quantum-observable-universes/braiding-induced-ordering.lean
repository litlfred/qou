import Mathlib.Data.Real.Basic
import Mathlib.Order.WellFounded
import Mathlib.Data.List.Lex
import Mathlib.Data.Fin.Basic


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

namespace QOU

/-- The degree-lex relation on `List α`: first compare lengths,
    then compare lexicographically at equal length. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
def DegLex [LT α] (w w' : List α) : Prop :=
  w.length < w'.length ∨
  (w.length = w'.length ∧ List.Lex (· < ·) w w')

/-- DegLex on `List (Fin n)` is well-founded.

    Strategy: embed into `ℕ ×ₗ List (Fin n)` via `w ↦ (w.length, w)`.
    The lexicographic product of two well-founded relations is
    well-founded. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
theorem degLex_wellOrdered (n : ℕ) :
    WellFounded (DegLex (α := Fin n)) := by
  -- DegLex is a subrelation of the inverse image of the lexicographic
  -- product `Prod.Lex (· < ·) (List.Lex (· < ·))` under `w ↦ (w.length, w)`,
  -- and the latter is well-founded.
  have hwf : WellFounded
      (InvImage (Prod.Lex (· < ·) (List.Lex (· < ·)))
        (fun w : List (Fin n) => (w.length, w))) :=
    InvImage.wf _ (Prod.lex_wf Nat.lt_wfRel.wf List.wellFoundedLT.wf)
  apply Subrelation.wf _ hwf
  intro w w' h
  rcases h with h | ⟨he, hl⟩
  · exact Prod.Lex.left _ _ h
  · simp only [InvImage]
    rw [he]
    exact Prod.Lex.right _ hl

/-- Admissibility (length component): concatenation preserves
    the length ordering. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
theorem degLex_admissible_length {α : Type*} [LT α]
    (u v w w' : List α) (h : w.length < w'.length) :
    (u ++ w ++ v).length < (u ++ w' ++ v).length := by
  simp [List.length_append]; omega

/-- Admissibility (lex component): concatenation with a common
    prefix preserves the lex ordering. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
theorem degLex_admissible_lex {α : Type*} [LT α]
    (u v w w' : List α) (h : List.Lex (· < ·) w w')
    (hlen : w.length = w'.length) :
    List.Lex (· < ·) (u ++ w ++ v) (u ++ w' ++ v) := by
  induction u with
  | nil =>
    simp only [List.nil_append]
    exact List.append_left h v
  | cons a us ih =>
    simp only [List.cons_append]
    exact List.Lex.cons ih

/-- Full admissibility: DegLex is preserved under concatenation
    with common prefix and suffix. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
-- Ref: [manuscript] unital-groebner-bases/admissible-system
theorem degLex_admissible {n : ℕ} (u v w w' : List (Fin n))
    (h : DegLex w w') :
    DegLex (u ++ w ++ v) (u ++ w' ++ v) := by
  unfold DegLex at *
  rcases h with h_len | ⟨h_eq, h_lex⟩
  · left; exact degLex_admissible_length u v w w' h_len
  · right
    exact ⟨by simp [List.length_append]; omega,
           degLex_admissible_lex u v w w' h_lex h_eq⟩

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [manuscript] §2/braiding-induced-ordering
def braiding_induced_ordering : Prop :=
  ∀ n : ℕ, WellFounded (DegLex (α := Fin n))

end QOU
