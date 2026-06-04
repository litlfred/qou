import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:selection-rule-c2-prediction",
  title:
    "Per-component selection rule at c=2: $\\mathrm{lw}(2) = (q+1)^2/(3q)$",
  tags: [
    "selection-rule",
    "linking-weight",
    "wedderburn",
    "gelfand",
    "prediction",
    "hopf",
    "c2",
    "lean",
  ],
  lean: {
    ref: "qou:QOU.Mass.selection_rule_c2_eq_closed_form",
    validation: "not_checked",
  },
  uses: ["prop:selection-rule-anchors-c1-c3"],
});
