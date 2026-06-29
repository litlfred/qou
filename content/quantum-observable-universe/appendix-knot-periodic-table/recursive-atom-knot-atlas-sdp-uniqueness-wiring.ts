import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-sdp-uniqueness-wiring",
  title: "Lean SDP-uniqueness wiring for the atlas entries",
  interprets: "prop:recursive-atom-knot-atlas",
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
  ],
  tags: [
    "atlas",
    "sdp-uniqueness",
    "appendix",
  ],
});
