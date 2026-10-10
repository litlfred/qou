---
# qou-bvo3
title: Add disclosure — 20 bare projections that are NON-EXEMPT (live scanner defects)
status: todo
type: task
priority: normal
tags:
    - vacuity
    - issue-2472
    - reorg-2026-10-04
created_at: 2026-08-10T01:47:54Z
updated_at: 2026-10-04T15:16:15Z
parent: qou-6qbv
---

**20 declarations** that project a class field verbatim with no disclosure and no citation — and are **non-exempt**, so they count against the scanner today.

Criterion (1) — *disclosure*. The scanner's §3b carve-out is justified by the premise that these docstrings state the content is class-carried with derivation pending. For these the premise is simply absent.

Priority above the exempt siblings: these are live in `proof-no-self-assuming-projection`.

- `content/quantum-observable-universe/lean/QOU/Appendix/DeltaMaxNumericalScale.lean:9` — `delta_max_numerical_scale`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/HeckeBaerStarGeneric/hecke_baer_star_generic.lean:95` — `hecke_baer_star_generic`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtClassification.lean:124` — `diagram_card`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/UnstableAtom/decay_channel.lean:108` — `decay_channel`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/e_infinity_identifications.lean:94` — `e_infinity_identifications`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/hoefsmit_scattering_pipeline.lean:137` — `hoefsmit_scattering_pipeline`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/joint_tower_sdp_confinement.lean:107` — `joint_tower_sdp_confinement`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/knot_factor_spectral_derivation.lean:72` — `knot_factor_spectral_derivation`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/knot_factor_spectral_derivation.lean:63` — `plancherelWeight_sum_eq_one`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/knot_mass_unified.lean:93` — `knot_mass_unified`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/mass_formula_regime_switching.lean:99` — `mass_formula_regime_switching`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/schur_weyl_mass_decomposition.lean:67` — `schur_weyl_mass_decomposition`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/six_term_mass_formula_complete.lean:49` — `six_term_mass_formula_complete`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/sorting_color_energy.lean:51` — `sorting_color_energy`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/wedderburnWeightCanonical.lean:104` — `wedderburnWeightCanonical`
- `content/quantum-observable-universe/lean/QOU/BraidKnot/wigner2_coefficient.lean:124` — `wigner2_coefficient`
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/PlancherelViaRecipe.lean:10` — `plancherel_via_recipe`
- `content/quantum-observable-universe/lean/QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean:132` — `dressed_mass_split_hypotheses`
- `content/quantum-observable-universe/lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:203` — `trefoil_crossing_count_eq_three`
- `content/quantum-observable-universe/lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:193` — `trefoil_strand_count_eq_two`

Criterion: `docs/audits/2026-08-09-honest-placeholder-criterion.md`
