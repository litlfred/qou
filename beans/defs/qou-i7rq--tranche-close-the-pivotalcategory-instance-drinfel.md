---
# qou-i7rq
title: 'TRANCHE: close the PivotalCategory instance — drinfeldIso naturality + FGModuleCat'
status: completed
type: milestone
priority: normal
created_at: 2026-08-26T16:22:41Z
updated_at: 2026-08-26T17:01:28Z
---

CLOSED 2026-08-26. Both PRs merged: #5819 (f03cf592a4) shipped the ribbon/pivotal
modules; #5839 (639b6fa2c3) shipped pivotalOfBraided.

Front 1 (qou-knsx) closed and Front 2 (qou-gsdb / qou-sr22 / qou-chkh) was
superseded before execution -- FGModuleCat K is symmetric, hence braided, so the
concrete witness came free from the general instance.

The tranche's own lesson: my difficulty estimate was wrong by an order of
magnitude because I read the size of a simp-unfolded goal as the difficulty of
the theorem. Attacking the mate's ALGEBRA instead of its DEFINITION took ~60
lines.
