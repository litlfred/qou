---
# qou-s39m
title: 'conj:crossing-graded-mass-expansion: xi -> +inf in the classical limit; the block is wrong as written'
status: in-progress
pr: 8187
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T13:45:00Z
updated_at: 2026-11-16T20:22:00Z
parent: qou-wp3h
---

**Scope-(a).** This is about the STATEMENT of one conjecture block. It refutes
NO ingredient: not Bloch-Wigner `D`, not the shape parameter `z_q`, not the
crossing grading, not the ideal-tetrahedron machinery. Nothing is wired to
production and `computations/canonical_mass.py` does not use `xi` at all.

## The defect

[`crossing-graded-mass-expansion.md`](../folio/quantum-observable-universe/mass-theory/crossing-graded-mass-expansion.md)
defines the depth scalar `xi(q) = D(z_q)/hbar_q^2` and closes with:

> "Taking the classical limit `xi -> 0` recovers the baseline Groebner-Shirshov
> reduction."

plus the locality corollary `m = m_GB * (1 + xi)^c`. But `hbar_q = 1 - 1/q`, so
the classical limit is `q -> 1`, where `hbar_q^2 -> 0`. For `xi -> 0` you would
need `D(z_q) -> 0` at least as fast. **It does not** — see the exact fact below.
So `xi -> +infinity` in the very limit the block calls classical. The block
cannot be correct as written.

## The exact fact (anchor-free)

At `q = 1` the Descartes cubic factors over Q:

    27x^3 + 18x + 20 = (3x + 2)(9x^2 - 6x + 10)

roots exactly `-2/3` and `1/3 +- i` — one real, one conjugate pair. So `z_1` is
non-real, the ideal tetrahedron at `z_1` is non-degenerate, and `D(z_1)` is a
nonzero constant. Ordering `(-2/3, 1/3-i, 1/3+i)` gives

    z_1 = (1+i)/(1-i) = i      EXACTLY

the regular ideal octahedron, so `D(z_1) = Catalan G = Vol(B_3)/8`, and
`xi = D/hbar_q^2 -> G/0+ = +infinity`.

This is exact rational arithmetic with **no anchor**, so the conclusion does not
depend on any measured input.

## Three readings — the owner's call, not an agent's

  (R1) The sentence is wrong and the expansion is simply not perturbative.
  (R2) `xi` was meant as `D * hbar_q^2`, which DOES tend to 0 (`= 8.98e-3` at
       the proton anchor) and is consistent with the classical-limit sentence.
  (R3) `z_q` denotes a third object whose `D` vanishes as `q -> 1`.

All three survive. What is removed is the possibility that the block is fine as
written. **Do not pick one and edit the block on an agent's own authority** —
`xi` is the block's central construct and (R2) would change every downstream
formula in it.

## Evidence

  * [`computations/qbeta/xi_classical_limit_probe.py`](../computations/qbeta/xi_classical_limit_probe.py)
    — the limit table + `q1_exact()`, which machine-checks the factorisation
    over `fractions.Fraction`. PR #4769.
  * [`computations/qbeta/descartes_lambda_shape_upper_half_plane.py`](../computations/qbeta/descartes_lambda_shape_upper_half_plane.py)
    — the sibling probe (PR #4744, merged `23a0d5f8`) that first flagged
    `xi = 93.2` at the anchor as OBSERVATION 2.

## History

PR #4744 flagged this from the single anchor value `xi = 93.2 >> 1`. That is
weak on its own — a quantity can be large at `q_0` and still tend to 0 in the
named limit — so the finding was strengthened to the limit itself in PR #4769,
which is the claim the block actually makes.

## Progress 2026-11-16 (PR #8187)

- [x] Added `descartes_cubic_at_q_one_factorization`, `descartes_quadratic_factor_complete_sq`, `descartes_cubic_eval_neg_two_thirds`, `descartes_cross_ratio_eq_I_coords`, `xi_product_at_zero_hbar`, and `xi_ne_zero_of_mul_hbar_sq_eq` in `folio/quantum-observable-universe/mass-theory/crossing-graded-mass-expansion.lean` + 80-dps `mpmath` probe (`litlfred/qou#8187`, `28237151a70df9ecb11495b374e141771a7b4a76`).
- [ ] Await review and merge of `litlfred/qou#8187`.
