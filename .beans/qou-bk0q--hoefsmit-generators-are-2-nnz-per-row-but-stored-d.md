---
# qou-bk0q
title: Hoefsmit generators are 2-nnz-per-row but stored DENSE — 5.2GB and O(dim^3) where O(dim^2) suffices
status: todo
type: task
created_at: 2026-08-15T12:17:14Z
updated_at: 2026-08-15T12:17:14Z
---


## Measured

`hoefsmit_matrices_numpy` allocates `np.zeros((dim, dim), dtype=np.float64)`
per generator. The matrices it fills are structurally **at most 2 nonzeros per
row** — a diagonal entry plus, when the swap partner exists, one symmetric
off-diagonal pair. Measured at q0:

| λ | dim | nnz/matrix | dense entries | density | max nnz/row |
|---|---|---|---|---|---|
| (5,2,2) | 120 | 188 | 14,400 | 1.31 % | **2** |
| (6,6) | 132 | 192 | 17,424 | 1.10 % | **2** |
| (4,4,4) | 462 | 714 | 213,444 | 0.34 % | **2** |

Density falls as dim grows, so the waste is worst exactly where it hurts.

## Why it matters — this is what blocks He-4

Partitions of 12 reach **dim 7700** (λ = (5,3,2,1,1)). Eleven dense generators
at 7700² × 8 B = **5.22 GB**, which matches the 4.8 GB / 5.1 GB RSS measured on
the two hung workers (see qou-5qwb). With the default 4 workers that is ~20 GB
on a 16 GB box, so the run does not merely slow down — it **hangs** in
`futex_do_wait` with `khugepaged` thrashing.

So the memory wall recorded in qou-5qwb is not inherent to the mathematics. It
is inherent to storing a 2-per-row matrix densely.

## Both resources, not just memory

With ≤2 nonzeros per column, `M @ cross` is O(2·dim²), not O(dim³):

| dim | dense matmul | sparse-aware | ratio |
|---|---|---|---|
| 462 | 9.9e7 flops | 4.3e5 | ~230x |
| 7700 | 4.6e11 flops | 1.2e8 | **~3900x** |

At dim 7700 a dense matmul is ~30 s at 15 GFLOPS, times 47 crossings ≈ 24 min
for ONE partition of 77. That is the real He-4 cost, and it is avoidable.

## No new dependency needed

scipy is absent in this sandbox (it IS in the recorded environment, but a core
compute module should not start requiring it). The structure does not need a
sparse library:

    cross = diag  +  symmetric pairs (i, j, b)

    (M @ cross)[:, j] = M[:, j] * diag[j]  +  M[:, i] * b
    (M @ cross)[:, i] = M[:, i] * diag[i]  +  M[:, j] * b

i.e. scale every column by the diagonal, then two vectorised column-adds per
pair. Pure numpy, still vectorised, no Python inner loop.

The accumulator `M` stays dense (dim × dim = 474 MB at dim 7700) unless the
trace is computed column-by-column, which would drop it to O(dim). That is a
second, larger step; the generator storage is the cheap 1900x win.

## This is P22, unimplemented

The compute-audit catalogue already names it: *"P22. Sparse representation when
nnz < 0.1·dim² for Hoefsmit matrices. `build_seminormal_matrices_cached`
already auto-switches at dim>500; instrument lower-dim callers to confirm
threshold."* The numpy path never got the switch — so the module written to be
the FAST path is the one missing it, the same shape as the dtype leak
(qou-5qwb), where four of five consumers had the guard and the fast path did
not.

## Before implementing

Validate against the current `chi_numpy` on many partitions (it is the
reference), benchmark per P28, and check whether `_HOEFSMIT_NUMPY_CACHE`
keying needs to change when the stored object is no longer an ndarray.

## Prototype built and measured — MEMORY confirmed, SPEED refuted

`computations/hoefsmit_sparse_prototype_probe.py`. Correctness first: the
structured path reproduces `chi_numpy` to **6.8e-16 worst case** across five
tritium partitions and 1.5e-15 at dim 891 — machine epsilon, as expected for
the same arithmetic in a different summation order.

| dim | generator memory | ratio | chi dense | chi structured |
|---|---|---|---|---|
| 297 | 7.8 MB -> 0.046 MB | **170x** | 0.04 s | **0.08 s** |
| 891 | 69.9 MB -> 0.139 MB | **503x** | 0.56 s | **0.75 s** |

### The speed claim above is WRONG — retracted

The earlier section argued "~3900x fewer flops at dim 7700" and implied a
matching speedup. Measured, the structured path is **1.3x to 2x SLOWER**.

Flop count was the wrong model. `M * diag[None, :]` is a full dim^2 multiply,
and each pair update does `M[:, I]` — a fancy-index gather that **copies** a
dim x (dim/2) array. So the step is ~3 dim^2 element-ops with poor locality,
against a dim^3 BLAS kernel that runs near peak. Memory bandwidth, not
arithmetic, is the binding constraint, and BLAS wins that comparison at every
dim tested.

This is the same error shape as the "sandbox is slow" call in qou-5qwb:
a plausible model asserted without measuring the thing it predicts.

### What survives, and it is enough

The memory reduction is real, large, and GROWS with dim (170x -> 503x). That
alone is what unblocks He-4:

  * generators at dim 7700: 5.22 GB -> ~10 MB
  * accumulator M stays dense: 474 MB, plus one temporary for `out`
  * per worker: ~5.7 GB -> ~1 GB

which fits 4 workers in 16 GB instead of hanging at ~20 GB.

So the correct framing is **a memory fix that makes an unrunnable atom
runnable**, at a ~1.3-2x compute cost — not a speedup. Whether that trade is
worth taking is a real question, and the honest alternatives are:

  1. Structured generators, dense accumulator (this prototype) — unblocks He-4,
     pays ~1.5x compute.
  2. Fewer workers with the dense path — unblocks He-4, pays 4x wall on the
     parallel part, changes no code.
  3. Build dense but only for the dims where it fits, structured above a
     threshold — the P22 "auto-switch at dim>500" shape, keeping BLAS where
     BLAS wins.

Option 3 is the one P22 actually describes and is probably right, but it needs
the crossover measured rather than guessed — the two data points here bracket
it poorly, and 297 vs 891 both favour dense.

### Not yet measured

Whether the O(dim^2) SYT partner search in the builder (P21) dominates at
dim 7700 — at that size it is ~59M comparisons per generator in pure Python,
which may exceed everything discussed above. Measure before optimising the
matmul further.
