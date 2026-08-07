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
updated_at: 2026-08-07T22:05:00Z
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

---

## 2026-08-07 (later) — repair attempt: two results, one of them inconclusive. Bean STAYS OPEN.

### DECISIVE: no uniform shape monomial repairs it

Tested `|det J| / m` for ten uniform candidates `m` — `prod|z|`, `prod|1-z|`,
`prod|z'|`, `prod|z''|`, `prod|z(1-z)|`, `prod|z/(1-z)|`, `prod|z''/z'|`, and
squares — over ~31 geometric retriangulations each of `5_2`, `L5a1`, `6_2`.
**None reaches a single value.** Best partial: `prod|1-z|` takes `5_2` from
8 distinct to 3; on `L5a1`/`6_2` most candidates make it WORSE (up to 20).

So the correction is not a fixed formula in the shapes. It requires genuine
per-tetrahedron integer exponents that vary with the triangulation — i.e. an
actual Neumann combinatorial flattening. That rules out the cheap fix and is
worth not re-trying.

### USEFUL: the flattening conditions are solvable from SnapPy, and the
### convention is now pinned

`M.gluing_equations_pgl()` returns `NeumannZagierTypeEquations` with
`.matrix` in `(z, z', z'')` form — columns `z_XXXX_i / zp_XXXX_i / zpp_XXXX_i`,
rows `edge_*` then `meridian_*` / `longitude_*`. So the flattening is an
integer linear system, no paper needed to set it up.

**Consistent convention, found by search rather than asserted:**

    edge rows   = 2
    cusp rows   = 0
    f + f' + f'' = +1   per tetrahedron

For `5_2` this admits e.g. `(-2,2,1, 2,1,-2, -2,2,1)`. Note the per-tetrahedron
sum is **+1, not -1** — the -1 that `zz'z'' = -1` naively suggests is
INCONSISTENT (no integer solution). Worth recording: I asserted -1 first and
the search corrected me.

### INCONCLUSIVE: the correction convention is not yet identified

With those flattenings, tested six placements of the monomial
(`detJ / prod z''^f'' z'^f'`, with `z'^-f'`, the full `z^f z'^f' z''^f''`,
each single factor, and the reciprocal) across 22 three-tetrahedron
retriangulations of `5_2`. **No placement yielded a value common to all
triangulations.**

**This is NOT a refutation of the flattening repair**, and must not be read as
one. The search was bounded: exponents restricted to `[-2,2]` and at most 3
flattenings kept per triangulation. The true flattening may lie outside that
box, or be a specific one among many that the truncation discarded. A proper
attempt needs a real integer solver (Smith normal form / HNF — `sympy` is not
installed in this container) enumerating the full solution coset, not a
bounded product search.

### Next step for whoever takes this

1. Install `sympy` (or implement HNF) and enumerate the flattening coset
   properly instead of brute-forcing a box.
2. Re-run the six placements. `5_2` remains the sharpest test: rank-1
   ambiguity, generator `sqrt(rho)`, so a correct correction must kill exactly
   that freedom and nothing else.
3. Only then re-derive the per-cusp factor — which the ambiguity-group result
   already shows is unidentifiable in its current form.

---

## 2026-08-07 (third pass) — full coset enumerated. A candidate appeared, then died.

The previous pass was inconclusive because the flattening search was a box on
the exponents. That is now fixed: `sympy` installed, and the coset is
enumerated properly as *particular solution + integer kernel* via
`gauss_jordan_solve`, keeping only integral members. That yields **12-25
genuine flattenings per triangulation** (params in `[-2,2]`), not a truncated
box.

### Result: no placement is invariant

Six placements of the monomial tested over **26** three-tetrahedron geometric
retriangulations of `5_2` (controls as before). All give `common = 0` — i.e.
no value is reachable in every triangulation:

    detJ / prod z''^f'' z'^f'      union=71  common=0
    detJ / prod z''^f'' z'^-f'     union=50  common=0
    detJ / prod z^f z'^f' z''^f''  union=60  common=0
    detJ / prod z''^f''            union=49  common=0
    detJ / prod z'^f'              union=45  common=0
    detJ / prod z^f                union=51  common=0

### The candidate that had to be killed — and how

`detJ / prod z'^f'` looked like a HIT at 14 triangulations: `common = 2`, then
`common = 1` on a re-run, with the surviving value `1.753071635790291`.

It passed a **null control** — replacing the flattenings with random integer
vectors of the same count and range gave a nonempty common set in **0/12**
trials, so it was not an artifact of set size.

It failed the **sample-size check**: at 26 triangulations `common = 0`.

Two things worth carrying forward:

1. The `common` statistic ("some flattening in each triangulation agrees") is
   WEAK, because each triangulation offers ~25 choices. A null control is
   necessary but NOT sufficient to validate it — the drift `2 -> 1 -> 0` as
   triangulations were added is what actually exposed it. Any future candidate
   must be re-tested at increasing sample size, not just against a null.
2. The value it converged on, `1.7530716357902911`, is exactly the SMALLEST
   observed `|det J|` rung for `5_2` — not an independent quantity. That
   should have raised suspicion immediately. (It is close to but distinct from
   `rho^2 = 1.7548776662`, so the plastic connection does not extend here.)

### Where this leaves the repair

Stronger negative than before, but STILL not a proof that no flattening-based
correction exists. Remaining bounds, stated honestly:

  * coset params restricted to `[-2,2]`;
  * only 3-tetrahedron triangulations of `5_2`;
  * only six placements, all of the form `prod (shape)^(flattening)`.

The DG 1-loop invariant also carries a global `1/2` and a SIGN that this test
ignores by taking `abs`. If the correct correction involves the flattening
non-monomially, or the determinant itself needs the `A D_z'' + B D_z'` form
rather than the `A - B z/(1-z)` form used by
`whitehead_c_sigma_torsion.py`, none of these placements would find it.

**Next: stop searching placements and get the DG formula itself right** — the
determinant's construction, not just its correction. That is a literature task
(Dimofte-Garoufalidis, Geom. Topol. 17 (2013) 1253), not a search task.
