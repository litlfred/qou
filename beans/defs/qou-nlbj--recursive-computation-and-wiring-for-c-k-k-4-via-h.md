---
# qou-nlbj
title: Recursive computation and wiring for c_k (k >= 4) via Habiro equation
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-07T19:12:42Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: SUPERSEDED.** Superseded by qou-cds1 and pruned by qou-rwhj: c_{k≥4} cannot be validated against one datum, and wiring a C-frame ladder is forbidden. Any recursion for c_k has to come from a D-frame ladder that does not yet exist.

Evidence: Body is empty. c_k for k ≥ 4 has zero reliable digits against a single scalar datum (red-team audit `docs/audits/2026-08-16-ck-ladder-red-team.md`; qou-rwhj). The C-frame ladder is non-canonical. On the ruled base the ladder form is excluded (cds1 row).

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
