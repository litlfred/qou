---
# qou-1knw
title: 'The keystone axiom guard cannot report: exit 2 on ~104 stale/missing oleans in its own cone'
status: done
type: task
created_at: 2026-09-06T04:38:59Z
updated_at: 2026-09-06T04:38:59Z
---


Found while checking whether the modules built under `qou-pdgc` / `qou-8jjo`
carried hidden `sorryAx`. They did not — **1226 declarations across 40 modules,
zero `sorryAx`** — but the attempt turned up something larger.

## The guard could not run

`scripts/lean-axiom-guard.py` is the corpus's `#print axioms` gate. It exits **2**
when any olean in the transitive cone of its registry is missing or stale, on the
stated principle that "a verdict from a stale olean set is not assurance — it is
the axiom status of an old snapshot." Measured 2026-09-06: **~104 modules** in
that cone were stale or missing, two of them (`QOU.Knot.RivinConcavity`,
`QOU.MathlibExt.IdealTriangulation`) **never built at all**.

So the gate has been silently non-functional. Not red — *blind*, which is the
failure mode `AGENTS.md` already names for CI health, here reproduced in the
axiom layer.

Rebuilding its cone (289 modules: 127 ok, 162 up-to-date, **0 errors**) restored
it: **exit 0, all 283 registry declarations checked.**

## What it found the moment it could speak: a PROMOTION

Four declarations recorded `sorryAx` since 2026-08-07 now measure exactly
`[propext, Classical.choice, Quot.sound]`:

- `BraidKnot.OVTopAssembly.sum_numSYT_sq_eq_factorial`
- `BraidKnot.RSKBurnsideDischarge.rskBurnsideHolds`
- `BraidsAndKnots.PlancherelNormalisation.sum_sytDim_sq_eq_factorial`
- `BraidsAndKnots.PlancherelNormalisation.nuV_top_closed_form_unconditional`

The upstream gap the registry described — RegularRepBlockTrace's sorry plus a
Specht-core cone where 16 of 23 modules carried sorry — is closed.

## The nuance that nearly went the wrong way

All four carry `[SnIsotypicSpechtSplit ℚ]`. My first check ran `infer_instance`
**without importing the instance module** and it failed, which read as
"conditional on a premise the corpus cannot supply" — the §3b-cond pattern
exactly. That was my error, not the corpus's: importing
`SnIsotypicSpechtSplitInstance` synthesises it, and the instance is itself clean.

So these are **established, not merely conditional** — but *derivative*: the
instance is built from `QOU.Mathlib.rskBurnsideHolds` (Schensted, unconditional,
no binder), so citing any of the four as the *source* of the RSK identity is
circular, as `RSKBurnsideDischarge.lean`'s own docstring already says. The
registry comment now records all of this.

## Surfaces corrected

The registry block (four entries `sorryAx` → `clean`, with the derivation
caveat), and `WedderburnConstruction.lean`, whose docstring quoted the stale
`sorryAx` entry as current when I wrote it in `qou-usol`.
