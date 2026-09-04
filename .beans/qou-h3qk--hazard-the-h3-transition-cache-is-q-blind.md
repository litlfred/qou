---
# qou-h3qk
title: 'HAZARD: the H_3 transition cache is q-BLIND — a second q silently gets the first q''s amplitudes'
status: completed
type: bug
priority: high
created_at: 2026-09-04T06:40:00Z
updated_at: 2026-09-04T07:35:00Z
---

## The defect

`reduced_block_kernel.get_h3_transitions(ab0, ab1, ab2, q, qi, shape_in, c_in, Dc)`
caches on

    key = (ab0, ab1, ab2, shape_in, c_in)

**`q` is not in the key.** The body demonstrably uses it — `hq = q - qi`, and
`D(delta) = hq / (1 - q**(-2*delta))` — so two calls with the same `ab`/shape but
different `q` return the SAME amplitudes, computed at whichever `q` arrived first.

Demonstrated directly, not inferred:

    cache cleared, call at q = 1.11, then call at q = 1.9 (same ab/shape)
      call2 (warm) == call1 (q=1.11)      -> True
      call2 (warm) == q=1.9 on COLD cache -> False

So the second `q` received the first `q`'s numbers, silently. No raise, no warning.

## When it fires, and when it does not

The `ab` tuples are themselves computed from `q` (`_alpha_beta(ds, q, qi)`), so for
most pairs of `q` the key differs and the cache correctly misses. The bug fires only
where two different `q` yield the SAME `ab` tuples.

Measured: the ab key **changes at every step** of an eta sweep
(1e-7 -> 1e-9 -> 1e-10 -> 1e-11 -> 1e-13 -> 1e-15, all distinct), so a plain
q-sweep in one process is not silently frozen.

It is still a live hazard for any process that evaluates at two `q` values reachable
with equal `ab` — and the cache is module-level, so it persists for the life of the
interpreter across unrelated callers.

## This is NOT the cause of qou-v1cp

Stated explicitly because the two look alike and conflating them would send the next
agent down a closed path. `qou-v1cp` is the eta < 1e-10 flavour collapse in
`tr_m_atom_zn`. This cache does not explain it:

  * the `pp`/`nn` key collision is present at **every** eta INCLUDING 1e-3, where
    the results are correct and distinct (2.38617 vs 2.26361) — so key collision
    alone does not produce the discontinuity;
  * the key changes at every eta step, so a warm cache does not freeze the answer
    below the threshold.

Both were tested for and both came back negative. The cache defect is real on its
own evidence; the v1cp cause remains open.

## Fix

Put `q` in the key. Because `q` is an `mpf` whose precision can vary, key on its
exact decimal string at a fixed precision (`mp.nstr(q, 50)`) rather than the object,
and consider keying on `mp.mp.dps` too — a block computed at 50 dps and reused at 90
is the same class of silent staleness one level down.

Add a regression test that is the demonstration above: same ab/shape, two `q`, assert
the warm result differs from the first and equals the cold-cache result.


## FIXED 2026-09-04

The key is now `((mp.nstr(q, 50), mp.mp.dps), ab0, ab1, ab2, shape_in, c_in)`
via a new `_q_key(q)` helper.

`q` is keyed by its exact 50-digit decimal rather than by the mpf object: an
mpf carries the precision it was CREATED at, so two mpf equal in value can be
distinct objects, and `mp.nstr` gives a stable hashable identity. `mp.mp.dps`
joins it for the reason the "Fix" section above anticipated -- a block computed
at 50 dps and reused at 90 is the same silent staleness one level down, and it
was measurably happening: pre-fix, a 90-dps call on the same `q` was served the
50-dps block byte-identically.

### Verification

Guard: `computations/audits/h3_transition_cache_q_key_audit.py`. It does not
wait for a natural collision -- it FORCES one, calling `get_h3_transitions`
twice with identical `(ab, shape, c)` and different `q`, which is precisely the
state the old key could not distinguish.

  * Run against the PRE-FIX key it exits 1 with three findings: `q_B` received
    `q_A`'s amplitudes, warm `q_B` differs from cold `q_B`, and the 90-dps call
    was served the 50-dps block. Post-fix it passes.
  * Production unmoved: D / T / 3He / 4He atom and free traces byte-identical
    (expected -- production uses one `q` per process, so the old key was never
    wrong there; that is why this was survivable and not why it was safe).
  * Cost measured, not assumed: 6Li cold 1.359 s after vs 1.484 s before, warm
    0.461 s vs 0.482 s. The `mp.nstr` in the hot loop is inside run-to-run
    variation, so the key is NOT hoisted out of `get_h3_transitions` -- keeping
    it at the point of use is what makes it impossible to bypass.

### Standing negative, unchanged

This is still NOT the cause of `qou-v1cp` (see the section above). That was an
absolute `_TOL` in `chi_monotone_transfer.word_to_mpfr` applied to templates
that all scale with `h = q - 1/q`; fixed separately in the same PR. The two
were tested for a causal link twice -- by key-collision analysis and then by
the decisive cold-cache experiment -- and cleared both times.
