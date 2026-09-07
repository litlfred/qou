---
# qou-6cu7
title: Cite [martelli2016] §14.1 + §15.2 at prop:hyperbolic-knot-shape-fields and the NZ-from-braid Lean (qou-n2cl / qou-yvyd) — held source for Thurston's equations and the Lagrangian NZ rows
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T13:41:29Z
updated_at: 2026-09-07T06:55:15Z
parent: qou-2akx
---

Source: triage of the 2026-09-06 uploads (docs/audits/2026-09-06-uploads-triage-eight-documents.md; ledger row library/arxiv-1610.02592v3). Citation-only task — the two-bridge layering work stays with qou-yvyd in the main session; do NOT do it here.

WHAT. Martelli, An Introduction to Geometric Topology (arXiv:1610.02592v3, 494 pp) is now held and registered as [martelli2016]. The sections that back existing corpus claims without a held textbook source:
- §14.1.3–14.1.5 + Prop 14.1.7 (pp. 429-441): Thurston's consistency (one per edge) and completeness (two per cusp) equations; a solution with Im z_i > 0 is a complete finite-volume hyperbolic structure. Backs prop:hyperbolic-knot-shape-fields (cites thurston1978, neumann-zagier1985 only) and prop:gluing-equations-do-not-detect-hyperbolicity.
- Prop 14.1.8 + Fig 14.7: the two-tetrahedron, valence-6 triangulation with all shapes e^{iπ/3} is the figure-eight complement (two regular ideal tetrahedra). Literature form of the NZ-from-braid audit §2 check (z_0 = z_1 = ω) and of QOU.Mass.FigureEightGluingFromMonodromy.figure_eight_gluing_at_sixth_root.
- §15.2: Prop 15.2.1 (#edges = #tetrahedra), Cor 15.2.8 (rk A = 2n − c), Prop 15.2.9 / 15.2.11 (the rows of the incidence matrix generate a Lagrangian subspace). The audit's 'NZ symplectic' check (edges isotropic, ω(μ,λ) = ±2) is this proposition; qou-yvyd's cross-knot gate can cite Cor 15.2.8 for the expected rank.
- Thm 13.1.3 + Cor 13.1.4: Vol(Δ) = Λ(α)+Λ(β)+Λ(γ), regular ideal tetrahedron maximal — the Λ-form behind the Vol(4_1) = 6Λ(π/3) = 2Cl_2(π/3) guard (AGENTS.md, bean qou-zdz5).

DO. (1) add 'martelli2016' to cites[] of hyperbolic-knot-shape-fields.ts and gluing-equations-do-not-detect-hyperbolicity.ts and cite §14.1 / Prop 14.1.7 in the .md where Thurston's equations are invoked; (2) add '-- Ref: [martelli2016] §14.1 (Prop 14.1.8), §15.2 (Prop 15.2.9)' to the module docstring of QOU/Mass/FigureEightGluingFromMonodromy.lean next to the existing FKP ref; (3) in docs/audits/2026-09-06-nz-gluing-data-from-braid-monodromy.md §2 attach Prop 15.2.9 to the symplectic check and Prop 14.1.8 to the sixth-root check (a dated audit — append, do not rewrite). Render-QA any touched .md.

NOT IN THIS BOOK: the Guéritaud two-bridge layered triangulation and the Floyd–Hatcher punctured-torus-bundle layering — keep citing library arxiv-0808.2716v4 (Futer–Kalfagianni–Purcell) for those. §11.4 covers only closed torus bundles (Prop 11.4.14, Anosov iff |tr A| > 2).



Claimed 2026-09-07 on branch claude/uploads-triage-chips-2026-09-07 (one PR for the three remaining citation/framing chips of the 2026-09-06 uploads triage).
