---
# qou-pag7
title: sublemma_2_1_h12_he4_phase25 builds and lambdifies all 77 H12 reps to read 77 integers — 67 h of work for a hook-length formula
status: completed
type: bug
priority: normal
created_at: 2026-08-23T16:11:29Z
updated_at: 2026-08-23T17:10:47Z
---

This is why the H12 ⁴He producer is listed "Not run" in PR #5517, and it is
not #5517's fault. Measured, not argued.

## The loop

`computations/sublemma_2_1_h12_he4_phase25.py` lines 79-83:

    parts_12 = partitions_of(12)
    dims = []
    for lam in parts_12:
        _, d = _compiled_sigmas(lam, "double")
        dims.append((lam, d))

It builds the **full seminormal rep** for every one of the 77 partitions of 12
— then keeps `d`, the dimension, and throws the matrices away. `d` is the
hook-length formula: exact, instant, no rep required.

## Cost, measured

`py-spy dump` on the live process found it inside a single `sp.lambdify`, in
sympy's *string printer*, 109 minutes in:

    precedence_Float (sympy/printing/precedence.py:86)
    ...
    _recursive_to_string (sympy/utilities/lambdify.py:989)
    lambdify (sympy/utilities/lambdify.py:894)
    _compiled_sigmas (computations/substrate/char_fast.py:156)

Timing `_compiled_sigmas(lam, "double")` per shape, both sides of #5517,
sequentially on an otherwise-idle box:

    dim    branch point    #5517 head   speedup
     54          1.48s         0.69s      2.14x
    132          8.66s         3.04s      2.85x
    165         13.32s         4.38s      3.04x
    275         36.71s        11.29s      3.25x
    330         53.58s        15.77s      3.40x
    462        107.41s        30.67s      3.50x
    616        >120s (timeout) 53.7s
    891              --       110.36s

Cleanly quadratic in dim on both sides. Fitted `t = c·dim²`:

    branch point   c = 5.03e-4
    #5517 head     c = 1.39e-4     (3.62x smaller)

And the total is **exact**, because `Σ_{λ⊢n} (dim λ)² = n!` (Burnside):

    Σ dim² over λ ⊢ 12  =  479,001,600  =  12!     (verified)

    projected cost of the loop, branch point:  67.0 h
    projected cost of the loop, #5517 head  :  18.5 h

Largest single shape is dim **7700**, i.e. ~2.3 h alone even after #5517.

## What this settles

1. **The producer is unrunnable in a session on EITHER side.** Nobody has been
   hiding a result; 67 h (or 18.5 h) is the entry price for 77 integers.
2. **#5517 helps a lot and is not the problem.** 3.6x, and the ratio grows with
   dim (2.1x at 54, 3.5x at 462), which extends the PR's own n=6 speed claim
   (7.5s -> 3.6s) to H12. It does not make the producer feasible.
3. **The 9.86 GB OOM was lambdify's working set, not a memory regression.**
   Both runs were inside `sp.lambdify` holding a printed source string for one
   shape. With 3.6x the throughput the head run was further into the 77 at the
   moment of the kill, so a larger resident set is expected. No memory
   comparison between the two versions is claimed — the runs were concurrent
   and are not comparable that way.

## Fix

Replace the call with the hook-length formula, or
`pyhecke.wedderburn.partition_dimension` which the corpus already uses
(`chi_at_q0_via_hoefsmit_mpfr.py:327`). The harness for the numbers above
computes all 77 dimensions in microseconds. Then `--max-dim` filtering happens
before any rep is built, and only the selected shapes cost anything.

Only after that is it worth asking whether the producer's real work is
feasible — this loop is pure overhead and hides the answer.



## Fixed

Swapped to `pyhecke.wedderburn.partition_dimension` after verifying it equals
the discarded `d` on all 66 partitions of n <= 8 and six H_12 shapes (zero
mismatches). The producer now runs end to end in **2 s**.

What that revealed is filed separately as `qou-ag9p`: with the loop out of the
way, the producer verifies **0 of 0** and writes a passing witness, because its
Path A cache key has never existed in the file it reads. Fixing the cost did not
make it verify anything, and the two should not be conflated.
