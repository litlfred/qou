# The O(1) residual is the missing many-body (α-saturation) term — not a categorical constant

**Date:** 2026-07-11 · **Axis:** Δ_λ closure (strong sector), the O(1) residual ·
**Follows:** the A-scaling selection ([PR #3569](https://github.com/litlfred/qou/pull/3569)) ·
**Gate:** Track-A (owner-reversed) · **Tier:** measurement (reuses previous work) ·
**Formalize-first NEGATIVE; no fit; nothing wired.**

## Scope

#3569 selected `Δ_λ = sgn·dim` (classical q=1 dim) by A-stability, leaving a residual
`target/B(dim)` of **D 5.9, T 4.4, ³He 3.3, ⁴He 9.3** (spread 2.8×). The tempting next move is
to *fit* that residual with a per-nucleon / color / interface O(1). Per the Δ_λ gate — **"do
not propose a seventh fit-based ansatz"** — and formalize-first, this probe instead **prunes**
the "single O(1) constant" hypothesis and **re-identifies** the residual structurally, before
any fit.

Probe [`deltalambda_o1_manybody_probe.py`](../../computations/deltalambda/deltalambda_o1_manybody_probe.py)
→ [witness](../../computations/deltalambda/deltalambda-o1-manybody-residual.witness.json) (3/3).

## Three structural facts (parameter-free)

| # | Fact | Consequence |
|---|------|-------------|
| **A1** | `n_strands = 3A` exactly (D:6, T:9, ³He:9, ⁴He:12) | the **color triplet ×3 per nucleon is already in the braid** — not a free residual factor |
| **A2** | T and ³He share braid topology (`n_strands=9`, `n_partitions=30`) yet residuals differ **4.4 vs 3.3 (35%)** | the residual is **not a function of braid topology** — no single topological O(1) can close it |
| **A3** | `B(dim)` sub-linear (0.38, 1.91, 2.34, 3.04 MeV) vs `B_AME` super-linear (2.22, 8.48, 7.72, **28.30**); residual **maximal at doubly-magic ⁴He** | the residual tracks the **many-body α-saturation**, not an isotope-independent coefficient |

On A3 in detail: `B_AME/A` peaks at ⁴He (7.07 MeV, the α-particle) but `B(dim)/A` is flat
(~0.76, max at ³He, **not** ⁴He). The residual's maximum at ⁴He is precisely the α-particle's
cooperative-binding enhancement that a single trace cannot reproduce.

## What the residual actually is

A single Jones–Markov trace `tr_M(β_K)` is a **2-body-like** object. The α-particle binding is
a **4-body saturation** effect. So the residual "O(1)" is the **size of the missing higher
(many-body) term** — exactly the AGENTS.md principle:

> *"A compositional / additive / trace object is already many-body … the probe measures the
> size of the missing higher term, it does not exclude the factor."*

This is a **scope-(a)** finding (the single-trace magnitude undershoots), **not** scope-(b)
(nothing is excluded). The derived sign (#3542/#3558) and the A-selected power (#3569) stand;
what is missing is a *term*, not a *correction to the power*.

## The residual is a known-open problem, not a fudge factor

Deriving the residual = deriving the **operator-valued branching combiner** — the
**Subgoal-1 closure path already named** in
[`docs/precision-goals.md`](../precision-goals.md) ("per-isotope Borromean-tower extension +
operator-valued branching combiner"). So the O(1) is not a new free parameter to fit; it is the
already-identified many-body term. Fitting `[3–9]` to four nuclei would be the **seventh
ansatz** the Δ_λ gate forbids.

## Updated picture

`Δ_λ = sgn·dim` is the correct **per-partition** object (sign derived + cross-isotope-validated,
power A-selected). The per-isotope binding formula `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` is a
**single-trace (≈2-body)** object; closing the binding requires the **many-body combiner**, not
an O(1) rescaling of `Δ_λ`. **Nothing wired.**

## Cross-references

- A-scaling selection: [PR #3569](https://github.com/litlfred/qou/pull/3569)
- Sign derivation + cross-isotope validation: [PR #3542](https://github.com/litlfred/qou/pull/3542), [PR #3558](https://github.com/litlfred/qou/pull/3558)
- Subgoal-1 many-body closure path: [`docs/precision-goals.md`](../precision-goals.md)
- Reused: `atom-chi-rust-{d,t,3he,4he}.witness.json`, `wedderburn_jones_markov.y_lambda_at`
