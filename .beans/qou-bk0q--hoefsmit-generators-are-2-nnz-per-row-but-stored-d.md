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
