---
# qou-bvgw
title: 'A_ω step 2: GGM Stokes dictionary extraction (2012.00062)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-17T22:01:00Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** The extraction is done: the GGM 4₁ Stokes data is implemented exactly and reproduces. The dictionary does not license "3 is an index coefficient" (see qou-3ent).

Evidence: `qbeta_g3_ggm_stokes_41.py` re-run: exit 0, 9 s. Results: det W_m = 2, q-difference (49) exact, and the sandwich reproduces (60)–(64) with 1 distinct S⁺. The dictionary scope (eq 20 is "up to GL(r)", eq 21 is diagonal-only) was extracted by the LIT3 sweep recorded in qou-3ent.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
