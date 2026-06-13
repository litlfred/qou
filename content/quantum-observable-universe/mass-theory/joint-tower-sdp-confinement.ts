import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:joint-tower-sdp-confinement",
  title:
    "Joint mass-tower confinement SDP at $q_0$ with GB-filtration + jet-order tracking",
  lean: {
    ref: "qou:QOU.BraidKnot.joint_tower_sdp_confinement",
    validation: "not_checked",
  },
  uses: ["prop:atom-knot-mass-derivation"],
  tags: [
    "sdp",
    "confinement",
    "joint-tower",
    "gb-filtration",
    "jet-order",
    "design-spec",
    "wedderburn",
    "cross-level-consistency",
  ],
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/d_from_scratch.py",
    witness: "folio-assistant/computations/d-from-scratch.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      body: "See [Table 2](#tbl:joint-tower-sdp-confinement-table2-data).\n\nThe certificate format (Wedderburn block $\\times$ filtration grade $\\times$ jet\nposition $\\to$ coefficient) is identical at every scale; only the variable\ncount grows.",
    },
  ],
});
