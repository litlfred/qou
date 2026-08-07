---
# qou-fl4t
title: 'REPAIR: restore the DG flattening + 1/2 so |det J| is triangulation-invariant, then re-derive the per-cusp factor'
status: todo
type: task
priority: normal
tags:
    - compute
    - torsion
    - whitehead
    - refuted-needs-repair
created_at: 2026-08-07T18:40:00Z
updated_at: 2026-08-07T18:40:00Z
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
