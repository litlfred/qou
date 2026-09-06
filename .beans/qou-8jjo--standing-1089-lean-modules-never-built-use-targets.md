---
# qou-8jjo
title: 'Standing: 1089 Lean modules never built; use --targets ranking, not another --all sweep'
status: in-progress
type: task
created_at: 2026-09-06T03:33:19Z
updated_at: 2026-09-06T03:33:19Z
---


Successor to `qou-pdgc`, whose titled subject — the Hecke oleans being ~3 months
stale, with three `def`s reading as AXIOMS and `wenzlBridge` carrying a retracted
form — is fixed. What remains is a **standing condition**, not a task, and is
recorded here so it stops being re-scoped onto a closed bean.

## State, measured 2026-09-06

| | |
|---|---|
| source modules | 2698 |
| never built | **1089** |
| ...of those, imported by ≥1 other | **602** |
| ...leaves (imported by nobody) | 487 |
| stale olean (older than source) | ~616 |

## What has already been ruled out

- **Shallow sweep** (`--all -k`, topological order): 798 attempted, **798 ok**.
  Biased toward the easiest modules by construction, so it licenses little.
- **Targeted deep tail** (top 40 by reverse in-degree): **40 of 40 built**, cones
  covering 98 modules. Top in-degree fell 9 → 4; never-built 1187 → 1089.

So the highest-leverage never-built modules — the ones where a defect would both
exist undetected and propagate — **all compile**. No source defect has been found
anywhere in ~840 modules attempted. The corpus's known "37 modules silently
stopped compiling" (2026-04-25 CI failure) is not visible in either population.

## How to spend an hour on this, if you have one

    python3 scripts/lean-olean-staleness-audit.py --targets 20
    bash scripts/lean-direct-cone.sh <top module> -k -j3

**Do not run another `--all` sweep.** It costs 20+ hours, spends the first
several on modules already known to compile, and mostly re-confirms the shallow
result.

**Verify by artifact, never by parsing build output.** `--targets` recomputes from
olean existence on every run, so re-running it *is* the check — the ranking
shrinking is the evidence. This is not a style note: a status column derived from
grepping cone output produced **five** false `FAILED` labels in one 40-module
pass, every one of them the same missed case (`done: up-to-date=N in 0s` has
neither `ok=` nor `err=`). One of those five was `MathlibExt.FaddeevQuantumDilogarithm`
— in-degree 7, zero QOU dependencies, exactly the profile the targeting exists to
catch. It read like the finding and was not.

## Why this is standing rather than urgent

`scripts/session-start-coord-sweep.sh` prints freshness every session, so the
condition cannot sit unseen. A module with no olean is not a broken module; it is
an unbuilt one, and ~840 attempts say the difference matters. Close this only when
the count reaches zero or somebody decides the corpus does not need one.
