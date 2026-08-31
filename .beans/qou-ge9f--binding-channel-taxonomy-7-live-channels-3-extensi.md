---
# qou-ge9f
title: 'Binding channel taxonomy: 7 live channels, 3 extensive+additive, the shipped one is neither'
status: completed
type: task
priority: normal
created_at: 2026-08-31T04:26:46Z
updated_at: 2026-08-31T04:27:27Z
---

## The full taxonomy (branch `claude/binding-channel-taxonomy-2026-08-31`)

Owner: *"explore all options"*. Enumerated by grepping `computations/` for the
ARTEFACT CLASS ("what computes a binding?") rather than for a mechanism — the
thing I had not done, and which is why three earlier findings were re-derivations.

**Seven live channels.** Scored on STRUCTURE, not on AME agreement (choosing the
channel nearest the data is the fit this arc exists to avoid; the AME column is
printed and explicitly not fed into any verdict).

| # | channel | source | extensive | additive/bond |
|---|---|---|---|---|
| 1 | `Q_β(\|tr_f\|−\|tr_a\|)` observe-early | `binding_canonical` **(ships)** | **no** | **no** |
| 2 | `Q_β Σ_λ y_λ(θ_f−θ_a)` angle | `binding_canonical`, self-REFUTED | — | no (over *partitions*) |
| 3 | `E₀ log(tr_f/tr_a)` | `log_ratio_binding_prototype`, `derived_bond_graph_binding` | **YES** | **YES** |
| 4 | `(E₀/2) Σ log(1/(f·f̄))` bar-norm | `derived_bond_graph_binding` | **YES** | **YES** |
| 5 | `Σ_chain E₀(tr_f−tr_a)_pair` | `derive_binding_chain_cooperative` | **YES** | **YES** |
| 6 | `m_e Vol(K_bind) Δtr` | `binding_link_volumes` | — | needs Vol, =0 for D |
| 7 | `ρ_F m_e A Vol(𝓑)` magic-A | `magic_A_formula` (deprecation-cand.) | trivially | says nothing |

**Extensivity tested exactly**, not by threshold: `B` affine in `A` ⟺ second
finite difference vanishes. On the grid `A = 8,16,24,32,40`:

    ch3, ch4   2nd diff / 1st diff  =  7.31e-51     -> exactly affine
    ch5                             =  4.69e-51     -> exactly affine
    ch1                             =  0.390        -> NOT

A first version of this probe used a "spread over the tail < 2 %" rule and called
ch3 non-extensive — wrong, because `B/A = c(A−1)/A` is still 2.5 % short of its
limit at A=40. The threshold contradicted the exact measurement I already had in
#6332; replaced by the finite-difference test.

**3 and 4 collapse together.** 2.8488631 vs 2.8488779 at A=40 (5e-6 apart),
converging, because under convention D the bar involution EXCHANGES pp and nn, so
on an N=Z chain the symmetrisation is nearly a no-op. **So seven channels reduce
to two distinct extensive candidates: the log family and the pairwise sum.**

## The answer to the channel question

It was not an independent question. The chain is FORCED by the strand layout
(`qou-gwr9`); on the chain the additive channels are *exactly* affine, hence
saturate; and `complete_graph_no_saturation` only ever bit on the additive family
in the first place. The shipped channel is outside that family entirely.

What is left open is the **magnitude** — 2–3× on the log family — which is the
`qou-brng` gap as it always was, now with the channel ambiguity removed.

## Corrections carried in the probe docstring

Two of my earlier "findings" were corpus re-derivations, recorded there rather
than quietly dropped: #6332's Channel-2 result is stated verbatim in
`log_ratio_binding_prototype`'s docstring; #6346 Part 2's measurement is stated in
`derive_binding_chain_cooperative`'s. What survives as new is the
`CoordinationSaturation` arity connection, the `A* = 2/ln c` prediction, and the
Lean proof that the chain is forced rather than merely observed.
