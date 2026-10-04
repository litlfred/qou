---
# qou-abvn
title: S1 Declare the dependency on folio-assistant-sci; drop folio.config.json (#7484)
status: todo
type: feature
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:15Z
updated_at: 2026-10-04T15:10:15Z
parent: qou-n4r9
---

Size S. qou.json gets needs:["folio-assistant-sci"]; qou.config.json gets a pinned {name, git, ref} dependency. Done when check:instance-config and check:needs-dependencies are green and content parity holds.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.
