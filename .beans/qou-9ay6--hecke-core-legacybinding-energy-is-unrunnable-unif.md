---
# qou-9ay6
title: 'hecke_core_legacy.binding_energy is unrunnable: unified_iterative_correction >120s at A=2, and binding_from_frobenius_pairing dies in scipy.sparse'
status: todo
type: task
created_at: 2026-08-30T20:31:59Z
updated_at: 2026-08-30T20:31:59Z
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
