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
updated_at: 2026-08-07T22:20:00Z
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

## 2026-08-07 (fourth pass) — DG 1202.6268 obtained. The formula is in hand and the root cause is confirmed.

`uploads/1202.6268v2.pdf` (Dimofte-Garoufalidis, "The quantum content of the
gluing equations"). Four results, all from the source rather than inference.

### 1. My searched flattening convention was RIGHT — Definition 2.1

    f_i + f'_i + f''_i = 1                    (2.10a)
    sum_i (G_Ii f_i + G'_Ii f'_i + G''_Ii f''_i) = 2  for edges I = 1..N
                                              = 0  for the cusp row I = N+1   (2.10b)

Exactly the convention I found by search after reasoning my way to the wrong
`-1`. Eliminating `f'` gives the clean form used below:

    A f + B f'' = nu                          (2.11)

a linear Diophantine system. Neumann [Neu92, Lem 6.1] proves every ideal
triangulation has a flattening.

### 2. The repo's determinant is THE WRONG MATRIX — this is the root cause

Definition 1.2 / eq (3.1):

    tau := -+ (1/2) det( A Delta_z'' + B Delta_z^{-1} ) * z^{f''} * z''^{-f}

Entry-wise that is `A_kj z''_j + B_kj / z_j`.
`whitehead_c_sigma_torsion.py` builds `A_kj - B_kj z_j/(1-z_j)`. **Different
matrix**, not a normalisation of the same one. This is exactly the bound I
flagged as untested in PR #4700: searching *corrections* could never have found
it, because the object being corrected was wrong.

Note also DG's `A`, `B` are exponents of `(z, z'')` — their gluing equations are
`z^A z''^B = (-1)^nu` — whereas SnapPy's `gluing_equations('rect')` is in
`(z, 1-z)`. `gluing_equations_pgl()` gives the `(z, z', z'')` form and is the
right entry point.

### 3. The monomial is a CROSS pairing — none of my six placements tested it

    z^{f''} * z''^{-f}

i.e. `z` carries `f''` and `z''` carries `-f`. I tested `z''^f'' z'^f'`,
`z''^f'' z'^-f'`, `z^f z'^f' z''^f''`, and the three single factors. The actual
pairing is not among them. The negative in PR #4700 is therefore explained, not
merely bounded.

### 4. The factor of 2 the script dropped is real — DG's worked 4_1 example

Section 3.1 computes the figure-eight directly and gets

    tau_{4_1} = (1/2)(z'' - w''^{-1}) = (1/2) sqrt(-3)      (3.2)

so `|tau(4_1)| = sqrt(3)/2`. The repo's `|det J| = sqrt(3)` is **exactly twice**
that — precisely the `1/2` its docstring claims is "NOT needed for the MODULUS,
because the calibration below reproduces the known figure-eight value sqrt(3)".
The calibration matched a number that differs from DG's normalisation by the
very factor being dropped.

### 5. And DG PROVE topological invariance — including under 2-3 moves

Section 3: independence of quad type, of edge choice, of meridian path, of the
flattening, and invariance under 2-3 moves (3.6). So the correct object IS
invariant. That vindicates the whole line of attack: the non-invariance measured
in PR #4691 is a property of the implementation, not of the invariant, and
"restore the flattening" was too weak a diagnosis — the determinant needs
rebuilding too.

### Next — now a bounded implementation task, not a search

1. Build `A`, `B` in DG's `(z, z'')` convention from `gluing_equations_pgl()`.
2. Solve `A f + B f'' = nu` over Z (sympy is now installed).
3. Form `-+ (1/2) det(A Delta_z'' + B Delta_z^{-1}) z^{f''} z''^{-f}`.
4. Gate: `4_1` must give `sqrt(3)/2`, and `5_2`, `6_2`, `L5a1`, `L6a4` must each
   collapse to ONE value under retriangulation. DG's own 4_1 worked example is
   the unit test.
5. Only then revisit the per-cusp factor. Note Definition 1.2 is stated for
   ONE-cusped manifolds; the multi-cusp generalisation is Section 4.5
   ("Invariance of the generalized torsion"), which is where any genuine
   c-dependence would actually live.
