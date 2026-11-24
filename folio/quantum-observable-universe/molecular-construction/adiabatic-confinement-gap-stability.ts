import { theorem } from "../../schema/builders";

/**
 * LP fiber invariance, adiabatic confinement gap stability (eta_k < 1),
 * and cross-layer deconfinement flip (eta_k > 1).
 */
export default theorem({
  label: "thm:adiabatic-confinement-gap-stability",
  title:
    "Reduced-cost fiber invariance, adiabatic gap stability, and cross-layer deconfinement flip",
  lean: {
    ref: "qou:ToricConicOpt.ConfinementLayerTower.hierarchical_confinement_of_gap_gt_perturbation",
    validation: "not_checked",
  },
  uses: ["def:iterated-confinement-layer"],
  cites: [
    "dantzig-wolfe1960",
    "bloch-horowitz1958",
    "schrieffer-wolff1966",
  ],
  computation: {
    engine: "python",
    script:
      "computations/probes/confinement_layer_tower_chem/confinement_layer_tower_chem_probe.py",
    witness: [
      "computations/probes/confinement_layer_tower_chem/confinement-layer-tower-chem.witness.json",
    ],
    status: "experimental",
  },
  tags: [
    "confinement-tower",
    "adiabatic-stability",
    "LP-duality",
    "deconfinement",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "Proved over generic `[CommRing K]` and `[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]` " +
        "(`reduced_cost_fiber_invariance`, `lp_optimality_of_complementary_slackness`, " +
        "`hierarchical_confinement_of_gap_gt_perturbation`, " +
        "`hierarchical_confinement_of_adiabatic_ratio_lt_one`, " +
        "`cross_layer_flip_of_perturbation_gt_gap`) in `QOU.MathlibInfra.ConfinementLayerTower` (bean qou-5lct).",
    },
  ],
});
