---
# qou-qbg2
title: 'S1: settle the q-Borel growth budget — no unramified level d absorbs deg_q(c_n)=n^2 (do BEFORE S2/S3)'
status: scrapped
type: task
priority: normal
created_at: 2026-08-08T08:05:00Z
updated_at: 2026-08-08T11:35:00Z
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

## INTERPRETATION WITHDRAWN 2026-08-08 (same day) — see qou-qbp5

The arithmetic here is fine and the Lean theorem stands:
`QOU.QBeta.ramified_qBorel_budget : m^2 = m(m-1) + m`, sorry-free.

What is withdrawn is the **reading** of it. This bean concluded "ramification is
forced, and level 2 is the matching kernel" for C1. That used `d = 2` on the
strength of the 08-01 audit's "slope 1/2 => level d = 2 (denominator)". RSZ p.38
in fact defines `d := mu_2 - mu_1 in N` -- the **difference between two
consecutive slopes** -- and §3.3 is titled "in the case of INTEGRAL slopes".

C1 has ONE slope, and it is not integral. So there is no RSZ level `d` for C1's
infinity in this sense, and "the level-2 kernel is the resolving transform for
C1" is not supported.

**Honest residue.** What survives is a statement about the two functions, with no
claim that either is C1's resolving transform: the exponent sequence `m^2` sits
exactly `m` above the sequence `qBorelExp 2 (2m) = m(m-1)`. That is a true and
mildly interesting numerical fact; it is NOT evidence that `B_{q,2}` resolves C1.

Do not cite this bean as establishing the transform. Re-open only if `qou-qbp5`
resolves in a way that restores a level to C1's infinity.

## VOID 2026-08-08 — see docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md

The growth budget presupposed an RSZ level `d` for C1's infinity. There is none:
§3.3 is integral-slopes-only and its `d` is the slope DIFFERENCE `mu_2 - mu_1`.
The Lean theorem `ramified_qBorel_budget` (`m^2 = m(m-1) + m`) remains TRUE and
stands; only its interpretation as C1's resolving transform is void.
