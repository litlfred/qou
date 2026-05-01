/-!
# Homological shell condensation (Lean class)

The conjecture asserts that the Białynicki-Birula spectral sequence
on the descent-graded brane-tower algebra `A_n` collapses entirely
above the `E_2` line at saturated `n ∈ {2, 8, 20, 28, 50, 82, 126}`:

  E_∞^{p, q}(n) = 0   for all p ∈ ℕ, q > 0,  whenever n ∈ M.

We axiomatise the conjecture as a `class` per CLAUDE.md §3b.
Downstream theorems (e.g., the `magic-numbers-from-q` ladder)
become conditional on `[ShellCondensation n]` instances.

-- Ref: [manuscript] conj:homological-shell-condensation
-- Ref: [bialynicki1973] https://doi.org/10.2307/1970915
-- Ref: [yekutieli2010] https://doi.org/10.1090/conm/518/10212
-- Ref: [ariki1996] https://doi.org/10.1112/S0024611596000366
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Finset.Basic

namespace QOU.ShellCondensation

/-- The seven observed magic numbers (mirrors
    `QOU.ShellNeutrality.magicSet`). -/
def magicSet : Finset ℕ := {2, 8, 20, 28, 50, 82, 126}

/-- A saturated level. -/
def Saturated (n : ℕ) : Prop := n ∈ magicSet

/-- The data of a Białynicki-Birula bigraded `E_∞` page at level
    `n`. The conjecture below asks whether this page vanishes above
    the `E_2` line.

    Concretely the QOU substrate instantiates `EInfty p q` as
    `H^q(gr_F^p A_n)` where `A_n` is the descent-graded brane-tower
    algebra and `F` is the BB-filtration induced by the descent
    involution `τ̂`. -/
class BBSpectralSequence (n : ℕ) where
  /-- The `E_∞` page entries, abstracted as a function of the
      bigrading. -/
  EInfty : ℕ → ℕ → Type*
  /-- Each entry is a commutative additive group (so "vanishing"
      means "trivial"). -/
  EInftyAddGroup : ∀ p q, AddCommGroup (EInfty p q)
  /-- A canonical zero element to compare against. -/
  EInftyZero : ∀ p q, EInfty p q

attribute [instance] BBSpectralSequence.EInftyAddGroup

/-- The conjecture, encoded as a class.

    A `HomologicalConjecture n` instance asserts that the strict-
    positive part of the `E_∞` page vanishes at the saturated level
    `n`. The unproved input is the existence of the instance;
    downstream conditional theorems are then fully verified. -/
-- Ref: [manuscript] conj:homological-shell-condensation
class HomologicalConjecture (n : ℕ) extends BBSpectralSequence n where
  /-- Precondition: `n` is saturated. -/
  saturated : Saturated n
  /-- The asserted vanishing: every entry above the `E_2` line is
      the zero element of its group. -/
  collapse :
    ∀ p q, 0 < q → ∀ x : EInfty p q, x = EInftyZero p q

/-- Conditional theorem: under the homological-condensation
    conjecture, every two elements of the strict-positive part of
    `E_∞` at a saturated level are equal (since they are both
    zero). -/
-- Ref: [manuscript] conj:homological-shell-condensation §"Statement"
theorem strict_positive_collapse_unique
    (n : ℕ) [c : HomologicalConjecture n]
    (p q : ℕ) (hq : 0 < q) (x y : c.EInfty p q) :
    x = y := by
  rw [c.collapse p q hq x, c.collapse p q hq y]

/-- Conditional theorem: at a saturated level, the strict-positive
    part of the `E_∞` page is a singleton (the zero subgroup). -/
-- Ref: [manuscript] conj:homological-shell-condensation §"Statement"
theorem strict_positive_subsingleton
    (n : ℕ) [c : HomologicalConjecture n]
    (p q : ℕ) (hq : 0 < q) :
    Subsingleton (c.EInfty p q) := by
  refine ⟨fun x y => ?_⟩
  exact strict_positive_collapse_unique n p q hq x y

end QOU.ShellCondensation
