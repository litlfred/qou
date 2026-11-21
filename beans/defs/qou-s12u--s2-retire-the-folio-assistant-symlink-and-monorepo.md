---
# qou-s12u
title: S2 Retire the folio-assistant symlink and monorepo paths
status: todo
type: feature
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:15Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---

Size M. 87 tracked files reference folio-assistant/cat-harness via a gitignored symlink; 10 blocks bypass the ../schema/builders shim (import line only). Blocked on folio-assistant resolving adapters by dependency name and on the sci repo being seeded.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Measured: `git grep -l 'folio-assistant/'` (excluding AGENTS.md) matches **51,730** tracked files on main, mostly witnesses and sidecars carrying the path as provenance, so the '87 files' figure here counted only code imports and needs re-measuring before any plan. Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
