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
  lean: {
    decl: "QOU.Descartes.cohomological_embedding",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-universe",
    "prop:skein-finiteness-bound",
    "prop:torus-knot-shell-binding",
    "prop:shell-closure-normal-form",
    "rem:fivefold-symmetry",
  ],
  examples: ["rem:fivefold-symmetry"],
});
