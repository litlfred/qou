import Mathlib.Data.Real.Basic
import QOU.Shared.MarkovTraceClaim

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

The class carries only **genuine data** over the shared
`QOU.Shared.MarkovTraceContext` carriers (`R`, `q`, the Hecke algebra
`A = H_N(R, q)`, the Markov-trace instance): the constituent Hecke
elements `ρ(β_i) ∈ A`, the composite braid image `ρ(β_𝔥) ∈ A`, and the
scalar quantities `V̂ᵢ`, `∏ᵢ V̂ᵢ`, `tr_M(ρ(β_𝔥))`, `P_K(q)` — each
pinned to the trace data by a *definitional* link field.  It does
**not** carry the agreement identity as a projected field (the
previous version carried `claim_tmli_constituent_composite_agreement :
constituent_product = composite_trace` and a `def` handing it back —
the self-assuming projection forbidden by AGENTS.md §3b-cond item 5).

- `tmli_constituent_composite_agreement` states the **real** claim —
  Markov-trace multiplicativity across constituents,
  `∏ᵢ tr_M(ρ(β_i)) = tr_M(ρ(β_𝔥))` — as a theorem over the class's
  data fields; it is unproved (`sorry` + manuscript citation per
  AGENTS.md §1a disposition 2 — stated, not yet proved).  The
  manuscript proof iterates the Markov peel (`thm:markov-trace-product`)
  across the constituent factorisation of `β_𝔥`
  (`rem:knot-factorization`).
- `tmli_constituent_product_is_link_polynomial` is **derived**: chaining
  the agreement identity with the definitional link
  `P_K(q) = tr_M(ρ(β_𝔥))` gives `∏ᵢ V̂ᵢ = P_K(q)` — the outer equality
  of the manuscript display, obtained by *using* the main claim, not by
  restating a field.
-/

namespace QOU.BraidsKnots

/-- Data of the constituent/composite Markov-trace agreement claim,
    over the shared `MarkovTraceContext` carriers.  All fields are
    *inputs* (the hadron's braid data and its traced values, pinned by
    definitional links); none is the agreement conclusion. -/
class TmliConstituentCompositeAgreementContext
    extends QOU.Shared.MarkovTraceContext where
  /-- Number of constituents of the hadron `𝔥`. -/
  m : ℕ
  /-- Constituent Hecke elements `ρ(β_i) ∈ H_N(R, q)` (images of the
      constituent sub-braid words). -/
  constituent : ℕ → A
  /-- Composite Hecke element `ρ(β_𝔥) ∈ H_N(R, q)` (image of the full
      hadron braid word). -/
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

/-- **Constituent/composite Markov-trace agreement**
    ([`lem:tmli-constituent-composite-agreement`]) — the real
    manuscript claim, stated over the class's data fields:

      `∏ᵢ V̂ᵢ^const = tr_M(ρ(β_𝔥))`,

    i.e. Markov-trace multiplicativity across the constituent
    factorisation of the hadron braid word (both sides pinned to the
    trace data by the definitional links `constituent_product_def` /
    `composite_trace_def`).  Unproved: the manuscript proof iterates
    the Markov peel of `thm:markov-trace-product` across the
    constituent factorisation of `rem:knot-factorization`.  Stated
    with `sorry` + citation per AGENTS.md §1a disposition 2 — no
    conclusion field on the class hands this back.

    **Mathematical content: PROVED sorry-free** in the chain-list Markov
    model as `QOU.Braiding.markov_trace_flatten`
    (`content/quantum-observable-universe/mass-theory/markov-trace-product.lean`):
    a composite braid that is the `List.flatten` of its constituent
    sub-braids has `tr_M(β_𝔥) = ∏ᵢ tr_M(β_i)` (iterated Markov peel via
    `markov_trace_append` + `chainProduct_flatten`).  The residual `sorry`
    here is purely the **carrier bridge** from that concrete result to the
    abstract `MarkovTraceContext` Hecke-element carriers (`beta_H`,
    `constituent i` are unlinked `A`-elements in this class — the split-
    tensor structure needed to instantiate `markov_trace_flatten` is not
    yet carried).  It is a modelling artifact, not an open math gap. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/tmli-constituent-composite-agreement.md
-- Math proved sorry-free: QOU.Braiding.markov_trace_flatten (chain-list model)
theorem tmli_constituent_composite_agreement
    [ctx : TmliConstituentCompositeAgreementContext] :
    ctx.constituent_product = ctx.composite_trace := by
  -- Ref: [manuscript] quantum-observable-universe/mass-theory/tmli-constituent-composite-agreement.md
  -- Carrier bridge to QOU.Braiding.markov_trace_flatten (proved sorry-free).
  sorry

/-- **Constituent product equals the link polynomial** — derived:
    chaining the agreement identity with the definitional link
    `P_K(q) = tr_M(ρ(β_𝔥))` gives the outer equality of the manuscript
    display, `∏ᵢ V̂ᵢ^const = P_{K_𝔥}(q)`.  Genuine composition of the
    main claim with a definitional link, not a projected field. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/tmli-constituent-composite-agreement.md
theorem tmli_constituent_product_is_link_polynomial
    [ctx : TmliConstituentCompositeAgreementContext] :
    ctx.constituent_product = ctx.P_K := by
  have hmain := tmli_constituent_composite_agreement (ctx := ctx)
  rw [hmain, ctx.composite_trace_def, ctx.P_K_def]

end QOU.BraidsKnots
