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

import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Perm

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

end QOU.Mathlib.PermutationEnumeration
