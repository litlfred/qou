---
# qou-f3hr
title: 'Accuracy compute & derivation (qou-j5b6, qou-bbr4, qou-tcl2/3): fix gg_scalar_per_step precision red, regenerate z_max=118 canonical-isotope shards, and wire derived T(T+1)+Coulomb composite beta/mass terms'
status: completed
type: task
priority: high
tags:
    - stability
    - compute-accuracy
created_at: 2026-11-28T10:29:08Z
updated_at: 2026-11-28T11:36:00Z
parent: qou-s028
---

2026-11-28 (Antigravity 92bff8c9, Sibling 8 in ws2-bridge-hecke -> claude/accuracy-compute-bbr4-j5b6-isospin-20261128): (1) Fix `qou-j5b6` witness-literal copy red gate in `gg_scalar_per_step_probe.py:96`; (2) complete `qou-bbr4` full `z_max = 118` canonical-isotope shard & index regeneration after #9699 Coulomb shape factor; (3) formalize & evaluate derived `T(T+1)` writhe + Coulomb isobaric slope (`qou-tcl2`, `qou-tcl3`, coordinating with #9747) on composite `Q_beta^-` (`ACCURACY.md` Table 3.4b).

Closed post-merge: landed on `origin/main` in PR #10000 (proton-pinned `gg_scalar_per_step_probe`, `Z00..Z118` 119-shard canonical-isotope witness + `qou-mass` vendor sync, `IsobaricBetaWritheCoulombStep.lean` + composite Q_beta probe).
