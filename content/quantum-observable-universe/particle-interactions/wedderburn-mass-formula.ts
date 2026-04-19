import { proposition } from "../../schema/builders";

/**
 * Complete Wedderburn mass formula.
 */
export default proposition({
  label: "prop:wedderburn-mass-formula",
  lean: {
    decl: "QOU.ParticleInteractions.wedderburn_mass_formula",
    file: "QOU/ParticleInteractions.lean",
    validation: "not_checked",
  },
  title: "Three-invariant mass formula",
  uses: ["def:atomic-braid", "prop:atomic-lp-stability"],
});
