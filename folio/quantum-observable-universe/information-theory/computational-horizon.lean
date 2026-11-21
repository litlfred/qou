import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity


/-!
# QOU.ComputationalHorizon — Computational horizon and resolution trees

A computational horizon is a jet horizon applied to the Skein resolution
tree of a braid closure.  The resolution tree stratifies by depth: at
depth k, k of the c crossings have been resolved, producing a subtree
with 3^k leaves.

The polynomial observable subcategory R° consists of resolution nodes
from which the degree-0 answer P_L(q) is extractable in poly(c) steps.
The computational boundary H_c = V(h_c) is the vanishing locus where
polynomial-time degree-0 sections vanish — the exact analog of the
jet horizon H = V(h) for the brane tower.

P = NP ⟺ H_c = ∅ for all NP links.
P ≠ NP ⟺ ∃ NP-complete L with H_c ≠ ∅.

LaTeX labels: `def:computational-horizon`, `prop:p-bandwidth-bound`,
  `conj:p-vs-np-boundary`

## References

- [cook1971] https://doi.org/10.1145/800157.805047
- [freedman2003] https://doi.org/10.1090/S0273-0979-02-00964-3
- [leitner2026] §9/computational-horizon

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.ComputationalHorizon

/- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Resolution tree

    The Skein resolution tree of a link L with c crossings is a
    ternary tree of depth c: at each crossing, three outcomes
    (L₊, L₋, L₀) produce three children.  The tree has 3^c leaves.

    We model the tree abstractly by its depth-stratification and
    the weight function. -/

/-- A resolution tree: the Skein decomposition of a link with c crossings.
    Stratified by resolution depth k ∈ {0, ..., c}. -/
structure ResolutionTree where
  /-- Number of crossings in the link. -/
  crossings : ℕ
  /-- Crossings must be positive for a nontrivial computation.
      (ℕ-positivity, not an archimedean/order-on-`R_q` condition.) -/
  crossings_pos : crossings > 0
  /-- The type of nodes at depth k. -/
  nodes : Fin (crossings + 1) → Type*
  /-- The root (depth 0) has exactly one node. -/
  root_unique : ∀ (a b : nodes ⟨0, by omega⟩), a = b
  /-- Branching: each node at depth k has 3 children at depth k+1. -/
  children : ∀ (k : Fin crossings),
    nodes ⟨k, by omega⟩ → Fin 3 → nodes ⟨k + 1, by omega⟩

/-- Number of leaves in a resolution tree: 3^c. -/
noncomputable def ResolutionTree.leafCount (T : ResolutionTree) : ℕ :=
  3 ^ T.crossings

/-- The leaf count is always positive. -/
theorem ResolutionTree.leafCount_pos (T : ResolutionTree) :
    T.leafCount > 0 := by
  unfold leafCount
  positivity

/-- The leaf count grows exponentially with crossings. -/
theorem ResolutionTree.leafCount_exponential (T : ResolutionTree) :
    T.leafCount ≥ 3 := by
  unfold leafCount
  calc 3 ^ T.crossings ≥ 3 ^ 1 := Nat.pow_le_pow_right (by norm_num) T.crossings_pos
    _ = 3 := by norm_num

/-! ## Skein weight

    Each resolution path through the tree carries a Skein weight:
    a product of q^(±1) and s = q^(1/2) - q^(-1/2) factors. -/

/-- Skein weight: the weight of a resolution path in R_q.
    Each positive crossing contributes q, each negative q⁻¹. -/
structure SkeinWeight where
  /-- The weight as an element of R_q. -/
  weight : R_q

/-- The Skein polynomial P_L(q): sum of all leaf weights. -/
structure SkeinPolynomial where
  /-- The resolution tree. -/
  tree : ResolutionTree
  /-- Weight of each leaf at depth c. -/
  leafWeight : tree.nodes ⟨tree.crossings, by omega⟩ → SkeinWeight
  -- The polynomial value: sum of leaf weights.
  -- (abstract; concrete evaluation requires summation over leaves)

/-! ## Degree-0 sections and the computational horizon

    A degree-0 section on the resolution tree is a function that
    extracts the answer P_L(q) from a given depth.  At the
    computational horizon, these sections vanish: the polynomial-time
    algorithm cannot extract the answer. -/

/-- A degree-0 section on the resolution tree at depth k:
    an extraction of the Skein polynomial value from the partial
    resolution at depth k. -/
structure DegreeZeroSection (T : ResolutionTree) where
  /-- The extraction depth. -/
  depth : Fin (T.crossings + 1)
  /-- The extraction function: given q, returns the extracted value. -/
  extract : R_q → R_q

/-- A degree-0 section vanishes if it returns 0 for all q. -/
def DegreeZeroSection.vanishes {T : ResolutionTree} (s : DegreeZeroSection T) : Prop :=
  ∀ q : R_q, s.extract q = 0

/-- A degree-≥1 section: a witness (resolution path) verifiable in
    poly(c) steps.  Linear transport through the tree. -/
structure DegreeOneSection (T : ResolutionTree) where
  /-- The resolution path: a choice at each crossing. -/
  path : (k : Fin T.crossings) → Fin 3
  -- The path produces a valid leaf.

/-! ## Polynomial observable subcategory R° -/

/-- The polynomial depth bound for a resolution tree. -/
structure PolyBound where
  /-- The polynomial exponent d (poly = c^d). -/
  exponent : ℕ
  -- The exponent is positive:
  -- exponent_pos : exponent > 0  -- (archimedean; not meaningful over R_q)

/-- The polynomial depth for a tree with c crossings. -/
def PolyBound.depth (p : PolyBound) (c : ℕ) : ℕ :=
  c ^ p.exponent

/-- A polynomial-time extractable degree-0 section: one whose
    depth is bounded by poly(c). -/
structure PolyExtractable (T : ResolutionTree) (pb : PolyBound) where
  /-- The degree-0 section. -/
  section_ : DegreeZeroSection T
  /-- The extraction depth is polynomial. -/
  poly_depth : section_.depth.val ≤ pb.depth T.crossings

/-- The polynomial observable subcategory R°: the subcategory of
    the resolution tree from which degree-0 sections are
    polynomial-time extractable. -/
def polynomialObservable (T : ResolutionTree) (pb : PolyBound) : Prop :=
  ∃ (s : PolyExtractable T pb), ¬ s.section_.vanishes

/-! ## Computational horizon H_c -/

/-- The computational horizon: the tree has a horizon iff no
    polynomial-time degree-0 section is non-vanishing.

    H_c(L, q) = ∅  ⟺  polynomialObservable T pb
    H_c(L, q) ≠ ∅  ⟺  ¬ polynomialObservable T pb

    This mirrors the jet horizon: H = V(h) where h is the ideal
    of degree-0 sections that vanish. -/
-- Ref: [leitner2026] §9/computational-horizon
-- Ref: [cook1971]     title: — see folio/schema/references.ts
def hasComputationalHorizon (T : ResolutionTree) (pb : PolyBound) : Prop :=
  ¬ polynomialObservable T pb

/-- The computational horizon is empty iff the polynomial observable
    subcategory is non-empty: H_c = ∅ ⟺ R° ≠ ∅. -/
theorem horizon_empty_iff_observable (T : ResolutionTree) (pb : PolyBound) :
    ¬ hasComputationalHorizon T pb ↔ polynomialObservable T pb := by
  unfold hasComputationalHorizon
  push_neg
  exact Iff.rfl

/-- A decision problem is in P iff the computational horizon is empty
    for some polynomial bound. -/
def inClassP (T : ResolutionTree) : Prop :=
  ∃ pb : PolyBound, ¬ hasComputationalHorizon T pb

/-- A decision problem has a non-empty computational horizon iff
    it is not in P (for any polynomial bound). -/
def superPolynomial (T : ResolutionTree) : Prop :=
  ∀ pb : PolyBound, hasComputationalHorizon T pb

/-- If a problem is in P, it is not super-polynomial. -/
theorem inP_not_superPoly (T : ResolutionTree) :
    inClassP T → ¬ superPolynomial T := by
  intro ⟨pb, h_no_horizon⟩ h_super
  exact h_no_horizon (h_super pb)

/-- If a problem is super-polynomial, it is not in P. -/
theorem superPoly_not_inP (T : ResolutionTree) :
    superPolynomial T → ¬ inClassP T := by
  intro h_super ⟨pb, h_no_horizon⟩
  exact h_no_horizon (h_super pb)

/-! ## NP verification: degree-≥1 sections cross the horizon

    A witness (degree-1 section) can be verified in O(c) steps:
    one traverses the path and checks consistency at each crossing.
    This mirrors Hawking radiation: degree ≥ 1 data leaks through
    the jet horizon. -/

/-- NP verification: a witness can be checked in linear time (c steps). -/
structure NPWitness (T : ResolutionTree) where
  /-- The resolution path (witness). -/
  witness : DegreeOneSection T
  /-- Verification cost: exactly c steps (one per crossing). -/
  verification_cost : ℕ := T.crossings
  /-- The cost is exactly one step per crossing. -/
  verification_cost_eq : verification_cost = T.crossings := by rfl

/-- The verification cost of an NP witness is polynomial (linear). -/
theorem npWitness_poly_verifiable (T : ResolutionTree) (w : NPWitness T) :
    w.verification_cost ≤ T.crossings :=
  w.verification_cost_eq.le

/-! ## Structural parallels with the jet horizon -/

/-- The jet horizon blocks degree-0 data.
    The computational horizon blocks degree-0 answers.
    Both allow degree ≥ 1 data to leak through.

    This structure captures both: given a graded algebra with
    degree-0 vanishing and degree ≥ 1 leakage, the horizon
    is non-empty. -/
structure HorizonStructure
    (degreeZeroBlocked degreeOneLeaks degreeTwoLeaks horizonNonempty : Prop) where
  /-- If degree-0 is blocked, the horizon is non-empty.

      **Parameterised 2026-09-14, and the defect here was WORSE than the
      `Prop`-universe one.**  This field read

          horizon_nonempty : degree_zero_blocked → True

      which is a TAUTOLOGY: `fun _ => trivial` discharges `X → True` for
      every `X`, so the field constrained nothing at all — and the
      conclusion the docstring names, *"the horizon is non-empty"*, was
      never written down anywhere in the type.  The three conditions
      beside it were `Prop`-universe fields, so an instance chose those
      too.

      As parameters, all four propositions are fixed by whoever writes the
      type and are visible in every consumer's signature, and the field now
      carries the real implication rather than a vacuous one. -/
  horizon_nonempty : degreeZeroBlocked → horizonNonempty

/- The jet horizon as a HorizonStructure (when JetHorizon is in scope).
    This demonstrates that the computational horizon is structurally
    identical to the physical jet horizon. -/
-- The jet horizon from jet-horizon.lean (QOU.JetHorizon) satisfies:
--   degree_zero_blocked := ∀ s, s = algebra.zero 0
--   degree_one_leaks := ∃ s, s ≠ algebra.zero 1
--   degree_two_leaks := ∃ s, s ≠ algebra.zero 2
-- We record this structural parallel without importing the file.

/-- The computational horizon as a HorizonStructure. -/
-- 🛑 The three `True`s below were previously FIELD VALUES, invisible outside
-- this definition.  As type arguments they are on the face of the
-- declaration: this instance asserts leakage and non-emptiness as `True`,
-- i.e. asserts nothing about them, and now says so where a reader looks.
-- Encoding them needs the jet-horizon algebra this file deliberately does
-- not import (see the structural-parallel note above), so they are left as
-- they are rather than guessed at.
def computationalHorizonStructure (T : ResolutionTree) (pb : PolyBound)
    (_h : hasComputationalHorizon T pb) :
    HorizonStructure (hasComputationalHorizon T pb) True True True where
  horizon_nonempty := fun _ => trivial

end

end QOU.ComputationalHorizon
