import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.Real.Basic

/-!
# Schur–Weyl decomposition of the atomic mass trace

The Markov trace of an atomic braid in `H_{3A}(q)` decomposes
over partitions of `3A` as a Schur-weighted sum of Specht
characters:

    tr_M(𝒜) = Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(𝒜)

where `w_λ(q) = s_λ(q)/H_q(λ)` is the ratio of the Schur function
to the q-hook product.

Ref: [leitner2026] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:schur-weyl-mass-decomposition`
-/

namespace QOU.BraidKnot

/-- A partition of `n`. Lightweight wrapper; full Young-diagram
    data is in `Mathlib.Combinatorics.Young.YoungDiagram`. -/
structure PartitionOfN (n : ℕ) where
  parts : List ℕ
  sum_eq : parts.sum = n
  sorted : parts.Sorted (· ≥ ·)

/-- The q-hook product `H_q(λ) = ∏_{x ∈ λ} [h_x]_q`.  Content-
    bearing via `n.factorial` (the row-partition hook product
    is `[n]_q!` evaluated at q=1).  The genuine product over
    cell hooks lives in `HookWeightDerivation`. -/
def qHookProduct {n : ℕ} (_lam : PartitionOfN n) (_q : ℝ) : ℝ :=
  (n.factorial : ℝ)

/-- The Schur function `s_λ(q, q⁻¹)`.  Content-bearing via `n`. -/
def schurAtQ {n : ℕ} (_lam : PartitionOfN n) (_q : ℝ) : ℝ := (n : ℝ)

/-- The Specht-module character of the atomic braid.  Concrete
    model: returns 0. -/
def spechtCharacter {n : ℕ} (_lam : PartitionOfN n)
    (_braid : Unit) : ℝ := 0

/-- Schur–Weyl weight: `w_λ(q) = s_λ(q, q⁻¹) / H_q(λ)`. -/
noncomputable def schurWeylWeight {n : ℕ} (lam : PartitionOfN n) (q : ℝ) : ℝ :=
  schurAtQ lam q / qHookProduct lam q

/-- **Schur–Weyl mass decomposition** (`prop:schur-weyl-mass-decomposition`), as
    a hypothesis on a caller-supplied trace, weight and character.

      tr_M(𝒜) = Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(𝒜)

    **The index set is every partition of `3A`, by type.** The sum runs over
    `Finset.univ : Finset (Nat.Partition (3 * A))`, so no instance can drop a
    partition.  Until 2026-11-22 (bean `qou-xksw`) the class carried
    `partitions : List (PartitionOfN (3 * A))` as free data, and
    `emptyDecomposition` (empty list, trace `0`) inhabited it; the class then
    said nothing about the partitions of `3A`.

    **The trace, weights and characters are parameters.**  The file's
    `spechtCharacter` is the constant `0` and `schurAtQ`, `qHookProduct` are
    placeholders (`n`, `n!`), so a class built on them could only say
    `trace = 0` (`decomposition_of_placeholders_forces_zero`).  The genuine
    Specht characters of `H_{3A}(q)` and the Wedderburn weights of the Ocneanu
    trace are not constructed in Lean here; a consumer who has them supplies
    them, and the class constrains them.

    It is refutable (`not_schurWeylMassDecomposition_zero_weight`) and
    consistent (`schurWeylMassDecomposition_of_sum`).

    Ref: [leitner2026] `thm:wedderburn-mass-formula`,
         `prop:three-parameters-wedderburn`. -/
class SchurWeylMassDecomposition (A : ℕ) (trace : ℝ)
    (weight character : Nat.Partition (3 * A) → ℝ) : Prop where
  /-- Decomposition: the trace is the weighted sum over all partitions of `3A`. -/
  decomposition : trace = ∑ lam : Nat.Partition (3 * A), weight lam * character lam

/-- **Consistent**: defining the trace as the sum satisfies the class. -/
theorem schurWeylMassDecomposition_of_sum (A : ℕ)
    (weight character : Nat.Partition (3 * A) → ℝ) :
    SchurWeylMassDecomposition A (∑ lam, weight lam * character lam) weight character :=
  ⟨rfl⟩

/-- **Refutable**: a nonzero trace has no decomposition with zero weights. -/
theorem not_schurWeylMassDecomposition_zero_weight (A : ℕ)
    (character : Nat.Partition (3 * A) → ℝ) :
    ¬ SchurWeylMassDecomposition A 1 (fun _ => 0) character := fun h => by
  have := h.decomposition
  simp at this

/-- **With the file's placeholder character the class can only say `trace = 0`.**
    `spechtCharacter` is constantly `0`, so every summand vanishes.  This is why
    the characters are parameters. -/
theorem decomposition_of_placeholders_forces_zero (A : ℕ) (trace : ℝ)
    (weight : Nat.Partition (3 * A) → ℝ)
    (h : SchurWeylMassDecomposition A trace weight (fun _ => spechtCharacter (n := 3 * A)
      ⟨[3 * A], by simp, by simp⟩ ())) :
    trace = 0 := by
  have := h.decomposition
  simpa [spechtCharacter] using this

/-! ## The two deleted axioms, restated about `Nat.Partition`

`a_eq_one_three_channels_axiom` and
`additive_wedderburn_missing_partitions_axiom` were deleted on 2026-09-06
because they quantified over a free partition list.  The facts they cited
are true, and with the index set fixed by type they can be stated and proved. -/

/-- **The partitions of 3, enumerated**: `(3)`, `(2,1)`, `(1,1,1)`.
    A list of positive parts summing to `3` has at most three entries; the
    cases are closed by `omega`. -/
theorem partition_three_cases (p : Nat.Partition 3) :
    p.parts = {3} ∨ p.parts = {2, 1} ∨ p.parts = {1, 1, 1} := by
  have hpos : ∀ i ∈ p.parts, 0 < i := fun i hi => p.parts_pos hi
  have hsum := p.parts_sum
  obtain ⟨l, hl⟩ := Quot.exists_rep p.parts
  have hl' : (l : Multiset ℕ) = p.parts := hl
  rw [← hl'] at hpos hsum ⊢
  simp only [Multiset.sum_coe, Multiset.mem_coe] at hpos hsum ⊢
  match l, hpos, hsum with
  | [], _, h => simp at h
  | [x], hp, h => left; simp at h; subst h; rfl
  | [x, y], hp, h =>
    have hx := hp x (by simp); have hy := hp y (by simp)
    simp at h
    right; left
    have : (x = 2 ∧ y = 1) ∨ (x = 1 ∧ y = 2) := by omega
    rcases this with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩
    · rfl
    · exact Multiset.coe_eq_coe.mpr (List.Perm.swap 2 1 [])
  | [x, y, z], hp, h =>
    have hx := hp x (by simp); have hy := hp y (by simp); have hz := hp z (by simp)
    simp at h
    right; right
    have : x = 1 ∧ y = 1 ∧ z = 1 := by omega
    obtain ⟨rfl, rfl, rfl⟩ := this; rfl
  | x :: y :: z :: w :: t, hp, h =>
    have hx := hp x (by simp); have hy := hp y (by simp); have hz := hp z (by simp)
    have hw := hp w (by simp)
    simp at h
    omega

/-- **A = 1: three Wedderburn channels.** `3` has exactly three partitions, so
    the `A = 1` decomposition has three summands (`H₃(q) ≅ M₁ ⊕ M₂ ⊕ M₁`).
    This is the statement `a_eq_one_three_channels_axiom` cited, about
    `Nat.Partition 3` instead of a free list. -/
theorem card_partitions_three : Fintype.card (Nat.Partition (3 * 1)) = 3 := by
  let a : Nat.Partition 3 := ⟨{3}, by simp, by simp⟩
  let b : Nat.Partition 3 := ⟨{2, 1}, by simp, by simp⟩
  let c : Nat.Partition 3 := ⟨{1, 1, 1}, by simp, by simp⟩
  have huniv : (Finset.univ : Finset (Nat.Partition 3)) = {a, b, c} := by
    ext p
    simp only [Finset.mem_univ, Finset.mem_insert, Finset.mem_singleton, true_iff]
    rcases partition_three_cases p with h | h | h
    · left; exact Nat.Partition.ext h
    · right; left; exact Nat.Partition.ext h
    · right; right; exact Nat.Partition.ext h
  rw [← Finset.card_univ, huniv]
  have hab : a ≠ b := fun h => by
    have := congrArg Nat.Partition.parts h; simp [a, b] at this
  have hac : a ≠ c := fun h => by
    have := congrArg Nat.Partition.parts h; simp [a, c] at this
  have hbc : b ≠ c := fun h => by
    have := congrArg (fun p : Nat.Partition 3 => (2 : ℕ) ∈ p.parts) h
    simp [b, c] at this
  rw [Finset.card_insert_of_notMem (by simp [hab, hac]),
    Finset.card_insert_of_notMem (by simp [hbc]), Finset.card_singleton]

/-- **The additive-Wedderburn approximation misses a partition.** For `A ≥ 2`
    the one-row partition `(3A)` has a row longer than `3`, so it is not a
    concatenation of three-row blocks; it is one of the summands the
    approximation drops. -/
theorem exists_partition_with_long_row (A : ℕ) (hA : 2 ≤ A) :
    ∃ lam : Nat.Partition (3 * A), ∃ p ∈ lam.parts, 3 < p :=
  ⟨Nat.Partition.indiscrete (3 * A), 3 * A,
    by rw [Nat.Partition.indiscrete_parts (by omega)]; simp, by omega⟩

end QOU.BraidKnot
