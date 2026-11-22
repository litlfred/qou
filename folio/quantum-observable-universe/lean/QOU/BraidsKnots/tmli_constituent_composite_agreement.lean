import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import QOU.Hecke.MarkovTrace

/-!
# QOU.BraidsKnots.tmli_constituent_composite_agreement

Canonical declaration for content block
[`lem:tmli-constituent-composite-agreement`](../../../mass-theory/tmli-constituent-composite-agreement.md):
*Constituent and composite Markov-trace evaluations agree exactly*.
The `lean.ref` URI
`qou:QOU.BraidsKnots.tmli_constituent_composite_agreement` resolves
here.

**Lemma statement** (from manuscript): for a hadron
$\mathfrak{H} \hookrightarrow V^{\otimes N}$ with
$N = 2(j_1 + \cdots + j_n)$ and braid word
$\beta_{\mathfrak{H}} \in B_N$, the constituent product
$\prod_i \hat{V}_i^{\mathrm{const}}$ and the composite trace
$\mathrm{tr}_M(\rho(\beta_{\mathfrak{H}}))$ evaluate the same element
of $H_N(q)$, so

$$
  \prod_i \hat{V}_i^{\mathrm{const}}
  =
  \mathrm{tr}_M(\rho(\beta_{\mathfrak{H}}))
  =
  P_{K_{\mathfrak{H}}}(q).
$$

## Disposition (integrity)

The class carries only **genuine data** (the constituent Hecke elements
`ρ(β_i) ∈ A`, the composite braid image `ρ(β_𝔥) ∈ A`, the scalar
quantities `V̂ᵢ`, `∏ᵢ V̂ᵢ`, `tr_M(ρ(β_𝔥))`, `P_K(q)` — each pinned to the
trace data by a *definitional* link field) plus the **Markov-peel
factorisation** of `β_𝔥` as per-step *structural* inputs
(`partialComposite`, `partial_zero`, `partial_full`, `peel`).  It does
**not** carry the agreement identity as a projected field (the previous
version carried `claim_… : constituent_product = composite_trace` and a
`def` handing it back — the self-assuming projection forbidden by
AGENTS.md §3b-cond item 5).

- `tmli_constituent_composite_agreement` states the **real** claim —
  Markov-trace multiplicativity across constituents,
  `∏ᵢ tr_M(ρ(β_i)) = tr_M(ρ(β_𝔥))` — and is now **proved sorry-free**
  (§3b-cond conditional class).  The class supplies the Markov peel of
  `thm:markov-trace-product` **one step per constituent** (`peel`); the
  theorem **derives** the aggregate identity by induction on the prefix
  length.  The `peel` field is the per-step hypothesis, not the aggregate
  conclusion (§3b-cond item 5, non-degenerate).  It mirrors the chain-list
  realisation `QOU.Hecke.markov_trace_append (ascending blocks on consecutive generators)`.
- `tmli_constituent_product_is_link_polynomial` is **derived**: chaining
  the agreement identity with the definitional link
  `P_K(q) = tr_M(ρ(β_𝔥))` gives `∏ᵢ V̂ᵢ = P_K(q)` — the outer equality
  of the manuscript display, obtained by *using* the main claim, not by
  restating a field.

## Base-ring convention (§7c / §7d)

The ring / algebra structure is carried as genuine **instance binders**
(`[CommRing R] [Ring A] [Algebra R A] [MarkovTrace n q A]`), *not* as
opaque data fields.  This is required for the induction: with the ring
stored as data the `Finset.prod`-side `1`/`*` (monoid path) and the
`peel`-side `1`/`*` (ring path) are non-defeq (the projections cannot
reduce past an opaque field), so `exact`/`ring`/`simp` cannot bridge
them.  With real instance binders the paths are defeq (Mathlib forgetful
inheritance) and the proof goes through.  Hence this block does not extend
the shared data-field carrier `QOU.Shared.MarkovTraceContext`.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/tmli-constituent-composite-agreement.md
-- Ref: QOU.Hecke.markov_trace_append (ascending blocks on consecutive generators) (chain-list realisation of the same identity)
-/

namespace QOU.BraidsKnots

universe u

/-- Data of the constituent/composite Markov-trace agreement claim, over
    genuine ring/algebra **instance binders** (see the base-ring note in
    the module docstring).  All fields are *inputs*: the hadron's braid
    data, its traced values (pinned by definitional links), and the
    per-step Markov-peel factorisation of `β_𝔥`; none is the agreement
    conclusion. -/
class TmliConstituentCompositeAgreementContext
    {R : Type u} [CommRing R] [Inv R] {n : ℕ} {q : R}
    {A : Type u} [Ring A] [Algebra R A]
    [QOU.Hecke.HeckeAlgebra R n q A]
    [markovInst : QOU.Hecke.MarkovTrace n q A] where
  /-- Number of constituents of the hadron `𝔥`. -/
  m : ℕ
  /-- Constituent Hecke elements `ρ(β_i) ∈ H_N(R, q)`. -/
  constituent : ℕ → A
  /-- Composite Hecke element `ρ(β_𝔥) ∈ H_N(R, q)`. -/
  beta_H : A
  /-- Traced constituent volumes `V̂ᵢ^const : R`. -/
  V_hat : ℕ → R
  /-- Definitional link: `V̂ᵢ^const = tr_M(ρ(β_i))`. -/
  V_hat_def : ∀ i, V_hat i = markovInst.trace (constituent i)
  /-- The constituent product `∏ᵢ V̂ᵢ^const : R`. -/
  constituent_product : R
  /-- Definitional link: the constituent product is the product of the
      traced constituent volumes over the `m` constituents. -/
  constituent_product_def :
    constituent_product = (Finset.range m).prod (fun i => V_hat i)
  /-- The composite Markov-trace value `tr_M(ρ(β_𝔥)) : R`. -/
  composite_trace : R
  /-- Definitional link: `composite_trace = tr_M(ρ(β_𝔥))`. -/
  composite_trace_def : composite_trace = markovInst.trace beta_H
  /-- The link-polynomial value `P_{K_𝔥}(q) : R`. -/
  P_K : R
  /-- Definitional link: the link polynomial of the hadron knot is the
      Markov trace of the composite braid image (Jones's construction). -/
  P_K_def : P_K = markovInst.trace beta_H
  /-- The Markov-peel partial composites: `partialComposite k` is the
      composite Hecke element of the first `k` constituents along Jones's
      constituent factorisation of `β_𝔥`. -/
  partialComposite : ℕ → A
  /-- Base of the Markov peel: the empty partial composite traces to `1`
      (`tr_M(𝟙) = 1`). -/
  partial_zero : markovInst.trace (partialComposite 0) = 1
  /-- Closure of the peel: the full partial composite over all `m`
      constituents is the composite hadron braid image `ρ(β_𝔥)`. -/
  partial_full : partialComposite m = beta_H
  /-- **One Markov peel per constituent** (`thm:markov-trace-product`
      applied at each interface): appending constituent `k` multiplies the
      running Markov trace by `tr_M(ρ(β_k))`.  Per-step *structural* input;
      the aggregate agreement is **derived** from it below (§3b-cond item 5,
      non-degenerate). -/
  peel : ∀ k, k < m →
    markovInst.trace (partialComposite (k + 1))
      = markovInst.trace (constituent k) * markovInst.trace (partialComposite k)

/-- **Constituent/composite Markov-trace agreement**
    ([`lem:tmli-constituent-composite-agreement`]) — proved sorry-free:

      `∏ᵢ V̂ᵢ^const = tr_M(ρ(β_𝔥))`,

    i.e. Markov-trace multiplicativity across the constituent
    factorisation of the hadron braid word.  The aggregate is obtained by
    inducting the per-constituent Markov peel (`peel`) over the prefix
    length; the definitional links `constituent_product_def` /
    `composite_trace_def` / `partial_full` reduce the claim to that
    aggregate. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/tmli-constituent-composite-agreement.md
-- Ref: QOU.Hecke.markov_trace_append (ascending blocks on consecutive generators) (chain-list realisation)
theorem tmli_constituent_composite_agreement
    {R : Type u} [CommRing R] [Inv R] {n : ℕ} {q : R}
    {A : Type u} [Ring A] [Algebra R A]
    [QOU.Hecke.HeckeAlgebra R n q A] [markovInst : QOU.Hecke.MarkovTrace n q A]
    [ctx : TmliConstituentCompositeAgreementContext (markovInst := markovInst)] :
    ctx.constituent_product = ctx.composite_trace := by
  -- Aggregate the per-constituent Markov peels: for every prefix of length
  -- `k ≤ m`, the running product of constituent traces equals the trace of
  -- the `k`-th partial composite.  Induction on `k`, one `peel` per step.
  have key : ∀ k, k ≤ ctx.m →
      (Finset.range k).prod (fun i => markovInst.trace (ctx.constituent i))
        = markovInst.trace (ctx.partialComposite k) := by
    intro k
    induction k with
    | zero =>
      intro _
      rw [Finset.prod_range_zero]
      exact ctx.partial_zero.symm
    | succ j ih =>
      intro hj
      rw [Finset.prod_range_succ, ih (Nat.le_of_succ_le hj), mul_comm]
      exact (ctx.peel j (Nat.lt_of_succ_le hj)).symm
  -- Instantiate at the full length `m` and unfold the definitional links.
  rw [ctx.constituent_product_def, ctx.composite_trace_def, ← ctx.partial_full]
  simp only [ctx.V_hat_def]
  exact key ctx.m (le_refl ctx.m)

/-- **Constituent product equals the link polynomial** — derived:
    chaining the agreement identity with the definitional link
    `P_K(q) = tr_M(ρ(β_𝔥))` gives the outer equality of the manuscript
    display, `∏ᵢ V̂ᵢ^const = P_{K_𝔥}(q)`.  Genuine composition of the
    main claim with a definitional link, not a projected field. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/tmli-constituent-composite-agreement.md
theorem tmli_constituent_product_is_link_polynomial
    {R : Type u} [CommRing R] [Inv R] {n : ℕ} {q : R}
    {A : Type u} [Ring A] [Algebra R A]
    [QOU.Hecke.HeckeAlgebra R n q A] [markovInst : QOU.Hecke.MarkovTrace n q A]
    [ctx : TmliConstituentCompositeAgreementContext (markovInst := markovInst)] :
    ctx.constituent_product = ctx.P_K := by
  have hmain := tmli_constituent_composite_agreement (ctx := ctx)
  rw [hmain, ctx.composite_trace_def, ctx.P_K_def]

end QOU.BraidsKnots
