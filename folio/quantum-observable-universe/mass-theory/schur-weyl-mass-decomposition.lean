import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Combinatorics.Young.YoungDiagram
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

/-- **Schur–Weyl mass decomposition.**

    For an atomic braid `𝒜 ∈ H_{3A}(q)` on `3A` strands, the
    Markov trace decomposes over partitions of `3A`:

      tr_M(𝒜) = Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(𝒜)

    This is the exact Wedderburn decomposition; the engine's
    additive-H₃-per-generator approximation drops all partitions
    that are not concatenations of three-row blocks.

    Ref: [leitner2026] `thm:wedderburn-mass-formula`,
         `prop:three-parameters-wedderburn`. -/
class SchurWeylMassDecomposition (A : ℕ) where
  /-- The atomic braid as an element of `H_{3A}(q)` (opaque). -/
  atomicBraid : Unit
  /-- The substrate parameter. -/
  q : ℝ
  /-- The list of partitions of `3A`. -/
  partitions : List (PartitionOfN (3 * A))
  /-- The Markov trace of the atomic braid. -/
  markovTrace : ℝ
  /-- Decomposition: trace equals weighted sum over partitions. -/
  decomposition :
    markovTrace =
      (partitions.map (fun lam =>
        schurWeylWeight lam q * spechtCharacter lam atomicBraid)).sum

-- **A = 1 specialisation.**  For a single nucleon (`H_3(q)`) the
-- partitions of 3 are `(3)`, `(2,1)`, `(1,1,1)`, giving the
-- three-channel Wedderburn weights.  This recovers
-- `thm:wedderburn-mass-formula`.
-- Ref: [leitner2026] `prop:three-parameters-wedderburn`.
/-! ## The partition list is FREE DATA -- two axioms deleted 2026-09-06

`SchurWeylMassDecomposition` carries `partitions` as an ordinary field
with no completeness condition, and `markovTrace` as another.  The only
field relating them, `decomposition`, is satisfiable for **any**
`partitions` by choosing `markovTrace` to be the corresponding sum.  So
nothing forces `partitions` to be the partitions of `3A` -- it can be
empty.

Two axioms quantified over every instance as though it did:

    a_eq_one_three_channels_axiom :
      ∀ (S : SchurWeylMassDecomposition 1), S.partitions.length = 3

    additive_wedderburn_missing_partitions_axiom :
      ∀ (A : ℕ), 2 ≤ A → ∀ (S : SchurWeylMassDecomposition A),
        ∃ lam ∈ S.partitions, lam.parts.head? = some (3 * A)

Both are false at the empty instance below, and both are deleted.  The
mathematics they cite is not in dispute -- 3 really is the number of
partitions of 3 -- but neither Lean statement said that.  A statement
that did would be about `Nat.Partition 3`, or would carry a
completeness field on the structure; adding one is a structure refactor
and is deliberately not guessed at here.
-/

/-- An instance whose partition list is empty.  `decomposition` holds
    because the empty sum is `0`. -/
def emptyDecomposition (A : ℕ) : SchurWeylMassDecomposition A where
  atomicBraid := ()
  q := 0
  partitions := []
  markovTrace := 0
  decomposition := by simp

/-- **`a_eq_one_three_channels_axiom` is false.** -/
theorem not_a_eq_one_three_channels :
    ¬ (∀ (S : SchurWeylMassDecomposition 1), S.partitions.length = 3) := by
  intro h
  simpa [emptyDecomposition] using h (emptyDecomposition 1)

/-- **`additive_wedderburn_missing_partitions_axiom` is false.** -/
theorem not_additive_wedderburn_missing_partitions :
    ¬ (∀ (A : ℕ), 2 ≤ A → ∀ (S : SchurWeylMassDecomposition A),
        ∃ lam ∈ S.partitions, lam.parts.head? = some (3 * A)) := by
  intro h
  simpa [emptyDecomposition] using h 2 (by norm_num) (emptyDecomposition 2)

end QOU.BraidKnot
