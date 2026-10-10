---
# qou-i9iq
title: '[REST S-REST-8] Hygiene'
status: completed
type: feature
priority: normal
tags:
    - migration
    - rest
created_at: 2026-10-04T16:36:01Z
updated_at: 2026-10-04T18:06:45Z
parent: qou-n4r9
---

From the REST migration analysis (2026-10-04), story S-REST-8. Full report: docs/audits/2026-10-04-workplan-and-migration/REST_report.md.

8. S-REST-8: Hygiene. - Scope: the `" .agents"` rename, `.mcp.json` absolute path, typedoc, devcontainer, lean-mcp, `.prepare-merge-ts`. - Done when: no tracked path has a leading space and no config names `/home/`. - Size S.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Progress 2026-10-04

Done (commit c468e3edf): the space-prefixed ' .agents' directory's only file moved into .agents by pure rename.


## Done 2026-10-04 (session_01NdDGeP1SyShmoUssLuRZ91)
Done-when holds: `git ls-files | grep -c '^ \|/ '` = 0, and no config names /home/ (.mcp.json fixed in qou#7503; the remaining /home/runner strings are in build-logs/lean-build-status.json, a log, not a config). typedoc retired under T13. .devcontainer names no /home/ and is left for T13 (its image is built by the to-be-retired build-lean-mcp.yml). .prepare-merge-ts is a one-line timestamp stamp; left as is.
