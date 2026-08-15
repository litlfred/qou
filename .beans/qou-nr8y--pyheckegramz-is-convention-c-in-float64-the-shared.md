---
# qou-nr8y
title: pyhecke.gram.z is convention C in float64 — the shared root under the remaining 25
status: todo
type: task
created_at: 2026-08-15T23:05:27Z
updated_at: 2026-08-15T23:05:27Z
---


## The finding

`tools/pyhecke/python/pyhecke/gram.py:121`

    z = 1.0 / (q0 ** 0.5 + qi ** 0.5)

That is convention C — `z = 1/(√q + 1/√q)` — hardcoded in the **published
`pyhecke` package**, and in float64 (`1.0`, `** 0.5`), not mpmath.

`computations/substrate/hecke_core.py:61` re-exports it (`from pyhecke.gram
import z, …`), and 7 in-repo producers import it from there. Verified at
runtime:

    hecke_core.z = 0.4993203341836945     <- C
    D would be   = 0.6126880371464652

So the two halves of the same package family disagree on the same constant:
`pyhecke_native.markov_z(q₀)` returns the **D** value 0.6126880371464652,
while `pyhecke.gram.z` is **C**. Same repo, same package name, one Rust and
one Python, opposite conventions.

## Why this is the answer to the remaining work list

The convention-C surface is now 25 witnesses, **all roots, zero derived** —
siblings drained the derived layer, which confirmed the `qou-lt8x` sequencing.
"All roots" was read as "25 separate producers each carrying C in their own
code". At least a large share of them do not: they import one shared constant
that is C. `entanglement-orders.witness.json` records `"z":
0.4993203341836945` as its own top-level field for exactly this reason.

This is the fourth instance in this arc of one defect shape — two
implementations of one quantity, drifting apart:

    three inline {sigma, sigma_inv, averaged} d-maps   -> d_for_ctype
    two WITNESS_REF regexes (.witness vs -witness)     -> one pattern
    two structural detectors ("3_2_1" parsing)         -> delegate to audit
    pyhecke.gram.z (C) vs pyhecke_native.markov_z (D)  -> THIS

## Why I did not just change it

`tools/pyhecke/` is a published PyPI package with 19 in-repo direct importers
(AGENTS.md §Project structure). Flipping a shared constant there changes every
consumer at once, and I cannot verify that blast radius in the context I have
left. The one-line edit is the easy part; knowing which consumers *depend* on
the C value being C — e.g. a convention-sensitivity probe such as
`qbeta-c3-ladder-trace-convention-sensitivity` — is the part that needs doing
first.

## To close

1. Enumerate consumers of `pyhecke.gram.z` and split them: those that want the
   canonical `z` (fix by the change) from those deliberately comparing C to D
   (must pin C explicitly, not inherit it).
2. Change `gram.py:121` to `z = q0**3 / (q0**2 + 1)` and carry it as mpmath
   from source, not float64 — the float64 form also trips the NO-FLOAT64
   family (`qou-j6gb` territory).
3. Re-run the 7 `hecke_core` importers, re-test each witness individually.
   Never batch: a sweep reports green without migrating anything, which is
   the `qou-eea0` failure this arc already paid for once.
4. Consider making `pyhecke.gram.z` delegate to the Rust `markov_z` so the two
   halves cannot drift again — the `d_for_ctype` remedy applied here.

## CORRECTION: it explains 2 of 25, not "a large share"

I wrote above that "a large share" of the 25 roots inherit this constant. That
was asserted from two examples, not measured. Measured — resolving each
flagged witness to its producer and parsing that producer's import list for
`z` from `pyhecke.gram` or `hecke_core`:

    flagged witnesses whose producer imports the shared z:  2 / 25

        entanglement-orders.witness.json          <- entanglement_orders.py
        h2o-bond-angle-magnitude-vsepr.witness.json <- h2o_bond_angle_magnitude_vsepr.py

So the shared constant is **not** the common root of the remaining surface.
The other 23 carry convention C by some other route, still unidentified, and
"25 roots = 25 separate source edits" remains the working assumption rather
than the thing I claimed to have overturned.

What survives unchanged, because it was measured rather than inferred:

* `pyhecke.gram.z = 1.0/(q0**0.5 + qi**0.5)` is convention C, in float64, in
  the published package. Runtime: `hecke_core.z = 0.4993203341836945` against
  `pyhecke_native.markov_z = 0.6126880371464652`.
* The Rust and Python halves of one package family hold opposite conventions.
* It is a real defect worth fixing on its own terms, and it is the fourth
  instance of the two-implementations-drifting shape.

What does not survive: the claim that fixing it clears most of the work list.
It clears two.

The failure mode is the one this arc keeps repeating and that I keep having to
correct in my own work — generalising a mechanism from the first two cases
that fit it, before counting how many actually do. Same shape as "16 of 31
missing" (real answer 4) and "the roots carry C in their own code" (the first
root I opened was already D).
