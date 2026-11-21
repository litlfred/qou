---
# qou-xumu
title: 'GAP: lean-library-sweep.py ABORTS on one slow module — 101 modules never attempted'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T11:26:54Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
---

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

**Completed.** `scripts/lean-library-sweep.py` on main has `--timeout` (default 1800 s) and catches `subprocess.TimeoutExpired` as TIMEOUT (unverified), and the sweep continues (lines ~338 and ~724 at `2ae54ab401`). One slow module no longer aborts the run.
