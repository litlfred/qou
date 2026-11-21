---
# qou-pjfi
title: '[REST S-REST-1] Declare qou''s undeclared directories'
status: todo
type: feature
priority: normal
tags:
    - migration
    - rest
    - upstream-fa
created_at: 2026-10-04T16:35:58Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---

From the REST migration analysis (2026-10-04), story S-REST-1. Full report: docs/audits/2026-10-04-workplan-and-migration/REST_report.md.

1. S-REST-1: Declare qou's undeclared directories. - Scope: add `docs` (split into `notes`/`archive` context kinds), `uploads`, `schemas` and `figures` entries to `qou.json`. - Done when: `harness:dirs:check` and `audit:coverage` list them; `git diff --stat` touches only `qou.json`. - Size S. Depends on: platform pin move (qou-8321).

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Blocked 2026-10-04: no fitting graph kind

Checked against the platform graph-kind registry at 26c5d37: `docs` is renderable and needs docs/docs.json (it would pull qou's working notes into the site), `uploads` is an intake queue (holds: state), and `schemas` needs a schemas.json concern-group declaration. There is no `notes` (context) kind for working notes, which the REST analysis already named as a platform gap. Unblocks when folio-assistant adds that kind; until then declaring docs/ would be wrong rather than incomplete.



## Owner ruling 2026-10-04: split docs/

- Outstanding-work docs (docs/backlog/, plans, attack-option lists) go to beans (agent work) or todos/ (the owner's own work).
- Math notes (derivation notes, cheat sheets, proofs, refutations) are NOT todos: filing them there would count finished derivations as open work. They wait for a working-notes graph kind, filed upstream as folio-assistant bean folio-assistant-8npa (child of 8jt6), or move into folio/ blocks only by an owner-approved verbatim move.
- Handoffs and coordination logs go to beans/notes; status surveys to beans/surveys (classify first, move by rename after approval).


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
