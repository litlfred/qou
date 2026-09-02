---
# qou-ge9f
title: 'Binding channel taxonomy: 7 live channels, 3 extensive+additive, the shipped one is neither'
status: completed
type: task
priority: normal
created_at: 2026-08-31T04:26:46Z
updated_at: 2026-08-31T04:50:22Z
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


## Follow-up: my "all-pairs estimate is a type-mix artefact" conjecture is REFUTED

After #6364 refreshed `log_ratio_binding_prototype`'s stale witness, its all-pairs
range came out **0.61–1.63×** of AME — the only range in the arc straddling 1. I
flagged it as probably an artefact: the extrapolation `E₀·L·C(A,2)/(A−1)` takes
`L` measured on the **chain** and rescales by the complete graph's bond count,
while the two bond sets have very different type mixes (at A=6 N=Z: chain
`(2,1,2)` vs complete `(3,9,3)`) and the per-bond energies spread by a factor
**1.85**.

**Measured against the true all-pairs sum `C(Z,2)ε_pp + ZN·ε_pn + C(N,2)ε_nn`,
the extrapolation is accurate to within 5.1 % on every nucleus D…¹⁶O**, and exact
on the deuteron. Conjecture refuted.

**Why it survives, and it is structural not luck.** `ε_pn = 2.8332` sits 3.1 %
below the arithmetic mean of `ε_pp` and `ε_nn` (2.9242), so the mean per-bond
energy is nearly mix-independent. That near-equality is forced: the bond factors
satisfy `f_pn = (f_pp + f_nn)/2 + hδ/4` **exactly** (verified, residual 1.3e-51 —
rounding order at 50 dps), so `f_pn` is the arithmetic mean of the other two. With
`ε = −E₀ log f`, comparing `ε_pn` to `(ε_pp+ε_nn)/2` compares log-of-mean to
mean-of-logs; by Jensen the first is larger, so `ε_pn ≤ mean` **necessarily** —
the *sign* of the gap is forced — and the gap is small because `f_pp/f_nn = 1.518`
is close to 1.

**What this does NOT rescue.** #6346's objection is untouched: the complete graph
is not *expressible* in the 3A word, since a single generator joins only
consecutive nucleons (`StrandLayoutForcesChain`). So the all-pairs number is an
arithmetically faithful evaluation of a bond set the word cannot write. The
extrapolation is sound; what it extrapolates *to* is unrealised. That makes the
0.61–1.63× range **more** interesting than I said, and no more realised.

Probe: `computations/allpairs_extrapolation_fidelity_probe.py`.

One output defect of my own, fixed before commit: the identity check printed two
identical-looking 20-digit numbers followed by `identical: False`, because a bare
`==` at 50 dps catches rounding order. Replaced with the difference (1.3e-51) and
an explicit tolerance.
