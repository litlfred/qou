---
# qou-qbr3
title: 'S2: ramification — Newton slope blocks A1,A2 at infinity and their square roots B1,B2 (gated on S1)'
status: scrapped
type: task
priority: normal
created_at: 2026-08-08T08:05:00Z
updated_at: 2026-08-08T11:35:00Z
---

Compute the slope blocks `A1, A2` from the Newton polygon of
`L1 = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1)` at `infinity` (single edge
(2,0)->(0,1), slope 1/2), then their `d`-th roots -- here **square roots**
`B1, B2`, the ramification intrinsic to a non-integral slope (RSZ §3.3).

Concrete linear algebra over a suitable extension. Exactly checkable, and no
resummation is involved yet.

**Deliverable:** explicit `A_i`; explicit `B_i`; `B_i^2 = A_i` verified
symbolically (exact arithmetic, not float).

**GATED on `qou-qbg2` (S1)** -- if S1 shows the slope->level mapping or the input
normalization is different, the blocks to root change.

Plan: `docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md` (stage S2).

## PARTIAL 2026-08-08 — Newton data done; RSZ read; A1,A2 identification still open

### Newton polygon, computed from the operator (not recalled)

`deg_x a_i = {2:1, 1:0, 0:0}` -> points `(0,1), (1,1), (2,0)`, single edge
`(2,0)->(0,1)` of slope 1/2. This independently reproduces the edge recorded in
the 08-01 audit. The edge height at `i=1` is `1/2` -- NOT a lattice point -- so
`i=1` sits strictly above and contributes nothing. Only the endpoints do:

  i=2 -> x-leading coeff of a_2 = q^2
  i=0 -> x-constant coeff of a_0 = -(q-1)
  => characteristic equation  q^2 t^2 - (q-1) = 0,  i.e. t^2 = (q-1)/q^2

### PROVED sorry-free: the ramification is not removable

`QOU/QBeta/C1NewtonRamification.lean`, `not_isSquare_newtonEdgeConstant`:
`q-1` is not a square in `Q[q]` (a degree parity: `f^2 = q-1` forces
`2*deg f = 1`). Since `q^2` is already a square, the edge equation has no
solution in `Q(q)` -- adjoining `sqrt(q-1)` is genuinely forced. Axioms
`[propext, Classical.choice, Quot.sound]`, no sorryAx.

### CORRECTION to my own earlier reading -- what RSZ actually says

Read from `library/arxiv-0903.0853v3/0903.0853v3.pdf` p.39 (extracted directly; the sandbox has no
pdftotext, so this was pulled from the FlateDecode streams):

  "We must also choose d-th roots B1, B2 of A1, A2. ... a necessary condition for
   the existence of an analytic solution X is that, for all i in a set of
   representatives mod d, one has: sum_{n = i (mod d)} B1^n Ztilde_n B2^{-n} = 0.
   This provides us with d obstructions in Mat_{r1,r2}(C)"

So **A1, A2 are TWO objects** -- the leading matrices of the two slope components
`P1, P2` -- and `B_i` is ONE d-th root of each. My earlier reading ("one
A = (q-1)/q^2 with two roots +/- sqrt(q-1)/q") FLATTENED that and was wrong: the
two roots of the characteristic equation are not `A1, A2`.

Also confirmed from the same page, and it settles the multiplier count
structurally: the obstructions are indexed by **residues mod d**, giving `d`
obstructions in `Mat_{r1,r2}(C)`. With `d = 2`, `r1 = r2 = 1` that is exactly
`C^2` -- the two Stokes multipliers. And `t_n = q^{n-d} t_{n-d}` with growth
`q^{n^2/2d}` and `t_n = q^{n(n-1)/2}` at `d=1`, which is precisely what S0
formalized.

### STILL OPEN (the rest of S2)

Identifying `A1, A2` concretely for C1 requires the **slope decomposition** of the
module into `P1, P2` -- which the single-edge Newton polygon does not by itself
hand over. That is the remaining work here. Do NOT label the characteristic-
equation roots as `A1, A2`; that is the error corrected above.

## VOID 2026-08-08 — see docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md

The Newton half of this bean STANDS (polygon, characteristic equation, and the
proved non-removability of sqrt(q-1) in `C1NewtonRamification.lean`) -- all
computed from the operator. What is void is the `A1,A2` target: RSZ's `A_i` are
the leading matrices of TWO slope components, and C1 has one slope at infinity.
