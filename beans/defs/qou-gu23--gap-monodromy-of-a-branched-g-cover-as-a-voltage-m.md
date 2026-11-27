---
# qou-gu23
title: 'GAP: monodromy of a branched G-cover as a voltage map (yslf step 2)'
status: todo
type: task
tags:
    - mathlib-gap
    - bring-foundations
created_at: 2026-11-27T22:05:07Z
updated_at: 2026-11-27T22:05:07Z
parent: qou-6qbv
blocking:
    - qou-yslf
---

Split out of qou-yslf on 2026-11-27 (branch claude/equivariant-triangulation-2026-11-27). Given a compact Riemann surface X with a holomorphic action of a finite group G, and a triangulation of X/G with every branch value a vertex: show X is homeomorphic to the voltage lift (MathlibExt/VoltageLift.lean, liftPerm) of that triangulation along the monodromy voltages, with face voltages trivial and voltages generating G. Needs: X minus the fibres of branch values is a regular G-covering of the complement, and its monodromy. Mathlib has IsCovering but no monodromy or classification of covers. Open. No axiom or class may stand in for it.
