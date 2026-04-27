import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:operator-selection-lp",
  title: "Knot operator selection as linear program with LP duality",
  tags: [
    "linear-programming",
    "operator-selection",
    "lp-duality",
    "frobenius-dual",
    "gram-matrix",
    "knot-operator",
  ],
  uses: ["prop:confinement-lp"],
});
