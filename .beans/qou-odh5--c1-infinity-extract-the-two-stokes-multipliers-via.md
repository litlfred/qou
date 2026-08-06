---
# qou-odh5
title: 'C1 infinity: extract the TWO Stokes multipliers via q-Borel/theta resummation (leading blocks now known)'
status: todo
type: task
priority: high
created_at: 2026-08-06T23:30:00Z
updated_at: 2026-08-06T23:30:00Z
---

## Why this matters

The 1ppq L2 two-front survey names the `c₃` closure as the shared root of
**three of the five L2 misses** (Q_β, m_n, Δ_pn), and KC22 closed the entire
(q-)holonomic search — the object is in the Écalle acceleration class, so
**q-Borel / Stokes is the only surviving route**. This is that route's
concrete next step.

## What just landed (do not redo)

`computations/qbeta/c3_w2_c1_ramification_leading_blocks.py` + witness
`c3-w2-c1-ramification-leading-blocks.witness.json`, 3/3 assertions.

The `2026-08-01-c1-inf-slope-half-rsz-stokes.md` audit recorded
*"ramification: square roots `B₁,B₂` of the leading blocks — **open**
(compute the `A_i`)"*. That is now closed:

- `L₁ = (q²x−1)σ² − (q−1)σ − (q−1)`; at ∞ the valuation is `v = −deg`, and
  the lower hull is the single edge `(0,0) → (2,−1)`, **slope −½**.
- The nilpotency of `A(∞) = [[0,1],[0,0]]` that blocked the earlier script
  is not an obstacle to route around — it is exactly what a non-integral
  slope looks like in the companion frame.
- Ramifying with index `d = 2` (`x = z²`, `q = p²`, so `τF(z) = F(pz)`
  realises `σ` on functions of `z²`) moves the hull to `(0,0) → (2,−2)`,
  **slope −1, integral**. The `q^{1/2}` introduced here *is* the source of
  the "square roots".
- Edge polynomial `p⁴T² − (p²−1) = 0`, giving

      B₁,₂  =  ± √(q−1) / q

  distinct for `q ≠ 1`, hence two non-degenerate sectors — consistent with
  RSZ §3.3 `F(P₁,P₂) ≅ Matr_{1,1}(ℂ)² = ℂ²`, i.e. **exactly two Stokes
  multipliers**.

## The task

Extract the two multipliers `U ∈ ℂ²`. Ingredients now all present:

1. **Leading blocks** `B₁,₂ = ±√(q−1)/q` — landed above.
2. **q-Borel kernel** at level `d`: `t_{n+1} = qⁿ·tₙ`, Jacobi-theta
   coefficients — `QBorelKernel` formalized in Lean (`d = 1` case);
   the `d = 2` family is built from theta functions on the ramified cover.
3. **0-side canonical solution** — already CONFIRMED
   (`c3_w2_c1_module_exponents.py`: exponents = roots of `t²+(q−1)t+(q−1)`,
   discriminant `(q−1)(q−5)`).

Route: q-Borel transform the ramified operator at level `d = 2`, build the
two sector solutions from the theta kernel, and read the connection matrix
between them. The multipliers are the off-diagonal entries.

## Cross-check available

`qou-105e` (completed) verified the FW eq(73) `4₁` Stokes integer q-series =
divisor-function Lambert series with constant term `−1/4`. That is an
independent handle on Stokes data for `4₁` and should be used to sanity-check
whatever the C1 extraction produces, rather than treating the two as
unrelated.

`qou-0e66` (todo) proposes the complementary **diagrammatic** route
(McPhail–Snyder per-edge integer state-sum over crossings, worked for the
`5₂` Kashaev invariant). A state-sum plausibly *produces two numbers*; that
is only a sensible target now that the unknown is finite-dimensional.

## Discipline

- Anti-fit gated. A multiplier obtained by inverting `c₃` against its
  measured value is a **fit**, must be labelled one, and may not be wired.
- Report honest negatives. If the resummation shows the multipliers cannot
  supply the `c₃` bar-odd signature, that is a scope-(a) negative on this
  route and is worth as much as a closure.
- **Ownership:** the c₃/GGM front is flagged OWNED, "do not fork", in
  `docs/coordination/2026-07-17-1ppq-program-ownership-map.md`. Post intent
  and name the distinct angle before attacking; measured research overlap is
  permitted per AGENTS.md but must be deliberate and visible.
