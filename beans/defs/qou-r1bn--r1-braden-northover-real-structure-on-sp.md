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
updated_at: 2026-11-21T08:00:00Z
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

## Result (2026-11-15)

Verdict: NO. The Braden-Northover real structure does not fix lambda without a choice. Draft PR #7834, stacked on #7825.
1. Scope (a): the corpus has no map from Bring's curve B, Jac(B) or H^1(B) to S_p.
2. Even with such a map, lambda stays free. Bring's one natural P^1 is P(H^1(E)), where H^1(B) = H^1(E) (x) std.
   - Hodge conjugation kappa swaps the Hodge pair. Matched to the chart centres, it becomes the reflection with normal i, which is lambda-invariant.
   - kappa.sigma* fixes the Hodge pair, so it lands in the #7825 family. But the circle it selects rotates with the phase of the identification, so arg lambda becomes that phase (moved, not removed).
   - All 26 real structures c.g of B induce the same map on P(H^1(E)). Only c commutes with S5.
Lean: BringRealStructureTransport.lean, lean-direct exit 0, no sorryAx (12 declarations).
The task is answered. The bean stays in-progress until #7834's disposition. No conjecture is closed here.

## 2026-11-21 — restored to the bean mount; core ported to main
This bean existed only on PR #7834's branch (`beans/` moved to the branch mount, issue #7642), so it was copied
here verbatim from that branch tip `bd78f30278`. The audit and `QOU/StandardModel/BringRealStructureTransport.lean`
are cherry-picked (-x) onto `claude/port-unowned-leftovers-2026-11-21` (thread "Port unowned leftover QOU PRs",
session https://claude.ai/code/session_01Qmmkt91GpCvJB15AZz7wMr). #7834 closes only after the owner taps close.
