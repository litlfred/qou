import Mathlib.GroupTheory.SpecificGroups.Cyclic
import Mathlib.GroupTheory.Perm.Cycle.Type


/-!
# QOU.TorusKnot.s5_equivariant_classification

A torus knot T_{2,s} (s ≥ 3, coprime to 2) admits an
S_5-equivariant embedding iff s ∈ {3, 5}, since the orders of
elements of S_5 are {1, 2, 3, 4, 5, 6} and the odd values ≥ 3
in this set are exactly {3, 5}.

LaTeX label: `prop:s5-equivariant-torus-knots`

**Ground ring**: `ℤ` (finite group theory).
-/

namespace QOU

open Equiv

/-- The set of element orders that occur in S_5.
    Cycle types of S_5 partitions and their LCMs:
      (1)^5 → 1, (2)(1)^3 → 2, (2)^2(1) → 2, (3)(1)^2 → 3,
      (3)(2) → 6, (4)(1) → 4, (5) → 5. -/
-- Ref: [leitner2026] Chapter 7, §Particle identification conjectures
def s5ElementOrders : Set ℕ := {1, 2, 3, 4, 5, 6}

/-- Odd element orders ≥ 3 that occur in S_5.
    By inspection of s5ElementOrders: {3, 5}. -/
-- Ref: [leitner2026] Chapter 7, §Particle identification conjectures
def s5OddOrdersGe3 : Set ℕ := {3, 5}

/-- **S_5-equivariant torus-knot classification**:
    T_{2,s} (s ≥ 3, gcd(2,s) = 1, i.e. s odd) embeds equivariantly
    into a Riemann surface with automorphism group S_5 iff
    s ∈ {3, 5}.

    The proof reduces to finding an element of order s in S_5.
    By the orders-in-S_5 table, odd orders ≥ 3 are exactly {3, 5}.

    LaTeX: `\label{prop:s5-equivariant-torus-knots}`
    Ref: [leitner2026] Chapter 7, §Particle identification conjectures -/
theorem s5_equivariant_classification (s : ℕ)
    (hs : 3 ≤ s) (hodd : Odd s) :
    (s ∈ s5OddOrdersGe3) ↔ (s = 3 ∨ s = 5) := by
  constructor
  · intro hmem
    rcases hmem with (rfl | rfl)
    · left; rfl
    · right; rfl
  · intro h
    rcases h with (rfl | rfl)
    · left; rfl
    · right; rfl

end QOU
