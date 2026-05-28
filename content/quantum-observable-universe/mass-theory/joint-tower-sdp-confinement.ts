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
    script: "folio-assistant/computations/probe_neutron_gap.py",
    witness: "folio-assistant/computations/neutron-gap-probes.witness.json",
    status: "verified",
  },
});
