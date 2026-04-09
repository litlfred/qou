import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-operator-selection",
  title: "Confinement operator selection via minimum action",
  tags: [
    "confinement",
    "borromean",
    "frobenius-dual",
    "gram-matrix",
    "minimum-action",
    "operator-selection",
    "beta-decay",
  ],
  uses: [
    "prop:knot-operator-selection",
    "prop:frobenius-gram-matrix",
    "def:categorical-proton",
    "def:categorical-neutron",
  ],
});
