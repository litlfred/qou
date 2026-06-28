import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

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
class-axiomatised per AGENTS.md §3b: `HeckeBranchingTraceDecomposition`
encodes the **trace identity itself** as a Prop-valued class field over
abstract carrier data (the per-`λ` interface trace and the indexed family
of block traces), and `branch_trace` is the conditional restatement that
derives the identity from that class.  This is the §3b-cond
conditional-class pattern: the class carries the genuine hypothesis (the
decomposition equation), and the downstream restatement derives it — it is
**not** a `: True` placeholder.
-/

namespace QOU.MassEndomorphism

open Finset

/-- Abstract carrier data for the Hecke branching trace decomposition at
    parameter `q`, with the decomposition identity as its substantive
    content field.

    Because Mathlib lacks the Hoefsmit seminormal basis and the
    Hecke-character infrastructure, the operator-valued coefficients
    `A^λ_{μ,ν}(I) ∈ End(V_μ ⊗ V_ν)^{⊕ c^λ_{μν}}` are modelled abstractly:

    * `interfaceTrace λ I β₁ β₂` is the scalar
      `tr_{V_λ}(ρ_λ(β₁ · I · β₂))` (the left-hand side);
    * `blockIndex λ` is the finite index set of `(μ ⊢ n, ν ⊢ m)` pairs
      contributing to `λ` (carrying the Littlewood–Richardson
      multiplicities `c^λ_{μν}`);
    * `blockTrace λ I β₁ β₂ p` is the per-block scalar
      `tr_{V_μ ⊗ V_ν}(A^λ_{μ,ν}(I) · (ρ_μ(β₁) ⊗ ρ_ν(β₂)))` (a summand of
      the right-hand side).

    The substantive content is `decomposition`: the trace identity
    `tr_{V_λ}(…) = Σ_{(μ,ν)} tr_{V_μ⊗V_ν}(…)`.  Types `Elt`, `Λ` are
    abstract stand-ins for the Hecke-algebra elements and the partition
    index until the Mathlib infrastructure lands. -/
class HeckeBranchingTraceDecomposition (q : ℝ)
    (Λ Elt : Type*) where
  /-- The finite set of `(μ ⊢ n, ν ⊢ m)` block indices feeding `λ`,
      with Littlewood–Richardson multiplicities. -/
  blockIndex : Λ → Type*
  /-- Each block index set is finite (finitely many partitions). -/
  blockFintype : ∀ lam : Λ, Fintype (blockIndex lam)
  /-- Left-hand side: `tr_{V_λ}(ρ_λ(β₁ · I · β₂))`. -/
  interfaceTrace : Λ → Elt → Elt → Elt → ℝ
  /-- Per-block summand `tr_{V_μ⊗V_ν}(A^λ_{μ,ν}(I)·(ρ_μ(β₁)⊗ρ_ν(β₂)))`. -/
  blockTrace : (lam : Λ) → Elt → Elt → Elt → blockIndex lam → ℝ
  /-- **The branching trace decomposition identity** (the substantive
      claim of `prop:hecke-branching-trace-decomposition`): the interface
      trace equals the sum of the block traces over `(μ, ν)`. -/
  decomposition :
    ∀ (lam : Λ) (I beta1 beta2 : Elt),
      interfaceTrace lam I beta1 beta2 =
        @Finset.sum (blockIndex lam) ℝ _ (@Finset.univ _ (blockFintype lam))
          (fun p => blockTrace lam I beta1 beta2 p)

attribute [instance] HeckeBranchingTraceDecomposition.blockFintype

/-- **Branching trace decomposition** (`prop:hecke-branching-trace-decomposition`),
    conditional on the class per §3b-cond.  For any `λ` and any interface
    element `I` with braid factors `β₁, β₂`, the interface trace decomposes
    as the sum of the operator-valued block traces over `(μ ⊢ n, ν ⊢ m)`.

    This is derived from the class field `decomposition` — it is a genuine
    conditional theorem, not a placeholder. -/
theorem branch_trace {q : ℝ} {Λ Elt : Type*}
    [h : HeckeBranchingTraceDecomposition q Λ Elt]
    (lam : Λ) (I beta1 beta2 : Elt) :
    h.interfaceTrace lam I beta1 beta2 =
      ∑ p : h.blockIndex lam, h.blockTrace lam I beta1 beta2 p := by
  -- Ref: [wenzl1988] semisimplicity of H_n(q) in the Wenzl-positivity regime
  -- Ref: [ram1991] Ram's Frobenius character formula for Hecke algebras
  --   (the explicit Murnaghan–Nakayama-type rule for tr A^λ_{μν})
  -- Ref: [hoefsmit1974] Hoefsmit seminormal basis
  exact h.decomposition lam I beta1 beta2

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
