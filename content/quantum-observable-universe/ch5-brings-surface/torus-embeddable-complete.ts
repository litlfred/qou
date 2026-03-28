import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-embeddable-complete",
  title:
    "Completeness of torus knots embeddable in the Bring surface",
  tags: [
    "torus-knot",
    "embeddability",
    "genus",
    "completeness",
    "seifert-genus",
    "brings-surface",
  ],
  lean: {
    decl: "QOU.Descartes.torus_embeddable_complete",
    validation: "not_checked",
  },
  uses: ["thm:embeddability-closure"],
});
