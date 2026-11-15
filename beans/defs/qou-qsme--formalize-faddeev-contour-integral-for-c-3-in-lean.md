---
# qou-qsme
title: Formalize Faddeev contour integral for c_3 in Lean
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

**Verdict: SUPERSEDED.** q\

Evidence: `qou-0gdn` (completed) plus the lean-route memo decided to use the modular-double product instead of the contour. `QOU/MathlibExt/PhiBProd.lean` landed: `faddeevPhi_phiBProd` inhabits `FaddeevPhi` under explicit `Multipliable` hypotheses, sorry-free by grep, 9 importers. The contour itself is needed only at \

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
