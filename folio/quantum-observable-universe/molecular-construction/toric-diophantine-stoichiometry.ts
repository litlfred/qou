import { theorem } from "../../schema/builders";

/**
 * Layer-4 Diophantine stoichiometry kernel, Hess's law fiber invariance,
 * toric binomial vanishing, canonical 1D primitive circuits, and exact 4D
 * Z-basis of the 3 x 7 C-H-O reaction network.
 */
export default theorem({
  label: "thm:toric-diophantine-stoichiometry",
  title:
    "Diophantine reaction kernel, Hess's law, toric binomials, and canonical stoichiometric circuits",
  lean: {
    ref: "qou:QOU.Molecular.ToricStoichiometry.ker_cho_iff_zspan",
    validation: "not_checked",
  },
  uses: [
    "def:iterated-confinement-layer",
    "thm:adiabatic-confinement-gap-stability",
  ],
  cites: [
    "deloera-hemmecke-koeppe2013",
    "sturmfels-thomas1997",
    "craciun-dickenstein-shiu-sturmfels2009",
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
    "stoichiometry",
    "diophantine-kernel",
    "toric-ideal",
    "groebner-basis",
    "hess-law",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "General ring and Diophantine theorems (`atom_conservation_iff_stoich_in_kernel`, " +
        "`hess_law_linear_and_reference_invariant`, `element_inventory_invariant_along_reactions`, " +
        "`toric_hom_vanishes_on_binomial_of_kernel`, `ker_A_H2O_iff`, `ker_A_CH4_iff`, " +
        "`ker_A_NH3_iff`, `ker_A_gluc_iff`) are proved in `QOU.MathlibInfra.ConfinementLayerTower`; " +
        "the complete 4-generator `ℤ`-basis equivalence `ker_cho_iff_zspan` and normal-form reduction " +
        "step for the `3 × 7` C–H–O network are proved in the sibling `toric-diophantine-stoichiometry.lean`.",
    },
  ],
});
