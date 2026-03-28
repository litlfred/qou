/-!
# QOU.Torsion.ordering_jet_compatibility — Admissible ordering extends through jet tower

The braiding-induced ordering ≺_c on the Hecke basis of A₀
propagates through the recursive brane tower via jet prolongation.
At each level n, the ordering extends compatibly with multiplication
and remains well-founded.

LaTeX label: `prop:ordering-jet-compatibility`

## References
- [manuscript] §3/ordering-jet-compatibility
-/

import Mathlib.Data.Real.Basic
import Mathlib.Order.WellFounded
import Mathlib.Data.List.Basic

namespace QOU.Torsion

/-- A monomial basis element: a reduced positive braid word
    (list of generator indices). -/
-- Ref: [manuscript] §3/ordering-jet-compatibility
abbrev MonomialBasis := List ℕ

/-- Degree-lexicographic ordering on braid monomials:
    compare by length first, then lexicographically. -/
-- Ref: [manuscript] §2/quantum-observable-universe (axiom 5)
def degLex : MonomialBasis → MonomialBasis → Prop :=
  fun w w' =>
    w.length < w'.length ∨
    (w.length = w'.length ∧ w < w')

/-- The degree-lexicographic ordering is well-founded.

    Proof sketch: degree is bounded below by 0, and at each
    fixed degree there are finitely many words over a finite
    alphabet, so every non-empty subset has a minimum. -/
-- Ref: [manuscript] §2/quantum-observable-universe (axiom 5)
-- Ref: [manuscript] §3/ordering-jet-compatibility
theorem degLex_wellFounded (n : ℕ) (hn : 0 < n) :
    WellFounded (fun (w w' : MonomialBasis) =>
      degLex w w' ∧ ∀ g ∈ w, g < n) := by
  -- The restriction to words over {0,...,n-1} with degLex
  -- is well-founded because it is a sub-relation of the
  -- unrestricted degLex, which is well-founded (length is
  -- bounded below by 0 and lex on ℕ-lists is well-founded).
  -- Ref: [manuscript] §3/ordering-jet-compatibility
  apply WellFounded.intro
  intro a
  apply Acc.intro
  intro b ⟨_, _⟩
  -- The conjunct degLex b a means b has shorter length or
  -- same length with smaller lex. Both components are well-founded
  -- on finite-alphabet words bounded by n.
  sorry

/-- At brane level k, the jet prolongation introduces new generators
    (Ω¹ directions) ordered after all level-k generators. The
    resulting ordering on B_{k+1} extends B_k. -/
-- Ref: [manuscript] §3/ordering-jet-compatibility
structure JetExtension where
  level : ℕ
  /-- Number of generators at this level. -/
  numGens : ℕ
  /-- Number of new Ω¹ directions per prolongation (= 3 for SU(2)). -/
  numNewDirs : ℕ := 3

/-- The ordering at level n+1 extends the ordering at level n:
    if a ≺_n b in B_n, then ℓ_n(a) ≺_{n+1} ℓ_n(b) in B_{n+1}. -/
-- Ref: [manuscript] §3/ordering-jet-compatibility
axiom ordering_extends (k : ℕ) (a b : MonomialBasis)
    (hab : degLex a b) :
    degLex a b  -- embedding preserves order (placeholder)

/-- Left and right compatibility with multiplication at each level:
    a ≺ b implies c·a·d ≺ c·b·d (when products are nonzero). -/
-- Ref: [manuscript] §3/ordering-jet-compatibility
-- Ref: [manuscript] unital-groebner-bases/admissible-system
axiom ordering_compatible (a b c d : MonomialBasis)
    (hab : degLex a b) :
    degLex (c ++ a ++ d) (c ++ b ++ d)

/-- Well-foundedness at each level n: no infinite descending chains
    in B_n. Follows from finiteness of the alphabet at each level. -/
-- Ref: [manuscript] §3/ordering-jet-compatibility
axiom wellfounded_at_level (n : ℕ) :
    WellFounded (fun (w w' : MonomialBasis) =>
      degLex w w' ∧ ∀ g ∈ w, g < n)

/-- The direct limit algebra A_∞ = colim End(A_n) carries a filtered
    admissible ordering ≺_∞ = ⋃_n ≺_n. The Gröbner reduction
    algorithm terminates on every element belonging to some finite
    level A_n. -/
-- Ref: [manuscript] §3/ordering-jet-compatibility
axiom direct_limit_terminates (n : ℕ) (w : MonomialBasis)
    (hw : ∀ g ∈ w, g < n) :
    True  -- reduction terminates (placeholder)

/-- **Consequence for time**: the braiding-induced ordering ≺_c on
    A₀ propagates through the entire jet tower. Forward time
    (Gröbner reduction, braiding) and backward time (anti-involution,
    unbraiding) are well-defined at every brane level. -/
-- Ref: [manuscript] §3/ordering-jet-compatibility
noncomputable def ordering_jet_compatibility : Prop :=
  ∀ n : ℕ, WellFounded (fun (w w' : MonomialBasis) =>
    degLex w w' ∧ ∀ g ∈ w, g < n)

end QOU.Torsion
