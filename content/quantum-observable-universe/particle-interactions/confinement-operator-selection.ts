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
    "descartes-universe:prop:knot-operator-selection",
    "descartes-universe:prop:frobenius-gram-matrix",
    "descartes-universe:def:categorical-proton",
    "descartes-universe:def:categorical-neutron",
  ],
});
