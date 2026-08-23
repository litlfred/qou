---
# qou-uz7q
title: alpha_5_lp_dual_crystal exceeds a 7-min budget and lacks the required progress logging — but editing it drifts scriptHash for zero payload change
status: todo
type: task
priority: normal
created_at: 2026-08-23T08:55:10Z
updated_at: 2026-08-23T08:55:40Z
---

Surfaced by the #5519 staleness sweep. `computations/alpha/alpha_5_lp_dual_crystal.py`
is TIMEOUT at a 420 s per-producer budget — twice, at 300 s and at 420 s.

## Genuinely long, not hung
Static read: the dominant structure is `for sub in combinations(eigs, ell)`
(line 133) over the cells of partitions with `height == 6` (line 183) — a
combinatorial enumeration, so a long wall time is expected rather than
suspicious.

## It lacks the progress logging AGENTS.md requires
Only 3 flush/print sites in 426 lines. The long-compute discipline requires any
> 5 min script to emit a progress line every ~10 s or ~5 % of work, with wall
elapsed + ETA. Because it does not, **I cannot say how far it got before the
budget expired, or what its true runtime is** — which is precisely the cost the
discipline exists to prevent.

## Why I did NOT just add the logging
Adding a print statement changes the file, which changes `scriptHash` — a
whole-file hash. AGENTS.md is explicit that a comment- or logging-only edit
drifts `scriptHash` while the recomputed payload is byte-identical, and that for
a LONG-COMPUTE producer the right move is to claim it as a bean rather than
spend the pass recomputing numbers that cannot change. Editing this file would
therefore manufacture staleness in the exact audit this branch exists to measure,
and would then demand an expensive re-run to clear the drift it caused.

## What closing this actually needs
1. Measure its true runtime with a generous budget, on its own, teed to a log
   (`python3 -u ... 2>&1 | tee`), so the number is known rather than bounded.
2. THEN decide: if it is minutes, raise the sweep budget and move on. If it is
   hours, it needs a long-compute plan before it can be regenerated in EITHER
   #5519 or #5500 — and the logging should be added in the same pass as the
   re-run, so the scriptHash drift is paid for exactly once.

Until (1), its staleness is UNMEASURED. That is not the same as UNCHANGED, and
it must not be reported as either.
