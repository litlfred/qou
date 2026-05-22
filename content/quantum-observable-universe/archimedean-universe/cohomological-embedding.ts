import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cohomological-embedding",
  title:
    "Cohomological embedding: torus knot representations exhaust $H^1(\\Sigma_g)$",
  tags: [
    "cohomological-embedding",
    "torus-knot",
    "representation",
    "jones-polynomial",
    "genus",
    "completeness",
    "magic-numbers",
    "shell-model",
  ],
  lean: { ref: "qou:QOU.Descartes.cohomological_embedding",
    validation: "not_checked",
  },
  uses: ["rem:fivefold-symmetry"],
  examples: ["rem:fivefold-symmetry"],
});
