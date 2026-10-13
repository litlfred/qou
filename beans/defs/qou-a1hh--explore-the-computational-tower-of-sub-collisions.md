---
# qou-a1hh
title: Explore the computational tower of sub-collisions (multi-strand convolution, C+O to CO)
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:48:36Z
updated_at: 2026-10-12T20:29:06Z
---

Owner 2026-10-12: explore two types of towers. Parent context: qou-jfx8 (segment collision datum, PR #7741). Prior-work grep in progress.


## 2026-10-12 — formalized (SegmentCollisionDatum.lean Parts E, F, lean-direct exit 0)
Part F chain3_trace: under the disjoint-block law, solved pieces joined by single-crossing letters compose by traces: tr(a ℓ₁ b ℓ₂ c) = μ₁μ₂ tr a tr b tr c. Part E: a window state depends only on the strands above the nearest bond it does not reach. Scale (exact integers): under convention D the trace factors through the two-row (TL) blocks, Σ dim² = Catalan(n): T/3He n=9 4862; ⁴He 2.08e5; C (n=36) 1.20e19; O (n=48) 1.31e26; CO (n=84) 2.71e47, max block 2.2e23. Direct evaluation of CO is impossible; composition by traces is O(#bonds) once pieces are solved. Open: what a depth-k window costs at a multi-strand (molecular) junction.


## 2026-10-12 — prior art
The chain law I derived (chain3_trace, conditional on DisjointBlockMultiplicative) was already MEASURED: docs/audits/2026-09-16-sdp-analysis-entangled-deviation-and-light-cone-recursion.md — tr(atom)/tr(free) = ∏(z_D + d_kind) to 1e-50 on D, T, ³He, ⁴He. chain3_trace is its derivation from the disjoint-block law (itself conditional on TowerSpan). Related: qou-tower ('There is no tower': GS reduction in H₃ leaves the same 6-dim state for every nucleus), molecular-construction/ (parabolic H_λ ↪ H_N; co-molecular-braid; co_lp_dual_binding.lean), universal-ilp-algorithm, ComputationalHorizon.lean, qou-sv7h (O(dim³) cost). No cost-per-level law exists in the corpus.


## 2026-10-12 — molecular junction window (PR #7769, stacked on #7741; probe 33/33, Lean junction corollaries exit 0)
CO vs N₂ (both 28 nucleons): for windows NOT containing the junction generator, they first separate at depth k* = 19 on the carbon side (agree over 6 nucleons; gap 1.85e-50 one short, 0.921 at k*, at the bond at carbon's p|n interface) and k* = 22 on the oxygen side. Lean (junction_window_above/below, junction_cannot_separate_above): a window off the junction generator sees one atom only, whatever the junction letter. Caveats: the depth is set by the builder's sorted p…p n…n ordering (a convention, D1 note), and the corpus has NO molecular junction letter (molecular-braid.md names a 'molecular crossing table' never specified; A+Z strands with electrons vs 3A nucleus words), so junction-containing windows were not measured and none was invented.

## 2026-10-13 — bond-order gap (U5 of #7773) is an encoding artifact; owner points to the dual-space operator
Owner: "there is a knot-convoluted tensor product that acts on braids, part of dual space" (answer to: which #_β?).
- Why U5 failed: #7773 read L_b (covalent-bond-shared-trefoil) as adjacent Artin letters linking extra trefoil BLOCKS laid contiguously on one line; only one block fits between the nuclei. Scope (a): a statement about that encoding, not about bonds. Correction comment posted on #7773.
- Corpus match for the owner's operator: prop:ilp-covalent-bond (molecular-construction/ilp-covalent-bond.md): the bond is a KNOT OPERATOR K acting by x ↦ NF(x·K), chosen in the LP's DUAL space ("the dual space of the LP is the knot operator space"); K = T_{2,3}^{-1}, min crossing s.t. G·NF(x·K) ≥ 0, tr(x·K) ≤ tr(x). Acting by multiplication on existing strands, k operators need NO new strands, so the contiguity obstruction does not arise.
- Corpus CONFLICT found: covalent-bond-shared-trefoil says "Hopf linking" of shared trefoils; ilp-covalent-bond says knots not links and "the Hopf link gives repulsive or weak binding". #7773 followed the former under the 2026-10-12 ruling "corpus L_b".
- Not fixed by the corpus: which strands of A⊗B the operator K acts on; and whether order k is K^k on one site or k sites. Existing producer molecular-trefoil-scan.py uses a 2-generator crossing-list "vertex volume" model in float64 with α_em/E_mol, not a Hecke product. Its D0(H₂) 0.1% figure is not re-derived here.

## 2026-10-13 — H₂ corpus LP for ⊗_K, both electron words, γγ-restricted (probe 5/5, KnotConvolutedTensor.lean exit 0)
Owner: "try both" (electron = corpus T_w0 σ0σ1σ0, which closes to a Hopf link; vs true trefoil σ0³σ1) and γγ-restricted K (σ_sσ_{s+1}⁻¹ = unknot, its square = 4₁). 8 configurations each (atom2 pe/ep, intra-atom p–e letter on/off, junction crossing-table letter on/off).
- p–e letter ON: reading 3 fails on the H₂ state itself in all 8 (both electrons) → no K feasible. Measured, scope (a).
- p–e OFF, junction letter OFF: γγ LP selects the vertex σσ⁻¹ (unknot) for both electrons, both orientations.
- p–e OFF, junction letter ON: T_w0 electron: full LP selects σ0⁻³σ1^± (true inverse trefoil) for e|p, unknot words for e|e; γγ selects nothing for e|p and the vertex for e|e. Trefoil electron: NO K feasible at all (full and γγ) in either orientation.
- γγ never selects 4₁ (min crossing picks the length-2 vertex whenever any γγ word is feasible).
- Corpus naming: σ0σ1σ0 "trefoil" closes to a Hopf link; σ0σ1 "Hopf link" closes to the unknot. Algebra unaffected; names shifted. Not edited (owner call).

## 2026-10-13 — 🛑 RETRACTION: both H₂ ⊗_K runs (e1ef182f22, 94552dacf2) computed tr(Mᵀ K), not tr(M K)
- Bug: knot_convoluted_tensor_h2_probe.py::tr_prod indexed M[j][i]; K[i] is column i ({j: K_ji}), so it returned tr(MᵀK). The probe's cross-check used M = identity, which cannot see a transpose.
- Invalidated: EVERY x·K figure — ratios, reading 3 on x·K, trace-decrease, hence every "LP selects" / "γγ selects" / "none feasible" row in the 2026-10-13 entry above and in the PR #7741 comments 6147812696 / 6147079940-follow-ups and chat.
- NOT affected: reading 3 on the H₂ state x itself (chi_x is read off the prefix diagonal) — "p–e letter on ⇒ x fails reading 3" stands; the knot-vs-link closure checks; the Lean file.
- Fix: M[i][j], plus a cross-check with a NON-identity prefix against chi of the concatenated word (old formula misses by 1.92, new by 4.6e-41). Re-run in progress.
- Found by a locality test (owner pick "try 1"): with the correct product, the ratio of σ0⁻³σ1^± at the e|p junction is identical on 6-, 9- and 12-strand windows (0.52575295871417605185 / 0.45095163122811970554 at 40 dps), and disagreed with the witness's 0.8865 / 0.8117.
