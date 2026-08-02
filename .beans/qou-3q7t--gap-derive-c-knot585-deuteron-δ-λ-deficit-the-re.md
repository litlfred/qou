---
# qou-3q7t
title: 'GAP: derive C_knot=5.85 (deuteron Δ_λ deficit) — the real ''improve binding'' target, not the scale-ambiguous A=3 near-miss'
status: todo
type: task
priority: normal
created_at: 2026-08-01T23:41:01Z
updated_at: 2026-08-02T09:11:04Z
---

## 2026-08-02 (PR #4556) — single-factor / single-scale route REFUTED with the pinned weight

With the binding weight now pinned to the derived Wenzl y_λ (#4543), the clean cross-isotope test:
C_knot(D/T/³He/⁴He) = 5.85/4.44/3.29/9.31 → spread 2.83× → NON-UNIVERSAL.

RULED OUT (all 0-fit): (1) weight (#4543); (2) dimension — f^λ is already tightest (vs d_q 116×, none 122×); (3) any single scale — global scale leaves the spread invariant, C_knot/A and C_knot/(A-1) non-constant, log C/log A non-constant, and a deuteron-pinned 0-fit scale mispredicts T/³He/⁴He by +32/+78/−37% (≫ isospin ±8%). Parallel checks also ruled out 'simple known invariant' and showed C_knot(D) 5.85× ≈ [sgn-chirality-cancellation 2.23×, NOT scale-fixable] × [intrinsic 2.62×].

Lean (sorry-free): T,³He at the SAME H₉ need C_knot differing 35% → no level-only rescale g(n,q₀) closes both (mirror_cross_ne / no_level_only_closure). scope-(b) for that closure class.

STILL OPEN: a genuine per-knot Δ_λ magnitude derivation. SURVIVING DIRECTION: the residual lives in the per-knot χ^λ-magnitude / word content, above a chirality-cancellation floor — NOT reachable by any weight/dim/scale choice. The one non-circular opening remains the per-vertex seminormal eigenphase / q-Reeb Δθ_λ (E₀-options audit Candidate #1), which to date closes only differences, not absolute magnitude. Audit: docs/audits/2026-08-02-c-knot-nonuniversal-pinned-weight.md.

## 2026-08-02 (PR #4619) — NA-Stokes surface-term sector: tessellation-independent but archimedean-degenerate; the blocker is the fibre τ-transfer, NOT a missing discretization

Attacked the pincer (#4615 qou-prjo + #4617 qou-i4pz) claim that the whole deuteron deficit = the transverse Yekutieli surface term over the σ₁³ Seifert surface, blocked on a missing surface discretization. Findings (empirical probe + Mathlib-free Lean; nothing wired):

1. **NOT a missing discretization.** Seifert's genus-1 CW tessellation (2 disks + 3 bands, χ=−1, g=1, rankH1=2) is canonical (Lean `Sigma1CubedSeifertTessellation`, decide, exit 0), and the SnapPy octahedral triangulation already exists.
2. **Tessellation-INDEPENDENT (owner's make-or-break test): YES.** The per-cell-DOF-free surface state-sum (writhe-normalised Kauffman/Jones) is identical on TESS-A (σ₁³, 8 states) and TESS-B (R2-refined, 32 states) to 5e-51 — a topological invariant, no tunable DOF ⇒ not a fit. (`sigma1cubed-seifert-surface-term.witness.json`.)
3. **But it does NOT reproduce 5.853.** At archimedean q₀ the σ₁³ (torus-knot, Vol=0, pinched octahedron `PinchedOctahedronDegenerate.lean`) surface state-sum is degenerate (value/target = 0.136).
4. **Scalar/character channel is provably null.** The surface-ordering correction is a product of commutators; χ^λ = block trace annihilates it (`tr[A,B]=0`, confirmed 0 @ 40 dps). Unifies holonomy_perm (#4357) + torus-knot Vol=0 + mi-sw-abelianisation. scope-(b) exclusion of the "Δ_λ = surface-curvature character correction" class.
5. **Real blocker = fibre→archimedean τ-transfer** of the pinched WRT regular part (already documented, geometric-qdilog-lifted-amplitude "SHARPENED WALL"; infra beans bwse/qou-nalu/qou-d7lh) — NOT surface discretization.
6. **Structurally-distinct Δ_λ candidate named (not computed, not a fit):** eigenphase-weighted per-block charge Σ_i θ_i^λ ⟨λ,i|[a₁,b₁]|λ,i⟩ of the handle commutator — naturally mixed-sign / sum-to-zero (matches PROBE-4 chirality req that KL-positivity can't supply), distinct from the six failed ansätze. Needs the H₁-handle holonomies inside the H₆ interface braid (H₂ trefoil is abelian ⇒ degenerate) — NOT in corpus. That identification is the honest next datum. Audit: docs/audits/2026-08-02-sigma1cubed-seifert-surface-term-trace-cyclicity-prune.md.
