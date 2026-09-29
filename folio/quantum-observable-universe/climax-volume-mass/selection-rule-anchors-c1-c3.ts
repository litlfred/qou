import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:selection-rule-anchors-c1-c3",
  title:
    "Per-component selection rule $\\frac{1}{c+1}\\sum_{\\lambda\\vdash c+1} \\dim_q V_\\lambda$ at c=1, c=3",
  tags: [
    "selection-rule",
    "linking-weight",
    "wedderburn",
    "gelfand",
    "family-a",
    "lean",
  ],
  lean: {
    ref: "qou:QOU.Mass.selection_rule_c3_anchor_derived",
    validation: "validated",
  },
  uses: [],
});
