---
# qou-brfy
title: 'Does an H_4 Farey layering exist? — the one search that decides the Bring route'
status: todo
type: task
priority: high
created_at: 2026-09-06T11:52:20Z
updated_at: 2026-09-06T11:52:20Z
---

OPENED 2026-09-06 from the owner proposal: "if we fix on brings, then every
hyperbolic knot convolution gets knot complement. from there to triangulation."

WHAT IS HELD (audit 2026-09-06-universal-triangulation-ep-route-assessment §9):
  * once-punctured-torus bundles <- LR word of the monodromy (Floyd-Hatcher);
    ALREADY INTERNAL to this repo for 4_1 via the braid-monodromy probe.
  * two-bridge links S(p,q) <- LR word of the continued fraction of p/q
    (Gueritaud; FKP arxiv-0808.2716v4 §2.4). Covers 4_1 = S(5,2) AND
    5_2 = S(7,3) under ONE functor. Beaned separately as qou-yvyd.
  * Bring's surface: arxiv-2402.08782v1 (Kattan-Singerman), Bring = H/H_4(5),
    20-sided hyperbolic polygon, Hecke-Farey fractions, Farey circuits.

THE GAP, and it is the whole question. The layering machinery runs on the
MODULAR GROUP H_3 = PSL(2,Z) -- the Farey tessellation there is the
once-punctured-torus combinatorics and R, L generate it. Bring's surface is
presented by H_4, a DIFFERENT Hecke group. Nothing in the corpus or the held
library asserts an H_4 analogue of the Floyd-Hatcher / Gueritaud layering.

THE TASK: settle whether an H_4 (or general H_q) layered-triangulation theorem
exists in the literature. This is a SEARCH with a definite answer -- either it
exists and is not yet held here, or it is genuinely open. It decides whether
"fix on Bring's" reaches a TRIANGULATION at all, or only a TESSELLATION.

CAUTION carried from the same audit: a Farey/flip story on a SURFACE is
2-dimensional; Pachner 2-3 moves on a 3-manifold triangulation are not the same
moves. The two connect through BUNDLES over the surface, which is exactly what
the first row above is. Keeping that distinction is what makes the route
checkable rather than suggestive.
