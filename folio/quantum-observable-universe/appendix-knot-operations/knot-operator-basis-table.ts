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
    "rem:hecke-operations",
    "prop:frobenius-gram-matrix",
  ],
  interprets: "prop:knot-operator-selection",
  authorNotes: [
    {
      kind: "note",
      body: "Symbolic NF products and Gram-matrix dual evaluations are cross-checked against `computations/knot-operator-table.witness.json` and `computations/gram-matrix-dual.witness.json` alongside `computations/photon-operator-table.witness.json`.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/photon_operator_table.py",
    witness: "computations/photon-operator-table.witness.json",
    status: "verified",
  },
});
