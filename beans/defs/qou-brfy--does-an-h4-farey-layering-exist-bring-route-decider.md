---
# qou-brfy
title: Does an H_4 Farey layering exist? — the one search that decides the Bring route
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T11:52:20Z
updated_at: 2026-11-17T23:08:22Z
parent: qou-v2om
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


---

## ANSWERED 2026-09-07 — and the reason is an invariant, not a failed search

The 2026-09-06 entry above recorded a scope-(a) "SEARCHED — NOT FOUND". That is
now superseded by a **structural** reason, which is stronger: the transfer fails
because its *input does not exist*, and the H_4 source says so itself.

### The obstruction

The Floyd-Hatcher / Gueritaud layering machinery consumes a **diagonal flip in a
triangulated surface** -- one flip dual to exactly one ideal tetrahedron.
Kattan-Singerman (`kattan2024`, arXiv:2402.08782v1, HELD and already cited)
state the relevant contrast as the premise of their own paper:

  "The Farey map F ... is the universal TRIANGULAR map, in that every
   triangular map on an orientable surface is a quotient of F by a subgroup of
   the modular group Gamma"

  "...Bring's surface ... comes from a regular 4-GONAL map.  We now use the
   universal 4-gonal map and the modular group is replaced by the Hecke group
   H_4."

  "Type {5,4} means that all faces are quadrilaterals and all vertices have
   valency 5."

A quadrangulation has **no diagonal to exchange**, so the layering theorem has
no input.  This is a type mismatch, not a gap in the literature search.

### The price of manufacturing one, counted exactly

Euler on Bring's {5,4} map (p*F = 2E, q*V = 2E, V - E + F = 2 - 2g, g = 4):

  V = 24,  E = 60,  F = 30,  V - E + F = -6  (checks against genus 4)
  2E = 120 = |S_5|  (matches the paper's Thm 2.1)

Triangulating each quadrilateral face is a free binary choice per face:

  2^30 = 1,073,741,824 refinements

Selecting among ~10^9 to match a target is **selection against the target** --
fitting under the NO-FITTING directive with no continuous parameter tuned.

### Measured, not asserted

The corpus's whole warrant for "Bring is presented by H_4" is this one paper,
and grepped whole it contains ZERO occurrences of: triangulation, 3-manifold,
ideal tetrahedron, knot, link, volume.  One of "hyperbolic".  Its sections are
congruence subgroups of Hecke groups / universal q-gonal maps / Hecke-Farey
fractions / poles / equivalence classes of vertices.  A 2-dimensional
maps-and-dessins paper end to end.

### Artifacts

  computations/probes/h4_universal_map_is_4gonal_probe.py          17/17, exit 0
  folio/quantum-observable-universe/lean/QOU/Brings/HeckeMapFaceSize.lean
      6 declarations, sorry-free, #print axioms clean
  PR #6975 (draft), issue #6974

### SCOPE — (a), and deliberately NOT (b).  THE BEAN STAYS OPEN.

Established: the Floyd-Hatcher/Gueritaud route does not carry from H_3 to H_4,
for a named invariant reason (face size 4 vs 3).

NOT established, and NOT claimed:
  * that no other H_4 -> 3-manifold construction exists;
  * that Bring's surface is irrelevant to the framework (its role elsewhere is
    untouched);
  * anything about H_q for q >= 5.

Per AGENTS.md, a (b) exclusion needs a proved invariant forbidding the
INGREDIENT in ANY closure.  What is proved here forbids one specific transfer.
So this bean remains open on the residual question: is there a DIFFERENT route
from H_4 / Bring to a 3-manifold triangulation?

### Literature gap, named for whoever takes that residual question

  Rosen lambda-continued fractions (Rosen 1954, Duke)        0 docs held
  any doc mentioning a Hecke group AND continued fractions   0 docs held

That is the H_q analogue of the continued fraction of p/q -- the input
Gueritaud's layering consumes.  It is NOT needed to settle the question above,
which the face-size argument settles without it; it would be needed by any
future attempt to build an H_4 word calculus.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


---

## Round 47 Progress (`lane-e925`, 2026-11-16 — PR #8154)

- **PR:** [litlfred/qou#8154](https://github.com/litlfred/qou/pull/8154) (`ffb527fcd5e3aac0c7b00570fecb3e6dded50749`), signed `ready: ffb527fcd5e3aac0c7b00570fecb3e6dded50749` ([comment](https://github.com/litlfred/qou/pull/8154#issuecomment-6925680171)).
- **New sorry-free Lean 4 formalisation in `folio/quantum-observable-universe/lean/QOU/Hecke/LevelLocalPathSumSupport.lean`:**
  - Proves `bring_quadrangulation_invariants` ($V = 24, E = 60, F = 30, 5V = 2E = 4F = 120, V - E + F = -6 = 2 - 2g$ for $g = 4$) and `bring_diagonal_refinement_triangulation_invariants` (splitting each of the $F = 30$ quadrangular faces by a diagonal yields $2^{30} = 1{,}073{,}741{,}824$ triangulations with $V' = 24, E' = 90, F' = 60, 3F' = 2E' = 180$, and Euler characteristic $V' - E' + F' = -6$, whereas no uniform vertex degree $d \in \mathbb{N}$ satisfies $24d = 180$ since $180 \bmod 24 = 12 \ne 0$).
- **Verified in `computations/probes/low_isotope_binding_substrate_probe.py` (`low-isotope-binding-substrate-probe.witness.json`):** assertion `qou_brfy_bring_quadrangulation_and_triangulation_invariants` PASSES.



## 2026-11-17 sibling sweep
Universal-triangulation thread, part B2 (the Farey layering search itself) left undone. Part B1 is its own task under qou-gwte.
Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.
