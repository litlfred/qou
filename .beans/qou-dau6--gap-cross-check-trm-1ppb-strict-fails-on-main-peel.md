---
# qou-dau6
title: 'GAP: cross_check_trM_1ppb --strict fails on main — peel witness computed at proton q0 but gate expects the muon pin'
status: todo
type: task
priority: normal
created_at: 2026-08-09T12:34:43Z
updated_at: 2026-08-23T07:59:27Z
---

## Cross-link (2026-08-23)

Same failing gate as `qou-3zby`, which carries a **different** root-cause
hypothesis: a **C/D convention straddle across the four methods**
(`hoef_vs_chi` improved 7 orders while `hoef_vs_peel` and `hoef_vs_habiro`
degraded), plus a third candidate — **import-cone drift in the Hoefsmit
cone** (`hoefsmit_50dps` 0.388 -> 0.575 on a bare re-run, the digits
AGENTS.md uses as its canonical import-cone example).

Three candidate causes for one red: (a) proton/muon pin mismatch [this bean],
(b) C/D straddle [qou-3zby], (c) import-cone drift [new]. Adjudicate together
rather than fixing against one hypothesis — the pin-mismatch fix would not
close (b) or (c), and would look like it had.
