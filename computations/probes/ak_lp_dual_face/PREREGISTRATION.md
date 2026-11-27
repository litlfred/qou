# Pre-registration: is the a_K LP dual identified on the y_λ = 0 rows?

Written 2026-11-25, **before** any exact computation was run. Committed on its
own so the order is checkable from git history.

## Context

`computations/aK_via_lp_dual_full.py` solves, per atom (proton, neutron,
deuteron, tritium, helium-3, helium-4), the operator-selection LP of
`pyhecke.lp_dual_solver.solve_operator_selection_lp`:

    primal:  min  Σ_j t_j x_j   s.t.  Σ_j x_j = n,   (G x)_i ≥ 0,   x_j ≥ −M
    dual:    max  n·y0 − M Σ_j w_j   s.t.  y0 + Σ_i G_ij u_i + w_j = t_j,
             u_i ≥ 0,  w_j ≥ 0

with `t_λ = |c_λ|`, `G = diag(|c_λ|)`, `c_λ = y_λ·χ^λ` (the chi-cache
`contribution`), `n = tr_M(W_atom)`, `M = 10^6`. The witness field
`u_lambda_star` is `u_λ`.

The 2026-11-24 witness refresh (#9395) moved `u_λ*` by exactly ×10⁻⁴
(5931.63 → 0.593163) **only** on rows with `y_λ = 0`; every `y_λ > 0` row was
identical to 50 digits. Likely trigger: the Clarabel fork bump `0b5b85fbaf6`.

## Hypothesis under test

On rows with `c_λ = 0` the optimal dual face is not a point in the `u_λ`
direction, so an interior-point solver returns an arbitrary point of it and a
solver change can move it without moving anything identified.

## Predictions (fixed before computing)

Let Z = {λ : c_λ = 0} (expected to coincide with {λ : y_λ = 0}; any mismatch
will be reported, and the predictions are stated on Z, the LP's own data).

- **P0.** Z = {λ : y_λ = 0} exactly, for every atom.
- **P1.** For every λ ∈ Z, `u_λ` ranges over **[0, +∞)** on the optimal dual
  face (min 0, max unbounded).
- **P2.** For every λ ∉ Z, `u_λ` is identified and equals **1 exactly**.
- **P3.** `y0` is identified and equals **0 exactly**; primal optimum = dual
  optimum = **0 exactly**.
- **P4.** `w_j` is identified and equals 0 on every column.
- **P5.** Consequently `is_active` (u > dual_tol) and `chirality_dual_sum`
  (sum of u over active non-self-conjugate rows) are **not identified** on any
  atom whose Z contains a non-self-conjugate partition; `self_conjugate_dual_sum`
  likewise where Z contains a self-conjugate one.
- **P6.** Both the pre-refresh and post-refresh published `u_λ*` lie in the
  face computed here (trivially for Z rows if P1 holds; to solver precision ≈1
  for non-Z rows).

## Falsifiers

Any Z row with a finite exact max, or any non-Z row whose min ≠ max, or
`y0 ≠ 0`, refutes the hypothesis as stated. A refutation will be reported as
such, not re-scoped.

## Method

Exact rational arithmetic only (`fractions.Fraction` / `sympy.Rational`, solved
with `sympy.solvers.simplex.linprog`). The chi-cache 50-digit decimal strings
are read as exact rationals; no float64 anywhere. For each atom: solve the
primal and dual exactly, check strong duality, then for every dual coordinate
minimise and maximise it over {dual feasible, dual objective = optimum}.
