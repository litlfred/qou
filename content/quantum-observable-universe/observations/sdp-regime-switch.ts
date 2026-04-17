import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sdp-regime-switch",
  title:
    "Discrete regime switches in SDP cross-channel couplings across isotopes",
  lean: {
    decl: "QOU.Observations.SDPRegimeSwitch",
    validation: "not_checked",
  },
  uses: [
    "prop:bw-coefficient-shadow-price",
    "prop:unified-iterative-correction",
    "prop:wigner-2-coefficient",
    "def:categorical-laplace",
  ],
  tags: [
    "sdp",
    "regime-switch",
    "cross-channel",
    "shell-closure",
    "isotope-scan",
  ],
});
