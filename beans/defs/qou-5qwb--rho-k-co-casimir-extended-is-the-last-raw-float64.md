---
# qou-5qwb
title: rho-k-co-casimir-extended is the last raw-float64 REGRESSED red; only a full re-run clears it
status: completed
type: task
priority: normal
created_at: 2026-08-15T05:25:46Z
updated_at: 2026-08-19T21:03:33Z
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

## CORRECTION — it was NOT the environment. It was a one-character bug.

Everything in the section above is **wrong about the cause**, and the
conclusion it reached ("do not retry here; land it from a faster environment")
was wrong too. The per-atom ratios were real, but I attributed them to sandbox
hardware without checking, and that misdiagnosis nearly buried a live
performance defect as an environment limit.

**Actual root cause.** `hoefsmit_numpy.chi_numpy` is the declared float64/BLAS
path. `canonical_braid_crossings.d_for_ctype` returns a plain `float` for
`sigma`, `sigma_inv` and `averaged` — but an mpmath **`mpf`** for
`averaged_weighted`. In

    cross = sigma + d_val * eye
    M = M @ cross

one `mpf` promotes `cross` to `dtype=object`; `M` is reassigned from that
product, so **`M` stays `dtype=object` for every remaining crossing**. The loop
silently leaves BLAS and finishes in pure-Python matmul — permanently, not just
for the offending crossing.

Measured on tritium (n=9, dim=120, 35 crossings): the first `averaged_weighted`
crossing sits at index 11, where matmul cost jumps **0.0005 s -> 2.7 s** and
never recovers. One partition: **66 s -> 0.16 s** after the fix.

**What disproved the environment theory.** numpy here is healthy — a 600x600
matmul takes 5 ms. A 120x120 matmul cannot take 2.7 s on that machine unless it
is not really running in numpy. That single comparison was enough, and it was
available before I wrote "projects to two to four days."

**Fix.** `float()` the value at the `chi_numpy` boundary. Correct by
construction — that function *is* the float64 path (full precision is
`chi_numeric`), and the result is unchanged against the mpmath reference:
rel_diff 5.3e-15, 4.0e-15, 5.2e-16 on (5,2,2), (3,3,3), (4,3,2), all inside the
module's documented 1e-14 tolerance.

**Consequence.** The re-run is feasible here after all: the first five atoms
complete in ~45 s. The witness is no longer blocked on hardware.

**Lesson worth keeping.** "The environment is slow" is an unfalsifiable
explanation, and I reached for it after one 6-hour observation. A 148x gap on
arithmetic is a *bug-shaped* number, not a *hardware-shaped* one — hardware
does not vary by two orders of magnitude on the same instruction mix. The
disproving measurement (benchmark the primitive in isolation) costs seconds.

## The workaround was folklore: 4 of 5 consumers already cast

Audited every numpy-based `d_for_ctype` consumer after fixing `chi_numpy`:

| consumer | casts? |
|---|---|
| `atom_level_wedderburn_tower.py:88` | yes |
| `hoefsmit_symbolic.py:269` | yes |
| `spectral_coordinates_all_atoms.py:57` | yes |
| `canonical_tr_m_via_branching.py:151` | yes |
| `hoefsmit_numpy.py` (`chi_numpy`) | **no — the straggler** |

Four separate authors independently hit this and each patched their own call
site. Nothing enforced the convention and nothing communicated it, so the
fifth author had no way to know. The one place that missed it was, with some
irony, the module whose whole purpose is to be the fast BLAS path.

That makes it a **class**, not an instance, and the fix landed here only closes
the instance. Raised with the ctype owners on PR #5073 with two options: make
`d_for_ctype`'s return type uniform at source, or keep `mpf` and add a test
asserting all ctypes agree in type, so the next consumer fails loudly instead
of silently running 4000x slower with a correct answer.

Not decided here: `averaged_weighted` may need the extra precision at the
symbolic call sites, and that is the piece of context that picks between the
two — it belongs to the arc that owns the vocabulary.

## Third finding: He-4 does not fail on TIME, it fails on MEMORY

With the dtype leak fixed, the re-run reached helium-4 in ~45 s and the five
smaller atoms came out **faster than the committed witness**:

| atom | committed | after the fix |
|---|---|---|
| #3 | 0.34 s | **0.13 s** |
| #4 (tritium) | 9.28 s | **5.86 s** |
| #5 (He-3) | 9.45 s | **5.68 s** |

So the machine is not slow — it is ~1.6x *faster* than whatever produced the
committed values. The environment theory is dead twice over.

**He-4 then hung.** Not "ran long" — hung:

- **Zero CPU delta** across a 6-second sample on both workers
  (`00:08:20` and `00:10:07`, unchanged).
- Both blocked in `futex_do_wait`.
- RSS **4.8 GB and 5.1 GB** for two workers — ~10 GB of a 16 GB box,
  with 3.2 GB free.
- `khugepaged` pinned at 80 % (kernel hugepage compaction — the signature
  of memory pressure, not of arithmetic).

Killing the run returned the box from 11.2 GB used to 6.1 GB.

So the He-4 atom (n=12, 77 partitions) exceeds available memory at the
default **4 workers**. The wall-clock reading was a symptom; the constraint
is RAM per worker times worker count.

### What to try next, in order

1. **Fewer workers.** `--atoms` exists but worker count is currently
   hardcoded at 4. One or two workers may fit in 16 GB and finish. This is
   the cheapest experiment and needs no code change beyond the pool size.
2. **Measure per-partition peak RSS at n=12.** 5 GB *per worker* is much
   larger than a float64 Hoefsmit matrix set should need, so there may be a
   second, memory-shaped defect in the n=12 path — worth measuring before
   assuming the size is inherent.
3. Only then conclude anything about hardware.

### Discipline note

This is the **third** cause proposed for the same symptom: environment (wrong),
dtype leak (real, and worth 4000x, but not the whole story), and now memory
(the actual blocker for this atom). Each earlier diagnosis was stated with
more confidence than the evidence supported. The lesson is the same one the
600x600-matmul check taught: measure the specific resource before naming it.

## CLOSED — verified on main 2026-08-19

The witness is clean and the ratchet is green:

    atoms: 6      raw float64: 0
    NEW dirty: 0  REGRESSED: 0   (48 files / +4,264 fields drained since baseline)

The run that finished it was `qou-9br4`'s (their item, now completed). What
made it finishable is recorded here for the causal chain, because the timings
are the evidence that the two fixes in this bean mattered:

| atom | committed (pre-fix) | after the fixes | ratio |
|---|---|---|---|
| #3 | 0.34 s | 0.08 s | 4x |
| tritium | 9.28 s | 0.43 s | **21x** |
| He-3 | 9.45 s | 0.19 s | **50x** |
| **He-4** | 2533 s | **734 s** | **3.5x** |

He-4 went from ~42 min to ~12 min, and its per-worker footprint from 5.22 GB
of dense generators to ~1 GB. Two prior attempts had been killed at that atom.

Contributing fixes, all merged: the `mpf` -> `dtype=object` leak in
`chi_numpy` (#5089), the `--workers` cap (#5104), and the P22 structured
auto-switch above dim 1200 (#5152).

Three wrong diagnoses preceded the right one — "the sandbox is slow" (it was
a dtype leak), "~14 minutes left" (it was hung), "flop count implies speedup"
(it was bandwidth-bound, and then the crossover reversed even that). All are
kept above rather than deleted; the shared failure was naming a mechanism
without measuring the resource it implicates.
