---
# qou-fl4t
title: 'REPAIR: restore the DG flattening + 1/2 so |det J| is triangulation-invariant, then re-derive the per-cusp factor'
status: in-progress
type: task
priority: normal
tags:
    - compute
    - torsion
    - whitehead
    - refuted-needs-repair
created_at: 2026-08-07T18:40:00Z
updated_at: 2026-08-07T21:20:00Z
---

## Why

`computations/whitehead_c_sigma_torsion.py` computes a 1-loop determinant and
takes `|tau| = |det J|`. PR #4691 (merged) shows that quantity is **not a
topological invariant**: retriangulating the same manifold gives 8 distinct
values for `5_2`, 15 for `6_2`, 4 for `L5a1`, 8 for `L6a4`, while every
2-tetrahedron case (`4_1`, `m003`, `m004`) is invariant. Controls verified —
`is_isometric_to` and 212-bit volume identical, non-geometric solutions
excluded.

The script drops the Dimofte-Garoufalidis flattening monomial and the global
1/2, justified in its own docstring by "the calibration below reproduces the
known figure-eight value sqrt(3)". `4_1` has two tetrahedra — it is the one
class that structurally cannot exhibit the dependence, so that calibration
cannot detect what is missing.

## Do

1. Restore the flattening monomial and the 1/2:
   `tau_DG = +- (1/2) det(A D_{z''} + B D_{z'}) / prod( z''^{f''} z'^{f'} )`.
2. Re-run `computations/probes/one_loop_triangulation_invariance_probe.py`.
   The gate is: `5_2`, `6_2`, `L5a1`, `L6a4` must each collapse to ONE value.
   `4_1`/`m003`/`m004` staying invariant proves nothing — they already are.
3. Only THEN re-derive the per-cusp factor `2^{(c-1)/2}` against the corrected
   torsion. It may survive, vanish, or change form; it is currently untested,
   having been fitted against the ambiguity.

## Do NOT

- Do not calibrate on a 2-tetrahedron manifold alone. `5_2` costs nothing and
  is the cheapest case that discriminates.
- Do not re-assert `c_sigma = 2^{-3/4}` as DERIVED until step 2 passes. It is
  back to IDENTIFICATION (bean `qou-pn5j`, reopened).
- Do not "fix" this by absorbing the discrepancy into a per-cusp constant.
  The observed spread is a sqrt(2) ladder of exactly the magnitude of
  `2^{(c-1)/2}`, so any c-dependence is unidentifiable until the underlying
  quantity is well-defined. That is the trap this bean exists to prevent.

## Not affected

The numerical value `c_sigma = 2^{-3/4}` (~20 digits, `whitehead_c_sigma_hiprec.py`,
pure mpmath, no SnapPy, no det J) is untouched. This is about the derivation.

<!-- 2026-08-07T21:05:00Z branch claude/beans-fl4t-t0rf — claimed: measuring the ambiguity's structure before implementing any flattening -->

---

## 2026-08-07 — the ambiguity GROUP is identified. Two readings killed.

New probe: `computations/probes/one_loop_ambiguity_group_probe.py`.
Rather than guess the DG flattening formula, measure which group `|det J|`
varies in — that constrains the repair without risking a wrong formula.

Two natural readings, both FALSE:

  H1  a universal sqrt(2) ladder, absorbable by a per-cusp constant
      `2^{(c-1)/2}`.  FALSE: `5_2` and `6_2` have NON-integral exponents.
      The sqrt(2) ladder is a property of L5a1/L6a4's arithmetic, not general.
  H2  a fixed power per 2-3 Pachner move, i.e. set by tetrahedron count.
      FALSE: `5_2` realises five distinct values at 3 tetrahedra alone.

What it actually is — the UNIT GROUP OF THE TRACE FIELD:

    4_1    1 cusp,  2 tet    1 value        no ambiguity (no room)
    5_2    1 cusp,  3 tet    9 values       generator sqrt(rho), rho = PLASTIC
    6_2    1 cusp,  5 tet   17 values       rank >= 2, 10 distinct gaps
    L5a1   2 cusp,  4 tet    6 values       generator sqrt(2)
    L6a4   3 cusp,  8 tet    7 values       generator sqrt(2)

rho is the real root of `x^3 = x + 1`; the `5_2` identification is exact to the
probe's tolerance (1e-25 relative). **`disc(x^3 - x - 1) = -23`, which is
`5_2`'s trace-field discriminant** — the field the corpus identified
independently in PR #4658.

### Why this CONFIRMS the flattening diagnosis rather than just describing it

The DG 1-loop invariant divides by `prod z_i''^{f_i''} z_i'^{f_i'}`. The shapes
`z_i` are units in the trace field, so that monomial lives in exactly the group
measured above. Dropping it leaves the answer well-defined precisely up to
those units — which is what is observed, per-manifold, with the right generator
each time. The diagnosis was a hypothesis in PR #4691; it now has direct
evidence.

### Consequence for the per-cusp factor — stronger than "unproved"

`2^{(c-1)/2}` is **UNIDENTIFIABLE**, not merely unproved. No universal
c-dependent constant can absorb a manifold-dependent unit group. Any value it
appears to take is an artifact of which rung the default triangulation landed
on. The "Do NOT" above (do not absorb the discrepancy into a per-cusp constant)
is now backed by measurement rather than caution.

### Still to do (this bean stays open)

Restore the flattening monomial + the 1/2 and re-run
`one_loop_triangulation_invariance_probe.py`. Gate unchanged: `5_2`, `6_2`,
`L5a1`, `L6a4` must each collapse to ONE value. `5_2` is now the sharpest
single test — its ambiguity group is rank 1 with a known generator, so a
correct flattening must kill exactly the sqrt(rho) freedom.
