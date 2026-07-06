# Route α decided: the basic-construction lift is trace-transparent (c₄-content ≡ 0)

**Date:** 2026-07-02
**Bean:** `1jrh` / Stage C. Executes step 1–2 of the decision structure in
[`2026-07-02-1jrh-lambda-derivation-routes.md`](../scope/2026-07-02-1jrh-lambda-derivation-routes.md)
(PR #3232) using the merged H₄ Markov-trace infra
([`2026-07-02-1jrh-h4-stagec-markov-infra.md`](2026-07-02-1jrh-h4-stagec-markov-infra.md), PR #3228).
**Probe:** [`computations/qbeta/qbeta_route_alpha_lift_prediction.py`](../../computations/qbeta/qbeta_route_alpha_lift_prediction.py)
→ `qbeta-route-alpha-lift-prediction.witness.json` (50 dps, 1.1 s; auditOnly).

## What was evaluated

The fully forced route-α candidate — zero free parameters, no enumeration:

    Λ_α = ι(ΔT)·e₃,   e₃ = (q·1 − σ₃)/(q + q⁻¹)

with ΔT the free-neutron-decay net transition operator (6-word H₃ NF basis,
exact symbolic coefficients from `free-neutron-decay.witness.json`; Gate 0
revalidates Δ(net) ≈ −0.18829062 against the witness) and e₃ the
Temperley–Lieb/Jones projector generating the basic construction for H₃ ⊂ H₄.

## Measurements (all exact laws or direct evaluations; no fit anywhere)

| # | measurement | result |
|---|---|---|
| P1 | ζ_w = tr_M^(H₄)(w·σ₃)/tr_M^(H₃)(w) across all 6 NF words, at proton q₀ + muon q₀ + 3 extra q-points | **word-independent to ≤ 1.1e-50** — the Markov property holds on the third strand; ζ(q₀) ≈ 0.49932033 |
| P2 | level-4 content L4 = tr_M^(H₄)(Λ_α) − τ(e₃)·tr_M^(H₃)(ΔT), τ(e₃) = (q−ζ)/(q+q⁻¹) | **≈ ±8.4e-53 at BOTH anchors** (opposite signs — pure roundoff): exactly zero |

tr_M^(H₄)(Λ_α) ≈ −0.03579931 at both anchors equals τ(e₃)·tr_M^(H₃)(ΔT)
to 5e-53 — the lift's H₄ trace factors completely through its H₃ shadow.

## Verdict — route α predicts c₄-content = 0, by structure

The Markov property (P1) makes this exact, not numerical: for any x ∈ H₃,

    tr_M^(H₄)(ι(x)·e₃) = [(q − ζ)/(q + q⁻¹)]·tr_M^(H₃)(x) = τ(e₃)·tr_M^(H₃)(x),

so e₃-dressing is **invisible to the Markov trace** — the basic-construction
lift adds zero level-4 trace content for *every* decay operator, at *every*
q. The L3 anchor-stability gate passes trivially (0 at both anchors).

**Scope-(a) statement (per the refutation discipline):** the
basic-construction lift Λ_α, *alone*, contributes no c₄ rung — its ladder
truncates at the H₃ content. This does **not** exclude e₃ as an ingredient
of a larger closure; it is the exact size-zero measurement of the α term.

**Structural consequence (the sharp fork the routes doc anticipated):** any
genuinely nonzero c₄ rung requires a **non-trivial defect coupling** to the
new strand — i.e. routes β (brane-tower kernel R(q,ξ)) or γ (color-tube
W_c₁c₂), both keystone-gated. Equivalently: within Stage C the surviving Λ
candidates are exactly the ones that *break* the conditional-expectation
factorization (L5 must hold only on the decay content, not on the trace).

## Feed into the 1jrh Casoratian test

With c₄(Λ_α) = 0 exactly, the α-route W₃ Casoratian degenerates (a zero
column) — the W₃ sign test is **not fed by route α**; it stays gated on a
β/γ-derived c₄, as the routes doc's "unstable" branch anticipated (here
obtained by exact vanishing rather than anchor-instability). The bean's
decision state is unchanged except that α is now *decided*, cheaply and
exactly, leaving β/γ as the sole live suppliers of a c₄ rung.

## Discipline

Zero free parameters; both q₀ anchors evaluated (proton `q_at`, muon
`q_muon_at`); no candidate enumeration; no target back-solving. The verdict
is a prediction outcome (c₄ = 0 on route α), recorded scope-(a).
