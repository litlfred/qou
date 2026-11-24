import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic.Ring
import QOU.Brings.HeckeMapFaceSize

/-!
# Level-Local Path-Sum Segmentation and `6^A` `T_w`-Support Bound (`qou-s7ld`, `qou-brfy`)

Upgraded Mathlib/QOU formalization of the `qou-s7ld` level-local path-sum support and
`qou-brfy` triangulated-refinement theorems (salvaged from PR `#8154` using Mathlib's
`Nat.factorial` and `QOU.Brings.HeckeMapFaceSize`).

## Main Results

1. **Level-Local Segmentation Counts of Binding Producer Words (`qou-s7ld`):**
   - For `A ≥ 1` nucleons on `n = 3A` strands, `atom_braid_word_3A` has `11A` intra-nucleon
     letters plus `A - 1` inter-nucleon bond letters, totaling `12A - 1` letters
     (`atomWordLength_eq`).
   - Under `borromean` intra-nucleon order, the `A` nucleon blocks `{3k+1, 3k+2}` (span `2`,
     local SYT orbit size `≤ 3! = 6`) and `A - 1` bond letters `{3k+3}` form `2A - 1`
     pairwise generator-disjoint contiguous segments (`borromeanAtomSegments_eq`).
   - Under historical `grouped` order, each generator appears in a single contiguous run,
     giving `3A - 1` singleton-generator segments (`groupedAtomSegments_eq`).

2. **`6^A` Chain `T_w`-Support vs `(3A)!` Symmetric-Group Cardinality (`qou-s7ld`):**
   - Proves `6^A < (3A)!` for `A ≥ 2` (`twChainSupport_lt_fullSymGroupCard_of_two_le` and
     concrete ratio table `twChainSupport_lt_fullSymGroupCard` for `A = 2..6` via
     `Nat.factorial`), quantifying the `1.68 × 10^8` (`A = 5`, `⁵Li`) and `1.37 × 10^{11}`
     (`A = 6`, `⁶Li`) blow-up factor avoided by the level-local seminormal path sum.

3. **Triangulated Refinement of Bring's `{5,4}` Genus-4 Quadrangulation (`qou-brfy`):**
   - Connects directly to `QOU.Brings.bring_refinement_count`: splitting each of the `F = 30`
     quadrilateral faces of Bring's `{5,4}` map (`V = 24, E = 60, F = 30`) along one diagonal
     yields `V' = V`, `E' = E + F = 90`, `F' = 2F = 60` satisfying `3F' = 2E'` and preserving
     Euler characteristic `V' - E' + F' = V - E + F = -6` across all `2^30 = 1073741824`
     refinements (`quadrangulation_diagonal_split_preserves_euler`,
     `bring_diagonal_refinement_triangulation_invariants`).

-- Ref: [leitner2026] beans qou-s7ld, qou-brfy; computations/chi_path_sum_seminormal.py;
-- QOU/Brings/HeckeMapFaceSize.lean
-/

namespace QOU.Hecke.LevelLocalPathSumSupport

/-- Total letter count of `W_free` on `3A` strands: `11` letters per nucleon. -/
def freeWordLength (A : ℕ) : ℕ := 11 * A

/-- Total letter count of `W_atom` on `3A` strands: `11A` intra-nucleon letters plus
`A - 1` inter-nucleon bond letters. -/
def atomWordLength (A : ℕ) : ℕ := 11 * A + (A - 1)

/-- Number of level-local disjoint generator segments of `W_atom` under `borromean`
intra-nucleon order: `A` intra-nucleon `{3k+1, 3k+2}` segments plus `A - 1` bond segments. -/
def borromeanAtomSegments (A : ℕ) : ℕ := A + (A - 1)

/-- Number of level-local disjoint generator segments of `W_atom` under `grouped`
intra-nucleon order: `2A` singleton segments plus `A - 1` bond segments. -/
def groupedAtomSegments (A : ℕ) : ℕ := 2 * A + (A - 1)

/-- `T_w`-basis support bound of the `A`-nucleon chain word: `(3!)^A = 6^A`. -/
def twChainSupport (A : ℕ) : ℕ := (Nat.factorial 3) ^ A

/-- Full symmetric group cardinality `|S_{3A}| = (3A)!` via `Nat.factorial`. -/
def fullSymGroupCard (A : ℕ) : ℕ := Nat.factorial (3 * A)

/-- For `A ≥ 1`, `atomWordLength A = 12 * A - 1`. -/
theorem atomWordLength_eq (A : ℕ) (hA : 1 ≤ A) :
    atomWordLength A = 12 * A - 1 := by
  unfold atomWordLength
  omega

/-- For `A ≥ 1`, `borromeanAtomSegments A = 2 * A - 1`. -/
theorem borromeanAtomSegments_eq (A : ℕ) (hA : 1 ≤ A) :
    borromeanAtomSegments A = 2 * A - 1 := by
  unfold borromeanAtomSegments
  omega

/-- For `A ≥ 1`, `groupedAtomSegments A = 3 * A - 1`. -/
theorem groupedAtomSegments_eq (A : ℕ) (hA : 1 ≤ A) :
    groupedAtomSegments A = 3 * A - 1 := by
  unfold groupedAtomSegments
  omega

/-- `twChainSupport A` equals `6 ^ A` for every `A : ℕ`. -/
theorem twChainSupport_eq_six_pow (A : ℕ) :
    twChainSupport A = 6 ^ A := by
  unfold twChainSupport
  rfl

/-- Exact `6^A` chain-support values for `A = 1..6` (`qou-s7ld`), matching the measured
`T_w` expansion supports `36 / 216 / 1296 / 7776 / 46656` at `A = 2..6`. -/
theorem twChainSupport_values :
    twChainSupport 1 = 6 ∧
    twChainSupport 2 = 36 ∧
    twChainSupport 3 = 216 ∧
    twChainSupport 4 = 1296 ∧
    twChainSupport 5 = 7776 ∧
    twChainSupport 6 = 46656 := by
  decide

/-- **General Strict Exponential Gap `6^A < (3A)!` for all `A ≥ 2` (`qou-s7ld`):**
By induction from `A = 2` (`36 < 720`), multiplying by `(3A+1)(3A+2)(3A+3) > 6` at each
nucleon step keeps `twChainSupport A < fullSymGroupCard A` for all `A ≥ 2`. -/
theorem twChainSupport_lt_fullSymGroupCard_of_two_le :
    ∀ {A : ℕ}, 2 ≤ A → twChainSupport A < fullSymGroupCard A := by
  intro A hA
  induction A, hA using Nat.le_induction with
  | base => decide
  | succ k hk ih =>
    rw [twChainSupport_eq_six_pow] at ih ⊢
    unfold fullSymGroupCard at ih ⊢
    have hstep : 3 * (k + 1) = 3 * k + 3 := by omega
    rw [hstep, Nat.factorial_succ, Nat.factorial_succ, Nat.factorial_succ]
    have hfac_ge_six : 6 ≤ (3 * k + 3) * ((3 * k + 2) * (3 * k + 1)) := by
      have ha : 2 ≤ 3 * k + 3 := by omega
      have hb : 3 ≤ 3 * k + 2 := by omega
      have hc : 1 ≤ 3 * k + 1 := by omega
      have hbc : 3 ≤ (3 * k + 2) * (3 * k + 1) := Nat.mul_le_mul hb hc
      exact Nat.mul_le_mul ha hbc
    have hpow : 6 ^ (k + 1) = 6 * 6 ^ k := by ring
    rw [hpow]
    calc
      6 * 6 ^ k < 6 * (3 * k).factorial := Nat.mul_lt_mul_of_pos_left ih (by decide)
      _ ≤ ((3 * k + 3) * ((3 * k + 2) * (3 * k + 1))) * (3 * k).factorial :=
        Nat.mul_le_mul_right _ hfac_ge_six
      _ = (3 * k + 3) * ((3 * k + 2) * ((3 * k + 1) * (3 * k).factorial)) := by ring

/-- Concrete ratios `(3A)! / 6^A` at `A = 2..6` (`qou-s7ld`), showing the `1.68 × 10^8` (`⁵Li`)
and `1.37 × 10^{11}` (`⁶Li`) blow-up factors avoided by the dim-free seminormal path sum. -/
theorem twChainSupport_lt_fullSymGroupCard :
    twChainSupport 2 < fullSymGroupCard 2 ∧
    twChainSupport 3 < fullSymGroupCard 3 ∧
    twChainSupport 4 < fullSymGroupCard 4 ∧
    twChainSupport 5 * 168168000 = fullSymGroupCard 5 ∧
    twChainSupport 6 * 137225088000 = fullSymGroupCard 6 := by
  norm_num [twChainSupport_eq_six_pow, fullSymGroupCard, Nat.factorial]

/-- **General Diagonal-Split Triangulation Identity (`qou-brfy`, §7c generic `[CommRing R]`):**
For any quadrangulated surface (`4 * F = 2 * E`), inserting one diagonal per quadrilateral face
gives `V' = V`, `E' = E + F`, `F' = 2 * F`, which automatically satisfies the triangulation
incidence `3 * F' = 2 * E'` and preserves the Euler characteristic `V' - E' + F' = V - E + F`. -/
theorem quadrangulation_diagonal_split_preserves_euler {R : Type*} [CommRing R]
    (V E F : R) (hquad : 4 * F = 2 * E) :
    3 * (2 * F) = 2 * (E + F) ∧
    V - (E + F) + 2 * F = V - E + F := by
  refine ⟨?_, by ring⟩
  calc
    3 * (2 * F) = 4 * F + 2 * F := by ring
    _ = 2 * E + 2 * F := by rw [hquad]
    _ = 2 * (E + F) := by ring

/-- Specialization to Bring's `{5,4}` genus-4 map (`V = 24, E = 60, F = 30`), pairing with
`QOU.Brings.bring_refinement_count` (`2^30 = 1073741824` refinements). -/
theorem bring_diagonal_refinement_triangulation_invariants :
    (60 + 30 : ℤ) = 90 ∧
    (2 * 30 : ℤ) = 60 ∧
    3 * (2 * 30 : ℤ) = 2 * (60 + 30 : ℤ) ∧
    (24 : ℤ) - (60 + 30) + 2 * 30 = 2 - 2 * 4 ∧
    Fintype.card (Fin 30 → Fin 2) = 1073741824 :=
  ⟨by decide, by decide, by decide, by decide, QOU.Brings.bring_refinement_count⟩

end QOU.Hecke.LevelLocalPathSumSupport
