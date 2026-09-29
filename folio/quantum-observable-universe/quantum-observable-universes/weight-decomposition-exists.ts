import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:weight-decomposition-exists",
  examples: ["ex:weight-decomposition-su2"],
  title: "Existence of the weight decomposition",
  lean: { ref: "qou:QOU.WeightDecomposition.ofMaximalTorus",
    validation: "not_checked",
  },
  uses: ["def:weight-decomposition"],
  proofs: ["prf:weight-decomposition-exists"],
  tags: ["existence", "weight", "decomposition"],
});
