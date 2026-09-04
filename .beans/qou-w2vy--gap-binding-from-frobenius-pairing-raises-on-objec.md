---
# qou-w2vy
title: 'GAP: binding_from_frobenius_pairing raises on object dtype -- latent behind term 1''s hang'
status: todo
type: task
priority: high
created_at: 2026-08-31T04:44:27Z
updated_at: 2026-08-31T05:11:06Z
---

Blocks qou-i7ju together with qou-4m9u. Evidence:
docs/audits/2026-08-31-binding-energy-cannot-run.md.

## The gap

`binding_from_frobenius_pairing(1,1)` raises on main in 0.52s:

    TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))

This is the SAME failure class the COO accumulator already fixed in
unified_iterative_correction -- scipy sparse refusing object dtype the moment an
mpf enters -- and it is UNFIXED here.

## Why nobody noticed

binding_energy applies term 1 (unified_iterative_correction) FIRST, and that
never returns for A>=2. Control never reaches term 3. The crash is latent behind
the hang.

Demonstrated: stub term 1 only, leave terms 2 and 3 as main has them ->

    binding_energy(1,1) deuterium RAISES TypeError
    binding_energy(1,2) tritium   RAISES TypeError
    binding_energy(2,2) he4       RAISES TypeError
    binding_energy(3,4) li7       RAISES TypeError

4 of 4. So binding_energy for A>=2 has TWO independent blockers, and fixing only
the performance one converts a hang into a crash.

## Corroboration

computations/hadron-knot-table.witness.json:
    computedAt      2026-06-17T04:13:13
    scriptCommitSha 08ec1c0d0999b6b6d8c902a4ec8fa5344a383a2d

2.5 months old. Its binding values predate whatever broke term 3, and nothing
since has been able to reproduce them.

## Term 2 for contrast

sdp_cross_channel_contribution(1,1) = 0.0 with BOTH the current and the
corrected matrices (27.9s / 67.1s). Unaffected, and zero, AT A=2 ONLY --
sdp_cross_channel.py consumes _build_ysn_matrices directly, so larger A is
untested and must not be assumed either way.

## Not established

The corrected-family run of term 3 had not completed at 10 min and is NOT
reported. Whether the crash is independent of which matrices are used is
untested -- though a dtype-conversion error suggests it is.


## FIXED 2026-08-31 -- and the fix exposes a THIRD blocker

atom_character_raw carried the unguarded branch; TWO identical occurrences
existed, both now fixed with the same COO object accumulation term 1 got in
da645cf0f32 (O(dim*nnz), COO cached per generator, no coercion of c/d to float).

**Term 3 no longer raises. It now does not terminate.** Deuterium ran >12 min
without completing, where before it raised in 0.52s. py-spy: 3/3 samples inside
the new COO accumulation (lines 1716, 1719) in mpmath __add__/__mul__.

So term 3 has the IDENTICAL performance wall as term 1 -- Python-level mpmath
over partitions up to dim 2310 -- and it was hidden behind the crash exactly as
the crash was hidden behind term 1's hang. Two layers of masking.

BLOCKERS NOW THREE:
  1. seminormal family is not a representation (qou-4m9u, settled; term 1 moves 71-221%)
  2. term 3 object-dtype crash -- FIXED
  3. Python-mpmath performance wall in BOTH term 1 and term 3 -- term 1 partly
     (5.8x guard fix), term 3 untouched

NEXT: lp_accumulator_step_traces_mpfr (built, merged in #6337) was written for
term 1's loop. Term 3's loop has the same shape -- identity start, per-crossing
M <- c(M.sigma) + dM, rescale, trace -- so the same kernel SHOULD serve both.
That is asserted FROM THE SHAPE, not measured. Wiring it into both is the next
concrete step, and it needs a value-equality gate the way the guard fix did.

## CORRECTION 2026-09-04 -- term 3 DOES terminate; the ">12 min" was a timeout

The section above states, flatly: **"It now does not terminate."** That is a
claim about termination drawn from a 12-minute observation, and it is wrong.

MEASURED, deuterium (Z=1, N=1), both halves that
`binding_from_frobenius_pairing` composes, on `main`:

    atom (include_inter=True )   503.6 s   type=mpf   0.89486186364004106
    free (include_inter=False)   454.9 s   type=mpf   3.2936269985705353
    ------------------------------------------------------------------
    total                        958.5 s = 15.97 min

`E_0*(|free| - |atom|) = 1.8766341061441356`, reproducing an earlier untraced
run of the whole function that returned `1.87663410614414` in 871.1 s. Two
independent runs, ~10 % apart in wall time, same value to every printed digit.

**So the bean stopped watching at 12 minutes on a 16-minute computation.** This
is the mirror of the trap AGENTS.md already records for `hadron_knot_table`
("a timeout is not proof of success") -- here a timeout was read as proof of
NON-termination. Neither direction is available from a timeout.

What survives unchanged: the **cost**. ~16 min for the FIRST bound atom is the
performance wall blocker 3 describes, and the `lp_accumulator_step_traces_mpfr`
wiring is still the right next step. Only the word "terminate" was wrong.

Reproduce (~16 min; do not re-run casually):

    python3 -u - <<'PY'
    import sys, time; sys.path.insert(0, "computations")
    import hecke_core_legacy as H
    for inter in (True, False):
        t0 = time.time(); v = H.atom_markov_trace(1, 1, None, include_inter=inter)
        print(f"{inter}: {time.time()-t0:.1f}s {type(v).__name__} {v!r}", flush=True)
    PY


## AND THE 16 MINUTES IS SPENT IN FLOAT64 ARITHMETIC (2026-09-04)

The run above printed, before doing any work, `mp.dps = 15`.

That is mpmath's **default**, and `mp.dps = 15` is `mp.prec = 53` -- exactly
float64's significand. Verified rather than assumed: at the default precision
2000/2000 random `mpf` values satisfy `mpf(x) == mpf(float(mpf(x)))`, i.e. every
mpf IS a float64. At `dps = 50` the same test fails, as it must.

**So an `mpf` return type is not evidence of precision**, and the COO mpmath
accumulation that blocker 3 measures is doing float64 arithmetic slowly.

Where the precision is not established, measured on `main`:

  * `hecke_core_legacy.py` -- **0** occurrences of `mp.dps`, `workdps`,
    `workprec`, or any `_precision` import, module-wide.
  * `atom_character_raw` (lines 1715-1818, 104 lines) -- **0** `workdps`,
    **0** `workprec`, **0** `mp.dps`, **0** `mpf(`, and **6** `float(`.
    It ends `chi = _trace_dim(M, dim)` / `return (float(chi), float(log_norm),
    int(dim))`, and `log_norm` accumulates through `math.log(m_max)`.
  * `computations/phase5/phase3_triton_binding_convention_b.py` -- the ONE
    external caller of `binding_from_frobenius_pairing` -- imports
    `mpmath as mp` at line 78 and **never sets `mp.dps`**.

The right pattern exists three files away and is not on this path:
`tools/pyhecke/python/pyhecke/atom.py:508` opens
`with _mpm.workdps(max(_mpm.mp.dps, 60)):` -- a FLOOR, so an ambient 15 becomes
60. `atom_character_raw` has no such floor.

**Scope, stated precisely:**

  * NOT a regression. This is legacy code and predates the COO fix; the fix
    changed the dtype handling, not the precision.
  * NOT the cause of anything measured here -- the termination result and the
    wall-clock stand on their own.
  * NOT covered by the existing gates. `precision-gates.sh` catches
    `mpf(<float>)` and an `mp.dps` no-op; **"nobody ever set dps" is a different
    hole**, and neither gate fires on it. A file with zero `mp.dps` occurrences
    is indistinguishable, to those gates, from a correct one.
  * "It is the EXPLORATORY path" is NOT an exemption -- the producer's own
    comment at line 84 says exploratory, and AGENTS.md is explicit that PROBES
    ARE NOT EXEMPT.

**NOT MEASURED, and it decides how much this matters:** what precision the
*inputs* carry. If the Hecke matrices reaching `atom_character_raw` are
themselves float64, raising `dps` buys nothing -- "a float64 input poisons the
whole result." I did not trace the input cone, so this is a ceiling I have
demonstrated, not a loss I have quantified. Establishing that is the next step,
and it is cheaper than the 16-minute run: instrument `_crossing_in_partition`
and `sigmas` for their element types.

**Related, same shape, one function over:** the `float(_tr)` narrowing at the
`_lp_kernel_steps` consumer already recorded on this bean. Two independent
float64 boundaries on the same term-3 path.
