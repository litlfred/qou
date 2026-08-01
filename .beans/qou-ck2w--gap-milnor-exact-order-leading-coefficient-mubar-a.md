---
# qou-ck2w
title: 'GAP: Milnor exact-order leading coefficient mubar_A != 0 (exact law order(D_A)=2(A-1)) is OPEN'
status: todo
type: task
created_at: 2026-08-01T19:16:41Z
updated_at: 2026-08-01T19:16:41Z
---


## What is open

The EXACT Milnor order law `order(D_A) = 2(A−1)` for the A-component Brunnian
trace deficit `D_A = 1 − τ_A` — equivalently the length-A Milnor invariant
μ̄(12…A) ≠ 0 (nonzero leading coefficient). #4471 proved only the **lower bound**
`order ≥ 2(A−1)` and left this as `MilnorExactOrderConjecture` (instance-less).

## What was tried (#4480, 2026-08-01)

- **Route B (inductive leading-coefficient tracking) — PROVED SUB-WALL.** #4471's
  order engine `iterCommTower` is a *Lie* (ring) commutator; any cyclic Markov
  trace kills it (`cyclic_trace_kills_iterCommTower`, sorry-free in
  `MilnorExactCoefficient.lean`). So the leading coefficient is provably NOT
  extractable from the Lie tower via the trace — Route B as stated is dead.
- **Route C (compute) — 4 data points.** Measured μ̄_A = (3/4)(−2)^{A−3} =
  {3/4,−3/2,3,−6} for A=3..6, orders exactly 2(A−1). Clean but MEASURED, not
  derived. The (−2)^{A−3} is the trace normalization; the true Milnor part is ±1.

## Surviving route (Route A — needs machinery Lean lacks)

The exact law = the Milnor = leading-Vassiliev-invariant bridge (Bar-Natan;
Habegger–Masbaum; Meilhan–Yasuhara): the first non-vanishing Vassiliev invariant
of the Jones trace at degree 2(A−1) is ±μ̄(12…A) = ±1. **Mathlib has no
finite-type / Vassiliev theory.** Next honest step: either (i) formalize enough
finite-type invariant theory to state μ̄(12…A) = ±1 (large), or (ii) derive the
measured closed form μ̄_A = (3/4)(−2)^{A−3} symbolically (exact Markov trace of
w_A in q; sympy Hoefsmit) and PROVE the A=5/A=6 tight slices like #4471's
`borromean_tight_slice` — that upgrades "measured" to "proved" per A but does not
give the all-A law.

Do NOT fabricate a `MilnorExactOrderConjecture` instance.
