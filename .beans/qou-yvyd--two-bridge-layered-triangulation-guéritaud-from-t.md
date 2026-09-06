---
# qou-yvyd
title: 'Two-bridge layered triangulation (Guéritaud) from the Farey word of p/q: NZ data for 5₂ = S(7,3) and the cross-knot gate'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T09:52:25Z
updated_at: 2026-09-06T14:01:02Z
parent: qou-2akx
---

Follow-on to qou-n2cl. The Floyd–Hatcher chain reaches 4₁ only (once-punctured-torus bundle). 5₂ is the two-bridge knot S(7,3) (also S(7,2)); Guéritaud (Geom. Topol. 2006) and Futer–Kalfagianni–Purcell §2.4 (library arxiv-0808.2716v4) give its canonical layered triangulation from the LR word of the continued fraction of p/q. Implement the 4-punctured-sphere layering, derive NZ rows for 4₁ (= S(5,2), a second derivation to cross-check the bundle route) and 5₂, verify Vol(5₂) = 2.8281220883 and the 5₂ shape field (cubic, disc −23), then feed the 5₂ NZ data to the 3d-index / DT machinery so the chirality-split {3,4} gate can be tested on DERIVED data. Chirality matters here (S⁺ vs S⁻): the orientation convention of the layering must be pinned on a chiral case before use. Open.

2026-09-06 RESULT (probe two_bridge_layered_nz_probe.py, run in progress for the final witness): pillowcase layering (two flip tetrahedra per letter on the 4-punctured sphere = T₄/ι) with the end folds found by exhaustive search (27×27 per word) under torus-cusp / one-cusp / H₁=ℤ / geometric filters. Word length is c−3: 4₁ ← 'R' (2 tetrahedra, both shapes e^{iπ/3}, Vol = 2Cl₂(π/3), cusp modulus 2√3 i — matches the bundle route of #6935 by a different labelling: rows (1,−2|−2,1)); 5₂ ← 'RL' (4 tetrahedra, Vol = 2.8281220883307831627… to 5e-50 against the corpus value, H₁ = ℤ, shapes z0=z1≈0.66236+0.56228i, z2=z3≈−0.87744+0.74486i, cusp modulus ≈ 0.49024+2.97945i, rows (1,1,−1,−1|1,1,1,1), (0,0,−1,−1|−2,−2,−1,−1), (−1,0,1,1|1,0,0,0;−), (0,−1,1,1|0,1,0,0;−)). Fold rule observed: every fold pair identifies a FRONT-square face with a BACK-square face (never two faces of one tetrahedron), by the orientation-reversing map that fixes two punctures for 5₂ (all four pairs) and for two of the four pairs of 4₁. Other folds of the same tetrahedra give other one-cusped knot complements by volume (2.7818, 2.9441, 3.3621, 3.4030, 3.6087, 3.6639, 3.7506, 3.7588, 3.8217; and m009's 2.6667 in the unfiltered run) — the reference volume, never an input, selects. Shape-field check (cubic, disc −23) and exact ℚ(θ) verification of the rows pending in the final run. Guéritaud's fold rule is not held; this is a FOUND fold, stated as such.

2026-09-06 FINAL for this tranche (PR #6962): 14/14. 5₂ shape field θ³−θ+1 = 0 (disc −23) found by PSLQ on the real projection and re-verified on the complex root; shapes (θ,θ,θ²−1,θ²−1); every rect row reduces to 0 mod the cubic in ℚ[θ]; Lean QOU.Mass.FiveTwoGluingFromFareyWord (row_one/row_two/row_three/all_rows, standard axioms). Audit docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md. STILL OPEN: (a) orientation — 5₂ is chiral, S⁺/S⁻ unpinned; (b) the 5₂ cusp rows (μ,λ) not yet identified against an independent invariant (A-polynomial elimination as for 4₁ is the natural check); (c) Guéritaud's fold rule not held — the fold is a search result. Bean stays in-progress.
