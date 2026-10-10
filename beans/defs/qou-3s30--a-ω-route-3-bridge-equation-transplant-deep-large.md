---
# qou-3s30
title: 'A_ω route 3: bridge-equation transplant — deep large-order on exact κ₁..κ₈, complex Borel singularity scan (W5 exemplar method)'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-17T20:20:36Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: SUPERSEDED.** Scrapped: the deep large-order/Borel scan was run under qou-fgte (qbeta-stokes3-largeorder-amplitude*.witness.json). The amplitude question it was meant to feed lives in qou-esx7.

Evidence: Empty body. The large-order/Borel work it names was executed under qou-fgte: `computations/qbeta/qbeta_stokes3_largeorder_amplitude_probe.py` and `_fit.py` give a 12-order κ-tower, κ₁–κ₄ = closed forms to 40+ digits, Borel–Padé, and a single real singularity. The fit re-run reproduced the witness result exactly. No "bridge-equation transplant" exists anywhere in the repo.

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
