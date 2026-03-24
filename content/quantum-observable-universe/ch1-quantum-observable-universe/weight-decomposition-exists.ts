import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:weight-decomposition-exists",
  title: "Existence of the weight decomposition",
  lean: {
    decl: "QOU.WeightDecomposition.ofMaximalTorus",
    validation: "not_checked",
  },
  uses: ["def:quantum-observable-universe", "def:maximal-torus", "def:higher-forms", "def:weight-decomposition"],
  tags: ["existence", "weight", "decomposition"],
});
