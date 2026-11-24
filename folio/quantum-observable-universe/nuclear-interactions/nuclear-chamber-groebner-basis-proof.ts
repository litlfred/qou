import { proof } from "../../schema/builders";

export default proof({
  label: "prf:nuclear-chamber-groebner-basis",
  title:
    "Facet implication over ordered groups, finite normal-form confluence, and shell hole positivity",
  of: "prop:nuclear-chamber-groebner-basis",
  lean: {
    ref: "qou:ToricConicOpt.NuclearChamberGS.gPhys_strict_cost_decrease_of_chamber",
    validation: "validated",
  },
  uses: ["prop:nuclear-chamber-groebner-basis"],
  tags: ["nuclear-binding", "toric-ideal", "groebner-fan"],
});
