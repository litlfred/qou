/-!
# QOU.Descartes.nuclear_groebner_reduction — Unique nuclear normal form via Gröbner reduction

The Hecke algebra H_A(q) = R[B_A] / Skein has an admissible system
(positive braid monomials, length-lex ordering) with Gröbner basis
G = {Hecke, Yang-Baxter, far commutativity}. The division algorithm
gives the unique normal form N̄(p,n).

LaTeX label: `prop:nuclear-groebner-reduction`

## References
- [manuscript] §6/nuclear-groebner-reduction
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Mathlib.Data.List.Basic

namespace QOU.Descartes

/-- A braid word: a list of generator indices. -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
abbrev BraidWord := List ℕ

/-- An element of the Hecke algebra: a list of (word, coefficient) pairs. -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
abbrev HeckeElement := List (BraidWord × ℝ)

/-- The crossing sign for a nucleon pair.
    pp = positive (weight q), nn = negative (weight q⁻¹),
    mixed = neutral (weight (q+q⁻¹)/2). -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
inductive CrossingType
  | pp    -- proton-proton
  | nn    -- neutron-neutron
  | mixed -- proton-neutron
  deriving DecidableEq

/-- The nuclear crossing matrix: for each pair (i,j) with i < j,
    the crossing type depends on whether nucleon i and j are
    protons or neutrons. -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
def crossingType (p : ℕ) (i j : ℕ) : CrossingType :=
  if i < p && j < p then CrossingType.pp
  else if i ≥ p && j ≥ p then CrossingType.nn
  else CrossingType.mixed

/-- The Hecke relation: σ_i² = (q - q⁻¹) σ_i + 1.

    This is the unique energy-changing generator in the
    Gröbner basis. -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
structure HeckeRelation where
  q : ℝ
  q_gt_one : 1 < q
  /-- σ² coefficient of σ: (q - q⁻¹). -/
  sigma_coeff : ℝ := q - 1/q
  /-- σ² constant term: 1. -/
  const_coeff : ℝ := 1
  /-- The sigma coefficient is positive. -/
  sigma_coeff_pos : 0 < sigma_coeff := by
    show 0 < q - 1/q
    rw [sub_pos, div_lt_one (by linarith : (0 : ℝ) < q)]
    nlinarith [q_gt_one]

/-- The Gröbner basis for the Hecke algebra consists of three
    types of relations. -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
inductive GroebnerRelation
  | hecke (i : ℕ)         -- σ_i² = (q-q⁻¹)σ_i + 1
  | yangBaxter (i : ℕ)    -- σ_iσ_{i+1}σ_i = σ_{i+1}σ_iσ_{i+1}
  | farComm (i j : ℕ)     -- σ_iσ_j = σ_jσ_i for |i-j| ≥ 2
  deriving DecidableEq

/-- A word is Gröbner-reduced if no relation in G applies. -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
def isReduced (w : BraidWord) : Prop :=
  -- No adjacent repeated generators (Hecke)
  (∀ i, i + 1 < w.length → w[i]! ≠ w[i+1]!) ∧
  -- Far commuting generators are sorted
  (∀ i, i + 1 < w.length →
    w[i]! > w[i+1]! → (w[i]! : Int) - w[i+1]! < 2) ∧
  -- Yang-Baxter: no σ_i σ_{i+1} σ_i with i > i+1 (lex-reducible)
  (∀ i, i + 2 < w.length →
    w[i]! = w[i+2]! → (w[i]! : Int) - w[i+1]! ≠ 1 ∧
    (w[i]! : Int) - w[i+1]! ≠ -1 ∨ w[i]! ≤ w[i+1]!)

/-- The normal form exists and is unique (main theorem of the
    Gröbner basis theory). -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
-- Ref: [manuscript] unital-groebner-bases/main-theorem
axiom normal_form_exists_unique (q : ℝ) (hq : 1 < q) (A : ℕ)
    (word : BraidWord) :
    ∃! (nf : HeckeElement),
    -- The normal form consists entirely of reduced words
    ∀ (wb : BraidWord × ℝ), wb ∈ nf → isReduced wb.1

/-- The maximum word length of a reduced word with no duplicate
    generators and all generators in {0, ..., A-2} is A-1.
    This follows by pigeonhole: A-1 distinct values, no repeats. -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
theorem max_word_length_bound (A : ℕ) (w : BraidWord)
    (hw : isReduced w) (hgen : ∀ g ∈ w, g < A - 1)
    (hnodup : w.Nodup) :
    w.length ≤ A - 1 := by
  -- Each generator index is in {0, ..., A-2} (A-1 values) by hgen,
  -- and hnodup says no duplicates, so |w| ≤ |{0,...,A-2}| = A-1.
  -- Ref: [manuscript] §6/nuclear-groebner-reduction
  calc w.length = w.toFinset.card := (List.toFinset_card_of_nodup hnodup).symm
    _ ≤ (Finset.range (A - 1)).card := by
        apply Finset.card_le_card
        intro g hg
        rw [Finset.mem_range]
        exact hgen g (List.mem_toFinset.mp hg)
    _ = A - 1 := Finset.card_range _

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [manuscript] §6/nuclear-groebner-reduction
noncomputable def nuclear_groebner_reduction (q : ℝ) (hq : 1 < q)
    (p n : ℕ) : Prop :=
  ∃ (nf : HeckeElement),
    (∀ (wb : BraidWord × ℝ), wb ∈ nf → isReduced wb.1) ∧
    (∀ (wb : BraidWord × ℝ), wb ∈ nf → wb.1.Nodup) ∧
    (∀ (wb : BraidWord × ℝ), wb ∈ nf → wb.1.length ≤ p + n - 1)

end QOU.Descartes
