/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import HeckeTemperleyLieb.QPartitionCombinatorics
import QOU.Nuclear.ColourReconnectionStokesAssembly

/-!
# Twelve-Quark Wigner `SU(4)` Spin-Isospin Pauli Antisymmetrizer & Chromomagnetic Binding

Closes Open Gap 1 (Option 1A) on light-nuclei `3q–12q` (`A = 1, 2, 3, 4`) colour-spin-isospin
binding (`0 sorry`, `0` custom `axiom`s, §7c generic rings/fields + `_real` bridge, zero empirical
literals):

1. **Conjugate Young-Diagram Pairing, Hook-Length Equality & `12q` Pauli Shell Closure (§1):**
   - Proves for every `A ≥ 1` that the `SU(3)_c`-singlet colour partition `rectThree A = [A, A, A]`
     has exact conjugate `colThree A = [3^A]` (`A` rows of length `3`), and vice versa
     (`conjugate_rectThree_eq_colThree`).
   - Proves for every `A : ℕ` that `hookLength (colThree A) i j = hookLength (rectThree A) j i`,
     so `spinIsospinSpechtDim A = su3SingletDim A` (`1, 5, 42, 462` for `A = 1, 2, 3, 4`).
   - Formalizes Wigner's `SU(4)_{στ}` Weyl hook-content dimension `su4WeylDimColThree A` over `ℤ`,
     proving `(20, 50, 20, 1)` for `A = (1, 2, 3, 4)` (unique `(S = 0, T = 0)` singlet at `⁴He`!)
     and **exact vanishing `su4WeylDimColThree A = 0` for all `A ≥ 5`** (`12`-quark `1s`-shell
     closure, paired with nucleon exterior-power `Nat.choose 4 A = 0` for `A ≥ 5`), plus the
     exact hidden-colour fraction `(d_A - 1) / d_A ∈ {0, 4/5, 41/42, 461/462}` and Matveev–Sorba /
     Harvey `6q` baryon-cluster decomposition `1/9 + 4/45 + 4/5 = 1`.

2. **Noncommutative Fierz–Pauli Identity, `SU(4)` Casimir & Chromomagnetic Spectrum `𝒪_CM` (§2):**
   - Over any (not necessarily commutative) `[Ring E]`, proves that commuting spin/isospin
     involutions `P_s² = P_t² = 1` obeying Pauli antisymmetry `P_c P_s P_t = -1` satisfy the exact
     operator identity `-((6 * P_c - 2) * (2 * P_s - 1)) = 12 * P_t - 6 * (P_s * P_t) +
     4 * P_s - 2` (`pauli_cmi_operator_identity`).
   - Over `[CommRing R]`, proves the Wigner supermultiplet `(S=1, T=0)` vs `(S=0, T=1)` pair-count
     identities (`wigner_pair_count_decomposition`).
   - Over any `[Field F]` (`char ≠ 2, 3, 5`), assembles the `n`-quark chromomagnetic eigenvalue
     `cmiEigenvalue n κ S_cas T_cas = n(n - 5) - 2 κ + (4/3) S_cas + 4 T_cas` from pair-transposition
     sums, proving `(-8, +8)` on `(N, Δ)` (splitting `16`), `+8/3` on `(0s)^6` `(S=1, T=0)`
     (short-range repulsive core `+56/3`), `+8` on `(0s)^6` `(S=0, T=1)` (repulsive core `+24`,
     exceeding deuteron by `+16/3`), `+40` on `(0s)^9`, `+96` on `(0s)^{12}`, and the Karl–Paton
     `6q` antisymmetrizer norm `⟨NN | 𝒜_6 | NN⟩ = 1/9` from `⟨P_{34}^{στ}⟩ = -1/27`.

3. **Exact `q`-Deformed Hoefsmit Conjugate Duality & Pauli Eigenstate (§3):**
   - Over any `[CommRing R]`, proves that if `X : Matrix (Fin n) (Fin n) R` satisfies the Hecke
     quadratic relation `X * X = h • X + 1` and `D = diagonal η` (`η_i² = 1`), then
     `Y := -(D * (X - h • 1)ᵀ * D)` satisfies `Y * Y = h • Y + 1`, `X * D * Yᵀ = -D` (exact `-1`
     eigenvalue on the maximally-entangled Pauli state for **every** braid-conjugated transposition,
     even when `Xᵀ ≠ X`), and the projected Pauli matrix `M_{ij} = -η_i η_j X_{ij} Y_{ij} =
     X_{ij} (X - h • 1)_{ji}` is **automatically symmetric** (`Mᵀ = M`) with **constant row-sum `+1`**.
   - Proves the `d = 3` inter-nucleon interface identity `[3]_q² - [2]_q [4]_q = 1`.

4. **Collective `K_A` Pauli Superradiance Bound & `ℝ` Specialisation (§4):**
   - Over any ordered field `F` (plus prescribed §7c `_real` bridge), proves that positive
     hidden-space Pauli self-attraction `0 < c_2 < c_4 < Δ₀` strictly amplifies the `A = 4` vs
     `A = 2` Schur-complement binding ratio beyond pairwise counting `C(4, 2) = 6`:
     `6 * |E_trial(2)| < |E_trial(4)|`.
-/

set_option autoImplicit false

namespace QOU.Nuclear.TwelveQuarkWignerPauliBinding

open scoped BigOperators Matrix
open Matrix
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.Nuclear.ColourReconnectionStokesAssembly

/-! ## §1. Conjugate Young-Diagram Pairing `[A, A, A]' = [3^A]`, Hooks & `12q` Shell Closure -/

section ConjugatePairingAndShellClosure

/-- Rectangular `A`-row, `3`-column partition `[3, 3, …, 3] ⊢ 3A` (`colThree A`) cutting out the
spin-isospin `S_{3A}` Specht module `S^{[3^A]}` conjugate to `SU(3)_c`-singlet colour `[A, A, A]`. -/
def colThree (A : ℕ) : Partition :=
  List.replicate A 3

private theorem maxPart_rectThree (A : ℕ) :
    Partition.maxPart (rectThree A) = A := by
  simp [Partition.maxPart, rectThree]

private theorem foldl_max_replicate_three (k : ℕ) :
    List.foldl Nat.max 3 (List.replicate k 3) = 3 := by
  induction k with
  | zero => rfl
  | succ m ih => simp [List.replicate_succ, ih]

private theorem maxPart_colThree {A : ℕ} (hA : 1 ≤ A) :
    Partition.maxPart (colThree A) = 3 := by
  rcases A with _ | k
  · omega
  · simp [Partition.maxPart, colThree, List.replicate_succ, foldl_max_replicate_three]

private theorem map_const_range_eq_replicate (n c : ℕ) :
    (List.range n).map (fun _ => c) = List.replicate n c := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [List.range_succ, List.map_append, ih, List.map_singleton, List.replicate_succ']

private theorem filter_gt_replicate_three (A j : ℕ) (hj : j < 3) :
    ((List.replicate A 3).filter (· > j)).length = A := by
  have hgt : decide (3 > j) = true := decide_eq_true hj
  simp [hgt]

/-- **Exact Conjugate Young-Diagram Pairing (`[A, A, A]' = [3^A]` and `[3^A]' = [A, A, A]`).**
For every `A ≥ 1`, transposing the `SU(3)_c`-singlet colour diagram `rectThree A = [A, A, A]` yields
`colThree A = [3^A]`, and transposing `colThree A` recovers `rectThree A`. -/
theorem conjugate_rectThree_eq_colThree {A : ℕ} (hA : 1 ≤ A) :
    Partition.conjugate (rectThree A) = colThree A ∧
    Partition.conjugate (colThree A) = rectThree A := by
  constructor
  · unfold Partition.conjugate colThree
    rw [maxPart_rectThree]
    have hmap : ((List.range A).map fun j => ((rectThree A).filter (· > j)).length) =
        (List.range A).map (fun _ => 3) := by
      refine List.map_congr_left fun j hj => ?_
      have hjA : j < A := List.mem_range.mp hj
      have hgt : decide (A > j) = true := decide_eq_true hjA
      simp [rectThree, hgt]
    rw [hmap, map_const_range_eq_replicate]
  · unfold Partition.conjugate
    rw [maxPart_colThree hA]
    have hr3 : List.range 3 = [0, 1, 2] := by decide
    rw [hr3]
    unfold colThree rectThree
    simp

/-- **Exact Hook-Length Transposition Identity on `colThree A = [3^A]`.**
Every cell `(i, j)` (`i < A`, `j < 3`) of `colThree A` has hook length `(A - i) + (2 - j)`, matching
the transposed cell `(j, i)` of `rectThree A`. -/
theorem hookLength_colThree (A i j : ℕ) (hi : i < A) (hj : j < 3) :
    Partition.hookLength (colThree A) i j = A - i + (2 - j) ∧
    Partition.hookLength (colThree A) i j = Partition.hookLength (rectThree A) j i := by
  have hval : Partition.hookLength (colThree A) i j = A - i + (2 - j) := by
    unfold Partition.hookLength colThree
    have hget : (List.replicate A 3)[i]? = some 3 := by
      rw [List.getElem?_eq_getElem (by simpa using hi), List.getElem_replicate]
    rw [hget]
    simp only [hj, ↓reduceIte, List.drop_replicate]
    rw [filter_gt_replicate_three (A - (i + 1)) j hj]
    omega
  exact ⟨hval, hval.trans (hookLength_rectThree A j i hj hi).symm⟩

/-- Product of all hook lengths across the `A × 3` cells of `colThree A`. -/
def hookProdColThree (A : ℕ) : ℕ :=
  ∏ i ∈ Finset.range A, ∏ j ∈ Finset.range 3, Partition.hookLength (colThree A) i j

/-- Dimension `(3A)! / hookProdColThree A` of the spin-isospin Specht module `S^{[3^A]}`. -/
def spinIsospinSpechtDim (A : ℕ) : ℕ :=
  (3 * A).factorial / hookProdColThree A

/-- **General-`A` Hook-Product & Specht-Dimension Equality (`dim S^{[3^A]} = dim S^{[A,A,A]}`).** -/
theorem hookProd_and_spechtDim_colThree_eq (A : ℕ) :
    hookProdColThree A = hookProdRectThree A ∧
    spinIsospinSpechtDim A = su3SingletDim A := by
  have hprod : hookProdColThree A = hookProdRectThree A := by
    unfold hookProdColThree hookProdRectThree
    rw [Finset.prod_comm]
    refine Finset.prod_congr rfl fun j hj => Finset.prod_congr rfl fun i hi => ?_
    exact (hookLength_colThree A i j (Finset.mem_range.mp hi) (Finset.mem_range.mp hj)).2
  exact ⟨hprod, by unfold spinIsospinSpechtDim su3SingletDim; rw [hprod]⟩

/-- Stanley–Weyl `SU(4)_{στ}` hook-content numerator `∏_{i < A} ∏_{j < 3} (4 + j - i)` in `ℤ`. -/
def su4ContentProd (A : ℕ) : ℤ :=
  ∏ i ∈ Finset.range A, ∏ j ∈ Finset.range 3, ((4 : ℤ) + (j : ℤ) - (i : ℤ))

/-- Wigner `SU(4)_{στ}` Weyl module dimension `dim V^{SU(4)}_{[3^A]} = su4ContentProd A / hookProd`
over `ℤ` (free of `ℕ`-subtraction truncation). -/
def su4WeylDimColThree (A : ℕ) : ℤ :=
  su4ContentProd A / (hookProdColThree A : ℤ)

/-- **Exact Wigner `SU(4)_{στ}` Multiplicity Spectrum & `12`-Quark `1s`-Shell Closure (`A ≥ 5`).**
1. Exact hook-product divisibility and Weyl dimensions `(20, 50, 20, 1)` for `A = 1, 2, 3, 4`:
   at `A = 4` (`⁴He`), `dim V^{SU(4)}_{[3,3,3,3]} = 1` (unique `(S = 0, T = 0)` singlet, blocking
   all global `Δ` admixtures);
2. For **every** `A ≥ 5` (`15+` quarks), `su4ContentProd A = 0`, `su4WeylDimColThree A = 0`, and
   nucleon exterior power `Nat.choose 4 A = 0` (exact Pauli `s`-shell closure after `⁴He`). -/
theorem su4WeylDim_light_nuclei_and_shell_closure :
    ((hookProdColThree 1 : ℤ) ∣ su4ContentProd 1 ∧ su4WeylDimColThree 1 = 20) ∧
    ((hookProdColThree 2 : ℤ) ∣ su4ContentProd 2 ∧ su4WeylDimColThree 2 = 50) ∧
    ((hookProdColThree 3 : ℤ) ∣ su4ContentProd 3 ∧ su4WeylDimColThree 3 = 20) ∧
    ((hookProdColThree 4 : ℤ) ∣ su4ContentProd 4 ∧ su4WeylDimColThree 4 = 1) ∧
    (Nat.choose 4 1 = 4 ∧ Nat.choose 4 2 = 6 ∧ Nat.choose 4 3 = 4 ∧ Nat.choose 4 4 = 1) ∧
    (∀ A : ℕ, 5 ≤ A →
      su4ContentProd A = 0 ∧ su4WeylDimColThree A = 0 ∧ Nat.choose 4 A = 0) := by
  refine ⟨by decide, by decide, by decide, by decide, by decide, fun A hA => ?_⟩
  have hinner0 : (∏ j ∈ Finset.range 3, ((4 : ℤ) + (j : ℤ) - ((4 : ℕ) : ℤ))) = 0 := by
    refine Finset.prod_eq_zero (Finset.mem_range.mpr (by decide : 0 < 3)) ?_
    norm_num
  have hnum0 : su4ContentProd A = 0 := by
    unfold su4ContentProd
    exact Finset.prod_eq_zero (Finset.mem_range.mpr (by omega : 4 < A)) hinner0
  have hdim0 : su4WeylDimColThree A = 0 := by
    unfold su4WeylDimColThree
    rw [hnum0, Int.zero_ediv]
  exact ⟨hnum0, hdim0, Nat.choose_eq_zero_of_lt (by omega : 4 < A)⟩

/-- Hidden-colour probability `(d_A - 1) / d_A` in the maximally-entangled `(0s)^{3A}` Pauli state
over any `[Field F]`. -/
def pauliHiddenFraction (F : Type*) [Field F] (A : ℕ) : F :=
  ((su3SingletDim A : F) - 1) / (su3SingletDim A : F)

/-- **Exact `(0s)^{3A}` Hidden-Colour Fractions & Matveev–Sorba / Harvey `6q` Sum Rule.**
Over any field `F` of characteristic `≠ 2, 3, 5, 7, 11`:
1. `pauliHiddenFraction` evaluates to `(0, 4/5, 41/42, 461/462)` for `A = 1, 2, 3, 4`;
2. At `A = 2` (`6q`), `P_{NN} = 1/9`, `P_{ΔΔ} = 4/45`, and `P_{88} = 4/5` satisfy
   `1/9 + 4/45 = 1/5 = 1 / d_2` and `1/9 + 4/45 + 4/5 = 1`. -/
theorem pauliHiddenFraction_and_harvey_sum_rule {F : Type*} [Field F]
    (h2 : (2 : F) ≠ 0) (h3 : (3 : F) ≠ 0) (h5 : (5 : F) ≠ 0)
    (h7 : (7 : F) ≠ 0) (h11 : (11 : F) ≠ 0) :
    pauliHiddenFraction F 1 = 0 ∧
    pauliHiddenFraction F 2 = 4 / 5 ∧
    pauliHiddenFraction F 3 = 41 / 42 ∧
    pauliHiddenFraction F 4 = 461 / 462 ∧
    ((1 : F) / 9 + 4 / 45 = 1 / 5 ∧ (1 : F) / 9 + 4 / 45 + 4 / 5 = 1) := by
  have hd1 : su3SingletDim 1 = 1 := su3SingletDim_light_nuclei.1.1
  have hd2 : su3SingletDim 2 = 5 := su3SingletDim_light_nuclei.2.1.1
  have hd3 : su3SingletDim 3 = 42 := su3SingletDim_light_nuclei.2.2.1.1
  have hd4 : su3SingletDim 4 = 462 := su3SingletDim_light_nuclei.2.2.2.1
  have h9 : (9 : F) ≠ 0 := by
    have : (9 : F) = 3 * 3 := by norm_num
    rw [this]; exact mul_ne_zero h3 h3
  have h45 : (45 : F) ≠ 0 := by
    have : (45 : F) = 9 * 5 := by norm_num
    rw [this]; exact mul_ne_zero h9 h5
  have h42 : (42 : F) ≠ 0 := by
    have : (42 : F) = 2 * 3 * 7 := by norm_num
    rw [this]; exact mul_ne_zero (mul_ne_zero h2 h3) h7
  have h462 : (462 : F) ≠ 0 := by
    have : (462 : F) = 42 * 11 := by norm_num
    rw [this]; exact mul_ne_zero h42 h11
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · unfold pauliHiddenFraction; rw [hd1]; simp
  · unfold pauliHiddenFraction; rw [hd2]; norm_num
  · unfold pauliHiddenFraction; rw [hd3]
    apply mul_right_cancel₀ h42
    field_simp [h42]; norm_num
  · unfold pauliHiddenFraction; rw [hd4]
    apply mul_right_cancel₀ h462
    field_simp [h462]; norm_num
  · apply mul_right_cancel₀ h45
    field_simp [h9, h45, h5]; norm_num
  · apply mul_right_cancel₀ h45
    field_simp [h9, h45, h5]; norm_num

end ConjugatePairingAndShellClosure

/-! ## §2. Noncommutative Fierz–Pauli Algebra, `SU(4)` Casimir & Chromomagnetic Operator `𝒪_CM` -/

section ChromomagneticAndWignerCasimir

/-- **Exact Content-Sum Skew-Symmetry & Quadratic `SU(4)` Casimir Values (`A = 1..4`).**
On `colThree A = [3^A]` vs `rectThree A = [A, A, A]`:
1. `contentSum [3^A] = (3, 3, 0, -6)` and `contentSum [A,A,A] = (-3, -3, 0, 6)` for `A = 1..4`;
2. Cleared quadratic `SU(4)` Casimir `8 * C₂^{SU(4)}([3^A]) = 8 * κ([3^A]) + 3A(16 - 3A)` evaluates
   to `(63, 84, 63, 0)` for `A = (1, 2, 3, 4)` — vanishing identically at `⁴He` (`A = 4`)! -/
theorem contentSum_and_su4Casimir_light_nuclei :
    (contentSum (colThree 1) = 3 ∧ contentSum (rectThree 1) = -3) ∧
    (contentSum (colThree 2) = 3 ∧ contentSum (rectThree 2) = -3) ∧
    (contentSum (colThree 3) = 0 ∧ contentSum (rectThree 3) = 0) ∧
    (contentSum (colThree 4) = -6 ∧ contentSum (rectThree 4) = 6) ∧
    (8 * contentSum (colThree 1) + 3 * 1 * (16 - 3 * 1) = 63 ∧
      8 * contentSum (colThree 2) + 3 * 2 * (16 - 3 * 2) = 84 ∧
      8 * contentSum (colThree 3) + 3 * 3 * (16 - 3 * 3) = 63 ∧
      8 * contentSum (colThree 4) + 3 * 4 * (16 - 3 * 4) = 0) := by
  decide

/-- **Exact Noncommutative Two-Quark Fierz–Pauli Chromomagnetic Identity (`[Ring E]`).**
In any (not necessarily commutative) ring `E` (such as `End_R(V)` or `Matrix n n R`), if `P_c, P_s, P_t`
satisfy `P_s² = 1`, `P_t² = 1`, `P_s P_t = P_t P_s`, and total Pauli antisymmetry `P_c P_s P_t = -1`,
then `P_c P_s = -P_t`, `P_c = -(P_s P_t)`, and the cleared colour-magnetic pair operator
`-(3 (λ_i · λ_j) (σ_i · σ_j)) = -((6 * P_c - 2) * (2 * P_s - 1))` equals
`12 * P_t - 6 * (P_s * P_t) + 4 * P_s - 2`. -/
theorem pauli_cmi_operator_identity {E : Type*} [Ring E]
    (P_c P_s P_t : E)
    (hs2 : P_s * P_s = 1) (ht2 : P_t * P_t = 1) (hst : P_s * P_t = P_t * P_s)
    (hpauli : P_c * P_s * P_t = -1) :
    P_c * P_s = -P_t ∧
    P_c = -(P_s * P_t) ∧
    -((6 * P_c - 2) * (2 * P_s - 1)) =
      12 * P_t - 6 * (P_s * P_t) + 4 * P_s - 2 := by
  have hcs : P_c * P_s = -P_t := by
    calc P_c * P_s
        = (P_c * P_s) * 1 := (mul_one _).symm
      _ = (P_c * P_s) * (P_t * P_t) := by rw [ht2]
      _ = (P_c * P_s * P_t) * P_t := (mul_assoc _ _ _).symm
      _ = (-1) * P_t := by rw [hpauli]
      _ = -P_t := by simp
  have hc : P_c = -(P_s * P_t) := by
    calc P_c
        = P_c * 1 := (mul_one _).symm
      _ = P_c * (P_s * P_s) := by rw [hs2]
      _ = (P_c * P_s) * P_s := (mul_assoc _ _ _).symm
      _ = (-P_t) * P_s := by rw [hcs]
      _ = -(P_t * P_s) := neg_mul P_t P_s
      _ = -(P_s * P_t) := by rw [hst]
  refine ⟨hcs, hc, ?_⟩
  have hexp :
      -((6 * P_c - 2) * (2 * P_s - 1)) =
        -(12 * (P_c * P_s)) + 6 * P_c + 4 * P_s - 2 := by
    noncomm_ring
  rw [hexp, hcs, hc]
  noncomm_ring

/-- Cleared Wigner supermultiplet `(S=1, T=0)` deuteron-pair count `4 * N_{(1,0)} = A(A - 1) + S_cas - T_cas`
and `(S=0, T=1)` dinucleon-pair count `4 * N_{(0,1)} = A(A - 1) - (S_cas - T_cas)` over `[CommRing R]`. -/
def wignerPairCount4 {R : Type*} [CommRing R] (A S_cas T_cas : R) : R × R :=
  (A * (A - 1) + (S_cas - T_cas), A * (A - 1) - (S_cas - T_cas))

/-- **Wigner `SU(4)` Supermultiplet Pair-Count Decomposition (`[CommRing R]`).**
Over any commutative ring `R`, `wignerPairCount4 A S_cas T_cas` sums to `2 * A * (A - 1)` (`4 * C(A,2)`)
and differs by `2 * (S_cas - T_cas)`, giving cleared `(4 N_{10}, 4 N_{01})` values `(4, 0)` for `²H`,
`(0, 4)` for `¹S₀` dinucleon, `(6, 6)` (`3/2, 3/2` pairs) for `³H/³He`, and `(12, 12)` (`3, 3` pairs)
for `⁴He`. -/
theorem wigner_pair_count_decomposition {R : Type*} [CommRing R] :
    (∀ A S_cas T_cas : R,
      (wignerPairCount4 A S_cas T_cas).1 + (wignerPairCount4 A S_cas T_cas).2 = 2 * A * (A - 1) ∧
      (wignerPairCount4 A S_cas T_cas).1 - (wignerPairCount4 A S_cas T_cas).2 = 2 * (S_cas - T_cas)) ∧
    wignerPairCount4 (2 : R) 2 0 = (4, 0) ∧
    wignerPairCount4 (2 : R) 0 2 = (0, 4) ∧
    wignerPairCount4 (4 : R) 0 0 = (12, 12) := by
  refine ⟨fun A S_cas T_cas => ⟨by unfold wignerPairCount4; ring, by unfold wignerPairCount4; ring⟩,
    ?_, ?_, ?_⟩ <;>
    · unfold wignerPairCount4; ext <;> norm_num

/-- Closed-form eigenvalue of the `n`-quark chromomagnetic operator
`𝒪_CM = -∑_{1 ≤ i < j ≤ n} (λ_i · λ_j)(σ_i · σ_j)` on an `(0s)^n` Pauli-antisymmetric state with
spin-isospin content sum `κ`, spin Casimir `S_cas = S(S+1)`, and isospin Casimir `T_cas = T(T+1)`. -/
def cmiEigenvalue {F : Type*} [Field F] (n κ S_cas T_cas : F) : F :=
  n * (n - 5) - 2 * κ + (4 / 3) * S_cas + 4 * T_cas

/-- **Exact Chromomagnetic Operator Sum Assembly, Repulsive Core & `6q` Pauli Norm (`[Field F]`).**
Over any field `F` with `(2 : F) ≠ 0`, `(3 : F) ≠ 0`, and `(5 : F) ≠ 0`:
1. Summing `4 P_t - 2 P_{st} + (4/3) P_s - 2/3` over all `n(n-1)/2` pairs with
   `∑ P_s = S_cas + n(n-4)/4`, `∑ P_t = T_cas + n(n-4)/4`, and `∑ P_{st} = κ` equals
   `cmiEigenvalue n κ S_cas T_cas`;
2. `N` (`n=3, κ=3, S_cas=3/4, T_cas=3/4`) has `-8` and `Δ` (`S_cas=T_cas=15/4`) has `+8` (gap `16`);
3. `(0s)^6` deuteron `(S=1, T=0)` has `+8/3` (short-range repulsive core `+56/3` above `2N = -16`),
   while `(0s)^6` dinucleon `(S=0, T=1)` has `+8` (core `+24`, exceeding deuteron by `+16/3`);
4. `(0s)^9` (`S=T=1/2`) has `+40` (core `+64` above `3N`) and `(0s)^{12}` (`S=T=0`) has `+96`
   (core `+128` above `4N`);
5. Karl–Paton `6q` spin-isospin exchange `(1/4)(1 + (1/9)(1) + (1/9)(-3) + (25/81)(-3)) = -1/27`
   yields the exact antisymmetrizer norm `(1/20)(1 - 9(1/3)(-1/27) - 9(1/3)(-1/27) + 1) = 1/9`. -/
theorem cmi_spectrum_and_pauli_norm {F : Type*} [Field F]
    (h2 : (2 : F) ≠ 0) (h3 : (3 : F) ≠ 0) (h5 : (5 : F) ≠ 0) :
    (∀ n κ S_cas T_cas : F,
      4 * (T_cas + n * (n - 4) / 4) - 2 * κ + (4 / 3) * (S_cas + n * (n - 4) / 4) -
        (2 / 3) * (n * (n - 1) / 2) = cmiEigenvalue n κ S_cas T_cas) ∧
    (cmiEigenvalue (3 : F) 3 (3 / 4) (3 / 4) = -8 ∧
      cmiEigenvalue (3 : F) 3 (15 / 4) (15 / 4) = 8) ∧
    (cmiEigenvalue (6 : F) 3 2 0 = 8 / 3 ∧
      cmiEigenvalue (6 : F) 3 2 0 - 2 * (-8) = 56 / 3 ∧
      cmiEigenvalue (6 : F) 3 0 2 = 8 ∧
      cmiEigenvalue (6 : F) 3 0 2 - cmiEigenvalue (6 : F) 3 2 0 = 16 / 3) ∧
    (cmiEigenvalue (9 : F) 0 (3 / 4) (3 / 4) = 40 ∧
      cmiEigenvalue (12 : F) (-6) 0 0 = 96) ∧
    (((1 : F) / 4) * (1 + (1 / 9) * 1 + (1 / 9) * (-3) + (25 / 81) * (-3)) = -1 / 27 ∧
      ((1 : F) / 20) * (1 - 9 * (1 / 3) * (-1 / 27) - 9 * (1 / 3) * (-1 / 27) + 1) = 1 / 9) := by
  have h4 : (4 : F) ≠ 0 := by
    have : (4 : F) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  have h9 : (9 : F) ≠ 0 := by
    have : (9 : F) = 3 * 3 := by norm_num
    rw [this]; exact mul_ne_zero h3 h3
  have h20 : (20 : F) ≠ 0 := by
    have : (20 : F) = 4 * 5 := by norm_num
    rw [this]; exact mul_ne_zero h4 h5
  have h27 : (27 : F) ≠ 0 := by
    have : (27 : F) = 9 * 3 := by norm_num
    rw [this]; exact mul_ne_zero h9 h3
  have h81 : (81 : F) ≠ 0 := by
    have : (81 : F) = 9 * 9 := by norm_num
    rw [this]; exact mul_ne_zero h9 h9
  refine ⟨fun n κ S_cas T_cas => ?_, ⟨?_, ?_⟩, ⟨?_, ?_, ?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · unfold cmiEigenvalue
    apply mul_right_cancel₀ (mul_ne_zero h3 h4)
    field_simp [h2, h3, h4]
    ring
  · unfold cmiEigenvalue; field_simp [h2, h3, h4]; ring
  · unfold cmiEigenvalue; field_simp [h2, h3, h4]; ring
  · unfold cmiEigenvalue; field_simp [h3]; ring
  · unfold cmiEigenvalue; field_simp [h3]; ring
  · unfold cmiEigenvalue; field_simp [h3]; ring
  · unfold cmiEigenvalue; field_simp [h3]; ring
  · unfold cmiEigenvalue; field_simp [h2, h3, h4]; ring
  · unfold cmiEigenvalue; field_simp [h3]; ring
  · apply mul_right_cancel₀ (mul_ne_zero h4 h81)
    field_simp [h4, h9, h27, h81]; norm_num
  · apply mul_right_cancel₀ (mul_ne_zero h20 h27)
    field_simp [h3, h9, h20, h27]; norm_num

end ChromomagneticAndWignerCasimir

/-! ## §3. Exact `q`-Deformed Hoefsmit Conjugate Duality & Pauli Bell/Slater Eigenstate -/

section HeckeConjugateDualityAndPauliMatrix

/-- Inverse `X - h • 1` of any Hecke-quadratic matrix `X` satisfying `X * X = h • X + 1`. -/
def heckeInv {R : Type*} [CommRing R] {n : ℕ} (h : R) (X : Matrix (Fin n) (Fin n) R) :
    Matrix (Fin n) (Fin n) R :=
  X - h • 1

/-- Conjugate-partition Hoefsmit matrix `Y = -(D * (X - h • 1)ᵀ * D)` with Yamanouchi sign diagonal
`D = diagonal η` (`η_i² = 1`). -/
def heckeConjDual {R : Type*} [CommRing R] {n : ℕ} (h : R) (η : Fin n → R)
    (X : Matrix (Fin n) (Fin n) R) : Matrix (Fin n) (Fin n) R :=
  -(diagonal η * (heckeInv h X).transpose * diagonal η)

/-- Projected Pauli-conjugate matrix `M_{ij} = X_{ij} (X - h • 1)_{ji}` representing
`-(X ⊗ Y)` restricted to `span { η_i (e_i ⊗ e'_i) }`. -/
def pauliProjMat {R : Type*} [CommRing R] {n : ℕ} (h : R) (X : Matrix (Fin n) (Fin n) R) :
    Matrix (Fin n) (Fin n) R :=
  Matrix.of fun i j => X i j * heckeInv h X j i

private theorem diagonal_sq_eq_one {R : Type*} [CommRing R] {n : ℕ}
    {η : Fin n → R} (hη : ∀ i, η i ^ 2 = 1) :
    diagonal η * diagonal η = (1 : Matrix (Fin n) (Fin n) R) := by
  ext i j
  rw [diagonal_mul_diagonal]
  by_cases hij : i = j
  · subst hij
    simp only [diagonal_apply_eq, one_apply_eq]
    linear_combination hη i
  · simp [diagonal_apply_ne _ hij, one_apply_ne hij]

/-- **Exact `q`-Deformed Hoefsmit Conjugate Duality & Pauli Eigenstate Theorem (`[CommRing R]`).**
Over any commutative ring `R` and any dimension `n : ℕ`, whenever `X * X = h • X + 1` and
`∀ i, η i ^ 2 = 1`:
1. `X * heckeInv h X = 1` and `heckeInv h X * X = 1`;
2. `Y := heckeConjDual h η X` satisfies the identical Hecke quadratic relation `Y * Y = h • Y + 1`;
3. `X * diagonal η * Yᵀ = -diagonal η` (i.e. `(X ⊗ Y) |Ψ_Pauli⟩ = -|Ψ_Pauli⟩` holds for **every**
   braid-conjugated transposition, even when `Xᵀ ≠ X`);
4. `pauliProjMat h X` equals `-(η_i η_j X_{ij} Y_{ij})` entrywise, is **automatically symmetric**
   (`(pauliProjMat h X)ᵀ = pauliProjMat h X`), and has **exact constant row-sum `+1`**. -/
theorem hecke_conjugate_duality_and_pauli_invariance
    {R : Type*} [CommRing R] {n : ℕ} (h : R) (η : Fin n → R)
    (X : Matrix (Fin n) (Fin n) R)
    (hX : X * X = h • X + 1) (hη : ∀ i, η i ^ 2 = 1) :
    let Xinv := heckeInv h X
    let Y := heckeConjDual h η X
    let M := pauliProjMat h X
    (X * Xinv = 1 ∧ Xinv * X = 1) ∧
    Y * Y = h • Y + 1 ∧
    X * diagonal η * Y.transpose = -diagonal η ∧
    (∀ i j, -(η i * η j * X i j * Y i j) = M i j) ∧
    M.transpose = M ∧
    (∀ i : Fin n, (∑ j : Fin n, M i j) = 1) := by
  dsimp only
  set D := diagonal η with hD_def
  have hD2 : D * D = 1 := diagonal_sq_eq_one hη
  have hDT : D.transpose = D := diagonal_transpose η
  have hXinv_r : X * heckeInv h X = 1 := by
    unfold heckeInv
    rw [mul_sub, mul_smul_comm, mul_one, hX]
    abel
  have hXinv_l : heckeInv h X * X = 1 := by
    unfold heckeInv
    rw [sub_mul, smul_mul_assoc, one_mul, hX]
    abel
  have hXinv_sq : heckeInv h X * heckeInv h X = 1 - h • heckeInv h X := by
    have h1 : (heckeInv h X + h • (1 : Matrix (Fin n) (Fin n) R)) = X := by
      unfold heckeInv; abel
    have h2 : (heckeInv h X + h • 1) * heckeInv h X = 1 := by
      rw [h1]; exact hXinv_r
    rw [add_mul, smul_mul_assoc, one_mul] at h2
    exact eq_sub_of_add_eq h2
  have hXinvT_sq : (heckeInv h X).transpose * (heckeInv h X).transpose =
      1 - h • (heckeInv h X).transpose := by
    rw [← transpose_mul, hXinv_sq, transpose_sub, transpose_one, transpose_smul]
  have hY_quad : heckeConjDual h η X * heckeConjDual h η X = h • heckeConjDual h η X + 1 := by
    unfold heckeConjDual
    rw [← hD_def, neg_mul_neg]
    calc (D * (heckeInv h X).transpose * D) * (D * (heckeInv h X).transpose * D)
        = D * (heckeInv h X).transpose * (D * D) * (heckeInv h X).transpose * D := by
            simp only [Matrix.mul_assoc]
      _ = D * ((heckeInv h X).transpose * (heckeInv h X).transpose) * D := by
            rw [hD2, mul_one]; simp only [Matrix.mul_assoc]
      _ = D * (1 - h • (heckeInv h X).transpose) * D := by rw [hXinvT_sq]
      _ = D * D - h • (D * (heckeInv h X).transpose * D) := by
            rw [mul_sub, mul_one, sub_mul, mul_smul_comm, smul_mul_assoc]
      _ = h • (-(D * (heckeInv h X).transpose * D)) + 1 := by
            rw [hD2, smul_neg]; abel
  have hPauli : X * D * (heckeConjDual h η X).transpose = -D := by
    unfold heckeConjDual
    rw [← hD_def, transpose_neg, transpose_mul, transpose_mul, transpose_transpose, hDT]
    calc X * D * -(D * (heckeInv h X * D))
        = -(X * (D * D) * (heckeInv h X * D)) := by
            rw [mul_neg]; simp only [Matrix.mul_assoc]
      _ = -((X * heckeInv h X) * D) := by
            rw [hD2, mul_one, Matrix.mul_assoc]
      _ = -D := by rw [hXinv_r, one_mul]
  have hentry : ∀ i j : Fin n,
      -(η i * η j * X i j * heckeConjDual h η X i j) = pauliProjMat h X i j := by
    intro i j
    unfold heckeConjDual pauliProjMat
    simp only [neg_apply, diagonal_mul, mul_diagonal, transpose_apply, of_apply]
    calc -(η i * η j * X i j * -(η i * heckeInv h X j i * η j))
        = (η i ^ 2) * (η j ^ 2) * (X i j * heckeInv h X j i) := by ring
      _ = X i j * heckeInv h X j i := by rw [hη i, hη j]; ring
  have hsym : (pauliProjMat h X).transpose = pauliProjMat h X := by
    ext i j
    simp only [pauliProjMat, transpose_apply, of_apply, heckeInv, sub_apply, smul_apply,
      smul_eq_mul]
    by_cases hij : i = j
    · subst hij; rfl
    · rw [one_apply_ne hij, one_apply_ne (Ne.symm hij)]
      ring
  have hrow : ∀ i : Fin n, (∑ j : Fin n, pauliProjMat h X i j) = 1 := by
    intro i
    simp only [pauliProjMat, of_apply]
    rw [← Matrix.mul_apply, hXinv_r, one_apply_eq]
  exact ⟨⟨hXinv_r, hXinv_l⟩, hY_quad, hPauli, hentry, hsym, hrow⟩

/-- **Exact `d = 3` Inter-Nucleon Pauli Interface Identity (`[3]_q² - [2]_q [4]_q = 1`).**
Over any field `F` with `q ≠ 0` and `[3]_q = q² + 1 + q⁻² ≠ 0`, the diagonal Pauli expectation on
`|Φ_fac⟩` at axial distance `d = 3` satisfies `1 - ([2]_q [4]_q) / [3]_q² = 1 / [3]_q²` (`1/9` at
`q = 1`). -/
theorem pauli_interface_d3_identity {F : Type*} [Field F] (q : F)
    (hq : q ≠ 0) (hq3 : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0) :
    let q2 := q + q⁻¹
    let q3 := q ^ 2 + 1 + q⁻¹ ^ 2
    let q4 := q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3
    q3 ^ 2 - q2 * q4 = 1 ∧
    1 - (q2 * q4) / q3 ^ 2 = 1 / q3 ^ 2 := by
  dsimp only
  have hpoly : (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2 - (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) = 1 := by
    field_simp [hq]
    ring
  refine ⟨hpoly, ?_⟩
  have hq3sq : (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2 ≠ 0 := pow_ne_zero 2 hq3
  apply mul_right_cancel₀ hq3sq
  calc (1 - (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2) *
          (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2
      = (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2 -
          ((q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2) *
            (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2 := by ring
    _ = (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2 - (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) := by
          rw [div_mul_cancel₀ _ hq3sq]
    _ = 1 := hpoly
    _ = (1 / (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2) * (q ^ 2 + 1 + q⁻¹ ^ 2) ^ 2 := by
          rw [one_div_mul_cancel hq3sq]

end HeckeConjugateDualityAndPauliMatrix

/-! ## §4. Collective `K_A` Pauli Superradiance Bound & `ℝ` Specialisation (§7c) -/

section CollectivePauliSuperradiance

/-- Collective Schur-complement ground-energy shift `-vSq / (Δ₀ - c)` with hidden-space Pauli
self-attraction `c < Δ₀`. -/
def collectiveSchurShift {F : Type*} [Field F] (vSq Δ₀ c : F) : F :=
  -vSq / (Δ₀ - c)

/-- **Collective `K_4` vs `K_2` Pauli Superradiance Amplification Theorem (§7c Ordered Field).**
Over any `[Field F] [LinearOrder F] [IsStrictOrderedRing F]`, if `0 < v2Sq` and hidden-space Pauli
self-attraction grows strictly from `A = 2` to `A = 4` (`0 < c2 < c4 < Δ₀`), then with complete-graph
pair count `C(4, 2) = 6 * C(2, 2)`:
1. Both `A = 2` and `A = 4` collective shifts are strictly negative, with `v2Sq / Δ₀ < |E_trial(2)|`;
2. `|E_trial(4)| = 6 * ((Δ₀ - c2) / (Δ₀ - c4)) * |E_trial(2)|`;
3. `6 * |E_trial(2)| < |E_trial(4)|` (strict super-pairwise enhancement beyond `6 : 1`!). -/
theorem pauli_collective_schur_superradiance
    {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (v2Sq Δ₀ c2 c4 : F)
    (hv2 : 0 < v2Sq) (hc2 : 0 < c2) (hc24 : c2 < c4) (hc4 : c4 < Δ₀) :
    collectiveSchurShift v2Sq Δ₀ c2 < 0 ∧
    v2Sq / Δ₀ < -collectiveSchurShift v2Sq Δ₀ c2 ∧
    collectiveSchurShift (6 * v2Sq) Δ₀ c4 < 0 ∧
    -collectiveSchurShift (6 * v2Sq) Δ₀ c4 =
      6 * ((Δ₀ - c2) / (Δ₀ - c4)) * (-collectiveSchurShift v2Sq Δ₀ c2) ∧
    6 * (-collectiveSchurShift v2Sq Δ₀ c2) < -collectiveSchurShift (6 * v2Sq) Δ₀ c4 := by
  have hden4 : 0 < Δ₀ - c4 := sub_pos.mpr hc4
  have hden2 : 0 < Δ₀ - c2 := by linarith
  have hΔ_pos : 0 < Δ₀ := by linarith
  have hpos2 : 0 < v2Sq / (Δ₀ - c2) := div_pos hv2 hden2
  have hpos4 : 0 < (6 * v2Sq) / (Δ₀ - c4) := div_pos (by linarith) hden4
  have hneg2 : collectiveSchurShift v2Sq Δ₀ c2 < 0 := by
    unfold collectiveSchurShift; rw [neg_div]; linarith
  have hgt_bh2 : v2Sq / Δ₀ < -collectiveSchurShift v2Sq Δ₀ c2 := by
    unfold collectiveSchurShift
    rw [neg_div, neg_neg]
    exact div_lt_div_of_pos_left hv2 hden2 (by linarith)
  have hneg4 : collectiveSchurShift (6 * v2Sq) Δ₀ c4 < 0 := by
    unfold collectiveSchurShift; rw [neg_div]; linarith
  have hrat_eq : -collectiveSchurShift (6 * v2Sq) Δ₀ c4 =
      6 * ((Δ₀ - c2) / (Δ₀ - c4)) * (-collectiveSchurShift v2Sq Δ₀ c2) := by
    unfold collectiveSchurShift
    have hd2_ne : Δ₀ - c2 ≠ 0 := ne_of_gt hden2
    have hd4_ne : Δ₀ - c4 ≠ 0 := ne_of_gt hden4
    field_simp [hd2_ne, hd4_ne]
  refine ⟨hneg2, hgt_bh2, hneg4, hrat_eq, ?_⟩
  have hgt1 : 1 < (Δ₀ - c2) / (Δ₀ - c4) := (one_lt_div hden4).mpr (by linarith)
  have hb2_pos : 0 < -collectiveSchurShift v2Sq Δ₀ c2 := by linarith
  calc 6 * (-collectiveSchurShift v2Sq Δ₀ c2)
      = 6 * 1 * (-collectiveSchurShift v2Sq Δ₀ c2) := by ring
    _ < 6 * ((Δ₀ - c2) / (Δ₀ - c4)) * (-collectiveSchurShift v2Sq Δ₀ c2) := by
        nlinarith
    _ = -collectiveSchurShift (6 * v2Sq) Δ₀ c4 := hrat_eq.symm

/-- Archimedean `ℝ` specialisation of `pauli_collective_schur_superradiance` (prescribed `§7c` `_real` bridge). -/
theorem pauli_collective_schur_superradiance_real
    (v2Sq Δ₀ c2 c4 : ℝ)
    (hv2 : 0 < v2Sq) (hc2 : 0 < c2) (hc24 : c2 < c4) (hc4 : c4 < Δ₀) :
    collectiveSchurShift v2Sq Δ₀ c2 < 0 ∧
    v2Sq / Δ₀ < -collectiveSchurShift v2Sq Δ₀ c2 ∧
    collectiveSchurShift (6 * v2Sq) Δ₀ c4 < 0 ∧
    -collectiveSchurShift (6 * v2Sq) Δ₀ c4 =
      6 * ((Δ₀ - c2) / (Δ₀ - c4)) * (-collectiveSchurShift v2Sq Δ₀ c2) ∧
    6 * (-collectiveSchurShift v2Sq Δ₀ c2) < -collectiveSchurShift (6 * v2Sq) Δ₀ c4 :=
  pauli_collective_schur_superradiance (F := ℝ) v2Sq Δ₀ c2 c4 hv2 hc2 hc24 hc4

end CollectivePauliSuperradiance

end QOU.Nuclear.TwelveQuarkWignerPauliBinding
