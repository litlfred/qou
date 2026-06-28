import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-interpretation",
  title:
    "Build-pipeline, Lean SDP-uniqueness wiring, and open problems for the recursive atom-knot atlas",
  interprets: "prop:recursive-atom-knot-atlas",
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
  ],
  tags: [
    "atlas",
    "build-pipeline",
    "sdp-uniqueness",
    "open-problems",
    "appendix",
  ],
});
