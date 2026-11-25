---
# qou-wv2b
title: 'Global non-abelian (Yekutieli) Stokes theorem on the Bring {5,4} map: spanning tree + face order in Lean'
status: todo
type: task
created_at: 2026-11-25T16:40:47Z
updated_at: 2026-11-25T16:40:47Z
parent: qou-i6e2
---

Owner 2026-11-25: 'bean up'. Statement: for a G-valued edge connection on the Bring {5,4} map (V,E,F=30,60,24, genus 4), the ordered product of the 24 face holonomies, each conjugated to a basepoint along a spanning tree (Yekutieli kites), equals the product of commutators [a1,b1]...[a4,b4] of the 8 generator holonomies (surface-group relation). Abelian specialisation: DEC.Complex2.total_circulation_zero (PR #9434).

Needs, none of which is in the corpus yet:
1. Bring map in Lean as explicit data: 60 edges with endpoints, 24 face boundary words (reuse BringRegularMap.lean from #9430: darts = S5, y order 4, t order 2, ty order 5).
2. A spanning tree of the 1-skeleton (29 edges) and a face ordering such that peeling faces one at a time keeps a disc (shelling).
3. The cut-open polygon: boundary word of the 4g = 16-gon and its identification pattern a1 b1 a1^-1 b1^-1 ...
4. Yekutieli kite composition: use MathlibExt/YekutieliIntegration (holonomy_append, stripHolonomy_telescope, segmentBoundary_glue) plus conjugation lemmas.

Base: QOU/FluidDynamics/DECYekutieliStokes.lean (faceHolonomy, faceHolonomy_eq_vort). Sibling's non-abelian side: QOU/BringsSurface/NonabelianStokesTrace.lean (#9428). Coordinate with #9428/#9430 before starting.
Done when: sorry-free Lean of the surface relation on Bring for arbitrary Group G, plus its abelian specialisation to total_circulation_zero. Generic G (§7c), lean-direct -DautoImplicit=false.
