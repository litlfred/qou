---
# qou-cmii
title: 'run_pipeline false staleness: q0 digit-length compare and _path_bridge drift'
status: in-progress
type: task
priority: normal
created_at: 2026-11-24T21:01:22Z
updated_at: 2026-11-24T21:16:58Z
parent: qou-s028
---

## 2026-11-24 (agent, session 01Eucf)
(1) The q0 width artifact is fixed in PR https://github.com/litlfred/qou/pull/9401 (02ef1d94019): matches_live_q0 now uses max(ulp_recorded, ulp_live), with a 5-test file. Corpus stale-q0 witnesses 452 -> 275; run_pipeline --content-only stale-q0 reason 35 -> 10 (the remaining 10 carry muon pins or q*).
(2) MEASURED: the '_path_bridge' cascade (134 of 226 in --content-only --dry-run) is NOT drift. _path_bridge.py has not changed since 2026-10-10 (77b39c7d1f3). run_pipeline treats every imported local module as a script, and a module with no witness returns 'no witness file' -> stale. Every importer then inherits 'dependency _path_bridge.py is stale'. The same applies to lp_dual_solver, knot_braid_database and binding_canonical (1 each). The right rule, which is a POLICY CHANGE and so goes to the owner: a dependency that emits no witness should propagate staleness only through a source-hash change, as the INFRA_SCRIPTS mechanism already does, never through 'no witness file'. Note that .infra-hashes.json is gitignored and absent in fresh containers, so the infra mechanism also flags everything on a first run.
