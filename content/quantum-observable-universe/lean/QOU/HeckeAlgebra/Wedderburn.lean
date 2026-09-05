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
The embedding itself is **not** in this module.  It lives in
`QOU/HeckeAlgebra/WedderburnConstruction.lean` as `blockDiagonal`
(unconditional, injective) and `wedderburnEmbedOf` (the same map
reindexed to `Fin (heckeDim n)`, given RSK as a hypothesis).  An
`opaque wedderburnEmbed` stood here until 2026-09-05 and is gone;
see the note where it was declared for why deletion and not
deprecation.

(This list previously also advertised `wedderburnEmbed_posSemidef`
— "block-diagonal-of-PSD-blocks is PSD on the whole".  No such
theorem exists in this file; the claim is removed rather than
left standing.)

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

**Superseded in part (2026-09-05, beans `qou-usol`, `qou-kp2z`).**
The first of those two is not in fact a blocker: on the natural
index type `Σ λ, Fin (f^λ) × Fin (f^λ)` the assembly is an ordinary
definition and is *injective*.
`QOU/HeckeAlgebra/WedderburnConstruction.lean` builds it
(`blockDiagonal`, `blockDiagonal_injective`) with axiom footprint
`[propext, Classical.choice, Quot.sound]`.  Only landing in
`Fin (n!)` needs RSK, and that step is isolated there as the
explicit hypothesis `RSKDimIdentity`.  The `opaque` that used to
stand below has been deleted, so what remains open here is
deleting it in favour of `wedderburnEmbedOf` is the clean
follow-up (its two remaining references are doc comments in
`MarkovTrace.lean`).

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
theorem PosSemidef.smul_nonneg
    {n : ℕ} {x : WedderburnDecomposition n} (h : x.PosSemidef)
    {c : ℝ} (hc : 0 ≤ c) :
    WedderburnDecomposition.PosSemidef (fun lam => c • x lam) := by
  intro lam
  exact (h lam).smul hc

/-- **Block-PSD is preserved under sum.** -/
theorem PosSemidef.add
    {n : ℕ} {x y : WedderburnDecomposition n}
    (hx : x.PosSemidef) (hy : y.PosSemidef) :
    WedderburnDecomposition.PosSemidef (fun lam => x lam + y lam) := by
  intro lam
  exact (hx lam).add (hy lam)

/-! ### The embedding: retired from this file (2026-09-05, bean `qou-kp2z`)

`opaque wedderburnEmbed : ∀ {n}, WedderburnDecomposition n →
Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ` stood here.  It is
deleted; `QOU/HeckeAlgebra/WedderburnConstruction.lean` carries the
real thing (`blockDiagonal`, and `wedderburnEmbedOf` for the
`Fin (heckeDim n)` landing).

Why it is a deletion rather than a deprecation: `opaque` is not a
free notation.  It is irreducible *and* it reports in
`#print axioms`, so every declaration routed through it read as
axiom-bearing by this corpus's own standard.  Measured on merged
`main` at 7e75622 before removal, nothing routed through it at all:
the sole term-level occurrence of the name in the whole Lean tree
was the declaration itself, and `wenzlBridge` — whose module doc
described the identity in terms of it — is in fact stated over
`markovTraceOnWedderburn`.  So the axiom was being paid for by
nobody, which is the cheapest possible case and also the easiest
one to leave standing forever.

Its docstring carried an argument worth answering rather than
discarding.  Per a Gemini review it held that the embedding could
not simply be *defined*, because a stub returning `0` would
contradict the Markov-trace structure (non-zero traces for
non-zero blocks via the Wenzl bridge) together with
`markovTrace_zero`.  That objection is met, not dodged:
`blockDiagonal` is not a stub, and `blockDiagonal_injective` shows
it is not the zero map — a non-zero decomposition has a non-zero
image.  The objection was to a stub; the answer is a construction.

The dimension identity `Σ_λ (f^λ)² = n!` (RSK) is still not
available here, and is not silently assumed: it is the named
hypothesis `RSKDimIdentity` in the construction module, discharged
by nothing in this corpus.
-/
-- Ref: [wedderburn1908] https://doi.org/10.1112/plms/s2-6.1.77 (Wedderburn decomposition ⊕_λ M_{f^λ}; Σ_λ(f^λ)²=n! via RSK, [fulton1997])

end QOU.HeckeAlgebra.Wedderburn
