---
# qou-a1hh
title: Explore the computational tower of sub-collisions (multi-strand convolution, C+O to CO)
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:48:36Z
updated_at: 2026-10-12T20:53:13Z
---

Owner 2026-10-12: explore two types of towers. Parent context: qou-jfx8 (segment collision datum, PR #7741). Prior-work grep in progress.


## 2026-10-12 — formalized (SegmentCollisionDatum.lean Parts E, F, lean-direct exit 0)
Part F chain3_trace: under the disjoint-block law, solved pieces joined by single-crossing letters compose by traces: tr(a ℓ₁ b ℓ₂ c) = μ₁μ₂ tr a tr b tr c. Part E: a window state depends only on the strands above the nearest bond it does not reach. Scale (exact integers): under convention D the trace factors through the two-row (TL) blocks, Σ dim² = Catalan(n): T/3He n=9 4862; ⁴He 2.08e5; C (n=36) 1.20e19; O (n=48) 1.31e26; CO (n=84) 2.71e47, max block 2.2e23. Direct evaluation of CO is impossible; composition by traces is O(#bonds) once pieces are solved. Open: what a depth-k window costs at a multi-strand (molecular) junction.


## 2026-10-12 — prior art
The chain law I derived (chain3_trace, conditional on DisjointBlockMultiplicative) was already MEASURED: docs/audits/2026-09-16-sdp-analysis-entangled-deviation-and-light-cone-recursion.md — tr(atom)/tr(free) = ∏(z_D + d_kind) to 1e-50 on D, T, ³He, ⁴He. chain3_trace is its derivation from the disjoint-block law (itself conditional on TowerSpan). Related: qou-tower ('There is no tower': GS reduction in H₃ leaves the same 6-dim state for every nucleus), molecular-construction/ (parabolic H_λ ↪ H_N; co-molecular-braid; co_lp_dual_binding.lean), universal-ilp-algorithm, ComputationalHorizon.lean, qou-sv7h (O(dim³) cost). No cost-per-level law exists in the corpus.


## 2026-10-12: molecular word on the corpus L_b (PR #7773, stacks on #7769)

Owner rulings, 2026-10-12: the bond operator is the corpus L_b, and each atom has 3A + 3Z strands (every electron is a trefoil in its own H₃).

**What the corpus fixes.**
- `covalent-bond-shared-trefoil`: `L_b = ∏ σ⁻¹_{g_e(p_j)} σ⁻¹_{g_e(p_i)}`. The electron is the positive trefoil σ₀σ₁σ₀.
- `molecular-crossing-table` (its table-data block): pp → σ, pn/nn/ne → id, p_i e_j → σ⁻¹ (c=1, d=−h), e_i e_j → σ. The parent probe said this table was unspecified; that was wrong.
- The nuclei are `atom_braid_word_3A`.

A letter is a single generator and both blocks are contiguous. So a shared trefoil must sit between the nuclei, with σ⁻¹ on the cut below it and on the cut above it. These are two distinct cuts, and no pp C_mol letter arises.

**Lean (`SegmentCollisionDatum` Part H, sorry-free, conditional on `DisjointBlockMultiplicative`).**
- `chain_trace`: the trace of a chain of blocks joined by letters is ∏(letter Markov values) × ∏(block traces).
- `sharedElectron_trace`: the junction contributes zinv².
- `hopfLetter_trace` / `hopf_value_eq`: the literal Hopf letter σ⁻² gives 1 − h·zinv. `twoCut_sub_hopf`: the two values differ by z·zinv − 1.
- `window_two_sided(_cannot_separate)`: a window that contains the junction sees only the letters in its range.

**Measured, probe `molecular_word_corpus_lb_probe.py`, 27/27.**
- (iii) H₂ junction ratio = zinv² = 0.1629153511662028022150883. It is equal to zinv² at 1e-40 on 9- and 12-strand chains.
  - The Hopf value 1 − h·zinv is different.
  - Owner choice: the corpus says "Hopf linking" but writes two different strands, which can never be the same strand pair.
- (ii) Reading 3 is INFEASIBLE.
  - On the 9-strand H₂ composite: χ < 0 on (7,2), (6,3), (5,4).
  - On the bare junction (unit nuclei + trefoil + 2 σ⁻¹): χ < 0 on (6,3), (5,4).
  - The production proton block alone already fails on (2,1).
  - The trefoil's χ_(2,1) = 0.
- (i) Window depth. A window containing a junction letter needs k* + 1 strands. CO vs N₂:
  - facing_sorted ordering: 20 strands, C side (k* = 19); O side 23.
  - one_proton_moved ordering: 23 strands.
  - So the depth DEPENDS on the nucleon ordering, which the corpus does not fix (atomic-braid clause 1 is intractable). This is a finding, not something to tune.

**Unfixed choices, for the owner.**
1. Nucleon ordering. A proton must face the junction; sorted p..p n..n puts a neutron at the top of the lower atom, so it is inadmissible.
2. CO shared trefoils: k_b = 3 (L_b over bond order) or 6 ("three electron pairs").
3. Which atom donates the shared trefoils.
4. Where the non-shared trefoils attach. This cancels in the ratio by `chain_trace`.
5. **Blocking for CO: L_b with k_b ≥ 2 is NOT realizable** on single generators with contiguous blocks (0 of 24 / 120 layouts for k_b = 2 / 3). Options:
   - non-contiguous nuclei (pull junction protons out of the chain);
   - long crossings (conjugated generators, which do not factor);
   - stacked trefoils, where the inner trefoils cross no nucleus (not L_b);
   - one trefoil per bond.

Nothing fitted or selected.
