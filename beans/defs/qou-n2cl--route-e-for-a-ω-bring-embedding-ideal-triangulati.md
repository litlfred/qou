---
# qou-n2cl
title: 'Route E for A_ω (Bring embedding → ideal triangulation → Neumann–Zagier data): the exact wall'
status: in-progress
pr: 8236
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T09:01:48Z
updated_at: 2026-11-17T06:55:00Z
parent: qou-avtq
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

## Simplicial volume — the one invariant defined on BOTH legs (2026-09-07, bean `qou-sfao`; framing and citation only)

The Bring/CS/Lawson dialog (docs/audits/2026-09-06-bring-cs-lawson-dialog-assessment.md, C2-B) dismissed the surface leg with "the Gromov norm is trivially zero on a 2-manifold". That is false, and the correct statement is worth having beside the 3-manifold one because it is the single invariant that lives on both sides of the wall above:

- **Surface leg (Bring, genus 4).** `‖Σ_g‖ = 2|χ(Σ_g)| = 4g − 4` for `g ≥ 2` (Gromov 1982, `[gromov1982]`, registered but not held), so `‖X_Bring‖ = 12`. Held positivity in Martelli `[martelli2016]`: Def 13.2.3 (`library/arxiv-1610.02592v3/sections/sec-073-132-simplicial-volume.md:44-46`), Cor 13.2.7 (:71), genus ≥ 2 positive (:76-77). The exact `2|χ|` is Gromov's, not in Martelli.
- **3-manifold leg (knot complements).** `‖S³∖K‖ = Vol(S³∖K)/v₃` with `v₃` the regular ideal tetrahedron volume — Martelli Thm 13.2.11 (`Vol = v₃‖M‖`, :158-159), Prop 13.2.13 `Vol ≤ v₃‖M‖` (:208). So `‖S³∖4₁‖ = 2` exactly (two regular ideal tetrahedra), and `‖S³∖5₂‖ = Vol(5₂)/v₃ ≈ 2.83`, not an integer.

What this buys: a common *frame* — both legs carry a Gromov norm, proportional to hyperbolic volume/area on each — which is what the dialog was looking for and then dismissed. What it does NOT buy, stated so nobody reads it otherwise: **no numerical relation between `12` and any framework quantity is proposed or admissible** — `‖X_Bring‖ = 12 = Area/π` is a topological count (`2|χ|`), and reading it against a coordination number, a kissing number, or `A = 12` would be the selection-against-target fit the NO-FITTING rule names. The wall in items 1–4 above is untouched: a Gromov norm on each side is not a dictionary between the sides.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The NZ derivation for 4₁ reproduces. A_ω is untouched, so this stays open. Item 3 should cite 9f527376 (5₂ entry 4, conditional) rather than "a co-occurring 4 in 4₁", which is GGM's 5₂ matrix.

Evidence: `nz_gluing_from_braid_monodromy_probe.py` re-run: exit 0, 5 s, every listed assertion PASS. Vol = 2.0298832128193072500424 = 2Cl₂(π/3), and the cusp shape is 2√3 i. It does not touch A_ω. Item 3's "disc reading already refuted (co-occurring 4)" rests on the eq-98 misattribution (finding 1).

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-11-17 — Round 52 formalization & probe witness (PR #8236, status: in-progress)

- [x] PR #8236 (`62b8fce5d1e824cf9dd59a1d9845d15631382086`): formalized `simplicial_vol_surface_eq_neg_two_euler`, `bring_surface_vs_fourone_simplicial_volume`, `stallings_monodromy_41_and_r2l_invariants`, `nz_symplectic_pairing_and_edge_isotropy_41`, `nz_symplectic_form_skew_symmetric`, and `qzeta3_qzeta5_discriminant_coprime` in `QOU/QBeta/BringSimplicialVolumeAndNZLayering.lean` (`0 sorry`, `0 axiom`, `0 vacuity`).
- [ ] Awaiting Merge Manager integration and owner review (kept `in-progress` per no-unilateral-closure policy).
