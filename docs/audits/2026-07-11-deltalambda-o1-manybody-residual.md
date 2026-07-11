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

## This is already decomposed in the corpus — not a fresh open direction

A corpus-grep (per the STRICT "before declaring open" checklist) shows the many-body deficit
is **already quantified**, far more finely than this per-isotope residual:

- [`pairwise_magnitude_gap_probe.py`](../../computations/probes/pairwise_magnitude_gap_probe.py)
  (PR #2630): the **leading/pairwise trace** — the same single-trace object as `B(dim)` here —
  **underbinds ~40% at A=3**, decomposed per-bond.
- [`b4-framework-connected-cumulant-deficit.witness.json`](../../computations/probes/b4-framework-connected-cumulant-deficit.witness.json):
  the connected (Ursell/Mayer) cumulants are measured — **b₄ = 0.58 MeV = 6.3%** of the
  9.24 MeV four-body target, with **b₃ wrong-signed** — and the missing piece is named: the
  **[1⁴] Slater term** (`Λ^A(4)` nucleon-flavor), pending the **Slater↔trace dictionary**.

So the residual found here (`target/B(dim)`, maximal at ⁴He) is the **coarse per-isotope shadow
of this already-decomposed connected-cumulant deficit** — the same missing higher term, seen at
the crude "one O(1) per nucleus" resolution instead of the b₃/b₄ cumulant resolution. It is
**consistent** (single trace ≈ leading/pairwise, undershoots; deficit grows with body-order and
peaks at the 4-body α) and adds nothing the cumulant line hasn't already quantified — its only
value is to confirm, from the #3569 Δ_λ side, that the gap is a *term*, not a *power/coefficient*.

The definitive statement is already in
[`docs/audits/2026-07-05-delta-lambda-gate-status.md`](2026-07-05-delta-lambda-gate-status.md):
the **×5.10 ⁴He magnitude gap is a missing ≥4-body, ⁴He-LOCAL term — "not a weight, not
sign-fixable."** Two points from that audit that this residual must respect:

- The ⁴He peak is **not** `∝ C(4,A)` (which peaks at A=2). The **Wigner SU(4) `[1^A]`
  supermultiplet gate** (`QOU.MassTheory.SU4SupermultipletGate`, **sorry-free**: `dim[1^A]=C(4,A)`,
  `=0` iff `A>4`) supplies the **A>4 *cutoff*** — it turns the term *off* above the closed α
  shell — while the peak *at* ⁴He is the α being maximally bound (measured super-pairwise excess
  2.093× at ⁴He, 0.944× at ⁶Li). My residual's ⁴He maximum is the per-isotope echo of that
  measured locality, **not** an independent claim that the enhancement scales as `C(4,A)`.
- The gap is closed only by the **connected `[1⁴]` ≥4-body magnitude term** (Option-E PROBE 2)
  or the geometric `W_λ` build — both **research-level and gated**, not a fit. Fitting `[3–9]`
  to four nuclei would be the **seventh ansatz** the Δ_λ gate forbids.

## Updated picture

`Δ_λ = sgn·dim` is the correct **per-partition** object (sign derived + cross-isotope-validated,
power A-selected). The per-isotope binding formula `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` is a
**single-trace (≈2-body)** object; closing the binding requires the **many-body combiner**, not
an O(1) rescaling of `Δ_λ`. **Nothing wired.**

## Honest status of this thread

This residual analysis **re-derives, at coarse per-isotope resolution, what the corpus already
establishes** (the ×5.10 ⁴He-local ≥4-body gap, the b₃/b₄ cumulant deficit, the SU(4) `[1⁴]`
gate + measured locality). Its contribution is narrow: it confirms **from the #3569 `Δ_λ` side**
that the #3569 residual is that same missing term — a *term*, not a coefficient — so the
`Δ_λ = sgn·dim` result is complete as a per-partition object and needs no O(1) fudge. The genuine
open problem is unchanged and **research-level**: the connected `[1⁴]` PROBE 2 magnitude leg
concludes **PARTIAL** — its A>4 vanishing is clean (SU(4) gate `C(4,6)=0`), but the ⁴He magnitude
"6% agreement" is **units-mismatched** (a dimensionless Mayer sum vs a binding-ratio, with a
Σg-normalization hidden DOF, Rule 14) — *not* a derivation. The crux is the **Slater↔trace
dictionary** that would make the `[1⁴]` Mayer magnitude commensurable with the binding-ratio
excess, or the geometric `W_λ` build. No new probe is warranted here — that would re-walk
anchored ground.

## Cross-references

- A-scaling selection: [PR #3569](https://github.com/litlfred/qou/pull/3569)
- Sign derivation + cross-isotope validation: [PR #3542](https://github.com/litlfred/qou/pull/3542), [PR #3558](https://github.com/litlfred/qou/pull/3558)
- **Already-quantified connected-cumulant deficit** (this residual's fine-grained form):
  [`pairwise_magnitude_gap_probe.py`](../../computations/probes/pairwise_magnitude_gap_probe.py) (PR #2630),
  [`b4-framework-connected-cumulant-deficit.witness.json`](../../computations/probes/b4-framework-connected-cumulant-deficit.witness.json)
- Subgoal-1 many-body closure path: [`docs/precision-goals.md`](../precision-goals.md);
  combiner: [`canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py),
  [`operator-valued-combiner-convergence.md`](../../content/quantum-observable-universe/mass-theory/operator-valued-combiner-convergence.md)
- Reused: `atom-chi-rust-{d,t,3he,4he}.witness.json`, `wedderburn_jones_markov.y_lambda_at`
