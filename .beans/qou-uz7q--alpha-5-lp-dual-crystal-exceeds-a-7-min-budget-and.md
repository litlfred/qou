---
# qou-uz7q
title: alpha_5_lp_dual_crystal exceeds a 7-min budget and lacks the required progress logging — but editing it drifts scriptHash for zero payload change
status: todo
type: task
priority: normal
created_at: 2026-08-23T08:55:10Z
updated_at: 2026-08-23T16:27:09Z
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

## CORRECTION to my own count — "3 print sites in 426 lines" is wrong

Measured: **20** print sites, at lines 152, 166, 253–256, 286, 292, 296, 299,
302, 303, 306, 310, 316–318, 341, 353, 421. I wrote 3. The producer is not
silent, and I should not have said so without counting.

**The conclusion survives, on a different and narrower basis.** Two things are
actually true, and they are the ones that matter:

1. **No timing anywhere.** `grep -cE "elapsed|ETA|time\.time|perf_counter"` →
   **0**. AGENTS.md's long-compute rule asks for periodic progress *including
   wall elapsed + ETA*; prints without timing cannot tell you whether a run is
   at 5 % or 95 %. That requirement is unmet regardless of the print count.
2. **The expensive region is the silent one.** Prints at 292–318 sit inside the
   stratum/atom loops, so that section does report. But the q-sweep at
   **321–338** (`for q_v in q_sweep_q` × `for atom in atoms`) emits nothing
   until line **341**, after it finishes. A timeout landing inside that nest —
   which is where a q-sweep's cost lives — produces no output at all.

So: "violates the logging rule" holds; "carries only 3 print sites" does not,
and the difference is not cosmetic. The first is a claim about *where and what*
it logs, which I checked; the second was a number I asserted without measuring
and which anyone opening the file would have caught.

## The decision is unchanged

Do **not** add logging now. `scriptHash` is a whole-file hash, so a
logging-only edit drifts it while the payload stays byte-identical —
manufacturing staleness inside the audit that exists to measure it. Add the
timing in the same pass as the eventual re-run, paying the drift once. That
reasoning never depended on the print count.

## This is a class, not one producer

All four TIMEOUT producers, measured:

| producer | lines | print sites | timing refs |
|---|---|---|---|
| `alpha_5_lp_dual_crystal` | 426 | 20 | **0** |
| `binding_via_interface_knot` | 361 | 7 | 3 |
| `block_swap_binding` | 192 | 17 | 3 |
| `he3_tritium_cosh_asymmetry_diagnosis` | 130 | 14 | **0** |

Two of four carry no timing at all. Four of 33 measured producers (12 %) are
TIMEOUT, i.e. unmeasured — and the sweep cannot say how close any of them came
to finishing, which is the decision it would need to inform a budget raise.
