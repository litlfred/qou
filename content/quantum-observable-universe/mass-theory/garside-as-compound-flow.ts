import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:six-canonical-knot-operators",
  label: "rem:garside-as-compound-flow",
  title: "Garside element as a compound Reeb flow",
  tags: [
    "garside-element",
    "reeb-flow",
    "braid-relation",
    "non-adjacent-transposition",
  ],
  uses: [
    "prop:six-canonical-knot-operators",
    "def:q-reeb-flow-on-color-coords",
  ],
});
