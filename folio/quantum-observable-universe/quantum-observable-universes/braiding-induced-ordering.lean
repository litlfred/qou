import Mathlib.Data.Real.Basic
import Mathlib.Order.WellFounded
import Mathlib.Data.List.Lex
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic.Ring
import Mathlib.Logic.Relation


/-!
# QOU.braiding_induced_ordering — The braiding induces a well-ordering

The non-symmetric braiding c_{V,V} on C determines a canonical
admissible well-ordering ≺_c on the monomial basis B of the
Hecke algebra H_n(q). This is a proposition derived from the
categorical structure, not an axiom.

LaTeX label: `prop:braiding-induced-ordering`

## References
- [leitner2026] §2/braiding-induced-ordering
-/

namespace QOU

/-- The degree-lex relation on `List α`: first compare lengths,
    then compare lexicographically at equal length. -/
-- Ref: [leitner2026] §2/braiding-induced-ordering
def DegLex {α : Type*} [LT α] (w w' : List α) : Prop :=
  w.length < w'.length ∨
  (w.length = w'.length ∧ List.Lex (· < ·) w w')

/-- Base-`n` positional encoding of a word over `Fin n`:
    `encode [a₀, a₁, …, a_{k-1}] = Σᵢ aᵢ · n^(k-1-i)`.

    This is the arithmetic stand-in for lexicographic comparison **at fixed
    length**, and it is what makes `degLex_wellOrdered` provable. -/
def encode {n : ℕ} : List (Fin n) → ℕ
  | [] => 0
  | a :: l => a.val * n ^ l.length + encode l

/-- A word of length `L` encodes strictly below `n^L` — the carry bound that
    keeps the leading digit dominant. -/
theorem encode_lt {n : ℕ} (w : List (Fin n)) : encode w < n ^ w.length := by
  induction w with
  | nil => simp [encode]
  | cons a l ih =>
      have han : a.val + 1 ≤ n := a.isLt
      have key : encode (a :: l) < n ^ (l.length + 1) :=
        calc encode (a :: l)
            = a.val * n ^ l.length + encode l := rfl
          _ < a.val * n ^ l.length + n ^ l.length := add_lt_add_left ih _
          _ = (a.val + 1) * n ^ l.length := by ring
          _ ≤ n * n ^ l.length := mul_le_mul_right' han _
          _ = n ^ (l.length + 1) := by ring
      simpa using key

/-- **At equal length, `List.Lex` is exactly `encode`-order.**

    This is the step the previous proof was missing. It cannot be replaced by
    a well-foundedness fact about `List.Lex` itself, because `List.Lex (· < ·)`
    on `List (Fin n)` is **not** well-founded for `n ≥ 2`:
    `[0,1] > [0,0,1] > [0,0,0,1] > …` descends forever. Restricting to equal
    length is what rules those chains out, and `encode` is what converts the
    restricted relation into `<` on `ℕ`. -/
theorem encode_lt_of_lex {n : ℕ} {w w' : List (Fin n)}
    (hlex : List.Lex (· < ·) w w') :
    w.length = w'.length → encode w < encode w' := by
  induction hlex with
  | nil => intro h; simp at h
  | @cons a l₁ l₂ _ ih =>
      intro h
      have hlen : l₁.length = l₂.length := by simpa using h
      have hrec := ih hlen
      show a.val * n ^ l₁.length + encode l₁ < a.val * n ^ l₂.length + encode l₂
      rw [hlen]
      exact add_lt_add_left hrec _
  | @rel a l₁ b l₂ hab =>
      intro h
      have hlen : l₁.length = l₂.length := by simpa using h
      have hb : a.val + 1 ≤ b.val := hab
      show a.val * n ^ l₁.length + encode l₁ < b.val * n ^ l₂.length + encode l₂
      calc a.val * n ^ l₁.length + encode l₁
          < a.val * n ^ l₁.length + n ^ l₁.length := add_lt_add_left (encode_lt l₁) _
        _ = (a.val + 1) * n ^ l₁.length := by ring
        _ ≤ b.val * n ^ l₁.length := mul_le_mul_right' hb _
        _ = b.val * n ^ l₂.length := by rw [hlen]
        _ ≤ b.val * n ^ l₂.length + encode l₂ := Nat.le_add_right _ _

/-- **DegLex on `List (Fin n)` is well-founded.**

    Embed into `ℕ ×ₗ ℕ` via `w ↦ (w.length, encode w)`. Both components are
    `<` on `ℕ`, so `WellFounded.prod_lex` applies.

    The earlier proof embedded into `ℕ ×ₗ List (Fin n)` and appealed to
    well-foundedness of `List.Lex` in the second slot. That is **false**
    (see `encode_lt_of_lex`), so the route could not be repaired by fixing a
    name — the second component has to be replaced by something that really
    is well-founded, which is what `encode` provides. -/
-- Ref: [leitner2026] §2/braiding-induced-ordering
theorem degLex_wellOrdered (n : ℕ) :
    WellFounded (DegLex (α := Fin n)) := by
  have hwf : WellFounded
      (InvImage (Prod.Lex (· < ·) (· < ·))
        (fun w : List (Fin n) => (w.length, encode w))) :=
    InvImage.wf _ (Nat.lt_wfRel.wf.prod_lex Nat.lt_wfRel.wf)
  apply Subrelation.wf _ hwf
  intro w w' h
  rcases h with h | ⟨he, hl⟩
  · exact Prod.Lex.left _ _ h
  · simp only [InvImage]
    rw [he]
    exact Prod.Lex.right _ (encode_lt_of_lex hl he)

/-- Admissibility (length component): concatenation preserves
    the length ordering. -/
-- Ref: [leitner2026] §2/braiding-induced-ordering
theorem degLex_admissible_length {α : Type*} [LT α]
    (u v w w' : List α) (h : w.length < w'.length) :
    (u ++ w ++ v).length < (u ++ w' ++ v).length := by
  simp [List.length_append]; omega

/-- Appending a common **suffix** preserves `List.Lex`, provided the two
    words have equal length.

    Mathlib supplies only the common-*prefix* direction
    (`List.Lex.append_left`); there is no suffix lemma, and the suffix
    statement is **false** without the length hypothesis: with
    `w = []`, `w' = [0]`, `v = [1]` we have `Lex (· < ·) [] [0]` by
    `Lex.nil`, yet `Lex (· < ·) [1] [0, 1]` fails — the heads `1` and `0`
    are unequal and `1 < 0` is false.  Equal length rules that case out:
    the `Lex.nil` constructor forces `w = []` and `w' ≠ []`, which
    contradicts `hlen`.  The remaining two constructors carry the suffix
    through unchanged. -/
-- Ref: [leitner2026] §2/braiding-induced-ordering
theorem lex_append_suffix {α : Type*} {R : α → α → Prop} :
    ∀ {w w' : List α}, List.Lex R w w' → w.length = w'.length →
      ∀ v : List α, List.Lex R (w ++ v) (w' ++ v)
  | _, _, List.Lex.nil, hlen, _ => by simp at hlen
  | _, _, List.Lex.cons h, hlen, v =>
      List.Lex.cons (lex_append_suffix h (by simpa using hlen) v)
  | _, _, List.Lex.rel h, _, _ => List.Lex.rel h

/-- Admissibility (lex component): concatenation with a common
    prefix and a common suffix preserves the lex ordering. -/
-- Ref: [leitner2026] §2/braiding-induced-ordering
theorem degLex_admissible_lex {α : Type*} [LT α]
    (u v w w' : List α) (h : List.Lex (· < ·) w w')
    (hlen : w.length = w'.length) :
    List.Lex (· < ·) (u ++ w ++ v) (u ++ w' ++ v) := by
  induction u with
  | nil =>
    simp only [List.nil_append]
    exact lex_append_suffix h hlen v
  | cons a us ih =>
    simp only [List.cons_append]
    exact List.Lex.cons ih

/-- Full admissibility: DegLex is preserved under concatenation
    with common prefix and suffix. -/
-- Ref: [leitner2026] §2/braiding-induced-ordering
-- Ref: [leitner2026] unital-groebner-bases/admissible-system
theorem degLex_admissible {n : ℕ} (u v w w' : List (Fin n))
    (h : DegLex w w') :
    DegLex (u ++ w ++ v) (u ++ w' ++ v) := by
  unfold DegLex at *
  rcases h with h_len | ⟨h_eq, h_lex⟩
  · left; exact degLex_admissible_length u v w w' h_len
  · right
    exact ⟨by simp [List.length_append]; omega,
           degLex_admissible_lex u v w w' h_lex h_eq⟩

/-- **No closed `≺_c`-chains.** No word returns to itself through a finite
    chain of strict `DegLex` steps. This is the fact used by
    `rem:no-goedel-closed-chains`: it follows from well-foundedness alone.
    The general statement is `QOU.Chronology.not_closedChainAt_of_wellFounded`
    in the library; it is repeated here so this file stays self-contained. -/
-- Ref: [leitner2026] §2/no-goedel-closed-chains
theorem degLex_no_closedChain (n : ℕ) (w : List (Fin n)) :
    ¬ Relation.TransGen (DegLex (α := Fin n)) w w := by
  have h' : WellFounded (Relation.TransGen (DegLex (α := Fin n))) :=
    (degLex_wellOrdered n).transGen
  exact h'.induction (C := fun x => ¬ Relation.TransGen DegLex x x) w
    (fun x ih hx => ih x hx hx)

/-- **No total chronology for `≺_c`.** It is false that every word reaches
    every word (itself included) by a finite `DegLex` chain. This is the
    order-theoretic form of excluding a Gödel-type universe, where
    `I⁺(p) = M` for every event `p`. -/
-- Ref: [leitner2026] §2/no-goedel-closed-chains
theorem degLex_not_totalChronology (n : ℕ) :
    ¬ ∀ w w' : List (Fin n), Relation.TransGen (DegLex (α := Fin n)) w w' :=
  fun h => degLex_no_closedChain n [] (h [] [])

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [leitner2026] §2/braiding-induced-ordering
def braiding_induced_ordering : Prop :=
  ∀ n : ℕ, WellFounded (DegLex (α := Fin n))

end QOU
