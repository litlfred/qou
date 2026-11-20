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
  computation: {
    engine: "python",
    script: "computations/photon_operator_table.py",
    witness: "computations/photon-operator-table.witness.json",
    status: "verified",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Witness**: `knot-operator-table.witness.json`. (second occurrence, after the photon-photon discussion: **Witness**: `knot-operator-table.witness.json`, `gram-matrix-dual.witness.json`.)" },
  ],
});
