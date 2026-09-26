---
# qou-144c
title: 'Four beans carry off-vocabulary types: research, parent, child'
status: todo
type: bug
priority: low
tags:
    - beans-hygiene
created_at: 2026-09-26T10:52:11Z
updated_at: 2026-09-26T10:53:23Z
parent: qou-w3yy
---

**Measured 2026-09-26.** Four beans carry types outside the CLI's vocabulary
(`milestone, epic, bug, feature, task`):

| id | type | status | what it is |
|---|---|---|---|
| `qou-rsrg` | `research` | todo | "SEPARATE LANE (not a dependency): resurgence / Stokes…" |
| `miga` | `parent` | completed | Folio-Assistant Infrastructure Migration (Parent) |
| `mig1` | `child` | completed | Package References & Routing |
| `mig2` | `child` | completed | GitHub Workflows & Final Cleanup |

## These are two different stories

`miga`/`mig1`/`mig2` are a **hand-rolled hierarchy predating `--parent`** — the
types literally spell "parent" and "child". All three are `completed`, so the
correct shape is `miga` → `epic` with `mig1`/`mig2` as `task` children via
`--parent`. Low risk: nothing open depends on them.

`qou-rsrg` is different — `research` is a type someone wanted and the CLI does
not have. The nearest legal type is `task` (or `feature` if it is an umbrella).
Note the title already says "SEPARATE LANE", so the *intent* was to mark it as
not-a-dependency, which a type cannot express; a **tag** can.

## Cost and risk

Four `beans update --type` calls. Derived-from-corpus (the CLI's `--help` fixes
the vocabulary). The only judgement is `qou-rsrg`'s replacement type, and since
it is `todo` and tracks open research, **rule 13a** means its status must not
change while the research is open — only its type.
