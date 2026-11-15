---
# qou-v6oz
title: 'Task5: close m_K/m_π EM-factor truncation-honesty gap — derive (3q²−1)/2q² or re-scope 47 ppb as truncation-dependent'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T20:13:22Z
updated_at: 2026-11-15T13:30:28Z
parent: qou-3l2l
---


---

## DISSOLVED, then LANDED 2026-08-22 (PR #5467)

This bean asked to *"derive (3q²−1)/2q² or re-scope 47 ppb as
truncation-dependent"*. Created 2026-08-08 — one day before the owner
ruled, on **2026-08-09**, that the EM factor is the full series
`1 + log(1+ℏ_q)` and that the truncation is a fit. `docs/precision-goals.md`
records the question as *"dissolved rather than answered — it is not the
physical object, it was where the series happened to be stopped"*.

The ruling never reached any producer. It has now: the dashboard, the
producer, `docs/observable-sector-tracker.md` and
`prop:meson-em-sinh-closed-form` all carry the full series, at 51.48 ppb
against a 263.6 ppb target (5.1× margin, scorecard unchanged at 1/5).

Neither branch of this bean's ask applies any more: `(3q²−1)/(2q²)` did
not need deriving, it needed removing, and the ppb figure did not need
re-scoping as truncation-dependent because the truncation is gone.

## 2026-11-15 closed (owner card, E3 bean triage)

Verified done against main 0d4e4a005: Dissolved by the 2026-08-09 owner ruling and landed in PR #5467 (merged 2026-08-23); computations/meson_em_sinh_closed_form.py carries the full series 1 + log(1+h_q). Not an open conjecture.
