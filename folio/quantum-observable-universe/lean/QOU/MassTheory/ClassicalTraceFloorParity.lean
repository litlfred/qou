/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Tactic
import QOU.MassTheory.ClassicalTraceFloor
import MathlibExt.CycleCountSwap

set_option autoImplicit false

/-!
# Interface-Multiplicity Parity & Cycle-Merge Derivation of the Classical Trace Floor

Bean `qou-zrx2` (epic `qou-v2om`). Companion to `QOU.MassTheory.ClassicalTraceFloor` and
`QOU.RiemannSurface.CycleCountSwap`.

## Mathematical Content

At `q = 1` (`h = q - q⁻¹ = 0`), every Hecke crossing letter in the `3A`-strand atomic braid
(`σ_g`, `σ_g⁻¹ = σ_g - h`, or averaged `σ_g - (h/2)·1`) collapses to the simple transposition
`Equiv.swap a b ∈ Perm D`. Consequently, an inter-nucleon interface applied with crossing
multiplicity `m : ℕ` degenerates at `q = 1` to `(swap a b) ^ m`:

1. **Transposition power parity (`swap_pow_of_even`, `swap_pow_of_odd`):**
   `(swap a b) ^ m = 1` when `Even m`, and `(swap a b) ^ m = swap a b` when `Odd m`.
2. **Permutation cycle-count step (`numCycles_mul_swap_pow_of_even`,
   `numCycles_mul_swap_pow_of_odd_not_sameCycle`):**
   Composing with an even-multiplicity interface preserves `numCycles`, whereas composing with an
   odd-multiplicity interface joining two distinct cycles merges them (`numCycles` drops by `1`
   via `QOU.RiemannSurface.CycleCountSwap.numCycles_mul_swap_of_not_sameCycle`). Inducting along a
   chain of interfaces (`DisjointInterfaceChain`) discharges follow-up (5) of `qou-zrx2`:
   `numCycles (applyInterfaceChain π L) + oddMultiplicityCount L = numCycles π`.
3. **General interface-parity classical trace floor (`classicalTraceFloorParityField`):**
   Over any `[Field K]`, with `c_free = 2A` and `c_atom = 2A - O` (`O` odd-multiplicity interfaces
   on `n = 3A` strands), the `q = 1` Schur–Weyl trace difference equals
   `c₀(A, O) = 2^(-A) · (1 - 2^(-O))`.
   - Specialising to `O = A - 1` recovers `2^(-A) - 2^(1 - 2A)` (`ClassicalTraceFloor`).
   - Over any ordered field, `c₀(A, O) = 0 ↔ O = 0` (`classicalTraceFloorParityField_eq_zero_iff`),
     establishing both that single nucleons (`A = 1`, `O = 0`) carry zero `ℏ_q⁰` floor and that
     among multi-nucleon chains the `ℏ_q⁰` floor vanishes iff every interface has even multiplicity
     (a structural diagnostic, not a parameter choice).

Base ring (§7c): generic `Fintype` permutations (`§1`), generic `[Field K]` / `[LinearOrder K]
[IsStrictOrderedRing K]` (`§2`), with `ℚ` compatibility to `ClassicalTraceFloor` and `ℝ`
archimedean specialisation (`§3`). Zero empirical literals.

-- Ref: [hoefsmit1974] Ch. 2 (seminormal matrices at q = 1 degenerate to S_n transpositions)
-- Ref: [ram1991] Thm. 4.14 (q = 1 character specialisation on Hecke algebras)
-- Ref: [leitner2026] bean qou-zrx2; computations/probes/classical_floor_is_interface_parity_probe.py
-/

namespace QOU.MassTheory

open Equiv Equiv.Perm
open QOU.RiemannSurface.CombinatorialMapEuler
open QOU.RiemannSurface.CycleCountSwap

/-! ## §1. Transposition Multiplicity Parity and Cycle-Merge Induction -/

section CycleMergeParity

/-- An even power of a transposition `swap a b` is the identity permutation. -/
theorem swap_pow_of_even {D : Type*} [DecidableEq D] (a b : D) {m : ℕ} (hm : Even m) :
    (swap a b : Perm D) ^ m = 1 := by
  rcases hm with ⟨k, rfl⟩
  rw [← two_mul, pow_mul]
  have hsq : (swap a b : Perm D) ^ 2 = 1 := by
    rw [sq, swap_mul_self]
  rw [hsq, one_pow]

/-- An odd power of a transposition `swap a b` equals `swap a b`. -/
theorem swap_pow_of_odd {D : Type*} [DecidableEq D] (a b : D) {m : ℕ} (hm : Odd m) :
    (swap a b : Perm D) ^ m = swap a b := by
  rcases hm with ⟨k, rfl⟩
  rw [pow_add, pow_one, swap_pow_of_even a b (even_two_mul k), one_mul]

/-- Right-multiplying `π` by an even-multiplicity interface `(swap a b)^m` preserves `numCycles`. -/
theorem numCycles_mul_swap_pow_of_even {D : Type*} [DecidableEq D]
    (π : Perm D) (a b : D) {m : ℕ} (hm : Even m) :
    numCycles (π * (swap a b) ^ m) = numCycles π := by
  rw [swap_pow_of_even a b hm, mul_one]

/-- Right-multiplying `π` by an odd-multiplicity interface `(swap a b)^m` whose endpoints lie in
distinct cycles of `π` merges those two cycles, decreasing `numCycles` by `1`. -/
theorem numCycles_mul_swap_pow_of_odd_not_sameCycle {D : Type*} [Fintype D] [DecidableEq D]
    (π : Perm D) {a b : D} {m : ℕ}
    (hm : Odd m) (hdisj : ¬ π.SameCycle a b) :
    numCycles (π * (swap a b) ^ m) + 1 = numCycles π := by
  rw [swap_pow_of_odd a b hm]
  exact numCycles_mul_swap_of_not_sameCycle π hdisj

/-- Sequential composition of `π` with a list of interface specifications `(a, b, m)`, where each
interface contributes `(swap a b)^m` at `q = 1`. -/
def applyInterfaceChain {D : Type*} [DecidableEq D] (π : Perm D) : List (D × D × ℕ) → Perm D
  | [] => π
  | (a, b, m) :: rest => applyInterfaceChain (π * (swap a b) ^ m) rest

/-- Number of interfaces in `L` whose crossing multiplicity `m` is odd. -/
def oddMultiplicityCount {D : Type*} : List (D × D × ℕ) → ℕ
  | [] => 0
  | (_, _, m) :: rest => (if m % 2 = 1 then 1 else 0) + oddMultiplicityCount rest

/-- Chain-merge admissibility: at every odd-multiplicity interface `(a, b, m)`, the endpoints `a`
and `b` lie in distinct cycles of the running permutation (as holds when each odd interface attaches
a fresh nucleon component along the linear chain). Even-multiplicity interfaces carry no cycle
requirement because `(swap a b)^m = 1`. -/
def DisjointInterfaceChain {D : Type*} [DecidableEq D] (π : Perm D) : List (D × D × ℕ) → Prop
  | [] => True
  | (a, b, m) :: rest =>
      (Odd m → ¬ π.SameCycle a b) ∧ DisjointInterfaceChain (π * (swap a b) ^ m) rest

/-- **Cycle-merge parity law (`qou-zrx2` follow-up 5).**
Along any `DisjointInterfaceChain`, the final cycle count plus the number of odd-multiplicity
interfaces equals the initial cycle count:
`numCycles (applyInterfaceChain π L) + oddMultiplicityCount L = numCycles π`. -/
theorem numCycles_applyInterfaceChain_add_odd {D : Type*} [Fintype D] [DecidableEq D]
    (π : Perm D) (L : List (D × D × ℕ))
    (hchain : DisjointInterfaceChain π L) :
    numCycles (applyInterfaceChain π L) + oddMultiplicityCount L = numCycles π := by
  induction L generalizing π with
  | nil =>
      simp [applyInterfaceChain, oddMultiplicityCount]
  | cons hd tl ih =>
      rcases hd with ⟨a, b, m⟩
      rcases hchain with ⟨hstep, hrest⟩
      have hrec := ih (π * (swap a b) ^ m) hrest
      simp only [applyInterfaceChain, oddMultiplicityCount]
      rcases Nat.even_or_odd m with hm | hm
      · have hmod : m % 2 ≠ 1 := by
          have := Nat.even_iff.mp hm
          omega
        rw [if_neg hmod]
        have hcyc := numCycles_mul_swap_pow_of_even π a b hm
        rw [hcyc] at hrec
        omega
      · have hmod : m % 2 = 1 := Nat.odd_iff.mp hm
        rw [if_pos hmod]
        have hcyc := numCycles_mul_swap_pow_of_odd_not_sameCycle π hm (hstep hm)
        omega

/-- **Canonical `m = 1` chain specialisation (`O = A - 1` on `c_free = 2A` cycles).**
When `1 ≤ A`, `numCycles π = 2 * A`, and all `A - 1` chain interfaces have odd multiplicity, the
bound-atom permutation has `A + 1` cycles. -/
theorem numCycles_applyInterfaceChain_canonical {D : Type*} [Fintype D] [DecidableEq D]
    (π : Perm D) (L : List (D × D × ℕ)) {A : ℕ}
    (hA : 1 ≤ A) (hfree : numCycles π = 2 * A)
    (hodd : oddMultiplicityCount L = A - 1)
    (hchain : DisjointInterfaceChain π L) :
    numCycles (applyInterfaceChain π L) = A + 1 := by
  have hsum := numCycles_applyInterfaceChain_add_odd π L hchain
  omega

end CycleMergeParity

/-! ## §2. General Interface-Parity Classical Floor `c₀(A, O) = 2^(-A) · (1 - 2^(-O))` -/

section ParityFloorField

/-- General interface-parity classical trace floor `2^(-A) * (1 - 2^(-O))` over any `[Field K]`,
where `A` is the nucleon count and `O` is the count of odd-multiplicity interfaces. -/
def classicalTraceFloorParityField {K : Type*} [Field K] (A O : ℤ) : K :=
  (2 : K) ^ (-A) * (1 - (2 : K) ^ (-O))

/-- Expanding the parity product over any `[Field K]` with `(2 : K) ≠ 0`:
`2^(-A) * (1 - 2^(-O)) = 2^(-A) - 2^(-(A + O))`. -/
theorem classicalTraceFloorParityField_expand {K : Type*} [Field K]
    (h2 : (2 : K) ≠ 0) (A O : ℤ) :
    classicalTraceFloorParityField (K := K) A O =
      (2 : K) ^ (-A) - (2 : K) ^ (-(A + O)) := by
  unfold classicalTraceFloorParityField
  rw [mul_sub, mul_one, ← zpow_add₀ h2]
  have hexp : -A + -O = -(A + O) := by omega
  rw [hexp]

/-- **Bridge to `ClassicalTraceFloor.classicalTraceFloor` over `ℚ`:**
For `c_free = 2A` and `c_atom = 2A - O` on `n = 3A` strands,
`classicalTraceFloor (2A) (2A - O) (3A) = 2^(-A) * (1 - 2^(-O))`. -/
theorem classicalTraceFloor_eq_parity (A O : ℤ) :
    classicalTraceFloor (2 * A) (2 * A - O) (3 * A) =
      classicalTraceFloorParityField (K := ℚ) A O := by
  unfold classicalTraceFloor
  rw [classicalTraceFloorParityField_expand (by norm_num : (2 : ℚ) ≠ 0)]
  congr 2 <;> omega

/-- **Canonical `m = 1` chain recovery (`O = A - 1`):**
Substituting `O = A - 1` yields `2^(-A) - 2^(1 - 2A)`. -/
theorem classicalTraceFloorParityField_canonical {K : Type*} [Field K]
    (h2 : (2 : K) ≠ 0) (A : ℤ) :
    classicalTraceFloorParityField (K := K) A (A - 1) =
      (2 : K) ^ (-A) - (2 : K) ^ (1 - 2 * A) := by
  rw [classicalTraceFloorParityField_expand h2]
  congr 2
  omega

/-- At `O = 0` (either a single nucleon `A = 1` or all-even interface multiplicities), the
classical trace floor vanishes identically. -/
@[simp]
theorem classicalTraceFloorParityField_zero_right {K : Type*} [Field K] (A : ℤ) :
    classicalTraceFloorParityField (K := K) A 0 = 0 := by
  unfold classicalTraceFloorParityField
  simp

/-- **Zero-floor characterisation over any ordered field (`§7c`):**
`c₀(A, O) = 0 ↔ O = 0`. The classical `ℏ_q⁰` floor vanishes if and only if zero inter-nucleon
interfaces have odd crossing multiplicity. -/
theorem classicalTraceFloorParityField_eq_zero_iff
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] (A O : ℤ) :
    classicalTraceFloorParityField (K := K) A O = 0 ↔ O = 0 := by
  unfold classicalTraceFloorParityField
  have hpow_pos : (0 : K) < (2 : K) ^ (-A) := zpow_pos (by norm_num : (0 : K) < 2) (-A)
  rw [mul_eq_zero, or_iff_right (ne_of_gt hpow_pos), sub_eq_zero]
  constructor
  · intro h1
    by_contra hO
    rcases lt_or_gt_of_ne hO with hlt | hgt
    · have hgt1 : (1 : K) < (2 : K) ^ (-O) :=
        one_lt_zpow₀ (by norm_num : (1 : K) < 2) (by omega : 0 < -O)
      linarith
    · have hlt1 : (2 : K) ^ (-O) < 1 :=
        zpow_lt_one_of_neg₀ (by norm_num : (1 : K) < 2) (by omega : -O < 0)
      linarith
  · rintro rfl
    simp

/-- **Strict monotonicity in the odd-interface count `O`:**
Increasing `O` strictly increases `c₀(A, O)` at fixed mass number `A`. -/
theorem classicalTraceFloorParityField_strictMono_right
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (A : ℤ) {O₁ O₂ : ℤ} (hO : O₁ < O₂) :
    classicalTraceFloorParityField (K := K) A O₁ <
      classicalTraceFloorParityField (K := K) A O₂ := by
  unfold classicalTraceFloorParityField
  have hpow_pos : (0 : K) < (2 : K) ^ (-A) := zpow_pos (by norm_num : (0 : K) < 2) (-A)
  have hzpow : (2 : K) ^ (-O₂) < (2 : K) ^ (-O₁) :=
    zpow_lt_zpow_right₀ (by norm_num : (1 : K) < 2) (by omega : -O₂ < -O₁)
  exact mul_lt_mul_of_pos_left (by linarith) hpow_pos

/-- Non-negativity and geometric upper bound `0 ≤ c₀(A, O) < 2^(-A)` whenever `0 ≤ O`. -/
theorem classicalTraceFloorParityField_bounds
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (A : ℤ) {O : ℤ} (hO : 0 ≤ O) :
    0 ≤ classicalTraceFloorParityField (K := K) A O ∧
      classicalTraceFloorParityField (K := K) A O < (2 : K) ^ (-A) := by
  unfold classicalTraceFloorParityField
  have hApos : (0 : K) < (2 : K) ^ (-A) := zpow_pos (by norm_num : (0 : K) < 2) (-A)
  have hOpos : (0 : K) < (2 : K) ^ (-O) := zpow_pos (by norm_num : (0 : K) < 2) (-O)
  have hOle1 : (2 : K) ^ (-O) ≤ 1 :=
    zpow_le_one_of_nonpos₀ (by norm_num : (1 : K) ≤ 2) (by omega : -O ≤ 0)
  refine ⟨mul_nonneg (le_of_lt hApos) (by linarith), ?_⟩
  have hlt : 1 - (2 : K) ^ (-O) < 1 := by linarith
  calc
    (2 : K) ^ (-A) * (1 - (2 : K) ^ (-O)) < (2 : K) ^ (-A) * 1 :=
      mul_lt_mul_of_pos_left hlt hApos
    _ = (2 : K) ^ (-A) := mul_one _

end ParityFloorField

/-! ## §3. Archimedean `ℝ` Specialisation (`§7c`) -/

section ArchimedeanReal

/-- Archimedean `ℝ` specialisation of `classicalTraceFloorParityField_eq_zero_iff` and
`classicalTraceFloorParityField_bounds`. -/
theorem classicalTraceFloorParity_real_zero_and_bounds (A O : ℤ) (hO : 0 ≤ O) :
    (classicalTraceFloorParityField (K := ℝ) A O = 0 ↔ O = 0) ∧
      0 ≤ classicalTraceFloorParityField (K := ℝ) A O ∧
      classicalTraceFloorParityField (K := ℝ) A O < (2 : ℝ) ^ (-A) :=
  ⟨classicalTraceFloorParityField_eq_zero_iff (K := ℝ) A O,
   classicalTraceFloorParityField_bounds (K := ℝ) A hO⟩

end ArchimedeanReal

end QOU.MassTheory
