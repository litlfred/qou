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
