import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:confinement-tower-chamber-gs",
  renamedFrom: ["alg:gb-filtration"],
  title:
    "Five-Layer Confinement-Tower Promotion and Physical Cluster-Chamber Reduction ($\\mathcal{L}_0\\to\\mathcal{L}_4$)",
  uses: [
    "prop:nuclear-chamber-groebner-basis",
    "def:iterated-confinement-layer",
    "rem:confinement-layer-operator-selection",
  ],
  cites: [
    "buchberger2006",
    "graver1975",
    "conti-traverso1991",
    "sturmfels-thomas1997",
    "dantzig-wolfe1960",
    "mulliken1934",
    "parr-pearson1983",
  ],
  lean: {
    ref: "qou:ToricConicOpt.ConfinementLayerTower.reduced_cost_decomposition",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script:
      "computations/probes/confinement_layer_tower_chem/confinement_layer_tower_chem_probe.py",
    witness: [
      "computations/probes/confinement_layer_tower_chem/confinement-layer-tower-chem.witness.json",
      "computations/probes/lp_bootstrap_dual_gaps/chamber-gs-model-a-b.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "mba",
    "confinement-tower",
    "nuclear-chamber",
    "toric-groebner",
    "stoichiometry",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Standardizes the 5-layer `ConfinementLayer` (`L_0..L_4`) recursion combining `QOU.MathlibInfra.NuclearChamberGS` (`gPhys_strict_cost_decrease_of_chamber`, `he5_normal_form_eq_alpha_neutron`, `hoyle_triple_alpha_bottleneck`) and `QOU.MathlibInfra.ConfinementLayerTower` (`reduced_cost_decomposition`, `promoteLayer_charge_conservation`).",
    },
  ],
});
