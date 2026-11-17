---
# qou-lrvc
title: 'SOURCE: which chirality is the Rolfsen 5₂ (and GGM''s S⁺/S⁻) in the derived (μ, λ, Im τ > 0) frame — needs a held table with its orientation convention'
status: in-progress
pr: 8245
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T09:54:34Z
updated_at: 2026-11-17T07:09:00Z
parent: qou-r9ih
---

SOURCE QUESTION (no held source; do not close until one is held and read): in the derived frame of #6985 — λ the cusp class dying in H₁(M), μ the unique complement whose filling admits no nondegenerate representation (Property P certificate), λ oriented so Im(t_λ/t_μ) > 0 for the Im z > 0 solution — the two-bridge triangulation of K(7,3) from the Farey word RL has boundary slopes {−10, −4, 0} and A-polynomial A = L³ + L²(M¹⁰−M⁸+2M⁴+2M²−1) + L(−M¹⁴+2M¹²+2M¹⁰−M⁶+M⁴) + M¹⁴ (the standard printed A_{5₂} under L ↦ 1/L). Its mirror has {0, 4, 10}. WHICH of the two is the Rolfsen-table 5₂ (equivalently: which chirality does GGM's S⁺(0)=[[1,4,0],[0,1,0],[−3,−9,1]] / S⁻(0) belong to in this frame) is a CONVENTION the library does not hold. Candidates to ingest and read: Rolfsen, Knots and Links (Appendix C table, with the diagram's crossing signs); Culler–Shalen / Cooper–Culler–Gillet–Long–Shalen 1994 (A-polynomial table, with their orientation and (μ,λ) convention); SnapPy's Manifold('5_2') orientation + boundary_slopes + A-polynomial (Culler's tables), which fixes a definite mirror; Hatcher–Oertel boundary-slope conventions. What resolves it: one source stating A_{5₂} or the slope set together with the crossing-sign / orientation convention, matched against the derived frame by the sign of the slopes.

What it changes: nothing in the Route-A verdict (both inputs are mirror-invariant — RouteANewtonPolygonDT.absSlopeEq_mirror / lProfile_mirror, PR #7032); it decides which of S⁺/S⁻ (4 vs 3) attaches to the derived triangulation, which any future chirality-graded count (qou-rtec D4, the bar-involution link) must state in a definite frame. Audit: docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md §3 and §3b. Parent qou-yvyd.

HALF SETTLED 2026-09-07 (owner: "build out needed library"). Two held sources, both reachable from the sandbox (SnapPy 3.3.2 via PyPI; Culler's census A-polynomials library/A_census.tgz), give the same answer: the derived Farey-word triangulation RL of K(7,3) is the MIRROR of the Rolfsen-table 5_2 as SnapPy digitises it (Manifold('5_2') = m015 = K3_2). Evidence: SnapPy's cusp shape is -conj(tau_derived) to 38 digits, its normal boundary slopes are {0,4,10} against the derived {0,-4,-10}, Culler's A_{K3_2} equals the derived polynomial under L -> 1/L exactly, and SnapPy's reverse_orientation() reproduces the derived frame exactly; the 4_1 control is identical. Probe fivetwo_chirality_frame_vs_snappy_probe.py (8/8). Audit §3d.

STILL OPEN (do not close): which of GGM's S+/S- attaches to which chirality — GGM state no table-relative orientation and the held resurgence papers (2012.00062, 2111.04763, 2208.14188) cover only 4_1 and 5_2 without one. Library build-out attempted: arXiv, publisher and author hosts return no route from this sandbox (only github.com, PyPI, api.github.com open); the Rolfsen book itself is not held. What would close it: GGM's or Wheeler's own statement of the 5_2 orientation used for the (96)/(97) factorisations, or a recomputation of the q->0 Stokes matrices from a triangulation with a known frame.

2026-09-07, second pass (owner uploads 7cc7e752: Dunfield math/9901120, GGM 2007.10190; both ingested). Two more held sources agree: Dunfield's revised Hatcher–Oertel table, notation following Rolfsen, gives 5_2 = K(3/7): {0,4,10} (probe assertion added, 9/9); and Garoufalidis–Zagier 2111.06645 §10 "Orientation conventions" state they use SnapPy's orientation convention for M_K with trace field and complex volume from SnapPy — so every GZ 5_2 quantity refers to SnapPy's 5_2 = the MIRROR of the derived triangulation. SnapPy's complex volume of 5_2 is 2.82812 - 3.02413 i (mirror: +3.02413 i); that sign is the one-line invariant a source must print to be pinned.

STILL OPEN: GGM's S+/S- (the (96)/(97) factorisations). None of the four held GGM texts (2007.10190, 2012.00062, 2111.04763, 2208.14188) states an orientation or prints a signed v(5_2) or an A_{5_2}(x,y) in its sectioned text; inheritance from GZ by citation is not a held statement. Closes with one printed signed complex volume or A-polynomial in a GGM text.

## 2026-11-17 — Round 53 formalization & probe witness (PR #8245, status: in-progress)

- [x] PR #8245 (`dea5885f0b662330ff1d63757512b50427bbc370`): formalized `fivetwo_boundary_slopes_mirror_equivalence` and `apoly_52_specialization_and_reciprocal_asymmetry` in `QOU/QBeta/CompositeModulusFermatAndFiveTwoChiralityFrame.lean` (`0 sorry`, `0 axiom`, `0 vacuity`), proving the mirror equivalence between derived `K(7,3)` slopes `[-10,-4,0]` and SnapPy/Dunfield `5_2` slopes `[0,4,10]` and `A_{5_2}(L,M)` reciprocal reversal.
- [ ] Awaiting Merge Manager integration and owner review (kept `in-progress` per no-unilateral-closure policy).
