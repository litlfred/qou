import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-selection",
  proofs: ["prf:knot-operator-selection"],
  lean: { ref: "qou:QOU.Archimedean.knot_operator_selection", validation: "not_checked" },
  title: "Knot operator selection via Frobenius dual",
  uses: ["prop:rj-canonical-inner-product"],
  tags: [
    "knot-operator",
    "pair-production",
    "frobenius-dual",
    "operator-selection",
    "hecke-algebra",
    "categorical-action",
    "rigid-duality",
    "multi-channel",
  ],
});
