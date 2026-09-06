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

## Follow-up: the gate now reports its own liveness (2026-09-06)

Restoring the gate by hand fixed nothing durable — the next cold-cache session
would have got exit 2 again and another month of silence. `--can-run` closes
that: it answers *can this gate produce a verdict at all?* using the same
freshness rule the verdict path uses, with no Lean and no olean contents read.
Exit **0 = READY**, **3 = BLIND**, deliberately distinct from the verdict path's
2 so a caller can tell "absent" from "environment broken".
`session-start-coord-sweep.sh` prints it, and renders "could not determine" as
explicitly **not a pass**.

It found a regression on its first run: `QOU.Torsion.GlobalGluing` had gone stale
within the hour, since `main` moved under the rebuild. Rebuilt; the gate now
reports `READY — 283 declarations across 49 modules`.

## A change I made, measured, and reverted

`check_freshness` calls `git log -1 --format=%ct` once per module, ~289
subprocesses. I replaced that with a single `--name-only` history walk and a
path → time index, and it was **wrong**: measured against the per-file call on a
40-module sample it disagreed on one
(`ParticleInteractions/mass_categorical_descent`, 7.8 days newer). `git log --
<path>` applies history simplification and prunes merges that did not change the
file; `--name-only` lists the path at those merges anyway.

The disagreement errs conservative — falsely "stale", never falsely "fresh" — so
no false verdict would have escaped. Reverted anyway: a freshness rule two tools
compute differently is exactly the deadlock `qou-5v24` was opened for, when this
gate compared COMMIT time while the rebuilder compared MTIME.

**And the speed case for it was not real either.** I justified the change with
"16.4s → 0.131s, 125×". The 16.4s was a cold git cache and the 0.131s a warm one,
so that compared cold-vs-warm rather than per-file-vs-batched. Warm, the per-file
form runs in ~0.10s (0.139 / 0.096 / 0.097 over three runs); cold it is ~16s
against a 2.48 GiB pack. Both the correctness finding and the bad measurement are
recorded in the script, because the wrong comparison is easy to make again and it
was briefly the stated reason for changing shared code.
