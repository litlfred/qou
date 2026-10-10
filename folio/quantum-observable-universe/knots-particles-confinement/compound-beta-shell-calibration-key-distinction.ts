import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:compound-beta-shell-calibration",
  label: "rem:compound-beta-shell-calibration-key-distinction",
  title: "Magic-crossing Q-value measures the difference of shell operators",
  tags: [
    "beta-decay",
    "compound-decay",
    "shell-closure",
    "knot-operator-transition",
  ],
  uses: [
    "prop:compound-beta-shell-calibration",
    "prop:shell-schur-weyl-self-duality",
  ],
});
