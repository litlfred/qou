---
# qou-slid
title: 'GAP: is the turn slide derivable from R1/R2/R3 and the join moves on diagram codes'
status: todo
type: task
priority: normal
tags:
    - pl-knots
created_at: 2026-11-21T22:45:00Z
updated_at: 2026-11-22T10:30:00Z
---

Issue #8902, PR #8962. `Move.slide` in `QOU/MathlibExt/LinkDiagramCode.lean` moves `t` turns from
both incoming edges of a crossing to both outgoing edges. Markov invariance of braid closures
(`reidemeisterEquiv_of_markovEquiv`, `LinkDiagramBraidMarkov.lean`) uses it, through conjugation and
far commutation. The owner chose to try to derive it before keeping it as a primitive (2026-11-21).

Status: neither derived nor shown independent.

- Direct route fails as attempted: a turn can be pushed into an antiparallel bigon (`r2anti`), but
  moving the crossing through that bigon needs R3, and R3 needs three strands. A lone crossing has two.
- Model search, exact (sympy Groebner, scratch only): no state-sum model whose crossings shift
  labels by a fixed cyclic permutation with label-dependent phases (n = 2, 3) satisfies the r1,
  r2par, r2anti and r3 identities of `Model.Invariant` while having non-constant `K`. So these
  models cannot show the slide is independent. A wider model class is untested.
- A linear invariant of the form sum over segments of turn times an end-type weight is not
  invariant under r2par or r2anti, which split segments at arbitrary points.

Next honest steps: (1) look for a derivation that uses a third strand already present in a braid
closure (enough for Markov invariance, though not for all codes); (2) search a wider model class,
e.g. general 2-label tensors, for an independence proof.

## 2026-11-21 (later): owner picked both routes ("1 2")

Wider model search (route 2), numerical only, scratch, mpmath 30 dps, Levenberg-Marquardt over general
2-label tensors (16 entries of X+, X- = inverse via r2par, K = (k0, k1), theta free), residuals
= the r1, r2anti, r3 identities of `Model.Invariant`:
- With only k0 != k1 imposed, 3 of 8 starts converged (residual < 1e-40), all with k1 = -k0. Their
  charge-changing entries change charge by 2, so K_a K_c = K_b K_d still holds and the slide holds.
- With k0^2 != k1^2 imposed (10 starts): no convergence. Runs stall at residual 1e-10..1e-5 with
  w = 1/(k0^2 - k1^2) growing (|w| ~ 1e2..3e3) and det R -> 0, i.e. they drift to the boundary
  where the slide holds again.
- With k1 = -k0 and a parity-violating entry imposed (6 starts): no convergence (residual >= 6e-5).
So no 2-label model breaking the slide was found. This is evidence, not proof, and it means
state sums are unlikely to show the slide independent.

Route 1 notes: a turn can cross a crossing only through `r2anti` (antiparallel bigon), and
braid strands meet only in parallel, so the obvious third-strand route needs an antiparallel pair.
Not yet attempted in Lean.

## 2026-11-22: owner picked routes 1 and 3

- **Correction to the 2026-11-21 route-1 note.** In codes `r2anti` applies to ANY two joins
  `(a,b,bigonTurn s)`, `(c,d,0)`: a code has no orientation of strands in the plane, so "braid
  strands are parallel" is not an obstacle. The note above was wrong on that point.
- A kink loop carries no net turn (`r1` removes it with turn `kinkTurn` inside), so the classical
  curl-through-a-crossing trick moves no turn by itself. Only `r2anti` moves a turn across a crossing.
- Model-level algebra (exact, by hand): `r2anti` for sign `false` follows from `r2anti` for sign
  `true` (with `X-` the inverse of `X+`); the two are not independent constraints.
- Numerical searches (mpmath 30 dps, LM, crossing matrix forced invertible via det*z = 1):
  - all identities, k0^2 != k1^2 forced: 6 starts, none converge; drift to k1 = -k0 (slide holds);
  - r2par + r2anti only: 4 starts at 3000 iterations stall at residual 1e-10..1e-11, drifting to
    k0^2 = k1^2; dropping r1 or r3 separately: same drift;
  - non-diagonalisable turn matrix K = lam [[1,1],[0,1]] (route 3, outside `Model`): 8 starts
    converge (residual ~1e-34) with lam = +-1 and slide defect ~1e-17, i.e. the slide holds.
  Reading (evidence only): the R2 identities alone appear to force the slide identity in every
  model found. If that is a theorem about models, its proof should point to a diagrammatic
  derivation using r2anti/r2par only.

## 2026-11-22 (later) — CORRECTION: R2 alone does NOT force the slide

The note above ("R2 alone appears to force slide") is **retracted**. It came from
numerical runs that drifted to `k0² = k1²`; it was never a proof, and it is false:

- **Linear-rack ansatz** `X+(u,u',o,o') = δ_{oo'} M_o[u,u']`, `X- = (X+)⁻¹`:
  r2par and r2anti hold for **every** invertible family `{M_o}` (checked by hand).
  So R2 places no constraint linking K to the slide.
- What constrains is **r1 + r3**:
  - r1 forces row and column `y` of `M_y` diagonal, `M_y[y,y] = θ·K_y`, and `K_y = ±1`.
  - r3 ⇔ `M_a M_b = M_{b0} M_a` whenever `M_a[b0,b] ≠ 0`.
  - The slide fails iff some `M_c[a,b] ≠ 0` with `K_a ≠ K_b`.
- **Exact (sympy Groebner, not numeric):** 3 labels, `K = (1,1,−1)`: no model with
  r1 + r3 + invertibility and any mixing entry nonzero (basis = [1]). So within this
  ansatz at 3 labels, r1 + r3 force the slide. Script:
  scratchpad `slide/rack.py` (evidence only, not committed).
- 4-label runs (`K = (1,1,−1,−1)`, `(1,1,1,−1)`) running.

Status unchanged: the slide's derivability is **OPEN**. Bean stays open.

## 2026-11-22 — hand proof: in the linear-rack ansatz, r1 + r3 force the slide (any label count)

The 4-label Groebner runs timed out (50 min each) and are superseded by this argument.
Suppose `K_a ≠ K_b` and `M_c[a,b] ≠ 0`. Apply r3 with `(a, b0, b) := (c, a, b)`:
`M_c M_b = M_a M_c`. Read off entry `(a,b)`.
- Row `a` of `M_a` is `θK_a` on the diagonal and 0 elsewhere (r1), so the right side gives `θK_a · M_c[a,b]`.
- Column `b` of `M_b` is likewise diagonal, so the left side gives `M_c[a,b] · θK_b`.
So `θ(K_a − K_b) M_c[a,b] = 0`. With `θ ≠ 0`, `M_c[a,b] = 0`. The case `c = a` is already
excluded by r1. **Consequence:** no linear-rack model separates the slide. This is
a statement about the ansatz only, so it does not settle derivability; the bean stays OPEN.
Diagrammatic hint for route 1: the proof uses one r3 (strand c over a, b) with a kink
at a and at b, i.e. "push a kink through a crossing with r3".
