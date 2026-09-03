---
# qou-6v5l
title: sw_period_eq_residue_sum is a conclusion-typed projection, and its stated justification misuses the residue theorem
status: completed
type: task
priority: normal
created_at: 2026-08-29T19:38:22Z
updated_at: 2026-08-29T19:49:54Z
---

RESOLVED 2026-08-29, PR #6067, branch claude/sw-period-residue-sum-projection-2026-08-29.
Found working qou-u8oy input (2), the non-abelian-Stokes keystone.

TWO DEFECTS in prop:sw-period-residue-sum.

1. sw_period_eq_residue_sum's statement IS the type of SWPeriodResidue.period_eq
   and its proof is := S.period_eq -- the self-assuming projection AGENTS.md
   3b-cond item 5 names. Already machine-flagged: lean-triviality.json carries
   the file as "closed": false since 2026-08-07, never agent-adjudicated, and
   absent from lean-vacuity-review-ledger.json entirely.

2. The warrant was the residue theorem read backwards. On a COMPACT Riemann
   surface the residues of a meromorphic 1-form SUM TO ZERO; the block summed
   over all p in S_c and called that the period, which forces a_D^(n) = 0 at
   every level. And P1 has H_1 = 0, so the proof block's "period over the
   generating cycle of S_c" does not exist. Only a bounding cycle has a
   residue-sum value, over the ENCLOSED poles.

NOT A DISCOVERY. prop:sw-classical-jet-exactness already holds period = 0 via
exactness (lambda = d(X^(n-1)), each residue vanishing individually), correctly
scoped scope-(b) on the classical-jet reading. The corpus-grep found it before
anything was written up as new. The lemma added here assumes strictly less
(only the TOTAL vanishes) and is driven by the ambient surface rather than the
jet rule -- a second route.

MEASURED. Colour cubic disc_X is squarefree of degree 6 => pole locus is
exactly 6 points, n-independent (three conjugate pairs |z| = 0.943, 1.000,
1.061, reproducing lever1_sw_period_lw_rate_refine). So the "residue family at
level n indexed by the weight data of rank n" reading needs p(n) <= 6 and
fails from n = 5. Scope-(b) against the BIJECTION only -- not against the
equality a_D^(n) = lw(n-1), since 6 numbers can sum to what 11 sum to.
Separately: the colour cubic is a smooth plane cubic, so genus 1 -- real
periods exist, but not on the genus-0 S_c where the block puts them.

SHIPPED: period_eq_zero_of_total_residue_vanishes + contrapositive (derived,
sorry-free, verified non-vacuous -- S.period = 0 needs sorry without the
hypothesis); both .md re-scoped to an enclosed subset E with E's identity named
as the open content; audit doc. sw_period_eq_residue_sum kept (downstream prose
cites the proposition by name) with an honest docstring.

LEFT FOR THE AUTHOR: no agent verdict added to lean-vacuity-review-ledger.json.
That is the prescribed way to clear a lean-triviality candidate, but
self-clearing it inside the PR that changes the file wants a second reader.

KEYSTONE UNCHANGED: still a 3b class with no instance. Only the residue-sum
route's overclaim is removed.
