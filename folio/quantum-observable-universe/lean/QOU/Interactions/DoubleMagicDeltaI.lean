import Mathlib.Data.List.Basic
import Mathlib.Tactic
import QOU.Interactions.BringShellBinding

/-!
# QOU.Interactions.DoubleMagicDeltaI — Δi ≤ 1 rule for double-magic isotopes

The empirical pattern: every observed doubly-magic isotope has
proton and neutron magic numbers in adjacent or equal Bring shells
(`|Δi| ≤ 1`). This module:

1. Records the empirical data as a list of (Z, N, i_Z, i_N) tuples.
2. Proves the partial claim: all 9 observed double-magic isotopes
   satisfy Δi ∈ {0, 1}.
3. States the framework conjecture as a typeclass.
4. Computes the search-space reduction (73%) for compute
   optimisation.

LaTeX label: `conj:double-magic-delta-i-bound`

## References

- [leitner2026] observations / double-magic-delta-i-bound
- [leitner2026] conj:diagrammatic-double-magic-lr-fusion
- [leitner2026] prop:torus-knot-shell-binding
-/

namespace QOU.Interactions.DoubleMagicDeltaI

open QOU.Interactions.BringShellBinding

/-! ## §1  Empirical doubly-magic data -/

/-- An empirically observed doubly-magic isotope. -/
structure DoubleMagicIsotope where
  name : String
  Z : ℕ
  N : ℕ
  iZ : ℕ
  iN : ℕ
  /-- iZ is a valid Bring shell index. -/
  iZ_valid : 1 ≤ iZ ∧ iZ ≤ 7
  /-- iN is a valid Bring shell index. -/
  iN_valid : 1 ≤ iN ∧ iN ≤ 7
  /-- Z = magicAt iZ. -/
  Z_eq : magicAt iZ = some Z
  /-- N = magicAt iN. -/
  N_eq : magicAt iN = some N

/-- The empirical Δi for an isotope. -/
def DoubleMagicIsotope.deltaI (iso : DoubleMagicIsotope) : ℤ :=
  (iso.iN : ℤ) - (iso.iZ : ℤ)

/-- The 9 empirically observed doubly-magic isotopes. -/
def empiricalDoubleMagicIsotopes : List DoubleMagicIsotope := [
  ⟨"He-4", 2, 2, 1, 1, by decide, by decide, rfl, rfl⟩,
  ⟨"O-16", 8, 8, 2, 2, by decide, by decide, rfl, rfl⟩,
  ⟨"Ca-40", 20, 20, 3, 3, by decide, by decide, rfl, rfl⟩,
  ⟨"Ca-48", 20, 28, 3, 4, by decide, by decide, rfl, rfl⟩,
  ⟨"Ni-56", 28, 28, 4, 4, by decide, by decide, rfl, rfl⟩,
  ⟨"Ni-78", 28, 50, 4, 5, by decide, by decide, rfl, rfl⟩,
  ⟨"Sn-100", 50, 50, 5, 5, by decide, by decide, rfl, rfl⟩,
  ⟨"Sn-132", 50, 82, 5, 6, by decide, by decide, rfl, rfl⟩,
  ⟨"Pb-208", 82, 126, 6, 7, by decide, by decide, rfl, rfl⟩
]

/-! ## §2  The Δi ≤ 1 rule on empirical data -/

/-- **Theorem (PROVED).** Every empirically observed doubly-magic
    isotope satisfies `|Δi| ≤ 1` (in fact, `Δi ∈ {0, 1}` since
    nuclei have N ≥ Z in stable cases). -/
-- Ref: [leitner2026] conj:double-magic-delta-i-bound
theorem empirical_deltaI_le_one :
    ∀ iso ∈ empiricalDoubleMagicIsotopes, |iso.deltaI| ≤ 1 := by
  intro iso h
  -- Case-split on which isotope.
  fin_cases h <;> decide

/-- **Theorem.** All 9 empirical doubly-magic isotopes have
    `Δi ∈ {0, 1}` (non-negative). -/
-- Ref: [leitner2026] conj:double-magic-delta-i-bound
theorem empirical_deltaI_in_zero_one :
    ∀ iso ∈ empiricalDoubleMagicIsotopes, iso.deltaI ∈ ({0, 1} : Set ℤ) := by
  intro iso h
  fin_cases h <;>
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] <;>
    decide

/-! ## §3  The Δi ≤ 1 conjecture -/

/-- **Conjecture (Δi ≤ 1 bound).** For any (hypothetical or
    actual) doubly-magic isotope corresponding to Bring-shell index
    pair `(iZ, iN)`, we have `|iN - iZ| ≤ 1`. The forward direction
    is proved on empirical data; the reverse — that no isotope
    with `|Δi| ≥ 2` can be doubly-magic — is the framework
    prediction. -/
-- Ref: [leitner2026] conj:double-magic-delta-i-bound
class DeltaIBoundConjecture where
  /-- Predicate: is the (iZ, iN)-shell pair LR-fusion-compatible
      (=> can support a doubly-magic isotope)? -/
  IsLRCompatible : ℕ → ℕ → Prop
  /-- The conjectural iff: LR-fusion is compatible iff `|Δi| ≤ 1`. -/
  compatible_iff_deltaI_le_one :
    ∀ (iZ iN : ℕ), 1 ≤ iZ → iZ ≤ 7 → 1 ≤ iN → iN ≤ 7 →
      (IsLRCompatible iZ iN ↔ |((iN : ℤ) - iZ)| ≤ 1)

/-! ## §4  Compute-optimisation — search-space reduction -/

/-- The set of all (iZ, iN) pairs in the 7×7 grid. -/
def allShellPairs : List (ℕ × ℕ) :=
  let idx := (List.range 7).map (· + 1)
  idx.product idx

/-- The set of (iZ, iN) pairs with |Δi| ≤ 1 — the
    LR-fusion-compatible band. -/
def lrCompatiblePairs : List (ℕ × ℕ) :=
  allShellPairs.filter (fun ⟨iZ, iN⟩ =>
    decide (|((iN : ℤ) - iZ)| ≤ 1))

/-- **Theorem.** All 49 (iZ, iN) pairs in the 7×7 grid. -/
theorem allShellPairs_card : allShellPairs.length = 49 := by
  decide

/-- **Theorem (compute speedup).** The LR-compatible band has 19
    ordered pairs out of 49 — both orderings (iZ, iN) and (iN, iZ)
    are included since the LR-fusion is non-commutative. -/
-- Ref: [leitner2026] conj:double-magic-delta-i-bound §compute-optimisations
theorem lrCompatiblePairs_card : lrCompatiblePairs.length = 19 := by
  decide

/-- **Compute speedup factor (ordered pairs).** Replacing exhaustive
    7×7 grid search with the LR-compatible band reduces the work
    by a factor of 49/19 ≈ 2.58. -/
-- Ref: [leitner2026] conj:double-magic-delta-i-bound §compute-optimisations
theorem speedup_factor_ordered :
    (49 : ℚ) / 19 > (2 : ℚ) ∧ (49 : ℚ) / 19 < (3 : ℚ) := by
  constructor <;> norm_num

/-- **Restricted pairs** with iZ ≤ iN (physical convention: N ≥ Z
    for stable nuclei). Count: 13. -/
def lrCompatiblePairsOrdered : List (ℕ × ℕ) :=
  lrCompatiblePairs.filter (fun ⟨iZ, iN⟩ => decide (iZ ≤ iN))

theorem lrCompatiblePairsOrdered_card :
    lrCompatiblePairsOrdered.length = 13 := by
  decide

/-- **Restricted-pair speedup** (assuming iZ ≤ iN convention):
    49/13 ≈ 3.77 reduction factor. -/
-- Ref: [leitner2026] conj:double-magic-delta-i-bound
theorem speedup_factor_restricted :
    (49 : ℚ) / 13 > (3 : ℚ) ∧ (49 : ℚ) / 13 < (4 : ℚ) := by
  constructor <;> norm_num

end QOU.Interactions.DoubleMagicDeltaI
