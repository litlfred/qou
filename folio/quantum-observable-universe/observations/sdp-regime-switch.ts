import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sdp-regime-switch",
  title:
    "Discrete regime switches in SDP cross-channel couplings across isotopes",
  lean: { ref: "qou:QOU.Observations.SDPRegimeSwitch",
    validation: "not_checked",
  },
  uses: [
    "prop:unified-iterative-correction",
    "prop:q-heat-kernel-peter-weyl",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([$q$-heat kernel Peter-Weyl](#prop:q-heat-kernel-peter-weyl))" },
  ],
  tags: [
    "sdp",
    "regime-switch",
    "cross-channel",
    "shell-closure",
    "isotope-scan",
  ],
});
