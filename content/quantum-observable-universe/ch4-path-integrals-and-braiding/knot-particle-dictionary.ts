import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:knot-particle-correspondence",
  label: "rem:knot-particle-dictionary",
  title: "Knot–particle dictionary",
  tags: ["knot", "particle", "dictionary", "mass"],
  uses: [
    "def:localized-knot",
    "def:hadron",
    "prop:knot-particle-correspondence",
  ],
});
