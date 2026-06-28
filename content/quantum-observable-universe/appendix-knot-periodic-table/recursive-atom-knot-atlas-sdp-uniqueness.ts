import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:recursive-atom-knot-atlas",
  label: "rem:recursive-atom-knot-atlas-sdp-uniqueness",
  title:
    "Lean SDP-uniqueness wiring for the recursive atom-knot atlas",
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
  ],
  tags: [
    "atlas",
    "sdp-uniqueness",
    "lean-infrastructure",
    "appendix",
  ],
});
