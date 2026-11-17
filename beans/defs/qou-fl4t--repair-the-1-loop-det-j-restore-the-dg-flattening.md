---
# qou-fl4t
title: 'REPAIR: restore the DG flattening + 1/2 so |det J| is triangulation-invariant, then re-derive the per-cusp factor'
status: in-progress
type: task
priority: normal
tags:
    - whitehead
    - refuted-needs-repair
    - reorg-2026-10-04
    - needs-owner
    - compute
    - torsion
created_at: 2026-08-07T18:40:00Z
updated_at: 2026-10-04T15:13:46Z
parent: qou-n4nr
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

---

## 2026-08-07 (fourth pass) — DG 1202.6268 obtained. The formula is in hand and the root cause is confirmed.

`library/arxiv-1202.6268v2/1202.6268v2.pdf` (Dimofte-Garoufalidis, "The quantum content of the
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

---

## 2026-08-07 (fifth pass) — impact analysis. A CORRECT implementation is already in-repo.

Full analysis: `docs/audits/2026-08-07-one-loop-fix-impact-analysis.md`.

`computations/probes/one_loop_vs_nu_sdp_probe.py` (bean qou-r307) already
implements DG/GY Def 2.1 — with the 1/2, the flattening (f+f'+f''=1, edges=2:
the convention this bean recorded), and the monomial. Tested here over ~19
retriangulations each:

    4_1  |tau| = 0.866025403784 = sqrt(3)/2   INVARIANT   (= DG's eq 3.2)
    5_2  |tau| = 1.161162738134               INVARIANT
    6_2  |tau| = 2.216589930891               INVARIANT

versus 8 and 17 distinct values under the broken construction. So the repair is
identified and verified — for ONE-CUSPED manifolds.

**The blocker moved.** That implementation swaps ONE edge row for ONE meridian
row, correct only at c=1. On the links it degenerates: |tau(L5a1)| = 0,
|tau(L6a4)| = 0. DG Definition 1.2 is itself stated for one-cusped manifolds;
multi-cusp is their Section 4.5. The whole c_sigma arc is c=2 and c=3, i.e.
entirely in the regime the correct formula (as implemented) does not cover.

So this is NOT a copy-paste fix. Revised plan on the audit doc; short version:
fix c=1 first (cheap, gives a trusted base), then implement DG Sec 4.5, and only
then touch c_sigma.

Blast radius checked, not assumed: no content .ts, no Lean, no production. 5
probes + 3 audits + 4 beans. #4671's "audit-only" claim HOLDS.

Also surfaced: `borromean_cusp_framing_factor.py` already recorded |det| varying
over framings ({64,128,256,512}); PR #4691 found the same object varying over
retriangulations. Two explanations for one phenomenon, and DG says neither is
the cause. That script is also where the 2^c framing count — the apparent origin
of the per-cusp factor — comes from.

And: the sqrt(3) calibration target may itself be wrong. This repo's
value-validated Porti probe gives |T_mu(4_1)| = 3; DG give sqrt(3)/2. sqrt(3) is
neither. one_loop_vs_nu_sdp_probe.py explicitly warns "Do NOT read the tau
values here as the adjoint torsion" — which is what the c_sigma script did.

---

## 2026-08-07 (sixth pass) — CORRECTION: the multi-cusp formula is NOT in DG.

Earlier passes of this bean, and PR #4706's audit, said the multi-cusp case is
"DG Section 4.5". **Wrong.** Section 4.5 is the CHARACTER-VARIETY
generalization — still one cusp, deformed representations with meridian
eigenvalue m. The multi-cusp formula is not in the paper.

DG list it in Section 1.9 among extensions, and say:

    "The generalization to multiple cusps is also quite straightforward, but
     left out mainly for simplicity of exposition."

So there is nothing to implement from this source. It must be DERIVED, and
"straightforward" is the authors' judgement, not a recipe. The one-cusped
derivation uses an identity that is specifically one-cusped:

    "For a one-cusped manifold, every edge begins and ends at the cusp, which
     implies sum_I G_Ii = sum_I G'_Ii = sum_I G''_Ii = 2"

That fails for c >= 2. It is what makes the N edge equations dependent in the
way the construction needs, so the extension is not a matter of adding rows.

LEAD. DG identify tau via Yamaguchi [Yam08] as tau_M = (1/c_M) dtau_M(t)/dt|_1
with c_M the CUSP SHAPE. Dubois-Huynh-Yamaguchi (library/arxiv-0706.2213v3/0706.2213v3.pdf,
Sec 5.3) independently express the torsion at holonomy via the cusp shape.
Cusp shape is per-cusp, so that is where a genuine c-dependence would enter —
and the place to look before inventing one. Note this is also the honest
setting in which to ask whether anything like 2^{(c-1)/2} exists at all.

Status unchanged: c=1 is fixed and trusted (computations/one_loop_torsion.py,
PR #4707). c>=2 is open and now correctly characterised as a derivation task,
not an implementation task.

---

## 2026-08-07 (seventh pass) — DERIVED. c >= 2 implemented and validated.

And the blocker asserted in the sixth pass above is WITHDRAWN.

That pass said the identity `sum_I G_Ii = sum_I G'_Ii = sum_I G''_Ii = 2`
"fails for c >= 2". **It does not.** Measured directly on 13 manifolds
(`probes/one_loop_multicusp_derivation_probe.py`, section A): it holds at every
cusp number. It is not a cusp statement at all — each tetrahedron has six edges
in three opposite pairs, one pair per shape type, each glued into exactly one
edge class, so the column sum is 2 with no reference to cusps. I turned a
quoted sentence into a structural obstruction without testing the sentence.

THE DERIVATION

  1. Because zeta + zeta' + zeta'' = 0, the identity forces the N specialised
     edge rows to SUM TO ZERO — at every c. Their rank is exactly N - c.
     So: N - c edge rows + c peripheral rows.
  2. The non-obvious part is WHICH N - c rows. An independent SUBSET spans the
     right complex subspace but can generate a proper SUBLATTICE of the edge
     lattice (index 2 observed), doubling the determinant. A Hermite-normal-form
     BASIS of the lattice generated by all N edge rows fixes it. The lattice
     lives in Z^{2N}, in Neumann-Zagier coordinates (a,b) = (G-G'', G'-G'').
  3. The flattening was never the c >= 2 problem: its kernel moves the monomial
     only by a phase (~1e-70), so |tau| is flattening-independent either way.

VALIDATION — not self-consistency

  * Triangulation invariance: 1 value on all 13 manifolds, 25 randomisations
    each. The subset variant gives 2 values (ratio exactly 2) on L5a1, L6a4,
    L7a1 — which is how the lattice effect was found.
  * CHANGE-OF-CURVE LAW, per cusp: swapping cusp k's meridian row for its
    longitude row multiplies tau by conj(cusp shape of cusp k). SnapPy computes
    cusp shapes from the cusp cross-section, independently of all of this.
    Holds to ~1e-59 at c = 1, 2, 3. This is the check with content at c >= 2,
    because it tests each cusp separately.
  * Independent presentations agree: L5a1 = 5^2_1 = m129 = sqrt(2);
    L6a4 = t12067 = 8; L6a2 = m203 = sqrt(3).

VALUES: |tau(L5a1)| = sqrt(2), |tau(m125)| = 2 sqrt(2), |tau(L6a2)| = sqrt(3),
|tau(L6a1)| = sqrt(7), |tau(L6a4)| = 8, |tau(s776)| = sqrt(14).
The old claims were |tau(L5a1)| = 2^{5/2} and |tau(L6a4)| = 2^6.

STILL NOT SETTLED — and it is exactly what this arc wanted

The overall constant at c >= 2. The 1/2 is DG's, pinned at c = 1. Invariance
cannot see a factor depending only on c, and the change-of-curve law is a ratio,
so `2^{alpha(c-1)} * 1/2` passes every test above. That is the shape of the
per-cusp factor 2^{(c-1)/2}. So this derivation does NOT revive it, and
c_sigma = 2^{-3/4} stays at IDENTIFICATION (bean qou-pn5j). Pinning it needs an
external multi-cusp reference value; nothing in library/ has one —
Garoufalidis-Yoon prove 1-loop = adjoint torsion for TWO-BRIDGE knots.

Do NOT close this bean by declaring c_sigma derived. Step 3 of "Do" above is
still open, and is now open for a sharper reason than when it was written.

Audit: docs/audits/2026-08-07-one-loop-multicusp-derivation.md

<!-- 2026-08-07T23:55:00Z branch claude/dg-scope-correction — derived, implemented, validated -->

---

## 2026-08-08 (eighth pass) — step 3 done: the per-cusp factor DISSOLVES.

Step 3 of "Do" above said: re-derive the per-cusp factor against the corrected
torsion; it may survive, vanish, or change form. **It vanishes.**

Against the corrected invariant (|tau(4_1)| = sqrt(3)/2, |tau(L5a1)| = sqrt(2),
|tau(L6a4)| = 8), the quantity

    k_c := c_sigma * |tau_DG|^{1/2}

is the SAME constant 2^{-1/2} at c = 1 and c = 2, to 17 digits. A per-cusp
factor would require k to move by sqrt(2); measured k_2/k_1 = 0.999999999999999995.
So the law is c_sigma = 2^{-1/2} |tau_DG|^{-1/2}, with no c-dependence, and
calibrating on 4_1 ALONE predicts c_sigma(L5a1) = 2^{-3/4} to 17 digits with
nothing adjustable.

NOT CIRCULAR: the c_sigma values are colored-Jones/Kashaev extractions with no
determinant anywhere (whitehead-c-sigma-fig8-calib and -hiprec witnesses), and
the fig8 witness states they use the same c_sigma definition, so c=1 and c=2 are
directly comparable.

WHY THE OLD FIT LOOKED RIGHT. On the DEFAULT triangulations of 4_1, L5a1, L6a4 —
and not in general — |tau_old| = 2^c |tau_DG|, so
2^{(c-1)/2}|tau_old|^{-1/2} = 2^{-1/2}|tau_DG|^{-1/2} identically. The per-cusp
factor was exactly the c-dependence needed to undo that 2^c: a reparametrization,
not a Gaussian-integration factor. Measured over 13 manifolds the 2^c relation
holds on 5 and fails on 8, including 5_2/6_2/7_4 at c=1 where no per-cusp factor
could be responsible.

ALSO CLOSES the normalization caveat the seventh pass left open, for c=1 vs 2:
invariance and the change-of-curve law are blind to a constant depending only on
c, but the Jones side is not. Under the prefactor form c_sigma ~ |tau|^{-1/2},
k_1 = k_2 says the DG normalization carries no extra c-dependence.

c=3 is SUPPORTING ONLY: k_3/k_1 = 1.0035 (0.35%), but that tower's witness flags
an unresolved normalization+cusp offset and returns p = 1.4993 vs 3/2.

Audit: docs/audits/2026-08-08-per-cusp-factor-dissolves.md
Probe: computations/probes/one_loop_c_sigma_percusp_dissolution_probe.py

<!-- 2026-08-08T00:40:00Z branch claude/dg-scope-correction -->

---

## 2026-08-08 (ninth pass) — the algebra is now Lean, sorry-free.

`folio/quantum-observable-universe/lean/QOU/OneLoopEdgeLattice.lean`.
Nine theorems, `#print axioms` = [propext, Classical.choice, Quot.sound] on every
one, zero sorries, wired into QOU.lean.

  zeta_sum_eq_zero              zeta + zeta' + zeta'' = 0
  zetaPP_eq                     zeta'' = -zeta - zeta'
  nz_pair_reduction             the row depends only on (G-G'', G'-G'')
  edge_rows_sum_zero            column sums 2  =>  specialised edge rows sum to 0
  edge_rows_hypotheses_satisfiable   non-vacuity witness
  det_basis_change              det(U B) = det(U) det(B) over Z -> C
  det_basis_change_unimodular   unimodular change fixes det up to sign
  det_sublattice_index          index-k sublattice scales det by k
  percusp_factor_absorbs        2^{(c-1)/2}(2^c t)^{-1/2} = 2^{-1/2} t^{-1/2}

WHY THESE. Almost all the evidence for the multi-cusp derivation is measurement.
These four steps were not measurements — they were algebra asserted in prose, and
one of them (the cusp-freeness of the edge-row degeneracy) is exactly where the
sixth pass went wrong by reading a quoted sentence as a hypothesis.
`edge_rows_sum_zero` has NO cusp number in its statement or proof, which makes
that claim checkable rather than asserted.

`percusp_factor_absorbs` is the sharpest of them: it proves the two c_sigma laws
are the SAME FUNCTION wherever |tau_old| = 2^c|tau|, so agreement at c = 1,2,3 on
that data confirmed nothing. The dissolution result is that k_1 = k_2 against the
CORRECTED invariant, where the identity does not apply.

NOT formalised: that the construction computes the adjoint torsion, or that it is
a topological invariant. Shapes are free complex numbers in the Lean file; no
gluing equation is imposed. Those stay numerical (and at c=1 a Garoufalidis-Yoon
theorem).

<!-- 2026-08-08T01:20:00Z branch claude/dg-scope-correction -->

---

## 2026-08-08 (tenth pass) — downstream chain reconciled; the framing sweep EXPLAINED.

Items 3 and 4 of the impact analysis's change table, closed.

`probes/borromean_cusp_framing_factor.py` — its framing sweep is CONFIRMED
EXACTLY and is now explained rather than observed. It is the CHANGE-OF-CURVE
LAW: replacing cusp k's meridian row by that cusp's longitude row multiplies tau
by conj(cusp shape of cusp k), and every Borromean cusp shape has modulus exactly
2. Recomputed with the corrected invariant:

    0 longitudes  |tau| =  8   2^c|tau| =  64      <- all-meridian
    1 longitude   |tau| = 16   2^c|tau| = 128  (x3)
    2 longitudes  |tau| = 32   2^c|tau| = 256  (x3)
    3 longitudes  |tau| = 64   2^c|tau| = 512

reproducing that file's observed {64,128,256,512} exactly. All-meridian is the
unique minimum because every cusp shape has modulus > 1.

What does NOT survive there: `exp(2c0)|det J_NZ| = 2^{c-1}` is stated in a
non-invariant quantity, so it is not a well-posed statement about the link; and
the 2^{c-1} is just 2^c/2, not a "reduced-vs-Kashaev normalization, one Gaussian
meridian integration per extra cusp". Its DECISIVE THIRD DATA POINT — the 2-cusp
Whitehead Kashaev tower — already existed in the corpus and PASSES
(c_sigma(L5a1) = 2^{-3/4} to 20 digits => exp(2c0) = 1/(2 sqrt 2), its exact
prediction) — and passes equally for the c-free law, which is the point.

`probes/borromean_jones_1loop_torsion.py` — the bounded follow-up it names
("compute tau(B3) from the octahedral NZ data") is delivered: |tau_DG(L6a4)| = 8.
Predicted exp(2c0) = 1/16 = 0.0625 vs measured 0.06294 (0.7%). Recorded as
SUPPORTING, not a match: its two fits bracket the prediction (spread 0.0093 vs
deviation 0.0035) and its own witness flags a normalization+cusp offset.

`probes/jones_1loop_c0_calibration_fig8.py` — not superseded; it is the anchor.
Added the normalization note: its |tau_adj| = 1/sqrt(3) is 1/T with T = 2|tau_DG|,
so its relation reads exp(2c0) = 1/(2|tau_DG|), which carries no per-cusp factor.

STILL OPEN on this bean: item 5, draining float64 from
whitehead_c_sigma_torsion.py and borromean_nz_adjoint_torsion.py (bean qou-t0rf's
class) — independent of everything above.

<!-- 2026-08-08T01:50:00Z branch claude/dg-scope-correction -->



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR litlfred/qou#8231)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8231 (`513987e80ae041a6d8bc835ffbdda5371ccac289`, scriptCommitSha `9bd895c1b028c3d1abf67e3de52aeade9e9e5ccc`)
- **Summary**: Added `zeta_elementary_symm_two`, `zeta_cubes_sum_eq_three_prod`, and `det_sublattice_index_cross_eq` in `QOU/OneLoopEdgeLattice.lean`, verified by 80-dps mpmath probe `hyperbolic_planck_oneloop_qint_dilog_probe.py` (`scriptHash: 83d59661279d`).
