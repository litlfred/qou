# The b-decay terminates at an EXACT zero (the sign rep), not an asymptote (qou-o6ov)

**Date:** 2026-08-31
**Directive (owner):** go (continue the Garoufalidis–Le / loop-expansion bridge).
**Scope:** scope-(a); no MeV, no fit, nothing wired.
**Lean:** `QOU.MassTheory.trace_rho_commutatorSum_eq_zero_of_commute` (sorry-free)
**Probe:** [`magnus_extreme_rep_endpoint_probe.py`](../../computations/deltalambda/magnus_extreme_rep_endpoint_probe.py)

## The observation every prior probe missed

The whole arc (#6311→#6372) studies the decay of `tr(ρ_λ ⁅A_a,A_{a+1}⁆)` as `b(λ)=n−λ_1`
grows. Every probe skipped `dim ≤ 1` partitions — so none of them looked at the **endpoint**.
But the two extreme partitions are one-dimensional:

| λ | rep | dim | b |
|---|---|---|---|
| `(n)` | trivial (each `σ_i = q`) | 1 | 0 |
| `(1ⁿ)` | **sign** (each `σ_i = −q⁻¹`) | 1 | **n−1 (maximal)** |

In any 1-dimensional rep the algebra is **commutative**, so `⁅A_a,A_{a+1}⁆ = 0`, hence
`tr(ρ_λ Ω₂) = 0` **exactly**. Confirmed numerically (A=1,2,3, exact mpf): both endpoints give
`0.0` to full precision.

**So the `b`-decay does not approach a mysterious asymptote — it terminates at a PROVABLE
zero** at the fully-antisymmetric (sign-rep) endpoint. The near-endpoint approach is visible in
the smallest high-`b` reps (A=3, `b=7`: `|tr|/dim` = 0.075–0.21).

## Rigorous (Lean, sorry-free)

`trace_rho_commutatorSum_eq_zero_of_commute`: if the germs pairwise commute
(`Commute (A k) (B k)` for every adjacent pair — automatic in any 1-dim/commutative rep), then
`Σ_k ⁅A_k,B_k⁆ = 0`, so `tr(ρ · Ω₂) = 0` for every word `ρ`, general `CommRing`. The sign-rep
and trivial-rep zeros are instances. This makes the endpoint an exact theorem, not a
measurement.

## Why this grounds the Garoufalidis–Le bridge (#6372)

Under **Schur–Weyl duality**, the `b`-grading of Hecke `H_n(q)` irreps is dual to a `U_q(gl_N)`
rep grading, and the sign rep `(1ⁿ)` is the **fully-antisymmetric / determinant** sector — the
same corner that hosts the **Alexander polynomial** in the Melvin–Morton–Rozansky loop
expansion. So the decay's endpoint sits precisely in the semiclassical/Alexander corner that
the arc-graph zeta reformulation (#6372) points to. This is **suggestive, not established**: the
Schur–Weyl identification of "sign-rep endpoint" with "Alexander sector of the color-`n` loop
expansion" is exactly the grading-bridge #6372 flagged as the open crux — this note shows the
*endpoint* lands there, it does not build the bridge.

## What is rigorous vs suggestive

- **Rigorous:** `tr(ρ_λ Ω₂) = 0` at both 1-dim reps (Lean, sorry-free); the maximal-`b` endpoint
  of the decay is an exact zero by commutativity. The decay terminates, it does not merely
  shrink.
- **Suggestive:** the sign rep is the antisymmetric/Alexander corner under Schur–Weyl, so the
  endpoint is the semiclassical anchor of the loop expansion. Consistent with #6372's framing;
  not proven to be the same object.
- **Still open:** the *rate* of the decay toward this endpoint (the actual theorem), and the
  Schur–Weyl grading bridge.

## Bottom line

The `b`-decay of `tr(ρ_λ Ω₂)` has a **provable exact-zero endpoint** at the sign rep `(1ⁿ)`
(and at the trivial rep `(n)`) — a `Commute ⇒ Ω₂=0` theorem now in Lean, sorry-free. This
anchors the decay at the fully-antisymmetric/Alexander corner that the Garoufalidis–Le loop
expansion points to, turning the arc's endpoint from a numerical tail into a structural
boundary condition. The rate, and the Schur–Weyl bridge to the color-`n` loop expansion, stay
open.
