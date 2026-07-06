import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-interpretation",
  title:
    "Build-pipeline integration for the recursive atom-knot atlas",
  interprets: "prop:recursive-atom-knot-atlas",
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
  ],
  tags: [
    "atlas",
    "build-pipeline",
    "appendix",
  ],
});
