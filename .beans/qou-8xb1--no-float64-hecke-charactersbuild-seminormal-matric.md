---
# qou-8xb1
title: 'NO-FLOAT64: hecke_characters.build_seminormal_matrices still f64-bound (qou-d8gq fixed only the pyhecke twin)'
status: todo
type: bug
priority: normal
created_at: 2026-08-25T16:38:19Z
updated_at: 2026-08-25T16:38:59Z
---

## Found 2026-08-25 while draining the 5 NEW raw-float64 witnesses on main

`qou-d8gq` (completed) fixed the f64-by-allocation defect in
`tools/pyhecke/python/pyhecke/syt_prefix_cache.py::build_seminormal_matrices_cached`:

    M = np.zeros((dim, dim), dtype=_value_dtype(vals))   # dtype follows the values

**Its twin was not fixed.** `computations/hecke/hecke_characters.py::build_seminormal_matrices`
still carries the identical line, and two coercions that make it strictly worse:

    168:  q_local = float(q0) if q is None else float(q)     <-- destroys q AT THE INPUT
    215:  b = float(mp.sqrt(abs(b_sq)))                      <-- computes in mpmath, throws it away
    228:  M = np.zeros((dim, dim))                           <-- the exact line qou-d8gq fixed

Line 168 is the important difference. `qou-d8gq`'s twin lost precision at the
*allocation*, so a dtype-aware container fixed it. This one coerces the caller's
`q` on entry, so **a dtype-aware allocation alone would not help** -- by the time
values are computed there is nothing left to preserve.

MEASURED (mirroring qou-d8gq's own before-table), shape (3,2,1), dim=16:

    q as f64 : dtype=float64  entry type=float64
    q as mpf : dtype=float64  entry type=float64
    bit-identical output for f64 vs mpf q : True

So passing `q_parameter.Q_MP` to this builder buys nothing, silently.

## Blast radius

102 consumers under `computations/` (72 repo-wide excluding the generated
`qou-mass/_internal/` mirror and tools), of which **65 emit witnesses**. Every
one is float64-bound by construction regardless of the q it passes.

## NOT a drive-by fix -- the coercion is DELIBERATE

The comment at line 377 records why:

    "Normalize q_value to float ONCE here, and use q_f consistently in both the
     q= override AND the h_local computation below -- so callers passing mpmath /
     str / numeric types don't break NumPy dtype handling further down
     (per Copilot review on PR #1861)."

So this is a design decision to protect numpy dtype handling, not an oversight.
Changing it is a real infra change needing its own PR: `_value_dtype`-style
dispatch, an mpf-safe `b = mp.sqrt(...)`, a guard for the scipy sparse path
(scipy rejects `dtype object` -- the su4_1111 defect class), and a check that
all 65 witness-emitting consumers are bit-identical on the f64 path.

`qou-d8gq` already establishes the trade this reopens: honest mpf matmul measured
**642x** slower at dim=162. Correct-and-slow vs fast-and-forbidden is the owner's
call, and it is the same call there.

## Why it surfaced here

`computations/deltalambda/deuteron_interface_handle_curvature_probe.py` is one of
the five NEW raw-float64-dirty witnesses the ratchet flags on main (42 fields).
It calls THIS builder, so it is f64-bound at the source. The other four in that
batch were pure-python/complex and are fixed (ffb57ab2d, 808156bb4, ca3fd097c).

**This one must NOT be "fixed" by wrapping `_precision.fmt` around its outputs.**
That is the float64-padding defect by construction -- `fmt()` renders a 53-bit
value to the full serialization width so it READS as measured while carrying ~15
significant digits, which is the shape `_precision.py`'s own docstring warns
about and the float64-padding ratchet exists to catch. There is no honest quick
fix for this probe; it is blocked on this bean.

## Gate gap (inherited from qou-d8gq, still open)

`numpy_mpmath_dtype_leak_audit.py` is blocking and reports 0 candidates with this
leak live -- its scope is `d_for_ctype` consumers and `hoefsmit_numpy.py`, so it
does not see `np.zeros(...)` allocations that later receive mpf, and it does not
see an input-side `float(q)` coercion at all. A detector keyed on the ALLOCATION
would still miss line 168.
