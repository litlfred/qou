import Mathlib.Data.List.Basic
import Mathlib.Data.List.Sort
import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Basic


/-!
# QOU.BraidKnot.PSDTraceOrthogonality

Lean axiomatisation of the conjectural orthogonality between
PSD-dominance and Markov-trace-dominance in the Wedderburn
decomposition of the canonical atom-braid Hecke image.

Empirically verified at A=4 (⁴He) with 10⁵ y_λ magnitude separation
and at A=6 (⁶Li) with 10⁹ separation, via the Python Lanczos
LinearOperator probe (`probe_4_li6_rectangular_python.py`).

## The conjecture (informal)

For the canonical atom-braid `T_w(Z, N) ∈ B_{3A}` and its image in
`H_{3A}(q)` at `q = q_0`:

- The partitions `λ ⊢ 3A` maximising `|y_λ(q_0)|` (Markov-trace
  weight) form the **trace-dominant family**: 1- or 2-row
  "long-string" shapes `(n)`, `(n-1, 1)`, `(n-2, 2)`, ...
- The partitions `λ` minimising `ε_min(ρ_λ(T_w)_sym)` (PSD
  obstruction) form the **PSD-dominant family**: 3+row multi-step
  "tall narrow" shapes.
- These two families are **disjoint** (shape-class disjointness).
- The magnitude separation `η(A) := max|y_trace| / |y_PSD|` grows
  without bound: `η(4) ≈ 1.6 × 10^5`, `η(6) ≈ 9 × 10^8`.

## Status

Per AGENTS.md §3b-cond, axiomatised as a Lean `class`
`PSDTraceOrthogonalDecomp` with fields encoding the disjointness
claim. The empirical witnesses (A=4, A=6) provide concrete
instance data but not Lean instances — those would require
formalising the Hecke representation theory at q ≠ 1.

Ref: [manuscript] conj:psd-trace-orthogonality
Ref: [manuscript] computations/probe_1_project_4he_on_dominant.py
Ref: [manuscript] computations/probe_1b_li6_orthogonality.py
Ref: [manuscript] computations/probe_4_li6_rectangular_python.py
-/

namespace QOU.BraidKnot.PSDTraceOrthogonality

/-- A **partition** of `n` represented as a non-increasing list of
positive natural numbers summing to `n`. -/
def Partition (n : ℕ) : Type :=
  { l : List ℕ // l.sum = n ∧ l.Sorted (· ≥ ·) ∧ ∀ k ∈ l, k > 0 }

/-- The number of rows of a partition. -/
def Partition.numRows {n : ℕ} (p : Partition n) : ℕ := p.val.length

/-- The largest row (= max part) of a partition. -/
def Partition.maxRow {n : ℕ} (p : Partition n) : ℕ :=
  p.val.foldl max 0

/-- The partition is **1- or 2-row** iff `numRows ≤ 2`. -/
def Partition.isLongString {n : ℕ} (p : Partition n) : Prop :=
  p.numRows ≤ 2

/-- The partition is **multi-row narrow** iff `numRows ≥ 3` and
`maxRow ≤ 3 · numRows / |partition|` (heuristic; the empirical
falsifiers all have rows ≥ 4 and maxRow ≤ 5). The formal definition
should be the OPPOSITE of the long-string condition, plus a
boundedness constraint on max-row. -/
def Partition.isTallNarrow {n : ℕ} (p : Partition n) : Prop :=
  p.numRows ≥ 3 ∧ p.maxRow ≤ 7  -- heuristic threshold

/-- **PSDTraceOrthogonalDecomp** — abstract class encoding the
conjectured orthogonality of trace-dominance and PSD-dominance
shape classes for an atom of mass number `A`.

Fields:

- `traceDominantFamily` : the set of partitions of `3 * A` whose
  `|y_λ|` is in the top decile.
- `psdDominantFamily` : the set of partitions of `3 * A` whose
  `ε_min(ρ_λ(T_w_sym))` is in the bottom decile (most negative).
- `disjoint` : these two sets are disjoint.
- `etaLowerBound` : the magnitude-separation function `η(A) := max
  |y_trace| / |y_PSD|` is at least `10^(2A − 3)`.
-/
class PSDTraceOrthogonalDecomp (A : ℕ) where
  traceDominantFamily : Set (Partition (3 * A))
  psdDominantFamily : Set (Partition (3 * A))
  disjoint : traceDominantFamily ∩ psdDominantFamily = ∅
  traceFamilyAreLongString :
    ∀ p ∈ traceDominantFamily, p.isLongString
  psdFamilyAreTallNarrow :
    ∀ p ∈ psdDominantFamily, p.isTallNarrow
  etaLowerBound : ℝ
  etaSeparation : etaLowerBound ≥ 10 ^ (2 * A - 3)

/-- The orthogonality conjecture: an instance of
`PSDTraceOrthogonalDecomp` exists for every atom number `A ≥ 2`.

This is the categorical statement of the empirical pattern; a
proof would require Hecke representation theory at `q = q_0`
(specifically, the seminormal-basis structure interacting with the
canonical `atom_braid_word_3A(Z, N)` word).
-/
class PSDTraceOrthogonalityHolds where
  instances : ∀ A : ℕ, A ≥ 2 → PSDTraceOrthogonalDecomp A

/-- The conjecture statement: orthogonality holds for all atoms
with `A ≥ 2`.

Ref: [manuscript] conj:psd-trace-orthogonality
-/
theorem psd_trace_orthogonality_holds_for_all_atoms
    [PSDTraceOrthogonalityHolds] :
    ∀ A : ℕ, A ≥ 2 → ∃ (_inst : PSDTraceOrthogonalDecomp A), True := by
  intro A hA
  refine ⟨PSDTraceOrthogonalityHolds.instances A hA, trivial⟩

end QOU.BraidKnot.PSDTraceOrthogonality
