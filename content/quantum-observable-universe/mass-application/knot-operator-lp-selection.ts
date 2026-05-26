import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-lp-selection",
  title:
    "Knot operators are selected per confinement by the Frobenius Gram-inverse LP/SDP dual basis",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.knot_operator_lp_selection",
    validation: "not_checked",
  },
  uses: [
    "prop:frobenius-gram-matrix",
    "rem:gram-matrix-spectral-connection",
    "thm:frobenius-codim-universal",
    "prop:operator-selection-lp",
    "conj:weak-spectral-completeness",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/wedderburn_pair_volumes.py",
    witness:
      "folio-assistant/computations/wedderburn-pair-volumes.witness.json",
    status: "verified",
  },
  tags: [
    "lp-dual",
    "sdp",
    "gram-inverse",
    "knot-operator",
    "operator-selection",
    "active-set",
    "confinement",
    "shadow-price",
  ],
});
