import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:joint-tower-sdp-confinement",
  title:
    "Joint mass-tower confinement SDP at $q_0$ with GB-filtration + jet-order tracking",
  lean: {
    ref: "qou:QOU.BraidKnot.joint_tower_sdp_confinement",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "prop:confinement-sdp",
    "prop:atom-knot-mass-derivation",
    "prop:gb-spectral-sequence",
    "prop:spectral-sequence-collapse",
    "prop:wedderburn-trace-identity",
    "prop:alpha-k-derivation-procedure",
  ],
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
});
