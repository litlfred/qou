import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:six-canonical-knot-operators",
  label: "rem:garside-flow-explicit-closed-form",
  title:
    "Explicit closed-form for the Garside trajectory in color coordinates",
  tags: [
    "garside-element",
    "reeb-flow",
    "explicit-solution",
    "color-sectors",
    "compound-flow",
  ],
  uses: ["rem:garside-as-compound-flow"],
});
