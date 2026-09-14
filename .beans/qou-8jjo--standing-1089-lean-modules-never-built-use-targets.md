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

---

## 🛑 The headline number is CONTAINER STATE, not corpus progress — 2026-09-14

Re-measured today, same script, same flag:

    python3 scripts/lean-olean-staleness-audit.py --targets 10
    never built: 97 of 2886 module(s); 36 imported by ≥1 other, 61 leaves

**1089 → 97 is not 992 modules repaired.** Nothing was repaired. The count is
`(source modules) − (oleans present in THIS container)`, and between the two
measurements the restored cache branch changed: AGENTS.md records the
2026-09-06 seed at 2702 QOU oleans, and this container holds **2793**, all
2793 trace-paired. A different restore gives a different count with no change
to the corpus whatever.

So the number this bean is titled after is not a corpus property and cannot be
driven to zero by any amount of building — a fresh container on a thinner
cache branch would report ~1100 again tomorrow. **Do not read a movement in it
as progress, in either direction.** That is the same container-scoped-inference
trap the `--all` audit retracted three times
(`docs/audits/2026-09-13-every-library-module-compiles-zero-defects.md`).

## What the corpus-level answer actually is, and its half-life

The question behind the title — *is any library module broken?* — was answered
on 2026-09-13 by a full `--all` sweep at `e22bd4561`: **2830 of 2836 judged,
0 RED**. That is a statement about source, not about oleans, and it is the
right kind of answer.

It is also **perishable, and faster than anyone had measured**:

| | |
|---|---|
| library modules at `e22bd4561` (2026-09-13) | 2835 |
| library modules at `316eafa36e` (2026-09-14) | **2886** |
| added since the sweep | **51** |
| modified since the sweep | **11** |
| **unjudged against current source** | **62** |

**~62 modules of unjudged surface per day**, i.e. a full sweep's green decays
at roughly 2 %/day. A 3 h 10 m `--all` run buys about a day. That is the real
argument for this bean's "use `--targets`, not another `--all` sweep" — not
that `--all` re-confirms the easy modules (it does), but that its answer is
stale before the next session starts.

## The cheap replacement: sweep the DELTA, not the closure

    git diff --name-only <last-sweep-commit>..HEAD \
      -- content/quantum-observable-universe/lean/QOU | grep '\.lean$'
    scripts/lean-shadow-verify.sh $(that list)

Measured on today's 62: `cone=414 rebuild=406 levels=23 widest=110` — a few
tens of minutes against 3 h 10 m, and it judges exactly the modules whose
status is actually unknown.

**Do NOT reach for the sweep's own dirty-closure mode for this.** It reports
`DIRTY CLOSURE 2821 (97.7 %)` here, so it costs an `--all` run.

### A hypothesis about that 97.7 % — mine, and MEASURED FALSE

`lean-library-sweep.py`'s freshness rule takes `max(last-commit-date, on-disk
mtime)`, and its own comment at line 232 says *"branch switching rewrites the
mtime of every differing file … some of that widening is churn"*. I inferred
the 97.7 % was mostly that churn, and that restricting the mtime term to files
dirty in the working tree (`git status --porcelain`) would collapse it.

It does not. Of 2563 modules the current rule calls changed, the stricter rule
calls **2556** changed — **7** are pure mtime churn, 0.27 %. The olean tree
genuinely is behind 2563 modules' last source commit. The rule is sound as
written and needs no change; I had a fix drafted and it would have bought
nothing. Probe kept at `docs/audits/2026-09-14-library-sweep-churn-probe.py`.
