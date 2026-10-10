---
# qou-p7n5
title: 'FINDING: R(q0) is a SINGLE SCALAR - c_2 := (R-1)/u^2 reproduces it exactly (residual 0.0 at 70dps), so a self-consistent chain gives c_k = 0 for all k>=3. At most ONE c_k is determinable from this datum. Canonical c_2=-1 and c_3=-2 are TESTED and pass (59x, 93x residual drops); c_4 onward buy <=1.81x against a ~117x expectation and are unconstrained. The ladder above c_3 must come from the Habiro/q-difference structure, which is what prop:q-beta-c-k-recursion says and why it forbids fitting'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - close-candidate
created_at: 2026-08-10T03:45:35Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: CLOSED-PROVED.** The one-datum/one-coefficient finding is proved by construction and holds in any frame. Its sub-claims "c_2 = -1, c_3 = -2 tested and pass (59×, 93×)" are C-frame, retired-base numbers and are not evidence under D.

Evidence: The counting finding is elementary and holds in any frame: c_2 := (R−1)/u² reproduces the single scalar R by construction, so one datum fixes at most one c_k. The red-team "DOF-vs-precision" record and qou-rwhj say the same. No probe file references the bean; the 70-dps residual 0.0 follows by construction.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
