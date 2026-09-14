# The 62 library modules that landed after the `--all` sweep all compile

*2026-09-14. Branch `claude/library-delta-sweep-2026-09-14`, bean `qou-8jjo`.*

## What was measured

The 2026-09-13 `--all` sweep judged **2830 of 2836 library modules at
`e22bd4561`, 0 RED**
([`2026-09-13-every-library-module-compiles-zero-defects.md`](2026-09-13-every-library-module-compiles-zero-defects.md)).
Between that commit and `316eafa36e` (2026-09-14), `main` added **51** library
modules and modified **11**. Those 62 had never been judged against current
source.

```
git diff --name-only e22bd4561..316eafa36e \
  -- content/quantum-observable-universe/lean/QOU | grep '\.lean$'    # 62
SHADOW=… REBUILD_JOBS=2 scripts/lean-shadow-verify.sh $(that list)
```

```
olean tree chosen by count: 2793 QOU oleans
# cone=414 changed_since_snapshot=2652 rebuild=406 levels=23 widest=110
rebuilding 406 module(s) from source, 23 level(s), 2x2 (jobs x threads)
```

## Result

| | |
|---|---|
| targets | **62** |
| `EXIT=0` | **62** |
| non-zero exit | **0** |
| cone modules rebuilt from source | **406 of 406** |
| `REBUILD FAILED` | **0** |
| wall, shadow creation → last write | **~26 min** |

Five warnings, all benign and all in two files: four
`automatically included section variable(s) unused` in
`QOU.BraidsAndKnots.ComponentCountSelectivity` and one `unused variable Γ` at
`QOU/OptionE/RungSelection.lean:82`.

So the library's compile status is now current against **today's** source, not
yesterday's — and the answer is unchanged: nothing is broken.

## What this does and does not establish

**Does.** Every module `main` gained or changed in the last day typechecks
against its real import cone, with 406 of its transitive dependencies rebuilt
from source rather than trusted from the snapshot. Under `lean-shadow-verify.sh`
the compile runs with `-DautoImplicit=false -s 65536`, so it is the strong
check, not a bare `lean` (bean `qou-56qy`).

**Does not.** This is 62 modules and their cone, not the library. The other
~2400 modules keep the 2026-09-13 verdict, which was taken against a commit that
is now a day behind. And 8 content-block siblings remain unverifiable in this
container for want of Mathlib oleans — a cache-branch gap, not a corpus defect
(recorded in AGENTS.md).

## The method, and why it is the one to use

The bean's standing advice is *"do not run another `--all` sweep"*. The reason
recorded there is that `--all` re-confirms modules already known to compile.
That is true but secondary. **The real reason is the half-life:** a 3 h 10 m
`--all` run is stale in about a day at the measured rate of ~62 new-or-changed
library modules per day.

The delta method costs ~26 min and judges exactly the modules whose status is
unknown. **Do not reach for the sweep's own dirty-closure mode instead** — it
reports `DIRTY CLOSURE 2821 (97.7 %)` in this container, so it costs an `--all`
run. That 97.7 % is genuine and not mtime churn: of 2563 modules the freshness
rule calls changed, restricting the mtime term to worktree-dirty files moves it
to 2556 — **7 modules, 0.27 %**
([`2026-09-14-library-sweep-churn-probe.py`](2026-09-14-library-sweep-churn-probe.py)).

## First real-workload shape for the parallel rebuild (#7387)

Module count per topological level, in order:

```
110 66 46 34 18 21 24 10 6 6 9 5 8 8 8 5 4 4 4 3 2 2 3
```

**The first seven levels carry 319 of 406 modules (79 %), all ≥ 18 wide** — the
regime where #7387's parallel rebuild was measured at **1.96×** on a width-40
level. The tail is 16 levels totalling 87 modules at widths 2–10, where
`REBUILD_JOBS=2` is barely saturated and the level barrier costs more than it
buys; #7387's own A/B measured **4.4 % slower** on a narrow cone.

**No speedup is claimed for this run.** The serial version was not run on this
cone, so there is no A/B here — only the width distribution, which says the
favourable regime is where the work is. The open follow-up from `qou-srb1`
stands: a global work queue would remove the tail's barrier cost. It is not
done, and it is a larger change to the script that guards the real olean tree.

## Artifacts

- log: `/tmp/claude-0/delta-sweep.log` (container-local, not committed)
- shadow kept at `/tmp/claude-0/delta-shadow` for reuse via `SHADOW=`
- the real olean tree is untouched: `lean-shadow-verify.sh` unlinks before
  writing and writes only inside `$SHADOW`
