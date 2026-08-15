---
# qou-5qwb
title: rho-k-co-casimir-extended is the last raw-float64 REGRESSED red; only a full re-run clears it
status: todo
type: task
created_at: 2026-08-15T05:25:46Z
updated_at: 2026-08-15T05:25:46Z
---


## State (2026-08-15)

On `main` the raw-float64 ratchet reports **NEW dirty 0, REGRESSED 1**, and the
one regression is `computations/rho-k-co-casimir-extended.witness.json`
(baseline 3 -> 4).

**The producer is already correct.** `rho_k_co_casimir_extended.py:354` emits
`"compute_wall_sec": f"{t1 - t0:.2f}"` — a string. Commit `29b209ce93` fixed it.
The committed witness simply predates that fix, so four `compute_wall_sec`
values are still raw float64 (`0.34`, `9.28`, `9.45`, `2533.2`). There is no
code change to make; only a full re-run rewrites those fields.

## Cost, measured rather than estimated

A re-run in this sandbox ran **100+ minutes without completing**, against a
committed worst-atom time of `2533.2 s` (42 min). Sequence observed:
deuteron/He-3 fast, tritium (n=9, 30 partitions) ~25 min, then helium-4 (n=12,
77 partitions) still running at 66 min. This machine is materially slower than
whatever produced the committed witness — budget well over an hour, and launch
with `2>&1 | tee` per the long-compute logging discipline.

## The trap — do not measure this witness mid-run

The producer **writes the witness after each atom**, so mid-run the file is
gutted. Twice it scored **0 raw floats** and made the ratchet report
`REGRESSED: 0`. Committing that would have been a false green *and* would have
destroyed the witness (`durationMs` 2552837 -> 519, 2272 deletions).

Check `durationMs` and the `per_atom` count (should be 6) before trusting any
measurement of this file. Root cause is bean `qou-0vn0`: the ratchet counts raw
floats, so an **empty** witness scores identically to a **clean** one.

## The re-run is NOT feasible in this sandbox — measured, then abandoned

A second attempt was killed after **6 hours**. It is not a matter of waiting
longer. Comparing the partial output against the committed witness, atom by atom:

| atom | committed `compute_wall_sec` | this sandbox | ratio |
|---|---|---|---|
| #3 | `0.34` | `0.35` | 1x |
| #4 (tritium, n=9) | `9.28` | `1373.82` | **148x** |
| #5 (He-3, n=9) | `9.45` | `698.07` | **74x** |
| #6 (helium-4, n=12, 77 partitions) | `2533.2` | killed at **21,600+** | > 8x and climbing |

At a 74-148x penalty on the mid-size atoms, the He-4 atom's committed 2533 s
projects to **two to four days**. The run was killed at 6 h with He-4 still in
its first write.

Two things this settles:

1. **The fix itself is confirmed correct.** The partial run wrote
   `'0.35'`, `'1373.82'`, `'698.07'` — strings, as the producer intends. Nothing
   is wrong with the code; the only blocker is wall time.
2. **Do not retry here.** Land this from an environment that reproduces the
   committed timings, or leave the red standing and say so. Re-running it in a
   sandbox burns hours and produces a gutted witness that scores a false green
   (see `qou-0vn0`).

Working tree was restored to HEAD after the kill; the committed witness is
intact (6 `per_atom` entries, original values).
