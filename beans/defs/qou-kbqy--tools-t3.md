---
# qou-kbqy
title: '[TOOLS T3] Rename qou tools/ → packages/ (container only)'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:41Z
updated_at: 2026-10-04T16:36:18Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T3. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T3 | Rename qou `tools/` → `packages/` (container only) | git sees pure renames (0 insertions, 0 deletions); every importer resolves (`build-pyhecke-native.sh`, the `_path_bridge` search); witnesses unchanged | M | owner (§5.6) |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
