---
# qou-r1bn
title: 'R1: does the Braden-Northover real structure on Jac(Bring) induce a real structure on S_p that fixes lambda without a choice?'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - real-structure
created_at: 2026-11-15T09:00:00Z
updated_at: 2026-11-15T09:00:00Z
parent: qou-qs0e
---

Owner 2026-11-15 ("work R1"), via coordinator session_01M5GA1LmsEf8tSMxFjMkmnn (tracker #7735).
Follows stream 6b (draft PR #7825): the polarization dictionary (phi0,phi1) -> [phi1 : lambda phi0]
has a free lambda in U(1); the cone carries a U(1) of real structures p -> u p u-bar, u = c j + d k,
and selects none. The Braden-Northover real structure on Jac(Bring) was the one untested candidate.

Question: does it induce an antilinear involution on S_p, and does that fix lambda without a choice?

Branch: claude/r1-braden-northover-real-structure-2026-11-15 (stacked on #7825).
Audit: docs/audits/2026-11-15-r1-braden-northover-real-structure-on-sp.md
Lean: QOU/StandardModel/BringRealStructureTransport.lean
