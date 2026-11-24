import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Mathlib.Data.List.Basic

/-!
# QOU.Archimedean.nuclear_groebner_reduction — Unique nuclear normal form via Gröbner reduction

The Hecke algebra H_A(q) = R[B_A] / Skein has an admissible system
(positive braid monomials, length-lex ordering). Its Gröbner–Shirshov basis
is the Hecke relation, far commutativity and the Bokut–Shiao family (which
contains Yang–Baxter); the three defining families alone are NOT a GS basis
for A ≥ 4 (`UGB.GrobnerShirshov.Hecke.NotAGSBasis.hecke_not_gs_basis_four`;
completed system: `heckeCompleted_isGrobnerShirshovBasis`). The division
algorithm gives the normal form N̄(p,n).

This module formalises only the reduced-word predicate for the three defining
families and a length bound; it does not formalise the basis or uniqueness.

LaTeX label: `prop:nuclear-groebner-reduction`

## References
- [leitner2026] §6/nuclear-groebner-reduction
-/

namespace QOU.Archimedean

-- Ref: [leitner2026] §6/nuclear-groebner-reduction
/-- A braid word as a plain list of generator indices, local to the
Gröbner–Shirshov reduction in this module.

Renamed from `BraidWord` (bean `qou-kfcl`): `QOU.Archimedean.BraidWord` is
already `List (Fin (n - 1) × Bool)` in `QOU.Archimedean.HeckeRep` — a
different type, not a mirror — so the two modules could never both be
imported. Renamed rather than namespace-nested because a content block's
`lean.ref` names `QOU.Archimedean.nuclear_groebner_reduction` in this file,
and nesting would have moved that name too. -/
abbrev NuclearBraidWord := List ℕ

/-- An element of the Hecke algebra: a list of (word, coefficient) pairs. -/
-- Ref: [leitner2026] §6/nuclear-groebner-reduction
abbrev HeckeElement := List (NuclearBraidWord × ℝ)

/-- The crossing sign for a nucleon pair.
    pp = positive (weight q), nn = negative (weight q⁻¹),
    mixed = neutral (weight (q+q⁻¹)/2). -/
-- Ref: [leitner2026] §6/nuclear-groebner-reduction
inductive CrossingType
  | pp    -- proton-proton
  | nn    -- neutron-neutron
  | mixed -- proton-neutron
  deriving DecidableEq

/-- The nuclear crossing matrix: for each pair (i,j) with i < j,
    the crossing type depends on whether nucleon i and j are
    protons or neutrons. -/
-- Ref: [leitner2026] §6/nuclear-groebner-reduction
def crossingType (p : ℕ) (i j : ℕ) : CrossingType :=
  if i < p && j < p then CrossingType.pp
  else if i ≥ p && j ≥ p then CrossingType.nn
  else CrossingType.mixed

/-- The Hecke relation: σ_i² = (q - q⁻¹) σ_i + 1.

    This is the unique energy-changing generator in the
    Gröbner basis. -/
-- Ref: [leitner2026] §6/nuclear-groebner-reduction
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

/-- The three defining relation families of the Hecke algebra. They are
    NOT a Gröbner–Shirshov basis for `A ≥ 4`; the basis adds the Bokut–Shiao
    family (see `UGB.GrobnerShirshov.Hecke.heckeCompleted_isGrobnerShirshovBasis`). -/
-- Ref: [leitner2026] §6/nuclear-groebner-reduction
inductive GroebnerRelation
  | hecke (i : ℕ)         -- σ_i² = (q-q⁻¹)σ_i + 1
  | yangBaxter (i : ℕ)    -- σ_iσ_{i+1}σ_i = σ_{i+1}σ_iσ_{i+1}
  | farComm (i j : ℕ)     -- σ_iσ_j = σ_jσ_i for |i-j| ≥ 2
  deriving DecidableEq

/-- A word is Gröbner-reduced if no relation in G applies. -/
-- Ref: [leitner2026] §6/nuclear-groebner-reduction
def isReduced (w : NuclearBraidWord) : Prop :=
  -- No adjacent repeated generators (Hecke)
  (∀ i, i + 1 < w.length → w[i]! ≠ w[i+1]!) ∧
  -- Far commuting generators are sorted
  (∀ i, i + 1 < w.length →
    w[i]! > w[i+1]! → (w[i]! : Int) - w[i+1]! < 2) ∧
  -- Yang-Baxter: no σ_i σ_{i+1} σ_i with i > i+1 (lex-reducible)
  (∀ i, i + 2 < w.length →
    w[i]! = w[i+2]! → (w[i]! : Int) - w[i+1]! ≠ 1 ∧
    (w[i]! : Int) - w[i+1]! ≠ -1 ∨ w[i]! ≤ w[i+1]!)

/- REMOVED (2026-08-25): `normal_form_exists_unique` was formally defective —
    the bound variables `q`, `hq`, `A`, `word` did not appear in the conclusion
    `∃! nf, ∀ wb ∈ nf, isReduced wb.1`, making the statement provably false
    (both `[]` and `[([], 1.0)]` satisfy the predicate). The axiom had zero
    consumers in the codebase. A correct formulation of Gröbner confluence
    would need the word and parameters to appear in the conclusion.
    See `nuclear_groebner_reduction` above for the working (non-unique) version. -/

/-- The maximum word length of a reduced word with no duplicate
    generators and all generators in {0, ..., A-2} is A-1.
    This follows by pigeonhole: A-1 distinct values, no repeats. -/
-- Ref: [leitner2026] §6/nuclear-groebner-reduction
theorem max_word_length_bound (A : ℕ) (w : NuclearBraidWord)
    (hw : isReduced w) (hgen : ∀ g ∈ w, g < A - 1)
    (hnodup : w.Nodup) :
    w.length ≤ A - 1 := by
  -- Each generator index is in {0, ..., A-2} (A-1 values) by hgen,
  -- and hnodup says no duplicates, so |w| ≤ |{0,...,A-2}| = A-1.
  -- Ref: [leitner2026] §6/nuclear-groebner-reduction
  calc w.length = w.toFinset.card := (List.toFinset_card_of_nodup hnodup).symm
    _ ≤ (Finset.range (A - 1)).card := by
        apply Finset.card_le_card
        intro g hg
        rw [Finset.mem_range]
        exact hgen g (List.mem_toFinset.mp hg)
    _ = A - 1 := Finset.card_range _

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [leitner2026] §6/nuclear-groebner-reduction
noncomputable def nuclear_groebner_reduction (q : ℝ) (hq : 1 < q)
    (p n : ℕ) : Prop :=
  ∃ (nf : HeckeElement),
    (∀ (wb : NuclearBraidWord × ℝ), wb ∈ nf → isReduced wb.1) ∧
    (∀ (wb : NuclearBraidWord × ℝ), wb ∈ nf → wb.1.Nodup) ∧
    (∀ (wb : NuclearBraidWord × ℝ), wb ∈ nf → wb.1.length ≤ p + n - 1)

end QOU.Archimedean
