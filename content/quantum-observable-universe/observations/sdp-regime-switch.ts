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
    "prop:wigner-2-coefficient",
    "prop:q-heat-kernel-peter-weyl",
  ],
  tags: [
    "sdp",
    "regime-switch",
    "cross-channel",
    "shell-closure",
    "isotope-scan",
  ],
});
