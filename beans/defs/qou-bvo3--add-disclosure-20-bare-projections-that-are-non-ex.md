---
# qou-bvo3
title: Add disclosure — 20 bare projections that are NON-EXEMPT (live scanner defects)
status: in-progress
type: task
priority: normal
tags:
    - vacuity
    - issue-2472
    - reorg-2026-10-04
created_at: 2026-08-10T01:47:54Z
updated_at: 2026-11-16T20:00:34Z
parent: qou-6qbv
---

**20 declarations** that project a class field verbatim with no disclosure and no citation — and are **non-exempt**, so they count against the scanner today.

Criterion (1) — *disclosure*. The scanner's §3b carve-out is justified by the premise that these docstrings state the content is class-carried with derivation pending. For these the premise is simply absent.

Priority above the exempt siblings: these are live in `proof-no-self-assuming-projection`.

- `folio/quantum-observable-universe/lean/QOU/Appendix/DeltaMaxNumericalScale.lean:9` — `delta_max_numerical_scale`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/HeckeBaerStarGeneric/hecke_baer_star_generic.lean:95` — `hecke_baer_star_generic`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/SpechtClassification.lean:124` — `diagram_card`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/UnstableAtom/decay_channel.lean:108` — `decay_channel`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/e_infinity_identifications.lean:94` — `e_infinity_identifications`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/hoefsmit_scattering_pipeline.lean:137` — `hoefsmit_scattering_pipeline`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/joint_tower_sdp_confinement.lean:107` — `joint_tower_sdp_confinement`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/knot_factor_spectral_derivation.lean:72` — `knot_factor_spectral_derivation`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/knot_factor_spectral_derivation.lean:63` — `plancherelWeight_sum_eq_one`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/knot_mass_unified.lean:93` — `knot_mass_unified`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/mass_formula_regime_switching.lean:99` — `mass_formula_regime_switching`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/schur_weyl_mass_decomposition.lean:67` — `schur_weyl_mass_decomposition`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/six_term_mass_formula_complete.lean:49` — `six_term_mass_formula_complete`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/sorting_color_energy.lean:51` — `sorting_color_energy`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/wedderburnWeightCanonical.lean:104` — `wedderburnWeightCanonical`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/wigner2_coefficient.lean:124` — `wigner2_coefficient`
- `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/PlancherelViaRecipe.lean:10` — `plancherel_via_recipe`
- `folio/quantum-observable-universe/lean/QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean:132` — `dressed_mass_split_hypotheses`
- `folio/quantum-observable-universe/lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:203` — `trefoil_crossing_count_eq_three`
- `folio/quantum-observable-universe/lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:193` — `trefoil_strand_count_eq_two`

Criterion: `docs/audits/2026-08-09-honest-placeholder-criterion.md`

## Round 49 Progress (`litlfred/qou#8180`, `75360a145951a3e9bdb50b79e4a7ca2a9c94a813`)

- Added explicit Criterion-(1)+(3) `"**Assumed, not derived here:**"` disclosures and proved consumer theorems (`substrate_split_factor_at_one`, `dressed_mass_down_eq_up_add_split`, `e_infinity_first_three_pages_sum`, `e_infinity_chirality_sq_eq_one`) in `folio/quantum-observable-universe/lean/QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean` and `folio/quantum-observable-universe/lean/QOU/BraidKnot/e_infinity_identifications.lean`.
- Verified `lean-self-assuming-audit.py` and `lean-self-assuming-typematch-scan.mjs` report `0` findings on both files.
