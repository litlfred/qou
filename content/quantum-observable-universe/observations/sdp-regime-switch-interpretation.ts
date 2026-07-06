import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:sdp-regime-switch",
  label: "rem:sdp-regime-switch-interpretation",
  title: "SDP regime switches: observed sign-flips and physical interpretation",
  uses: [
    "prop:sdp-regime-switch",
    "prop:q-heat-kernel-peter-weyl",
    "prop:mass-coefficient-shadow-price",
    "def:q-heat-equation",
  ],
  tags: [
    "sdp",
    "regime-switch",
    "shell-closure",
    "isotope-scan",
    "interpretation",
  ],
});
