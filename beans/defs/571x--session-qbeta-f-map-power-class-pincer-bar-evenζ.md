---
# 571x
title: 'Session: qbeta f-map power-class pincer (bar-even/ζ₄) + kernel-constraint Lean'
status: completed
type: epic
priority: normal
created_at: 2026-07-06T11:48:04Z
updated_at: 2026-07-25T19:45:00Z
---

2026-07-13: advanced from claude/askey-derivation-gap-canonical-xaf8h7 (orig PR #3429 closed unmerged). Landed Arm-2 Lean prune + refuted-class row C19. Remaining: Arm-1 symbolic probe + full-class unconditional verdict. Axis has largely moved to the analytic Φ_b face (C15-C18, §3 update 2026-07-11).

2026-07-25 (corpus-grep currency): the "remaining Arm-1 + full-class verdict" above is **already discharged in-corpus** — refuted-class-map row C19 records the Arm-1 probe **executed 2026-07-13 (PR #3781)** (`qbeta_fmap_power_class_prune.py`, all six obstructions fire with exact closed forms), so C19 is REFUTED — FULL CLASS, scope-(b) UNCONDITIONAL. This bean's status note simply lagged the row. The only genuine loose end — the Arm-2 Lean marked "lean-direct pending" in C19 — was closed: `QbetaFmapPowerClassPrune.lean` independently re-verified `lean`-direct exit 0 against current `main` (dep `ComplexVolumeZeta4Partner` recompiled). Refuted-class-map C19 + row-number note updated to remove the stale "partial/pending" framing. Nothing further to derive on the power-class pincer; the live frontier is the analytic Φ_b face + keystone W_λ axis (separate beans). Recommend closing 571x (owner).
