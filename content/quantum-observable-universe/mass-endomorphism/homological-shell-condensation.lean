import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import QOU.Common.MagicNumbers


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
-- Ref: [bialynicki1973]     title: — see content/schema/references.ts
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
-- Ref: [ariki1996] Ariki, "On the decomposition numbers of the Hecke algebra of G(m, 1, n)," J. Math. Kyoto Univ. 36 (1996)
-/

namespace QOU.ShellCondensation

-- Single source of truth: QOU.Common.magicSet (see PR #501
-- review). Re-exported as abbreviations for local ergonomics.
abbrev magicSet : Finset ℕ := QOU.Common.magicSet
abbrev Saturated (n : ℕ) : Prop := QOU.Common.Saturated n

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

/-- Conditional theorem: the strict-positive part of the `E_∞`
    page contains exactly one element (the zero of the additive
    group), at a saturated level. Combines `Subsingleton` with
    the existence of `EInftyZero`. -/
-- Ref: [manuscript] conj:homological-shell-condensation §"Statement"
theorem strict_positive_eq_zero
    (n : ℕ) [c : HomologicalConjecture n]
    (p q : ℕ) (hq : 0 < q) (x : c.EInfty p q) :
    x = c.EInftyZero p q :=
  c.collapse p q hq x

/-- Conditional corollary: at a saturated level, every additive
    operation in the strict-positive part of `E_∞` is trivial.
    `x + y = 0` for any `x, y` in the strict-positive page. -/
-- Ref: [manuscript] conj:homological-shell-condensation §"Statement"
theorem strict_positive_add_zero
    (n : ℕ) [c : HomologicalConjecture n]
    (p q : ℕ) (hq : 0 < q) (x y : c.EInfty p q) :
    x + y = c.EInftyZero p q + c.EInftyZero p q := by
  rw [c.collapse p q hq x, c.collapse p q hq y]

/-- Conditional theorem: at a saturated level, every diagonal
    entry `E_∞^{p, p}` for `p ≥ 1` is also trivial — the BB
    spectral sequence collapses on the entire upper-triangular
    region above the `q = 0` line, not just the strictly off-
    diagonal part. -/
-- Ref: [manuscript] conj:homological-shell-condensation §"Statement"
theorem strict_diagonal_collapse
    (n : ℕ) [c : HomologicalConjecture n]
    (p : ℕ) (hp : 0 < p) (x : c.EInfty p p) :
    x = c.EInftyZero p p :=
  c.collapse p p hp x

end QOU.ShellCondensation
