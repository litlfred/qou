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
  authorNotes: [
    {
      kind: "status",
      body: "- **c=1 anchor** ($\\mathrm{lw}(1) = 1$): proved in\n  [`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3) (this branch).\n- **c=3 anchor** ($\\mathrm{lw}(3) = 5/2 + (3/4)h^2$): proved in\n  [`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3) (this branch).\n- **c=2 prediction** ($\\mathrm{lw}(2) = (q+1)^2/(3q)$): proved here.\n- **General $c \\geq 4$ prediction**: requires a q-deformed hook-length\n  identity in Lean; out of scope for this proposition.",
    },
  ],
});
