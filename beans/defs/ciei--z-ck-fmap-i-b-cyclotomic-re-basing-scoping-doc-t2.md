---
# ciei
title: 'z-ck-fmap: I-B cyclotomic re-basing — scoping doc (T2, multi-session)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-06T23:40:24Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** The scoping doc this bean asked for exists, and its route was executed and obstructed (KC17, scope-(a)). That obstruction was derived in convention C (it uses bar-even z_C and c2 = −1), so any D-frame re-basing belongs under qou-cds1, not here.

Evidence: Scope doc landed: `docs/scope/2026-07-06-z-ck-fmap-ib-rebasing-scope.md`. Its steps B1–B3 were then executed (`docs/coordination/z-ck-fmap-keystone.md` §4-sexies/§4-septies). The B3-U outcome is OBSTRUCTION scope-(a), registry KC17: probe `qbeta_b3u_uside_transfer_probe.py` (4/4) plus Lean `uPow_bar_twist`. The keystone ledger's own currency banner says §1–§4 use convention C (z = √q/(1+q)).

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
