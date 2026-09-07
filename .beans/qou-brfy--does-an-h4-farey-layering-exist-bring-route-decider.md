---
# qou-brfy
title: Does an H_4 Farey layering exist? — the one search that decides the Bring route
status: in-progress
type: task
priority: high
created_at: 2026-09-06T11:52:20Z
updated_at: 2026-09-07T04:30:54Z
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

## SEARCHED 2026-09-06 — NOT FOUND. Scope-(a), stated precisely.

SURFACE SEARCHED:
  (i)  full held library, BOTH sections/ and ocr/ tiers, for "Hecke group":
       EXACTLY ONE hit -- arxiv-2402.08782v1, the Bring paper itself -- and it
       scores ZERO on triangulation vocabulary (ideal triangulation / layered /
       tetrahedr / 3-manifold).
  (ii) 8 held docs carry layered-triangulation vocabulary (4geo-dedi-rev,
       angled-survey, arxiv-0808.2716v4, arxiv-1303.5278v1, arxiv-1604.02688v1,
       arxiv-2601.05136v2, arxiv-2604.16077v1, topologicalinvariance3dindex).
       NONE of them mentions a Hecke group.
  (iii) one targeted web search.

RESULT: the two literatures are DISJOINT across everything searched. The
layering program (Akiyoshi, Lackenby, Gueritaud; an early special case of Agol's
veering triangulations) runs on the FAREY GRAPH OF THE MODULAR GROUP -- once-
punctured torus bundles, 4-punctured sphere bundles, two-bridge links, layered
solid tori. "Farey maps associated with Hecke groups" DO exist as a body of
theory, but nothing found carries an H_4 Farey word to a layered ideal
triangulation of a 3-MANIFOLD.

SCOPE-(a), NOT (b). This is "not found across the held library plus one targeted
search", NOT "no such theorem exists". What would separate them: a systematic
read of the Hecke-group Farey-map literature. Worth noting H_q is ARITHMETIC
only for q = 3, 4, 6 -- so H_4 being arithmetic means an analogue is not
obviously excluded on those grounds.

TWO ACQUISITION REQUESTS, neither held:
  * arXiv:2108.09349 "Geometric triangulations of a family of hyperbolic
    3-braids". DIRECTLY on triangulating BRAID CLOSURES, which is exactly
    qou-eptr question 2 (are the per-atom closures hyperbolic?). Higher value
    to this arc than the H_4 question itself.
  * arXiv:math/0406242 Gueritaud (appendix Futer), "On canonical triangulations
    of once-punctured torus bundles and two-bridge link complements" -- the
    PRIMARY source for both rows of the audit's §9 family table, currently
    cited only indirectly via FKP arxiv-0808.2716v4. Note `futer-gueritaud-
    angled` is already a references.ts key, so the author is cited but this
    paper is not held.
