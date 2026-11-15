import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:weight-decomposition-exists",
  title: "Existence of the weight decomposition",
  lean: {
    decl: "QOU.WeightDecomposition.ofMaximalTorus",
    validation: "not_checked",
  },
  uses: ["def:weight-decomposition"],
  proofs: ["prf:weight-decomposition-exists"],
  tags: ["existence", "weight", "decomposition"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/weight-decomposition-exists-0.svg", blockIndex: 0, hash: "b61d7cb67799" },
  ],

});
