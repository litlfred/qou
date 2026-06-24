import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:force-carrier-bring-uniqueness",
  proofs: ["prf:force-carrier-bring-uniqueness"],
  title:
    "$(T_{2,9}, T_{3,5})$ is the unique pair of genus-$4$ torus knots",
  lean: {
    ref: "qou:QOU.Archimedean.force_carrier_bring_uniqueness",
    validation: "not_checked",
  },
  uses: ["prop:torus-knot-genus-four-unique"],
  tags: [
    "force-carrier",
    "torus-knot",
    "genus-4",
    "brings-surface",
    "uniqueness",
    "number-theoretic",
  ],
});
