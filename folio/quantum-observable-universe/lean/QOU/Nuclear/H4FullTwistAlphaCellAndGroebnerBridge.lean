import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic
import QOU.MassTheory.H4GPMTModifiedDimensionCumulants
import QOU.Nuclear.AlphaSimplexCoordinationDerivation

/-!
# `H_4(q)` Full-Twist $\Delta_4^2$ Singlet Cell, GPMT Casimir Completion & Inductive Gröbner–Shirshov Bridge

This module formalizes the representation-theoretic and algebraic core of Lane N1 (`qou-ki22` under
Epic `qou-8ffl`), uniting the four-strand Iwahori–Hecke full-twist $\Delta_4^2 = (T_1 T_2 T_3)^4$
spectrum and Geer–Patureau-Mirand–Turaev (GPMT) modified trace on $H_4(q)$ with the inductive
$2 \times 2$ transfer-matrix Gröbner–Shirshov reduction for multi-crossing nuclear braids, with
zero free parameters, zero empirical fitting, zero axioms, and zero `sorry`.

## Main Results

1. **Section 1 — Partitions of `4`, SYT Dimensions, Content Sums & Wigner-$SU(4)$ Conjugation Duality:**
   * Enumerates the five partitions `H4Partition` (`(4)`, `(3,1)`, `(2,2)`, `(2,1^2)`, `(1^4)`),
     their standard Young tableau dimensions `(1, 3, 2, 3, 1)` satisfying
     `∑ d_λ^2 = 24 = 4!` (`h4Partition_sum_sytDim_sq`), and their explicit 4-box Young diagrams
     with exact content sums `∑ c(□) ∈ {+6, +2, 0, -2, -6}` (`contentSum_values`).
   * Proves transpose conjugation symmetry `sytDim_conj`, `contentSum_conj`, and the Wigner-$SU(4)$
     antisymmetrization pairing `(4)' = (1^4)` (`wignerSU4_singlet_conjugate_pairing`).

2. **Section 2 — Explicit Specht Matrix Action on $H_4(q)$ & Full-Twist $\Delta_4^2$ Framing Eigenvalues:**
   * Constructs Laurent-polynomial Specht matrix representations `(specht4, specht31, specht22,
     specht211, specht1111)` over any field `K` (`q ≠ 0`), proving every Hecke quadratic relation
     `G_i^2 = (q - q⁻¹) G_i + 1` and every Artin braid relation (`G_1 G_2 G_1 = G_2 G_1 G_2`,
     `G_2 G_3 G_2 = G_3 G_2 G_3`, `G_1 G_3 = G_3 G_1`).
   * Verifies all 25 irreducible character values on `(1, T_1, T_1 T_2, T_1 T_3, T_1 T_2 T_3)` via
     `Matrix.trace` and proves directly by matrix multiplication that the 4-strand full twist
     `fullTwist4 G_1 G_2 G_3 = (G_1 G_2 G_3)^4` acts centrally on each Specht block by the scalar
     `q^{2 ∑ c(□)} ∈ {q^{12}, q^4, 1, q^{-4}, q^{-12}}` (`specht4_fullTwist` .. `specht1111_fullTwist`).

3. **Section 3 — Closed-Form Rational Expressions in `ℚ(q)` for Convention-D + GPMT Full-Twist & Casimir:**
   * Proves exact factored rational identities for the Convention-D two-row full-twist traces
     `trConventionDFullTwistPos_closed_form`, `trConventionDFullTwistNeg_closed_form`, their
     palindromic `q ↔ q⁻¹` duality, and the two-row Casimir identity
     `casimirConventionD q = 12 (q^4 + 1) / (q^2 + 1)^2` (`casimirConventionD_closed_form`).
   * Proves exact rational identities and strict `q > 0` positivity for the GPMT-completed
     `≥ 3`-row full-twist functionals `gpmtRow3FullTwistPos`, `gpmtRow3FullTwistNeg`, the
     GPMT Casimir functional `casimirGPMTRow3`, and the Wigner-$SU(4)$ `(1^4)` singlet channel
     `wignerSingletGPMTFullTwistPos`.

4. **Section 4 — Inductive Transfer-Matrix / Gröbner–Shirshov Multi-Crossing Reduction:**
   * Formalizes the polynomial recurrence `C^2 = h C + 1 ⟹ C^k = heckePowerA h k • C + heckePowerB h k • 1`
     (`hecke_pow_eq_linear_nf`) over any `R`-algebra `A`, its `2 × 2` matrix realization `tmBase`,
     and the general crossing transfer matrix `tmGeneral h c d = !![c h + d, c; c, d]` compressing
     an arbitrary `m`-crossing product `∏ (c_r C + d_r)` into two normal-form terms in `O(m)` steps
     (`crossingChain_eq_tmProduct_nf`).
   * Proves the inverse crossing quadratic `C_inv^2 = (-h) C_inv + 1` (`hecke_inv_sq_eq`) and the
     achiral `gg` crossing square collapse `(C - (h/2) • 1)^2 = (1 + h^2 / 4) • 1` (`achiralGG_sq_scalar`),
     eliminating the linear Hecke generator term at even crossing multiplicities.

5. **Section 5 — Multi-$\alpha$ Cluster Threshold Bridge (`^8Be` vs `2 ^4He` and `^12C` vs `3 ^4He`):**
   * Connects to `AlphaSimplexCoordinationDerivation`, proving that intra-$\alpha$ strong cell
     energies cancel identically in `N_α`-cluster breakup thresholds (`be8_two_alpha_threshold_diff`,
     `c12_three_alpha_threshold_diff`), isolating `^8Be` instability (`1` bridge edge vs Coulomb jump)
     from `^12C` triangular `K_3` stability (`3` bridge edges + `1` inter-cluster triangle).
-/

namespace QOU.Nuclear.H4FullTwistAlphaCellAndGroebnerBridge

open Matrix BigOperators
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace (zD dMod111)
open QOU.MassTheory.GPMTThreeRowCumulantBridge (sq_add_one_pos pow_four_add_sq_add_one_pos)
open QOU.MassTheory.H4GPMTModifiedDimensionCumulants
open QOU.Nuclear.AlphaSimplexCoordinationDerivation

-- ============================================================================
-- § 1. The 5 Partitions of 4, SYT Dimensions, Content Sums & SU(4) Duality
-- ============================================================================

/-- The five integer partitions of `4` indexing the irreducible Specht modules of `H_4(q)`. -/
inductive H4Partition : Type
  | p4 : H4Partition
  | p31 : H4Partition
  | p22 : H4Partition
  | p211 : H4Partition
  | p1111 : H4Partition
  deriving DecidableEq, Repr

instance : Fintype H4Partition where
  elems := {.p4, .p31, .p22, .p211, .p1111}
  complete := by
    intro x
    cases x <;> decide

/-- There are `5` partitions of `4`. -/
theorem card_h4Partition : Fintype.card H4Partition = 5 := by
  decide

/-- Standard Young tableau (Specht) dimension `d_λ` for each partition `λ ⊢ 4`. -/
def sytDim : H4Partition → ℕ
  | .p4 => 1
  | .p31 => 3
  | .p22 => 2
  | .p211 => 3
  | .p1111 => 1

/-- Number of Young-diagram rows `ℓ(λ)` for each partition `λ ⊢ 4`. -/
def rowCount : H4Partition → ℕ
  | .p4 => 1
  | .p31 => 2
  | .p22 => 2
  | .p211 => 3
  | .p1111 => 4

/-- Transpose (conjugate) partition `λ'` obtained by reflecting the Young diagram across the main diagonal. -/
def conjPartition : H4Partition → H4Partition
  | .p4 => .p1111
  | .p31 => .p211
  | .p22 => .p22
  | .p211 => .p31
  | .p1111 => .p4

/-- Explicit 0-indexed `(row, col)` cell list of the 4-box Young diagram of `λ ⊢ 4`. -/
def youngCells : H4Partition → List (ℕ × ℕ)
  | .p4 => [(0, 0), (0, 1), (0, 2), (0, 3)]
  | .p31 => [(0, 0), (0, 1), (0, 2), (1, 0)]
  | .p22 => [(0, 0), (0, 1), (1, 0), (1, 1)]
  | .p211 => [(0, 0), (0, 1), (1, 0), (2, 0)]
  | .p1111 => [(0, 0), (1, 0), (2, 0), (3, 0)]

/-- Content `c(r, k) = k - r` of a Young-diagram cell `(r, k)` in 0-indexed coordinates. -/
def boxContent (cell : ℕ × ℕ) : ℤ :=
  (cell.2 : ℤ) - (cell.1 : ℤ)

/-- Total Young-diagram content sum `κ_λ = ∑_{□ ∈ λ} c(□)` of a partition `λ ⊢ 4`. -/
def contentSum (lam : H4Partition) : ℤ :=
  ((youngCells lam).map boxContent).sum

/-- Full-twist framing exponent `2 κ_λ = 2 ∑_{□ ∈ λ} c(□)` of `Δ_4^2 = (T_1 T_2 T_3)^4` on `S^λ`. -/
def fullTwistExponent (lam : H4Partition) : ℤ :=
  2 * contentSum lam

/-- Every Young diagram of `λ ⊢ 4` consists of `4` boxes. -/
theorem youngCells_length_eq_four (lam : H4Partition) :
    (youngCells lam).length = 4 := by
  cases lam <;> rfl

/-- Wedderburn dimension identity on `H_4(q)`: `∑_{λ ⊢ 4} d_λ^2 = 1 + 9 + 4 + 9 + 1 = 24 = 4!`. -/
theorem h4Partition_sum_sytDim_sq :
    (∑ lam : H4Partition, (sytDim lam) ^ 2) = 24 ∧ Nat.factorial 4 = 24 := by
  decide

/-- Sum of irreducible Specht dimensions of `H_4(q)`: `1 + 3 + 2 + 3 + 1 = 10`. -/
theorem h4Partition_sum_sytDim :
    (∑ lam : H4Partition, sytDim lam) = 10 := by
  decide

/-- Exact Young-diagram content sums `κ_λ ∈ {+6, +2, 0, -2, -6}` across the five partitions of `4`. -/
theorem contentSum_values :
    (contentSum .p4, contentSum .p31, contentSum .p22, contentSum .p211, contentSum .p1111) =
      (6, 2, 0, -2, -6) := by
  decide

/-- Exact 4-strand full-twist framing exponents `2 κ_λ ∈ {+12, +4, 0, -4, -12}`. -/
theorem fullTwistExponent_values :
    (fullTwistExponent .p4, fullTwistExponent .p31, fullTwistExponent .p22,
      fullTwistExponent .p211, fullTwistExponent .p1111) = (12, 4, 0, -4, -12) := by
  decide

/-- Transpose conjugation is an involution preserving Specht dimension and negating content sum. -/
theorem conjPartition_properties (lam : H4Partition) :
    conjPartition (conjPartition lam) = lam ∧
    sytDim (conjPartition lam) = sytDim lam ∧
    contentSum (conjPartition lam) = -contentSum lam ∧
    fullTwistExponent (conjPartition lam) = -fullTwistExponent lam := by
  cases lam <;> decide

/-- Wigner-$SU(4)$ / Pauli antisymmetrization pairing on `A = 4` nucleons:
the totally symmetric spatial `s`-wave sector `(4)` (`κ = +6`) pairs under total antisymmetry
with the unique 1-dimensional spin-isospin singlet `(1^4)` (`d_{(1^4)} = 1`, `2 κ_{(1^4)} = -12`). -/
theorem wignerSU4_singlet_conjugate_pairing :
    conjPartition .p4 = .p1111 ∧
    sytDim .p4 = 1 ∧
    sytDim .p1111 = 1 ∧
    rowCount .p1111 = 4 ∧
    fullTwistExponent .p4 = 12 ∧
    fullTwistExponent .p1111 = -12 := by
  decide

-- ============================================================================
-- § 2. Explicit Specht Matrix Action on H_4(q) & Full-Twist Δ_4^2 Eigenvalues
-- ============================================================================

section SpechtRepresentationsAndFullTwist

variable {K : Type*} [Field K]

/-- 4-strand Coxeter braid element `C_4 = G_1 G_2 G_3` in any matrix representation. -/
def coxeter4 {n : ℕ} (G1 G2 G3 : Matrix (Fin n) (Fin n) K) : Matrix (Fin n) (Fin n) K :=
  G1 * G2 * G3

/-- 4-strand positive full-twist element `Δ_4^2 = (G_1 G_2 G_3)^4` of word length `12 = 2 C(4, 2)`. -/
def fullTwist4 {n : ℕ} (G1 G2 G3 : Matrix (Fin n) (Fin n) K) : Matrix (Fin n) (Fin n) K :=
  (coxeter4 G1 G2 G3) ^ 4

/-- Predicates asserting the defining quadratic and Artin braid relations of `H_4(q)`
(`G_i^2 = (q - q⁻¹) G_i + 1`) on an `n × n` matrix triple `(G1, G2, G3)`. -/
def IsH4MatrixRep {n : ℕ} (q : K) (G1 G2 G3 : Matrix (Fin n) (Fin n) K) : Prop :=
  G1 * G1 = (q - q⁻¹) • G1 + 1 ∧
  G2 * G2 = (q - q⁻¹) • G2 + 1 ∧
  G3 * G3 = (q - q⁻¹) • G3 + 1 ∧
  G1 * G2 * G1 = G2 * G1 * G2 ∧
  G2 * G3 * G2 = G3 * G2 * G3 ∧
  G1 * G3 = G3 * G1

/-- 1D trivial/symmetric `(4)` Specht generator `G_i = [q]`. -/
def specht4Gen (q : K) : Matrix (Fin 1) (Fin 1) K
  | _, _ => q

/-- 1D sign/antisymmetric `(1^4)` Specht generator `G_i = [-q⁻¹]`. -/
def specht1111Gen (q : K) : Matrix (Fin 1) (Fin 1) K
  | _, _ => -q⁻¹

/-- 3D standard `(3,1)` Specht generator `T_1` over `K[q, q⁻¹]`. -/
def specht31Gen1 (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨0, _⟩ => -q⁻¹
  | ⟨0, _⟩, ⟨1, _⟩ => q
  | ⟨1, _⟩, ⟨1, _⟩ => q
  | ⟨2, _⟩, ⟨2, _⟩ => q
  | _, _ => 0

/-- 3D standard `(3,1)` Specht generator `T_2` over `K[q, q⁻¹]`. -/
def specht31Gen2 (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨0, _⟩ => q
  | ⟨1, _⟩, ⟨0, _⟩ => q⁻¹
  | ⟨1, _⟩, ⟨1, _⟩ => -q⁻¹
  | ⟨1, _⟩, ⟨2, _⟩ => q
  | ⟨2, _⟩, ⟨2, _⟩ => q
  | _, _ => 0

/-- 3D standard `(3,1)` Specht generator `T_3` over `K[q, q⁻¹]`. -/
def specht31Gen3 (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨0, _⟩ => q
  | ⟨1, _⟩, ⟨1, _⟩ => q
  | ⟨2, _⟩, ⟨1, _⟩ => q⁻¹
  | ⟨2, _⟩, ⟨2, _⟩ => -q⁻¹
  | _, _ => 0

/-- 2D rectangular `(2,2)` Specht generator `T_1` over `K[q, q⁻¹]`. -/
def specht22Gen1 (q : K) : Matrix (Fin 2) (Fin 2) K
  | ⟨0, _⟩, ⟨0, _⟩ => -q⁻¹
  | ⟨0, _⟩, ⟨1, _⟩ => q
  | ⟨1, _⟩, ⟨1, _⟩ => q
  | _, _ => 0

/-- 2D rectangular `(2,2)` Specht generator `T_2` over `K[q, q⁻¹]`. -/
def specht22Gen2 (q : K) : Matrix (Fin 2) (Fin 2) K
  | ⟨0, _⟩, ⟨0, _⟩ => q
  | ⟨1, _⟩, ⟨0, _⟩ => q⁻¹
  | ⟨1, _⟩, ⟨1, _⟩ => -q⁻¹
  | _, _ => 0

/-- 2D rectangular `(2,2)` Specht generator `T_3 = T_1` via the `S_4 → S_3` Klein-four quotient. -/
def specht22Gen3 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  specht22Gen1 q

/-- 3D hook `(2,1^2)` Specht generator `T_1` obtained from `(3,1)` under `q ↦ -q⁻¹`. -/
def specht211Gen1 (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨0, _⟩ => q
  | ⟨0, _⟩, ⟨1, _⟩ => -q⁻¹
  | ⟨1, _⟩, ⟨1, _⟩ => -q⁻¹
  | ⟨2, _⟩, ⟨2, _⟩ => -q⁻¹
  | _, _ => 0

/-- 3D hook `(2,1^2)` Specht generator `T_2` over `K[q, q⁻¹]`. -/
def specht211Gen2 (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨0, _⟩ => -q⁻¹
  | ⟨1, _⟩, ⟨0, _⟩ => -q
  | ⟨1, _⟩, ⟨1, _⟩ => q
  | ⟨1, _⟩, ⟨2, _⟩ => -q⁻¹
  | ⟨2, _⟩, ⟨2, _⟩ => -q⁻¹
  | _, _ => 0

/-- 3D hook `(2,1^2)` Specht generator `T_3` over `K[q, q⁻¹]`. -/
def specht211Gen3 (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨0, _⟩ => -q⁻¹
  | ⟨1, _⟩, ⟨1, _⟩ => -q⁻¹
  | ⟨2, _⟩, ⟨1, _⟩ => -q
  | ⟨2, _⟩, ⟨2, _⟩ => q
  | _, _ => 0

/-- The 1D `(4)` representation satisfies all `H_4(q)` quadratic and braid relations. -/
theorem specht4_isH4MatrixRep (q : K) (hq : q ≠ 0) :
    IsH4MatrixRep q (specht4Gen q) (specht4Gen q) (specht4Gen q) := by
  refine ⟨?_, ?_, ?_, rfl, rfl, rfl⟩ <;>
    · ext i j; fin_cases i; fin_cases j
      simp only [specht4Gen, Matrix.mul_apply, Fin.sum_univ_one,
        Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul]
      field_simp [hq]; ring

private lemma specht31_rel1 (q : K) (hq : q ≠ 0) :
    specht31Gen1 q * specht31Gen1 q = (q - q⁻¹) • specht31Gen1 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht31Gen1, Matrix.mul_apply, Fin.sum_univ_three,
        Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
        Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
      try (field_simp [hq]; ring)

private lemma specht31_rel2 (q : K) (hq : q ≠ 0) :
    specht31Gen2 q * specht31Gen2 q = (q - q⁻¹) • specht31Gen2 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht31Gen2, Matrix.mul_apply, Fin.sum_univ_three,
        Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
        Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
      try (field_simp [hq]; ring)

private lemma specht31_rel3 (q : K) (hq : q ≠ 0) :
    specht31Gen3 q * specht31Gen3 q = (q - q⁻¹) • specht31Gen3 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht31Gen3, Matrix.mul_apply, Fin.sum_univ_three,
        Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
        Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
      try (field_simp [hq]; ring)

private lemma specht31_braid12 (q : K) (hq : q ≠ 0) :
    specht31Gen1 q * specht31Gen2 q * specht31Gen1 q =
      specht31Gen2 q * specht31Gen1 q * specht31Gen2 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht31Gen1, specht31Gen2, Matrix.mul_apply, Fin.sum_univ_three]
      try (field_simp [hq]; ring)

private lemma specht31_braid23 (q : K) (hq : q ≠ 0) :
    specht31Gen2 q * specht31Gen3 q * specht31Gen2 q =
      specht31Gen3 q * specht31Gen2 q * specht31Gen3 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht31Gen2, specht31Gen3, Matrix.mul_apply, Fin.sum_univ_three]
      try (field_simp [hq]; ring)

private lemma specht31_comm13 (q : K) :
    specht31Gen1 q * specht31Gen3 q = specht31Gen3 q * specht31Gen1 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht31Gen1, specht31Gen3, Matrix.mul_apply, Fin.sum_univ_three]
      ring

/-- The 3D `(3,1)` representation satisfies all `H_4(q)` quadratic and braid relations. -/
theorem specht31_isH4MatrixRep (q : K) (hq : q ≠ 0) :
    IsH4MatrixRep q (specht31Gen1 q) (specht31Gen2 q) (specht31Gen3 q) :=
  ⟨specht31_rel1 q hq, specht31_rel2 q hq, specht31_rel3 q hq,
   specht31_braid12 q hq, specht31_braid23 q hq, specht31_comm13 q⟩

/-- The 2D `(2,2)` representation satisfies all `H_4(q)` quadratic and braid relations. -/
theorem specht22_isH4MatrixRep (q : K) (hq : q ≠ 0) :
    IsH4MatrixRep q (specht22Gen1 q) (specht22Gen2 q) (specht22Gen3 q) := by
  have hq1 : specht22Gen1 q * specht22Gen1 q = (q - q⁻¹) • specht22Gen1 q + 1 := by
    ext i j; fin_cases i <;> fin_cases j <;>
      · simp only [specht22Gen1, Matrix.mul_apply, Fin.sum_univ_two,
          Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
          Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
        try (field_simp [hq]; ring)
  have hq2 : specht22Gen2 q * specht22Gen2 q = (q - q⁻¹) • specht22Gen2 q + 1 := by
    ext i j; fin_cases i <;> fin_cases j <;>
      · simp only [specht22Gen2, Matrix.mul_apply, Fin.sum_univ_two,
          Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
          Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
        try (field_simp [hq]; ring)
  have hb12 : specht22Gen1 q * specht22Gen2 q * specht22Gen1 q =
      specht22Gen2 q * specht22Gen1 q * specht22Gen2 q := by
    ext i j; fin_cases i <;> fin_cases j <;>
      · simp only [specht22Gen1, specht22Gen2, Matrix.mul_apply, Fin.sum_univ_two]
        try (field_simp [hq]; ring)
  exact ⟨hq1, hq2, hq1, hb12, hb12.symm, rfl⟩

private lemma specht211_rel1 (q : K) (hq : q ≠ 0) :
    specht211Gen1 q * specht211Gen1 q = (q - q⁻¹) • specht211Gen1 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht211Gen1, Matrix.mul_apply, Fin.sum_univ_three,
        Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
        Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
      try (field_simp [hq]; ring)

private lemma specht211_rel2 (q : K) (hq : q ≠ 0) :
    specht211Gen2 q * specht211Gen2 q = (q - q⁻¹) • specht211Gen2 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht211Gen2, Matrix.mul_apply, Fin.sum_univ_three,
        Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
        Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
      try (field_simp [hq]; ring)

private lemma specht211_rel3 (q : K) (hq : q ≠ 0) :
    specht211Gen3 q * specht211Gen3 q = (q - q⁻¹) • specht211Gen3 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht211Gen3, Matrix.mul_apply, Fin.sum_univ_three,
        Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
        Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
      try (field_simp [hq]; ring)

private lemma specht211_braid12 (q : K) (hq : q ≠ 0) :
    specht211Gen1 q * specht211Gen2 q * specht211Gen1 q =
      specht211Gen2 q * specht211Gen1 q * specht211Gen2 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht211Gen1, specht211Gen2, Matrix.mul_apply, Fin.sum_univ_three]
      try (field_simp [hq]; ring)

private lemma specht211_braid23 (q : K) (hq : q ≠ 0) :
    specht211Gen2 q * specht211Gen3 q * specht211Gen2 q =
      specht211Gen3 q * specht211Gen2 q * specht211Gen3 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht211Gen2, specht211Gen3, Matrix.mul_apply, Fin.sum_univ_three]
      try (field_simp [hq]; ring)

private lemma specht211_comm13 (q : K) :
    specht211Gen1 q * specht211Gen3 q = specht211Gen3 q * specht211Gen1 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    · simp only [specht211Gen1, specht211Gen3, Matrix.mul_apply, Fin.sum_univ_three]
      ring

/-- The 3D `(2,1^2)` representation satisfies all `H_4(q)` quadratic and braid relations. -/
theorem specht211_isH4MatrixRep (q : K) (hq : q ≠ 0) :
    IsH4MatrixRep q (specht211Gen1 q) (specht211Gen2 q) (specht211Gen3 q) :=
  ⟨specht211_rel1 q hq, specht211_rel2 q hq, specht211_rel3 q hq,
   specht211_braid12 q hq, specht211_braid23 q hq, specht211_comm13 q⟩

/-- The 1D `(1^4)` representation satisfies all `H_4(q)` quadratic and braid relations. -/
theorem specht1111_isH4MatrixRep (q : K) (hq : q ≠ 0) :
    IsH4MatrixRep q (specht1111Gen q) (specht1111Gen q) (specht1111Gen q) := by
  refine ⟨?_, ?_, ?_, rfl, rfl, rfl⟩ <;>
    · ext i j; fin_cases i; fin_cases j
      simp only [specht1111Gen, Matrix.mul_apply, Fin.sum_univ_one,
        Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul]
      field_simp [hq]; ring

/-- Companion `3 × 3` Coxeter matrix `C_{31}(q) = T_1 T_2 T_3` on `S^{(3,1)}`. -/
def coxeter31Mat (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨2, _⟩ => -q
  | ⟨1, _⟩, ⟨0, _⟩ => q
  | ⟨1, _⟩, ⟨2, _⟩ => -q
  | ⟨2, _⟩, ⟨1, _⟩ => q
  | ⟨2, _⟩, ⟨2, _⟩ => -q
  | _, _ => 0

/-- Square `C_{31}(q)^2` on `S^{(3,1)}`. -/
def coxeter31SqMat (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨1, _⟩ => -q ^ 2
  | ⟨0, _⟩, ⟨2, _⟩ => q ^ 2
  | ⟨1, _⟩, ⟨1, _⟩ => -q ^ 2
  | ⟨2, _⟩, ⟨0, _⟩ => q ^ 2
  | ⟨2, _⟩, ⟨1, _⟩ => -q ^ 2
  | _, _ => 0

/-- Explicit `2 × 2` Coxeter matrix `C_{22}(q) = T_1 T_2 T_3` on `S^{(2,2)}`. -/
def coxeter22Mat (q : K) : Matrix (Fin 2) (Fin 2) K
  | ⟨0, _⟩, ⟨1, _⟩ => -q
  | ⟨1, _⟩, ⟨0, _⟩ => -q⁻¹
  | _, _ => 0

/-- Companion `3 × 3` Coxeter matrix `C_{211}(q) = T_1 T_2 T_3` on `S^{(2,1^2)}`. -/
def coxeter211Mat (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨2, _⟩ => q⁻¹
  | ⟨1, _⟩, ⟨0, _⟩ => -q⁻¹
  | ⟨1, _⟩, ⟨2, _⟩ => q⁻¹
  | ⟨2, _⟩, ⟨1, _⟩ => -q⁻¹
  | ⟨2, _⟩, ⟨2, _⟩ => q⁻¹
  | _, _ => 0

/-- Square `C_{211}(q)^2` on `S^{(2,1^2)}`. -/
def coxeter211SqMat (q : K) : Matrix (Fin 3) (Fin 3) K
  | ⟨0, _⟩, ⟨1, _⟩ => -(q ^ 2)⁻¹
  | ⟨0, _⟩, ⟨2, _⟩ => (q ^ 2)⁻¹
  | ⟨1, _⟩, ⟨1, _⟩ => -(q ^ 2)⁻¹
  | ⟨2, _⟩, ⟨0, _⟩ => (q ^ 2)⁻¹
  | ⟨2, _⟩, ⟨1, _⟩ => -(q ^ 2)⁻¹
  | _, _ => 0

lemma coxeter4_specht31_eq (q : K) (hq : q ≠ 0) :
    coxeter4 (specht31Gen1 q) (specht31Gen2 q) (specht31Gen3 q) = coxeter31Mat q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    · simp only [coxeter4, coxeter31Mat, specht31Gen1, specht31Gen2, specht31Gen3,
        Matrix.mul_apply, Fin.sum_univ_three, Fin.isValue]
      field_simp [hq]
      ring

lemma coxeter4_specht22_eq (q : K) (hq : q ≠ 0) :
    coxeter4 (specht22Gen1 q) (specht22Gen2 q) (specht22Gen3 q) = coxeter22Mat q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    · simp only [coxeter4, coxeter22Mat, specht22Gen1, specht22Gen2, specht22Gen3,
        Matrix.mul_apply, Fin.sum_univ_two, Fin.isValue]
      field_simp [hq]
      ring

lemma coxeter4_specht211_eq (q : K) (hq : q ≠ 0) :
    coxeter4 (specht211Gen1 q) (specht211Gen2 q) (specht211Gen3 q) = coxeter211Mat q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    · simp only [coxeter4, coxeter211Mat, specht211Gen1, specht211Gen2, specht211Gen3,
        Matrix.mul_apply, Fin.sum_univ_three, Fin.isValue]
      field_simp [hq]
      ring

/-- Matrix-trace verification of the five Markov conjugacy-class characters on `S^{(3,1)}`:
`(tr(1), tr(T_1), tr(T_1 T_2), tr(T_1 T_3), tr(T_1 T_2 T_3)) = (3, 2q - q⁻¹, q^2 - 1, q^2 - 2, -q)`. -/
theorem specht31_conjugacy_characters (q : K) (hq : q ≠ 0) :
    Matrix.trace (1 : Matrix (Fin 3) (Fin 3) K) = 3 ∧
    Matrix.trace (specht31Gen1 q) = 2 * q - q⁻¹ ∧
    Matrix.trace (specht31Gen1 q * specht31Gen2 q) = q ^ 2 - 1 ∧
    Matrix.trace (specht31Gen1 q * specht31Gen3 q) = q ^ 2 - 2 ∧
    Matrix.trace (coxeter4 (specht31Gen1 q) (specht31Gen2 q) (specht31Gen3 q)) = -q := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [Matrix.trace_fin_three]; norm_num
  · rw [Matrix.trace_fin_three]
    dsimp [specht31Gen1]; ring
  · rw [Matrix.trace_fin_three]
    simp only [specht31Gen1, specht31Gen2, Matrix.mul_apply, Fin.sum_univ_three, Fin.isValue]
    field_simp [hq]; ring
  · rw [Matrix.trace_fin_three]
    simp only [specht31Gen1, specht31Gen3, Matrix.mul_apply, Fin.sum_univ_three, Fin.isValue]
    field_simp [hq]; ring
  · rw [coxeter4_specht31_eq q hq, Matrix.trace_fin_three]
    dsimp [coxeter31Mat]; ring

/-- Matrix-trace verification of the five Markov conjugacy-class characters on `S^{(2,2)}`:
`(tr(1), tr(T_1), tr(T_1 T_2), tr(T_1 T_3), tr(T_1 T_2 T_3)) = (2, q - q⁻¹, -1, q^2 + (q^2)⁻¹, 0)`. -/
theorem specht22_conjugacy_characters (q : K) (hq : q ≠ 0) :
    Matrix.trace (1 : Matrix (Fin 2) (Fin 2) K) = 2 ∧
    Matrix.trace (specht22Gen1 q) = q - q⁻¹ ∧
    Matrix.trace (specht22Gen1 q * specht22Gen2 q) = -1 ∧
    Matrix.trace (specht22Gen1 q * specht22Gen3 q) = q ^ 2 + (q ^ 2)⁻¹ ∧
    Matrix.trace (coxeter4 (specht22Gen1 q) (specht22Gen2 q) (specht22Gen3 q)) = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [Matrix.trace_fin_two]; norm_num
  · rw [Matrix.trace_fin_two]
    dsimp [specht22Gen1]; ring
  · rw [Matrix.trace_fin_two]
    simp only [specht22Gen1, specht22Gen2, Matrix.mul_apply, Fin.sum_univ_two, Fin.isValue]
    field_simp [hq]; ring
  · rw [Matrix.trace_fin_two]
    simp only [specht22Gen1, specht22Gen3, Matrix.mul_apply, Fin.sum_univ_two, Fin.isValue]
    field_simp [hq]; ring
  · rw [coxeter4_specht22_eq q hq, Matrix.trace_fin_two]
    dsimp [coxeter22Mat]; ring

/-- Matrix-trace verification of the five Markov conjugacy-class characters on `S^{(2,1^2)}`:
`(tr(1), tr(T_1), tr(T_1 T_2), tr(T_1 T_3), tr(T_1 T_2 T_3)) = (3, q - 2q⁻¹, -1 + (q^2)⁻¹, -2 + (q^2)⁻¹, q⁻¹)`. -/
theorem specht211_conjugacy_characters (q : K) (hq : q ≠ 0) :
    Matrix.trace (1 : Matrix (Fin 3) (Fin 3) K) = 3 ∧
    Matrix.trace (specht211Gen1 q) = q - 2 * q⁻¹ ∧
    Matrix.trace (specht211Gen1 q * specht211Gen2 q) = -1 + (q ^ 2)⁻¹ ∧
    Matrix.trace (specht211Gen1 q * specht211Gen3 q) = -2 + (q ^ 2)⁻¹ ∧
    Matrix.trace (coxeter4 (specht211Gen1 q) (specht211Gen2 q) (specht211Gen3 q)) = q⁻¹ := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [Matrix.trace_fin_three]; norm_num
  · rw [Matrix.trace_fin_three]
    dsimp [specht211Gen1]; ring
  · rw [Matrix.trace_fin_three]
    simp only [specht211Gen1, specht211Gen2, Matrix.mul_apply, Fin.sum_univ_three, Fin.isValue]
    field_simp [hq]; ring
  · rw [Matrix.trace_fin_three]
    simp only [specht211Gen1, specht211Gen3, Matrix.mul_apply, Fin.sum_univ_three, Fin.isValue]
    field_simp [hq]; ring
  · rw [coxeter4_specht211_eq q hq, Matrix.trace_fin_three]
    dsimp [coxeter211Mat]; ring

/-- **Full-Twist Eigenvalue on `S^{(4)}`**: `Δ_4^2 = (T_1 T_2 T_3)^4` acts by `q^{12} · I_1`. -/
theorem specht4_fullTwist (q : K) :
    fullTwist4 (specht4Gen q) (specht4Gen q) (specht4Gen q) =
      (q ^ 12) • (1 : Matrix (Fin 1) (Fin 1) K) := by
  have hpow :
      (coxeter4 (specht4Gen q) (specht4Gen q) (specht4Gen q)) ^ 4 =
        (coxeter4 (specht4Gen q) (specht4Gen q) (specht4Gen q) *
          coxeter4 (specht4Gen q) (specht4Gen q) (specht4Gen q)) *
        (coxeter4 (specht4Gen q) (specht4Gen q) (specht4Gen q) *
          coxeter4 (specht4Gen q) (specht4Gen q) (specht4Gen q)) := by
    simp [pow_succ, pow_zero, mul_assoc]
  unfold fullTwist4
  rw [hpow]
  ext i j
  fin_cases i; fin_cases j
  simp only [coxeter4, specht4Gen, Matrix.mul_apply, Fin.sum_univ_one,
    Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul]
  ring

/-- **Full-Twist Eigenvalue on `S^{(3,1)}`**: `Δ_4^2 = (T_1 T_2 T_3)^4` acts centrally by `q^4 · I_3`. -/
theorem specht31_fullTwist (q : K) (hq : q ≠ 0) :
    fullTwist4 (specht31Gen1 q) (specht31Gen2 q) (specht31Gen3 q) =
      (q ^ 4) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  have hsq : coxeter31Mat q * coxeter31Mat q = coxeter31SqMat q := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      · simp only [coxeter31Mat, coxeter31SqMat, Matrix.mul_apply, Fin.sum_univ_three]
        ring
  have hpow : (coxeter31Mat q) ^ 4 = coxeter31SqMat q * coxeter31SqMat q := by
    calc
      (coxeter31Mat q) ^ 4 = (coxeter31Mat q * coxeter31Mat q) * (coxeter31Mat q * coxeter31Mat q) := by
        simp [pow_succ, pow_zero, mul_assoc]
      _ = coxeter31SqMat q * coxeter31SqMat q := by rw [hsq]
  unfold fullTwist4
  rw [coxeter4_specht31_eq q hq, hpow]
  ext i j
  fin_cases i <;> fin_cases j <;>
    · simp only [coxeter31SqMat, Matrix.mul_apply, Fin.sum_univ_three,
        Matrix.smul_apply, Matrix.one_apply, Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
      ring

/-- **Full-Twist Eigenvalue on `S^{(2,2)}`**: `Δ_4^2 = (T_1 T_2 T_3)^4` acts by the identity `1 · I_2`. -/
theorem specht22_fullTwist (q : K) (hq : q ≠ 0) :
    fullTwist4 (specht22Gen1 q) (specht22Gen2 q) (specht22Gen3 q) =
      (1 : K) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  have hsq : coxeter22Mat q * coxeter22Mat q = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      · simp only [coxeter22Mat, Matrix.mul_apply, Fin.sum_univ_two,
          Matrix.one_apply, Fin.mk.injEq, Nat.reduceEqDiff, reduceIte]
        field_simp [hq]; ring
  unfold fullTwist4
  rw [coxeter4_specht22_eq q hq]
  calc
    (coxeter22Mat q) ^ 4 = (coxeter22Mat q * coxeter22Mat q) * (coxeter22Mat q * coxeter22Mat q) := by
      simp [pow_succ, pow_zero, mul_assoc]
    _ = 1 := by rw [hsq, mul_one]
    _ = (1 : K) • 1 := (one_smul K _).symm

/-- **Full-Twist Eigenvalue on `S^{(2,1^2)}`**: `Δ_4^2 = (T_1 T_2 T_3)^4` acts centrally by `q^{-4} · I_3`. -/
theorem specht211_fullTwist (q : K) (hq : q ≠ 0) :
    fullTwist4 (specht211Gen1 q) (specht211Gen2 q) (specht211Gen3 q) =
      ((q ^ 4)⁻¹) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  have hsq : coxeter211Mat q * coxeter211Mat q = coxeter211SqMat q := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      · simp only [coxeter211Mat, coxeter211SqMat, Matrix.mul_apply, Fin.sum_univ_three]
        field_simp [hq]; ring
  have hpow : (coxeter211Mat q) ^ 4 = coxeter211SqMat q * coxeter211SqMat q := by
    calc
      (coxeter211Mat q) ^ 4 =
          (coxeter211Mat q * coxeter211Mat q) * (coxeter211Mat q * coxeter211Mat q) := by
        simp [pow_succ, pow_zero, mul_assoc]
      _ = coxeter211SqMat q * coxeter211SqMat q := by rw [hsq]
  unfold fullTwist4
  rw [coxeter4_specht211_eq q hq, hpow]
  ext i j
  fin_cases i <;> fin_cases j <;>
    · simp only [coxeter211SqMat, Matrix.mul_apply, Fin.sum_univ_three,
        Matrix.smul_apply, Matrix.one_apply, Fin.mk.injEq, Nat.reduceEqDiff, smul_eq_mul, reduceIte]
      field_simp [hq]; ring

/-- **Full-Twist Eigenvalue on `S^{(1^4)}`**: `Δ_4^2 = (T_1 T_2 T_3)^4` acts by `q^{-12} · I_1`. -/
theorem specht1111_fullTwist (q : K) (hq : q ≠ 0) :
    fullTwist4 (specht1111Gen q) (specht1111Gen q) (specht1111Gen q) =
      ((q ^ 12)⁻¹) • (1 : Matrix (Fin 1) (Fin 1) K) := by
  have hpow :
      (coxeter4 (specht1111Gen q) (specht1111Gen q) (specht1111Gen q)) ^ 4 =
        (coxeter4 (specht1111Gen q) (specht1111Gen q) (specht1111Gen q) *
          coxeter4 (specht1111Gen q) (specht1111Gen q) (specht1111Gen q)) *
        (coxeter4 (specht1111Gen q) (specht1111Gen q) (specht1111Gen q) *
          coxeter4 (specht1111Gen q) (specht1111Gen q) (specht1111Gen q)) := by
    simp [pow_succ, pow_zero, mul_assoc]
  unfold fullTwist4
  rw [hpow]
  ext i j
  fin_cases i; fin_cases j
  simp only [coxeter4, specht1111Gen, Matrix.mul_apply, Fin.sum_univ_one,
    Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul]
  field_simp [hq]

/-- Framing scalar eigenvalue `q^{2 κ_λ}` of `Δ_4^2` on block `λ ⊢ 4`. -/
def fullTwistEigenvalue (q : K) (lam : H4Partition) : K :=
  q ^ (fullTwistExponent lam)

/-- Exact closed forms `(q^{12}, q^4, 1, (q^4)⁻¹, (q^{12})⁻¹)` of `fullTwistEigenvalue`. -/
theorem fullTwistEigenvalue_tuple (q : K) :
    (fullTwistEigenvalue q .p4,
     fullTwistEigenvalue q .p31,
     fullTwistEigenvalue q .p22,
     fullTwistEigenvalue q .p211,
     fullTwistEigenvalue q .p1111) =
      (q ^ 12, q ^ 4, 1, (q ^ 4)⁻¹, (q ^ 12)⁻¹) := by
  have h1 : fullTwistExponent .p4 = ((12 : ℕ) : ℤ) := rfl
  have h2 : fullTwistExponent .p31 = ((4 : ℕ) : ℤ) := rfl
  have h3 : fullTwistExponent .p22 = 0 := rfl
  have h4 : fullTwistExponent .p211 = -((4 : ℕ) : ℤ) := rfl
  have h5 : fullTwistExponent .p1111 = -((12 : ℕ) : ℤ) := rfl
  unfold fullTwistEigenvalue
  rw [h1, h2, h3, h4, h5]
  simp only [zpow_neg, zpow_natCast, zpow_zero]

end SpechtRepresentationsAndFullTwist

-- ============================================================================
-- § 3. Convention-D + GPMT Full-Twist Characters & Casimir Closed Forms in Q(q)
-- ============================================================================

section H4FullTwistAndCasimirClosedForms

variable {K : Type*} [Field K]

/-- Generic-`z` Ocneanu Markov trace of the 4-strand positive full twist `Δ_4^{+2}`:
`∑_{λ ⊢ 4} w_λ(q, z) d_λ q^{2 κ_λ}`. -/
def trOcneanuFullTwistPos (q z : K) : K :=
  w4 q z * q ^ 12 + 3 * w31 q z * q ^ 4 + 2 * w22 q z +
    3 * w211 q z * (q ^ 4)⁻¹ + w1111 q z * (q ^ 12)⁻¹

/-- Generic-`z` Ocneanu Markov trace of the 4-strand inverse full twist `Δ_4^{-2}`:
`∑_{λ ⊢ 4} w_λ(q, z) d_λ q^{-2 κ_λ}`. -/
def trOcneanuFullTwistNeg (q z : K) : K :=
  w4 q z * (q ^ 12)⁻¹ + 3 * w31 q z * (q ^ 4)⁻¹ + 2 * w22 q z +
    3 * w211 q z * q ^ 4 + w1111 q z * q ^ 12

/-- Convention-D (`z = z_D = q^3 / (q^2 + 1)`) Markov trace of `Δ_4^{+2}`. -/
def trConventionDFullTwistPos (q : K) : K :=
  trOcneanuFullTwistPos q (zD q)

/-- Convention-D (`z = z_D = q^3 / (q^2 + 1)`) Markov trace of `Δ_4^{-2}`. -/
def trConventionDFullTwistNeg (q : K) : K :=
  trOcneanuFullTwistNeg q (zD q)

/-- Convention-D two-row content-sum Casimir expectation `<2 κ_λ>_D`:
`12 w_{(4)}(z_D) + 12 w_{(3,1)}(z_D) + 0 · w_{(2,2)}(z_D)`. -/
def casimirConventionD (q : K) : K :=
  12 * w4 q (zD q) + 3 * 4 * w31 q (zD q) + 2 * 0 * w22 q (zD q)

/-- GPMT-weighted `≥ 3`-row trace of the positive full twist `Δ_4^{+2}` combining the
Springer-signed modified quantum dimensions `-3 d_D(S^{(2,1^2)}) > 0` and `+d_D(S^{(1^4)}) > 0`. -/
def gpmtRow3FullTwistPos (q : K) : K :=
  (-3 * dMod211 q) * (q ^ 4)⁻¹ + dMod1111 q * (q ^ 12)⁻¹

/-- GPMT-weighted `≥ 3`-row trace of the inverse full twist `Δ_4^{-2}`. -/
def gpmtRow3FullTwistNeg (q : K) : K :=
  (-3 * dMod211 q) * q ^ 4 + dMod1111 q * q ^ 12

/-- GPMT-weighted `≥ 3`-row content-sum Casimir expectation `<-2 κ_λ>_{GPMT, ≥3}`:
`(-3 d_D(S^{(2,1^2)})) · 4 + d_D(S^{(1^4)}) · 12`. -/
def casimirGPMTRow3 (q : K) : K :=
  (-3 * dMod211 q) * 4 + dMod1111 q * 12

/-- Pure Wigner-$SU(4)$ `(1^4)` singlet GPMT full-twist amplitude `d_D(S^{(1^4)}) · q^{-12}`. -/
def wignerSingletGPMTFullTwistPos (q : K) : K :=
  dMod1111 q * (q ^ 12)⁻¹

/-- **Exact Rational Closed Form of `tr_M^D(Δ_4^{+2})`**:
At `z_D = q^3 / (q^2 + 1)`, the `(q^2 + 1)^2` factor cancels between numerator and denominator:
`trConventionDFullTwistPos q = q^4 (q^4 + 1)(q^8 - q^6 + q^4 - q^2 + 2) / (q^2 + 1)^2`. -/
theorem trConventionDFullTwistPos_closed_form
    (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    trConventionDFullTwistPos q =
      q ^ 4 * (q ^ 4 + 1) * (q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 2) / (q ^ 2 + 1) ^ 2 := by
  have hq21 : q21 q ≠ 0 := hq2
  unfold trConventionDFullTwistPos trOcneanuFullTwistPos
  rw [w4_conventionD q hq2 hq41 hq421, w31_conventionD q hq2 hq41 hq421,
    w22_conventionD q hq2 hq41 hq421, w211_conventionD q hq2, w1111_conventionD q hq2]
  change
    ((q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) / q21 q ^ 4) * q ^ 12 +
      3 * (q ^ 2 * (q ^ 4 + q ^ 2 + 1) / q21 q ^ 4) * q ^ 4 +
      2 * (q ^ 4 / q21 q ^ 4) + 3 * 0 * (q ^ 4)⁻¹ + 0 * (q ^ 12)⁻¹ =
    q ^ 4 * (q ^ 4 + 1) * (q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 2) / q21 q ^ 2
  rw [mul_zero, zero_mul, zero_mul, add_zero, add_zero]
  have hd4 : q21 q ^ 4 ≠ 0 := pow_ne_zero 4 hq21
  have hd2 : q21 q ^ 2 ≠ 0 := pow_ne_zero 2 hq21
  field_simp [hd4, hd2, hq21]
  unfold q21
  ring

/-- **Exact Rational Closed Form of `tr_M^D(Δ_4^{-2})`**:
`trConventionDFullTwistNeg q = (q^4 + 1)(2 q^8 - q^6 + q^4 - q^2 + 1) / (q^{12} (q^2 + 1)^2)`. -/
theorem trConventionDFullTwistNeg_closed_form
    (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    trConventionDFullTwistNeg q =
      (q ^ 4 + 1) * (2 * q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 1) /
        (q ^ 12 * (q ^ 2 + 1) ^ 2) := by
  have hq21 : q21 q ≠ 0 := hq2
  unfold trConventionDFullTwistNeg trOcneanuFullTwistNeg
  rw [w4_conventionD q hq2 hq41 hq421, w31_conventionD q hq2 hq41 hq421,
    w22_conventionD q hq2 hq41 hq421, w211_conventionD q hq2, w1111_conventionD q hq2]
  change
    ((q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) / q21 q ^ 4) * (q ^ 12)⁻¹ +
      3 * (q ^ 2 * (q ^ 4 + q ^ 2 + 1) / q21 q ^ 4) * (q ^ 4)⁻¹ +
      2 * (q ^ 4 / q21 q ^ 4) + 3 * 0 * q ^ 4 + 0 * q ^ 12 =
    (q ^ 4 + 1) * (2 * q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 1) / (q ^ 12 * q21 q ^ 2)
  rw [mul_zero, zero_mul, zero_mul, add_zero, add_zero]
  field_simp [hq21, hq]
  unfold q21
  ring

/-- **Exact Cancellation Identity for the Convention-D Two-Row Casimir `<2 κ_λ>_D`**:
`casimirConventionD q = 12 (q^4 + 1) / (q^2 + 1)^2`. -/
theorem casimirConventionD_closed_form
    (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    casimirConventionD q = 12 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hq21 : q21 q ≠ 0 := hq2
  unfold casimirConventionD
  rw [w4_conventionD q hq2 hq41 hq421, w31_conventionD q hq2 hq41 hq421]
  change
    12 * ((q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) / q21 q ^ 4) +
      3 * 4 * (q ^ 2 * (q ^ 4 + q ^ 2 + 1) / q21 q ^ 4) +
      2 * 0 * w22 q (zD q) =
    12 * (q ^ 4 + 1) / q21 q ^ 2
  rw [mul_zero, zero_mul, add_zero]
  field_simp [hq21]
  unfold q21
  ring

/-- **Exact Rational Closed Form of `gpmtRow3FullTwistPos`**:
`(-3 dMod211 q) q^{-4} + dMod1111 q q^{-12} =
  (3 q^{12} + 6 q^{10} + 9 q^8 + 6 q^6 + 3 q^4 + 1) / (q^5 (q^2 + 1)^3 (q^4 + 1)(q^4 + q^2 + 1))`. -/
theorem gpmtRow3FullTwistPos_closed_form
    (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    gpmtRow3FullTwistPos q =
      (3 * q ^ 12 + 6 * q ^ 10 + 9 * q ^ 8 + 6 * q ^ 6 + 3 * q ^ 4 + 1) /
        (q ^ 5 * ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))) := by
  have hden : h4ModDenom q ≠ 0 := h4ModDenom_ne_zero q hq2 hq41 hq421
  unfold gpmtRow3FullTwistPos
  rw [dMod211_over_h4ModDenom q hq421, dMod1111_over_h4ModDenom q]
  change
    (-3 * (-q ^ 3 * (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / h4ModDenom q)) * (q ^ 4)⁻¹ +
      (q ^ 7 / h4ModDenom q) * (q ^ 12)⁻¹ =
    (3 * q ^ 12 + 6 * q ^ 10 + 9 * q ^ 8 + 6 * q ^ 6 + 3 * q ^ 4 + 1) /
      (q ^ 5 * h4ModDenom q)
  field_simp [hden, hq]
  ring

/-- **Exact Rational Closed Form of `gpmtRow3FullTwistNeg`**:
`(-3 dMod211 q) q^4 + dMod1111 q q^{12} =
  q^7 (q^{12} + 3 q^8 + 6 q^6 + 9 q^4 + 6 q^2 + 3) / ((q^2 + 1)^3 (q^4 + 1)(q^4 + q^2 + 1))`. -/
theorem gpmtRow3FullTwistNeg_closed_form
    (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    gpmtRow3FullTwistNeg q =
      q ^ 7 * (q ^ 12 + 3 * q ^ 8 + 6 * q ^ 6 + 9 * q ^ 4 + 6 * q ^ 2 + 3) /
        ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  have hden : h4ModDenom q ≠ 0 := h4ModDenom_ne_zero q hq2 hq41 hq421
  unfold gpmtRow3FullTwistNeg
  rw [dMod211_over_h4ModDenom q hq421, dMod1111_over_h4ModDenom q]
  change
    (-3 * (-q ^ 3 * (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / h4ModDenom q)) * q ^ 4 +
      (q ^ 7 / h4ModDenom q) * q ^ 12 =
    q ^ 7 * (q ^ 12 + 3 * q ^ 8 + 6 * q ^ 6 + 9 * q ^ 4 + 6 * q ^ 2 + 3) / h4ModDenom q
  field_simp [hden]
  ring

/-- **Exact Rational Closed Form of the GPMT `≥ 3`-Row Casimir `casimirGPMTRow3`**:
`casimirGPMTRow3 q = 12 q^3 (q^8 + 2 q^6 + 4 q^4 + 2 q^2 + 1) / ((q^2 + 1)^3 (q^4 + 1)(q^4 + q^2 + 1))`. -/
theorem casimirGPMTRow3_closed_form
    (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    casimirGPMTRow3 q =
      12 * q ^ 3 * (q ^ 8 + 2 * q ^ 6 + 4 * q ^ 4 + 2 * q ^ 2 + 1) /
        ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  have hden : h4ModDenom q ≠ 0 := h4ModDenom_ne_zero q hq2 hq41 hq421
  unfold casimirGPMTRow3
  rw [dMod211_over_h4ModDenom q hq421, dMod1111_over_h4ModDenom q]
  change
    (-3 * (-q ^ 3 * (q ^ 4 + q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) / h4ModDenom q)) * 4 +
      (q ^ 7 / h4ModDenom q) * 12 =
    12 * q ^ 3 * (q ^ 8 + 2 * q ^ 6 + 4 * q ^ 4 + 2 * q ^ 2 + 1) / h4ModDenom q
  field_simp [hden]
  ring

/-- **Exact Closed Form of the Pure Wigner-$SU(4)$ Singlet `(1^4)` GPMT Full-Twist Amplitude**:
`wignerSingletGPMTFullTwistPos q = 1 / (q^5 (q^2 + 1)^3 (q^4 + 1)(q^4 + q^2 + 1))`. -/
theorem wignerSingletGPMTFullTwistPos_closed_form
    (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0)
    (hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    wignerSingletGPMTFullTwistPos q =
      1 / (q ^ 5 * ((q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))) := by
  have hden : h4ModDenom q ≠ 0 := h4ModDenom_ne_zero q hq2 hq41 hq421
  unfold wignerSingletGPMTFullTwistPos
  rw [dMod1111_over_h4ModDenom q]
  change q ^ 7 / h4ModDenom q * (q ^ 12)⁻¹ = 1 / (q ^ 5 * h4ModDenom q)
  field_simp [hden, hq]

end H4FullTwistAndCasimirClosedForms

section H4FullTwistPositivityBounds

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Strict positivity of `gpmtRow3FullTwistPos`, `gpmtRow3FullTwistNeg`, `casimirGPMTRow3`,
`casimirConventionD`, and `wignerSingletGPMTFullTwistPos` for all `q > 0`. -/
theorem h4_gpmt_fullTwist_and_casimir_pos (q : R) (hq : 0 < q) :
    0 < casimirConventionD q ∧
    0 < gpmtRow3FullTwistPos q ∧
    0 < gpmtRow3FullTwistNeg q ∧
    0 < casimirGPMTRow3 q ∧
    0 < wignerSingletGPMTFullTwistPos q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  have hq41 : q ^ 4 + 1 ≠ 0 := ne_of_gt (pow_four_add_one_pos q)
  have hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt (pow_four_add_sq_add_one_pos q)
  rcases sRow3GPMT_H4_four_both_terms_pos q hq with ⟨hd211, hd1111, _⟩
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [casimirConventionD_closed_form q hq2 hq41 hq421]
    exact div_pos (mul_pos (by norm_num) (pow_four_add_one_pos q)) (pow_pos (sq_add_one_pos q) 2)
  · unfold gpmtRow3FullTwistPos
    exact add_pos
      (mul_pos hd211 (inv_pos.mpr (pow_pos hq 4)))
      (mul_pos hd1111 (inv_pos.mpr (pow_pos hq 12)))
  · unfold gpmtRow3FullTwistNeg
    exact add_pos
      (mul_pos hd211 (pow_pos hq 4))
      (mul_pos hd1111 (pow_pos hq 12))
  · unfold casimirGPMTRow3
    linarith
  · unfold wignerSingletGPMTFullTwistPos
    exact mul_pos hd1111 (inv_pos.mpr (pow_pos hq 12))

/-- For `1 < q`, the Convention-D inverse full-twist trace satisfies
`0 < trConventionDFullTwistNeg q < 1` (so `-ln(trConventionDFullTwistNeg q) > 0` is strictly attractive). -/
theorem trConventionDFullTwistNeg_bounds_of_one_lt (q : R) (hq1 : 1 < q) :
    0 < trConventionDFullTwistNeg q ∧ trConventionDFullTwistNeg q < 1 := by
  have hq : 0 < q := lt_trans zero_lt_one hq1
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  have hq41 : q ^ 4 + 1 ≠ 0 := ne_of_gt (pow_four_add_one_pos q)
  have hq421 : q ^ 4 + q ^ 2 + 1 ≠ 0 := ne_of_gt (pow_four_add_sq_add_one_pos q)
  have hw4 : 0 < w4 q (zD q) := by
    rw [w4_conventionD q hq2 hq41 hq421]
    apply div_pos
    · positivity
    · exact pow_pos (sq_add_one_pos q) 4
  have hw31 : 0 < w31 q (zD q) := by
    rw [w31_conventionD q hq2 hq41 hq421]
    apply div_pos
    · exact mul_pos (pow_pos hq 2) (pow_four_add_sq_add_one_pos q)
    · exact pow_pos (sq_add_one_pos q) 4
  have hw22 : 0 ≤ w22 q (zD q) := by
    rw [w22_conventionD q hq2 hq41 hq421]
    exact le_of_lt (div_pos (pow_pos hq 4) (pow_pos (sq_add_one_pos q) 4))
  have hsum := weights_h4_conventionD_twoRow_sum_eq_one q hq2 hq41 hq421
  unfold trConventionDFullTwistNeg trOcneanuFullTwistNeg
  rw [w211_conventionD q hq2, w1111_conventionD q hq2]
  simp only [mul_zero, zero_mul, add_zero]
  have hinv4_lt : (q ^ 4)⁻¹ < 1 := inv_lt_one_of_one_lt₀ (one_lt_pow₀ hq1 (by decide))
  have hinv12_lt : (q ^ 12)⁻¹ < 1 := inv_lt_one_of_one_lt₀ (one_lt_pow₀ hq1 (by decide))
  constructor
  · have t1 : 0 < w4 q (zD q) * (q ^ 12)⁻¹ := mul_pos hw4 (inv_pos.mpr (pow_pos hq 12))
    have t2 : 0 < 3 * w31 q (zD q) * (q ^ 4)⁻¹ :=
      mul_pos (mul_pos (by norm_num) hw31) (inv_pos.mpr (pow_pos hq 4))
    linarith
  · have t1 : w4 q (zD q) * (q ^ 12)⁻¹ < w4 q (zD q) :=
      mul_lt_of_lt_one_right hw4 hinv12_lt
    have t2 : 3 * w31 q (zD q) * (q ^ 4)⁻¹ < 3 * w31 q (zD q) :=
      mul_lt_of_lt_one_right (mul_pos (by norm_num) hw31) hinv4_lt
    linarith

end H4FullTwistPositivityBounds

-- ============================================================================
-- § 4. Inductive Transfer-Matrix / Gröbner–Shirshov Multi-Crossing Reduction
-- ============================================================================

section TransferMatrixGroebnerReduction

variable {R : Type*} [CommRing R]

/-- Linear generator coefficient `a_k(h)` in the Hecke power reduction `C^k = a_k(h) C + b_k(h)`. -/
def heckePowerA (h : R) : ℕ → R
  | 0 => 0
  | k + 1 => h * heckePowerA h k + (match k with | 0 => 1 | m + 1 => heckePowerA h m)

/-- Constant unit coefficient `b_k(h)` in the Hecke power reduction `C^k = a_k(h) C + b_k(h)`. -/
def heckePowerB (h : R) : ℕ → R
  | 0 => 1
  | k + 1 => heckePowerA h k

/-- Step recurrence `a_{k+1}(h) = h a_k(h) + b_k(h)` and `b_{k+1}(h) = a_k(h)`. -/
theorem heckePower_step (h : R) (k : ℕ) :
    heckePowerA h (k + 1) = h * heckePowerA h k + heckePowerB h k ∧
    heckePowerB h (k + 1) = heckePowerA h k := by
  cases k <;> simp [heckePowerA, heckePowerB]

/-- Explicit low-degree values of `(a_k(h), b_k(h))` for `k = 0, 1, 2, 3, 4`. -/
theorem heckePower_low_degrees (h : R) :
    (heckePowerA h 0, heckePowerB h 0) = (0, 1) ∧
    (heckePowerA h 1, heckePowerB h 1) = (1, 0) ∧
    (heckePowerA h 2, heckePowerB h 2) = (h, 1) ∧
    (heckePowerA h 3, heckePowerB h 3) = (h ^ 2 + 1, h) ∧
    (heckePowerA h 4, heckePowerB h 4) = (h ^ 3 + 2 * h, h ^ 2 + 1) := by
  refine ⟨rfl, ?_, ?_, ?_, ?_⟩
  · ext <;> simp [heckePowerA, heckePowerB]
  · ext <;> simp [heckePowerA, heckePowerB]
  · ext <;> (simp [heckePowerA, heckePowerB]; try ring)
  · ext <;> (simp [heckePowerA, heckePowerB]; try ring)

/-- **Inductive Hecke Quadratic Power-Reduction Theorem (`C^2 = h C + 1 ⟹ C^k = a_k(h) C + b_k(h)`)**:
In any `R`-algebra `A`, if `C : A` satisfies `C^2 = h • C + 1`, then every non-negative integer
power `C^k` reduces to the two-term normal form `heckePowerA h k • C + heckePowerB h k • 1`. -/
theorem hecke_pow_eq_linear_nf {A : Type*} [Ring A] [Algebra R A]
    (h : R) (C : A) (hC : C ^ 2 = h • C + 1) (k : ℕ) :
    C ^ k = heckePowerA h k • C + heckePowerB h k • (1 : A) := by
  induction k with
  | zero =>
    simp [heckePowerA, heckePowerB]
  | succ k ih =>
    rcases heckePower_step h k with ⟨ha, hb⟩
    rw [pow_succ, ih, ha, hb]
    have hC_mul : C * C = algebraMap R A h * C + 1 := by
      simpa [sq, Algebra.smul_def] using hC
    simp only [Algebra.smul_def, map_add, map_mul, mul_one]
    calc
      (algebraMap R A (heckePowerA h k) * C + algebraMap R A (heckePowerB h k)) * C
          = algebraMap R A (heckePowerA h k) * (C * C) +
              algebraMap R A (heckePowerB h k) * C := by noncomm_ring
      _ = algebraMap R A (heckePowerA h k) * (algebraMap R A h * C + 1) +
              algebraMap R A (heckePowerB h k) * C := by rw [hC_mul]
      _ = (algebraMap R A h * algebraMap R A (heckePowerA h k) +
              algebraMap R A (heckePowerB h k)) * C +
              algebraMap R A (heckePowerA h k) := by
            have hcomm : algebraMap R A (heckePowerA h k) * algebraMap R A h =
                algebraMap R A h * algebraMap R A (heckePowerA h k) := by
              rw [← map_mul, mul_comm, map_mul]
            calc
              algebraMap R A (heckePowerA h k) * (algebraMap R A h * C + 1) +
                  algebraMap R A (heckePowerB h k) * C
                  = (algebraMap R A (heckePowerA h k) * algebraMap R A h) * C +
                      algebraMap R A (heckePowerB h k) * C +
                      algebraMap R A (heckePowerA h k) := by noncomm_ring
              _ = (algebraMap R A h * algebraMap R A (heckePowerA h k) +
                      algebraMap R A (heckePowerB h k)) * C +
                      algebraMap R A (heckePowerA h k) := by
                    rw [hcomm]; noncomm_ring

/-- General `2 × 2` crossing transfer matrix `T(c, d) = !![c h + d, c; c, d]` acting on `(a, b)`
in the `a C + b · 1` normal-form basis. -/
def tmGeneral (h c d : R) : Matrix (Fin 2) (Fin 2) R :=
  !![c * h + d, c;
     c,         d]

/-- Fundamental `pp` crossing transfer matrix `T(1, 0) = !![h, 1; 1, 0]`. -/
def tmBase (h : R) : Matrix (Fin 2) (Fin 2) R :=
  tmGeneral h 1 0

/-- Exact determinant formula `det T(c, d) = c d h + d^2 - c^2`. -/
theorem tmGeneral_det (h c d : R) :
    Matrix.det (tmGeneral h c d) = c * d * h + d ^ 2 - c ^ 2 := by
  simp [tmGeneral, Matrix.det_fin_two]
  ring

/-- Iterating `tmBase h` on `![0, 1]` yields `![heckePowerA h k, heckePowerB h k]`. -/
theorem tmBase_pow_mulVec (h : R) (k : ℕ) :
    (tmBase h ^ k) *ᵥ ![0, 1] = ![heckePowerA h k, heckePowerB h k] := by
  induction k with
  | zero =>
    ext i; fin_cases i <;> simp [heckePowerA, heckePowerB]
  | succ k ih =>
    rcases heckePower_step h k with ⟨ha, hb⟩
    have hpow : tmBase h ^ (k + 1) = tmBase h * (tmBase h ^ k) := by
      rw [pow_succ']
    rw [hpow, ← Matrix.mulVec_mulVec, ih, ha, hb]
    ext i
    fin_cases i <;>
      · simp only [Fin.zero_eta, Fin.mk_one, tmBase, tmGeneral, Matrix.mulVec, dotProduct,
          Fin.sum_univ_two, Fin.isValue, Matrix.of_apply, Matrix.cons_val',
          Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_fin_one]
        ring

/-- Single-step transfer-matrix action in any `R`-algebra `A`: left multiplication by `c • C + d • 1`
on `a • C + b • 1` maps `(a, b)` to `tmGeneral h c d *ᵥ ![a, b]`. -/
theorem crossing_mul_nf_step {A : Type*} [Ring A] [Algebra R A]
    (h c d a b : R) (C : A) (hC : C ^ 2 = h • C + 1) :
    (c • C + d • (1 : A)) * (a • C + b • (1 : A)) =
      ((tmGeneral h c d *ᵥ ![a, b]) 0) • C +
        ((tmGeneral h c d *ᵥ ![a, b]) 1) • (1 : A) := by
  have hC_mul : C * C = algebraMap R A h * C + 1 := by
    simpa [sq, Algebra.smul_def] using hC
  have haC : C * algebraMap R A a = algebraMap R A a * C :=
    (Algebra.commutes a C).symm
  have hbC : C * algebraMap R A b = algebraMap R A b * C :=
    (Algebra.commutes b C).symm
  have hca : algebraMap R A c * (C * (algebraMap R A a * C)) =
      (algebraMap R A c * algebraMap R A a) * (C * C) := by
    calc
      algebraMap R A c * (C * (algebraMap R A a * C))
          = algebraMap R A c * ((C * algebraMap R A a) * C) := by noncomm_ring
      _ = algebraMap R A c * ((algebraMap R A a * C) * C) := by rw [haC]
      _ = (algebraMap R A c * algebraMap R A a) * (C * C) := by noncomm_ring
  have hv0 : (tmGeneral h c d *ᵥ ![a, b]) 0 = (c * h + d) * a + c * b := by
    simp only [tmGeneral, Matrix.mulVec, dotProduct, Fin.sum_univ_two, Fin.isValue,
      Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.cons_val_fin_one]
  have hv1 : (tmGeneral h c d *ᵥ ![a, b]) 1 = c * a + d * b := by
    simp only [tmGeneral, Matrix.mulVec, dotProduct, Fin.sum_univ_two, Fin.isValue,
      Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.cons_val_fin_one]
  rw [hv0, hv1]
  simp only [Algebra.smul_def, map_add, map_mul, mul_one]
  calc
    (algebraMap R A c * C + algebraMap R A d) * (algebraMap R A a * C + algebraMap R A b)
        = algebraMap R A c * (C * (algebraMap R A a * C)) +
            algebraMap R A c * (C * algebraMap R A b) +
            algebraMap R A d * (algebraMap R A a * C) +
            algebraMap R A d * algebraMap R A b := by noncomm_ring
    _ = (algebraMap R A c * algebraMap R A a) * (algebraMap R A h * C + 1) +
            (algebraMap R A c * algebraMap R A b) * C +
            (algebraMap R A d * algebraMap R A a) * C +
            algebraMap R A d * algebraMap R A b := by
          rw [hca, hC_mul, hbC]
          noncomm_ring
    _ = ((algebraMap R A c * algebraMap R A h + algebraMap R A d) * algebraMap R A a +
            algebraMap R A c * algebraMap R A b) * C +
          (algebraMap R A c * algebraMap R A a + algebraMap R A d * algebraMap R A b) := by
          have hcah :
              (algebraMap R A c * algebraMap R A a) * algebraMap R A h =
                algebraMap R A c * algebraMap R A h * algebraMap R A a := by
            simp only [← map_mul]; congr 1; ring
          calc
            (algebraMap R A c * algebraMap R A a) * (algebraMap R A h * C + 1) +
                (algebraMap R A c * algebraMap R A b) * C +
                (algebraMap R A d * algebraMap R A a) * C +
                algebraMap R A d * algebraMap R A b
                = ((algebraMap R A c * algebraMap R A a) * algebraMap R A h) * C +
                    (algebraMap R A d * algebraMap R A a) * C +
                    (algebraMap R A c * algebraMap R A b) * C +
                    (algebraMap R A c * algebraMap R A a +
                      algebraMap R A d * algebraMap R A b) := by noncomm_ring
            _ = ((algebraMap R A c * algebraMap R A h + algebraMap R A d) * algebraMap R A a +
                    algebraMap R A c * algebraMap R A b) * C +
                  (algebraMap R A c * algebraMap R A a +
                    algebraMap R A d * algebraMap R A b) := by
                  rw [hcah]; noncomm_ring

/-- Product of linear crossing elements `∏_{(c, d) ∈ L} (c • C + d • 1)` in an `R`-algebra `A`. -/
def crossingChainProd {A : Type*} [Ring A] [Algebra R A] (C : A) : List (R × R) → A
  | [] => 1
  | p :: ps => (p.1 • C + p.2 • (1 : A)) * crossingChainProd C ps

/-- **Multi-Crossing Transfer-Matrix Normal-Form Compression Theorem**:
For any finite crossing sequence `L : List (R × R)`, the product `crossingChainProd C L` reduces
in `O(L.length)` `2 × 2` matrix steps to the two-term Gröbner–Shirshov normal form
`v 0 • C + v 1 • 1`, where `v = (L.map (fun p => tmGeneral h p.1 p.2)).prod *ᵥ ![0, 1]`. -/
theorem crossingChain_eq_tmProduct_nf {A : Type*} [Ring A] [Algebra R A]
    (h : R) (C : A) (hC : C ^ 2 = h • C + 1) (L : List (R × R)) :
    let v := (L.map (fun p => tmGeneral h p.1 p.2)).prod *ᵥ ![0, 1]
    crossingChainProd C L = v 0 • C + v 1 • (1 : A) := by
  induction L with
  | nil =>
    simp [crossingChainProd]
  | cons p ps ih =>
    dsimp only at ih ⊢
    rw [crossingChainProd, ih, List.map_cons, List.prod_cons, ← Matrix.mulVec_mulVec]
    set w := (List.map (fun p => tmGeneral h p.1 p.2) ps).prod *ᵥ ![0, 1]
    have hw : ![w 0, w 1] = w := by
      ext i; fin_cases i <;> rfl
    have hstep := crossing_mul_nf_step h p.1 p.2 (w 0) (w 1) C hC
    rwa [hw] at hstep

/-- **Inverse (`nn`) Crossing Identity & Conjugate Quadratic Law**:
For `C_inv = C - h • 1`, if `C^2 = h • C + 1`, then `C_inv * C = 1`, `C * C_inv = 1`, and
`C_inv^2 = (-h) • C_inv + 1`. -/
theorem hecke_inv_relations {A : Type*} [Ring A] [Algebra R A]
    (h : R) (C : A) (hC : C ^ 2 = h • C + 1) :
    let C_inv := C - h • (1 : A)
    C_inv * C = 1 ∧ C * C_inv = 1 ∧ C_inv ^ 2 = (-h) • C_inv + 1 := by
  dsimp only
  have hC_mul : C * C = algebraMap R A h * C + 1 := by
    simpa [sq, Algebra.smul_def] using hC
  refine ⟨?_, ?_, ?_⟩
  · simp only [Algebra.smul_def, mul_one]
    calc
      (C - algebraMap R A h) * C = C * C - algebraMap R A h * C := by noncomm_ring
      _ = (algebraMap R A h * C + 1) - algebraMap R A h * C := by rw [hC_mul]
      _ = 1 := by noncomm_ring
  · simp only [Algebra.smul_def, mul_one]
    calc
      C * (C - algebraMap R A h) = C * C - C * algebraMap R A h := by noncomm_ring
      _ = (algebraMap R A h * C + 1) - algebraMap R A h * C := by
            rw [hC_mul, Algebra.commutes h C]
      _ = 1 := by noncomm_ring
  · simp only [sq, Algebra.smul_def, map_neg, mul_one]
    have hcomm : C * algebraMap R A h = algebraMap R A h * C :=
      (Algebra.commutes h C).symm
    calc
      (C - algebraMap R A h) * (C - algebraMap R A h)
          = C * C - C * algebraMap R A h - algebraMap R A h * C +
              algebraMap R A h * algebraMap R A h := by noncomm_ring
      _ = (algebraMap R A h * C + 1) - algebraMap R A h * C - algebraMap R A h * C +
              algebraMap R A h * algebraMap R A h := by rw [hC_mul, hcomm]
      _ = -algebraMap R A h * (C - algebraMap R A h) + 1 := by noncomm_ring

/-- **Achiral (`gg`) Symmetrized Crossing Square Collapse**:
Over a field `K` (`2 ≠ 0`), the symmetrized crossing `C_gg = C - (h / 2) • 1` has vanishing
linear generator term at `k = 2`: `C_gg^2 = (1 + h^2 / 4) • 1`. When `h = q - q⁻¹` (`q ≠ 0`),
`1 + h^2 / 4 = ((q^2 + 1) / (2 q))^2`. -/
theorem achiralGG_sq_scalar {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A]
    (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) (C : A)
    (hC : C ^ 2 = (q - q⁻¹) • C + 1) :
    let h := q - q⁻¹
    let C_gg := C - (h / 2) • (1 : A)
    C_gg ^ 2 = (1 + h ^ 2 / 4) • (1 : A) ∧
    1 + h ^ 2 / 4 = ((q ^ 2 + 1) / (2 * q)) ^ 2 := by
  dsimp only
  set h := q - q⁻¹
  have h4 : (4 : K) ≠ 0 := by
    rw [show (4 : K) = 2 * 2 by ring]
    exact mul_ne_zero h2 h2
  have hC_mul : C * C = algebraMap K A h * C + 1 := by
    simpa [sq, Algebra.smul_def] using hC
  have hcomm : C * algebraMap K A (h / 2) = algebraMap K A (h / 2) * C :=
    (Algebra.commutes (h / 2) C).symm
  have htwo_half : algebraMap K A h - algebraMap K A (h / 2) - algebraMap K A (h / 2) = 0 := by
    have hk : h - h / 2 - h / 2 = 0 := by field_simp [h2]; ring
    calc
      algebraMap K A h - algebraMap K A (h / 2) - algebraMap K A (h / 2)
          = algebraMap K A (h - h / 2 - h / 2) := by simp only [map_sub]
      _ = 0 := by rw [hk, map_zero]
  have hsq_half : algebraMap K A (h / 2) * algebraMap K A (h / 2) = algebraMap K A (h ^ 2 / 4) := by
    rw [← map_mul]
    congr 1
    field_simp [h2, h4]
    ring
  refine ⟨?_, ?_⟩
  · simp only [sq, Algebra.smul_def, map_add, map_one, mul_one]
    calc
      (C - algebraMap K A (h / 2)) * (C - algebraMap K A (h / 2))
          = C * C - C * algebraMap K A (h / 2) - algebraMap K A (h / 2) * C +
              algebraMap K A (h / 2) * algebraMap K A (h / 2) := by noncomm_ring
      _ = (algebraMap K A h - algebraMap K A (h / 2) - algebraMap K A (h / 2)) * C +
              (1 + algebraMap K A (h ^ 2 / 4)) := by
            rw [hC_mul, hcomm, hsq_half]
            noncomm_ring
      _ = 1 + algebraMap K A (h ^ 2 / 4) := by
            rw [htwo_half, zero_mul, zero_add]
      _ = 1 + algebraMap K A (h * h / 4) := by
            rw [← sq]
  · dsimp [h]
    field_simp [hq, h2, h4]
    ring

end TransferMatrixGroebnerReduction

-- ============================================================================
-- § 5. Multi-α Cluster Threshold Bridge: ⁸Be Instability vs ¹²C K_3 Closure
-- ============================================================================

section MultiAlphaThresholdBridge

/-- Simplicial topological counts on `^4He` (`A = 4`), `^8Be` (`A = 8`), and `^12C` (`A = 12`):
`^8Be` has `2` α-tetrahedra linked by only `1` inter-cluster bridge edge (`0.5` bridges per α),
whereas `^12C` has `3` α-tetrahedra linked by `3` inter-cluster `K_3` bridge edges (`1.0` bridge per α). -/
theorem alpha_cluster_light_medium_counts :
    (intraAlphaTetrahedra 4, intraAlphaEdges 4, interClusterEdges 4, totalAlphaClusterEdges 4) =
      (1, 6, 0, 6) ∧
    (intraAlphaTetrahedra 8, intraAlphaEdges 8, interClusterEdges 8, totalAlphaClusterEdges 8) =
      (2, 12, 1, 13) ∧
    (intraAlphaTetrahedra 12, intraAlphaEdges 12, interClusterEdges 12, totalAlphaClusterEdges 12) =
      (3, 18, 3, 21) ∧
    (intraAlphaTetrahedra 16, intraAlphaEdges 16, interClusterEdges 16, totalAlphaClusterEdges 16) =
      (4, 24, 6, 30) := by
  decide

/-- **`^8Be` vs `2 × ^4He` Breakup Threshold Cancellation Identity**:
For ANY intra-α strong cell energy `B_α` (whether 1-crossing or multi-crossing `H_4(Δ_4^2)` + GPMT)
and single inter-cluster bridge energy `b_inter`, `2 B_α` cancels identically in
`B(^8Be) - 2 B(^4He) = b_inter - (E_C(^8Be) - 2 E_C(^4He))`.
In an ordered ring, `^8Be` is unbound relative to `2 ^4He` iff `b_inter < E_C(^8Be) - 2 E_C(^4He)`. -/
theorem be8_two_alpha_threshold_diff {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (Bα bInter ecHe4 ecBe8 : R) :
    (2 * Bα + bInter - ecBe8) - 2 * (Bα - ecHe4) = bInter - (ecBe8 - 2 * ecHe4) ∧
    ((2 * Bα + bInter - ecBe8) < 2 * (Bα - ecHe4) ↔ bInter < ecBe8 - 2 * ecHe4) := by
  have hid : (2 * Bα + bInter - ecBe8) - 2 * (Bα - ecHe4) = bInter - (ecBe8 - 2 * ecHe4) := by
    ring
  refine ⟨hid, ?_⟩
  constructor <;> intro h <;> linarith

/-- **`^12C` vs `3 × ^4He` Triangular Hoyle/Ground Threshold Cancellation Identity**:
For ANY intra-α strong cell energy `B_α`, inter-cluster edge energy `b_inter`, and inter-cluster
3-body triangle energy `w3_inter`, `3 B_α` cancels identically in
`B(^12C) - 3 B(^4He) = 3 b_inter + w3_inter - (E_C(^12C) - 3 E_C(^4He))`. -/
theorem c12_three_alpha_threshold_diff {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (Bα bInter w3Inter ecHe4 ecC12 : R) :
    (3 * Bα + 3 * bInter + w3Inter - ecC12) - 3 * (Bα - ecHe4) =
      3 * bInter + w3Inter - (ecC12 - 3 * ecHe4) ∧
    (3 * (Bα - ecHe4) < (3 * Bα + 3 * bInter + w3Inter - ecC12) ↔
      ecC12 - 3 * ecHe4 < 3 * bInter + w3Inter) := by
  have hid :
      (3 * Bα + 3 * bInter + w3Inter - ecC12) - 3 * (Bα - ecHe4) =
        3 * bInter + w3Inter - (ecC12 - 3 * ecHe4) := by
    ring
  refine ⟨hid, ?_⟩
  constructor <;> intro h <;> linarith

end MultiAlphaThresholdBridge

end QOU.Nuclear.H4FullTwistAlphaCellAndGroebnerBridge
