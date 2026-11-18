---
# qou-k34v
title: 'GAP: Frobenius manifolds (Dubrovin) are the literature for the metric-from-pairing step and are uncited'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T19:08:39Z
updated_at: 2026-10-04T15:20:02Z
parent: qou-ddmn
---

MEASURED: 'Frobenius manifold' and 'Dubrovin' return ZERO hits across content/ (.md and .ts). That is the existing mathematical theory of precisely the object qou-dygk needs at step 2 — a manifold whose every tangent space carries a Frobenius algebra whose nondegenerate invariant pairing IS a flat metric, with the compatibility worked out. The corpus builds the Frobenius pairing correctly (FrobeniusPairingCategorical.lean) and then has nowhere to vary it, while the literature for varying it is unread. Cheapest useful next step in the whole gravity arc: read Dubrovin's lectures before writing any new Lean for step 2.
