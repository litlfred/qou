---
# qou-d838
title: Other :True carriers (needs author intent)
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T18:41:39Z
updated_at: 2026-11-22T21:17:12Z
parent: qou-6qbv
---

mass-tower-deeper-fillers(83,121,129), MathlibExt/SDP(141,150), MmuR9V9Closure(453,456), WignerSU4FromSpinIsospin(22,29,48), S5bbGeometricIndex(28,32). Assess each: SDP dual_feas/obj_eq may be LP-statable; others likely need author intent.

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.
Done on main: every carrier this bean listed is gone. `mass-tower-deeper-fillers.lean` lines 19/23/78, `MmuR9V9Closure.lean` 432/472 and `WignerSU4FromSpinIsospin.lean` 148 now hold only history comments saying the `: True` fields were removed; `MathlibExt/SDP.lean` and `S5bbGeometricIndex.lean` have no `True` field (grep for `: True`, `:= trivial` returns nothing). The statements behind removed markers are tracked in `qou-n2un`.
