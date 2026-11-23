import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-interpretation",
  title:
    "Provenance of the recursive atom-knot atlas entries",
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
