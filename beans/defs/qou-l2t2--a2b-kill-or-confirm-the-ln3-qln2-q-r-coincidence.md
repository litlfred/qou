---
# qou-l2t2
title: 'A2b: kill-or-confirm the ln[3]_q/ln[2]_q ~ r* coincidence'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T08:37:48Z
updated_at: 2026-11-17T11:58:00Z
parent: qou-v2om
blocked_by:
    - qou-fvzm
---

1.5871 vs r*=1.5852 (0.12%). **ROAST (fatal as stated):** the ratio used SYMMETRIC q-integers by my convenience, NOT derived. The unsymmetrized convention gives 1.6159 (2% miss). So the 0.12% depends entirely on an arbitrary convention choice = shape-probing, which the repo bans. Any probe MUST derive the normalization factor from the Markov moves FIRST, then evaluate -- never select the convention afterwards. Also the q-correction moves the WRONG way: classical log_2 3 (1.58496) fits r* 8x better than the q-deformed ratio, which is backwards if the mechanism were real. Build the probe to KILL this.

## Round 89 Progress (`litlfred/qou#8334`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/QuantumIntegerRatioAndLevelTwoStokesBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all directory-mode static audits).
- **80-dps Probe & Witness**: `computations/probes/quantum_integer_ratio_and_level_two_stokes_brick_probe.py` & `computations/probes/quantum-integer-ratio-and-level-two-stokes-brick.witness.json` (`scriptCommitSha = 4d6630423af48b31069a83d2407a32bd592eec79`, HEAD `c9d68807b57ef2cf531ca6340ce9802c12bf8d5d`, `allPassed = true`).
