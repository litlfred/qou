---
# qou-212w
title: 'T1: q-adic order of the n=4 interleaving cross term z(z^2-hz-1) at convention D — exact in Q(q), no float'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T20:20:46Z
updated_at: 2026-09-05T20:29:59Z
parent: qou-2akx
---

## 2026-09-05 — MEASURED: answer NO, and the order-zero term is a component count

Probe computations/probes/interleaving_cross_term_q_adic_order_probe.py (exact sympy, 15/15, witness proton). At convention D:
S = q^3(q^4+1)^2/(q^2+1)^3, I = q^5(q^6+q^2-1)/(q^2+1)^3, Δ = -q^3 Φ3 Φ6 / Φ4^3.
ν_(q-1)(S) = ν(I) = ν(Δ) = 0; S(1)=1/2, I(1)=1/8, Δ(1)=-3/8.
At q=1, z=1/2 the trace is 2^(c(w)-4), c = cycles = closure components: interleaved word closes to a knot (c=1), sequential to a 3-component link (c=3). So the cross term at order zero = difference of component counts — classical word topology (matches §7b attribution).
ℏ-series (ℏ=1-1/q) exact to order 8, radius √2 (poles q=±i). Proton pin: order-0 term carries 81.3 % of Δ(q0)=-0.46117; extra nats 0.895 vs classical 2 ln 2 = 1.386 (deformation REDUCES the classical cross term).
Habiro half: normalised traces have a triple pole at Φ4 (the tr(1)=1 normalisation, [2]_q^4); unnormalised [2]_q^4 Δ = -(q^6+2q^4+2q^2+1)/q is a Laurent polynomial, simple zeros at Φ3, Φ4, Φ6, value -6 at q=1, order 0.
CONSEQUENCE (judgement): route B's claim on b3 WEAKENED per the test's own criterion; routes A, C move up. Scope (a): one word pair, convention D. Doc §7c.
