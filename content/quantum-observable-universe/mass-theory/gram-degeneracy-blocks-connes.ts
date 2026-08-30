import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gram-degeneracy-blocks-connes",
  title: "A Lipschitz seminorm with nonzero kernel has no finite Connes sup",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.lip_kernel_forces_unbounded",
    validation: "not_checked",
  },
  uses: ["prop:markov-gram-star-positive"],
  tags: [
    "connes-distance",
    "spectral-triple",
    "radical",
    "convention-d",
    "trace-convention",
  ],
});
