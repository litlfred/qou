---
# qou-p2ka
title: 'VERIFY: A2 residual at the refreshed sample point (qou-vbw1 leftover)'
status: completed
type: task
priority: normal
created_at: 2026-08-08T04:00:00Z
updated_at: 2026-08-08T04:00:00Z
---

The one claim from PR #4513 that is **stated but not verified**. Filed so it is
not lost, per the "bean the gap" rule rather than quietly leaving it.

## What is unverified

Commit `dbbe12fd` (qou-vbw1, last consumer) changed one line in
`computations/probes/qbeta_3bp8_annihilator_continuation_probe.py`:

    0.8 * e^{2i * 0.20323503}          (stale typed theta)
 -> 0.8 * e^{2i * theta_t4("proton")}  (derived, 0.20313250701827611...)

Phase A1 re-ran GREEN (max rel residual 6.55e-15; A1s scaling 1.15e-15 @1600 ->
1.35e-28 @2400). **A1 does not touch the changed line.** Phase A2 does, and A2
has never completed since the change.

## Why it did not complete

Three attempts. Two full-probe runs were killed by container restarts (~40 min
into A2, at 99.6% CPU — progressing, just slow). The cost is the `I(m,e)` cache
over `m in [-2,3] x |e| <= 60` at `ORD_SEQ = 1600`: 726 values, and large `|e|`
is far more expensive than A1's `|e| <= 3` grid (0 of 726 completed in ~3 min).
It needs longer than this environment's restart interval.

## What was tried and REJECTED as uninformative

A reduced-settings proxy (ORD=400, e-window +/-12) ran to completion and gave
`ratio new/old = 0.9989`. **Do not cite this as verification.** Both residuals
came out at O(0.8) — window-truncation dominated, exactly as the probe's own
comment warns ("the first run's O(10) A2 residual was WINDOW TRUNCATION at
near-boundary points"). A 0.1% delta between two truncation-dominated numbers
says nothing about the converged 1e-15-scale residual.

## The structural argument (an ARGUMENT, not a verification)

Recorded because it is the reason the change is expected inert — and labelled
so nobody promotes it to a check:

  * `I(m,e)` is cached and independent of `w`, so both points reuse identical
    sequence values; only `w` differs.
  * The two moduli are **exactly** equal: `| |w_old| - |w_new| | = 0.0` at 60
    dps (both 0.8). Every convergence/window condition in the probe is stated in
    terms of `|w|`, so the convergence regime is bit-identical.
  * Only the phase moves, by 2.05e-4 rad.
  * The identity `g_L = 0` is exact, so the converged residual is set by
    truncation, which is `|w|`-controlled and therefore unchanged.

This makes a regression unlikely. It does not make it checked.

## HOW TO FINISH IT (resumable harness committed)

`computations/probes/qbeta_3bp8_a2_sample_point_delta_check.py` runs A2 at the
probe's REAL settings (ORD_SEQ=1600, E_GF=60) for both the old and the new
sample point from one shared cache, and **persists the `I(m,e)` cache to
`.a2_icache.json`** (gitignored) so a restart resumes instead of restarting.
Just re-run it until it prints the verdict:

    nohup python3 -u computations/probes/qbeta_3bp8_a2_sample_point_delta_check.py \
        > .a2_run.log 2>&1 &

It reports `A2 verdict unchanged by the substitution: True/False`. If False,
`dbbe12fd` needs a follow-up commit (not a quiet amend — the commit message
already promised that).

Alternatively run the original probe end-to-end anywhere with >2h of
uninterrupted wall time; that is the authoritative check.

## Honesty note

`dbbe12fd`'s message already states this verification status plainly, and PR
#4513's test plan does not claim A2 as passed. Nothing in the corpus asserts a
green A2 for the new point.

---

## CLOSED 2026-08-08 — A2 RE-RUN COMPLETED, VERDICT UNCHANGED

The resumable harness finished (4696s wall, 726 I(m,e) values at ORD_SEQ=1600,
E_GF=±60, dps=70), resuming across two container restarts as designed.

    old (typed, stale theta 0.20323503)   max rel residual = 1.6703807e-10
    new (derived theta 0.20313250701828)  max rel residual = 1.6719466e-10
    A2_TOL = 1e-8  ->  both PASS
    A2 verdict unchanged by the substitution: TRUE   (ratio 1.0009375)

So commit `dbbe12fd` (qou-vbw1, last consumer) is verified: refreshing the A2
sample point from the stale typed theta to the derived one moved the residual by
0.09% and changed no verdict. `qou-vbw1` is now fully verified, all 4 remaining
consumers included.

## The structural argument was right, and is now confirmed rather than assumed

This bean recorded an ARGUMENT for why a regression was unlikely — identical
modulus (`| |w_old| - |w_new| | = 0.0` at 60 dps), `I(m,e)` independent of `w`,
every convergence condition stated in terms of `|w|`, so only the phase moved by
2.05e-4 rad. That predicted a tiny, non-verdict-changing shift. Measured: 0.09%.

Worth keeping the distinction the bean drew: the argument was **not** treated as
a check, and the PR's test plan did not claim A2 as passed. It is passed now
because it was run, not because it was reasoned about.

## Also confirmed: the reduced-settings proxy was RIGHT to be rejected

This bean recorded a proxy run (ORD=400, window ±12) giving ratio 0.9989, and
rejected it as uninformative because both residuals came out truncation-dominated
at O(0.8). The converged run gives residuals of 1.67e-10 — **nine orders of
magnitude smaller**. The proxy's numbers were meaningless as absolute values,
exactly as recorded. Its ratio happened to be in the right ballpark (0.9989 vs
1.0009), but that was luck, not signal.

The harness stays in the tree (`qbeta_3bp8_a2_sample_point_delta_check.py`) —
it is a working example of a resumable long-compute that survives container
restarts, which the long-compute discipline in AGENTS.md has no other instance of.
