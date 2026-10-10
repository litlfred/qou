import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-sdp",
  label: "rem:confinement-sdp-multi-operator",
  title: "Multi-operator binding from active dual support",
  uses: ["prop:confinement-sdp"],
  tags: [
    "interpretation",
    "multi-operator-binding",
    "active-support",
    "shell-closure",
    "magic-numbers",
  ],
});
