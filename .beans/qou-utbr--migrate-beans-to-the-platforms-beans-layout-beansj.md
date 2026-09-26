---
# qou-utbr
title: 'Migrate .beans/ to the platform''s beans/ layout: beans.json, defs/, defs/archive/, workflows/'
status: todo
type: feature
priority: high
tags:
    - beans-hygiene
    - migration
created_at: 2026-09-26T11:19:55Z
updated_at: 2026-09-26T11:25:43Z
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
