/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Tactic.Positivity
import QOU.MassTheory.B3ExtensiveCellSumCarrier
import QOU.MassTheory.NucleusBondValence

/-!
# Exploratory Alpha-Quartet `K_4` Closure, FCC `(111)` Face Contacts & Isobaric Valley Concavity

Division-free algebraic, combinatorial, and strict-ordered-ring theorems over generic
`[CommRing R]` (`0 sorry`, `0` custom axioms, `0` `[Field K]` binders, `0` `field_simp` calls,
zero archimedean `ℝ` or transcendental imports per §7c / `qou-8318` / `qou-dk7p`) paired with
the **exploratory macroscopic cluster-model comparison (`§3b-cond`, unwired)** for beans
`qou-v2om`, `qou-gpb5`, `qou-sbn9`, and `qou-d9iv`.

## Applicability & Scope Under the 2026-11-27 `T3` Valence Ruling (`PR #9710`)

On 2026-11-27 (`docs/coordination/owner-rulings.md` row 22; `QOU.MassTheory.NucleusBondValence`,
`PR #9710`), the owner ruled that the production nucleus bond count (gap `G5`) is fixed by the
colour valence cap **`T3`**: each quark strand carries at most one inter-nucleon bond with a
distinct colour label at each nucleon, bounding inter-nucleon bonds by `3⌊A / 2⌋` (`1.5` per
nucleon; `V6` is not adopted without a corpus derivation).

At `A = 4m` (`m` disjoint `(2p, 2n)` `K₄` α-quartets), `3⌊4m / 2⌋ = 6m` coincides identically
with the `6m` internal edges of the `m` disjoint `K₄` tetrahedra (`t3_valence_cap_eq_disjoint_quartet_internal_bonds`,
`card_le_six_mul_of_t3_proper_colouring`). Consequently, the surface-corrected FCC `(111)`
inter-quartet face-contact functional packaged in `AlphaQuartetPauliWignerSaturationHypothesis`
is strictly an **exploratory macroscopic cluster-model comparison (`§3b-cond`, unwired from the
production mass table)** studied alongside the ruled `T3` valence bound — it does **not**
replace the ruled `T3` bond count unless and until a `3A`-strand derivation produces residual
inter-quartet face couplings.

## Main Results

1. **Quartet-Closed Intra-Shell Pauli–Wigner Carrier (`quartetClosedKernel`)**:
   - `quartetClosed_deuteron_eq`, `quartetClosed_triton_eq`, `quartetClosed_he3_eq`,
     `quartetClosed_b3_eq`: replacing the `j = 3` width-4 cell by `b4Quartet - φ 1 - φ 2`
     preserves `²H`, `³H`, `³He`, and `b₃ = φ 2 - 2 φ 1` identically.
   - `quartetClosed_he4_eq`, `quartetClosed_b4_eq`, `quartetClosed_b4_jump`:
     lifts every completed `(2p, 2n)` quartet to `b4Quartet` with exact 4-body cumulant
     `b₄ = b4Quartet - 4 φ 2 + 2 φ 1` and cumulant jump `b4Quartet - (φ 1 + φ 2 + φ 3)`.
   - `quartetClosed_alpha_mul`, `quartetClosed_alpha_plus_excessPairs`, and
     `quartetClosed_isobar_odd_to_even_jump`: proves linear `m * b4Quartet` α-extensivity,
     linear excess-pair slope `k * φ 1`, and the exact discrete odd-to-even isobaric jump
     `b4Quartet - (φ 1 + φ 2)` along `(2m + 1, 2m + 3) → (2m + 2, 2m + 2)`.

2. **Ruled `T3` Valence Bound vs Exploratory FCC `(111)` External Coordination (`Rˣ` & `[CommRing R]`)**:
   - `t3_valence_cap_eq_disjoint_quartet_internal_bonds` & `card_le_six_mul_of_t3_proper_colouring`:
     at `A = 4m`, the ruled `T3` colour-valence cap `3⌊A / 2⌋` (`QOU.MassTheory.NucleusBondValence`)
     equals `6m`, matching the internal edges of `m` disjoint `K₄` α-quartets.
   - `two_mul_fcc_sub_k4_external_bonds_eq`: cleared by `2` over `[CommRing R]`,
     `12 A - 3 A = 3 (3 A) = 9 A` (`3` bridges per `(111)` face across `(3 / 2) A` faces).
   - `qIntUnit_three_mul_sq` & `qSimplex_two_clearing_eq`: over `[CommRing R]` with unit `q : Rˣ`,
     `q² * [3]_q = q⁴ + q² + 1` and `([3]_q + 1) * q² = (q⁴ + q² + 1) + q²`.
   - `twoInterQuartetFaceCountCube_at_two` & `twoInterQuartetFaceCountCube_pos_of_gt_two`:
     `3 u³ - 6 u² = 3 u² (u - 2)` vanishes at `u = 2` (`A = 8`, `⁸Be` two-α dimer) and is
     strictly positive for all `u > 2` (`A > 8`).

3. **Division-Free Wigner Isospin Numerator & Isobaric Stability-Valley Strict Concavity**:
   - `wignerIsoNumerator_eq_sum_sq_sub_asym_sq` & `wignerIsoNumerator_le_sum_sq`:
     `4 Z N = (Z + N)² - (N - Z)² ≤ (Z + N)²` over `[CommRing R]`.
   - `isobaric_binding_second_diff_eq` & `isobaric_binding_second_diff_neg`:
     proves the constant negative `A²`-scaled second difference
     `-(8 sStrong + 8 aKin A + 2 cCoul A²) < 0` along every isobar `Z + N = A`.
   - `isobaric_beta_step_eq` & `isobaric_beta_exothermic_iff`: exact `A²`-scaled `β⁻` step
     and exothermicity threshold.

4. **Exploratory Conditional Saturation Synthesis (`AlphaQuartetPauliWignerSaturationHypothesis`)**:
   - Honest `§3b-cond` class over `[CommRing R]` paired with consistency witness `trivialModel`
     (Pattern 3.3), deriving `composite_nuclear_saturation_identity` and
     `alpha_decay_qValue_shell_jump`.

-- @conjecture: primary
-- Ref: [leitner2026] beans qou-v2om, qou-gpb5, qou-sbn9, qou-d9iv; QOU.MassTheory.NucleusBondValence
No numerical value enters.
-/

set_option autoImplicit false

namespace QOU.Nuclear

open QOU.MassTheory.B3ExtensiveCellSumCarrier

section QuartetClosedPauliWigner

variable {R : Type*} [CommRing R]

/-- Intra-shell cell kernel replacing the `j = 3` fourth-column entry of `φ` so that every
completed `(2p, 2n)` quartet (`r = 4`) evaluates to the `K₄` ground-state binding `b4Quartet`
while `r ∈ {1, 2, 3}` retain `0`, `φ 1`, and `φ 1 + φ 2`. -/
def quartetClosedKernel (φ : Nat → R) (b4Quartet : R) : Nat → R
  | 0 => 0
  | 1 => φ 1
  | 2 => φ 2
  | 3 => b4Quartet - φ 1 - φ 2
  | _ => 0

/-- Monomer baseline `quartetClosedKernel φ b4Quartet 0 = 0`. -/
@[simp]
theorem quartetClosedKernel_zero (φ : Nat → R) (b4Quartet : R) :
    quartetClosedKernel φ b4Quartet 0 = 0 := rfl

/-- Completed width-4 row sum of `quartetClosedKernel φ b4Quartet` equals `b4Quartet`. -/
theorem rowCellSum_quartetClosed_four (φ : Nat → R) (b4Quartet : R) :
    rowCellSum (quartetClosedKernel φ b4Quartet) 4 = b4Quartet := by
  simp [rowCellSum, quartetClosedKernel]

/-- Deuteron `(1, 1)` binding is unchanged by `K₄` quartet closure at `j = 3`. -/
theorem quartetClosed_deuteron_eq {φ : Nat → R} (h0 : φ 0 = 0) (b4Quartet : R) :
    pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 1 1 =
      pauliWignerCellSum φ 1 1 := by
  rw [pauliWignerCellSum_deuteron (quartetClosedKernel_zero φ b4Quartet),
      pauliWignerCellSum_deuteron h0]
  rfl

/-- Triton `(1, 2)` binding is unchanged by `K₄` quartet closure at `j = 3`. -/
theorem quartetClosed_triton_eq {φ : Nat → R} (h0 : φ 0 = 0) (b4Quartet : R) :
    pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 1 2 =
      pauliWignerCellSum φ 1 2 := by
  rw [pauliWignerCellSum_triton (quartetClosedKernel_zero φ b4Quartet),
      pauliWignerCellSum_triton h0]
  rfl

/-- Helium-3 `(2, 1)` binding is unchanged by `K₄` quartet closure at `j = 3`. -/
theorem quartetClosed_he3_eq {φ : Nat → R} (h0 : φ 0 = 0) (b4Quartet : R) :
    pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 2 1 =
      pauliWignerCellSum φ 2 1 := by
  rw [pauliWignerCellSum_he3 (quartetClosedKernel_zero φ b4Quartet),
      pauliWignerCellSum_he3 h0]
  rfl

/-- Helium-4 `(2, 2)` evaluates to the `K₄` tetrahedral ground-state energy `b4Quartet`. -/
theorem quartetClosed_he4_eq (φ : Nat → R) (b4Quartet : R) :
    pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 2 2 = b4Quartet := by
  rw [pauliWignerCellSum_he4 (quartetClosedKernel_zero φ b4Quartet)]
  unfold quartetClosedKernel
  ring

/-- Connected 3-body cumulant `b₃` is preserved identically under `K₄` quartet closure:
`b₃ = φ 2 - 2 φ 1`. -/
theorem quartetClosed_b3_eq (φ : Nat → R) (b4Quartet : R) :
    b3Sym (pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 1 1)
      (pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 1 2) =
      φ 2 - 2 * φ 1 := by
  rw [pauliWigner_b3_eq (quartetClosedKernel_zero φ b4Quartet)]
  rfl

/-- Connected 4-body cumulant under `K₄` quartet closure:
`b₄ = b4Quartet - 4 φ 2 + 2 φ 1` (`= b4Quartet - 4 (φ 1 + φ 2) + 6 φ 1`). -/
theorem quartetClosed_b4_eq (φ : Nat → R) (b4Quartet : R) :
    b4Sym (pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 1 1)
      (pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 1 2)
      (pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 2 2) =
      b4Quartet - 4 * φ 2 + 2 * φ 1 := by
  rw [pauliWigner_b4_eq (quartetClosedKernel_zero φ b4Quartet)]
  unfold quartetClosedKernel
  ring

/-- Exact 4-body cumulant enhancement relative to the bare intra-shell kernel `φ`:
`b₄(quartetClosed) - b₄(φ) = b4Quartet - (φ 1 + φ 2 + φ 3)`. -/
theorem quartetClosed_b4_jump {φ : Nat → R} (h0 : φ 0 = 0) (b4Quartet : R) :
    b4Sym (pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 1 1)
      (pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 1 2)
      (pauliWignerCellSum (quartetClosedKernel φ b4Quartet) 2 2) -
    b4Sym (pauliWignerCellSum φ 1 1)
      (pauliWignerCellSum φ 1 2)
      (pauliWignerCellSum φ 2 2) =
      b4Quartet - (φ 1 + φ 2 + φ 3) := by
  rw [quartetClosed_b4_eq φ b4Quartet, pauliWigner_b4_eq h0]
  ring

/-- Exact multi-α extensivity plus excess neutron-pair slope under `K₄` quartet closure:
`S(2m, 2m + 2k) = m * b4Quartet + k * φ 1`. -/
theorem quartetClosed_alpha_plus_excessPairs (φ : Nat → R) (b4Quartet : R) (m k : Nat) :
    pauliWignerCellSum (quartetClosedKernel φ b4Quartet) (2 * m) (2 * m + 2 * k) =
      (m : R) * b4Quartet + (k : R) * φ 1 := by
  rw [pauliWignerCellSum_alpha_plus_excessPairs (quartetClosedKernel_zero φ b4Quartet) m k]
  unfold quartetClosedKernel
  ring

/-- Exact linear α-conjugate extensivity `S(2m, 2m) = m * b4Quartet`. -/
theorem quartetClosed_alpha_mul (φ : Nat → R) (b4Quartet : R) (m : Nat) :
    pauliWignerCellSum (quartetClosedKernel φ b4Quartet) (2 * m) (2 * m) =
      (m : R) * b4Quartet := by
  simpa using quartetClosed_alpha_plus_excessPairs φ b4Quartet m 0

/-- Evaluation of `pauliWignerCellSum` on the odd-odd isobaric neighbour `(2m + 1, 2m + 3)`:
`m` completed width-4 quartets plus one width-3 shell and one monomer shell. -/
theorem quartetClosed_odd_plus_three (φ : Nat → R) (b4Quartet : R) (m : Nat) :
    pauliWignerCellSum (quartetClosedKernel φ b4Quartet) (2 * m + 1) (2 * m + 3) =
      (m : R) * b4Quartet + φ 1 + φ 2 := by
  induction m with
  | zero =>
    have hne : ¬(1 = 0 ∧ 3 = 0) := by omega
    rw [Nat.mul_zero, Nat.zero_add, Nat.zero_add, pauliWignerCellSum, dif_neg hne]
    simp [rowCellSum, quartetClosedKernel,
      pauliWignerCellSum_neutron (quartetClosedKernel_zero φ b4Quartet)]
  | succ m ih =>
    have hz : 2 * (m + 1) + 1 = (2 * m + 1) + 2 := by omega
    have hn : 2 * (m + 1) + 3 = (2 * m + 3) + 2 := by omega
    have hne : ¬((2 * m + 1) + 2 = 0 ∧ (2 * m + 3) + 2 = 0) := by omega
    have hminZ : min 2 ((2 * m + 1) + 2) = 2 := by omega
    have hminN : min 2 ((2 * m + 3) + 2) = 2 := by omega
    have hsubZ : (2 * m + 1) + 2 - 2 = 2 * m + 1 := by omega
    have hsubN : (2 * m + 3) + 2 - 2 = 2 * m + 3 := by omega
    rw [hz, hn, pauliWignerCellSum, dif_neg hne]
    simp only [hminZ, hminN, hsubZ, hsubN]
    rw [ih, rowCellSum_quartetClosed_four]
    push_cast
    ring

/-- **Isobaric odd-to-even quartet closure jump.** Transitioning from `(2m + 1, 2m + 3)` to
the α-conjugate nucleus `(2m + 2, 2m + 2)` jumps by `b4Quartet - (φ 1 + φ 2)`, isolating
algebraically why integer-shell floor truncation produces an odd-even sawtooth in `Q_{β⁻}`. -/
theorem quartetClosed_isobar_odd_to_even_jump (φ : Nat → R) (b4Quartet : R) (m : Nat) :
    pauliWignerCellSum (quartetClosedKernel φ b4Quartet) (2 * (m + 1)) (2 * (m + 1)) -
      pauliWignerCellSum (quartetClosedKernel φ b4Quartet) (2 * m + 1) (2 * m + 3) =
      b4Quartet - (φ 1 + φ 2) := by
  rw [quartetClosed_alpha_mul φ b4Quartet (m + 1), quartetClosed_odd_plus_three φ b4Quartet m]
  push_cast
  ring

end QuartetClosedPauliWigner

section FccFaceCoordinationAndThreshold

/-- **Ruled `T3` valence saturation on `m` disjoint α-quartets (`A = 4m`).**
Under the 2026-11-27 `T3` colour-valence ruling (`QOU.MassTheory.NucleusBondValence`, `PR #9710`),
the maximum proper 3-coloured bond count `3 * (A / 2)` at `A = 4m` equals `6m` — identical to the
`6` internal edges of each of the `m` disjoint `K₄` α-quartets, leaving zero unused `T3` strand
valence for inter-quartet pairwise bonds. -/
theorem t3_valence_cap_eq_disjoint_quartet_internal_bonds (m : ℕ) :
    3 * ((4 * m) / 2) = 6 * m := by
  omega

/-- Direct specialization of `QOU.MassTheory.NucleusBondValence.card_le_of_proper_colouring`
to a `4m`-nucleon system (`k = 3` colours): any proper 3-coloured inter-nucleon bond graph has at
most `6m` bonds. -/
theorem card_le_six_mul_of_t3_proper_colouring {ι V : Type*} [DecidableEq V] [Fintype V]
    (m : ℕ) (hcard : Fintype.card V = 4 * m) (E : Finset ι) (ends : ι → Finset V)
    (htwo : ∀ e ∈ E, (ends e).card = 2) (col : ι → Fin 3)
    (hproper : ∀ e ∈ E, ∀ e' ∈ E, e ≠ e' → col e = col e' → Disjoint (ends e) (ends e')) :
    E.card ≤ 6 * m := by
  have hbound :=
    QOU.MassTheory.NucleusBondValence.card_le_of_proper_colouring E ends htwo col hproper
  rw [hcard, t3_valence_cap_eq_disjoint_quartet_internal_bonds m] at hbound
  exact hbound

variable {R : Type*} [CommRing R]

/-- **Exploratory macroscopic FCC coordination identity (cleared by `2` over `[CommRing R]`).**
Subtracting twice the `(3 / 2) A` internal `K₄` quartet edges (`3 A`, matching the even-`A` `T3`
cap) from twice the `6 A` interior edges (`12 A`) of an exploratory `12`-coordinated FCC cluster
lattice leaves `9 A = 3 * (3 A)`, corresponding to `3` nucleon-pair bridges across each of
`(3 / 2) A` inter-quartet `(111)` triangular faces. -/
theorem two_mul_fcc_sub_k4_external_bonds_eq (aMass : R) :
    (12 : R) * aMass - 3 * aMass = 3 * (3 * aMass) ∧
    3 * (3 * aMass) = 9 * aMass := by
  constructor <;> ring

/-- Balanced Laurent quantum integer `[j]_q` over any commutative ring `R` with invertible
aether parameter `q : Rˣ` (`§7c`, `qou-8318`). -/
def qIntUnit (q : Rˣ) : Nat → R
  | 0 => 0
  | 1 => 1
  | 2 => (q : R) + ↑(q⁻¹)
  | 3 => (q : R) ^ 2 + 1 + (↑(q⁻¹) : R) ^ 2
  | _ => 0

/-- Exact Laurent polynomial clearing `q² * [3]_q = q⁴ + q² + 1` over `[CommRing R]` (`q : Rˣ`). -/
theorem qIntUnit_three_mul_sq (q : Rˣ) :
    (q : R) ^ 2 * qIntUnit q 3 = (q : R) ^ 4 + (q : R) ^ 2 + 1 := by
  unfold qIntUnit
  have hq : (q : R) * ↑(q⁻¹) = 1 := Units.mul_inv q
  calc
    (q : R) ^ 2 * ((q : R) ^ 2 + 1 + (↑(q⁻¹) : R) ^ 2)
        = (q : R) ^ 4 + (q : R) ^ 2 + ((q : R) * ↑(q⁻¹)) ^ 2 := by ring
    _ = (q : R) ^ 4 + (q : R) ^ 2 + 1 := by rw [hq]; ring

/-- Division-free clearing of the three-nucleon Wenzl `(111)` triangular-face weight
`1 + 1 / [3]_q = 1 + q² / (q⁴ + q² + 1)` over `[CommRing R]` (`q : Rˣ`):
`(qIntUnit q 3 + 1) * q² = (q⁴ + q² + 1) + q²`. -/
theorem qSimplex_two_clearing_eq (q : Rˣ) :
    (qIntUnit q 3 + 1) * (q : R) ^ 2 = ((q : R) ^ 4 + (q : R) ^ 2 + 1) + (q : R) ^ 2 := by
  calc
    (qIntUnit q 3 + 1) * (q : R) ^ 2
        = (q : R) ^ 2 * qIntUnit q 3 + (q : R) ^ 2 := by ring
    _ = ((q : R) ^ 4 + (q : R) ^ 2 + 1) + (q : R) ^ 2 := by rw [qIntUnit_three_mul_sq q]

/-- Twice the surface-corrected exploratory inter-quartet `(111)` face count
`2 * ((3 / 2) A - 3 A^{2/3})` evaluated at `A = u³`, i.e. `3 u³ - 6 u²` over `[CommRing R]`. -/
def twoInterQuartetFaceCountCube (u : R) : R := 3 * u ^ 3 - 6 * u ^ 2

/-- Factored polynomial form `twoInterQuartetFaceCountCube u = 3 u² (u - 2)`. -/
theorem twoInterQuartetFaceCountCube_factored (u : R) :
    twoInterQuartetFaceCountCube u = 3 * u ^ 2 * (u - 2) := by
  unfold twoInterQuartetFaceCountCube
  ring

/-- At `u = 2` (`A = 2³ = 8`, `⁸Be` two-α dimer), the surface-corrected inter-quartet face
count vanishes identically (`3 · 8 - 6 · 4 = 0`). -/
theorem twoInterQuartetFaceCountCube_at_two :
    twoInterQuartetFaceCountCube (2 : R) = 0 := by
  unfold twoInterQuartetFaceCountCube
  ring

/-- Over any strict ordered commutative ring, for all `u > 2` (`A = u³ > 8`), the doubled
surface-corrected inter-quartet face count is strictly positive. -/
theorem twoInterQuartetFaceCountCube_pos_of_gt_two [LinearOrder R] [IsStrictOrderedRing R]
    {u : R} (hu : 2 < u) :
    0 < twoInterQuartetFaceCountCube u := by
  rw [twoInterQuartetFaceCountCube_factored u]
  have hu0 : 0 < u := by linarith
  have hsub : 0 < u - 2 := by linarith
  have h3 : (0 : R) < 3 := by norm_num
  exact mul_pos (mul_pos h3 (sq_pos_of_pos hu0)) hsub

end FccFaceCoordinationAndThreshold

section WignerIsospinAndValleyConcavity

variable {R : Type*} [CommRing R]

/-- Division-free Wigner isoscalar quartet numerator `4 Z N` over `[CommRing R]`. -/
def wignerIsoNumerator (zProt nNeut : R) : R :=
  4 * zProt * nNeut

/-- **Exact quadratic isobaric parabola identity over `[CommRing R]`.**
`4 Z N = (Z + N)² - (N - Z)²`. -/
theorem wignerIsoNumerator_eq_sum_sq_sub_asym_sq (zProt nNeut : R) :
    wignerIsoNumerator zProt nNeut = (zProt + nNeut) ^ 2 - (nNeut - zProt) ^ 2 := by
  unfold wignerIsoNumerator
  ring

/-- Symmetric `Z = N` matter saturates the Wigner numerator `4 Z² = (Z + Z)²`. -/
theorem wignerIsoNumerator_symmetric (zProt : R) :
    wignerIsoNumerator zProt zProt = (zProt + zProt) ^ 2 := by
  unfold wignerIsoNumerator
  ring

/-- Pure neutron matter `(0, N)` has zero Wigner quartet numerator (`wignerIsoNumerator 0 N = 0`). -/
theorem wignerIsoNumerator_pure_neutron (nNeut : R) :
    wignerIsoNumerator 0 nNeut = 0 := by
  unfold wignerIsoNumerator
  ring

/-- Over any strict ordered commutative ring, `4 Z N ≤ (Z + N)²`. -/
theorem wignerIsoNumerator_le_sum_sq [LinearOrder R] [IsStrictOrderedRing R]
    (zProt nNeut : R) :
    wignerIsoNumerator zProt nNeut ≤ (zProt + nNeut) ^ 2 := by
  rw [wignerIsoNumerator_eq_sum_sq_sub_asym_sq]
  have hsq : 0 ≤ (nNeut - zProt) ^ 2 := sq_nonneg _
  linarith

/-- Division-free `A²`-scaled isobaric binding polynomial at fixed mass number `A = Z + N`:
`A² B_A(Z) = sStrong * (4 Z (A - Z)) - aKin * A * (A - 2 Z)² - cCoul * A² * Z (Z - 1)`. -/
def aSqIsobaricBindingParabola (sStrong aKin cCoul aMass zProt : R) : R :=
  sStrong * (4 * zProt * (aMass - zProt)) -
    aKin * aMass * (aMass - 2 * zProt) ^ 2 -
    cCoul * aMass ^ 2 * zProt * (zProt - 1)

/-- **Constant negative `A²`-scaled second difference along an isobar over `[CommRing R]`.**
`A² (B(Z + 1) - 2 B(Z) + B(Z - 1)) = -(8 sStrong + 8 aKin A + 2 cCoul A²)`. -/
theorem isobaric_binding_second_diff_eq (sStrong aKin cCoul aMass zProt : R) :
    aSqIsobaricBindingParabola sStrong aKin cCoul aMass (zProt + 1) -
      2 * aSqIsobaricBindingParabola sStrong aKin cCoul aMass zProt +
      aSqIsobaricBindingParabola sStrong aKin cCoul aMass (zProt - 1) =
      -(8 * sStrong + 8 * aKin * aMass + 2 * cCoul * aMass ^ 2) := by
  unfold aSqIsobaricBindingParabola
  ring

/-- **Strict discrete concavity of the nuclear stability valley.** Over any strict ordered
commutative ring, whenever `0 < A`, `0 ≤ sStrong`, `0 < aKin`, and `0 ≤ cCoul`, the `A²`-scaled
second difference along the isobar is strictly negative. -/
theorem isobaric_binding_second_diff_neg [LinearOrder R] [IsStrictOrderedRing R]
    {sStrong aKin cCoul aMass zProt : R}
    (ha : 0 < aMass) (hs : 0 ≤ sStrong) (hk : 0 < aKin) (hc : 0 ≤ cCoul) :
    aSqIsobaricBindingParabola sStrong aKin cCoul aMass (zProt + 1) -
      2 * aSqIsobaricBindingParabola sStrong aKin cCoul aMass zProt +
      aSqIsobaricBindingParabola sStrong aKin cCoul aMass (zProt - 1) < 0 := by
  rw [isobaric_binding_second_diff_eq]
  have term1 : 0 ≤ 8 * sStrong := by positivity
  have term2 : 0 < 8 * aKin * aMass := by positivity
  have term3 : 0 ≤ 2 * cCoul * aMass ^ 2 := by positivity
  linarith

/-- **Exact `A²`-scaled `β⁻` binding difference `(Z, A - Z) → (Z + 1, A - Z - 1)` over `[CommRing R]`.** -/
theorem isobaric_beta_step_eq (sStrong aKin cCoul aMass zProt : R) :
    aSqIsobaricBindingParabola sStrong aKin cCoul aMass (zProt + 1) -
      aSqIsobaricBindingParabola sStrong aKin cCoul aMass zProt =
      4 * (sStrong + aKin * aMass) * (aMass - 2 * zProt - 1) -
        2 * cCoul * aMass ^ 2 * zProt := by
  unfold aSqIsobaricBindingParabola
  ring

/-- **Isobaric `β⁻` exothermicity threshold (`A²`-cleared over `[CommRing R]`).** For single-nucleon
kinematic split `deltaNP`, `A² Q_{β⁻} = A² deltaNP + A² (B(Z + 1) - B(Z)) > 0` holds iff the
symmetry-restoring gain `4 (sStrong + aKin A) (A - 2 Z - 1)` plus `A² deltaNP` exceeds the
Coulomb increment `2 cCoul A² Z`. -/
theorem isobaric_beta_exothermic_iff [LinearOrder R] [IsStrictOrderedRing R]
    (deltaNP sStrong aKin cCoul aMass zProt : R) :
    0 < aMass ^ 2 * deltaNP +
      (aSqIsobaricBindingParabola sStrong aKin cCoul aMass (zProt + 1) -
        aSqIsobaricBindingParabola sStrong aKin cCoul aMass zProt) ↔
      2 * cCoul * aMass ^ 2 * zProt <
        aMass ^ 2 * deltaNP + 4 * (sStrong + aKin * aMass) * (aMass - 2 * zProt - 1) := by
  rw [isobaric_beta_step_eq]
  constructor <;> intro h <;> linarith

end WignerIsospinAndValleyConcavity

section ConditionalSaturationSynthesis

/-- **Exploratory conditional hypothesis class (`§3b-cond`, unwired): macroscopic cluster-model
comparison alongside the ruled `T3` valence bound (`QOU.MassTheory.NucleusBondValence`, `PR #9710`).**

Stated division-free over `[CommRing R]` by clearing `4 A²`: packages the four zero-parameter
macroscopic cluster hypotheses connecting:
1. intra-quartet `K₄` ground-state energy (`aMass * b4Quartet`),
2. exploratory surface-corrected FCC `(111)` triangular-face inter-quartet contacts (`4 * mFace * phi2Wenzl`),
3. Wigner isospin numerator `4 Z N` plus 3D Pauli Fermi kinetic surplus `dTPauli`,
4. valence pairing `deltaPair`, Strutinsky shell correction `deltaShell`, minus FCC Coulomb `eCoulomb`. -/
class AlphaQuartetPauliWignerSaturationHypothesis (R : Type*) [CommRing R] where
  /-- Mass number `A`, proton count `Z`, and neutron count `N`. -/
  aMass : R
  zProt : R
  nNeut : R
  mass_sum : zProt + nNeut = aMass
  /-- Intra-quartet `K₄` energy `b4Quartet` and three-nucleon Wenzl face energy `phi2Wenzl`. -/
  b4Quartet : R
  phi2Wenzl : R
  /-- Surface-corrected exploratory inter-quartet `(111)` face count `mFace`. -/
  mFace : R
  /-- 3D Pauli Fermi kinetic asymmetry surplus `dTPauli`, valence pairing `deltaPair`,
  Nilsson–Strutinsky shell stabilization `deltaShell`, and discrete-proton FCC Coulomb
  energy `eCoulomb`. -/
  dTPauli : R
  deltaPair : R
  deltaShell : R
  eCoulomb : R
  /-- Total composite nuclear binding energy `bindingTotal` and `4 A²`-cleared assembly law. -/
  bindingTotal : R
  assembly :
    4 * aMass ^ 2 * bindingTotal =
      (aMass * b4Quartet + 4 * mFace * phi2Wenzl) * wignerIsoNumerator zProt nNeut +
        4 * aMass ^ 2 * (-dTPauli + deltaPair + deltaShell - eCoulomb)

/-- **Trivial model (Pattern 3.3 consistency witness).**
Certifies `AlphaQuartetPauliWignerSaturationHypothesis R` is consistent over every `[CommRing R]`.
Provided as a `def` (never `instance`) so it cannot pollute typeclass resolution. -/
-- Ref: [leitner2026] beans qou-v2om, qou-d9iv
def trivialModel (R : Type*) [CommRing R] : AlphaQuartetPauliWignerSaturationHypothesis R where
  aMass := 0
  zProt := 0
  nNeut := 0
  mass_sum := by ring
  b4Quartet := 0
  phi2Wenzl := 0
  mFace := 0
  dTPauli := 0
  deltaPair := 0
  deltaShell := 0
  eCoulomb := 0
  bindingTotal := 0
  assembly := by
    unfold wignerIsoNumerator
    ring

/-- **Composite nuclear saturation identity (conditional on
`AlphaQuartetPauliWignerSaturationHypothesis`, division-free over `[CommRing R]`).**

Expands `4 A² bindingTotal` into its symmetric strong core `(A b4Quartet + 4 mFace phi2Wenzl) A²`,
exact Wigner potential symmetry deficit `-(A b4Quartet + 4 mFace phi2Wenzl) (N - Z)²`, and
`4 A² (-dTPauli + deltaPair + deltaShell - eCoulomb)`. -/
theorem composite_nuclear_saturation_identity (R : Type*) [CommRing R]
    [H : AlphaQuartetPauliWignerSaturationHypothesis R] :
    4 * H.aMass ^ 2 * H.bindingTotal =
      (H.aMass * H.b4Quartet + 4 * H.mFace * H.phi2Wenzl) * H.aMass ^ 2 -
        (H.aMass * H.b4Quartet + 4 * H.mFace * H.phi2Wenzl) * (H.nNeut - H.zProt) ^ 2 +
        4 * H.aMass ^ 2 * (-H.dTPauli + H.deltaPair + H.deltaShell - H.eCoulomb) := by
  rw [H.assembly, wignerIsoNumerator_eq_sum_sq_sub_asym_sq, H.mass_sum]
  ring

/-- **Exact `Q_α` shell-jump decomposition.** Over any commutative ring `R`, if total binding
splits into smooth macroscopic saturation `bSmooth` plus shell stabilization `bShell` (with
`bShell = 0` on the doubly-magic `⁴He` quartet), then `Q_α = B_daughter + B_α - B_parent` equals
the smooth macroscopic `Q_α` plus `bShell_daughter - bShell_parent`. -/
theorem alpha_decay_qValue_shell_jump {R : Type*} [CommRing R]
    (bSmoothParent bSmoothDaughter bAlpha bShellParent bShellDaughter : R) :
    (bSmoothDaughter + bShellDaughter) + bAlpha - (bSmoothParent + bShellParent) =
      (bSmoothDaughter + bAlpha - bSmoothParent) + (bShellDaughter - bShellParent) := by
  ring

end ConditionalSaturationSynthesis

end QOU.Nuclear
