---
# qou-ezqh
title: S5 Retire legacy QOU rendering, including the deploy/ viewer
status: todo
type: feature
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:16Z
updated_at: 2026-10-04T15:10:16Z
parent: qou-n4r9
---

Size M. Owner ruling 2026-10-04 (decision 12): retire deploy/. Retire the old docs-site workflow; add the staging workflow. Blocked on folio-assistant yj32 gaining paper support (math, Lean links, notation macros). Legacy LaTeX/PDF build is out of scope (owner ruling).

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.
