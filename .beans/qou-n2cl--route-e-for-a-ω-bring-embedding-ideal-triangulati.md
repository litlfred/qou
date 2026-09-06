---
# qou-n2cl
title: 'Route E for A_ω (Bring embedding → ideal triangulation → Neumann–Zagier data): the exact wall'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T09:01:48Z
updated_at: 2026-09-06T09:52:25Z
parent: qou-2akx
---

Owner asked 2026-09-06: "If we restrict to Bring's surface can we do more" on A_ω. Corpus answer (bean qou-arc1, audit 2026-08-11-aomega-internal-derivation-attack-options.md §3 Route E): the ONLY Bring-specific handle on A_ω is Route E — derive the Neumann–Zagier gluing data of an ideal triangulation of S³∖K from the Bring embedding of K, so the 3d-index (hence the q→0 Stokes/DT count) becomes internal by construction.

THE WALL, stated so a Bring-restricted attempt starts here:

1. A Bring embedding is a map K → X_Bring (genus-4 Riemann surface). It is surface data. An ideal triangulation is data on the cusped 3-manifold S³∖K. No dictionary surface-embedding → ideal triangulation exists in the corpus (grep 2026-09-06: docs/audits, content/, .beans — the only "Route E" hits are the UNRELATED binding-gap Route E of 2026-09-04/05). The Hecke–Farey triangulation of Bring's curve (library arxiv-2402.08782v1) triangulates the SURFACE, not the complement.
2. Restriction to Bring does not remove the cross-knot gate: both 4₁ and 5₂ embed (brings-surface/embeddability-closure-table-data.md lines 5, 7). Every scalar route is already Lean-proved insufficient by the 5₂ chirality split (Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_datum).
3. Bring's field ℚ(ζ₅) cannot act through the trace field: the Stokes constants are integers, and ℚ(ζ₃) ⊄ ℚ(ζ₅) (predicted-spectra/bring-hyperbolic-knot-bloch-decomposition.md Observation 1). The disc(ℚ(√−3)) = −3 reading is already refuted (co-occurring 4).
4. Even with the dictionary, computing I_M from NZ data "is re-importing GGM, not a categorical shortcut" (memo §0).

What Bring restriction DOES buy: the S₅-equivariance filter on which knots contribute (a selection rule on summands), not a derivation of the integer 3.

Next honest step, if anyone reopens: construct, for 4₁ specifically, the relation between its genus-1 embedding (T₂,₃ ∪_H T₂,₃)^σ in Bring and the two-tetrahedron triangulation of its complement; that is a geometry target with no corpus precedent and no library precedent (0 CoHA/DT-categorification docs held).

Not a result. A map of the wall. Stays open.

2026-09-06 ATTACKED (owner: 'Derive neumann-zagier gluing data'). computations/probes/nz_gluing_from_braid_monodromy_probe.py derives the NZ data of S³∖4₁ with no SnapPy input: (σ₁σ₂⁻¹)² → Stallings monodromy [[2,1],[1,1]] (= R·L, Δ = t²−3t+1) → Floyd–Hatcher layering (2 tetrahedra) → edge equation z0 z1 (1−z0)(1−z1) = 1 (Thurston's), μ row (−1,0|0,−1), λ row (1,−1|1,−1). Checks: exact solution ω = e^{iπ/3}; Vol = 2Cl₂(π/3) to 50 dps; cusp modulus 2√3 i (and the sister V_{−φ} = m003 gets (1+√3 i)/2 from the same word); NZ Gram ω(μ,λ) = −2, edges isotropic; |det J_NZ| = √3 (= the corpus's SnapPy-derived value); A-polynomial elimination reproduces A_{4₁} exactly. General layering validated on R²L: 3 tetrahedra, shapes exactly in ℚ(√−7), Vol 2.666744783449… (m009). Scope: fibred genus-1 knots only ⇒ 4₁ alone among hyperbolic knots; 5₂ needs the two-bridge layering (next). Stays OPEN: A_ω itself is untouched.
