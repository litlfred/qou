---
# qou-sxyr
title: 'Beans citing a Lean declaration go stale silently: 6 of 10 in sp00 were open while proved'
status: in-progress
type: task
created_at: 2026-09-06T10:27:08Z
updated_at: 2026-09-06T10:27:08Z
---


Found while planning attacks on `sp08` (Okounkov–Vershik) and the Specht standard
basis. Both were already proved. So were four of their siblings.

## The measurement

`sp00` is a ten-brick epic, phase-ordered, each brick naming one Lean declaration.
Re-measured 2026-09-06 with `#print axioms` against freshly-rebuilt oleans:
**all ten are proved and axiom-clean**, and **six were recorded `todo`** —
`sp02`, `sp04`, `sp05`, `sp07`, `sp08`, `sp10`. The epic itself was
`in-progress` while complete.

Four bricks (`sp01`, `sp03`, `sp06`, `sp09`) *were* updated by hand when they
closed. That asymmetry is the diagnosis: the process is manual, so it works
exactly as often as someone remembers.

## Why this is worth a mechanism and not just a sweep

The cost is not tidiness. It is:

1. **Wasted starts.** Two "famous, absent from Mathlib, HARD" bricks were the
   obvious next research targets in this repo. Any agent picking them up spends
   its opening hours re-deriving something already in the tree.
2. **Wrong priors about the corpus.** `sp10` read "Mathlib has no RSK. Famous."
   — true, and beside the point, because the corpus built RSK **in-repo** across
   ~48 `Schensted*` modules. A reader trusting the bean concludes the identity is
   unavailable when it is unconditional and clean.
3. **It is exactly the defect class this session kept finding**, one layer up:
   `wedderburnEmbed_posSemidef` advertised but absent; `wenzlBridge` advertised at
   the wrong strength; a `sorryAx` registry entry a month out of date; an axiom
   gate blind for a month. Every one was a *record* that outlived the *fact*, and
   every one was found by measuring rather than reading.

## Proposed mechanism (not built here)

A bean whose body names a fully-qualified Lean declaration is machine-checkable
against that declaration's real status. Sketch:

- extract `QOU.…` identifiers from non-completed beans;
- resolve each against the environment (as `lean-axiom-guard.py` already does);
- report beans that are open while their declaration exists and is `sorryAx`-free.

Three properties it must have, each learned the hard way in this session:

- **Verify by artifact, not by parsing prose.** A grep for "sorry-free" in a
  docstring is the failure mode, not the check.
- **"Could not resolve" is a third state**, never rendered as "still open" and
  never as "done". A declaration that does not exist is a *renamed or deleted*
  one, which is its own finding.
- **A class binder means the check is not finished.** `sp07` and `sp10` are clean
  *and* carry `[SnIsotypicSpechtSplit]`; whether that is established depends on
  an instance existing. Any such tool must report the binder rather than call
  clean "done" — this exact distinction went the wrong way twice in one session
  before being caught.

## Scope note

Not built here deliberately. The measurement above is a one-off audit of one
epic; whether the mechanism earns its keep depends on how many other beans cite
declarations, which is itself unmeasured. Someone should count that first.

## Counted, then built (2026-09-06)

The scope note above said someone should count first. Counted: **248
non-completed beans cite 456 distinct `QOU.*` dotted identifiers.** That
justified the tool, so `scripts/bean-declaration-audit.py` exists.

Of the 456, **118 resolve now** (their owning module has an olean); 97 own a
module that is not built, and 79 match no module prefix. Probing those 118:

| verdict | n | meaning |
|---|---|---|
| CLEAN | **14** | proved theorem, no instance binder — citing bean is a **candidate stale** |
| REVIEW | 21 | proved, but the type carries an instance binder — clean does not settle it (see `sp07`) |
| SORRY | **0** | genuinely open |
| ABSENT | 44 | does not resolve — renamed, deleted, or namespace ≠ module |
| DEF | 39 | a **definition**, not a theorem |

**13 candidate-stale beans.** Raw output kept at
`docs/audits/2026-09-06-bean-declaration-audit.txt`.

## The correction that mattered most was to my own tool

The first version reported **42 CLEAN and 29 candidate-stale beans**. It counted
any resolvable constant as "proved". Spot-checking one — `qou-6dzi` cites
`Wedderburn.WedderburnDecomposition`, an `abbrev` for a type — showed the flaw:
a definition *exists*; that says nothing about whether the bean's work is done.
Restricting to `thmInfo` dropped CLEAN 42 → 14 and the bean count 29 → 13.

**The first version would have overstated the finding threefold**, in a tool
whose entire purpose is to catch records that overstate. Recorded because the
temptation is structural: a checker that resolves names will happily resolve
names that were never claims.

Two smaller ones, same session: a string test on the pretty-printed type for
instance binders (does not parse, and the printed form is not a reliable carrier
— replaced by walking `binderInfo`), and a summary line calling the no-module
bucket "renamed, deleted, or never existed" when it mostly holds the ordinary
case of a namespace differing from its module.

## Deliberately not done: bulk-closing the 13

The tool prints "candidate, not verdict" and means it. A bean can legitimately
stay open for wiring, a consumer, or documentation after its core theorem lands —
`sp00`'s own children did exactly that. Closing 13 beans on a script's say-so
would be the same failure this bean exists to name, pointed the other way.

## One incidental finding

`QOU.Archimedean.R_q` is declared by **both** `Archimedean.GroundRing` and
`Archimedean.WeierstrassProjection`, so those two modules can never be
co-imported — a single probe importing every owning module fails outright. That
is why the tool emits one probe per module. Not chased further here.
