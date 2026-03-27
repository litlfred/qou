import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:localized-knot",
  label: "rem:knot-particle-dictionary",
  title: "Knot–particle dictionary",
  tags: ["knot", "particle", "dictionary", "mass"],
  uses: [
    "def:localized-knot",
    "def:hadron",
  ],
});
