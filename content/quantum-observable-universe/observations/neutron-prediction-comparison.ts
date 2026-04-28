import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:neutron-prediction-comparison",
  title:
    "Comparison of predicted and observed stable neutron numbers for $p \\leq 103$",
  tags: [
    "stability-cubic",
    "neutron-number",
    "codata",
    "comparison",
    "beta-stability",
  ],
  lean: { ref: "qou:QOU.Descartes.stable_neutron_max_error",
    validation: "not_checked",
  },
  uses: ["prop:integer-stability"],
});
