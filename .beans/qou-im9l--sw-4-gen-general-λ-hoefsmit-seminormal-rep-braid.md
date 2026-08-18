---
# qou-im9l
title: 'SW-4-gen: general-λ Hoefsmit seminormal rep + braid (Yang-Baxter/axial-distance) — the residual sorry in HoefsmitRep.lean'
status: completed
type: task
priority: normal
created_at: 2026-08-02T20:13:08Z
updated_at: 2026-08-18T21:44:16Z
parent: qou-59vq
blocked_by:
    - qou-rsbf
---

Discharge the one Ref'd sorry in HoefsmitRep.lean (hoefsmit_seminormal_rep): SYT-indexed orthonormal basis of S^λ, block-diagonal (over s_i-orbits) seminormal matrices with axialDistance rational entries (generalizing S1 from the (2,1) case), and the braid relation for arbitrary λ (Hoefsmit's Yang-Baxter identity across 3 consecutive entries). This is the hard core; the (2,1) 2×2 braid is already proved sorry-free as the template. Ref: [hoefsmit1974], [ram1997].

## Construction roadmap (2026-08-10) — research-grade, multi-session

Assessed after landing the concrete (2,1) case (SW-4) + the n=3 dim-infra.
This is Hoefsmit's thesis theorem (general seminormal form), NOT a plumbing
task. Precise construction:

1. **SYT basis of S^λ.** Reuse `QOU.SchurWeyl.dLambda` / the in-repo
   `QOU.Mathlib.StandardYoungTableau` (SW-2). Index a free ℝ-module by `SYT λ`.
2. **Axial-distance data.** `cellContent`, `axialDistance` already exist
   (HoefsmitRep.lean, SW-4, sorry-free). For a SYT `t` and generator `σ_i`,
   let `d = axialDistance` between the cells of `i`, `i+1` in `t`.
3. **Seminormal matrices.** σ_i acts block-diagonally over the `s_i`-orbits of
   `SYT λ` (orbits are size 1 — `i,i+1` in same row/col, σ_i scalar `q`/`-q⁻¹`;
   or size 2 — the 2×2 axial-distance block generalizing S1 from the (2,1) case:
   diagonal `1/[d]`-type, off-diagonal the square-root-free entries realized for (2,1)).
4. **Relations.** Quadratic + far-commutation are per-block (reuse (2,1) template).
   The **braid relation for arbitrary λ** is the hard core: the Yang–Baxter /
   axial-distance identity across three consecutive entries i,i+1,i+2 — case
   analysis on their relative SYT positions. This is the multi-session piece.
5. **Assemble** via `Hecke.lift` (as `seminormalRep21` does) → `ρ_λ`.

Then SW-5-gen (irreducibility, general λ) and the general Wedderburn iso follow.
Ref: [hoefsmit1974] (thesis), [ram1997] (axial-distance formulas), [wenzl1988].
Honest scope: research project, not a one-session grind. Concrete (2,1) template
is in HoefsmitRep.lean/Irreducibility.lean/BurnsideSpan.lean as the pattern to generalize.



## CLOSED 2026-08-18 — general-λ Hoefsmit rep PROVED sorry-free (takeover, owner-authorised)
hoefsmit_seminormal_rep_general (HoefsmitGeneral.lean): ∀ λ ⊢ N, ∃ ρ : H_{N-1}(q) →ₐ[ℝ] M_{d_λ}(ℝ), and d_λ ≥ 2 → some generator is non-scalar. #print axioms → [propext, Classical.choice, Quot.sound], NO sorryAx. HoefsmitRep.lean is now 0-sorry (the cited stub retired; it could not be discharged in place — its proof runs through SeminormalRep, which imports HoefsmitRep, so the theorem lives downstream).

What I contributed on top of the prior owner's work (they had proved genMat_quadratic/far_comm/braid + seminormalRepFin):
- SytRigidity.lean (new): syt_eq_of_cellOf_eq, cellOf_col_succ_of_row/_row_succ_of_col, cellOf_eq_of_row/_of_col, and the target exists_admissible_of_ne — '#SYT ≥ 2 ⇒ some generator moves some tableau', the non-scalarity input the owner's GAP note named as missing. Route: an immovable tableau is pinned to the single row (0,j-1) or single column (j-1,0) (using left-justification to force the start at 0); same orientation ⇒ equal, mixed ⇒ value 2 at both (0,1) and (1,0), impossible. Avoids the full SYT-connectivity theorem.
- card_shape : |shape λ| = N, and the assembly (reindex injectivity + genMat_ne_scalar).

Also wired SytRigidity/HoefsmitGeneral into QOU.lean — the general-λ files (TableauCells, SeminormalParam, SeminormalRep, Orbit3/6Braid, HeckeWedderburnData3) were NOT in the umbrella, so nothing type-checked them there (the qou-orph pattern).
