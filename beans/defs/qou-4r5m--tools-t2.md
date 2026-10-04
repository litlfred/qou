---
# qou-4r5m
title: '[TOOLS T2] qou: declare computations/ witnesses and fsh-guts/ in qou.json'
status: in-progress
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:41Z
updated_at: 2026-10-04T18:23:08Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T2. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T2 | qou: declare `computations/` witnesses and `fsh-guts/` in `qou.json` | both declared; global invariant holds; `kg:validate` reports per-file results | S | T1 |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-10-04 (session_01NdDGeP1SyShmoUssLuRZ91): fsh-guts half done, the rest is blocked
- Declared `fsh-guts/` in qou.json (kind `fsh-guts`, a plain path, not the platform's branch-source form). Platform resolver confirms: `fshGutsDirectories(qou)` → `fsh-guts /home/user/qou/fsh-guts`. check-instance-graph clean; run-validate unchanged (5 issues).
- The witness half waits for T1 (qou-qb6t, the platform witness kind).
- The done-when check `kg:validate reports per-file results` CANNOT pass from qou today, for ANY qou file. Run from qou, kg-validate answers "could not determine" even for long-declared `library/0110001v3/structure.json`, because `owningInstanceRoot` resolves `checkoutRootFor(fallback)` from the script's own checkout. That is downstream tool discovery (T6, qou-bcuy), not this declaration.


## Owner ruling 2026-10-04
Verbatim: "all witnesses tools will need to go into the KG". Every witness producer becomes a declared Tool node whose output is a witness graph node. This needs T1 (the platform computation-witness graph kind) and T5 (wrap the content-wired producers). Recorded by session_01NdDGeP1SyShmoUssLuRZ91.
