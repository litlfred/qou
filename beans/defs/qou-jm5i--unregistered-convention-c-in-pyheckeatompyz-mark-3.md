---
# qou-jm5i
title: UNREGISTERED convention C in pyhecke/atom.py::z_mark — 31 callers never got the D ruling
status: completed
type: bug
priority: normal
created_at: 2026-08-16T11:25:44Z
updated_at: 2026-08-16T11:26:12Z
---

## The find

`tools/pyhecke/python/pyhecke/atom.py::atom_per_generator_volumes` computed

    z_mark = 1.0 / (q0 ** 0.5 + qi ** 0.5)        # = 0.4993203  -> convention C

**and the same function already imported `z` from `pyhecke.gram` at line 37**,
where `z = q0**3 / (q0**2 + 1)` = 0.6126880 — convention **D**, migrated
2026-08-15. The local recomputation shadowed the import.

So every caller of `atom_per_generator_volumes` — **31 files**, including
`canonical_tower.py`, `substrate/hecke_core.py`, `pn_alpha_lp_dual.py`,
`mass_table_comprehensive.py` and the brane-tower probes — was still running
convention C, eight days after `33a6c7aa4` ("the trace is now D everywhere").

## Why the migration missed it

`docs/coordination/trace-convention-registry.json` lists exactly three C
implementations:

    computations/schur_principal_mpmath.py::_wenzl_constants_convention_C_HISTORICAL
    computations/schur_principal_mpmath.py::y_lambda_at_q0_mpmath_convention_C_HISTORICAL
    tools/pyhecke/python/pyhecke/gram.py::z   (BLOCKED, qou-wgta item 11)

`atom.py::z_mark` is not among them. It was never registered, so no sweep, no
blast-radius queue and no audit ever visited it. This is the same shape as
qou-lt8x one level further out: that bean found 31 *witnesses* that are C on
their own; this is a C *source* site upstream of some of them.

Also worth noting for the registry: it still records `gram.py::z` as BLOCKED
and staying at C, but `gram.py` line 175 has been D since 2026-08-15. The
registry is stale on its own blocked entry.

## Fix

Deleted the local recomputation; the function now uses the imported `z`, and
also the imported `W_SYM/W_STD/W_ALT` instead of recomputing those.

The **weights were not divergent** — the local recomputation reproduced gram's
to the last f64 digit — so this is not a second numerical bug. But recomputing
a constant that is imported three lines above is exactly how the `z` fork
happened, so both now come from the single source.

## Measured effect: it IMPROVES the fit

q-CLT binding channel, mean |err| over {D, T, 3He, 4He, 7Li, 16O}:

           D        T      3He      4He      7Li      16O    mean|err|
    C  +161.59   +57.67   +25.77   -39.00    -7.61   -32.68     54.05%
    D   +97.86   +21.00    -4.74   -53.30   -28.93   -48.21     42.34%

Same signature as the symbolic channel under the ruling: light atoms improve
sharply, heavy atoms degrade, aggregate improves. Note this is the OPPOSITE
direction from the ruling's own binding-table note (37.39% -> 43.85%) because
that measured the symbolic channel, which had already moved; this one had not.

## Blast radius — NOT regenerated here

31 callers change value. Their committed witnesses are now stale in the same
way `mass-table-comprehensive` was, and they belong on the same queue
(qou-lt8x / qou-c6xo), not in this commit. Naming them is the next step.

## Bonus find, not fixed: the mpf braid word is laundered here anyway

`atom.q0`, `atom.qi`, `atom.h` are all **Python floats** (q0 =
1.1099785827513808 — and that is the *proton-pin* anchor, not the canonical
one). `efcaf79ed` made the braid-word coefficients mpf, but they are multiplied
against a float64 q0 one line later, so the result is an mpf carrying f64
information. That is laundering, in the file the NO-FLOAT64 campaign touched —
and it is why that commit cost 11.5x (qou-53p1) for precision it does not
deliver. Fixing it is an owner call because it changes 31 callers again.
