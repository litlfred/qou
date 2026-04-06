import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:yekutieli-lifting",
  lean: { decl: "QOU.YekutieliLifting", validation: "not_checked" },
  title: "Yekutieli Lifting Condition holds in the brane tower",
  tags: ["yekutieli", "lifting", "brane-tower"],
  examples: ["ex:yekutieli-lifting-su2"],
  uses: ["def:quantum-characteristic-classes", "def:yekutieli-lifting-condition"],
  proofs: ["prf:yekutieli-lifting"],
});
