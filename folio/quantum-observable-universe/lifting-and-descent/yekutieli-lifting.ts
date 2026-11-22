import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:yekutieli-lifting",
  lean: { ref: "qou:QOU.YekutieliLifting", validation: "not_checked" },
  title: "Categorical lifting condition holds in the brane tower",
  tags: ["yekutieli", "lifting", "brane-tower"],
  examples: ["ex:yekutieli-lifting-su2"],
  uses: ["def:quantum-characteristic-classes"],
  proofs: ["prf:yekutieli-lifting"],
});
