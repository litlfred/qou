---
# qou-0y6l
title: Sweep L6a4 obstruction classes 2-13 with the saturated msolve pipeline
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T03:41:37Z
updated_at: 2026-09-06T10:26:59Z
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

## 2026-09-06 10:26 — the staircase route is CALIBRATED on a real corpus system

`gb_staircase.py` reproduces **L6a4 class 1 = dim 0, degree 4** from the Groebner
basis ALONE — no RUR, no parametrisation — matching the independently established
result (over Q, round-tripped witness, #6815 as corrected). Five hand-checked toy
ideals also pass. The tool can now be trusted on class 2.

**Timing, and it is informative.** GB only, 1 thread: **286 s** (10:21:22 →
10:26:08). Full RUR for the same class: 373 s. So for class 1 the Groebner basis is
most of the cost and the FGLM change-of-order is cheap — unsurprising at degree 4,
where the linear algebra is tiny.

**That sharpens what a class-2 timeout would mean.** My stated rationale for the
probe was that FGLM is 'routinely dominant' for a high-degree ideal. Class 1 does not
exhibit that, because its degree is 4. So if the class-2 GB also times out, the cost
is in the Groebner basis itself and no RUR budget helps; if the GB lands quickly, the
degree is large and FGLM was indeed the wall. Either outcome is diagnostic — which is
the property a blind longer run does not have.

**The verdict remains ASYMMETRIC** (recorded in the tool's own output): the FKR
reduction clears denominators via `numer(q.subs(x,-B/A))`, ADDING the locus {A=0},
so genuine solutions inject into the reduced system but not conversely. EMPTY would
be conclusive; NON-EMPTY is an upper bound only, and — the limitation I missed when
launching — a Groebner basis supplies no POINT, so a non-empty GB-only verdict cannot
be round-tripped at all without the RUR.
