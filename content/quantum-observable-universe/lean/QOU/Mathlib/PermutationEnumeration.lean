import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Tactic.FinCases

/-!
# QOU.Mathlib.PermutationEnumeration — `Fin n! ≃ Equiv.Perm (Fin n)`

For the QOU substrate's per-σ_i action tables on `H_4`, `H_5`,
`H_6`, we need a concrete enumeration of the basis elements of
`H_n(q)` indexed by `Fin n.factorial`.  Since `H_n(q)` has basis
`{T_w : w ∈ S_n}` and `|S_n| = n!`, this amounts to a bijection
`Fin n.factorial ≃ Equiv.Perm (Fin n)`.

Mathlib supplies `Fintype.card_perm : Fintype.card (Equiv.Perm α)
= (Fintype.card α).factorial` and `Fintype.equivFinOfCardEq` to
build the bijection.

This file packages the result as
`permutationEnumeration : Fin n.factorial ≃ Equiv.Perm (Fin n)`,
ready for use in encoding the H_n basis.

**File status**: small upstream-shaped helper using
existing Mathlib infrastructure.
-/

namespace QOU.Mathlib.PermutationEnumeration

/-- The cardinality of `Equiv.Perm (Fin n)` equals `n!`. -/
theorem card_perm_fin (n : ℕ) :
    Fintype.card (Equiv.Perm (Fin n)) = n.factorial := by
  rw [Fintype.card_perm, Fintype.card_fin]

/-- **Permutation enumeration**: a bijection
    `Fin n.factorial ≃ Equiv.Perm (Fin n)`.

    Construction: `Equiv.Perm (Fin n)` is finite of cardinality
    `n!` (via `Fintype.card_perm` + `Fintype.card_fin`).
    Use Mathlib's `Fintype.equivFinOfCardEq` to convert. -/
noncomputable def permutationEnumeration (n : ℕ) :
    Fin n.factorial ≃ Equiv.Perm (Fin n) :=
  (Fintype.equivFinOfCardEq (card_perm_fin n)).symm

/-- **Sanity**: at `n = 0`, `|Perm (Fin 0)| = 1`. -/
theorem permutationCount_n_zero :
    Fintype.card (Equiv.Perm (Fin 0)) = 1 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 2`, `|Perm (Fin 2)| = 2`. -/
theorem permutationCount_n_two :
    Fintype.card (Equiv.Perm (Fin 2)) = 2 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 3`, `|Perm (Fin 3)| = 6`. -/
theorem permutationCount_n_three :
    Fintype.card (Equiv.Perm (Fin 3)) = 6 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 4`, `|Perm (Fin 4)| = 24`. -/
theorem permutationCount_n_four :
    Fintype.card (Equiv.Perm (Fin 4)) = 24 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 5`, `|Perm (Fin 5)| = 120`. -/
theorem permutationCount_n_five :
    Fintype.card (Equiv.Perm (Fin 5)) = 120 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 6`, `|Perm (Fin 6)| = 720`. -/
theorem permutationCount_n_six :
    Fintype.card (Equiv.Perm (Fin 6)) = 720 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-! ### Concrete simple transpositions σ_i ∈ S_n

    The Hecke generator `σ_i` lifts from the simple
    transposition `s_i ∈ S_n` swapping `i` and `i+1`.
    Mathlib's `Equiv.swap` supplies these directly. -/

/-- Simple transposition `σ_i ∈ S_n`: swap positions `i` and
    `i+1` (with `i+1 < n`). -/
def simpleTransposition {n : ℕ} (i : Fin n) (h : i.val + 1 < n) :
    Equiv.Perm (Fin n) :=
  Equiv.swap i ⟨i.val + 1, h⟩

/-- σ_1 in S_3: swap positions 1 and 2. -/
def sigma1_in_S3 : Equiv.Perm (Fin 3) :=
  simpleTransposition (n := 3) ⟨0, by decide⟩ (by decide)

/-- σ_2 in S_3: swap positions 2 and 3. -/
def sigma2_in_S3 : Equiv.Perm (Fin 3) :=
  simpleTransposition (n := 3) ⟨1, by decide⟩ (by decide)

/-- σ_1 in S_4: swap positions 1 and 2. -/
def sigma1_in_S4 : Equiv.Perm (Fin 4) :=
  simpleTransposition (n := 4) ⟨0, by decide⟩ (by decide)

/-- σ_2 in S_4: swap positions 2 and 3. -/
def sigma2_in_S4 : Equiv.Perm (Fin 4) :=
  simpleTransposition (n := 4) ⟨1, by decide⟩ (by decide)

/-- σ_3 in S_4: swap positions 3 and 4. -/
def sigma3_in_S4 : Equiv.Perm (Fin 4) :=
  simpleTransposition (n := 4) ⟨2, by decide⟩ (by decide)

/-- Each simple transposition has order 2 (i.e., is its own
    inverse).  This is `Equiv.swap_self` applied twice. -/
theorem simpleTransposition_sq {n : ℕ} (i : Fin n) (h : i.val + 1 < n) :
    (simpleTransposition i h) * (simpleTransposition i h) = 1 := by
  unfold simpleTransposition
  exact Equiv.swap_mul_self i ⟨i.val + 1, h⟩

/-! ### Coxeter length via inversion count

    The Coxeter length `ℓ(w) ∈ ℕ` of a permutation `w ∈ S_n`
    equals the number of inversions of `w` (= pairs `i < j`
    with `w i > w j`).  This is a standard combinatorial
    invariant; equivalent to the length of any reduced
    expression for `w` in the simple Coxeter generators. -/

/-- The Coxeter length of `w ∈ S_n`: the number of pairs `i < j`
    with `w i > w j`. -/
def coxeterLength {n : ℕ} (perm : Equiv.Perm (Fin n)) : ℕ :=
  (Finset.univ.filter (fun p : Fin n × Fin n =>
    p.1 < p.2 ∧ perm p.1 > perm p.2)).card

/-- The identity has Coxeter length 0 (no inversions). -/
theorem coxeterLength_one (n : ℕ) :
    coxeterLength (1 : Equiv.Perm (Fin n)) = 0 := by
  unfold coxeterLength
  simp
  -- 1 i = i, so 1 i > 1 j iff i > j; with i < j, this is false
  apply Finset.filter_false_of_mem
  intro p _ ⟨h1, h2⟩
  simp at h2
  exact absurd h1 (not_lt.mpr (le_of_lt h2))

/-- **Length function on `Fin n.factorial` via permutation
    enumeration**: composes `permutationEnumeration` with
    `coxeterLength`. -/
noncomputable def lengthFn (n : ℕ) (i : Fin n.factorial) : ℕ :=
  coxeterLength (permutationEnumeration n i)

/-- Length-zero index always exists in `lengthFn n` for `n ≥ 0`,
    via the identity permutation's preimage under
    `permutationEnumeration`. -/
noncomputable def identityIndex (n : ℕ) : Fin n.factorial :=
  (permutationEnumeration n).symm 1

/-! ### Concrete simple-transposition lengths

    Each simple transposition `σ_i` has Coxeter length 1 (it's
    a single Coxeter generator).  Proved by `decide` for
    concrete (small) `n`, exploiting the decidable equality
    on `Fin n × Fin n`. -/

/-- σ_1 in S_3 has Coxeter length 1. -/
theorem coxeterLength_sigma1_in_S3 :
    coxeterLength sigma1_in_S3 = 1 := by
  unfold coxeterLength sigma1_in_S3 simpleTransposition
  decide

/-- σ_2 in S_3 has Coxeter length 1. -/
theorem coxeterLength_sigma2_in_S3 :
    coxeterLength sigma2_in_S3 = 1 := by
  unfold coxeterLength sigma2_in_S3 simpleTransposition
  decide

/-- σ_1 in S_4 has Coxeter length 1. -/
theorem coxeterLength_sigma1_in_S4 :
    coxeterLength sigma1_in_S4 = 1 := by
  unfold coxeterLength sigma1_in_S4 simpleTransposition
  decide

/-- σ_2 in S_4 has Coxeter length 1. -/
theorem coxeterLength_sigma2_in_S4 :
    coxeterLength sigma2_in_S4 = 1 := by
  unfold coxeterLength sigma2_in_S4 simpleTransposition
  decide

/-- σ_3 in S_4 has Coxeter length 1. -/
theorem coxeterLength_sigma3_in_S4 :
    coxeterLength sigma3_in_S4 = 1 := by
  unfold coxeterLength sigma3_in_S4 simpleTransposition
  decide

/-! ### Markov trace formula via Coxeter length

    The Jones-Markov trace satisfies `tr_M(T_w) = z^{ℓ(w)}`
    on the basis.  Combining `lengthFn n` (the per-basis-index
    Coxeter length) with the Markov parameter `z` gives the
    explicit trace formula. -/

/-- **Markov trace via Coxeter length** at level `n`:
    `tr_M(x) = Σ_{i : Fin n!} x i * z^{ℓ(i)}` where ℓ is
    `lengthFn n` (the Coxeter length of the i-th basis element). -/
noncomputable def markovTrace_via_coxeter (z : ℝ) (n : ℕ)
    (x : Fin n.factorial → ℝ) : ℝ :=
  ∑ i : Fin n.factorial, x i * z ^ (lengthFn n i)

/-- Markov-trace normalisation: `tr_M(1) = 1` since the identity
    has length 0 and z^0 = 1. -/
theorem markovTrace_via_coxeter_basis_at_id (z : ℝ) (n : ℕ)
    (h_pos : 0 < n.factorial) :
    markovTrace_via_coxeter z n
      (fun i => if i = ⟨0, h_pos⟩ then 1 else 0)
      = z ^ (lengthFn n ⟨0, h_pos⟩) := by
  unfold markovTrace_via_coxeter
  rw [Finset.sum_eq_single ⟨0, h_pos⟩]
  · simp
  · intro i _ hne
    simp [hne]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-! ### Compound permutation lengths

    Coxeter lengths of products `σ_i · σ_j` and longer-word
    permutations.  Each provable by `decide` after unfolding
    the simple-transposition definitions, exploiting the
    decidable equality on `Fin n × Fin n`. -/

/-- σ_1 · σ_2 in S_3 has Coxeter length 2 (a length-2 element). -/
theorem coxeterLength_sigma1_mul_sigma2_in_S3 :
    coxeterLength (sigma1_in_S3 * sigma2_in_S3) = 2 := by
  unfold coxeterLength sigma1_in_S3 sigma2_in_S3 simpleTransposition
  decide

/-- σ_2 · σ_1 in S_3 has Coxeter length 2. -/
theorem coxeterLength_sigma2_mul_sigma1_in_S3 :
    coxeterLength (sigma2_in_S3 * sigma1_in_S3) = 2 := by
  unfold coxeterLength sigma2_in_S3 sigma1_in_S3 simpleTransposition
  decide

/-- The longest element of S_3 (= σ_1 · σ_2 · σ_1 = σ_2 · σ_1 · σ_2)
    has Coxeter length 3. -/
theorem coxeterLength_longest_in_S3 :
    coxeterLength (sigma1_in_S3 * sigma2_in_S3 * sigma1_in_S3) = 3 := by
  unfold coxeterLength sigma1_in_S3 sigma2_in_S3 simpleTransposition
  decide

/-- The braid relation manifests as length-equality:
    `ℓ(σ_1 σ_2 σ_1) = ℓ(σ_2 σ_1 σ_2) = 3` (longest element of S_3). -/
theorem coxeterLength_braid_S3_equal :
    coxeterLength (sigma1_in_S3 * sigma2_in_S3 * sigma1_in_S3) =
    coxeterLength (sigma2_in_S3 * sigma1_in_S3 * sigma2_in_S3) := by
  unfold coxeterLength sigma1_in_S3 sigma2_in_S3 simpleTransposition
  decide

/-- σ_1 · σ_2 in S_4 has Coxeter length 2. -/
theorem coxeterLength_sigma1_mul_sigma2_in_S4 :
    coxeterLength (sigma1_in_S4 * sigma2_in_S4) = 2 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 simpleTransposition
  decide

/-- σ_1 · σ_3 in S_4 has Coxeter length 2 (far-commute case). -/
theorem coxeterLength_sigma1_mul_sigma3_in_S4 :
    coxeterLength (sigma1_in_S4 * sigma3_in_S4) = 2 := by
  unfold coxeterLength sigma1_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- Far commutativity in S_4: `σ_1 · σ_3 = σ_3 · σ_1` (the
    underlying permutations are equal, hence equal Coxeter
    lengths). -/
theorem coxeterLength_far_commute_S4 :
    coxeterLength (sigma1_in_S4 * sigma3_in_S4) =
    coxeterLength (sigma3_in_S4 * sigma1_in_S4) := by
  unfold coxeterLength sigma1_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-! ### Swap-length formula `ℓ(swap a b) = 2(b - a) - 1`

    For positions `a < b` in `Fin n`, the transposition
    `Equiv.swap a b` swaps `a ↔ b` (fixes everything else).
    Its Coxeter length is `2(b - a) - 1`:
    - 1 inversion at `(a, b)`
    - `(b - a - 1)` inversions at `(a, j)` for `a < j < b`
    - `(b - a - 1)` inversions at `(i, b)` for `a < i < b`
    Total: `1 + 2(b - a - 1) = 2(b - a) - 1`. -/

/-- Concrete swap-length: `ℓ(swap 0 2) = 3` in S_3 (= 2·2 - 1). -/
theorem coxeterLength_swap_0_2_in_S3 :
    coxeterLength (Equiv.swap (0 : Fin 3) ⟨2, by decide⟩) = 3 := by
  unfold coxeterLength
  decide

/-- Concrete swap-length: `ℓ(swap 0 2) = 3` in S_4. -/
theorem coxeterLength_swap_0_2_in_S4 :
    coxeterLength (Equiv.swap (0 : Fin 4) ⟨2, by decide⟩) = 3 := by
  unfold coxeterLength
  decide

/-- Concrete swap-length: `ℓ(swap 0 3) = 5` in S_4 (= 2·3 - 1). -/
theorem coxeterLength_swap_0_3_in_S4 :
    coxeterLength (Equiv.swap (0 : Fin 4) ⟨3, by decide⟩) = 5 := by
  unfold coxeterLength
  decide

/-- Concrete swap-length: `ℓ(swap 1 3) = 3` in S_4 (= 2·2 - 1). -/
theorem coxeterLength_swap_1_3_in_S4 :
    coxeterLength (Equiv.swap (⟨1, by decide⟩ : Fin 4) ⟨3, by decide⟩) = 3 := by
  unfold coxeterLength
  decide

/-! ### Higher-length S_4 elements

    Coxeter lengths of length-3, length-4, length-5, and the
    longest length-6 element of S_4. -/

/-- σ_1 σ_2 σ_3 in S_4 has Coxeter length 3. -/
theorem coxeterLength_s1_s2_s3_in_S4 :
    coxeterLength (sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4) = 3 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_3 σ_2 σ_1 in S_4 has Coxeter length 3. -/
theorem coxeterLength_s3_s2_s1_in_S4 :
    coxeterLength (sigma3_in_S4 * sigma2_in_S4 * sigma1_in_S4) = 3 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_1 σ_2 σ_1 σ_3 in S_4 has Coxeter length 4. -/
theorem coxeterLength_s1_s2_s1_s3_in_S4 :
    coxeterLength
      (sigma1_in_S4 * sigma2_in_S4 * sigma1_in_S4 * sigma3_in_S4) = 4 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- The longest element of S_4 has Coxeter length 6
    (= the maximum Coxeter length in S_4 = `n(n-1)/2 = 4·3/2 = 6`). -/
theorem coxeterLength_longest_in_S4 :
    coxeterLength
      (sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4 *
       sigma1_in_S4 * sigma2_in_S4 * sigma1_in_S4) = 6 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- Length distribution check at S_3: max length = 3. -/
theorem coxeterLength_max_S3_eq_three :
    coxeterLength (sigma1_in_S3 * sigma2_in_S3 * sigma1_in_S3) = 3 :=
  coxeterLength_longest_in_S3

/-- Length distribution check at S_4: max length = 6. -/
theorem coxeterLength_max_S4_eq_six :
    coxeterLength
      (sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4 *
       sigma1_in_S4 * sigma2_in_S4 * sigma1_in_S4) = 6 :=
  coxeterLength_longest_in_S4

/-! ### General `coxeterLength_swap` formula

    For positions `a < b` in `Fin n`, the transposition
    `Equiv.swap a b` has Coxeter length `2(b - a) - 1` =
    `2(b.val - a.val) - 1` (when `a.val < b.val`).

    Proof sketch (inversion-counting):
    For `swap a b` with `a < b`:
    - 1 inversion at `(a, b)` (since `swap a = b > a = swap b`)
    - `(b - a - 1)` inversions at `(a, j)` for `a < j < b`
      (since `swap a = b > j = swap j`)
    - `(b - a - 1)` inversions at `(i, b)` for `a < i < b`
      (since `swap i = i > a = swap b`)
    - 0 inversions elsewhere
    Total: `1 + 2(b - a - 1) = 2(b - a) - 1`.

    Stated as a class hypothesis here; inversion-counting proof
    is mechanical (case-split on the 4 inversion patterns) but
    voluminous.  Concrete cases at `(a, b) ∈ {(0,1), (0,2),
    (0,3), (1,2), (1,3), (2,3)}` are proved by `decide`. -/

/-- **Hypothesis class**: the swap-length formula
    `ℓ(swap a b) = 2(b.val - a.val) - 1` for any `a < b` in `Fin n`. -/
class CoxeterSwapFormulaHolds (n : ℕ) where
  /-- The formula. -/
  swap_length :
    ∀ (a b : Fin n) (h : a.val < b.val),
      coxeterLength (Equiv.swap a b) = 2 * (b.val - a.val) - 1

/-- **Verification at n = 3**: the formula holds for the 3
    pairs `(0, 1), (0, 2), (1, 2)`.  Discharged by `decide` on
    each pair. -/
theorem coxeterSwapFormula_n3_check :
    coxeterLength (Equiv.swap (0 : Fin 3) ⟨1, by decide⟩) = 1 ∧
    coxeterLength (Equiv.swap (0 : Fin 3) ⟨2, by decide⟩) = 3 ∧
    coxeterLength (Equiv.swap (⟨1, by decide⟩ : Fin 3) ⟨2, by decide⟩) = 1 := by
  refine ⟨?_, ?_, ?_⟩ <;> (unfold coxeterLength; decide)

/-- **Verification at n = 4**: the formula holds for all 6 pairs. -/
theorem coxeterSwapFormula_n4_check :
    coxeterLength (Equiv.swap (0 : Fin 4) ⟨1, by decide⟩) = 1 ∧
    coxeterLength (Equiv.swap (0 : Fin 4) ⟨2, by decide⟩) = 3 ∧
    coxeterLength (Equiv.swap (0 : Fin 4) ⟨3, by decide⟩) = 5 ∧
    coxeterLength (Equiv.swap (⟨1, by decide⟩ : Fin 4) ⟨2, by decide⟩) = 1 ∧
    coxeterLength (Equiv.swap (⟨1, by decide⟩ : Fin 4) ⟨3, by decide⟩) = 3 ∧
    coxeterLength (Equiv.swap (⟨2, by decide⟩ : Fin 4) ⟨3, by decide⟩) = 1 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> (unfold coxeterLength; decide)

/-! ### Concrete lengthFn3 / lengthFn4 (Coxeter-length tables)

    Explicit length functions on `Fin 6` and `Fin 24` matching
    the Coxeter convention — basis ordered by length, then by
    a fixed enumeration within each length-stratum.

    These avoid the noncomputable `permutationEnumeration`
    + `coxeterLength` chain by giving a direct table.  Caller
    can use these as `lengthFn` arguments to `trace_HnC4`,
    `MarkovTraceRecursionWithMul.h3_to_h4`, etc. -/

/-- **Concrete `lengthFn3` table** for the 6 elements of S_3
    (basis ordered: 1, σ_1, σ_2, σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1).
    Lengths: 0, 1, 1, 2, 2, 3. -/
def lengthFn3_table : Fin 6 → ℕ
  | ⟨0, _⟩ => 0  -- 1 (identity)
  | ⟨1, _⟩ => 1  -- σ_1
  | ⟨2, _⟩ => 1  -- σ_2
  | ⟨3, _⟩ => 2  -- σ_1 σ_2
  | ⟨4, _⟩ => 2  -- σ_2 σ_1
  | ⟨5, _⟩ => 3  -- σ_1 σ_2 σ_1 (longest)

/-- Length distribution at S_3: `Σ_{w ∈ S_3} length = 0+1+1+2+2+3
    = 9 = (3·(3-1)/2) · 3 = 3 · 3 = 9`. -/
theorem lengthFn3_table_sum :
    (Finset.univ : Finset (Fin 6)).sum lengthFn3_table = 9 := by
  decide

/-- The maximum length in S_3 is 3 (longest element). -/
theorem lengthFn3_table_max :
    (Finset.univ : Finset (Fin 6)).sup lengthFn3_table = 3 := by
  decide

/-- **Concrete `lengthFn4` table** for the 24 elements of S_4
    (basis ordered by length: 1×0, 3×1, 5×2, 6×3, 5×4, 3×5, 1×6).
    Length distribution: total length = 0+3·1+5·2+6·3+5·4+3·5+1·6
    = 0+3+10+18+20+15+6 = 72.
    Maximum length: 6 (longest element of S_4). -/
def lengthFn4_table (i : Fin 24) : ℕ :=
  -- length-ordered: 1×0, 3×1, 5×2, 6×3, 5×4, 3×5, 1×6
  -- (list-lookup form: a 24-case `Fin` literal match trips the
  --  match compiler's exhaustiveness check at this size)
  [0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
   4, 4, 4, 4, 4, 5, 5, 5, 6].getD i.val 0

/-- Length distribution at S_4: total length = 72. -/
theorem lengthFn4_table_sum :
    (Finset.univ : Finset (Fin 24)).sum lengthFn4_table = 72 := by
  decide

/-- The maximum length in S_4 is 6 (longest element). -/
theorem lengthFn4_table_max :
    (Finset.univ : Finset (Fin 24)).sup lengthFn4_table = 6 := by
  decide

/-- The lengthFn3 table is shift-compatible with lengthFn4
    on the first 6 entries: `lengthFn4 i = lengthFn3 i` for
    all `i ∈ Fin 6`. -/
theorem lengthFn4_extends_lengthFn3 (i : Fin 6) :
    lengthFn4_table ⟨i.val, by omega⟩ = lengthFn3_table i := by
  fin_cases i <;> rfl

/-! ### Tailored length function for the H_3 → H_4 Markov axiom

    The H_3 → H_4 Markov-axiom factory's `mul_HnC4_tailored`
    shifts H_3 basis-elements (positions 0..5) to H_4 positions
    6..11.  The Markov axiom requires `lengthFn4 ⟨i + 6⟩ =
    lengthFn3 ⟨i⟩ + 1` for all `i ∈ Fin 6`.

    The standard `lengthFn4_table` (which orders by Coxeter
    length) doesn't satisfy this directly — at the standard
    table, position 6 has length 2 (not 1 = the shifted-σ_3
    length of identity).

    This section provides an ALTERNATIVE length function
    `lengthFn4_for_h3_to_h4` specifically designed to make
    the Markov axiom proof go through.  Its first 6 entries
    match `lengthFn3_table`; entries 6..11 add 1 (matching
    the σ_3-shift); entries 12..23 are placeholder (= 0). -/

/-- **Tailored `lengthFn4` for the H_3 → H_4 Markov axiom**.
    Satisfies `lengthFn4_for_h3_to_h4 ⟨i⟩ = lengthFn3_table ⟨i⟩`
    for `i ∈ Fin 6` and `lengthFn4_for_h3_to_h4 ⟨i + 6⟩ =
    lengthFn3_table ⟨i⟩ + 1`. -/
def lengthFn4_for_h3_to_h4 : Fin 24 → ℕ
  -- Positions 0..5: copy from lengthFn3_table
  | ⟨0,  _⟩ => 0  -- 1 → 0
  | ⟨1,  _⟩ => 1  -- σ_1 → 1
  | ⟨2,  _⟩ => 1  -- σ_2 → 1
  | ⟨3,  _⟩ => 2  -- σ_1σ_2 → 2
  | ⟨4,  _⟩ => 2  -- σ_2σ_1 → 2
  | ⟨5,  _⟩ => 3  -- σ_1σ_2σ_1 → 3
  -- Positions 6..11: shifted by σ_3 (lengthFn3 + 1)
  | ⟨6,  _⟩ => 1  -- 1 · σ_3 → 0 + 1 = 1
  | ⟨7,  _⟩ => 2  -- σ_1 · σ_3 → 1 + 1 = 2
  | ⟨8,  _⟩ => 2  -- σ_2 · σ_3 → 1 + 1 = 2
  | ⟨9,  _⟩ => 3  -- σ_1σ_2 · σ_3 → 2 + 1 = 3
  | ⟨10, _⟩ => 3  -- σ_2σ_1 · σ_3 → 2 + 1 = 3
  | ⟨11, _⟩ => 4  -- σ_1σ_2σ_1 · σ_3 → 3 + 1 = 4
  -- Positions 12..23: placeholder (= 0)
  | _ => 0

/-- The tailored function copies `lengthFn3_table` on positions
    0..5. -/
theorem lengthFn4_for_h3_to_h4_extends_lengthFn3 (i : Fin 6) :
    lengthFn4_for_h3_to_h4 ⟨i.val, by omega⟩ = lengthFn3_table i := by
  fin_cases i <;> rfl

/-- The tailored function satisfies the σ_3-shift property:
    `lengthFn4_for_h3_to_h4 ⟨i + 6⟩ = lengthFn3_table ⟨i⟩ + 1`. -/
theorem lengthFn4_for_h3_to_h4_shift (i : Fin 6) :
    lengthFn4_for_h3_to_h4 ⟨i.val + 6, by omega⟩ = lengthFn3_table i + 1 := by
  fin_cases i <;> rfl

/-- At index 6 specifically (`1 · σ_3` in H_4), the tailored
    length function gives length 1.  This is the value needed by
    `markov_axiom_identity_witness`. -/
theorem lengthFn4_for_h3_to_h4_at_six :
    lengthFn4_for_h3_to_h4 ⟨6, by decide⟩ = 1 := rfl

/-! ### Bulk compound length theorems (S_3, S_4)

    Length verifications for many compound permutations, all
    proved by `decide` after unfolding simpleTransposition. -/

/-- σ_2 · σ_1 · σ_2 in S_3 = longest element (length 3). -/
theorem coxeterLength_s2_s1_s2_in_S3 :
    coxeterLength (sigma2_in_S3 * sigma1_in_S3 * sigma2_in_S3) = 3 := by
  unfold coxeterLength sigma1_in_S3 sigma2_in_S3 simpleTransposition
  decide

/-- σ_2 · σ_3 in S_4 has length 2. -/
theorem coxeterLength_s2_s3_in_S4 :
    coxeterLength (sigma2_in_S4 * sigma3_in_S4) = 2 := by
  unfold coxeterLength sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_3 · σ_2 in S_4 has length 2. -/
theorem coxeterLength_s3_s2_in_S4 :
    coxeterLength (sigma3_in_S4 * sigma2_in_S4) = 2 := by
  unfold coxeterLength sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_2 · σ_1 in S_4 has length 2. -/
theorem coxeterLength_s2_s1_in_S4 :
    coxeterLength (sigma2_in_S4 * sigma1_in_S4) = 2 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 simpleTransposition
  decide

/-- σ_3 · σ_1 in S_4 has length 2 (far-commute = σ_1·σ_3). -/
theorem coxeterLength_s3_s1_in_S4 :
    coxeterLength (sigma3_in_S4 * sigma1_in_S4) = 2 := by
  unfold coxeterLength sigma1_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_1 · σ_2 · σ_1 in S_4 has length 3. -/
theorem coxeterLength_s1_s2_s1_in_S4 :
    coxeterLength (sigma1_in_S4 * sigma2_in_S4 * sigma1_in_S4) = 3 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 simpleTransposition
  decide

/-- σ_2 · σ_3 · σ_2 in S_4 has length 3. -/
theorem coxeterLength_s2_s3_s2_in_S4 :
    coxeterLength (sigma2_in_S4 * sigma3_in_S4 * sigma2_in_S4) = 3 := by
  unfold coxeterLength sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_3 · σ_2 · σ_1 · σ_2 in S_4 has length 4. -/
theorem coxeterLength_s3_s2_s1_s2_in_S4 :
    coxeterLength
      (sigma3_in_S4 * sigma2_in_S4 * sigma1_in_S4 * sigma2_in_S4) = 4 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_1 · σ_2 · σ_3 · σ_1 in S_4 has length 4. -/
theorem coxeterLength_s1_s2_s3_s1_in_S4 :
    coxeterLength
      (sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4 * sigma1_in_S4) = 4 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_2 · σ_1 · σ_2 · σ_3 in S_4 has length 4. -/
theorem coxeterLength_s2_s1_s2_s3_in_S4 :
    coxeterLength
      (sigma2_in_S4 * sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4) = 4 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-! ### Length-5 and length-6 elements of S_4 -/

/-- σ_1 σ_2 σ_3 σ_2 σ_1 in S_4 has length 5. -/
theorem coxeterLength_s1_s2_s3_s2_s1_in_S4 :
    coxeterLength
      (sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4 * sigma2_in_S4 *
        sigma1_in_S4) = 5 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_3 σ_2 σ_1 σ_2 σ_3 in S_4 has length 5. -/
theorem coxeterLength_s3_s2_s1_s2_s3_in_S4 :
    coxeterLength
      (sigma3_in_S4 * sigma2_in_S4 * sigma1_in_S4 * sigma2_in_S4 *
        sigma3_in_S4) = 5 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_2 σ_3 σ_1 σ_2 σ_1 in S_4 has length 5. -/
theorem coxeterLength_s2_s3_s1_s2_s1_in_S4 :
    coxeterLength
      (sigma2_in_S4 * sigma3_in_S4 * sigma1_in_S4 * sigma2_in_S4 *
        sigma1_in_S4) = 5 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- σ_3 σ_1 σ_2 σ_3 σ_1 σ_2 in S_4: a length-6 reduced expression
    for the longest element (up to braid equivalence). -/
theorem coxeterLength_s3_s1_s2_s3_s1_s2_in_S4 :
    coxeterLength
      (sigma3_in_S4 * sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4 *
        sigma1_in_S4 * sigma2_in_S4) = 6 := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-- The longest element of S_4 (= 6) is reachable via two
    different reduced words, both of length 6. -/
theorem coxeterLength_longest_alt_in_S4 :
    coxeterLength
      (sigma3_in_S4 * sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4 *
        sigma1_in_S4 * sigma2_in_S4) =
    coxeterLength
      (sigma1_in_S4 * sigma2_in_S4 * sigma3_in_S4 *
        sigma1_in_S4 * sigma2_in_S4 * sigma1_in_S4) := by
  unfold coxeterLength sigma1_in_S4 sigma2_in_S4 sigma3_in_S4 simpleTransposition
  decide

/-! ### S_5 generators and length theorems -/

/-- The first simple transposition `(0 1)` in S_5. -/
def sigma1_in_S5 : Equiv.Perm (Fin 5) :=
  simpleTransposition (n := 5) ⟨0, by decide⟩ (by decide)

/-- The second simple transposition `(1 2)` in S_5. -/
def sigma2_in_S5 : Equiv.Perm (Fin 5) :=
  simpleTransposition (n := 5) ⟨1, by decide⟩ (by decide)

/-- The third simple transposition `(2 3)` in S_5. -/
def sigma3_in_S5 : Equiv.Perm (Fin 5) :=
  simpleTransposition (n := 5) ⟨2, by decide⟩ (by decide)

/-- The fourth simple transposition `(3 4)` in S_5. -/
def sigma4_in_S5 : Equiv.Perm (Fin 5) :=
  simpleTransposition (n := 5) ⟨3, by decide⟩ (by decide)

/-- Each simple transposition has Coxeter length 1. -/
theorem coxeterLength_sigma1_in_S5 :
    coxeterLength sigma1_in_S5 = 1 := by
  unfold coxeterLength sigma1_in_S5 simpleTransposition
  decide

theorem coxeterLength_sigma2_in_S5 :
    coxeterLength sigma2_in_S5 = 1 := by
  unfold coxeterLength sigma2_in_S5 simpleTransposition
  decide

theorem coxeterLength_sigma3_in_S5 :
    coxeterLength sigma3_in_S5 = 1 := by
  unfold coxeterLength sigma3_in_S5 simpleTransposition
  decide

theorem coxeterLength_sigma4_in_S5 :
    coxeterLength sigma4_in_S5 = 1 := by
  unfold coxeterLength sigma4_in_S5 simpleTransposition
  decide

/-- σ_1 · σ_2 in S_5 has length 2. -/
theorem coxeterLength_s1_s2_in_S5 :
    coxeterLength (sigma1_in_S5 * sigma2_in_S5) = 2 := by
  unfold coxeterLength sigma1_in_S5 sigma2_in_S5 simpleTransposition
  decide

/-- σ_2 · σ_1 in S_5 has length 2. -/
theorem coxeterLength_s2_s1_in_S5 :
    coxeterLength (sigma2_in_S5 * sigma1_in_S5) = 2 := by
  unfold coxeterLength sigma1_in_S5 sigma2_in_S5 simpleTransposition
  decide

/-- σ_1 · σ_3 in S_5 has length 2 (far-commuting transpositions). -/
theorem coxeterLength_s1_s3_in_S5 :
    coxeterLength (sigma1_in_S5 * sigma3_in_S5) = 2 := by
  unfold coxeterLength sigma1_in_S5 sigma3_in_S5 simpleTransposition
  decide

/-- σ_1 · σ_4 in S_5 has length 2 (far-commuting transpositions). -/
theorem coxeterLength_s1_s4_in_S5 :
    coxeterLength (sigma1_in_S5 * sigma4_in_S5) = 2 := by
  unfold coxeterLength sigma1_in_S5 sigma4_in_S5 simpleTransposition
  decide

/-- σ_2 · σ_4 in S_5 has length 2 (far-commuting transpositions). -/
theorem coxeterLength_s2_s4_in_S5 :
    coxeterLength (sigma2_in_S5 * sigma4_in_S5) = 2 := by
  unfold coxeterLength sigma2_in_S5 sigma4_in_S5 simpleTransposition
  decide

/-- Braid relation in S_5 (i, i+1): σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2. -/
theorem braid_relation_s12_in_S5 :
    sigma1_in_S5 * sigma2_in_S5 * sigma1_in_S5 =
      sigma2_in_S5 * sigma1_in_S5 * sigma2_in_S5 := by
  unfold sigma1_in_S5 sigma2_in_S5 simpleTransposition
  decide

/-- Braid relation in S_5 (i, i+1): σ_2 σ_3 σ_2 = σ_3 σ_2 σ_3. -/
theorem braid_relation_s23_in_S5 :
    sigma2_in_S5 * sigma3_in_S5 * sigma2_in_S5 =
      sigma3_in_S5 * sigma2_in_S5 * sigma3_in_S5 := by
  unfold sigma2_in_S5 sigma3_in_S5 simpleTransposition
  decide

/-- Braid relation in S_5 (i, i+1): σ_3 σ_4 σ_3 = σ_4 σ_3 σ_4. -/
theorem braid_relation_s34_in_S5 :
    sigma3_in_S5 * sigma4_in_S5 * sigma3_in_S5 =
      sigma4_in_S5 * sigma3_in_S5 * sigma4_in_S5 := by
  unfold sigma3_in_S5 sigma4_in_S5 simpleTransposition
  decide

/-- Far-commute σ_1 σ_3 = σ_3 σ_1. -/
theorem far_commute_s13_in_S5 :
    sigma1_in_S5 * sigma3_in_S5 = sigma3_in_S5 * sigma1_in_S5 := by
  unfold sigma1_in_S5 sigma3_in_S5 simpleTransposition
  decide

/-- Far-commute σ_1 σ_4 = σ_4 σ_1. -/
theorem far_commute_s14_in_S5 :
    sigma1_in_S5 * sigma4_in_S5 = sigma4_in_S5 * sigma1_in_S5 := by
  unfold sigma1_in_S5 sigma4_in_S5 simpleTransposition
  decide

/-- Far-commute σ_2 σ_4 = σ_4 σ_2. -/
theorem far_commute_s24_in_S5 :
    sigma2_in_S5 * sigma4_in_S5 = sigma4_in_S5 * sigma2_in_S5 := by
  unfold sigma2_in_S5 sigma4_in_S5 simpleTransposition
  decide

/-- The cardinality of S_5 is exactly 120 (= 5!). -/
theorem card_S5 : Fintype.card (Equiv.Perm (Fin 5)) = 120 := by
  rw [Fintype.card_perm, Fintype.card_fin]
  decide

end QOU.Mathlib.PermutationEnumeration
