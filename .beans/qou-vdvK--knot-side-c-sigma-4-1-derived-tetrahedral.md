---
# qou-vdvK
title: 'The knot side: c_sigma(4_1) = 3^{-1/4} derived, and k = 2^{-1/2} forced by the saddle'
status: completed
type: task
priority: high
tags:
    - one-loop
    - c-sigma
    - adjoint-torsion
    - figure-eight
    - kashaev-invariant
    - saddle-point
created_at: 2026-08-08T19:20:00Z
updated_at: 2026-08-08T19:20:00Z
---

## The ask

`qou-vdvS` closed the LINK side and left this explicitly open: "a b=1 Whitehead
chain has c+d+1 >= 2 components, so nothing above derives c_sigma(4_1) =
3^{-1/4}, and the one-cusped leg still rests on Garoufalidis-Yoon together with
the 4_1 calibration."

## Resolution

Done, and it did not need van der Veen. It needed the observation of WHY his
computation closed: his critical point sits at `(pi/2, pi/4)`, a RATIONAL point,
because those complements are glued from regular ideal OCTAHEDRA. Nothing else
in the argument cares which link it is.

`4_1` is two regular ideal TETRAHEDRA, and Kashaev's invariant is a
one-variable sum in the same `s_k`:

    <4_1>_N = sum_k |(q;q)_k|^2 = sum_k exp(-2 s_k)

    saddle   Lambda'(theta) = -log(2 sin theta) = 0  =>  theta* = 5 pi/6
    volume   (2N/pi) Lambda(pi/6) = Vol N/2pi,  Vol(4_1) = 4 Lambda(pi/6)
    Stirling 2 N sin(theta*) = N
    Hessian  Lambda''(theta*) = -cot(theta*) = -sqrt3  =>  sqrt(N/sqrt3)

    <4_1>_N ~ 3^{-1/4} N^{3/2} e^{Vol N/2pi}

so `c_sigma(4_1) = 3^{-1/4}` AND the power `N^{3/2}` are derived. Richardson at
N = 32000, 64000 gives 0.759835685682 vs 3^{-1/4} = 0.759835685652 (rel 4.0e-11);
the corpus's extrapolated value agrees to 4.5e-18.

**Two things came out that were not asked for.**

1. RIGIDITY. In one variable the saddle condition IS `2 sin theta* = 1`, so the
   Stirling factor is pinned to 1 and `c_sigma = |cot theta*|^{-1/2} = 3^{-1/4}`
   with no freedom. `3^{-1/4}` is a property of "one summation variable", not of
   `4_1`.

2. `k = 2^{-1/2}` IS FORCED BY THE SADDLE CONDITION ALONE. Since
   `c_sigma = 2 sin theta* |cot theta*|^{-1/2}` and `|tau| = |cot theta*|/2`,
   the Hessian cancels in `k := c_sigma |tau|^{1/2}` BEFORE it is evaluated:
   `k^2 = (2 sin theta*)^2/2 = 1/2`. No trace field, no cusp number, no
   manifold. The `4_1` calibration the whole arc rested on was never carrying
   information.

Also exhibits `tau_DG` as literally the Hessian: `|tau_DG|(4_1) =
|cot theta*|/2 = sqrt3/2`, matching the corpus's independent computation.

Lean (sorry-free, three standard axioms): `saddle_forces_cot`,
`c_sq_sqrt_three_of_saddle`, `c_pow_four_eq_third`, `k_sq_eq_half_of_saddle`.
The ANALYTIC input (Euler-Maclaurin for `s_k`, Laplace's method) is assumed as
hypotheses, not formalised — Mathlib has no usable form of it. What is proved is
the algebra downstream, which is where the rigidity lives.

Probe: `computations/probes/one_loop_c_sigma_tetrahedral_probe.py`.
Audit: "The knot side, closed" in
`docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md`.
Follow-up: `qou-dodK`.
