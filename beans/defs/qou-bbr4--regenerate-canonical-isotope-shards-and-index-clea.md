---
# qou-bbr4
title: Regenerate canonical-isotope shards and index cleanly after Coulomb shape factor (#9699)
status: todo
type: task
created_at: 2026-11-27T21:20:51Z
updated_at: 2026-11-27T21:20:51Z
parent: qou-myts
---

Left out of #9715: a regeneration run in a resource-limited container truncated the index (z_max 118 -> 20) and moved rows at A >= 5. Regenerate on a container that can complete the full run, then verify z_max = 118 before committing.
