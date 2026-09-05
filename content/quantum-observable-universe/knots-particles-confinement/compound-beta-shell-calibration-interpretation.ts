import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:compound-beta-shell-calibration",
  label: "rem:compound-beta-shell-calibration-interpretation",
  title: "Magic-shell calibration corollaries and open implementation",
  tags: [
    "beta-decay",
    "compound-decay",
    "shell-closure",
    "calibration",
    "parameter-free",
  ],
  uses: [
    "prop:compound-beta-shell-calibration",
    "def:three-calibration-discipline",
  ],
});
