---
# qou-rt0a
title: 'Route A EXECUTED — Newton polygon of A_4_1/C1 vs G3 DT spectrum {3,4} (partial; slope-reading refuted on 5_2, #connections survives)'
status: done
type: task
priority: high
tags:
    - alien-habiro
    - g3-aomega
created_at: 2026-08-11T00:35:00Z
updated_at: 2026-09-07T09:35:38Z
parent: qou-vr3q
---

Route A of docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md, run 2026-08-11 (owner "try A").
Probe: computations/probes/qbeta_g3_aomega_route_a_newton_polygon.py (audit-only, scope-(a), 4/5; the FAIL is the intended falsification).

AIRTIGHT (4_1): the DT integers {3,4} ARE Newton-polygon data of A_4_1 —
 3 = full-A L-degree = #boundary-parabolic connections {0,g,gbar};
 4 = |max boundary slope| (hull (0,1),(4,0),(8,1),(4,2), edge slopes ±4).
C1 binding carrier [m+2]_q b_{m+2}=b_{m+1}+b_m is NOT the quantum A-polynomial of 4_1 (its Newton polygon has slopes ±1/2, not ±4). Route A must use the true colored-Jones recursion Â_K, not the binding carrier — concrete scoping correction.

CROSS-KNOT GATE (anti-numerology): slope reading R2 (DT=boundary slope) REFUTED on 5_2 (max slope 10 ∉ {3,4}); L-degree reading R1 (DT=#connections) SURVIVES (4_1:3, 5_2:4, both ∈ {3,4}).

CONSEQUENCE: the internal handle is the connection count / A-poly L-degree = a (motivic) Euler-characteristic datum, NOT the slope — the decategorified shadow of Route C. Pivot to qou-rtec. Companion 4 still needs the motivic weight R1's bare count lacks.

CAVEAT: 5_2 boundary slopes {0,-4,-10} + #connections=4 are LITERATURE-recalled (SnapPy unavailable) — harden via qou-52sn before treating the 5_2 refutation as final.

CAVEAT RETIRED 2026-09-07: the 5_2 boundary data is derived in-corpus (#6985), equal to the recalled values; the cross-knot refutation of R2 and survival of R1 stand unconditionally. New structural point: both Route-A inputs (|max slope|, L-degree) are mirror-invariant (RouteANewtonPolygonDT.absSlopeEq_mirror, lProfile_mirror), so the {4 in S+, 3 in S-} split is not Newton-polygon data in any frame — the memo's Route-A falsifier is answered in the negative structurally. See qou-52sn, audit §3b.
