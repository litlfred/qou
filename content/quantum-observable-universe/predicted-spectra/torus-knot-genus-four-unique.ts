import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-knot-genus-four-unique",
  proofs: ["prf:torus-knot-genus-four-unique"],
  title:
    "Genus-$4$ torus knots: $\\{T_{2,9}, T_{3,5}\\}$ are the only solutions",
  lean: {
    ref: "qou:QOU.Archimedean.torus_knot_genus_four_unique",
    validation: "not_checked",
  },
  uses: ["prop:torus-knot-generators"],
  tags: [
    "torus-knot",
    "genus-4",
    "diophantine",
    "uniqueness",
    "number-theoretic",
  ],
});
