---
# qou-6u3n
title: '[TOOLS T13] Retire renderers and deploy into fsh-guts/ (deploy/, paper-builder-image, build-lean-mcp, docs-site.yml,…'
status: in-progress
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:45Z
updated_at: 2026-10-04T18:06:44Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T13. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T13 | Retire renderers and deploy into `fsh-guts/` (`deploy/`, `paper-builder-image`, `build-lean-mcp`, `docs-site.yml`, typedoc, `make-all-tables`, `split-pdf`) and move `computations/_deprecated` → `fsh-guts/` | pure renames; `convention-c-deprecated-citation-audit.py` shows 0 content citations into `_deprecated` before the move | S | owner ack on `_deprecated` |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Progress 2026-10-04

Done (commit 46af43b18): docs-site.yml and docs/_config.yml parked in fsh-guts/deprecated by pure rename. Remaining: deploy/ (needs the owner to stop the live self-updating server first; its access lists are CODEOWNERS-protected), and computations/_deprecated (owner ack). The LaTeX/PDF path is out of scope (owner: ignore, not retire).


2026-10-04 (session_01NdDGeP1SyShmoUssLuRZ91): TypeDoc retired. typedoc.json → fsh-guts/deprecated/docs-site/ (pure rename); build:docs script and typedoc devDependency removed; README points at the platform's gen-schema-docs. Still to do in T13: deploy/ (waits on the owner's server decision), paper-builder-image, build-lean-mcp.yml, make-all-tables, split-pdf, computations/_deprecated.
