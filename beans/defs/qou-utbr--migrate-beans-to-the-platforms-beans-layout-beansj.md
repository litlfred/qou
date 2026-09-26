---
# qou-utbr
title: 'Migrate .beans/ to the platform''s beans/ layout: beans.json, defs/, defs/archive/, workflows/'
status: in-progress
type: feature
priority: high
tags:
    - beans-hygiene
    - migration
created_at: 2026-09-26T11:19:55Z
updated_at: 2026-09-26T12:07:31Z
parent: qou-n4r9
---

**This is the structural half of the owner's "reeval of bean/workplan", and the
platform has already done it — so there is a concrete target rather than a
design question.**

## Measured: the platform migrated off `.beans/` entirely

Platform main `42ccfb38b63`:

```
beans/beans.json          (config)
beans/defs/               372 entries
beans/defs/archive/       631 entries
beans/workflows/          per-workflow JSON
.beans/                   0 entries   <- fully migrated away
```

qou today: **`.beans/` flat, 5,341 files, no `archive/`, no `workflows/`**, config
at `.beans.yml`.

## Why this is the fix for the orphan/scale problem too

`qou-63fo` records 2,039 of 2,446 open beans unparented and asks whether to build
an epic layer. A large part of what makes that list unreadable is that
**2,738 completed beans sit in the same flat directory as the live ones**. The
platform's answer is `defs/archive/` — 631 of its 1,003 beans are archived, i.e.
**63 % of its tracker is out of the working set**. Applying the same split to qou
moves ~2,890 completed+scrapped beans out of `defs/`, leaving ~2,450 live.

That is a **mechanical** change decided by status, with no per-bean judgement —
which is exactly what `qou-63fo`'s option (D) is not. It does not reparent
anything and does not need the ASK-THE-OWNER gate that mass-reparenting does.

## Open questions to measure BEFORE moving anything

1. **Does the `beans` CLI read `beans/defs/`?** qou's installed binary is
   `hmans/beans@latest` and reads `.beans/` via `.beans.yml`. The platform's
   `beans/beans.json` is a *different* config filename — so either the platform
   pins a newer/forked beans, or it drives the layout through folio-assistant's
   own tooling (`src/workflow/store.ts`, `bean-link.ts`, `beans-prime.ts` were
   all seen referencing beans). **Establish which before migrating**, or qou ends
   up with a layout its own CLI cannot read.
2. **What is `beans/workflows/*.json`?** Names seen on main include
   `code-change-review--*.json`, `crdm--folio-assistant-6lb8.json`. Unknown
   whether qou needs these.
3. **Do the ~5,341 files need reformatting**, or only relocating? The platform's
   `defs/*.md` front matter should be diffed against qou's before any move.

## Cost / risk

Relocating 5,341 files is one `git mv` per directory plus a config change, but
**every path in `.claude/skills/local/todo-manager.md`,
`bean-coordination.md`, `session-start-coord-sweep.sh` and the four
`*-queue.json` references changes with it** — 1,161 files mention `.beans` (and
14 mention `".beans` with a quote, i.e. inside JSON). Reversible by `git revert`
while nothing else has landed on top.

**Do not start until question 1 is answered.** A tracker the CLI cannot read is
worse than a flat one.



## 🛑 CORRECTION 2026-09-26 — the archive does NOT shrink the working set. My claim was wrong.

This bean's body above says: *"The platform's answer is `defs/archive/` — 631 of its 1,003
beans are archived, i.e. 63 % of its tracker is out of the working set. Applying the same
split to qou moves ~2,890 completed+scrapped beans out of `defs/`, leaving ~2,450 live."*

**Measured, and it is false: the `beans` CLI RECURSES into `archive/`.** Controlled
fixture — a scratch tree with `.beans.yml` `path: beans/defs`, one bean in `defs/` and
one in `defs/archive/`:

    beans list  ->  BOTH appear   (t-aaaa TOP LEVEL, t-bbbb ARCHIVED)
    RECURSES into archive/: True

So `beans/defs/archive/` is **filesystem organisation** — git, grep and editor
convenience — and buys **nothing** for `beans list`, the §4 idle-backlog policy, or the
session-start sweep. The scale argument in this bean's body is withdrawn.

**What that does NOT change:** the layout migration is still viable and still what
"align to f-asst" asks for. Gate question 1 of this bean is ANSWERED — the CLI reads a
`beans/defs` layout correctly, because `.beans.yml` keeps carrying the path. The platform's
own `beans/beans.json` says so in as many words: *"NOTE: `.beans.yml` still carries the
defs path because the `beans` binary is third-party; `bun run check:harness-dirs` fails
when they disagree."* Platform `.beans.yml` reads `path: beans/defs`.

**A corroboration I could NOT get, stated as such.** I tried to confirm the recursion on the
platform's real 372-defs / 631-archive tracker and could not: the platform CHECKOUT is at the
pin `df28d02` (2026-09-07), which predates its own beans migration, so `beans/defs` is
empty there and `beans list` reported 94 beans out of the pinned `.beans/` instead. The
372/631 figures are from `git ls-tree origin/main` and are correct for main; the recursion
finding rests on the fixture alone, which is controlled and decisive but is not the platform's
data.

## Measured blast radius for the move

| population | count |
|---|---|
| bean files to relocate | 5,341 |
| **EXECUTABLE files with a hardcoded `.beans` path** | **17** |
| prose references in `.claude/` skills, commands, agent memory | ~106 |
| `docs/` prose | 145 |
| `AGENTS.md` | 13 lines |
| references inside bean bodies themselves | 102 |

The 17 are what break: `scripts/bean-append-merge.py` (`path.startswith(".beans/")`),
`bean-completion-candidates.py`, `bean-dangling-path-audit.py`, `bean-declaration-audit.py`,
`bean-staleness-triage.py`, `bean-status-outlier-triage.py`, `check-beans.sh`,
`install-beans.sh` and others. The ten `.beans/*-queue.json` watcher queues move with the
directory but are named in AGENTS.md §4 and in several skills.

## Timing note, from AGENTS.md's own measurement

AGENTS.md records that bean files collide on essentially every landing — `main` takes 169
commits/24 h and `.beans/qou-brng` alone is touched by 9 of them. A wholesale directory move
conflicts with **every** in-flight branch that appends to any bean. Right now that risk is
unusually low: `main` is 0 ahead of this branch and the newest sibling branch is two weeks
old. If this does not land in that window it should wait for another one.
