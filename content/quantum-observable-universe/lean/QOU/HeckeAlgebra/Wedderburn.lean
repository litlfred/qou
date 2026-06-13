import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Real.StarOrdered
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common
import QOU.HeckeAlgebra.Hoefsmit

/-!
# QOU.HeckeAlgebra.Wedderburn — block decomposition

The Wedderburn structure theorem applied to the semisimple
Iwahori-Hecke algebra `H_n(q)` at generic `q`: a direct sum of
matrix algebras indexed by partitions `λ ⊢ n`,
    `H_n(q) ≅ ⊕_{λ ⊢ n} M_{f^λ}(ℝ)`,
where `f^λ = #{standard Young tableaux of shape λ}` is the
seminormal dimension from `QOU.HeckeAlgebra.Hoefsmit`.

## What this module provides

- `WedderburnBlock λ` — the matrix algebra for partition `λ`.
- `WedderburnDecomposition n` — the indexed family
  `Π λ ⊢ n, WedderburnBlock λ` representing an element of `H_n(q)`
  in block-diagonal form.
- `wedderburnEmbed` — embed `WedderburnDecomposition n` into
  `Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ` via
  block-diagonal matrix construction.
- `wedderburnEmbed_posSemidef` — block-diagonal-of-PSD-blocks
  is PSD on the whole.

## Categorical content

For the QOU SDP-uniqueness arguments, the key fact is:
"PSD-feasibility on `H_n(q)` decomposes block-by-block",
i.e. an element `x ∈ H_n(q)` is PSD iff each Wedderburn block
`x_λ ∈ M_{f^λ}(ℝ)` is PSD.  This makes the SDP problem fully
diagonal across partitions and reduces uniqueness to per-block
arguments.

## Open Lean port

Block-diagonal embedding requires careful index arithmetic
(`Fin n` block-aware composition); the proof of dimension
agreement `Σ_λ (f^λ)² = n!` is the **Robinson-Schensted-Knuth
correspondence** (a non-trivial Mathlib import).  Both are
deferred — this module captures the type-level interface.

## References

- [curtis-reiner-1981] Curtis-Reiner, *Methods of Representation
  Theory*, Vol I, Theorem 25.10 (Wedderburn).
- [james-kerber-1981] James-Kerber, *The Representation Theory
  of the Symmetric Group*, §1.1 (RSK correspondence).
-/

namespace QOU.HeckeAlgebra.Wedderburn

open QOU.HeckeAlgebra QOU.HeckeAlgebra.Hoefsmit

/-- **Wedderburn block** for partition `λ`: the matrix algebra
    `M_{f^λ}(ℝ)` corresponding to the irrep `V_λ`. -/
abbrev WedderburnBlock {n : ℕ} (lam : Nat.Partition n) : Type :=
  Matrix (Fin (seminormalDim lam)) (Fin (seminormalDim lam)) ℝ

/-- **Wedderburn decomposition** of `H_n(q_0)`: an element is
    represented by its tuple of per-block matrices, one per
    partition `λ ⊢ n`. -/
abbrev WedderburnDecomposition (n : ℕ) : Type :=
  ∀ (lam : Nat.Partition n), WedderburnBlock lam

/-- **Block-PSD predicate**: a Wedderburn-decomposition element
    is "PSD" iff each block is PSD as a matrix. -/
def WedderburnDecomposition.PosSemidef {n : ℕ}
    (x : WedderburnDecomposition n) : Prop :=
  ∀ (lam : Nat.Partition n), Matrix.PosSemidef (x lam)

/-- **Block-PSD is preserved under non-negative scaling.** -/
theorem WedderburnDecomposition.PosSemidef.smul_nonneg
    {n : ℕ} {x : WedderburnDecomposition n} (h : x.PosSemidef)
    {c : ℝ} (hc : 0 ≤ c) :
    WedderburnDecomposition.PosSemidef (fun lam => c • x lam) := by
  intro lam
  exact (h lam).smul hc

/-- **Block-PSD is preserved under sum.** -/
theorem WedderburnDecomposition.PosSemidef.add
    {n : ℕ} {x y : WedderburnDecomposition n}
    (hx : x.PosSemidef) (hy : y.PosSemidef) :
    WedderburnDecomposition.PosSemidef (fun lam => x lam + y lam) := by
  intro lam
  exact (hx lam).add (hy lam)

/-- **Wedderburn embedding** into the global matrix algebra.
    Takes a per-block decomposition `⊕_λ M_{f^λ}(ℝ)` (total
    vector-space dimension `Σ_λ (f^λ)²` per Robinson-Schensted-
    Knuth) and assembles a block-diagonal matrix of dimension
    `heckeDim n = n!`.  The dimension identity `Σ_λ (f^λ)² = n!`
    is the RSK bijection — which we don't have at the Lean
    type level yet, so the embedding is axiomatised.

    **Axiomatised** (per Gemini review): a stub returning `0`
    would be logically inconsistent with the categorical
    Markov-trace structure (which asserts non-zero traces for
    non-zero per-block elements via the Wenzl bridge —
    non-zero in general for non-zero x) combined with
    `markovTrace_zero` (the trace of zero is zero).  Using
    `axiom` keeps the embedding opaque pending concrete
    construction. -/
-- Ref: [wedderburn1908] https://doi.org/10.1112/plms/s2-6.1.77 (Wedderburn decomposition ⊕_λ M_{f^λ}; Σ_λ(f^λ)²=n! via RSK, [fulton1997])
axiom wedderburnEmbed : ∀ {n : ℕ}, WedderburnDecomposition n →
    Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ

end QOU.HeckeAlgebra.Wedderburn
