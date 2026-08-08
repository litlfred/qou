---
# qou-qbg2
title: 'S1: settle the q-Borel growth budget — no unramified level d absorbs deg_q(c_n)=n^2 (do BEFORE S2/S3)'
status: completed
type: task
priority: normal
created_at: 2026-08-08T08:05:00Z
updated_at: 2026-08-08T08:30:00Z
---

**A formalize-first prune already bites here.** With `deg_q(c_n) = n^2` now
PROVED for all `n` (`QOU/QBeta/C1InfDegreeLaw.lean`,
`docs/audits/2026-08-08-c1-inf-degree-law-proved.md`) and the RSZ level-`d`
kernel growth `q^{n^2/2d}` (recurrence iterated on degrees; reproduces RSZ's
stated growth to 3 decimals at n=400):

  deg(c_n / t_n) / n^2  =  +0.50 (d=1), +0.75 (d=2), +0.83 (d=3), +0.88 (d=4)

**No level `d` absorbs the growth, and larger `d` is strictly worse.** So the
*unramified* `B_{q,d}` applied directly to `sum c_n x^{-n}` cannot converge, for
any `d`.

**This is a consistency computation on degrees, NOT a theorem about RSZ**
(scope-(a)). Decide which of these holds:

1. **Ramification is forced, not cosmetic** -- the pullback `z = zeta^d` must
   precede the transform (this is why RSZ needs the square roots `B1,B2`), and
   the budget is the quantitative reason it cannot be skipped.
2. **Normalization mismatch** -- `c_n` enters after a gauge/shearing change or in
   a different variable, so `n^2` is not the input growth.
3. **Slope->level convention** -- if slope 1/2 does not map to `d = 2` under RSZ's
   convention, the table is read against the wrong `d`.

**Deliverable:** a stated identity `deg(input_n) = <expr>`, in the correct
variable after the correct gauge, plus the `d` making `deg(input_n) - deg(t_n)`
bounded.

**Falsifiable and worth recording either way:** if nothing bounds it even after
ramification, the RSZ route as currently mapped is wrong and the mapping must be
re-derived -- a genuine negative.

**Do this before investing in the analytic machinery** (S2/S3). The prune took
minutes; the route it guards is multi-session.

Plan: `docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md` (stage S1).

## RESOLVED 2026-08-08 — candidate (1): ramification is FORCED, and level 2 is the match

The three candidates are settled by the degree budget alone.

  input                          d=1 kernel   d=2 kernel
  unramified   (deg = n^2)         +0.50        +0.75
  ramified z=zeta^2 (deg = N^2/4)  -0.25        +0.0006 -> 0

Ramifying `z = zeta^2` (the pullback forced by the non-integral slope 1/2) puts
`c_m` at index `N = 2m`. Against the LEVEL-2 kernel there the match is critical,
and the leftover is not approximately zero but EXACTLY LINEAR:

    deg c_m = m^2,   exp(2, 2m) = m(m-1),   difference = m  exactly.

Linear (sub-quadratic) leftover is precisely the convergence condition. So the
resolving transform is **ramification THEN level 2** — which is the quantitative
reason RSZ's square roots `B1,B2` are forced rather than cosmetic bookkeeping.
The `d=1` ramified pairing over-converges (-0.25) and is not the canonical choice.

**PROVED in Lean, sorry-free:** `QOU.QBeta.ramified_qBorel_budget`
(`m^2 = m(m-1) + m`), composing `cCoeff_natDegree` with `qBorelExp_two_even`.
Axioms `[propext, Classical.choice, Quot.sound]`, no sorryAx.

Caveat retained: this is a DEGREE-budget determination, not a theorem about RSZ's
analytic construction. It fixes which pairing can converge; it does not by itself
construct the transform. S2 (`qou-qbr3`) is now unblocked and its target is
confirmed: the square roots of the slope blocks.
