import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-hopf-stability",
  proofs: ["prf:torus-hopf-stability"],
  title:
    "Torus knot composites on Bring's surface are stable hadrons",
  tags: [
    "stability",
    "torus-knot",
    "hadron",
    "euler-characteristic",
    "crossing-energy",
  ],
  lean: { ref: "qou:QOU.Archimedean.torus_hopf_stability",
    validation: "not_checked",
  },
});
