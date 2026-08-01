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

### Route C — A=5/A=6 exact orders + μ̄_A sequence ✅ (compute + measured Lean defs)

_Witness:_ `computations/deltalambda/milnor_exact_coefficient_probe.py` →
`milnor-exact-coefficient.witness.json`. Lean measured section (§3 of
`MilnorExactCoefficient.lean`).

Brunnian iterated-commutator deficits `D_A = 1 − τ_A`, A ∈ {3,4,5,6}, computed in
**two** conventions from the same Hoefsmit χ_λ + Wenzl y_λ — the genuine cyclic
Markov trace `tr_M = Σ y_λ χ_λ` and the non-cyclic perblock `g = Σ y_λ|χ_λ|`
(#4364/#4378). On this Brunnian family the two **coincide** to machine precision.
Every word is Brunnian-verified (delete-strand → ≈1e-49).

| A | measured order (small-h slope) → exact | measured leading coeff μ̄_A (Richardson h→0) | vs `(3/4)(−2)^{A−3}` |
|---|-----------------------------------------|-----------------------------------------------|----------------------|
| 3 | 4.0005 → **4** | +0.7500000 | 3/4 (relerr 1e-8; **proved**, #4471) |
| 4 | 6.0005 → **6** | −1.4999996 | −3/2 (relerr 3e-7; measured) |
| 5 | 8.0005 → **8** | +2.9999985 | +3 (relerr 5e-7; **measured, new**) |
| 6 | 10.0005 → **10** | −5.9999954 | −6 (relerr 8e-7; **measured, new**) |

**A=5 order = 8 and A=6 order = 10 confirmed with nonzero leading coefficient** —
turning #4471's two exact-order data points (A=3 proved, A=4 measured) into **four**.

**Extracted μ̄_A sequence:** `μ̄_A = (3/4)·(−2)^{A−3}` — consecutive ratio **exactly
−2**, magnitude `3·2^{A−5}`, sign `(−1)^{A−1}` (matching #4389's Milnor-parity sign
law). This is a *measured candidate* for the trace-normalised leading coefficient;
the identification with the genuine Milnor invariant μ̄(12…A) = ±1 (Route A) is
open. Lean records it as `mubarMeasured` with proved arithmetic facts
(`_ratio` = −2, `_ne_zero`, `_sign_odd`) — **not** as a proof of the exact law and
**not** an instance of `MilnorExactOrderConjecture`.

### The 1.585× bridge — definitive NO

The A=3 magnitude bracketing (#4364/#4376/#4392/#4472) flagged a missing `1.585×`
(≈ log₂3) structure. The μ̄_A leading-coefficient sequence has consecutive ratio
**exactly −2**; no ratio, magnitude, reciprocal, or log combination of the μ̄_A
lands within 0.05 of 1.585 (checked both conventions). **μ̄_A does NOT encode the
1.585× magnitude structure.** Reported with zero fitting. So the order-law leading
coefficient is a *clean, self-contained* object (ratio −2) that is **not** the
bridge to the A=3 magnitude anomaly — the missing magnitude structure lives
elsewhere.

## Verdict

- **Route B:** honest **PROVED trace-cyclicity sub-wall** — the leading coefficient
  is not extractable from #4471's Lie tower via a cyclic trace. The exact order law
  stays open; the coefficient requires group-commutator / finite-type (Milnor)
  theory (Route A, Mathlib-inaccessible, cited).
- **Route C:** A=5/A=6 exact orders (8, 10) proved-by-measurement; μ̄_A sequence
  = (3/4)(−2)^{A−3} extracted; **4 data points** now (was 2).
- **Bridge:** μ̄_A does **not** encode 1.585× (ratio is −2). Clean negative.
- **Route A:** cited (Bar-Natan; Habegger–Masbaum; Meilhan–Yasuhara), never
  axiomatised.

## Anti-fit / honesty ledger

- 0 free parameters. Nothing wired to production.
- No instance of `MilnorExactOrderConjecture` created (the exact law is open).
- μ̄_A **extracted**, never fit to 1.585×; the 1.585× check is an honest NO.
- A=5/A=6 orders + μ̄_A recorded as **measured** `def`s (not theorems asserting the
  exact law), matching #4471's `tauL4MeasuredOrder` discipline.
