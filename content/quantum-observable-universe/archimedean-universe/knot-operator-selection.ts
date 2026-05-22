import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-selection",
  lean: { ref: "qou:QOU.Descartes.knot_operator_selection", validation: "not_started" },
  title: "Knot operator selection via Frobenius dual",
  uses: [
    "def:breit-wheeler-pair-production",
    "prop:rj-canonical-inner-product",
  ],
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
