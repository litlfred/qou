import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# `prop:hecke-branching-trace-decomposition` — Hecke branching trace decomposition

For the inclusion `H_n(q) ⊗ H_m(q) ↪ H_{n+m}(q)`, the character
`χ^λ(β_1 · I · β_2)` of an interface element decomposes as a sum over
`(μ ⊢ n, ν ⊢ m)` of traces of operator-valued matrix coefficients
`A^λ_{μ,ν}(I) ∈ End(V_μ ⊗ V_ν)^{⊕ c^λ_{μν}}`, with multiplicities
given by Littlewood–Richardson coefficients.

Provable from Wenzl 1988 (semisimplicity of `H_n(q)` in the
Wenzl-positivity regime `q^{1/2} + q^{-1/2} > 2`) + the standard
branching rule for the Iwahori–Hecke inclusion (Halverson–Ram 1998,
Hoefsmit 1974). The substrate parameter `q_0 ≈ 1.11` is comfortably
inside the regime.

Mathlib does not yet carry the Hoefsmit seminormal basis or the
Hecke-algebra branching infrastructure, so the formalization is
class-axiomatised per AGENTS.md §3b.

## Re-encoded 2026-09-04 (bean `qou-tmmt`) — §3b-cond item 5

This module's own docstring used to argue that it satisfied §3b-cond, in these
words: *"the class carries the genuine hypothesis (the decomposition equation),
and the downstream restatement derives it — it is **not** a `: True`
placeholder."* The second clause is right and the first is the defect. Item 5
does not ask that the class field be non-trivial; it asks that the class
axiomatise the **hypotheses** and the theorem **derive** the claim. A class
whose field is the block's conclusion, consumed by `exact h.decomposition …`,
is a self-assuming projection however substantive that field looks.

What was missing is that **the trace identity is not an independent
assumption** — it follows from the branching itself. The branching rule says
`V_λ ↓ (H_n ⊗ H_m) ≅ ⊕_{(μ,ν)} (V_μ ⊗ V_ν)^{⊕ c^λ_{μν}}`, so `ρ_λ(β₁ · I · β₂)`
has a matrix in a basis indexed by pairs *(block, position within block)*.
Summing a diagonal over such an index set is summing over blocks and then
within each block. That is `Fintype.sum_sigma`, and it needs no hypothesis
about the operator at all — not even block-diagonality, since a trace reads
only the diagonal.

So the class now carries the branching data and the two identifications that
say what `interfaceTrace` and `blockTrace` *are* in that basis, and
`branch_trace` derives the decomposition. The physical content is unchanged and
the conditional status is unchanged; what changed is that the sum rule is now
proved rather than assumed alongside the thing it follows from.
-/

namespace QOU.MassEndomorphism

open Finset

/-- Abstract carrier data for the Hecke branching trace decomposition at
    parameter `q`.

    Because Mathlib lacks the Hoefsmit seminormal basis and the
    Hecke-character infrastructure, the branched representation is modelled
    abstractly:

    * `blockIndex lam` is the finite index set of `(μ ⊢ n, ν ⊢ m)` pairs
      contributing to `λ`, carrying the Littlewood–Richardson multiplicities
      `c^λ_{μν}` (a pair occurring with multiplicity `c` appears `c` times);
    * `blockDim lam p` is `dim (V_μ ⊗ V_ν)` for that block;
    * `branchedMatrix lam I β₁ β₂` is the matrix of `ρ_λ(β₁ · I · β₂)` in the
      branched basis, indexed by `(block, position within block)`;
    * `interfaceTrace` and `blockTrace` are the named scalars of the
      proposition, tied to that matrix by `interfaceTrace_eq` / `blockTrace_eq`.

    The conjectural content is the branching itself — that such a basis exists
    and that the named scalars are read off it. The **sum rule is not a field**:
    it is derived in `branch_trace`. -/
class HeckeBranchingTraceDecomposition (q : ℝ)
    (Λ Elt : Type*) where
  /-- The finite set of `(μ ⊢ n, ν ⊢ m)` block indices feeding `λ`,
      with Littlewood–Richardson multiplicities. -/
  blockIndex : Λ → Type*
  /-- Each block index set is finite (finitely many partitions). Declared as an
      instance binder so the sigma-indexed matrix type below elaborates. -/
  [blockFintype : ∀ lam : Λ, Fintype (blockIndex lam)]
  /-- `dim (V_μ ⊗ V_ν)` for the block `p`. -/
  blockDim : (lam : Λ) → blockIndex lam → ℕ
  /-- **H1 — the branching.** The matrix of `ρ_λ(β₁ · I · β₂)` in a basis
      indexed by `(block, position within block)`. Its existence *is* the
      branching rule; nothing here derives it. -/
  branchedMatrix : (lam : Λ) → Elt → Elt → Elt →
    Matrix (Σ p : blockIndex lam, Fin (blockDim lam p))
      (Σ p : blockIndex lam, Fin (blockDim lam p)) ℝ
  /-- Left-hand side: `tr_{V_λ}(ρ_λ(β₁ · I · β₂))`. -/
  interfaceTrace : Λ → Elt → Elt → Elt → ℝ
  /-- Per-block summand `tr_{V_μ⊗V_ν}(A^λ_{μ,ν}(I)·(ρ_μ(β₁)⊗ρ_ν(β₂)))`. -/
  blockTrace : (lam : Λ) → Elt → Elt → Elt → blockIndex lam → ℝ
  /-- **H2 — the interface trace is that matrix's trace.** Trace is
      basis-independent, so this identifies the named scalar with the branched
      picture. -/
  interfaceTrace_eq : ∀ (lam : Λ) (I beta1 beta2 : Elt),
    interfaceTrace lam I beta1 beta2 =
      Matrix.trace (branchedMatrix lam I beta1 beta2)
  /-- **H3 — the block trace is the diagonal sum over that block.** -/
  blockTrace_eq : ∀ (lam : Λ) (I beta1 beta2 : Elt) (p : blockIndex lam),
    blockTrace lam I beta1 beta2 p =
      ∑ i : Fin (blockDim lam p),
        branchedMatrix lam I beta1 beta2 ⟨p, i⟩ ⟨p, i⟩

attribute [instance] HeckeBranchingTraceDecomposition.blockFintype

/-- **Branching trace decomposition** (`prop:hecke-branching-trace-decomposition`),
    conditional on the class per §3b-cond.  For any `λ` and any interface
    element `I` with braid factors `β₁, β₂`, the interface trace decomposes
    as the sum of the operator-valued block traces over `(μ ⊢ n, ν ⊢ m)`.

    **Derived, not assumed.** The proof is: rewrite both sides into the branched
    basis by H2 and H3, then split a sum over `Σ p, Fin (blockDim p)` into a sum
    over blocks of sums within blocks. No hypothesis about the operator is used
    — a trace reads only the diagonal, so block-diagonality is not needed
    either. -/
theorem branch_trace {q : ℝ} {Λ Elt : Type*}
    [h : HeckeBranchingTraceDecomposition q Λ Elt]
    (lam : Λ) (I beta1 beta2 : Elt) :
    h.interfaceTrace lam I beta1 beta2 =
      ∑ p : h.blockIndex lam, h.blockTrace lam I beta1 beta2 p := by
  -- Ref: [wenzl1988] semisimplicity of H_n(q) in the Wenzl-positivity regime
  -- Ref: [ram1991] Ram's Frobenius character formula for Hecke algebras
  --   (the explicit Murnaghan–Nakayama-type rule for tr A^λ_{μν})
  -- Ref: [hoefsmit1974] Hoefsmit seminormal basis
  rw [h.interfaceTrace_eq lam I beta1 beta2]
  simp only [h.blockTrace_eq lam I beta1 beta2, Matrix.trace, Matrix.diag]
  exact Fintype.sum_sigma _

/-- **Corollary (the case used downstream).** Taking `β₁ = β₂ = Iid`
    (the algebra identity) recovers the scalar form
    `χ^λ(I) = Σ_{μ,ν} tr A^λ_{μ,ν}(I)` consumed by the operator-valued
    Frobenius budget (`rem:operator-valued-magnitude-budget`). -/
theorem branch_trace_character {q : ℝ} {Λ Elt : Type*}
    [h : HeckeBranchingTraceDecomposition q Λ Elt]
    (lam : Λ) (Iid I : Elt) :
    h.interfaceTrace lam I Iid Iid =
      ∑ p : h.blockIndex lam, h.blockTrace lam I Iid Iid p :=
  branch_trace lam I Iid Iid

end QOU.MassEndomorphism
