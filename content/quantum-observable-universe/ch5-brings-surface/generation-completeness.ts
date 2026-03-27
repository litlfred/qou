import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:generation-completeness",
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
  lean: {
    decl: "QOU.Descartes.generation_completeness",
    validation: "not_checked",
  },
  uses: [
    "prop:torus-embeddable-complete",
    "prop:torus-knot-generators",
    "thm:embeddability-closure",
    "def:knot-particle-generation",
    "rem:knot-formula-table",
  ],
});
