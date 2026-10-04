---
# qou-abvn
title: S1 Declare the dependency on folio-assistant-sci; drop folio.config.json (#7484)
status: completed
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:15Z
updated_at: 2026-10-04T16:34:43Z
parent: qou-n4r9
---

Size S. qou.json gets needs:["folio-assistant-sci"]; qou.config.json gets a pinned {name, git, ref} dependency. Done when check:instance-config and check:needs-dependencies are green and content parity holds.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.



## Summary of Changes

Done 2026-10-04 on branch claude/s1-platform-pin-2026-10-04: platform pin cb194b1 -> 26c5d37 (platform main) in .folio-assistant-pin and build.yml; qou.json declares needs [folio-assistant-sci], repository and canonicalUrl, and drops the retired dependents key; qou.config.json re-points adapterModule to folio-assistant-sci and authors the dependency edge; folio.config.json removed; setup-folio-assistant.sh fetches the pinned SHA and initialises submodules. run-validate 4 -> 5 issues (same 4 + qa-reports notice); check-instance-graph clean; no content file changed.
