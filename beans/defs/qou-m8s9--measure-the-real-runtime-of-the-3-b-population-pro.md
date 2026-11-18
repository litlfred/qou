---
# qou-m8s9
title: Measure the real runtime of the 3 B-population producers that exceeded 300s
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T15:43:19Z
updated_at: 2026-10-04T15:21:32Z
parent: qou-5vkl
---

audits/term5_aK_audit.py, garside-irrep-qvalues.py and qbeta/qbeta_h4_route_a_gate_probe.py each exceeded the 300 s per-producer budget in the B-population sweep. 300 s is a BOUND, not a runtime - a TIMEOUT is neither UNCHANGED nor SUBSTANTIVE, it is an absence of measurement, and must not be reported as either. Re-run each under a budget that lets it finish and record the actual wall time, then decide whether its witness is drainable. PR #5889.
