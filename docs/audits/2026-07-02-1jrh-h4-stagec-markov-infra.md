# Stage-C instrumented base: the H₄ Markov trace wired + gated (no Λ evaluated)

**Date:** 2026-07-02
**Bean:** `1jrh` (c₄ rungs gate the Casoratian W₃ sign test) — the
infrastructure half of Stage C per
[`docs/scope/2026-06-18-qbeta-c4-h4-tower-stage-c-scope.md`](../scope/2026-06-18-qbeta-c4-h4-tower-stage-c-scope.md) §3.
**Probe:** [`computations/habiro/qbeta_h4_stagec_markov_infra.py`](../../computations/habiro/qbeta_h4_stagec_markov_infra.py)
→ `qbeta-h4-stagec-markov-infra.witness.json` (50 dps, 0.7 s; auditOnly).

## What is now wired

`tr_M^{H₄}(W) = Σ_{λ⊢4} y_λ·χ^λ(W)` as a single callable accepting **any**
H₄ braid word — including σ₃-involving words — assembled from the two
already-validated corpus pieces: `young_seminormal.seminormal_sigma` (λ⊢4
reps, preflight-validated to 1e-40) and `y_lambda_wenzl_bridge_numeric`
(Wenzl weights, any n). **No σ₃-lift candidate is enumerated or evaluated**
— the scope's no-fit rule; the categorical Λ stays the sole open Stage-C item.

## Gates (all exact laws, no fitting — ALL PASS)

| gate | law | worst deviation |
|---|---|---|
| A | Hecke on characters: `χ(σ_i²) = h·χ(σ_i) + χ(1)`, all λ⊢4, i = 1..3 | 5.4e-51 |
| B | Markov generator-uniformity `tr_M(σ₁) = tr_M(σ₂) = tr_M(σ₃)` (exercises the new strand) | 0.0 |
| C | H₃→H₄ stabilization ratio `tr_M^{H₄}(ιw)/tr_M^{H₃}(w)` word-independent across the 6 decay-NF words + 3 extras, at **5 q-points** | 1.1e-50 |
| D | branching cross-check: direct λ⊢4 trace ≡ `Σ_μ y_μ Σ_{λ↗μ} χ^λ` (H₃ characters only) | 0.0 |

## Finding — the stabilization constant is exactly 1

In the Wenzl normalization the C12 ratio is **1.0** (to 1e-50, 5 q-points):
`tr_M^{H₄}(ιw) = tr_M^{H₃}(w)` on σ₃-free words. Consequence for Stage C:
the level-4 content of any candidate lift `Λ` reads **directly** as
`tr_M^{H₄}(Λ) − tr_M^{H₃}(Λ's H₃ shadow)` — no normalization constant to
carry. Combined with the preflight's σ₃-gating (σ₃-free ⇒ zero new DOF),
the pipeline isolates exactly the quantity the c₄ rung lives in.

## What remains open (unchanged)

The **categorical specification of Λ** — which length-4 σ₃-involving element
of H₄(q) is the lift of the decay operator ΔT — per the scope's §2 rules:
derived from the decay categorical content (confinement defect / brane-tower
N→N+1 map), anchor-stable, bar-even-respecting; **never** back-solved from a
c₄ target. Once specified, its evaluation here is one call, and the 1jrh
Casoratian W₃ sign test follows from the resulting c₄^even (plus a c₄^odd
beyond the CAL-anchored tier).
