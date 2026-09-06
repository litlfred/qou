---
# qou-0y6l
title: Sweep L6a4 obstruction classes 2-13 with the saturated msolve pipeline
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T03:41:37Z
updated_at: 2026-09-06T09:05:43Z
---

## 2026-09-06 — why three class-2 attempts produced no verdict, and the fourth is running

**None of the three failures was mathematical.** Each died when the filesystem
filled; the third took its own log with it, so its outcome is unknowable.

**Root cause (not the solve).** `scripts/setup-lean-toolchain.sh` runs as a
SessionStart hook and re-stages **5.0 GB** of Lean on every resume — a 697 MB zip
it never deletes plus a 4.3 GB extract, into `/tmp`, which does not survive a
container. Quota ~38 GB, resident repo ~33 GB: **33 + 5 = 38.** One resume fills
the container with no compute running. Fixed in `1432473982` (drop the zip after
extract; refuse to stage below ~6 GB free). Verified on the next resume — no
re-stage, disk held at 5.0 GB.

**A full disk is not a degraded session, it is a dead one:** the harness cannot
write a child's stdout, so every command fails including the `rm` that would fix
it. Reached <100 KB free twice.

**Caps for the fourth attempt are asymmetric on purpose** (15 GB RAM / 13 free,
5.0 GB disk): `ulimit -v` 10 GB generous — an OOM kill is survivable;
`ulimit -f` 1 GB tight — a runaway `.res` is not. Capping memory tightly was my
first draft and is the wrong instinct: it constrains the plentiful resource.

**Two corrections of my own.**
1. Class 2 keeps **11 variables** vs class 1's 12 — my original figure. My
   "correction" to 12/13 was wrong: that is the `.ms` header, which also counts
   msolve's linear form `u`. Two conventions, not a discrepancy. Confirmed live by
   the run: `eliminated 16 -> 11 vars, 17 eqs, maxdeg 12, 129.6s`. Better size
   signal: **59,475 bytes vs 10,225 — 5.8x the polynomial data.**
2. The sibling branch's class-1 result is **not** independent confirmation. Both
   result commits are patch-identical across the branches
   (`c6622b885874`, `359769e26b60`) — same patches, different SHAs after rebase.
   One computation, not two. Class 1's real evidence stays its **round trip**.

**Whatever class 2 returns is PROVISIONAL.** The driver lets elimination consume
`t` and re-imposes the non-zero condition only on surviving variables, so it does
not restore it by construction — eliminated coordinates' denominators can still
vanish at a solution. No dimension/degree may be reported until
`ptolemy_exact_character.py` round-trips a point against snappy's original
equations. That gap is exactly what forced the class-1 retraction in #6815.
