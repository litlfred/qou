---
# qou-sxyr
title: 'Beans citing a Lean declaration go stale silently: 6 of 10 in sp00 were open while proved'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T10:27:08Z
updated_at: 2026-10-04T15:11:59Z
parent: qou-5vkl
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

## The ABSENT bucket, split — and four more corrections to my own tool

The previous pass left 44 identifiers unresolved and I called them "beans citing
declarations that no longer exist — a worse record than a stale one". That framing
was too strong. Split properly:

| | n | |
|---|---|---|
| relocated | 27 | namespace ≠ my module guess — a **resolver** limitation, not a corpus defect |
| rename drift | 12 | shortlist; the matcher over-fires and this needs a human |
| no near match | 17 | most likely names a declaration the bean intends to **create** |

**The case I nearly got wrong: a bean naming work it intends to do SHOULD cite a
name that does not exist yet.** Reporting those as defects would manufacture ~17
findings out of ordinary planning. That distinction is now in the tool's docstring
so the next reader does not have to rediscover it.

### Four fixes, all to code I wrote in the previous pass

1. **Cross-product namespace index.** `fullname_index` paired every namespace in a
   file with every declaration in it, so a file with `namespace A … namespace B`
   manufactured `A.<decl from B>`. Those phantoms then **matched themselves** in
   the drift shortlist — `cites: X / near: X` for 10+ entries. A tool inventing
   the evidence for its own finding. Fixed with a namespace stack.
2. **Resolver precedence.** The prefix rule ran before the index and won for the
   wrong reason whenever a namespace shares a name with a module that does not
   declare the constant: `JucysMurphy.syt_adjacentSwap_connected` is declared in
   `JucysMurphyOV`, so the prefix rule imported `JucysMurphy` and reported ABSENT
   for a theorem that exists. Index first, prefix as fallback.
3. **`--classify-absent` read the wrong bucket** — the pre-probe unresolved list
   rather than the probe's own ABSENT lines. An identifier that never resolved was
   never asked about, so it is not evidence of anything.
4. **Possessive capture.** Lean allows `'` in identifiers, so the extractor pulled
   `QOU.Hecke.Wedderburn's` out of English prose.

Net effect of (1) + (2): identifiers probed **118 → 184**, ABSENT **44 → 29**.

## Standing limitation, stated rather than fixed

Some NO-NEAR-MATCH entries do exist in source — `WeierstrassProjection.weierstrassProjection`
is an `opaque` in the file of that name — but were ABSENT from the built olean.
The tool does not distinguish "not in the source" from "not in the artifact
because the artifact is stale", and conflating those is the exact confusion
`qou-pdgc` was opened for. Cross-checking against
`lean-olean-staleness-audit.py` would close it; not done here.

Current: **184 probed, 41 CLEAN, 35 REVIEW, 0 SORRY, 29 ABSENT, 79 DEF; 34
candidate-stale beans.** Raw output in `docs/audits/`.

## Standing limitation closed: ABSENT cross-checked against olean freshness

The previous pass shipped with a stated gap — the tool could not tell *"the
constant is not in the corpus"* from *"the constant is not in the artifact because
the artifact is stale"*. `--cross-check` closes it, and the result changes the
finding again:

| of 29 ABSENT | n | meaning |
|---|---|---|
| **artifact CURRENT** | **8** | the module is up to date, so the name really is not there |
| artifact STALE/MISSING | **21** | ABSENT says nothing — the probe read an environment older than the source |

**So the trustworthy count is 8, not 29, and not the 44 I first reported.** Three
successive corrections, each shrinking the claim: 44 → 29 (resolver fixes) → 8
(freshness cross-check).

The validation worth recording: `Archimedean.WeierstrassProjection.weierstrassProjection`
is the case I identified *by hand* last pass as the limitation — it exists in
source as an `opaque` yet probed ABSENT. The cross-check now files it under
STALE automatically, which is the right answer for the right reason.

The freshness rule is **imported from `lean_freshness`**, the same module the
axiom guard and the cone rebuilder use, not reimplemented. A freshness rule two
tools compute differently is the deadlock `qou-5v24` records, and this session
already reverted one batched reimplementation for disagreeing on 1 of 40 samples.

Incidental: `QOU.HeckeAlgebra.MarkovTrace` is in the stale bucket — the module
rebuilt this morning under `qou-1knw`. `main` moved underneath it within hours.
That is the churn rate the standing bean `qou-8jjo` exists to live with, measured
rather than assumed.

Raw output: `docs/audits/2026-09-06-bean-audit-cross-check.txt`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
