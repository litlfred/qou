---
# qou-s12u
title: S2 Retire the folio-assistant symlink and monorepo paths
status: todo
type: feature
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:15Z
updated_at: 2026-10-04T15:10:15Z
parent: qou-n4r9
---

Size M. 87 tracked files reference folio-assistant/cat-harness via a gitignored symlink; 10 blocks bypass the ../schema/builders shim (import line only). Blocked on folio-assistant resolving adapters by dependency name and on the sci repo being seeded.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.
