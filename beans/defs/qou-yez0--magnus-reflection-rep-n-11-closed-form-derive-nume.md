---
# qou-yez0
title: Magnus reflection-rep (n-1,1) closed form -- DERIVE (numerical fit inconclusive)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T17:41:56Z
updated_at: 2026-10-04T15:21:23Z
parent: qou-v2om
---

tr(rho_{(n-1,1)} Omega2) is the dominant term of the Magnus sign, NEGATIVE for all A=2..13 (measured). Growth base drifts (~3.85 at A=13, not converged); the 'base=4' fit was RETRACTED as a transient (#6265). A closed form needs DERIVATION (standard rep + germ log-derivative are explicit), not fitting. Would give sign(P(A)) in closed form. Data A=2..13 in magnus_sign_growth_analysis.py --reflection.

## Round 77 Progress (2026-11-17T12:34:08Z)
- Advanced in PR `litlfred/qou#8342` (branch `feat/round77-uicgate-deuteron1st-ecatrad-polydom-magnusbound-43c1`, head `5cf054672f4eaf9dc177beab1666e1bca45dbc19`).
