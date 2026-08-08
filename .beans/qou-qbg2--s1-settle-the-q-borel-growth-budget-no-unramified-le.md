---
# qou-qbg2
title: 'S1: settle the q-Borel growth budget — no unramified level d absorbs deg_q(c_n)=n^2 (do BEFORE S2/S3)'
status: todo
type: task
priority: normal
created_at: 2026-08-08T08:05:00Z
updated_at: 2026-08-08T08:05:00Z
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
