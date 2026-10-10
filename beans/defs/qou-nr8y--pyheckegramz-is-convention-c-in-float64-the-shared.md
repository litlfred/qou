---
# qou-nr8y
title: pyhecke.gram.z is convention C in float64 — the shared root under the remaining 25
status: completed
type: task
priority: normal
created_at: 2026-08-15T23:05:27Z
updated_at: 2026-08-15T23:23:08Z
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

## RETRACTED as a defect: the C here is load-bearing, and D is SINGULAR

Asked to excise convention C, I went to change `gram.py:121` and read the
comment block directly above it first. It rules the change out:

> under D there is exactly ONE null direction, the row-cap one, under BOTH
> pairings. So **det G = 0 and G_INV does not exist**. C stays invertible
> either way, because `y_(1^3) = 0.0227 != 0`.
>
> And numpy does not protect you: `np.linalg.inv` on the D matrix **RAISES
> NOTHING**. It returns entries up to 7.6e15 with `||G @ G_INV - I|| = 1.64`.

`pyhecke.gram` computes `G_INV`. Under convention D the Wedderburn Gram matrix
is **singular** — that is the *same* fact as `y_λ = 0` on 3+-row blocks, seen
from the determinant side, and it is already Lean-proved:
`MarkovGramDegenerate.wedderburnGram_det_eq_zero_of_dead`.

So the C in this module is not stale, and not a drift against the Rust half.
It is the convention under which the object this module exists to build
actually exists. Flipping `z` to D would leave every call site running on a
fabricated inverse, with no exception raised — exactly the failure the file
documents in advance.

**Excision is therefore blocked here, on a proved invariant rather than on
caution.** This is a scope-(b) structural exclusion in the AGENTS.md sense:
the ingredient cannot be removed because a proved degeneracy forbids the
replacement, not because the numbers came out wrong.

### What this means for the two witnesses

`entanglement-orders` and `h2o-bond-angle-magnitude-vsepr` inherit C from a
module that must be C. Migrating them is not "flip the shared constant" — it
is either (a) they should not be using the Gram-inverse path at all, or (b)
they need a D-convention trace that does not route through `G_INV`. Which one
is a per-witness question, and neither is a one-line edit.

### Correction history on this bean, in order

1. "the shared root under the remaining 25"        -> it explains 2 of 25
2. "a real defect worth fixing on its own terms"   -> it is load-bearing; D is
                                                      singular here
Both corrections came from measuring or reading rather than from inference,
and both retracted something I had already published. The finding that
survives is narrow and still worth having: `hecke_core.z` is C while
`pyhecke_native.markov_z` is D, the two are used side by side, and *nothing
in either module says which one a caller should expect*. That is a real
hazard even though neither value is wrong.

## CLOSED — redundant. The registry already owns this.

Ran the corpus-grep checklist (AGENTS.md §Before declaring "open") *after*
opening this bean rather than before, which is the wrong order and is why this
exists at all. `docs/coordination/trace-convention-registry.md` — the
authoritative ledger — already carries every part of it:

* **Convention C is `EXCISED` as of 2026-08-09** (bean `qou-wgta`); D is
  `PRODUCTION`. The excision is done, not pending.
* `pyhecke/gram.py::z` is a **registered `blocked_migrations` entry** in the
  JSON twin, with the exact mechanism I "found": *"switching it silently
  destroys `G_INV`, because the Markov–Gram form is degenerate under D."*
* C survives in exactly **three** deliberate places: two historical functions
  in `schur_principal_mpmath` kept so the excised convention stays quotable for
  the D-vs-C comparison, plus this blocked migration.
* The registry even anticipates the failure mode: *"R9 asserts all three are
  still C; the preserved reference stopping being C without anyone noticing is
  precisely what happened to its predecessor."*

So the finding was correct, the blocker was correct, and both were already
recorded, machine-checked and validator-enforced. Nothing here is new.

### What was actually mine, and it is small

`hecke_core.py:61` re-exports the blocked-migration `z` under a name that says
nothing about its convention, and `entanglement_orders.py` imports it as
`Z_MARKOV` — a name that reads as *the* Markov z. The registry governs
`pyhecke/gram.py::z`; it does not say the re-export is safe to read as
canonical. That is a naming hazard on top of a governed constant, not a
convention defect, and it is worth at most a comment at the re-export site.

### Corrected disposition of the 25 flagged witnesses

Not "convention C awaiting excision". The excision happened 2026-08-09 and
their producers are D. They are **stale outputs predating it**. That makes the
sweep result from earlier in this arc — 11/41 producers re-run, not one witness
moved C→D — the live contradiction worth pulling, because the registry says
those producers are already D.

### Process note

Three corrections on one bean: scope (25 → 2), status (defect → load-bearing),
and now existence (novel → already registered). All three were avoidable by
reading `docs/coordination/` first. The checklist exists precisely because a
plausible mechanism found in code reads as a discovery when it is a
rediscovery.
