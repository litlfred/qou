---
# qou-9ay6
title: 'hecke_core_legacy.binding_energy is unrunnable: unified_iterative_correction >120s at A=2, and binding_from_frobenius_pairing dies in scipy.sparse'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T20:31:59Z
updated_at: 2026-08-31T02:51:48Z
---


Split out of `qou-c7g8` 2026-08-30. Two defects in
`computations/hecke_core_legacy.py::binding_energy`, both reached only at A≥2
(it opens `if A <= 1: return 0.0`).

## (a) `unified_iterative_correction` — >120 s on the SMALLEST A=2 input

    unified_iterative_correction(1, 1)     >120s     <- bottleneck
    sdp_cross_channel_contribution(1, 1)   0.01s
    binding_from_frobenius_pairing(1, 1)   TypeError -- see (b)

Z=1, N=1 is deuterium, the smallest case that reaches this code at all. Callers
iterate far past it — `hadron_knot_table.ATOMS` runs to **ca40 (A=40)**. So any
producer that calls `binding_energy` over a nuclide table is not slow, it is
**unrunnable**, and raising a timeout does not reach it.

Known blast radius so far: `hadron_knot_table` (cannot finish; therefore also
the corpus's single Q0_FLIP, since it cannot be re-run to repin), and
`q0_migration_decompose`, which appears to "time out" only because it runs
`hadron_knot_table` twice under a 900 s child cap. Other callers of
`binding_energy` are not yet enumerated — do that before estimating scope.

## (b) `binding_from_frobenius_pairing` cannot run at all

    scipy/sparse/_sputils.py  upcast(*map(np.dtype, args))
    TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))

An object dtype — almost certainly mpmath `mpf` — reaches a `scipy.sparse`
operation, and sparse supports no object dtype.

**This is currently invisible**: (a) times out first, so nothing ever gets here.
It will surface the moment (a) is fixed. Do not treat fixing (a) as finishing
the job.

Two candidate causes, neither tested:
- this container runs **scipy 1.17.1 / numpy 2.4.6**, newer than whatever built
  the June witness; an older scipy may have tolerated the upcast;
- or it is a genuine leak of `mpf` values into a matrix that must be numeric.

Distinguish before fixing: if it is the leak, casting to float64 to silence it
would silently drop 50-dps precision, which the NO-FLOAT64 directive forbids.
Find where the object dtype enters, do not coerce at the boundary.

## How this was localized

Bisected `compute_atom("deuterium", 1, 1)` call by call. `build_atom_nf`,
`nf_tr`, `nf_net`, `check_frobenius`, `classify_nuclear_knot` and
`ground_state_ordering` are **all 0.00 s**; only `binding_energy` is slow.

⚠️ Note for whoever picks this up: `binding_energy` and
`compute_per_generator_volumes` BOTH short-circuit below A=2, so the first A=2
atom is the first time either runs. That made `ground_state_ordering` look
guilty on the evidence of the per-atom output alone. It is innocent — measure,
do not infer, which of the two is slow.

## 2026-08-31 — (b) FIXED at the root. And my first fix was wrong.

### The defect was a MISSING BRANCH, in 2 of 3 places

`_step_chain_generic` yields mpmath `mpf` coefficients (`d = -h`, i.e. ℏ_q —
correctly so), so `c * Msig + d * M_run` promotes the float64 accumulator to an
OBJECT array, and the next float64 `csr_matrix.dot` rejects it. Confirmed by
reading the failing frame's locals rather than inferring:

    sig_sparse : csr_matrix   dtype=float64  shape=(35,35)
    M_run      : ndarray      dtype=object   shape=(35,35)

`unified_iterative_correction` **already handled this**, with a comment naming
the exact TypeError and even naming the consequence — *"which is why this
producer had been dead: its witness is from 2026-06-17"*, i.e. hadron_knot_table.
But the identical loop appears at **three** sites, and only that one had the
object branch:

    unified_iterative_correction    had the branch
    atom_character_raw              BARE .dot   <- died here
    _contrib_single_partition       BARE .dot

So the defect is the divergence between three copies of one loop, not a bug in
any single one of them.

### 🛑 My first attempt was wrong and is reverted

I patched all three to `float(c) * Msig + float(d) * M_run`, reasoning that
`sig_sparse` is float64 so precision is capped anyway. The existing code refutes
that, in writing, at the site I was about to overwrite:

    > Densify and multiply with object arithmetic rather than coercing c/d to
    > float — that would silently discard the precision the mpf exists to carry
    > (AGENTS.md: never compute in float).

That is exactly the coercion this bean's own "Fix" section warned against
("casting to float64 to silence it would silently drop 50-dps precision... Find
where the object dtype enters, do not coerce at the boundary"). Reverted before
committing.

### What landed instead

Extracted the working logic into `_msig_object_safe(sig_sparse, M_run, gen,
coo_cache)` and wired all three sites to it. Extracted rather than copied a
third time — the divergence IS the defect. Complexity preserved per the
original's own note: accumulating over σ's nonzeros is O(dim·nnz), the same
order the float64 branch gets from sparse BLAS, whereas densifying σ is O(dim³)
in object arithmetic and does not finish.

    3 call sites via the helper, 0 bare `.dot` remaining
    pytest tools/qou-substrate/tests/ tests/  ->  145 passed

`binding_from_frobenius_pairing(1,1)` no longer raises: it previously failed in
well under a second with the TypeError, and now proceeds into real computation.

### (a) still open — and now clearly separate

The dtype crash and the >120 s cost are independent. `unified_iterative_correction`
never crashed; it was always slow, and it is slow *because* object arithmetic
replaces vectorised BLAS — which the corpus accepts deliberately, to keep the
mpf precision. So (a) is not a bug to fix but a design cost to engineer around:
making it fast means finding a formulation that keeps precision without
per-element Python arithmetic, not switching to float64.

## 2026-08-31 — (b) CONFIRMED FIXED by measurement

    binding_from_frobenius_pairing(1,1):
      before   TypeError in well under a second
      after    >600s with NO TypeError — it now computes

The dtype crash is gone. The function is slow for reason (a), which is a
different problem in a different function.

## (a) remains open — and it is a DESIGN COST, not a bug

`unified_iterative_correction` is slow *because* it does object arithmetic to
keep mpf precision, which the corpus chose deliberately and documented in
place:

    > Densify and multiply with object arithmetic rather than coercing c/d to
    > float — that would silently discard the precision the mpf exists to carry
    > (AGENTS.md: never compute in float).

So there is nothing here to "fix" in the sense of correcting a mistake. The
existing code already avoids the two obvious wrong answers: coercing to float64
(loses 50-dps precision, violates NO-FLOAT64) and densifying σ (O(dim³) in
object arithmetic, measured >10 min on the A=2 atom alone). It already reduced
the inner product to O(dim·nnz), the same order sparse BLAS achieves.

Making it fast therefore means a different formulation, not a patch. Options
worth someone's time, none attempted here:

- carry the mpf part as a SCALAR alongside a float64 matrix where the chain
  allows it, so BLAS does the matrix work and mpf only tracks scale;
- move the accumulation into the Rust `hecke-engine` with a high-precision
  scalar type, alongside the existing float64 path;
- exploit that `c` is `int` at every crossing measured and only `d` is mpf —
  the update `M_run = c·Msig + d·M_run` may factor.

**Do not "fix" this by lowering precision.** That is the one direction the
corpus has already ruled out in writing, and a fourth agent rediscovering the
float coercion is the likely failure mode here — I was the third.
