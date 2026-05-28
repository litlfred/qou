import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:six-canonical-knot-operators",
  label: "rem:garside-flow-explicit-closed-form",
  title:
    "Explicit closed-form for the Garside trajectory in coral coordinates",
  tags: [
    "garside-element",
    "reeb-flow",
    "explicit-solution",
    "coral-sectors",
    "compound-flow",
  ],
  uses: ["rem:garside-as-compound-flow"],
});
