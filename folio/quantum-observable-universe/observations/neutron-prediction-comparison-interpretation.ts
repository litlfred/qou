import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:neutron-prediction-comparison",
  label: "rem:neutron-prediction-comparison-interpretation",
  title: "Shell-structure reading of the neutron-prediction residuals",
  tags: [
    "stability-cubic",
    "neutron-number",
    "beta-stability",
    "shell-structure",
    "interpretation",
  ],
  uses: ["prop:neutron-prediction-comparison"],
});
