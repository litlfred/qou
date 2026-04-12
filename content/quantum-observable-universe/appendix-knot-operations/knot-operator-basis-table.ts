import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-operator-basis-table",
  title: "Knot operator action on NF basis pairs (symbolic in $q$)",
  tags: [
    "hecke",
    "knot-operator",
    "normal-form",
    "appendix",
    "pair-production",
    "frobenius-dual",
  ],
  uses: [
    "rem:particle-nf-table",
    "rem:hecke-operations",
    "prop:knot-operator-selection",
    "prop:frobenius-gram-matrix",
  ],
  interprets: "prop:knot-operator-selection",
});
