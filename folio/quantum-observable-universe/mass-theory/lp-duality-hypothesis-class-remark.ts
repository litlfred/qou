import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lp-duality-hypothesis-class-remark",
  title: "Lean form of the finite LP duality hypothesis",
  interprets: "def:lp-duality-hypothesis-class",
  uses: [
    "def:lp-duality-hypothesis-class",
    "prop:operator-selection-lp",
  ],
});
