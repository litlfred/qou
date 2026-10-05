---
# qou-kbqy
title: '[TOOLS T3] Rename qou tools/ → packages/ (container only)'
status: scrapped
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:41Z
updated_at: 2026-10-05T07:12:57Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T3. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T3 | Rename qou `tools/` → `packages/` (container only) | git sees pure renames (0 insertions, 0 deletions); every importer resolves (`build-pyhecke-native.sh`, the `_path_bridge` search); witnesses unchanged | M | owner (§5.6) |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Owner ruling 2026-10-05: option A (session_01NdDGeP1SyShmoUssLuRZ91)
Do NOT rename tools/ → packages/. Measured cost of the rename: 349 files moved and 601 files outside tools/ rewritten, including 36 under folio/ (paper content), 229 producer scripts (every scriptHash changes, so every witness reads stale), 136 beans and 157 docs. Instead qou.json declares the instance's `tools` graph at `tool-defs/`, overriding by id, and tools/ keeps the Rust and Python packages. The owner chose option A when asked. Scrapped rather than completed: the rename was decided against, not done.
