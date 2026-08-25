import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:confinement-level",
  label: "rem:ilp-solution-count-unwrap",
  title:
    "ILP solution count determines unwrap depth via confinement level",
  tags: [
    "ilp",
    "solution-count",
    "unwrap-depth",
    "confinement",
    "computational-shortcut",
  ],
  uses: ["prop:stable-atom-decidable"],
});
