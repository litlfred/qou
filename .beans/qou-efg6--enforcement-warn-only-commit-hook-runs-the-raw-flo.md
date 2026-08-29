---
# qou-efg6
title: 'Enforcement: warn-only commit hook runs the raw-float64 ratchet (the gate nothing invoked)'
status: completed
type: task
priority: normal
created_at: 2026-08-25T19:05:19Z
updated_at: 2026-08-25T19:06:13Z
---

Owner decision 2026-08-25: **warn on commit**; the push-side block was offered
and declined. Implemented as `scripts/precommit-precision-warn.sh`, a
`PreToolUse` hook on `Bash` in `.claude/settings.json`.

## The gap

`scripts/precision-gates.sh` is documented as THE gate — CI is
`workflow_dispatch`-only under the 2026-06-30 Actions-billing directive,
reaffirmed by the owner on 2026-08-09 with the failure cost on the table, and
AGENTS.md says not to re-propose the trigger without a new reason. I had no new
reason, so CI was never on the table here.

What was on the table: **nothing ever ran the gate.** Measured — `core.hooksPath`
unset, no `.githooks/`, and every reference to `precision-gates.sh` in the tree
is prose (docs plus the workflow's own comments). A gate nobody invokes is
documentation. `.claude/settings.json` already ran SessionStart and PostToolUse
hooks, so the mechanism existed and was simply unused for this.

## Two measurements decided the design

    witness_raw_float64_audit.py --strict   1.8 s     <- the only BLOCKING gate
    scripts/precision-gates.sh (all gates)  3 m 12 s

A `PreToolUse` hook runs BEFORE the tool call. Wiring the full family in would
add three minutes to every witness-touching commit, which buys avoidance rather
than safety. So the hook runs the ratchet only and names the full script for
everything else.

Second: the hook **always exits 0**. A `PreToolUse` hook exiting non-zero blocks
the tool call, and a bare container is the DEFAULT here — this session had to
`pip install` mpmath, numpy, scipy and clarabel — which is exactly when a
blocking hook would brick every commit. `precision-gates.sh` already separates
the cases (exit 1 real red, exit 2 "PREFLIGHT FAILED ... this is NOT a gate
failure"), and the hook mirrors that distinction in its wording.

## Two defects found by testing, not by reading

1. **Matcher false-positive.** The first separator class included plain
   whitespace, so `echo git commit` fired the audit — and would have printed a
   RED banner on a command that commits nothing. That is how a warning gets
   learned as noise. Tightened to require a real separator (`^ ; & | && ||`,
   newline via grep's line orientation). Battery 8/8 including
   `git commit-tree`, `echo "run git commit next"`, `git push`.
2. **Carve-out leakage.** `grep -E '^ +[0-9]+ +computations/'` also matched the
   DECLARED carve-out listings (float64-integrator, deprecated-f64, LP-dual), so
   the RED output listed four files that are fine above the one that was not.
   Replaced with an awk range anchored on the "NEW witnesses carrying raw
   float64" header.

Verified end to end against a fabricated dirty witness: fires, prints only the
real offender with its field count, exits 0.

## What this does NOT do

It covers ONE gate on the commit path. It does not replace the preflight, does
not run the advisory gates, and — being warn-only — can be ignored. It raises
the odds a dirty witness is noticed before it lands; it does not guarantee it.
The revolving door `qou-mnrd` documented is narrowed, not closed.
