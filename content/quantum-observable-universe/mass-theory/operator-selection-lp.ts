import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:operator-selection-lp",
  proofs: ["prf:operator-selection-lp"],
  lean: { ref: "qou:QOU.ParticleInteractions.operator_selection_lp", validation: "not_checked" },
  title: "Knot operator selection as linear program with LP duality",
  tags: [
    "linear-programming",
    "operator-selection",
    "lp-duality",
    "frobenius-dual",
    "gram-matrix",
    "knot-operator",
    "motivic-shadows",
  ],
  uses: ["prop:confinement-lp"],
});
