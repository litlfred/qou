---
# qou-a1hh
title: Explore the computational tower of sub-collisions (multi-strand convolution, C+O to CO)
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:48:36Z
updated_at: 2026-10-12T18:53:35Z
---

Owner 2026-10-12: explore two types of towers. Parent context: qou-jfx8 (segment collision datum, PR #7741). Prior-work grep in progress.


## 2026-10-12 — formalized (SegmentCollisionDatum.lean Parts E, F, lean-direct exit 0)
Part F chain3_trace: under the disjoint-block law, solved pieces joined by single-crossing letters compose by traces: tr(a ℓ₁ b ℓ₂ c) = μ₁μ₂ tr a tr b tr c. Part E: a window state depends only on the strands above the nearest bond it does not reach. Scale (exact integers): under convention D the trace factors through the two-row (TL) blocks, Σ dim² = Catalan(n): T/3He n=9 4862; ⁴He 2.08e5; C (n=36) 1.20e19; O (n=48) 1.31e26; CO (n=84) 2.71e47, max block 2.2e23. Direct evaluation of CO is impossible; composition by traces is O(#bonds) once pieces are solved. Open: what a depth-k window costs at a multi-strand (molecular) junction.


## 2026-10-12 — prior art
The chain law I derived (chain3_trace, conditional on DisjointBlockMultiplicative) was already MEASURED: docs/audits/2026-09-16-sdp-analysis-entangled-deviation-and-light-cone-recursion.md — tr(atom)/tr(free) = ∏(z_D + d_kind) to 1e-50 on D, T, ³He, ⁴He. chain3_trace is its derivation from the disjoint-block law (itself conditional on TowerSpan). Related: qou-tower ('There is no tower': GS reduction in H₃ leaves the same 6-dim state for every nucleus), molecular-construction/ (parabolic H_λ ↪ H_N; co-molecular-braid; co_lp_dual_binding.lean), universal-ilp-algorithm, ComputationalHorizon.lean, qou-sv7h (O(dim³) cost). No cost-per-level law exists in the corpus.
