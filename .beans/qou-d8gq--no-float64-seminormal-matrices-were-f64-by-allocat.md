---
# qou-d8gq
title: 'NO-FLOAT64: seminormal matrices were f64 BY ALLOCATION — np.zeros() truncated every mpf entry'
status: completed
type: bug
priority: normal
created_at: 2026-08-16T13:45:22Z
updated_at: 2026-08-16T13:45:22Z
---

## The defect

`pyhecke/syt_prefix_cache.py::build_seminormal_matrices_cached` allocated

    M = np.zeros((dim, dim))        # float64

and then filled it with `M[r, c] = v`. When `v` is an `mpf`, numpy **silently
truncates it to 53 bits**. So the Hoefsmit seminormal representation came back
float64 *no matter what `q_val` was handed in* — a caller passing
`q_parameter.Q_MP` got bit-identical output to one passing the f64 `Q`.

Measured before the fix:

    q as f64 : build 0.01s  dim=162  dtype=float64  entry type=float64
    q as mpf : build 0.01s  dim=162  dtype=float64  entry type=float64   <-- destroyed

## Why it is worse than a plain precision loss

`mass_at_3A_proper.per_generator_V_hat_3A` multiplies these matrices against an
**mpf braid word** (19 of 35 steps carry an mpf since `efcaf79ed`):

    M = M @ (c * sigmas[i] + d * I_lam)

`c * float64_array + mpf` promotes the RESULT to `dtype=object`, so the matmul
leaves BLAS for Python-level mpmath. Measured at dim=162:

    3 matmuls:  as-is 18.928s   forced float64 0.0295s   ratio 642x

That is bean **qou-5qwb**'s failure mode. The computation was paying full
mpmath cost while carrying only float64 information — laundered precision AND
the slow path. It is why `per_generator_V_hat_3A` cannot reach 3A = 9
(qou-2tuv) while 3A = 6 takes 0.6 s.

## The fix, and the direction it deliberately does NOT take

The tempting fix — cast the braid word down to f64 at the matrix boundary —
would remove the leak and give a 642x speedup. **It is the forbidden
direction** (NO FLOAT64) and it was my first recommendation; the owner
rejected it, correctly. The matrices being f64 is the bug, not the mpf meeting
them.

Fixed at the allocation:

    M = np.zeros((dim, dim), dtype=_value_dtype(vals))

`_value_dtype` returns `float` when every entry is a plain float/int and
`object` otherwise, so the decision follows the values rather than a new flag.

    q as f64 : dtype=float64  entry type=float64   (unchanged, BLAS kept)
    q as mpf : dtype=object   entry type=mpf       (precision preserved)

**Existing f64 callers are bit-identical and no slower** — verified: the full
deuteron comparison table reproduces to the last digit after the change.

## What this does and does not buy

It removes the *silent destruction*: high precision is now possible when
requested. It does NOT by itself make `mass_at_3A_proper` correct, because that
module still seeds its cache from the f64 `Q0`
(`_cached_seminormal` -> `stem_name = f"n{n}_q{Q0:.10f}_..."`), so it still gets
float64 matrices and still leaks when the mpf braid word arrives.

Switching it to `Q_MP` is now MEANINGFUL where before it was a no-op — but it
will be slow, because honest mpf matmul at dim 162-216 is what the 642x
measures. That trade (correct and slow vs fast and forbidden) is the real
decision, and it is the owner's.

## Gate gap

`numpy_mpmath_dtype_leak_audit.py` is blocking and reported **0 candidates**
throughout, including with the leak live. Its scope is `d_for_ctype` consumers
and `hoefsmit_numpy.py`; it does not look for `np.zeros(...)` allocations that
later receive mpf. `computations/f64_into_mpmath_audit.py` DOES name this shape
in prose — "`BlockCache(float(Q0), float(HA_VAL))` seeds a cache with doubles"
— but it is **not wired into `scripts/precision-gates.sh`**, so nothing ran it.
Two separate gaps, both worth their own item.
