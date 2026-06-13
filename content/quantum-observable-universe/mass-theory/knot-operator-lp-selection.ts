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
    "rem:gram-matrix-spectral-connection",
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
  authorNotes: [
    {
      kind: "status",
      body: "**Open** as a fully-formalized proposition. The LP/SDP\ninfrastructure is already first-class\n([CLAUDE.md §LP/SDP duals](https://github.com/litlfred/qou/blob/main/CLAUDE.md))\nand witnesses for individual confinements are in place. To\npromote to `proposition`:\n\n1. **Discharge** the LP-feasibility $\\leftrightarrow$ confinement-realisability\n   equivalence (currently asserted as part of [`prop:operator-selection-lp`](#prop:operator-selection-lp); requires\n   a categorical-physics statement linking the Frobenius-positive\n   cone to physical confinement).\n2. **Verify** that for every authored confinement (proton,\n   neutron, deuteron, ...) the LP/SDP solver returns an active\n   set matching the existing categorical-physics identification.\n3. **Lean formalization**: encode the LP duality statement as a\n   class hypothesis with the witness data as an instance proof.",
    },
  ],
});
