---
# qou-6u3n
title: '[TOOLS T13] Retire renderers and deploy into fsh-guts/ (deploy/, paper-builder-image, build-lean-mcp, docs-site.yml,…'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:45Z
updated_at: 2026-10-04T16:36:21Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T13. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T13 | Retire renderers and deploy into `fsh-guts/` (`deploy/`, `paper-builder-image`, `build-lean-mcp`, `docs-site.yml`, typedoc, `make-all-tables`, `split-pdf`) and move `computations/_deprecated` → `fsh-guts/` | pure renames; `convention-c-deprecated-citation-audit.py` shows 0 content citations into `_deprecated` before the move | S | owner ack on `_deprecated` |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
