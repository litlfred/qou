---
# qou-xeys
title: Wire the derived Coulomb mirror term into the light-isotope binding
status: completed
type: task
priority: normal
created_at: 2026-08-10T17:11:59Z
updated_at: 2026-08-10T17:21:45Z
parent: qou-1nvh
---

Done in c213ef37 (PR #4939). Rewired onto canonical coulomb_energy: worst-case mirror residual 37% -> 17%, inside Nolen-Schiffer. Also found+fixed stale verdict prose asserting production over-splits 200-350% (actual now 0-53%); headline every-pair assertion left FAILING on 3H/3He rather than weakened. Follow-up opened: qou-lbdl.
