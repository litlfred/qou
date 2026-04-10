import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:equation-of-state-uniqueness",
  title:
    "The number of independent equations of state is bounded by $\\dim HH^1(\\mathrm{Ad})$",
  lean: {
    decl: "QOU.IncompletenessHorizon.equation_of_state_uniqueness",
    validation: "not_checked",
  },
  tags: [
    "equation-of-state",
    "hochschild-cohomology",
    "deformation-theory",
    "statistical-mechanics",
    "polynomial-invariant",
    "ideal-gas-law",
    "uniqueness",
  ],
  uses: [
    "thm:qou-obstruction-reduction",
    "prop:quantum-ideal-gas-law",
    "def:classical-limit-obstruction",
  ],
  cites: ["goedel1931", "yekutieli2010"],
});
