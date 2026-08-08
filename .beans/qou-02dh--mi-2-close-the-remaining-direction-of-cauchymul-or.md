---
# qou-02dh
title: 'MI-2: close the remaining >= direction of cauchyMul_order (Laplace term selection under positivity)'
status: completed
type: task
created_at: 2026-08-08T17:05:00Z
updated_at: 2026-08-08T17:05:00Z
---

Branch: `claude/sorry-audit-joo5` (qou).
File: `content/quantum-observable-universe/lean/QOU/Mathlib/QGevreyOrder.lean`.

Follows qou-0z7n, which restated `cauchyMul_order` truthfully (positive real
coefficients) and proved its `≤` half. This closes the other half, so the
declaration becomes `sorry`-free.

## The idea

The `≤` half is an upper bound on a sum of norms, so the triangle inequality
carries it and no positivity is needed. The `≥` half is where positivity is
load-bearing: every summand of `(a ⋆ b)_n = ∑_{k≤n} a_k b_{n−k}` is positive, so
the sum **dominates each individual term**, and it suffices to name the term at
the maximiser of `θ ↦ sθ² + t(1−θ)²`.

That turns the Laplace/saddle argument into a composition of limits. Along
`kₙ = ⌊θn⌋`:

    2·log_q(a_{kₙ}·b_{n−kₙ}) / n²
      = (2·log_q a_{kₙ}/kₙ²)·(kₙ/n)² + (2·log_q b_{n−kₙ}/(n−kₙ)²)·((n−kₙ)/n)²
      → s·θ² + t·(1−θ)².

The maximiser comes straight off `cauchyEnvelope`'s closed form: an endpoint
`θ ∈ {0,1}` in the convex (`max`) branch, `θ = t/(s+t)` in the concave branch
(where `sθ² + t(1−θ)² = st/(s+t)` exactly). Degenerate concave sub-cases
(`s = 0`, `t = 0`, `s+t = 0`) all have envelope `0` and are served by an endpoint
choice — so no `θ` outside `[0,1]` is formed and `s+t = 0` is never divided by.

## Todo

- [x] `isQGevreyOrder_pos` — drop the norm for positive real sequences
- [x] `cauchyMul_pos`, `term_le_cauchyMul` — positivity and term domination
- [x] `tendsto_logb_const` — a frozen index contributes 0 (the endpoint cases)
- [x] `tendsto_logb_comp` — reindex along `uₙ → ∞` with `uₙ/n → c`, giving `s·c²`
- [x] `tendsto_term` — the two contributions add (`log` of the product)
- [x] `term_coeff_le`, `cauchyMul_coeff_le` — the two squeeze bounds
- [x] `cauchyMul_order` — case split + `tendsto_order` glue
- [x] build green, axioms `[propext, Classical.choice, Quot.sound]`
- [x] update the file's scope notes (three places still say the `≥` half is open)

## Mathlib pieces that made it cheap

`tendsto_nat_floor_mul_div_atTop` (⌊θx⌋/x → θ), `tendsto_natCast_atTop_iff`,
`tendsto_nat_floor_atTop`, `Tendsto.const_mul_atTop`, `Tendsto.div_atTop`,
`tendsto_order`.

## Summary of Changes

`cauchyMul_order` is proved. `QOU/Mathlib/QGevreyOrder.lean` now has **zero
`sorry`s** — MI-1, MI-2, MI-3 and MI-4 are all discharged.

`#print axioms cauchyMul_order` → `[propext, Classical.choice, Quot.sound]`.

New in MI-4: `isQGevreyOrder_pos`, `cauchyMul_pos`, `term_le_cauchyMul`,
`tendsto_logb_const`, `tendsto_logb_comp`, `tendsto_term`, `term_coeff_le`,
`cauchyMul_coeff_le`. Three stale scope notes (file header, MI-2 SCOPE block,
MI-3(c) docstring) rewritten — they all still described the `≥` half as cited.
