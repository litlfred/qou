# Δ_λ / Milnor exact-order coefficient — Route B (trace-cyclicity sub-wall) + Route C (A=5/A=6)

**Date:** 2026-08-01
**Branch:** `claude/deltalambda-milnor-exact-coefficient-2026-08-01`
**Predecessor:** #4471 (`MilnorOrderLawGeneral`, all-A order **lower bound**
`order(D_A) ≥ 2(A−1)`, sorry-free; `MilnorExactOrderConjecture` instance-less).

## Objective

Upgrade #4471's lower bound toward the **exact** order law `order(D_A) = 2(A−1)`
— equivalently the length-A Milnor invariant μ̄(12…A) ≠ 0 (nonzero **leading
coefficient** of the deficit `D_A(h) = 1 − τ_A(h)`, `h = q − q⁻¹`).

- **Route B** — inductive leading-coefficient tracking through the commutator
  recursion. Attempt sorry-free; honest sub-wall if the trace-cyclicity
  obstruction blocks it.
- **Route C** — explicit A=5, A=6 exact orders + extraction of the μ̄_A sequence;
  check whether μ̄_A encodes the 1.585× "missing structure" from the A=3
  magnitude bracketing (#4364/#4376/#4392/#4472).
- **Route A** — the Milnor = leading-Vassiliev bridge (Bar-Natan;
  Habegger–Masbaum; Meilhan–Yasuhara). Mathlib lacks finite-type theory ⇒ CITED
  only, never axiomatised as proved.

## Status: WIP (this is the living audit; results below are filled as they land)

### Route B — PROVED NEGATIVE (trace-cyclicity sub-wall)

_Lean:_ `content/quantum-observable-universe/lean/QOU/MassTheory/MilnorExactCoefficient.lean`
(lean-direct exit 0, sorry-free).

The result is an **honest, proved sub-wall**, not a proof of the exact law:

- `cyclic_trace_kills_iterCommTower`: for every cyclic Markov trace `τ` and every
  `n`, `τ(iterCommTower c (n+1)) = 0`. #4471's order engine is the **Lie**
  (ring) iterated-commutator tower; a cyclic trace annihilates every ring
  commutator, so it kills the whole top level of the tower.
- `leading_coefficient_witness_is_uninformative`: #4471's `HasOrder.trace`
  witness `τ(V n) = h^k·s` holds with `s = 0` for a cyclic trace — the h-adic
  divisibility is achieved by the zero element and constrains the leading
  coefficient not at all.
- `cyclic_trace_group_commutator_rearrange`: the positive contrast — the
  **group** commutator `g·h·g⁻¹·h⁻¹` only cyclically rearranges under `τ`, it does
  **not** collapse to `τ(1)`. This is where the nonzero order-`2(A−1)` coefficient
  (the Milnor content) lives.

**Consequence:** the exact law's leading coefficient μ̄_A is provably **not**
recoverable from #4471's Lie-tower infrastructure by applying the (cyclic) Markov
trace. Route B, as "track γ_A through the Lie recursion and apply τ", is
trace-annihilated. The nonzero coefficient requires the **group**-commutator /
finite-type (Milnor / Vassiliev) structure — Route A, which Mathlib cannot
express. So the exact law stays open (`MilnorExactOrderConjecture`, no instance);
no instance is fabricated.

### Route C — A=5/A=6 exact orders + μ̄_A sequence (compute)

_Witness:_ `computations/deltalambda/milnor_exact_coefficient_probe.py` →
`milnor-exact-coefficient.witness.json` (filled below once run).

TBD — leading orders, leading coefficients μ̄_A for A ∈ {3,4,5,6}, and the 1.585×
check.

## Anti-fit / honesty ledger

- 0 free parameters. Nothing wired to production.
- No instance of `MilnorExactOrderConjecture` is created (the exact law is open).
- μ̄_A is **extracted**, never fit to 1.585×; the 1.585× check reports an honest
  yes/no with no tuning.
