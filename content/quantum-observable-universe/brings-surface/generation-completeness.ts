import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:generation-completeness",
  proofs: ["prf:generation-completeness"],
  title:
    "Generation completeness: all embeddable knots are reachable",
  tags: [
    "completeness",
    "skein",
    "unknotting",
    "genus",
    "generation",
    "spectral-filter",
    "embeddability",
  ],
  lean: { ref: "qou:QOU.Archimedean.generation_completeness",
    validation: "not_checked",
  },
});
